# mcp/src/agents_remember/memory/knowledge_index/schema.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The index's own `ix_*` tables (MIK-R23 rule 3) and its format name.** The index file holds the eight logical tables the projection fills alongside these lookup tables, so the existing read code runs over the index unchanged. `INDEX_FORMAT` is `ar-knowledge-index/v7`. A cached file of another format is rebuilt.

## Code Commentary

`INDEX_DDL` creates `ix_meta` (name/value: format, key, source, location, state, converted, builtAt), `ix_problem`, `ix_record`, `ix_entry`, `ix_member` and `ix_route`,  `ix_link`, `ix_history_row` and `ix_revision`. The revision table uses the record and revision as its key and carries standing and writer attribution. History rows are keyed `(path, id)` (MIK-R74 rule 4): two closed files may hold the same row ID, and both are indexed. Secondary indexes cover the reverse lookups. Every table is `STRICT`; each record, entry and row keeps its canonical JSON `document` so a lookup returns what the file recorded.

### Invariants And Boundaries

- Nothing here is authored: every row is a join over recorded fields of one tree's files, and deleting the file loses nothing.

## Evidence



- History rows are keyed by file and ID [7]

- The index format name a cached file must carry is v7. [5]
- The derived revision table keys each row by record and revision. [8]

- The ix tables and their reverse lookups are defined in the derived index layout. [6]
