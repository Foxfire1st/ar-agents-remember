# mcp/src/agents_remember/application/knowledge_reader/records_batch.py

## Governing Overview

[application](../overview.md)

## Purpose

Implements `knowledge_read(view="records")` for batch full-text lookup of up to 25 record IDs without ever trimming statements, returning verbatim record fields, symbol-preserving `realizedIn`/`proofs` paths, and inline `staleAnchors` diagnostics within the 5,000-token `knowledge_read` ceiling.

## Code Commentary

- `records_view` strips and deduplicates `recordIds`, refusing empty lists or lists exceeding `MAX_BATCH_RECORD_IDS` (`25`) with `refusalCode="invalid-input"`, and refusing invalid or out-of-range cursors with `bad_continuation`.
- Preserves requested ID order while collecting absent IDs in `missing`; hydrates `states_at` currentness for found invariants and `index.standings` for all found records.
- `_format_invariant` returns verbatim `statement` (never trimmed), `applicability`, `conditions`, `exclusions`, `realizedIn`, `proofs`, and `families`; whenever `anchors["stale"] > 0`, includes `staleAnchors` with exact `count` and up to `STALE_ANCHOR_INLINE_CAP = 10` inline entries (`id`, `kind`, `path`, `state`, optional `reason`).
- `_entry_paths` groups realizations and proofs by normalized path and emits every recorded symbol verbatim as `<path>::<sym1>, <sym2>` with no symbol collapse or cap.
- Paginates via `fit_slice_in_budget` using `DEFAULT_RECORDS_BUDGET_TOKENS = 4650` and `MAX_RECORDS_PER_PAGE = 20`.

## Relationships

- Called by `mcp/src/agents_remember/mcp/tools/knowledge_queries.py` (`records_view`) and re-exported by `application/knowledge_reader/truth.py`; tested in `mcp/tests/test_kno_r07_knowledge_queries.py`.
- Depends on `application/knowledge_query_formatting.py`, `application/file_briefs/titles.py::rule_title`, `application/knowledge_reader/paths.py::states_at`, `application/knowledge_reader/selection.py::ReaderSelection`, and `memory/knowledge_index`.

## Evidence

- `records_view` enforces 25-ID cap, 20-record page cap, 4,650-token budget, and cursor validation. [1]
- `_format_invariant` returns verbatim statements, conditions, exclusions, and inline `staleAnchors` whenever `stale > 0`. [2]
- `_entry_paths` preserves every realization and proof symbol locator verbatim per path without collapsing or capping symbols. [3]
