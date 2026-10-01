# mcp/src/agents_remember/memory/knowledge/__init__.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The package boundary statement: schema, codecs and the insert-only operation, but not approval, task status or Git attribution. [1]
- The served storage surface as an explicit re-export list. [2]
- The connection contract re-exported here. [3]
- The schema manifest and fingerprint re-exported here. [4]
- The composition seam that is this package's only consumer. [5]
- The layer charter paragraph that records this storage home in `[package.memory]`. [6]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
