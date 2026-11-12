# dashboard/src/panels/engine-room/ledger.tsx

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

The memory-ledger warp coupler and its popover table, extracted from
`EnclosureCanvas.tsx` by the 260731-EFA-L8 responsibility split. `WarpCoupler`
renders the code ⇄ memory hash-pair link between worktree columns and opens the
`memory.md` ledger lookup popover (`LedgerPopover` / `LedgerTable`).

## Code Commentary

### Logic

`WarpCoupler` takes the coupler's visible/bound state, ledger rows, and current code
hash. `LedgerPopover` renders the compact card with the highlighted current row, the
"show N more" expand control, and the "+N more in memory.md" footer; `LedgerTable`
builds the mirrored six-column row (date · message · code-hash ⇄ memory-hash ·
message · date).

### Conventions

The coupler label is a real button (`ledgerButton`) with `pointerEvents:none` on the
label text. Hash pairs are mono, aligned to the centre seam.

### Invariants And Boundaries

The popover only reads rows the observer I/O layer provided; it never queries git
itself. Rows absent from the window fall back to the bounded footer count.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The warp-coupler entry point with ledger popover wiring. [1]
- The ledger popover/table internals. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
