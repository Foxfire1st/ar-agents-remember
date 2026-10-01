# mcp/src/agents_remember/memory_quality/style/citations/prose.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Parse the prose citation form ``cit:([anchors], path:start-end)``.

## Code Commentary

### Logic

Module-level surface:

- `Block` (class, lines 44-57) — One paragraph of prose, joined into a single string with its line numbers kept.
- `Superseded` (class, lines 60-66) — One citation in the old spelling: where it is and what it says.
- `ProseScan` (class, lines 69-76) — Everything one document's prose holds.
- `ProseParts` (class, lines 79-87) — The mutable accumulator one document's blocks are read into.
- `blocks` (function, lines 90-108) — Prose paragraphs: unfenced, outside any table, split at blank lines.
- `misplaced_in_tables` (function, lines 111-131) — A ``cit:`` written into a table cell -- the wrong serialisation, one report per row.
- `Parts` (class, lines 134-144) — Where a ``cit:`` body's two halves are, as offsets into that body.
- `parts` (function, lines 147-160) — ``[anchors], sources`` split into offsets, or ``None`` when it is not that shape.
- `parse_citation` (function, lines 163-176) — ``[anchors], sources`` into a claim, or ``None`` when it is not that shape.
- `scan_block` (function, lines 179-206) — Every ``cit:`` in one block, and the extent each one covers.
- `record` (function, lines 209-217)
- `anchor_extents` (function, lines 220-225) — Every code span and every quoted literal -- the two things that can anchor a range.
- `scan_anchored` (function, lines 228-240) — ``X (L47)`` and ``(X L775-L795)`` -- an anchor with a range beside it.
- `scan_bare` (function, lines 243-255) — A bare parenthesized two-endpoint range with nothing beside it: no anchor, no file, no referent.
- `scan` (function, lines 258-271) — Every citation one document's prose holds, current spelling and superseded.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Block` (lines 44-57) — One paragraph of prose, joined into a single string with its line numbers kept.. [1]
- Defines the class `Superseded` (lines 60-66) — One citation in the old spelling: where it is and what it says.. [2]
- Defines the class `ProseScan` (lines 69-76) — Everything one document's prose holds.. [3]
- Defines the class `ProseParts` (lines 79-87) — The mutable accumulator one document's blocks are read into.. [4]
- Defines the function `blocks` (lines 90-108) — Prose paragraphs: unfenced, outside any table, split at blank lines.. [5]
- Defines the function `misplaced_in_tables` (lines 111-131) — A ``cit:`` written into a table cell -- the wrong serialisation, one report per row.. [6]
- Defines the class `Parts` (lines 134-144) — Where a ``cit:`` body's two halves are, as offsets into that body.. [7]
- Defines the function `parts` (lines 149-162) — ``[anchors], sources`` split into offsets, or ``None`` when it is not that shape.. [8]
- Defines the function `parse_citation` (lines 163-176) — ``[anchors], sources`` into a claim, or ``None`` when it is not that shape.. [9]
- Defines the function `scan_block` (lines 179-206) — Every ``cit:`` in one block, and the extent each one covers.. [10]
- Defines the function `record` (lines 209-217). [11]
- Defines the function `anchor_extents` (lines 220-225) — Every code span and every quoted literal -- the two things that can anchor a range.. [12]
- Defines the function `scan_anchored` (lines 228-240) — ``X (L47)`` and ``(X L775-L795)`` -- an anchor with a range beside it.. [13]
- Defines the function `scan_bare` (lines 243-255) — ``(L126-L173)`` with nothing beside it: no anchor, no file, no referent.. [14]
- Defines the function `scan` (lines 258-271) — Every citation one document's prose holds, current spelling and superseded.. [15]
