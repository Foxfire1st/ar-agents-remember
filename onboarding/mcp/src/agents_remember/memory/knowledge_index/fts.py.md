# mcp/src/agents_remember/memory/knowledge_index/fts.py

## Governing Overview

[memory](../overview.md)

## Purpose

Deterministic SQLite FTS5 indexing and query module (`ix_fts`) embedded inside the derived knowledge index. Indexes live record text (`title`, `statement`, `conditions`, `applicability`) using `porter unicode61` tokenization and ranks matches deterministically without altering memory-repository schemas or handling MCP formatting.

## Code Commentary

- `DEFAULT_SEARCH_KINDS` defaults to `("invariant", "family", "weakness")`; `ALLOWED_SEARCH_KINDS` covers the 12 live record kinds and excludes `history/`.
- `populate_fts` iterates `sorted(parsed.records)` for byte-reproducible builds, skips retired invariants and closed weaknesses via `_excluded_from_live_fts`, extracts four text columns per record kind, and inserts rows into `ix_fts`.
- `tokenize_query` extracts lowercase `[A-Za-z0-9_]+` tokens, deduplicates in order, and drops single-character tokens when longer tokens exist; empty token lists or empty normalized kinds return `()`.
- `search_fts` executes an `OR` FTS5 query with `_BM25_WEIGHTS = "0.0, 0.0, 3.0, 2.0, 1.2, 1.0"`, computes distinct-term coverage and multi-term phrase matches, combines BM25 magnitude, coverage, and phrase boost (`+12.0`), and tie-breaks deterministically by `(-score, -phrase_matched, -terms_matched, record_id)`.

## Relationships

- Called by `memory/knowledge_index/build.py` (`populate_fts`) and `memory/knowledge_index/query.py` (`search_fts`); re-exported by `memory/knowledge_index/__init__.py`; tested in `mcp/tests/test_kno_r07_knowledge_queries.py`.
- Uses `apsw` SQLite FTS5 over the `ix_fts` virtual table declared in `memory/knowledge_index/schema.py`.

## Evidence

- Defines default and allowed live search kinds (excluding `history/`) and BM25 column weights. [1]
- `populate_fts` populates `ix_fts` in sorted `record_id` order while skipping retired invariants and closed weaknesses. [2]
- `search_fts` ranks hits with BM25, distinct-term coverage, exact-phrase boost, and deterministic `record_id` tie-breaking. [3]
- `_excluded_from_live_fts` filters out retired invariants and closed weaknesses from the live FTS table. [4]
