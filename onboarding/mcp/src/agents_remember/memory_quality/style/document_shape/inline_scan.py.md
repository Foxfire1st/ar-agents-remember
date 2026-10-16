# mcp/src/agents_remember/memory_quality/style/document_shape/inline_scan.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Locate Markdown code spans, fences, and table-cell boundaries.

## Code Commentary

### Logic

`cell_boundaries` interprets escaped pipes and code spans. `cell_spans` obtains those boundaries and delegates to `cell_spans_from_boundaries`; the latter derives cell offsets from supplied positions without rescanning and preserves optional outer pipes and empty cells. Table materialization in `tables.rows_of` skips the scanner for lines without a pipe and passes one scan's positions to this helper. The no-pipe shortcut belongs to that caller, not to `cell_boundaries` itself.

The unused stripped-cell wrapper `split_row` and its export are removed. Existing Windows-cell and escaped-pipe assertion callers now use the retained cell-span path; no replacement wrapper or table interpretation is introduced. Fence helpers remain kernel re-exports.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each native symbol reference resolves its definition; no prose line-number inventory overrides that binding.


- Every maximal run of backticks is located without consulting backslash escapes. [1]


- Defines the function `code_span_ranges` — Half-open ``(start, end)`` ranges covering each code span, delimiters included. [2]


- Defines the function `cell_boundaries` — Indexes of the pipes that divide this line into table cells. [3]


- Defines the function `enclosing_span_end`. [4]


- Cell offsets preserve optional outer pipes and reuse supplied boundaries without rescanning. [5]

- Re-exports the kernel `fence_delimiter` helper used for fenced scanning. [7]
- Re-exports the kernel `unfenced_lines` helper used for fence-aware scanning. [8]

## MIK-R95 Illustrative Example Corrected

The docstring's multi-backtick example no longer claims a card location: it keeps the `ariaLabel` illustration and says only that equal-length runs make it one span, after the referenced card was removed by the same leaf. Parser logic and the historical fixture bytes are unchanged.
