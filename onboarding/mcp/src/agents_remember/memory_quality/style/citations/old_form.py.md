# mcp/src/agents_remember/memory_quality/style/citations/old_form.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Read the superseded citation format without writing it.

## Code Commentary

### Logic

Module-level surface:

- `Span` (class, lines 32-36) — One range read out of an old document, in the file it was written about.
- `link_targets` (function, lines 39-49) — Every path this Source Path cell names, in order, however it spelled them.
- `path_candidates` (function, lines 52-72) — Every repo-relative spelling of ``target`` worth trying, most specific first.
- `_mirrored` (function, lines 75-87) — ``../src/x.ts`` read against the card's own place in the mirrored tree.
- `resolved_path` (function, lines 90-107) — The one spelling of ``target`` that names a file in either tree, or ``None``.
- `old_span` (function, lines 110-117) — The first ``L`` range in a Citations cell, as numbers. A tiebreaker, never an output.
- `verified_hint` (function, lines 120-130) — ``span`` if EVERY anchor really occurs inside it in ``path``, otherwise ``None``.
- `is_marker` (function, lines 133-135) — Whether a cell is one of the four spellings this tree uses for 'nothing to cite'.
- `marker_of` (function, lines 138-144) — The no-citation marker a table already uses, so a padded row does not invent a fifth.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Span` (lines 32-36) — One range read out of an old document, in the file it was written about.. [1]
- Defines the function `link_targets` (lines 39-49) — Every path this Source Path cell names, in order, however it spelled them.. [2]
- Defines the function `path_candidates` (lines 52-72) — Every repo-relative spelling of ``target`` worth trying, most specific first.. [3]
- Defines the function `_mirrored` (lines 75-87) — ``../src/x.ts`` read against the card's own place in the mirrored tree.. [4]
- Defines the function `resolved_path` (lines 90-107) — The one spelling of ``target`` that names a file in either tree, or ``None``.. [5]
- Defines the function `old_span` (lines 110-117) — The first ``L`` range in a Citations cell, as numbers. A tiebreaker, never an output.. [6]
- Defines the function `verified_hint` (lines 120-130) — ``span`` if EVERY anchor really occurs inside it in ``path``, otherwise ``None``.. [7]
- Defines the function `is_marker` (lines 133-135) — Whether a cell is one of the four spellings this tree uses for 'nothing to cite'.. [8]
- Defines the function `marker_of` (lines 138-144) — The no-citation marker a table already uses, so a padded row does not invent a fifth.. [9]
