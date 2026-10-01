# dashboard/src/panels/sprint-graph/SprintGraphView.test.tsx

## Governing Overview

[sprint-graph overview](overview.md)

## Purpose

Component forcing suite for the sprint graph wave-grid view (260815-DAG-L12 R2/R6/R7): the
zero-edge graph and segmented-master scenarios that route review requires as mounted-UI
evidence, plus the frontier badge and the declarative responsive contracts.

## Code Commentary

### Logic

Renders real `SprintGraphView` components with @testing-library: a zero-edge graph renders
one wave row of independent boxes with no predecessor labels (an atomic master renders as
the lump); a segmented master renders across three wave rows with labeled edge reasons
(`← Master One — OM1's early segment lands before the atomic block`); each box exposes
`data-frontier` for the frontier badge; the grid and narrow single-column declarations are
pinned against the exported `waveGridStyles` (jsdom cannot evaluate media queries); and the
ellipsized leaf line's ch-based growth is pinned against `leafLineStyles`.

### Invariants And Boundaries

- Renders mounted components — projection-only assertions are insufficient for the L12-R7
  rendering requirements.
- jsdom limitations are worked around by exporting and asserting the declarative style
  objects rather than computed layout.

## Evidence

### Repo-Internal References

- The component forcing suite. [1]
- The component under test. [2]
- The style contracts asserted. [3]

### Cross-Repo References

No cross-repository implementation source governs this file.
