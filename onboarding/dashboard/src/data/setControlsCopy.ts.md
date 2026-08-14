# dashboard/src/data/setControlsCopy.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setControlsCopy.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared copy and announcement formatters. | `setWaitingCopy`, `clampChipCopy`, `queuedChipCopy`, `setRouteErrorCopy`, `setResultAnnouncement`, `sessionAwaitingInputAnnouncement` | dashboard/src/data/setControlsCopy.ts:19-21; dashboard/src/data/setControlsCopy.ts:25-27; dashboard/src/data/setControlsCopy.ts:29-31; dashboard/src/data/setControlsCopy.ts:60-74; dashboard/src/data/setControlsCopy.ts:83-101; dashboard/src/data/setControlsCopy.ts:125-127 |
| Presentation-model consumer. | `deriveSetChips` | dashboard/src/data/setChips.ts:58-216 |
| I/O and live-region consumer. | "The set-controls driver (260715-FEUI-L4 S1/S3/S4)" | dashboard/src/data/setClient.ts:42-42 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-03T02:38:23+02:00 — W3-B04 curator: curated 3 table citations (3 total), supplying exact anchors and paths; the scoped fixer generated all final extents.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R4/R5/R8 after final reviewer PASS.
  Verification metadata is pinned to the contract base until the code commit exists.
