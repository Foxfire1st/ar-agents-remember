# mcp/src/agents_remember/mcp/tools/base.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/mcp/tools/base.py`    |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-07-08T18:45+02:00                     |
| lastVerifiedCommitHash | `8b7c1933611a13ada98dcd6fc3476c0457e136ac`                                      |
| lastVerifiedCommitDate | 2026-07-08T07:43:47+02:00|
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
`RESERVED_TOOLS`, and `_tool_payload(tool_name, payload)`. `_tool_payload`
selects the declared Pydantic model from `models.tool_registry.TOOL_RESPONSE_MODELS`, validates the
controller/core payload, serializes it with
`model_dump(mode="json", exclude_none=True)`, and stamps token-accounting
metadata onto the dumped dict via `finalize_payload_tokens` (from
`models/tokens.py`). It then calls `ambient().emit_tool(name, finalized)` (slice
2b): when a lifecycle is active the observer records one `observed`
`tool.completed` for the call, and a lifecycle-less call is dropped — so the
audit trail is complete by construction with no per-tool wiring. Task 28 then
runs the NOTIFY-AND-CONTINUE **auto-dismiss**: when the active lifecycle is parked
in `awaiting-developer` AND `tool_name != "lifecycle_turn_end_notification"`,
`_tool_payload` calls `amb.resume_from_await()` so the next AR tool call resumes
the lifecycle to `running` — the turn-end notification is a *stop*, not a stall.
The tool-name guard is load-bearing: `lifecycle_turn_end_notification` flows
through this same choke point in the very call that set `awaiting-developer`, so
without the guard the notification would self-dismiss. After that, task 27
attaches the engine-computed next move:
`next_step = next_step_for(amb, tool_name)` (top-level `from .next_step import
next_step_for`) projects the active lifecycle state to the single next step, and
`finalized["nextStep"] = next_step` is set only when non-`None`. So this one
choke point now carries the slice-2b emission hook, the task-28
`awaiting-developer` auto-dismiss, AND the task-27 next-step
hint — every in-lifecycle response gets a `nextStep` from the projected lifecycle
state with no per-tool wiring, while lifecycle-less responses stay unchanged
(`next_step_for` returns `None`). `next_step_for` is exception-contained, so the
hint path never raises into a tool call. Because this is the single choke point
every public payload passes through, that one path also gives every MCP response
a real `tokens`/`tokenizer`/`tokenCountExact` rather than the model defaults.

**260707-HFX2-L2 R5** adds a third thing this one choke point surfaces on every call: after the
next-step attachment, `_tool_payload` calls `supervisor_heartbeat.supervisor_staleness_banner(amb.root,
now=datetime.now(UTC), stale_cutoff_seconds=DEFAULT_SUPERVISOR_STALE_CUTOFF_SECONDS)` (imported from
`serving.supervisor_heartbeat`; the cutoff constant from `kernel.agentic_settings`) wrapped in a bare
`try/except Exception: banner = None` — an unreadable/absent heartbeat file must never block a tool
response. When the sweep's heartbeat tick has gone stale past the cutoff, the result is attached as
`finalized["supervisorBanner"]` (a short string, e.g. `"supervisor stale 2.3m (past the 60s
cutoff)"`); a heartbeat that has never ticked (supervisor never run in this workspace) stays silent
by the helper's own design (see `supervisor_heartbeat.py`'s doc), so this choke point never needs to
special-case "never ticked" itself. This is issue #15's "the watcher must be code AND watched" —
the fail-loud surface for the supervisor's OWN liveness, reachable from any seat's next AR call
regardless of whether it happens to look at the dashboard.

### Invariants And Boundaries

- `PUBLIC_TOOLS` must match server registration in `server.py` and the public
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
  raise (containment lives in `next_step.next_step_for`).
- `nextStep` is attached only when `next_step_for` returns non-`None`, and only
  after `emit_tool` — the emission ordering is load-bearing.
- Task 28 auto-dismiss order is fixed: `emit_tool` → (if `awaiting-developer` and
  the tool is not `lifecycle_turn_end_notification`) `resume_from_await` →
  next-step attachment. The `tool_name != "lifecycle_turn_end_notification"`
  name-guard is mandatory — it is what keeps the notification from self-dismissing
  in the same call that parked the lifecycle.
- The supervisor-banner check (260707-HFX2-L2) runs last and is exception-contained by its own
  `try/except Exception` at the call site (not inside the helper) — a banner failure must never
  prevent `nextStep`/token accounting from reaching the caller. It is attached only when non-`None`,
  same pattern as `nextStep`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Response model registry resolved per tool name. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| Server registers exactly the `PUBLIC_TOOLS` names. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| Token-accounting finalizer applied to every dumped payload. | [tokens.py](agents-remember/mcp/src/agents_remember/models/tokens.py) |
| The ambient lifecycle the emission hook tags every tool call onto. | [observer/ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The next-step engine whose hint is attached after emission. | [next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py) |
| The two new public tools' payload builders. | [terminal.py](terminal.py.md) |
| The supervisor heartbeat store + the `supervisor_staleness_banner` helper this choke point calls (260707-HFX2-L2 R5). | [../../serving/supervisor_heartbeat.py](../../serving/supervisor_heartbeat.py.md) |
| The `AmbientLifecycle.root` accessor this helper call resolves the observer root through. | [../../observer/ambient.py](../../observer/ambient.py.md) |

## Update History

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
