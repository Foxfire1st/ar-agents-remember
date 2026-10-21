# dashboard/src/panels/review/reading/readerLine.test-utils.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Provide deterministic column layout, scroll and frame observations for reader-line tests.

## Code Commentary

### Logic

ColumnLayout replaces DOM rectangles and column scroll dimensions with ordered declared blocks, whole-pixel clamping, min-height held-box room and side-by-side children. Mutation-aware reads invalidate its cached layout, and an optional watch hook observes commit-time reads. Helpers drive wheel/scroll events, advance the gesture clock, sample animation callbacks after fixed microtask turns, and mount useReaderAnchor in a bare column. Editor helpers supply document-line lookup and a growable line-3 spacer widget.

### Invariants And Boundaries

This is the geometry/clock model used by its callers, not browser layout or a source of passed assertions itself. Callers own the selected block heights, supplied DOM, fixture changes and restoration of global spies.

## Evidence

- ColumnLayout supplies ordered-block geometry, held rooms and rounded/clamped scroll dimensions. [4]
- Scroll, clock, frame-sampling and anchored-column helpers drive controlled observations. [5]
- Editor document-line lookup and growable spacer support editor-specific cases. [6]
