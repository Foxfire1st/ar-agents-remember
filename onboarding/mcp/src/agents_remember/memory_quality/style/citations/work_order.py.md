# mcp/src/agents_remember/memory_quality/style/citations/work_order.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Group declined citation repairs into one work order per document.

## Code Commentary

### Logic

Module-level surface:

- `Item` (class, lines 18-45) — One declined citation and the edit that clears it.
- `orders` (function, lines 48-67) — One entry per document, in tree order, each holding its own items in line order.
- `counted` (function, lines 70-75) — Every decline reason with its count, worst first -- the complete list (L6-R15).

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Item` (lines 18-45) — One declined citation and the edit that clears it.. [1]
- Defines the function `orders` (lines 48-67) — One entry per document, in tree order, each holding its own items in line order.. [2]
- Defines the function `counted` (lines 70-75) — Every decline reason with its count, worst first -- the complete list (L6-R15).. [3]
