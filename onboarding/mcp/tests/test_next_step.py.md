# test_next_step.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_next_step.py`              |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-27T22:00+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

Nearest route overview: [../overview.md](../overview.md) (the `mcp/` overview).

## Purpose

Pins the task-27 lifecycle next-step engine
`mcp/src/agents_remember/mcp/tools/next_step.py`: the single state→next-move
projection attached to every tool response at the `mcp.tools.base._tool_payload`
choke point. Two test classes split the pure state machine (`compute_next_step`
/ `_from_guidance`) from the exception-contained edge (`next_step_for`) plus the
`lifecycle_start` rundown. Guards the contract that an in-lifecycle response
always carries one actionable hint while a lifecycle-less response stays silent,
and that the I/O edge never raises into a tool call. Task 28 added the
NOTIFY-AND-CONTINUE assertions: every ACTIVE hint (front-half/`decide`/the
`_gate_after` overlays/the `lifecycle_start` rundown) now points at
`lifecycle_turn_end_notification`, an `awaiting-developer` lifecycle hints the
stop (`nextTool=None`), and an end-to-end test proves the choke-point auto-dismiss
(the notification does not self-dismiss; the next call resumes). The parked
`blocked`-gate await/resume tests stay intact.

## Code Commentary

### Logic

`PureEngineTests` exercises `compute_next_step(state, contract, tool_name,
guidance=…)` directly:

- **No hint** outside a lifecycle (`state=None`) and when terminal
  (`state="completed"`) → `None`.
- **`lifecycle_end`** with `state=None` returns the loop-back `NextStep` whose
  `summary` names both `lifecycle_start` and `worktree_attach`; any other
  lifecycle-less call (`ping`) stays `None`.
- **Blocked at a gate** (`state="blocked"`, asserted for both `close` and `build`
  phases, `test_blocked_at_a_gate_awaits_the_decision`): returns `_AWAIT_GATE` —
  `nextTool="lifecycle_resume"` and a summary containing "await" — never the
  post-gate operational step, proving the gate can open in any phase and is never
  jumped. The PARKED gate path — unchanged by task 28.
- **Awaiting-developer** (`state="awaiting-developer"`, phase `build`,
  `test_awaiting_developer_hints_the_stop`): the task-28 NOTIFY-AND-CONTINUE stop —
  `nextTool is None` and the summary contains "resumes automatically".
- **Front-half generic** (`contract=None`, phase `reframe-research`,
  `test_front_half_generic_points_back_to_the_rundown`): summary mentions
  "rundown", and task 28 repointed it to `nextTool="lifecycle_turn_end_notification"`
  with a `summary` in `nextArgs`.
- **`decide`** (`contract=None`, `test_decide_points_to_the_turn_end_notification`)
  → `nextTool="lifecycle_turn_end_notification"` with a `summary` in `nextArgs`
  (task 28 repointed it off the old `worktree-intent` gate).
- **Linear, no gate moment** (contract present + `guidance=_GUIDANCE`):
  delegates to `_from_guidance` → `nextOperation="continue_work"`,
  `nextTool="worktree_status"`, and no `kind` in `nextArgs`.
- **Turn-end overlay** via `_gate_after`, keyed on tool + contract sub-state —
  task 28 repointed all three off their former approval gates onto
  `lifecycle_turn_end_notification` (each asserts that `nextTool` + a `summary` in
  `nextArgs`): `worktree_closeout_preview` *while `approved_for_commit` is False*
  (`test_closeout_preview_hints_the_turn_end_until_approved`), falling back to
  guidance once approved; `worktree_integrate` (`closeout_status="completed"`,
  `integration_status="not-started"`, `test_integrate_dry_run_hints_the_turn_end`);
  `lifecycle_finalize_task` (`integration_status="completed"`, `cleanup="pending"`,
  `test_finalize_dry_run_hints_the_turn_end`).
- **`_from_guidance`** maps the guidance dict's `summary`/`nextOperation`/
  `nextTool`/`nextArgs` onto the `NextStep` shape.

`EdgeAndChokePointTests` installs a real `AmbientLifecycle` (over a tmp
`EventStore`, `heartbeat_seconds=3600`) via `install_ambient`, with cleanups for
`reset_ambient` + `amb.shutdown` + tmpdir. It drives `next_step_for(amb,
tool_name)` (returns the JSON-dumped dict, not a `NextStep`):

- **No active lifecycle** → `None`.
- **Blocked gate (live seam)**: after `amb.start()` + `amb.block(kind=…)`,
  `next_step_for(amb, "lifecycle_gate")` returns `nextTool="lifecycle_resume"` —
  the raised gate's response carries the await/resume hint, not a premature step.
- **Front half / dry-run windows** (`test_next_step_for_*`,
  `test_dry_run_window_in_decide_shows_turn_end`,
  `test_corrupt_contract_degrades_gracefully`): a `promote`d lifecycle whose
  enclosure file is missing or torn (`}{ not a contract`) degrades to the
  front-half hint — task 28 made it `nextTool="lifecycle_turn_end_notification"`
  with a `summary` in `nextArgs` (never silent, never raises).
- **Linear delegation**: a written contract (`write_contract`) + promote yields
  `nextOperation="continue_work"` (`test_next_step_for_linear_delegates_to_guidance`).
- **Choke point**: `lifecycle_start_payload()` carries
  `frontHalfRundown == FRONT_HALF_RUNDOWN` and a `nextStep` whose
  `nextTool == "lifecycle_turn_end_notification"` with a `summary` in `nextArgs`
  (`test_tool_payload_attaches_next_step_and_lifecycle_start_emits_rundown`).
- **Auto-dismiss end-to-end**
  (`test_turn_end_notification_does_not_self_dismiss_then_next_call_resumes`):
  `lifecycle_turn_end_notification_payload(...)` parks the lifecycle in
  `awaiting-developer` and its OWN response keeps `nextTool` absent + "resumes
  automatically" (the choke-point name-guard prevents self-dismiss) while the
  projected `build_attention_queue` holds exactly one `awaiting-developer` item;
  then an arbitrary next call (`ping_payload()`) auto-resumes the lifecycle to
  `running` and that attention item disappears.

### Conventions

`sys.path.insert(0, mcp/src)` before package imports (the suite idiom). `_state`
builds a `LifecycleState` (`fleeting = enclosure is None`); `_contract` builds a
fully-populated `WorktreeContract` over a tmp `Path` with keyword `overrides`
for the sub-state fields each gate case needs. `# type: ignore` annotates the
deliberately-loose `state`/`phase` literals and `**base` splat. Edge tests use a
`tempfile.TemporaryDirectory` instance plus `addCleanup`; pure tests use the
`with tempfile.TemporaryDirectory()` form.

### Invariants And Boundaries

- The pure tests must NOT touch disk for the contract sub-state cases — they pass
  a constructed `WorktreeContract`, so the gate overlay is asserted in isolation
  from contract I/O.
- The edge tests assert the no-raise contract: every degraded path
  (missing/torn contract, no lifecycle) returns a value (`None` or a hint), never
  an exception — mirroring `next_step_for`'s blanket containment.
- Assertions read the dumped dict by key (`step["nextArgs"]`) for `next_step_for`
  but attribute access (`step.nextArgs`) for `compute_next_step`.

### Todos

None.

## Docs References

| Source | Relevance |
| --- | --- |

No relevant documentation found after checking live sources.

## Repo-Internal References

The suite pins `next_step.py` and the collaborators it resolves at the edge plus
the `lifecycle_start` payload it asserts the rundown on.

| Finding | Source Path |
| --- | --- |
| The next-step engine under test. | [next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py) |
| The choke point that attaches `nextStep` to every response. | [base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| `lifecycle_start_payload` whose `frontHalfRundown` + `nextStep` are asserted. | [lifecycle.py](agents-remember/mcp/src/agents_remember/mcp/tools/lifecycle.py) |
| The ambient lifecycle installed/started/promoted by the edge tests. | [ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The projected `LifecycleState` the pure tests construct. | [lifecycle_state.py](agents-remember/mcp/src/agents_remember/observer/lifecycle_state.py) |
| The `EventStore` backing the ambient under test. | [store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| `WorktreeContract` + `write_contract`/`load_contract` used by the gate + edge cases. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The `NextStep` shape the assertions read. | [base.py](agents-remember/mcp/src/agents_remember/models/base.py) |
| The `lifecycle_guidance` state machine the linear half delegates to. | [guidance.py](agents-remember/mcp/src/agents_remember/worktrees/modules/guidance.py) |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): the ACTIVE-hint assertions were repointed off `lifecycle_gate` onto `lifecycle_turn_end_notification` — `test_front_half_generic_points_back_to_the_rundown`, the renamed `test_decide_points_to_the_turn_end_notification`, the renamed `_gate_after` overlays (`test_closeout_preview_hints_the_turn_end_until_approved`/`test_integrate_dry_run_hints_the_turn_end`/`test_finalize_dry_run_hints_the_turn_end`), the edge dry-run/torn-contract cases, and the `lifecycle_start` choke-point rundown assertion. Added `test_awaiting_developer_hints_the_stop` (`nextTool=None`, "resumes automatically") and the end-to-end `test_turn_end_notification_does_not_self_dismiss_then_next_call_resumes` (the notification keeps its own response on `awaiting-developer`; the next call auto-resumes). The parked `blocked`-gate await/resume tests are unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T20:16+02:00 — Added two gate-await tests: `test_blocked_at_a_gate_awaits_the_decision` (pure — a `blocked` state in both `close` and `build` phases yields `_AWAIT_GATE`/`lifecycle_resume`) and `test_next_step_for_blocked_gate_awaits_resume` (edge — the live `amb.start()` + `amb.block(...)` seam returns the resume hint on the `lifecycle_gate` response). Both pin the blocked-state branch added to `compute_next_step`.
- 2026-06-27T18:43+02:00 — Added file-level onboarding for the new task-27 test suite covering the `compute_next_step` state machine (front-half/decide pointers, linear guidance delegation, the closeout/integrate/finalize gate overlays, `_from_guidance`, and `lifecycle_end` loop-back), the exception-contained `next_step_for` edge (missing/torn-contract degradation, dry-run windows), and the `_tool_payload`/`lifecycle_start` rundown choke point. Verification metadata pinned until closeout stamps the task-27 code commit.
