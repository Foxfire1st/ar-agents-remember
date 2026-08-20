# mcp/src/agents_remember/tasks/execution_graph_titles.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/tasks/execution_graph_titles.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `overview.md`                                    |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Joined master/leaf titles for one sprint execution graph (260815-DAG-L12 R1/R4). The
persisted graph stores refs and leaf ids only; the human-readable render (mermaid diagram,
dashboard projection) joins titles from the commanded master documents. This module owns
that join so the renderer and the projection share one source of truth.

## Code Commentary

### Logic

- `SprintGraphTitles` (frozen dataclass): `master_titles` keyed by a master ref's `key`
  (`repository/path`), `leaf_titles` keyed by leaf id. Absent keys mean the source
  document was missing or invalid; callers fall back to the raw key / leaf id.
- `build_graph_titles(graph, masters)`: pure in-memory join — for every graph master ref,
  read the master's `title` and index its `subTasks` rows by `number` (the graph's leaf ids
  ARE the row `number` values, sprint-wide unique per the L11 contract) so the row `name`
  is the leaf's title. Masters the caller did not supply are skipped.
- `read_graph_titles(tasks_root, graph)`: the disk-backed form — resolves
  `tasks_root / repository / path` for each master ref, validates with
  `TaskDocument.model_validate_json`, tolerates missing/invalid documents (they render
  with the ref-key/leaf-id fallback), then delegates to `build_graph_titles`. Used by the
  application writers that regenerate a sprint's `task.md`.

### Invariants And Boundaries

- One join source shared by the mermaid renderer and the dashboard projection.
- Missing/invalid master documents never raise; they degrade to fallback labels.
- Read-only; the join never writes or mutates documents.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The in-memory title join from master documents. | `build_graph_titles` | mcp/src/agents_remember/tasks/execution_graph_titles.py:36-57 |
| The disk-backed join used by application writers. | `read_graph_titles` | mcp/src/agents_remember/tasks/execution_graph_titles.py:60-75 |
| The persisted graph whose refs/leaf ids this joins. | `SprintExecutionGraph` | mcp/src/agents_remember/tasks/document.py:319-372 |
| The mermaid renderer consumes the joined titles. | `_execution_graph_lines` | mcp/src/agents_remember/tasks/render.py:173-213 |
| The render-ready view builder consumes the same titles. | `build_execution_graph_view` | mcp/src/agents_remember/observer/projection_graph.py:228-260 |
| The title-join unit tests. | `ExecutionGraphMermaidRenderTests`; `AuthoringBatchTitlesTests` | mcp/tests/test_authoring_batch_titles.py:58-85; mcp/tests/test_execution_graph_render.py:50-223 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1/R4): the shared master/leaf title

join (in-memory `build_graph_titles` + disk-backed `read_graph_titles`) that both the

mermaid renderer and the dashboard projection consume. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1/R4): the shared master/leaf title
  join (in-memory `build_graph_titles` + disk-backed `read_graph_titles`) that both the
  mermaid renderer and the dashboard projection consume. Verified at code commit b7f2c8e2.
