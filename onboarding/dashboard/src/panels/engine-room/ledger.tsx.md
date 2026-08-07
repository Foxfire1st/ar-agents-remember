# dashboard/src/panels/engine-room/ledger.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/ledger.tsx`               |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The warp-coupler entry point with ledger popover wiring. | `WarpCoupler` | dashboard/src/panels/engine-room/ledger.tsx:210-282 |
| The ledger popover/table internals. | `LedgerPopover`; `LedgerTable` | dashboard/src/panels/engine-room/ledger.tsx:31-88; dashboard/src/panels/engine-room/ledger.tsx:148-209 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the new
  ledger module extracted from `EnclosureCanvas.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
