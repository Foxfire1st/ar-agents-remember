# mcp/src/agents_remember/tasks/execution_graph_titles.py

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

## Evidence

### Docs References

No Domain Documentation sources are configured for this repository-internal join.

No relevant external documentation was available after checking the configured source registry.

### Repo-Internal References

- The in-memory join keys leaf titles by owning ref plus local row number; missing documents are skipped. [1]
- The disk-backed join tolerates missing or invalid master documents and delegates to the same owner. [2]
- Mermaid and observer consumers use the qualified key. [3]
- Projection maps every leaf title through `(node.ref, leaf_id)`. [4]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
