# mcp/src/agents_remember/memory_quality/style/citations/cells.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Parse the anchor/source cells of the `Finding | Anchor | Source` form shared by conversion and converted card authoring.

## Code Commentary

### Logic

Module-level surface:


- `parse_row` (function, lines 28-37)




### Conventions

`unescaped` resolves only GFM escaped pipes (`\|`) to literal pipes before model parsing; all other backslashes remain content. `parse_row` records anchors, sources, malformed source segments and unchecked code spans in a Claim shared by conversion/authoring. It performs no citation-table discovery walk.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.


- parse_row unescapes GFM pipes and parses anchor/source cells for conversion and converted card authoring. [2]
