# mcp/src/agents_remember/memory/knowledge/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `3332a4ce7029777d49feca22b499350435a9f83c`|
| lastVerifiedCommitDate | 2026-09-16T11:50:16+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../../overview.md)

## Purpose

The package facade for the concrete knowledge store. It states the package's ownership in its docstring and
re-exports the served storage surface: the connection contract, the schema manifest and fingerprint, and the
store's open functions and `OpenedKnowledgeStore`.

## Code Commentary

### Logic

The module docstring declares the boundary: the package owns the schema, the row codecs and the insert-only
revision operation; it does **not** own approval, task status or Git attribution, and nothing ranked below it may
import it — lower worktree and memory-quality owners receive `models.knowledge` values or prepared results from
the application layer instead.

`__all__` re-exports `BUSY_TIMEOUT_MILLISECONDS`, `discard_closed_wal_peers` and `immediate_transaction` from
`.connection`; `CANONICAL_COLUMNS`, `CANONICAL_TABLES`, `IMMUTABILITY_TRIGGERS`, `SCHEMA_USER_VERSION`,
`create_schema_statements`, `schema_fingerprint` and `schema_manifest` from `.schema`; and
`OpenedKnowledgeStore`, `open_existing_knowledge_store` and `open_knowledge_store` from `.store`.

**One exported name carries a caller precondition, and it is the one to read before calling anything here:**
`discard_closed_wal_peers` unlinks `-wal`/`-shm` peers and may be used only by a caller that has independently
established that **no connection holds the database**. Since 260915-KS-L4 no close path in this package calls it —
`OpenedKnowledgeStore.close()` relies on SQLite, which checkpoints its WAL and removes both peers itself on the last
clean close — because the unlink cannot know whether another connection (in this process or another) still has the
file open, and a reader holding a read transaction blocks that checkpoint, so an unconditional call destroyed a
committed batch. Its remaining callers are an offline repair or an enclosure cleanup that owns the file. The
function is still exported because that legitimate use exists; it is not a lifecycle call.

### Conventions

The facade deliberately does **not** re-export `records` or `refusals`: the row codecs and the refusal factories
are internal to the package, while the schema manifest and the open functions are the surface a consumer is
entitled to name.

### Invariants And Boundaries

- The import direction is downward and one-way: `memory.knowledge` imports `kernel.canonical_json`,
  `kernel.file_lock` and `models.knowledge`. No package ranked below `memory` (rank 12) may import it back; the
  only consumer today is `application` (rank 21).
- The package writes exactly one database file and holds no durable state, no transport and no approval decision.
- `open_knowledge_store` creates or validates the schema; `open_existing_knowledge_store` never creates or repairs.
  A caller choosing between them is choosing whether a new candidate may be minted.

### Todos

None recorded. The seven canonical tables that this leaf does not write (family, family revision, family
predecessor, source anchor, family member, realization claim) exist with no operations yet.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package boundary statement: schema, codecs and the insert-only operation, but not approval, task status or Git attribution. | "The package owns the schema, the row codecs and the insert-only revision operation." | mcp/src/agents_remember/memory/knowledge/__init__.py:1-7 |
| The served storage surface as an explicit re-export list. | `__all__` | mcp/src/agents_remember/memory/knowledge/__init__.py:29-42 |
| The connection contract re-exported here. | `BUSY_TIMEOUT_MILLISECONDS`; `immediate_transaction` | mcp/src/agents_remember/memory/knowledge/connection.py:23-25; mcp/src/agents_remember/memory/knowledge/connection.py:87-90 |
| The schema manifest and fingerprint re-exported here. | `CANONICAL_TABLES`; `schema_manifest`; `schema_fingerprint` | mcp/src/agents_remember/memory/knowledge/schema.py:31-42; mcp/src/agents_remember/memory/knowledge/schema.py:362-392 |
| The composition seam that is this package's only consumer. | `create_knowledge_revision`; `open_admitted_knowledge_store` | mcp/src/agents_remember/application/knowledge.py:137-165 |
| The layer charter paragraph that records this storage home in `[package.memory]`. | "[package.memory]" | layers.toml:206-222 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): recorded the **caller precondition on the one exported name that has one**. `discard_closed_wal_peers` is still re-exported, but since this leaf no close path in the package calls it: `OpenedKnowledgeStore.close()` relies on SQLite's own last-clean-close behaviour, because the unconditional unlink destroyed a committed batch whenever a reader held a read transaction and blocked the checkpoint. The card states the legitimate remaining use (an offline repair or enclosure cleanup that owns the file exclusively), which is why the name stays exported, and states that it is not a lifecycle call. The re-export list itself is unchanged by this leaf, so no other body text moved. Verification metadata remains closeout-owned.

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new concrete knowledge-storage package facade. It records the package's ownership boundary, the one-way import direction and the create-versus-reopen split. Verification metadata remains empty until closeout stamps the code commit.
