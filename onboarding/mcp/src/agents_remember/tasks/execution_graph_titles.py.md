# mcp/src/agents_remember/tasks/execution_graph_titles.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/tasks/execution_graph_titles.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-24T13:43+02:00                           |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`       |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation was available after checking the configured source registry. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The in-memory join keys leaf titles by owning ref plus local row number; missing documents are skipped. | `SprintGraphTitles`; `build_graph_titles` | mcp/src/agents_remember/tasks/execution_graph_titles.py:22-34; mcp/src/agents_remember/tasks/execution_graph_titles.py:37-59 |
| The disk-backed join tolerates missing or invalid master documents and delegates to the same owner. | `read_graph_titles` | mcp/src/agents_remember/tasks/execution_graph_titles.py:62-77 |
| Mermaid and observer consumers use the qualified key. | `_mermaid_segment_lines` | mcp/src/agents_remember/tasks/render.py:331-345 |
| Projection maps every leaf title through `(node.ref, leaf_id)`. | `_node_view` | mcp/src/agents_remember/observer/projection_graph.py:188-225 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-08-24T13:43+02:00 — DAGQC L1: leaf-title identity changed from a flat local number to
  `(owning TaskDocumentRef, local leaf id)` across both consumers; the missing-qualified-key raw
  label remains local to that node. Verification metadata remains pinned until closeout.

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1/R4): the shared master/leaf title

join (in-memory `build_graph_titles` + disk-backed `read_graph_titles`) that both the

mermaid renderer and the dashboard projection consume. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1/R4): the shared master/leaf title
  join (in-memory `build_graph_titles` + disk-backed `read_graph_titles`) that both the
  mermaid renderer and the dashboard projection consume. Verified at code commit b7f2c8e2.
