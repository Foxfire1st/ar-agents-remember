# mcp/tests/test_authoring_batch_titles.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_authoring_batch_titles.py`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-24T13:43+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Direct unit tests for the shared publication-batch graph-title join (260815-DAG-L12 R1/R4,
centralized by 260821-DAGQC-L1). `build_publication_batch_graph_titles` is the application seam
that labels the sole graph-bearing document's Mermaid render from the in-memory master documents
of one publication batch. It is shared by topology and sprint-linkage publication rather than
duplicated behind private authoring helpers.

## Code Commentary

### Logic

`AuthoringBatchTitlesTests` builds an in-memory batch of `(ref, root, document)` tuples and
asserts that `build_publication_batch_graph_titles` joins master titles (keyed by `ref.key`) and
leaf titles (keyed by `(ref, row.number)`) from the batch's own masters — and returns `None` when
no document in the batch carries an `executionGraph`. The separate cardinality suite owns the
two-graph refusal; this file pins the positive and zero-graph title construction paths.

### Invariants And Boundaries

- Tests the shared application seam directly rather than duplicating the publication flow.
- A batch without a graph produces no titles (render falls back to ref keys).
- Leaf title keys retain the owning master reference; no flat-key reader is accepted.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The publication-batch title-join forcing suite. | `AuthoringBatchTitlesTests` | mcp/tests/test_authoring_batch_titles.py:59-86 |
| The central application seam under test admits zero or one graph-bearing document and constructs one title context. | `build_publication_batch_graph_titles`; `require_single_graph_document` | mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py:17-34; mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py:37-49 |
| The shared in-memory title join preserves master-qualified leaf identity. | `build_graph_titles` | mcp/src/agents_remember/tasks/execution_graph_titles.py:23-52 |
| The separate graph-publication suite pins the cardinality refusal before the publication transaction. | `TaskDocGraphPublicationTests` | mcp/tests/test_task_doc_graph_publication.py:93-160 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: moved the card from the retired private authoring
  helper to the shared publication-batch graph-title owner and recorded qualified leaf-title keys.
  Verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1/R4): direct unit tests for the

authoring-batch graph-title join (titles from in-memory masters; `None` for a batch

without a graph). Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1/R4): direct unit tests for the
  authoring-batch graph-title join (titles from in-memory masters; `None` for a batch
  without a graph). Verified at code commit b7f2c8e2.
