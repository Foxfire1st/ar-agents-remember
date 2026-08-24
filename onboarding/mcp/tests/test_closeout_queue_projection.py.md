# mcp/tests/test_closeout_queue_projection.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/tests/test_closeout_queue_projection.py`          |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Covers the read-only closeout-queue serving projection (`_closeout_queue.py`). It reuses `QueueFixture`
from `test_closeout_queue.py` so the queue artifact, task documents, and execution graph are real rather
than test-only, then asserts candidates (state, grade, reasons), the empty-artifact case, and the active
atomic blocker projection.

## Code Commentary

### Logic

`test_projects_candidates_and_grades_from_queue_artifact` declares two candidates (one graded, one
grade-less) and asserts the projected state/grade/reasons. `test_projects_no_queue_when_artifact_absent`
proves the reader stays quiet with no artifact. `test_projects_atomic_blocker` writes an active blocker
into the artifact directly and asserts it projects with its rationale.

### Invariants And Boundaries

- Candidate grade, state, and reasons are asserted against the durable artifact, not inferred.
- The blocker test bypasses `acquire-blocker` validation to isolate the projection path.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate, grade, and reason projection. | `test_projects_candidates_and_grades_from_queue_artifact` | mcp/tests/test_closeout_queue_projection.py:15-31 |
| Empty-artifact projection stays quiet. | `test_projects_no_queue_when_artifact_absent` | mcp/tests/test_closeout_queue_projection.py:39-41 |
| Active blocker projection with rationale. | `test_projects_atomic_blocker` | mcp/tests/test_closeout_queue_projection.py:38-57 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces source-census purity, deterministic fingerprints, drift fencing, malformed-neighbor refusal, waiting-only membership, and valid terminal-empty projections.

### Current Invariants

- Old queue rows are never rebuild input.
- Source mismatch or unreadable authority is non-admitting and never treated as absence.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the closeout-queue projection test suite.
  Verification metadata pinned until closeout stamps the L8 commit.
