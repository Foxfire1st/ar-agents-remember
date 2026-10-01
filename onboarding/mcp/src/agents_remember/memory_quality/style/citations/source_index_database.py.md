# mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Store and query one immutable SQLite citation source-index generation, proving that its metadata matches the published readiness authority.

## Code Commentary

### Logic

`Database` stores file identities, direct-anchor postings, compressed quote streams and their lookup indexes, and call-literal extents. `locations` routes non-quote anchors through keyed direct lookup and quote anchors through indexed candidate streams, returning deterministic file/range results.

`write_snapshot` flushes buffered postings and writes generation, content snapshot, roots, counters, application digest, and candidate selection. Filesystem selection is stored as an empty `candidate_tree` string; a Git selection stores its exact tree identity.

`open` checks the database's actual size, opens SQLite read-only/immutable, validates the exact metadata key set and readiness identity, and checks bounded counters. Roots and candidate selection must match the ready marker. Explicit integrity verification additionally performs SQLite `quick_check` and decodes/checks the application values and checksum; ordinary queries retain their keyed lookup path.

### Conventions

Readiness schema and limits come from `source_index_state`. This module owns SQLite layout, encoding, query telemetry, and database validation; source census, cache locking, and publication order remain in their existing acquisition owners.

### Invariants And Boundaries

- A missing `candidate_tree` metadata key is malformed; filesystem and Git-candidate generations cannot substitute for each other through equal content hashes.
- Generation/snapshot identity, roots, candidate selection, counters, and database size must agree with the supplied readiness marker before queries are admitted.
- SQLite structural validity alone does not prove packed postings, quote streams, or their cross-references are usable; explicit prebuild validation checks both layers.
- Stored candidate identity binds this database to an acquisition selection; it does not itself inspect Git or prove current working-tree bytes.

### Todos

None.

## Evidence

### Repo-Internal References

- The exact metadata schema binds generation, snapshot, roots, and candidate selection to readiness. [1]
- Canonical bounded counters must match the ready marker. [2]
- Opening checks size and metadata before admitting read-only queries, with explicit integrity checks when requested. [3]
- Snapshot publication records candidate identity alongside the application checksum and counters. [4]
- Anchor queries retain distinct direct and quote lookup paths. [5]
- Explicit integrity validation checks packed data, references, counters, and the stored digest. [6]
- The application checksum covers query-bearing rows including FTS term/document pairs. [7]
