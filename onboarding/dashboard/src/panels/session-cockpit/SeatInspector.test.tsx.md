# dashboard/src/panels/session-cockpit/SeatInspector.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SeatInspector.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom SeatInspector suite (260715-FEUI-L6 additions — the L2 card previously rode along in
the view suite): the two-archetype pane fact, the retire stop residual on a retired row, and the
raw pending-interaction payload the InteractionBar's unrepresentable fallback points at.

## Code Commentary

### Logic

- **Archetype fact (R1)** (L19-L28): controlled seats say "runner line-log", legacy raw "vendor
  TUI" (`inspector-archetype`).
- **Retire residual (R5)** (L30-L42): `L6_RETIRED_WITH_STOP_ERROR` renders state `retired` (not
  failed), the stop note contains "informational" AND the verbatim server detail, and the
  lowercase text NEVER contains "fail" — the residual-honesty regression net.
- **Raw payload (R4)** (L44-L54): `inspector-pending-interaction-raw` carries the VERBATIM
  JSON (`"kind": "vendor-custom"`, `"opaque": true`) — the unrepresentable fallback's target.

### Invariants And Boundaries

Fixture-driven over the shared L6 rows; no store/fetch dependencies (the card is read-only
catalog truth). Test-only.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The card under test (archetype fact, stop note, raw payload). | L62-L136 | [SeatInspector.tsx](SeatInspector.tsx) |
| The retired-with-stop-error + unrepresentable fixtures. | L243-L280 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The archetype/residual copy asserted against. | L29-L32, L80-L84 | [lifecycleCopy.ts](lifecycleCopy.ts) |

## Update History

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 (R1/R4/R5): the inspector's L6 surface —
  archetype naming per seat, the informational (never "fail") retire stop note on a retired row,
  and the verbatim pending-interaction payload. Verification metadata pinned to the leaf base
  until closeout stamps the L6 code commit.
