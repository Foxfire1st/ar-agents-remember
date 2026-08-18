# mcp/tests/test_closeout_queue_projection.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/tests/test_closeout_queue_projection.py`          |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-08-18T00:00+02:00                                 |
| lastVerifiedCommitHash | `2597ff98306ba7c7963005092ac597c4972e63ce`             |
| lastVerifiedCommitDate | 2026-08-18T15:45:32+02:00|
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

## Update History

- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the closeout-queue projection test suite.
  Verification metadata pinned until closeout stamps the L8 commit.
