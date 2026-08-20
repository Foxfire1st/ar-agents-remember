# mcp/tests/test_authoring_batch_titles.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_authoring_batch_titles.py`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `overview.md`                                    |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Direct unit tests for the authoring-batch graph-title join (260815-DAG-L12 R1/R4).
`_authoring_batch_titles` is the application seam that labels a sprint's mermaid render
from the in-memory master documents of one authoring batch
(`migrate_execution_topology` / `task_sprint_linkage`). The full authoring flow is heavy
(judgment registers, integration locks), so the join is pinned directly here.

## Code Commentary

### Logic

`AuthoringBatchTitlesTests` builds an in-memory batch of `(ref, root, document)` tuples and
asserts that `_authoring_batch_titles` joins master titles (keyed by `ref.key`) and leaf
titles (from the master's `subTasks` rows) from the batch's own masters — and returns
`None` when no document in the batch carries an `executionGraph`.

### Invariants And Boundaries

- Tests the private seam directly rather than duplicating the heavy authoring flow.
- A batch without a graph produces no titles (render falls back to ref keys).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The authoring-batch title-join forcing suite. | `AuthoringBatchTitlesTests` | mcp/tests/test_authoring_batch_titles.py:58-85 |
| The application seam under test. | `_authoring_batch_titles` | mcp/src/agents_remember/application/task_execution_topology.py:320-329 |
| The shared in-memory title join. | `build_graph_titles` | mcp/src/agents_remember/tasks/execution_graph_titles.py:36-57 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1/R4): direct unit tests for the

authoring-batch graph-title join (titles from in-memory masters; `None` for a batch

without a graph). Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1/R4): direct unit tests for the
  authoring-batch graph-title join (titles from in-memory masters; `None` for a batch
  without a graph). Verified at code commit b7f2c8e2.
