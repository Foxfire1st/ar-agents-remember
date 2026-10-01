# mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py

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
- `fence_delimiter` (re-export from `kernel/onboarding_doc.py`) — ``(character, length)`` if this line opens or closes a fenced code block.
- `unfenced_lines` (re-export from `kernel/onboarding_doc.py`) — ``(zero-based index, line)`` for every line outside a fenced code block.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the function `backtick_runs` (lines 20-37) — Every maximal run of backticks, as ``(start, length)``.. [1]
- Defines the function `code_span_ranges` (lines 40-63) — Half-open ``(start, end)`` ranges covering each code span, delimiters included.. [2]
- Defines the function `cell_boundaries` (lines 66-83) — Indexes of the pipes that divide this line into table cells.. [3]
- Defines the function `enclosing_span_end` (lines 86-90). [4]
- Defines the function `cell_spans` (lines 93-116) — Where each cell of a table row sits, with GFM's optional outer pipes removed.. [5]
- Defines the function `split_row` (lines 119-121) — The cells of a table row, stripped.. [6]
- Re-exports the kernel `fence_delimiter` helper used for fenced scanning. [7]
- Re-exports the kernel `unfenced_lines` helper used for fence-aware scanning. [8]
