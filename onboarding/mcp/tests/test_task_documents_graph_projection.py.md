# mcp/tests/test_task_documents_graph_projection.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_documents_graph_projection.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `overview.md`                                    |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the task-documents projection wiring for the render-ready graph view (260815-DAG-L12
R4): `read_task_documents` now projects `TaskDocNode.executionGraphView` for a sprint whose
master documents exist, and `_master_docs_by_ref` builds the title/status/nature join table
from the bounded payload window.

## Code Commentary

### Logic

`TaskDocumentsGraphViewProjectionTests` writes real task documents into a disposable
coordination root and reads them through the public `read_task_documents`: a sprint doc
with a graph carries the render-ready `executionGraphView` (nodes with joined master/leaf
titles, wave indexes, mechanical frontier states, natures, predecessors); the segmented
master scenario projects titles and predecessor reasons across waves; and
`_master_docs_by_ref` skips invalid master payloads and non-master documents while indexing
valid masters by their `TaskDocumentRef`. Non-sprint docs project `None` (backward
compatible).

### Invariants And Boundaries

- Tests construct only disposable coordination roots.
- The projection is exercised through the public reader, not the internal builder.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection wiring forcing suite. | `TaskDocumentsGraphViewProjectionTests` | mcp/tests/test_task_documents_graph_projection.py:34-222 |
| The reader that now carries the graph view. | `read_task_documents` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:63-101 |
| The master join-table builder under test. | `_master_docs_by_ref` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:370-396 |
| The served field on the task-document node. | `executionGraphView` | mcp/src/agents_remember/observer/projection.py:798-798 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R4): the task-documents projection

wiring suite — render-ready graph view on sprint docs, segmented-master scenario, and the

master-join-table builder. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R4): the task-documents projection
  wiring suite — render-ready graph view on sprint docs, segmented-master scenario, and the
  master-join-table builder. Verified at code commit b7f2c8e2.
