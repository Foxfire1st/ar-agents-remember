# mcp/src/agents_remember/memory_quality/style/citations/cells.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Parse the table citation form ``| Finding | Anchor | Source |``.

## Code Commentary

### Logic

Module-level surface:

- `CitationTable` (class, lines 24-36) — One table this check claims, whether or not it is in the current format.
- `parse_row` (function, lines 39-48)
- `scan_tables` (function, lines 51-53) — Parse every GFM table once for reuse by citation checks.
- `table_lines` (function, lines 56-64) — Every zero-based line index a table occupies -- what :mod:`prose` must not read.
- `citation_tables` (function, lines 67-101) — Every evidence table in one document, current format or not.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `CitationTable` (lines 24-36) — One table this check claims, whether or not it is in the current format.. [1]
- Defines the function `parse_row` (lines 39-48). [2]
- Defines the function `scan_tables` (lines 51-53) — Parse every GFM table once for reuse by citation checks.. [3]
- Defines the function `table_lines` (lines 56-64) — Every zero-based line index a table occupies -- what :mod:`prose` must not read.. [4]
- Defines the function `citation_tables` (lines 67-101) — Every evidence table in one document, current format or not.. [5]
