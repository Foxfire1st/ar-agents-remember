# mcp/tests/test_sequential_default_mode.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sequential_default_mode.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
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
| The lane block, stale-artifact replacement, and dispatch surfacing forcing. | `SequentialLaneTests` | mcp/tests/test_sequential_default_mode.py:191-354 |
| The scheduling-mode resolver under test. | `resolve_scheduling_mode`; `effective_execution_nature`; `sequential_lane_owner` | mcp/src/agents_remember/worktrees/scheduling_mode.py:46-156 |
| The lane-blocked bootstrap under test. | `_sequential_lane_block` | mcp/src/agents_remember/worktrees/modules/start_contract.py:269-312 |
| The dispatch structural-outcome surfacing under test. | `_manager_series_bootstrap_refusal` | mcp/src/agents_remember/application/structural/agent_tools.py:419-484 |

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created as the atomic-sequential default and series
  lane forcing suite. Verification remains closeout-owned.
