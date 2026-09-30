# dashboard/src/panels/review/intentMarkerScope.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/intentMarkerScope.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The marker scope's reads and inventory rule (2 cases; review R1 F4 N11, F5, and the review R2 gap).** The real scope
through `renderHook`, with `fetch` the only stand-in, answered with the real `notes.py` classification of the scratch
leaf (`markerReturn.file.captured.json`).

## Code Commentary

### Logic

- **Case 1.** An unlisted path is never asked about (`classify` returns `null`, no request); a listed one is asked once,
  with `file=` and `comparison=`; a second `classify` shares the pending answer, and `peek` holds it once settled.
- **Case 2.** `markerInventory` counts an inventory as partial when it is `partial` or not `measured` at all, and lists
  its paths.

### Conventions

- `renderHook` over `useIntentMarkerScope` with recording moves.

### Invariants And Boundaries

- Pins the changed-path gate (mutation N11) and the partial rule (R2-7).

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One read per listed path per surface; none for an unlisted path. | "classifies a listed path once per surface, and never an unlisted one" | dashboard/src/panels/review/intentMarkerScope.test.ts:22-60 |
| A partial or unmeasured inventory is partial. | "counts an inventory that is partial, or not measured at all, as partial (review R2)" | dashboard/src/panels/review/intentMarkerScope.test.ts:62-76 |
| The scope under test. | `markerInventory`; `useIntentMarkerScope` | dashboard/src/panels/review/intentMarkerScope.ts:66-129 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new scope test module MIK-R34 adds (2 cases), recording review R1 F4 (N11) and F5 and the review R2 gap. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
