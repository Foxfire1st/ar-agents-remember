# mcp/src/agents_remember/tasks/execution_graph_titles.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/tasks/execution_graph_titles.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-24T13:43+02:00                           |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`       |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
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

- `SprintGraphTitles` (frozen dataclass): `master_titles` is keyed by a master ref's `key`
  (`repository/path`), while `leaf_titles` is keyed by `(TaskDocumentRef, leaf id)`. The
  qualified leaf key preserves ownership when independent masters reuse the same local row number.
  An absent qualified key falls back to that node's raw leaf id; it never borrows a title from a
  different master.
- `build_graph_titles(graph, masters)`: pure in-memory join — for every graph master ref,
  read the master's `title` and index its `subTasks` rows by `(ref, number)`. Explicitly placed
  leaf ids remain sprint-wide unique, but unplaced/lump-mode task rows may reuse another master's
  local number. Masters the caller did not supply are skipped.
- `read_graph_titles(tasks_root, graph)`: the disk-backed form — resolves
  `tasks_root / repository / path` for each master ref, validates with
  `TaskDocument.model_validate_json`, tolerates missing/invalid documents (they render
  with the ref-key/leaf-id fallback), then delegates to `build_graph_titles`. Used by the
  application writers that regenerate a sprint's `task.md`.

### Conventions

Persisted graph identity stays in refs and leaf ids. Joined titles are derived display data and
must retain that complete identity through every renderer/projection consumer.

### Invariants And Boundaries

- One join source shared by the mermaid renderer and the dashboard projection.
- Missing/invalid master documents never raise; they degrade to fallback labels.
- Leaf-title lookup is always `(owning master ref, local leaf id)`; there is no flat-key reader.
- Read-only; the join never writes or mutates documents.

### Todos

None.

## Docs References

No Domain Documentation sources are configured for this repository-internal join.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation was available after checking the configured source registry. | _None._ | _No external source._ |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The in-memory join keys leaf titles by owning ref plus local row number; missing documents are skipped. | L22-L59 | [execution_graph_titles.py](mcp/src/agents_remember/tasks/execution_graph_titles.py) |
| The disk-backed join tolerates missing or invalid master documents and delegates to the same owner. | L62-L77 | [execution_graph_titles.py](mcp/src/agents_remember/tasks/execution_graph_titles.py) |
| Mermaid and observer consumers use the qualified key. | L333-L347 | [render.py](mcp/src/agents_remember/tasks/render.py) |
| Projection maps every leaf title through `(node.ref, leaf_id)`. | L188-L209 | [projection_graph.py](mcp/src/agents_remember/observer/projection_graph.py) |
| Focused proof uses legal same-numbered rows and verifies the missing-owner raw-label boundary. | L300-L389 | [test_execution_graph_render.py](mcp/tests/test_execution_graph_render.py) |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-24T13:43+02:00 — DAGQC L1: leaf-title identity changed from a flat local number to
  `(owning TaskDocumentRef, local leaf id)` across both consumers; the missing-qualified-key raw
  label remains local to that node. Verification metadata remains pinned until closeout.

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1/R4): the shared master/leaf title

join (in-memory `build_graph_titles` + disk-backed `read_graph_titles`) that both the

mermaid renderer and the dashboard projection consume. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1/R4): the shared master/leaf title
  join (in-memory `build_graph_titles` + disk-backed `read_graph_titles`) that both the
  mermaid renderer and the dashboard projection consume. Verified at code commit b7f2c8e2.
