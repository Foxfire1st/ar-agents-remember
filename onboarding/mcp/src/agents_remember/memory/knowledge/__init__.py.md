# mcp/src/agents_remember/memory/knowledge/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `76c7697ca275a8d2764729145c950c166f3f9ec3`|
| lastVerifiedCommitDate | 2026-09-16T10:27:28+02:00|
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

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new concrete knowledge-storage package facade. It records the package's ownership boundary, the one-way import direction and the create-versus-reopen split. Verification metadata remains empty until closeout stamps the code commit.
