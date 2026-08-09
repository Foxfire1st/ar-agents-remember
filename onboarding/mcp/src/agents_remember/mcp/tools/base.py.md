# mcp/src/agents_remember/mcp/tools/base.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/mcp/tools/base.py`    |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-08-09T06:48+02:00                     |
| lastVerifiedCommitHash | `fb0296562ceb29929a3675a1b0195700d23bc56a`|
| lastVerifiedCommitDate | 2026-08-09T20:35:49+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

Shared payload-builder primitives for the MCP tools package: the advertised
public tool-name list and the single response-validation helper that every
modeled builder uses. L11 adds `task_reopen` to `PUBLIC_TOOLS`, listed beside
`task_doc` (it is a task tool, not a worktree tool). L2 adds `spawn_agent_session`
beside `attach_terminal_session_to_leaf` (both terminal-catalog tools). L3 adds
`orchestration_nudge_manager` for rate-limited manager nudges over the inbox.
L4 adds `operator_inbox_supersede` for explicit supersession (R11).

## Code Commentary

### Logic

`_tool_payload` delegates the decoded mapping to `complete_tool_response`.
cit:([`_tool_payload`], mcp/src/agents_remember/mcp/tools/base.py:73-75)

`complete_tool_response` calls `finalize_tool_response` for validation and enrichment, and `_attach_lifecycle_tail` sets `nextStep` plus the optional supervisor banner.
cit:([`complete_tool_response`], mcp/src/agents_remember/application/tool_response.py:47-61)
cit:([`finalize_tool_response`], mcp/src/agents_remember/models/tool_response.py:15-26)
cit:([`_attach_lifecycle_tail`], mcp/src/agents_remember/application/tool_response.py:34-44)

### Invariants And Boundaries

- `PUBLIC_TOOLS` must match the public tool declarations and the public response-model registry.
- `_tool_payload` delegates response validation and lifecycle-tail shaping; request validation remains in server signatures and application entry points.
- Every public payload must pass through the shared payload entry point, with lifecycle response ownership kept in the application response layer.
- The module does not own the lifecycle tail implementation; changes to `complete_tool_response` and its helpers are documented with that application-layer source.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Response model registry resolved per tool name. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:116-179 |
| The response envelope union names the strict and flexible families, and `FlexibleResponseEnvelope` declares the shared `ok`/token/`nextStep`/`agentNotifierBanner` fields. | `ResponseEnvelope`; `FlexibleResponseEnvelope` | mcp/src/agents_remember/models/base.py:72-89; mcp/src/agents_remember/models/base.py:98-98 |
| The server registers tool families through its registrar loop. | `register_tools` | mcp/src/agents_remember/mcp/server.py:33-34 |
| The registrar tuple owns the tool-family set consumed by that loop. | `TOOL_REGISTRARS` | mcp/src/agents_remember/mcp/registration/__init__.py:35-48 |
| Token-accounting finalizer used by the completed response payload. | `finalize_payload_tokens` | mcp/src/agents_remember/models/tokens.py:232-249 |
| The ambient lifecycle records each completed tool call. | `emit_tool` | mcp/src/agents_remember/observer/ambient.py:405-424 |
| The next-step engine returns the `NextStep` model. | `next_step_for` | mcp/src/agents_remember/application/next_step.py:260-281 |
| The two terminal-catalog public tools' payload builders. | `attach_terminal_session_to_leaf_payload`; `spawn_agent_session_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:26-43; mcp/src/agents_remember/mcp/tools/terminal.py:46-63 |
| The agent-notifier heartbeat helper used for the optional banner. | `agent_notifier_staleness_banner` | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:141-157 |
| `AmbientLifecycle.root` exposes the observer-store root used by the supervisor-banner helper. | "    def root(self) -> Path:"; "def _agent_notifier_banner(amb: AmbientLifecycle)" | mcp/src/agents_remember/observer/ambient.py:157-157; mcp/src/agents_remember/application/tool_response.py:22-22 |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded `operator_inbox_supersede` joining
  `PUBLIC_TOOLS` (explicit supersession, R11); `_tool_payload` behavior unchanged. Verification
  metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-04T11:34:10+02:00 — 260731-EFA-L6 S18-B12 curator: split the base-tool ownership record across the payload entry point, response finalizer/lifecycle tail, envelope models, registrar loop/tuple, and supervisor-banner root; the scoped fixer will generate citation ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
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
