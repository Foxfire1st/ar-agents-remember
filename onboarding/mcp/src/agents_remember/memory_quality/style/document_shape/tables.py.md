# mcp/src/agents_remember/memory_quality/style/document_shape/tables.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Report Markdown table rows whose cell count differs from the header.

## Code Commentary

### Logic

Module-level surface:

- `Row` (class, lines 36-41) — One line of a candidate table: where it was, and how many cells it holds.
- `check_onboarding_root` (function, lines 44-52)
- `check_file` (function, lines 55-60)
- `rows_of` (function, lines 63-66)
- `tables` (function, lines 69-86) — Every GFM table in the file, as its header row and its body rows.
- `starts_table` (function, lines 89-96)
- `read_body` (function, lines 99-112)
- `ragged_findings` (function, lines 119-141)
- `ragged_message` (function, lines 144-168) — Return the complete repair for a short or long table row.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Row` (lines 36-41) — One line of a candidate table: where it was, and how many cells it holds.. [1]
- Defines the function `check_onboarding_root` (lines 44-52). [2]
- Defines the function `check_file` (lines 55-60). [3]
- Defines the function `rows_of` (lines 63-66). [4]
- Defines the function `tables` (lines 69-86) — Every GFM table in the file, as its header row and its body rows.. [5]
- Defines the function `starts_table` (lines 89-96). [6]
- Defines the function `read_body` (lines 99-112). [7]
- Defines the function `ragged_findings` (lines 119-141). [8]
- Defines the function `ragged_message` (lines 144-168) — Return the complete repair for a short or long table row.. [9]
