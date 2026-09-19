# mcp/src/agents_remember/memory/knowledge/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

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
`.connection`; `CANONICAL_COLUMNS`, `CANONICAL_TABLES`, `IMMUTABILITY_TRIGGERS`, `SCHEMA_USER_VERSION` and
`schema_manifest` from `.schema`; `CURRENT_GENERATION`, `GENERATIONS`, `GENERATION_1`, `GENERATION_1_FINGERPRINT`,
`GENERATION_2`, `SchemaGeneration`, `generation_of_database`, `generation_of_new_store`,
`require_pinned_generation_1_unchanged`, `structure_fingerprint` and `structure_manifest` from
`.schema_generations`; and `OpenedKnowledgeStore`, `open_existing_knowledge_store` and `open_knowledge_store` from
`.store`.

**Since 260915-KS-L10 the facade publishes the generation registry and no longer publishes the two builders that
moved behind it.** `create_schema_statements` and `schema_fingerprint` left `__all__` because both are now functions
of a *generation record* rather than of the running build: a consumer that wants either must name the generation it
means (`structure_fingerprint`/`structure_manifest` over `GENERATION_1` or `GENERATION_2`, or
`create_schema_statements` from `.schema_generations`), and re-exporting the old argument-less spellings would have
invited a caller to fingerprint "whatever this build is". `generation_of_new_store` and `CURRENT_GENERATION` are the
published way to answer "what will a store I create declare", and `require_pinned_generation_1_unchanged` is published
so a consumer can run the pin itself. The facade still does **not** re-export `records`, `refusals`, `routes` or
`record_envelope`: those remain internal to the package, and the route and envelope operations are reached through
their own modules.

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
| The connection contract re-exported here. | `BUSY_TIMEOUT_MILLISECONDS`; `immediate_transaction` | mcp/src/agents_remember/memory/knowledge/connection.py:23-23; mcp/src/agents_remember/memory/knowledge/connection.py:131-134 |
| The schema manifest and fingerprint re-exported here. | `CANONICAL_TABLES`; `schema_manifest`; `schema_fingerprint` | mcp/src/agents_remember/memory/knowledge/schema.py:31-42; mcp/src/agents_remember/memory/knowledge/schema.py:412-422; mcp/src/agents_remember/memory/knowledge/schema.py:425-442 |
| The composition seam that is this package's only consumer. | `create_knowledge_revision`; `open_admitted_knowledge_store` | mcp/src/agents_remember/application/knowledge.py:193-204; mcp/src/agents_remember/application/knowledge.py:207-221 |
| The layer charter paragraph that records this storage home in `[package.memory]`. | "[package.memory]" | layers.toml:206-222 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): **the facade's served surface moved with the schema.** `__all__` gained the generation registry (`CURRENT_GENERATION`, `GENERATIONS`, `GENERATION_1`, `GENERATION_1_FINGERPRINT`, `GENERATION_2`, `SchemaGeneration`, `generation_of_database`, `generation_of_new_store`, `require_pinned_generation_1_unchanged`, `structure_fingerprint`, `structure_manifest`) and **dropped** `create_schema_statements` and `schema_fingerprint`, because both are now functions of a generation record rather than of the running build — re-exporting the old argument-less spellings would have invited a caller to fingerprint whatever this build happens to be. The card records that the registry is the published way to ask what a created store will declare, that the pin is published so a consumer can run it, and that `routes` and `record_envelope` stay unexported like `records` and `refusals`. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T07:33:51+00:00: Generated citation repair: `BUSY_TIMEOUT_MILLISECONDS`; `immediate_transaction` repointed to mcp/src/agents_remember/memory/knowledge/connection.py:26-26; mcp/src/agents_remember/memory/knowledge/connection.py:124-127. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `create_knowledge_revision`; `open_admitted_knowledge_store` repointed to mcp/src/agents_remember/application/knowledge.py:207-221; mcp/src/agents_remember/application/knowledge.py:193-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `BUSY_TIMEOUT_MILLISECONDS` in the row 81 of this card from mcp/src/agents_remember/memory/knowledge/connection.py:124-125 to mcp/src/agents_remember/memory/knowledge/connection.py:26, the extent of the construct the claim is about (the checker named line(s) [26, 46, 65] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/memory/knowledge/connection.py:124-125 in the row 81 of this card; the repetition added no pooled evidence

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): recorded the **caller precondition on the one exported name that has one**. `discard_closed_wal_peers` is still re-exported, but since this leaf no close path in the package calls it: `OpenedKnowledgeStore.close()` relies on SQLite's own last-clean-close behaviour, because the unconditional unlink destroyed a committed batch whenever a reader held a read transaction and blocked the checkpoint. The card states the legitimate remaining use (an offline repair or enclosure cleanup that owns the file exclusively), which is why the name stays exported, and states that it is not a lifecycle call. The re-export list itself is unchanged by this leaf, so no other body text moved. Verification metadata remains closeout-owned.

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new concrete knowledge-storage package facade. It records the package's ownership boundary, the one-way import direction and the create-versus-reopen split. Verification metadata remains empty until closeout stamps the code commit.
