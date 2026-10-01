# dashboard/src/panels/sprint-graph/styles.ts

## Governing Overview

[sprint-graph overview](overview.md)

## Purpose

The sprint graph wave-grid layout (260815-DAG-L12 R2/R6): at most 3 boxes per row before
wrapping on wide screens, collapsing to a single wave-ordered column on narrow/phone
viewports. The two declarative layout objects are exported so tests can pin the responsive
contract (jsdom cannot evaluate media queries or `ch` units).

## Code Commentary

### Logic

- `waveGridStyles`: `display: grid; grid-template-columns: repeat(3, minmax(0, 1fr))` with
  an `@media (max-width: 720px)` override to `1fr` — the ≤3-boxes-per-row and narrow
  single-column contract, exported as a plain object.
- `leafLineStyles`: one ellipsized leaf line whose visible character range grows with the
  viewport — `maxWidth: min(100%, 30ch)` base, stepped up to `48ch` at `sm` and `72ch` at
  `lg` (Panda CSS breakpoints); exported so tests pin the ch-based growth.
- The remaining exports are Panda `css()`/`cva()` tokens: `graph` (column flex),
  `wave`/`waveHead`, `waveGrid`, `box`/`boxHead`/`boxTitle`, the `frontier` cva
  (landed/ready/waiting/in-flight/abandoned color variants), `leaves`/`leafLine`, `lump`, and
  `preds`/`pred`.

### Conventions

- Export the declarative style objects (`waveGridStyles`, `leafLineStyles`) for test
  pinning; the memoized component consumes them through `css(...)`.

### Invariants And Boundaries

- Narrow layout preserves box grouping and predecessor info; only the column count changes.
- No layout algorithm, no canvas, no library dependency — the documented L12-R3 fallback.

### Todos

None.

## Evidence

### Repo-Internal References

- The responsive grid contract (≤3 per row, narrow single column). [1]
- The ellipsized, viewport-growing leaf line contract. [2]
- The frontier-state color variants, including the `abandoned` dormant tone the projection can serve. [3]
- The component consuming these styles. [4]
- The responsive-contract forcing tests. [5]

### Cross-Repo References

No cross-repository implementation source governs this file.
