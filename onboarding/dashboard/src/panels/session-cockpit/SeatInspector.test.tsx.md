# dashboard/src/panels/session-cockpit/SeatInspector.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SeatInspector.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T08:33+02:00                           |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786`       |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom SeatInspector suite: L6 archetype/residual/raw-interaction facts plus FEUI-L4's
collapsible set-ledger, explicit-view acknowledgment, and seat-switch isolation.

## Code Commentary

### Logic

- **Archetype fact (R1)** (L19-L28): controlled seats say "runner line-log", legacy raw "vendor
  TUI" (`inspector-archetype`).
- **Retire residual (R5)** (L30-L42): `L6_RETIRED_WITH_STOP_ERROR` renders state `retired` (not
  failed), the stop note contains "informational" AND the verbatim server detail, and the
  lowercase text NEVER contains "fail" — the residual-honesty regression net.
- **Raw payload (R4)** (L44-L54): `inspector-pending-interaction-raw` carries the VERBATIM
  JSON (`"kind": "vendor-custom"`, `"opaque": true`) — the unrepresentable fallback's target.
- **Set ledger (L4 R6/F22)** (L58-L144): rendering alone does not acknowledge; expansion does.
  Rows render newest first with the acceptance word, requested/effective split, detail, and
  unacknowledged word. Switching seats remounts the new seat collapsed without acknowledging it;
  the pure line formatter also pins unsupported wording.

### Invariants And Boundaries

Catalog sections remain fixture-driven; the L4 ledger cases use the real cockpit store to prove
the intentional acknowledgment side effect and per-seat reset. Test-only.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The card under test (ledger, archetype fact, stop note, raw payload). | L49-L218 | [SeatInspector.tsx](SeatInspector.tsx) |
| The retired-with-stop-error + unrepresentable fixtures. | L243-L280 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The archetype/residual copy asserted against. | L29-L32, L80-L84 | [lifecycleCopy.ts](lifecycleCopy.ts) |

## Update History

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R6/F22 added ledger expansion-as-viewing,
  newest-first requested/effective lines, explicit unacknowledged wording, and a seat-switch
  regression proving the next seat stays collapsed and unacknowledged. Verification metadata is
  pinned to the contract base until code commit.
- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 (R1/R4/R5): the inspector's L6 surface —
  archetype naming per seat, the informational (never "fail") retire stop note on a retired row,
  and the verbatim pending-interaction payload. Verification metadata pinned to the leaf base
  until closeout stamps the L6 code commit.
