# mcp/src/agents_remember/memory/knowledge_index/adapters.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_index/adapters.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:01:17+02:00 |
| lastVerifiedCommitHash | `ffd043f1354e94a7dcf435e10b4b7224495cbcba`|
| lastVerifiedCommitDate | 2026-09-29T08:30:03+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The three adapters and the case that proves the scope matches.

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-only store over an index. | `index_store` | mcp/src/agents_remember/memory/knowledge_index/adapters.py:26-36 |
| One declared side and its declaration, bound to the index's exact snapshot. | `scope_snapshot_source`; `scope_snapshot_declaration`; `SCOPE_SELECTOR_POLICY_VERSION` | mcp/src/agents_remember/memory/knowledge_index/adapters.py:39-44; mcp/src/agents_remember/memory/knowledge_index/adapters.py:47-56; mcp/src/agents_remember/memory/knowledge_index/adapters.py:23-23 |
| The registered scope over the index equals the scope over the equivalent database, for same sides and for a changed candidate. | `test_the_registered_scope_constructs_the_same_scope_over_the_index` | mcp/tests/test_knowledge_index_surfaces.py:147-230 |

## Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
