# mcp/src/agents_remember/memory/knowledge_index/adapters.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The adapter that hands the worklist's registered-scope construction an index as its data source (MIK-R23 rule 6).** The read, view and comparison seams take a dataset *path*, and `KnowledgeIndex.database_path` is that path. `memory/knowledge/registered_scope.py` instead takes an opened store per declared side; this module opens one over an index, through a connection that cannot write, so `construct_registered_scope` runs unchanged and reads nothing but the index.

## Code Commentary

### Logic

- `index_store(index)` opens `open_read_only_database(index.database_path)` and wraps it as an `OpenedKnowledgeStore` with the index namespace (`index.repository_id`) and the inspected schema. The caller closes the connection.
- `scope_snapshot_source(side, index)` is one declared side: its snapshot is `dataset_identity(index.database_path)` and its store is `index_store(index)`.
- `scope_snapshot_declaration(side, index)` is the matching declaration, naming `SCOPE_SELECTOR_POLICY_VERSION` (`recorded-family-frontier/v1`).

### Conventions

- `resource_lock_path` is the index file itself: the store never writes, so no lock is taken on anything else.

### Invariants And Boundaries

- The connection is read-only; the adapter adds no traversal of its own, so the scope construction's semantics stay in `registered_scope.py`.
- Parity with the database is proved for same-side and candidate-changed scopes; composition-policy traversal is not part of text storage and was not declared.

### Todos

MIK-R08 owns the worklist semantics over the index.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The three adapters and the case that proves the scope matches.

- The read-only store over an index. [1]
- One declared side and its declaration, bound to the index's exact snapshot. [2]
- The registered scope over the index equals the scope over the equivalent database, for same sides and for a changed candidate. [3]

### Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

No cross-repo boundary is crossed by this file.
