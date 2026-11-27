# mcp/src/agents_remember/application/knowledge_search.py

## Governing Overview

[application](overview.md)

## Purpose

Implements `knowledge_read(view="search")` over the derived SQLite FTS5 `ix_fts` table with kind validation, optional `files`/`folder` scoping, standing and anchor currentness enrichment, 80-word statement trimming, compact mode, and token-bounded pagination.

## Code Commentary

- `search_view` refuses empty/blank queries and unsupported `kinds` (including `"history"`) with `refusalCode="invalid-input"`; `_validate_kinds` defaults to `DEFAULT_SEARCH_KINDS` (`invariant`, `family`, `weakness`) and expands `"all"` to sorted `ALLOWED_SEARCH_KINDS`.
- Queries `index.search_fts`, optionally filters hits by `files`/`folder` scope via `_filter_hits_by_scope`, and rejects bad or out-of-range cursors with `refusalCode="bad_continuation"`.
- Hydrates records, standings, and invariant currentness (`states_at`) only for a bounded 60-hit lookahead window (`scoped_hits[start : start + 60]`) to avoid loading full match sets on every page.
- `_format_hit` emits either a one-line compact string (`compact=True`) or a structured row with `id`, `kind`, `score`, `termsMatched` (`m/n` or `m/n+phrase`), `standing`, 80-word trimmed `statement`, optional `title`, and `at` paths capped at `_SEARCH_FILE_CAP = 4`.
- Paginates via `fit_slice_in_budget` with `DEFAULT_SEARCH_BUDGET_TOKENS = 3350` and `_MAX_ITEMS_PER_PAGE = 20`.

## Relationships

- Called by `mcp/src/agents_remember/mcp/tools/knowledge_queries.py` (`SearchQuery`, `search_view`); tested in `mcp/tests/test_kno_r07_knowledge_queries.py`.
- Depends on `application/knowledge_query_formatting.py`, `application/file_briefs/titles.py::rule_title`, `application/knowledge_reader/paths.py::states_at`, `application/knowledge_reader/selection.py::ReaderSelection`, and `memory/knowledge_index` (`ALLOWED_SEARCH_KINDS`, `DEFAULT_SEARCH_KINDS`, `FtsHit`).

## Evidence

- `search_view` validates query/kinds/cursor, runs FTS5 search, hydrates a 60-hit window, and paginates within `DEFAULT_SEARCH_BUDGET_TOKENS` (`3350`). [1]
- `_validate_kinds` defaults to `DEFAULT_SEARCH_KINDS`, expands `"all"`, and refuses unsupported kinds such as `"history"`. [2]
- `_format_hit` formats `termsMatched` (`+phrase`), standing, 80-word trimmed statement, and capped `at` paths (or compact line). [3]
