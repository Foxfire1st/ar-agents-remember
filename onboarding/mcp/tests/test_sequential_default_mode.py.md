# mcp/tests/test_sequential_default_mode.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sequential_default_mode.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `3eafc555c848ac45a07a07720641f1735f8df0eb` |
| lastVerifiedCommitDate | 2026-08-21T05:15:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the 260815-DAG-L13-R1 scheduling semantics: a sprint without an `executionGraph` runs the
atomic-sequential default — every commanded master executes atomically regardless of declared
nature, and at most one master is in flight through the series landing lane.

## Code Commentary

### Logic

`SchedulingModeTests` proves mode resolution (graph ⇒ dag, no graph ⇒ atomic-sequential, non-sprint
refused), the effective-nature matrix, and lane ownership as the stored fact of a live
(non-terminal) series contract. `SequentialLaneTests` forces the series-bootstrap lane block: a
second commanded master's bootstrap returns the blocked `sequential-lane-owned` result naming the
owner and legal next operations, the block is rechecked under the bootstrap lock, lane-resolution
failure fails closed, a terminal stale series artifact is replaced rather than honored, a
standalone master has no lane contention, and manager dispatch surfaces the block as a structural
outcome.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; the deployed coordinator is never written.
- Lane ownership is asserted through stored series contracts, not request data.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Mode resolution and the effective-nature matrix forcing. | `SchedulingModeTests` | mcp/tests/test_sequential_default_mode.py:118-189 |
| The lane block, stale-artifact replacement, and dispatch surfacing forcing. | `SequentialLaneTests` | mcp/tests/test_sequential_default_mode.py:191-350 |
| The scheduling-mode resolver under test. | `resolve_scheduling_mode`; `effective_execution_nature`; `sequential_lane_owner` | mcp/src/agents_remember/worktrees/scheduling_mode.py:46-156 |
| The lane-blocked bootstrap under test. | `_sequential_lane_block` | mcp/src/agents_remember/worktrees/modules/start_contract.py:269-312 |
| The dispatch structural-outcome surfacing under test. | `_manager_series_bootstrap_refusal` | mcp/src/agents_remember/application/structural/agent_tools.py:512-576 |

## Update History

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 curator: repaired the `_manager_series_bootstrap_refusal` citation range (agent_tools.py:419-484 → 518-582) surfaced by the leaf-scoped quality check; no content impact on the documented test contract. Verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created as the atomic-sequential default and series
  lane forcing suite. Verification remains closeout-owned.
