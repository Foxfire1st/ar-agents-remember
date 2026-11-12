# dashboard/src/panels/engine-room/ledger.styles.ts

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The memory-ledger popover style domain of the Engine Room, split from
`engineRoomStyles.ts` by the 260731-EFA-L8 R6 ruling. Owns the coupler trigger
(`ledgerButton`), the popover card/table rows, the scroll expansion (`ledgerScroll`),
the show-more control, and the six-column hash-pair seam styles.

## Code Commentary

### Logic

`ledgerCard` is capped (`min(92vw, 46rem)`); `ledgerScroll` expands from a compact
13rem to `min(72vh, 46rem)` when opened. Hash cells are mono and aligned so the two
sides meet at `ledgerSeam`.

### Conventions

The trigger brightens on hover; the label carries `pointerEvents:none`. All colours
via tokens.

### Invariants And Boundaries

The popover reads windowed rows only; styles never query data.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The popover card/scroll recipes. [1]
- The six-column row/seam recipes. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
