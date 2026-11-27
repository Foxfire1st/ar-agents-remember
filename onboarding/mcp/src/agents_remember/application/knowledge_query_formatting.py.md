# mcp/src/agents_remember/application/knowledge_query_formatting.py

## Governing Overview

[application](overview.md)

## Purpose

Shared pure formatting, path normalization, statement trimming, standing/anchor labeling, query-cursor encoding/decoding, and token-budget pagination helpers used across `impact`, `search`, and `records` query views. Does not open indexes or build MCP response envelopes.

## Code Commentary

- `normalize_repo_path` standardizes path separators and strips leading `./` and boundary slashes; `resolve_indexed_paths` resolves exact normalized paths or unique `/{suffix}` matches against `index.live_entry_paths_under("")`, returning `(resolved_paths, unmatched_files)`.
- `trim_statement` trims statements beyond `STATEMENT_WORD_CAP` (`80` words), preferring a sentence boundary in the trailing 20-word window, and appends ` … (full: records <record_id>)`.
- `anchor_counts`, `writer_label`, and `standing_label` summarize `Currentness` and `RecordStanding` into compact `<state>|<writer>|<anchor_text>` labels.
- `scope_digest` (12-hex SHA-256 of canonical JSON), `encode_query_cursor`, and `decode_query_cursor` implement `kq1.<view>:<digest>:<offset>` continuation cursors, returning descriptive errors on prefix, format, view, or scope/tree digest mismatch.
- `fit_slice_in_budget` binary-searches the longest item prefix fitting `budget_tokens` via `response_tokens`, guaranteeing at least one item per non-empty page so pagination strictly advances; `estimate_total_pages` computes exact page counts using the same packer.

## Relationships

- Called by `application/knowledge_impact.py`, `application/knowledge_search.py`, and `application/knowledge_reader/records_batch.py`.
- Depends on `application/knowledge_currentness.py::Currentness`, `application/knowledge_paging/threshold.py::response_tokens`, and `memory/knowledge_index` (`KnowledgeIndex`, `RecordStanding`).

## Evidence

- `trim_statement` caps statements at `STATEMENT_WORD_CAP` (`80` words) and appends a `records <ID>` pointer. [1]
- `anchor_counts` and standing helpers compute current/stale/unverifiable totals and pipe-delimited standing tags. [2]
- `resolve_indexed_paths` resolves exact and unique-suffix paths against indexed entries and reports unmatched inputs. [3]
- `decode_query_cursor` validates `kq1.<view>:<digest>:<offset>` prefix, syntax, view, and scope/tree digest. [4]
- `fit_slice_in_budget` binary-searches token-bounded page slices with guaranteed progress and exact page estimation. [5]
