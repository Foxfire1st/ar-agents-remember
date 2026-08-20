# mcp/tests/test_queue_read_degradation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_queue_read_degradation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the 260815-DAG-L13-R4 read-degradation contract: the closeout queue `status` read degrades
to facts and never raises on an absent executionGraph or a missing/malformed canonical register,
while mutations stay guarded. The queue fixture and refs are imported from `test_closeout_queue.py`.

## Code Commentary

### Logic

`QueueReadDegradationTests` proves a graph-less sprint projects the atomic-sequential default with
mode, lane owner, and legal next operations; absent and malformed registers are reported as
per-register facts; mutations on a degraded sprint stay guarded with the register repair named; a
healthy graph status reports `dag` mode; a missing or non-sprint document fails as an argument
fault; mode-resolution movement fails closed; and the degraded scope authorizes only the sprint
architect/strategist/orchestrator or a commanded manager.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; the deployed coordinator is never written.
- The suite asserts behavior through the public `closeout_queue` tool boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Read-degradation forcing across graph-less, register-degraded, and healthy sprints. | `QueueReadDegradationTests` | mcp/tests/test_queue_read_degradation.py:26-167 |
| The status readout and degraded projection under test. | `_status_readout`; `_degraded_projection` | mcp/src/agents_remember/worktrees/queue/closeout_queue.py:254-306; mcp/src/agents_remember/worktrees/queue/closeout_queue.py:323-367 |
| The per-register read facts under test. | `register_section_facts` | mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:437-465 |

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created as the queue read-degradation forcing suite.
  Verification remains closeout-owned.
