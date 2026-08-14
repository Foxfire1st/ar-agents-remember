# mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Locate Markdown code spans, fences, and table-cell boundaries.

## Code Commentary

### Logic

Module-level surface:

- `backtick_runs` (function, lines 20-37) — Every maximal run of backticks, as ``(start, length)``.
- `code_span_ranges` (function, lines 40-63) — Half-open ``(start, end)`` ranges covering each code span, delimiters included.
- `cell_boundaries` (function, lines 66-83) — Indexes of the pipes that divide this line into table cells.
- `enclosing_span_end` (function, lines 86-90)
- `cell_spans` (function, lines 93-116) — Where each cell of a table row sits, with GFM's optional outer pipes removed.
- `split_row` (function, lines 119-121) — The cells of a table row, stripped.
- `fence_delimiter` (function, lines 124-140) — ``(character, length)`` if this line opens or closes a fenced code block.
- `unfenced_lines` (function, lines 143-164) — ``(zero-based index, line)`` for every line outside a fenced code block.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `backtick_runs` (lines 20-37) — Every maximal run of backticks, as ``(start, length)``.. | `backtick_runs` | mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py:20-37 |
| Defines the function `code_span_ranges` (lines 40-63) — Half-open ``(start, end)`` ranges covering each code span, delimiters included.. | `code_span_ranges` | mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py:40-63 |
| Defines the function `cell_boundaries` (lines 66-83) — Indexes of the pipes that divide this line into table cells.. | `cell_boundaries` | mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py:66-83 |
| Defines the function `enclosing_span_end` (lines 86-90). | `enclosing_span_end` | mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py:86-90 |
| Defines the function `cell_spans` (lines 93-116) — Where each cell of a table row sits, with GFM's optional outer pipes removed.. | `cell_spans` | mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py:93-116 |
| Defines the function `split_row` (lines 119-121) — The cells of a table row, stripped.. | `split_row` | mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py:119-121 |
| Defines the function `fence_delimiter` (lines 124-140) — ``(character, length)`` if this line opens or closes a fenced code block.. | `fence_delimiter` | mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py:124-140 |
| Defines the function `unfenced_lines` (lines 143-164) — ``(zero-based index, line)`` for every line outside a fenced code block.. | `unfenced_lines` | mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py:143-164 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
