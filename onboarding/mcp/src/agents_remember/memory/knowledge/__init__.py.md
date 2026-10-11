# mcp/src/agents_remember/memory/knowledge/__init__.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The package facade for the derived index's readers. It states the package's ownership in its docstring and
re-exports the served surface: the connection contract, the one schema and its pin, and the
store's open functions and `OpenedKnowledgeStore`.

## Code Commentary

### Logic

The module docstring declares the boundary: the package owns the schema, the row codecs and the read operations; it owns no writer
of knowledge rows — the canonical database was retired — and it does **not** own approval, task status or Git attribution, and nothing ranked below it may
import it — lower worktree and memory-quality owners receive `models.knowledge` values or prepared results from
the application layer instead.

`__all__` re-exports `BUSY_TIMEOUT_MILLISECONDS` from `.connection`; `CURRENT_GENERATION`,
`SchemaGeneration`, `generation_of_database`, `generation_of_new_store`,
`require_pinned_schema_unchanged`, `structure_fingerprint` and `structure_manifest` from
`.schema`; and `OpenedKnowledgeStore`, `open_existing_knowledge_store` and `open_read_only_store` from
`.store`. The generation registry is gone: one schema is composed and pinned, and the read-only
open joins the surface because readers run over the index without ever writing it.

**The generation registry is gone, and with it the two builders that hid behind it.** `GENERATIONS`,
`GENERATION_1`, `GENERATION_2`, `require_pinned_generation_1_unchanged` and `schema_generations`
left the surface: one schema is composed by `_compose` and pinned by fingerprint, and
`generation_of_new_store` and `CURRENT_GENERATION` answer "what will a store I create declare".

**`discard_closed_wal_peers` is gone with the writer.** The WAL-peer unlink belonged to the retired
canonical store's close path; readers of the derived index never unlink peers.

### Conventions

The facade deliberately does **not** re-export `records` or `refusals`: the row codecs and the refusal factories
are internal to the package, while the schema manifest and the open functions are the surface a consumer is
entitled to name.

### Invariants And Boundaries

- The import direction is downward and one-way: `memory.knowledge` imports `kernel.canonical_json`,
  `kernel.file_lock` and `models.knowledge`. No package ranked below `memory` (rank 12) may import it back; the
  only consumer today is `application` (rank 21).
- The package writes no knowledge dataset and holds no durable state, no transport and no approval decision: knowledge is text in Git, and the only SQLite this build creates is the derived index the index cache owns.
- `open_existing_knowledge_store` never creates or repairs, and `open_read_only_store` runs reads
  over the index without ever writing it. A caller choosing among them is choosing whether a new candidate may be minted, and whether the open may write at all.

### Todos

None recorded. The eight logical tables are all read here; no table exists without a reader.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The package boundary: schema, codecs and reads, but not approval, task status or Git attribution [1]
- The served surface is one schema, its pin, and the read opens [2]
- The read-only open joins the surface [4]
- The connection contract re-exported here. [3]
- The layer charter paragraph that records this storage home in `[package.memory]`. [6]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
