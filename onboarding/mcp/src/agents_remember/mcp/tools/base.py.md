# mcp/src/agents_remember/mcp/tools/base.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/mcp/tools/base.py`    |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-08-01T01:10+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`|
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

Shared payload-builder primitives for the MCP tools package: the advertised
public tool-name list and the single response-validation helper that every
modeled builder uses. L11 adds `task_reopen` to `PUBLIC_TOOLS`, listed beside
`task_doc` (it is a task tool, not a worktree tool). L2 adds `spawn_agent_session`
beside `attach_terminal_session_to_leaf` (both terminal-catalog tools). L3 adds
`orchestration_nudge_manager` for rate-limited manager nudges over the inbox.

## Code Commentary

### Logic

Declares `TRANSPORT = "stdio"`, the `PUBLIC_TOOLS` tuple (advertised MCP tools:
core/context/runtime/memory/provider/worktree/baseline/carryover/benchmark tools,
the L9 `attach_terminal_session_to_leaf` hosted-chat/terminal leaf reassignment tool,
the L2 `spawn_agent_session` agent-facing dispatch tool (create + leaf-attach +
context-prime a hosted session, listed right after attach), the 260707-HFX-L8
`session_retire`/`session_rename` seat-lifecycle tools (listed right after
`spawn_agent_session`: authority-checked terminate+provenance, and post-spawn identity rename), the L3
`orchestration_nudge_manager` communication helper,
the public lifecycle signals `lifecycle_start`/`lifecycle_resume`/
`lifecycle_turn_end_notification` (task-28 NOTIFY-AND-CONTINUE turn end)/
`lifecycle_end`/`switch_lifecycle`/`lifecycle_phase`, the slice-3c `task_doc` authoring tool,
the unified `lifecycle_gate` junction, the remaining public gate tools
`gate_decide`/`gate_list`, the task-10 external-chat inbox tools
`operator_inbox_post`/`operator_inbox_poll`/`operator_inbox_consume`, and the
dashboard task-14 `lifecycle_finalize_task`),
`RESERVED_TOOLS`, `_supervisor_banner`, `_attach_lifecycle_tail`, and
`_tool_payload(tool_name, payload)`.

### 260731-EFA-L4: set on the model, then dump once

`_tool_payload` (L132-L148) is now four steps in this order:

1. `response = model.model_validate(payload)` — the declared Pydantic model from
   `models.tool_registry.TOOL_RESPONSE_MODELS`, validated but **not yet dumped**.
2. If a lifecycle is active, `_attach_lifecycle_tail(response, amb, tool_name)`
   sets the two lifecycle-wide envelope fields **on the model**.
3. `finalized = finalize_payload_tokens(response.model_dump(mode="json", exclude_none=True))`
   — one dump, then one token pass over it.
4. If a lifecycle is active, `amb.emit_tool(tool_name, finalized)` — **last**, off
   the final payload.

`_attach_lifecycle_tail(response, amb, tool_name)` (L99-L129) owns the tail:

- The task-28 NOTIFY-AND-CONTINUE **auto-dismiss** runs first — when the active
  lifecycle is parked in `awaiting-developer` AND
  `tool_name != "lifecycle_turn_end_notification"`, it calls
  `amb.resume_from_await()` so the next AR tool call resumes the lifecycle to
  `running`; the turn-end notification is a *stop*, not a stall. The tool-name
  guard is load-bearing: `lifecycle_turn_end_notification` flows through this same
  choke point in the very call that set `awaiting-developer`, so without the guard
  the notification would self-dismiss. It runs **before** `next_step_for`, which
  reads the state it just moved.
- `response.nextStep = next_step_for(amb, tool_name)` (L128) — the task-27
  engine-computed next move (top-level `from .next_step import next_step_for`).
  Since 260731-EFA-L4 `next_step_for` returns the `NextStep` **model**, not a dump
  of it.
- `response.supervisorBanner = _supervisor_banner(amb)` (L129).

Both are assigned unconditionally, `None` included: `exclude_none=True` drops a
`None`, so a lifecycle-less or live-supervisor response is byte-identical to
before. `nextStep` and `supervisorBanner` are declared fields of the envelope
(`models.base.ResponseEnvelope`), which is what makes setting them here legal.

**What this fixed.** Both fields used to be written into the *already-dumped,
already-token-counted* dict:

- `finalize_payload_tokens` ran before the injections, so the advertised token
  count under-reported by the whole `nextStep` object — roughly 69% short on every
  in-lifecycle response.
- `supervisorBanner` was declared on no model at all, so a payload carrying one
  was outside its own schema: a stale supervisor made every response fail its own
  `model_validate`.
- `emit_tool` ran before the tail was attached, so the `tokens` recorded against
  the lifecycle was the same short count the wire advertised. It now runs last,
  off `finalized`, so the recorded figure is the count the caller was actually
  served — hint included.

Because this is the single choke point every public payload passes through, that
one path gives every MCP response a real `tokens`/`tokenizer`/`tokenCountExact`
rather than the model defaults — and now a *correct* one.

`emit_tool` itself is the slice-2b hook: when a lifecycle is active the observer
records one `observed` `tool.completed` for the call, and a lifecycle-less call is
dropped — so the audit trail is complete by construction with no per-tool wiring.

**260707-HFX2-L2 R5** is the third thing this choke point surfaces on every call,
now extracted into `_supervisor_banner(amb)` (L81-L96): it calls
`supervisor_heartbeat.supervisor_staleness_banner(amb.root, now=datetime.now(UTC),
stale_cutoff_seconds=DEFAULT_SUPERVISOR_STALE_CUTOFF_SECONDS)` (imported from
`serving.supervisor_heartbeat`; the cutoff constant from `kernel.agentic_settings`)
inside its own `try/except Exception: return None` — an unreadable/absent
heartbeat file must never block a tool response. Since 260731-EFA-L4 that
containment lives **inside the helper**, not at the call site. When the sweep's
heartbeat tick has gone stale past the cutoff the result is a short string (e.g.
`"supervisor stale 2.3m (past the 60s cutoff)"`); a heartbeat that has never
ticked (supervisor never run in this workspace) stays silent by the helper's own
design (see `supervisor_heartbeat.py`'s doc), so this choke point never needs to
special-case "never ticked" itself. This is issue #15's "the watcher must be code
AND watched" — the fail-loud surface for the supervisor's OWN liveness, reachable
from any seat's next AR call regardless of whether it happens to look at the
dashboard.

### Invariants And Boundaries

- `PUBLIC_TOOLS` must match the `@server.tool()` declarations in `mcp/registration/` (260731-EFA-L2
  moved them out of `server.py`) and the public
  subset in `models/tool_registry.PUBLIC_TOOL_RESPONSE_MODELS`.
- `_tool_payload` uses `TOOL_RESPONSE_MODELS`, which also includes lower-level
  compatibility builders that are not advertised as public MCP tools.
- `_tool_payload` validates response shape only; request validation stays in
  server signatures and controllers.
- Every public payload in the sibling domain modules must pass through
  `_tool_payload` — including the `lifecycle_*` builders, which is exactly why the
  emission hook AND the next-step hint here cover every tool with no per-tool code.
- The emission hook must never raise into the tool path (containment lives in
  `AmbientLifecycle.emit_tool`); likewise the next-step attachment must never
  raise (containment lives in `next_step.next_step_for`) and neither must the
  banner (containment lives inside `_supervisor_banner`).
- **Everything the caller receives is a field of the model dumped here.** There is
  exactly one `model_dump` in this file, and it happens after the tail is set.
  Never write a key into `finalized` after the dump: a key added there is outside
  the response model (so the payload fails its own `model_validate`) and outside
  `finalize_payload_tokens` (so the advertised token count is short by whatever
  was added). That is precisely what `nextStep` and `supervisorBanner` used to do.
- **Both tail fields are assigned unconditionally, including `None`.**
  `exclude_none=True` is what drops them, so a lifecycle-less or live-supervisor
  response stays byte-identical. Do not reintroduce an `if ... is not None` guard
  around the assignment.
- **`emit_tool` runs last, off the final payload.** The `tokens` recorded against
  the lifecycle must be the count the caller was served, hint included — emitting
  before the tail is attached records the short count.
- Task 28 auto-dismiss order is fixed and lives in `_attach_lifecycle_tail`:
  (if `awaiting-developer` and the tool is not `lifecycle_turn_end_notification`)
  `resume_from_await` → `nextStep` → `supervisorBanner`. The auto-dismiss must
  stay *before* `next_step_for`, which reads the state it just moved. The
  `tool_name != "lifecycle_turn_end_notification"` name-guard is mandatory — it is
  what keeps the notification from self-dismissing in the same call that parked
  the lifecycle.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Response model registry resolved per tool name. | — | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| `ResponseEnvelope` — the `TypeAlias` (L93) union of `ResponseModel` and `FlexibleResponseEnvelope`, the two families that declare `nextStep` and `supervisorBanner`; that declaration is what lets `_attach_lifecycle_tail` set them on the model before the single dump. | `ResponseModel.nextStep` L51, `.supervisorBanner` L57; `FlexibleResponseEnvelope` L69 (`nextStep` L77, `supervisorBanner` L81); `ResponseEnvelope` L93 | [models/base.py](agents-remember/mcp/src/agents_remember/models/base.py) |
| The registration package declares exactly the `PUBLIC_TOOLS` names. | — | [registration overview](../registration/overview.md) |
| Token-accounting finalizer applied to the single dumped payload — now after the tail, so the advertised count includes it. | — | [tokens.py](agents-remember/mcp/src/agents_remember/models/tokens.py) |
| The ambient lifecycle the emission hook tags every tool call onto; `emit_tool` now runs last, off `finalized`. | `emit_tool` | [observer/ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The next-step engine, which now returns the `NextStep` model rather than a dump of it. | `next_step_for` L260-L281 | [next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py) |
| The two terminal-catalog public tools' payload builders (advertised at `PUBLIC_TOOLS` L23-L24 here). | `attach_terminal_session_to_leaf_payload` L117-L154; `spawn_agent_session_payload` L640-L765 | [terminal.py](terminal.py.md) |
| The supervisor heartbeat store + the `supervisor_staleness_banner` helper this choke point calls (260707-HFX2-L2 R5). | — | [../../serving/supervisor_heartbeat.py](../../serving/supervisor_heartbeat.py.md) |
| The `AmbientLifecycle.root` accessor this helper call resolves the observer root through. | `AmbientLifecycle.root` | [../../observer/ambient.py](../../observer/ambient.py.md) |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## Update History
- 2026-08-01T01:10+02:00 — 260731-EFA-L4 curator: the Logic section and four invariants described a
  `_tool_payload` that no longer exists — every claim about dump-then-inject was wrong. Verified
  against the diff and the current source and rewrote the section. `_tool_payload` (L132-L148) now
  validates into a model, calls the new `_attach_lifecycle_tail(response, amb, tool_name)`
  (L99-L129) to set `response.nextStep` (L128) and `response.supervisorBanner` (L129) **on the
  model**, then dumps once and finalizes tokens over that dump, then emits. The card said
  `finalized["nextStep"] = next_step` "is set only when non-`None`" and that the banner was
  attached "only when non-`None`, same pattern"; both are now unconditional assignments with
  `exclude_none=True` doing the dropping, so a lifecycle-less response stays byte-identical.
  Recorded the three defects the old order caused: `finalize_payload_tokens` ran before the
  injections (the advertised token count was short by the whole `nextStep` object — about 69% on
  every in-lifecycle response), `supervisorBanner` was declared on no model so a stale supervisor
  made the payload fail its own `model_validate`, and `emit_tool` ran before the tail so the
  `tokens` recorded against the lifecycle was that same short count. The card's ordering invariant
  ("`nextStep` … only after `emit_tool` — the emission ordering is load-bearing" and "auto-dismiss
  order is fixed: `emit_tool` → `resume_from_await` → next-step attachment") was exactly inverted
  and is replaced: the tail is now attached first and `emit_tool` runs last, off `finalized`. Also
  corrected the banner containment claim — the `try/except Exception` moved from the call site
  **into** the extracted `_supervisor_banner(amb)` helper (L81-L96). Added four invariants
  (one dump; unconditional `None`; emit last; auto-dismiss before `next_step_for`), a reference
  row for `models.base.ResponseEnvelope`, and citations on the rows that had none; the
  Repo-Internal References header was two columns and is now three.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: `base.py` itself is unchanged by this leaf, but two
  of its claims pointed at `server.py` for tool registration, which moved wholesale to
  `mcp/registration/`. Repointed the `PUBLIC_TOOLS` invariant and the reference row; nothing else
  touched.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep, R5, issue #15): `_tool_payload` now
  attaches `finalized["supervisorBanner"]` when the supervisor heartbeat has gone stale past
  `DEFAULT_SUPERVISOR_STALE_CUTOFF_SECONDS`, via `supervisor_heartbeat.supervisor_staleness_banner`
  and `amb.root`; exception-contained at the call site, silent when the supervisor has never ticked.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8: `PUBLIC_TOOLS` now advertises `session_retire` and
  `session_rename` right after `spawn_agent_session`; `_tool_payload` behavior is unchanged.
  Verification metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-04T12:31+02:00 - L3: `PUBLIC_TOOLS` now advertises
  `orchestration_nudge_manager`; `_tool_payload` behavior is unchanged.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2: `PUBLIC_TOOLS` now advertises `spawn_agent_session` (the agent-facing
  dispatch tool) right after `attach_terminal_session_to_leaf`; `_tool_payload` behavior is unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-03T00:30+02:00 — L11 advertises `task_reopen` in PUBLIC_TOOLS next to `task_doc`.
- 2026-07-02T17:04+02:00 — L9: `PUBLIC_TOOLS` now advertises
  `attach_terminal_session_to_leaf`, the agent-facing hosted chat/terminal leaf reassignment tool.
  `_tool_payload` behavior is unchanged. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): `PUBLIC_TOOLS` grew to 51 with `lifecycle_turn_end_notification`, and `_tool_payload` gained the awaiting-developer auto-dismiss — after `emit_tool`, when `amb.current.state == "awaiting-developer"` and `tool_name != "lifecycle_turn_end_notification"`, it calls `amb.resume_from_await()` so the next AR tool call resumes the parked lifecycle to `running` (notification = stop, not stall). The tool-name guard is load-bearing: the notification flows through the same choke point in the call that parked the lifecycle, so without it the notification would self-dismiss. The auto-dismiss runs between `emit_tool` and the task-27 next-step attachment. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Task 27: after `amb.emit_tool(...)`, `_tool_payload` now attaches `finalized["nextStep"] = next_step_for(amb, tool_name)` (new top-level `from .next_step import next_step_for`) when non-`None`, so the single response choke point carries both the slice-2b emission hook and an engine-computed next-step hint for every in-lifecycle tool, with no per-tool wiring. `next_step_for` is exception-contained. New collaborator `mcp/src/agents_remember/mcp/tools/next_step.py`.
- 2026-06-26T14:16+02:00 — Task 25: `PUBLIC_TOOLS` now advertises `lifecycle_gate` and no longer advertises `lifecycle_block`, `gate_create`, `gate_wait`, or `gate_response_wait`; `_tool_payload` validates against `TOOL_RESPONSE_MODELS` so retained compatibility builders still keep strict response contracts.
- 2026-06-25T07:17+02:00 — Task 19: `PUBLIC_TOOLS` grew to 52 with `gate_response_wait`; `_tool_payload` is unchanged. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: `PUBLIC_TOOLS` grew to 51 with `lifecycle_finalize_task`; `_tool_payload` is unchanged. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: `PUBLIC_TOOLS` grew to 50 with `operator_inbox_post`, `operator_inbox_poll`, and `operator_inbox_consume`; `_tool_payload` is unchanged. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: `PUBLIC_TOOLS` grew to 47 with the control-plane gate tools (`gate_create`/`gate_decide`/`gate_wait`/`gate_list`); `_tool_payload` is unchanged. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-13T22:34 — Slice 3c commit 1: `PUBLIC_TOOLS` grew to 43 with the `task_doc` authoring tool; `_tool_payload` is unchanged. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T16:41+02:00 — Slice 2b: `PUBLIC_TOOLS` grew to 42 with the six `lifecycle_*` signal tools, and `_tool_payload` now calls `ambient().emit_tool(...)` so every tool call is attributed to the active lifecycle by construction. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — Removed `direct_closeout_preview`/`direct_closeout_apply` from `PUBLIC_TOOLS` (issue #62 worktree-only closeout); tuple is now 36 names (the earlier "37" count was itself stale — the tuple held 38 before this removal).
- 2026-06-10T09:56+02:00 — Registered `worktree_sync` in `PUBLIC_TOOLS` (GitHub #54 sub-task D); tuple is now 37 names.
- 2026-06-01T20:45+02:00 — Registered `worktree_abandon` in `PUBLIC_TOOLS` so its response is validated like every other public tool.
- 2026-05-30T22:29+02:00: Documented that `_tool_payload` now finalizes token-accounting metadata via `finalize_payload_tokens` (S6 wiring), making it the single point that populates `tokens`/`tokenizer`/`tokenCountExact` on every MCP response. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-29T18:35+02:00: Created when `mcp/tools.py` was split into the `mcp/tools/` package (commit `01f503d`); holds the `_tool_payload`/`PUBLIC_TOOLS` contract previously documented in `tools.py.md`.
