# mcp/src/agents_remember/mcp/tools

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                             |
| sourceRoute            | `mcp/src/agents_remember/mcp/tools`            |
| doc_type               | `route-local-overview`                         |
| lastUpdated            | 2026-07-04T12:31+02:00 |
| lastVerifiedCommitHash | `6b940141fc319f1d2d18b2c94fd9e9a213d43141`                                      |
| lastVerifiedCommitDate | 2026-07-04T12:52:03+02:00|
| governingOverview      | `../../../../../overview.md`                   |

## Purpose

`mcp/tools/` is the pure payload-builder registry for the Agents Remember MCP
server. It was split out of the former single `mcp/tools.py` module (commit
`01f503d`) into one submodule per tool domain, behind a facade `__init__.py`
that preserves the public import surface (L11: `task_reopen_payload` lives in the
task-domain `task_doc.py` submodule, and `PUBLIC_TOOLS` lists `task_reopen` beside
`task_doc`): every `*_payload` builder, the
`PUBLIC_TOOLS`/`RESERVED_TOOLS`/`TRANSPORT` constants, and the `_tool_payload`
re-export remain importable from `agents_remember.mcp.tools`.

## Hot Path Summary

Server registration imports advertised `*_payload` builders from
`agents_remember.mcp.tools`; each builder forwards typed MCP arguments to its
domain controller and validates the result through `base._tool_payload`. Since
task 27 that choke point also attaches the engine-computed `nextStep` hint (after
the ambient emission hook) onto every active-lifecycle response, computed by
`next_step.py`. Task 28 makes `lifecycle_turn_end_notification` the active
NOTIFY-AND-CONTINUE turn-end tool: `_tool_payload` auto-dismisses an
`awaiting-developer` lifecycle on the next call (`resume_from_await`, name-guarded
to skip the notification itself), and `next_step.py`'s active hints repoint onto
it — the `lifecycle_gate`/inbox stack stays exported but PARKED (un-hinted). Start
at `base.py` for the shared `_tool_payload`/`PUBLIC_TOOLS` contract, then the
domain submodule that owns the tool. Task 25 makes `lifecycle_gate_payload` the
public agent-facing gate junction; split gate/block/wait builders remain exported
for internal compatibility and tests but are not registered as public MCP tools. L9 adds the
`terminal.py` submodule and public `attach_terminal_session_to_leaf` builder, an agent-facing wrapper over
the dashboard terminal catalog move policy. L2 adds the public `spawn_agent_session` builder to that same
submodule — the agent-facing dispatch tool that composes the shared serving opener + an echo-confirmed
context paste to create a role-configured, leaf-attached, context-primed hosted session.
L3 adds `orchestration.py` and public `orchestration_nudge_manager`, a rate-limited manager nudge helper
that records an orchestration nudge event and enqueues a manager-addressed inbox message.

## Layout

| Module          | Owns                                                                       |
| --------------- | -------------------------------------------------------------------------- |
| `base.py`       | `TRANSPORT`, `PUBLIC_TOOLS` (52 with L9 `attach_terminal_session_to_leaf`), `RESERVED_TOOLS`, and `_tool_payload` — the choke point that, after the ambient emission hook, runs the task-28 `awaiting-developer` auto-dismiss (`amb.resume_from_await()` for every tool except `lifecycle_turn_end_notification`) and then attaches the `next_step.py`-computed `nextStep` hint to every active-lifecycle response (exception-safe; never raises into the tool path). |
| `next_step.py`  | The lifecycle next-step engine (task 27): pure `compute_next_step` maps the projected lifecycle state to one `NextStep` hint. Front half (no worktree contract yet) is a stable prose pointer back to the one-time `lifecycle_start` rundown (`FRONT_HALF_RUNDOWN`); linear half (from `worktree_start`) delegates to `worktrees/modules/guidance.lifecycle_guidance` and overlays a turn-end hint at the gate moments. Task 28 made NOTIFY-AND-CONTINUE the active turn-end model: the `decide`/`_gate_after`/rundown ACTIVE hints now point at `lifecycle_turn_end_notification` (notify + stop, no wait), and a new `awaiting-developer` branch returns a `nextTool=None` stop hint. The `blocked` branch (a raised `lifecycle_gate` → `amb.block()`) still returns the `_AWAIT_GATE` await-developer hint at `lifecycle_resume` — the PARKED gate path, valid but un-hinted. A terminal `lifecycle_end` returns the loop-back hint. Edge `next_step_for` resolves state/contract/guidance and is exception-contained. |
| `core.py`       | ping, server_info, context_packet, runtime_install, resolve_context, skills_install; `compact_runtime_install_payload`. |
| `memory.py`     | drift_check, memory_quality_check, route_index_refresh, memory_init, baseline status/adopt, carryover plan/apply; `compact_carryover_payload`. |
| `providers.py`  | provider status/diagnostics/watchers, GrepAI search/trace, CGC query tools; `compact_diagnostics_payload`, `compact_watchers_payload`. |
| `worktree.py`   | worktree start/attach/status/sync/closeout/integrate/cleanup/abandon, including `parent_task`/`leaf_id` forwarding for leaf enclosure lookup. |
| `benchmark.py`  | codex_benchmark_prepare, codex_benchmark_run.                              |
| `lifecycle.py`  | lifecycle signal builders driving the observer ambient lifecycle; `lifecycle_block_payload` is retained for lower-level compatibility. Since task 27 `lifecycle_start_payload` also emits the one-time `frontHalfRundown` (`next_step.py`'s `FRONT_HALF_RUNDOWN`). Task 28 adds `lifecycle_turn_end_notification_payload(summary)` — the NOTIFY-AND-CONTINUE turn end: drives `await_developer` → `awaiting-developer` and returns immediately (no gate, no wait), the one builder the choke-point auto-dismiss skips by name. |
| `lifecycle_finalize.py` | the terminal `lifecycle_finalize_task` builder, forwarding to the worktree finalizer and strict response model. |
| `task_doc.py`   | the `task_doc` JSON-primary task-document authoring builder (create/set_status/set_step/set_subtask/set_section/append_decision/set_field/get; master ops are set_subtask/set_section), forwarding to the `task_doc_tools` controller. |
| `gates.py`      | `lifecycle_gate_payload` (the public create+block+wait junction that blocks until a developer decision or gate-specific inbox response), public `gate_decide`/`gate_list` builders, lower-level compatibility create/wait/response-wait builders, and the non-tool `gate_decide_for_lifecycle` the serving layer calls, config-rooted over a `GateStore(observer_root(config))`; lifecycle gate creation expires older open gates, targeted decisions reject stale gate ids, and `cancel` deletes throwaway gate interactions. The gate substrate itself lives in `controlplane/` (task 6). |
| `operator_inbox.py` | the three `operator_inbox_*` durable inbox builders (post/poll/consume), config-rooted over `OperatorInboxStore(observer_root(config))`; L3 adds agent role/message/artifact metadata plus optional hosted push delivery through the serving catalog/terminal paster seams; public consume returns the entry then deletes the pending throwaway row. The inbox substrate itself lives in `controlplane/` (task 10/L3). |
| `orchestration.py` | the L3 `orchestration_nudge_manager_payload` builder: records/rate-limits manager nudges, emits `orchestration.nudge`, and queues a manager inbox message through `operator_inbox_post_payload`. |
| `terminal.py`   | the L9 `attach_terminal_session_to_leaf_payload` builder (config-rooted over the dashboard `TerminalCatalog`, delegating durable reassignment to `serving.terminal_leaf_assignment`, returning `attached` / `leaf-taken` / `unknown-session`) AND the L2 `spawn_agent_session_payload` dispatch builder — it validates the harness against detection, composes the shared `serving.terminal_opener.open_terminal_session` (create + leaf claim + env-seeded tmux ensure) then a `serving.terminal_paste.TerminalPaster` echo-confirmed context paste, records spawned-by provenance, and returns `spawned` / `leaf-taken` / `harness-unknown` / `harness-not-detected` / `bad-kind` through the strict response model. |
| `__init__.py`   | Facade re-exporting the full builder surface and `_tool_payload`.          |

Since 2.5.1 this route also owns the response token-budget layer: the verbose
tools (`runtime_install`, `provider_diagnostics`, `provider_watchers`, and
since 2.5.2 the carryover plan/apply pair) write their full result to
`temp/tool-reports/<tool>/` via `mcp/tool_reports.py` (keep-last-5 / 7-day
write-time prune, secret redaction) and return a compact outcome with an
inline `reportPath` through the per-domain `compact_*_payload` helpers.

## Invariants And Boundaries

- `PUBLIC_TOOLS` (in `base.py`) must match server registration in `server.py`
  and the public response-model subset in `models/tool_registry.py`.
- `TOOL_RESPONSE_MODELS` may include retained compatibility builders that are not
  public MCP tools; do not infer public availability from facade exports alone.
- Every public payload returned from any submodule must go through
  `base._tool_payload`, which validates response shape only (request validation
  stays in server signatures and controllers).
- Payload builders stay transport-thin; deterministic behavior belongs in
  controllers and package services. Import the domain controller that owns the
  tool's behavior — do not reintroduce a mega-facade.
- Submodules use `..` for `mcp`-package imports (`from .. import SERVER_NAME`,
  `from ..config import McpRuntimeConfig`) since they sit one level below the
  former `tools.py`.
- The facade `__init__.py` re-exports `_tool_payload` with an explicit
  `import _tool_payload as _tool_payload` so the conformance test's
  `tools._tool_payload` access keeps working.
- Compaction is wire-shape only and lives in this route, not in controllers:
  the full result is written to the tool report BEFORE any compaction mutates
  it, decision/outcome facts stay inline, and
  `test_tool_response_budgets.py` holds every compact builder under
  `INLINE_BUDGET_CHARS` with deliberately fat inputs.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| FastMCP server registration calls these payload builders. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| Public response model registry maps each tool name to a Pydantic model. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| Domain controllers own the tool behavior the builders forward to. | [controllers overview](agents-remember/mcp/src/agents_remember/controllers/overview.md) |
| Schema tests assert public tool and response model coverage. | [test_models.py](agents-remember/mcp/tests/test_models.py) |
| Conformance test validates every builder routes through `_tool_payload`. | [test_tool_response_conformance.py](agents-remember/mcp/tests/test_tool_response_conformance.py) |
| The external-chat inbox builders post, poll, and consume operator responses. | [operator_inbox.py](agents-remember/mcp/src/agents_remember/mcp/tools/operator_inbox.py) |
| The lifecycle finalizer builder exposes the terminal task finalization tool. | [lifecycle_finalize.py](agents-remember/mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py) |
| The next-step engine computes the `nextStep` hint the `_tool_payload` choke point attaches. | [next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py) |
| The linear-half hint delegates to the worktree guidance state machine. | [guidance/lifecycle_guidance](agents-remember/mcp/src/agents_remember/worktrees/modules/guidance.py) |

## Update History

- 2026-07-04T12:31+02:00 - L3 route impact: added `orchestration.py` and
  `orchestration_nudge_manager`, while `operator_inbox.py` gained role/message
  metadata and optional hosted push delivery. Verification metadata pinned until
  closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2 route impact: the `terminal.py` submodule gains the public
  `spawn_agent_session_payload` dispatch builder beside `attach_terminal_session_to_leaf_payload`;
  `base.py`'s `PUBLIC_TOOLS`, the facade, `server.py`, and `models/tool_registry.py` now
  expose/validate the agent-facing session-spawn path. It composes the shared serving opener +
  echo-confirmed paste (durable behavior stays in `serving/`; this builder stays transport-thin).
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: task_doc.py hosts task_reopen_payload; base.py advertises task_reopen next to task_doc.
- 2026-07-02T17:04+02:00 — L9 route impact: added the `terminal.py` tools submodule and public
  `attach_terminal_session_to_leaf` tool. `base.py`, the facade, `server.py`, and `models/tool_registry.py`
  now expose/validate the agent-facing hosted chat reassignment path. Verification metadata pinned until
  closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE active turn end): the route
  now documents `lifecycle_turn_end_notification` as the active turn-end tool —
  `lifecycle.py` adds `lifecycle_turn_end_notification_payload(summary)`, `base.py`
  grew `PUBLIC_TOOLS` to 51 and gained the `_tool_payload` `awaiting-developer`
  auto-dismiss (name-guarded), and `next_step.py`'s ACTIVE hints
  (`decide`/`_gate_after`/rundown) repointed off `lifecycle_gate` onto it with a new
  `awaiting-developer` `nextTool=None` stop branch. The `lifecycle_gate`/inbox stack
  stays exported but parked (un-hinted). Hot Path Summary + Layout updated.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T20:16+02:00 — Task 27 follow-up: the `next_step.py` Layout row now
  records the gate-await behavior — a `blocked` lifecycle (a raised `lifecycle_gate`
  → `amb.block()`) returns the `lifecycle_resume` await hint, carrying the chain
  through the open gate. Verification metadata pinned until closeout stamps the
  code commit.
- 2026-06-27T18:43+02:00 — Task 27: added `next_step.py` (the lifecycle next-step
  engine) to the Layout; `base._tool_payload` now attaches the engine-computed
  `nextStep` to every active-lifecycle response (after the emission hook), and
  `lifecycle.py::lifecycle_start_payload` emits a one-time `frontHalfRundown`.
  Hot Path Summary and references updated. Verification metadata pinned until
  closeout stamps the task-27 code commit.
- 2026-06-26T18:43+02:00 — Regression fix: `gates.py` row now records that
  public `lifecycle_gate_payload` waits until a developer decision or
  gate-specific inbox response, and does not wake on stale lifecycle-scoped inbox
  rows.
- 2026-06-26T17:05+02:00 — Regression fix: `gates.py` row now records
  `lifecycle_gate_payload` as the public create+block+bounded-wait junction,
  not a wait-initialization junction.
- 2026-06-26T14:16+02:00 — Task 25: route overview now identifies `lifecycle_gate_payload` as the public gate junction and classifies split gate/block/wait builders as internal compatibility exports.
- 2026-06-25T14:02+02:00 — Task 24 reopened: `gates.py` now treats omitted `lifecycle_id` as the active ambient lifecycle for gate creation, rejecting lifecycle-less creation instead of producing workspace-shaped lifecycle gates.
- 2026-06-25T13:20+02:00 — Task 23/24: gate payloads now treat cancel/response-wait cleanup as deletion of throwaway interaction rows, and `gate_response_wait` owns the default five-minute wait loop.
- 2026-06-25T07:26+02:00 — Task 19: the gate tool surface gained `gate_response_wait`; `gates.py`
  now enforces one open lifecycle gate by expiring older open gates, supports targeted decision notes,
  and waits on both durable gate state and matching operator-inbox entries. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: payload builders now expose `parent_task` and `leaf_id` on resolver/worktree entrypoints, while closeout/integration continue to use explicit leaf enclosure `series-contract.md` paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: added `lifecycle_finalize.py` to the route. `PUBLIC_TOOLS`, the facade, the server, and the response registry now include `lifecycle_finalize_task`. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: added `operator_inbox.py` to the route and grew `base.py`/facade exports with `operator_inbox_post`, `operator_inbox_poll`, and `operator_inbox_consume`. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-19T07:23 — No route impact: slice 3c R5 threads a `dry_run` flag through the `task_doc.py` payload builder (forwarding only); the `mcp/tools/` route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: `gates.py` gained a non-tool helper `gate_decide_for_lifecycle` (the dashboard write-path the serving layer calls); the registered public-tool surface is unchanged (still 47 tools, no `PUBLIC_TOOLS`/registry edit), so the payload-builder route model this overview describes holds. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: new `gates.py` domain submodule (the four `gate_*` control-plane builders) added to the Layout; `base.py`'s `PUBLIC_TOOLS` and the facade exports grew to 47. The gate substrate itself lives in `controlplane/`. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: the `task_doc.py` Layout row now lists the master ops (`set_subtask`/`set_section`); the builder gained `subtask`/`section` forwarding. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Slice 3c commit 1: new `task_doc.py` builder added to the Layout (the JSON-primary task-document authoring tool forwarding to the `task_doc_tools` controller); `base.py`'s `PUBLIC_TOOLS` and the facade exports grew to 43. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T18:45+02:00 — No route impact: slice 2c only forwards a new `on_unsaved` argument through `lifecycle.py`'s `switch_lifecycle_payload` and `worktree.py`'s `worktree_attach_payload`; the payload-builder route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-13T16:41+02:00 — Slice 2b: new `lifecycle.py` domain submodule (the six `lifecycle_*` signal builders) added to the Layout; `base.py`'s `_tool_payload` gained the ambient emission hook and `PUBLIC_TOOLS` grew to 42. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: `worktree.py` dropped the two `direct_closeout_*` payload builders (Layout row updated to the current worktree verb set, including sync/abandon); `base.py`'s `PUBLIC_TOOLS` and the facade exports shrank to 36 names.
- 2026-06-10T09:56+02:00 — No route impact: sub-task D adds `worktree_sync_payload` (plus the `PUBLIC_TOOLS`/facade registrations) following the existing one-builder-per-tool pattern; the payload-builder route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T09:30+02:00 — No route impact: `tools/worktree.py` and `tools/core.py` only forward the new `stale_base_choice` / `include_freshness` arguments to their controllers (GitHub #54); the payload-builder surface this overview describes is unchanged.
- 2026-06-10T07:40+02:00 — No route impact: `tools/worktree.py` only forwards the new `retry_provider_setup` flag to the controller (GitHub #53).
- 2026-06-10T05:30+02:00 — Route body caught up with the 2.5.1/2.5.2 response-budget layer (compact builders per domain, tool-report filing, report-before-compaction and budget-test invariants); previous closeouts had only stamped the verification header. Developer-flagged gap.
- 2026-05-30T21:33+02:00: Re-verified the route against `8927f03` after the 0.9.x run; the per-domain Layout, hot path, and invariants still match the current exports. `core.py` gained `no_cache`/`install_provider_deps` forwarding in `runtime_install_payload` (documented on the file card); the registry's public surface is unchanged.
- 2026-05-29T18:35+02:00: Split `mcp/tools.py` (831 lines) into this `mcp/tools/` package by domain (commit `01f503d`); moved the registry purpose, invariants, and references here from the retired `tools.py.md`. Import surface unchanged.
- 2026-05-28T19:52+02:00: (from `tools.py`) Updated after all public payload builders were wired through the Pydantic response model registry and controller imports were split by domain.
- 2026-05-26T23:11+02:00: (from `tools.py`) Refreshed verification metadata after source commit `5ab704a` landed typed GrepAI payload forwarding.
- 2026-05-24T02:47+02:00: (from `tools.py`) Updated after public tool expectations added `memory_quality_check`.
- 2026-05-23T13:09+02:00: (from `tools.py`) Established for the complete Phase 04 public MCP tool surface.
