# mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Resolve every exact anchor location through one immutable source snapshot index.

## Code Commentary

### Logic

Module-level surface:

- `Location` (class, lines 32-40) — One range in one file that satisfies an anchor.
- `Sightings` (class, lines 44-78) — Where one anchor exists in the code tree, and how much of it fitted.
- `_Batch` (class, lines 82-106) — One anchor's accumulating result while the walk is in progress.
- `locate` (function, lines 109-122) — Every location from the shared snapshot index, preserving direct-resolver order.
- `_located` (function, lines 125-133)
- `locate_uncached` (function, lines 136-144) — Direct source resolver retained as the semantic parity oracle for the index.
- `walk` (function, lines 147-154) — Every readable code file, with the path text a ``Source`` would spell it as.
- `_visit` (function, lines 157-167) — Record every anchor this one file holds, reading and deriving it at most once.
- `described` (function, lines 170-182) — The tree-wide half of a finding: every location, or the fact that there are none.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Location` (lines 32-40) — One range in one file that satisfies an anchor.. [1]
- Defines the class `Sightings` (lines 44-78) — Where one anchor exists in the code tree, and how much of it fitted.. [2]
- Defines the class `_Batch` (lines 82-106) — One anchor's accumulating result while the walk is in progress.. [3]
- Defines the function `locate` (lines 109-122) — Every location from the shared snapshot index, preserving direct-resolver order.. [4]
- Defines the function `_located` (lines 125-133). [5]
- Defines the function `locate_uncached` (lines 136-144) — Direct source resolver retained as the semantic parity oracle for the index.. [6]
- Defines the function `walk` (lines 147-154) — Every readable code file, with the path text a ``Source`` would spell it as.. [7]
- Defines the function `_visit` (lines 157-167) — Record every anchor this one file holds, reading and deriving it at most once.. [8]
- Defines the function `described` (lines 170-182) — The tree-wide half of a finding: every location, or the fact that there are none.. [9]
