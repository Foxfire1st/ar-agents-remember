# mcp/src/agents_remember/memory/knowledge_index/schema.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The index's own `ix_*` tables (MIK-R23 rule 3) and its format name.** The index file holds the eight logical tables the projection fills alongside these lookup tables, so the existing read code runs over the index unchanged. `INDEX_FORMAT` is `ar-knowledge-index/v3` since MIK-R74; a cached file of another format is rebuilt, as before.

## Code Commentary

`INDEX_DDL` creates `ix_meta` (name/value: format, key, source, location, state, converted, builtAt), `ix_problem`, `ix_record`, `ix_entry`, `ix_member` and `ix_route`, `ix_link`, and `ix_history_row`. History rows are keyed `(path, id)` (MIK-R74 rule 4): two closed files may hold the same row ID, and both are indexed. Secondary indexes cover the reverse lookups. Every table is `STRICT`; each record, entry and row keeps its canonical JSON `document` so a lookup returns what the file recorded.

### Invariants And Boundaries

- Nothing here is authored: every row is a join over recorded fields of one tree's files, and deleting the file loses nothing.

## Evidence

- The index format name a cached file must carry is v3 [5]
- The `ix_*` tables and their reverse-direction indexes [6]
- History rows are keyed by file and ID [7]
