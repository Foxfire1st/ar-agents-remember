# dashboard/src/panels/engine-room/ledger.styles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/ledger.styles.ts`         |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The popover card/scroll recipes. | `ledgerCard`; `ledgerScroll`; `ledgerButton` | dashboard/src/panels/engine-room/ledger.styles.ts:4-29; dashboard/src/panels/engine-room/ledger.styles.ts:54-63 |
| The six-column row/seam recipes. | `ledgerDate`; `ledgerHashCode`; `ledgerHashMem`; `ledgerSeam` | dashboard/src/panels/engine-room/ledger.styles.ts:81-95 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the ledger
  style domain split from `engineRoomStyles.ts`. Verification pinned to the leaf base
  until closeout stamps the code commit.
