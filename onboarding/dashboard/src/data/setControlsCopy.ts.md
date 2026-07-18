# dashboard/src/data/setControlsCopy.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setControlsCopy.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Central copy source for set waiting, acceptance, clamp, queue, route, promotion, cycling, and
session-transition messages.

## Code Commentary

### Logic

Formats every chip and live-region sentence from typed inputs. Clamp copy retains requested and
effective values; unsupported and route failures preserve server detail; route retry wording is
limited to retryable outages; session failure and awaiting-input messages name the seat label.

### Conventions

Acceptance words are literal visible text, never color-only semantics. Copy functions are pure so
header chips, toasts, and announcements cannot drift into competing vocabularies.

### Invariants And Boundaries

The module presents evidence but never classifies it; reducers and route classifiers own that
decision. Requested and effective values remain distinct in every relevant sentence.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Shared copy and announcement formatters. | L1-L127 | [setControlsCopy.ts](setControlsCopy.ts) |
| Presentation-model consumer. | L1-L232 | [setChips.ts](setChips.ts) |
| I/O and live-region consumer. | L1-L433 | [setClient.ts](setClient.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R4/R5/R8 after final reviewer PASS.
  Verification metadata is pinned to the contract base until the code commit exists.
