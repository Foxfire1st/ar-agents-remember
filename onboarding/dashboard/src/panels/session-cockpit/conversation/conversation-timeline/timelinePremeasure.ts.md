# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelinePremeasure.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelinePremeasure.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The initial-measurement premeasure hooks of the Conversation Timeline, extracted
from `ConversationTimeline.tsx` by the 260731-EFA-L8 split. Owns the stored
measurement read, premeasure eligibility, sliced premeasure batches, completion, and
width invalidation.

## Code Commentary

### Logic

`useStoredMeasurements` loads the cache; `usePremeasureEligibility` decides whether
premeasure applies; `usePremeasureSync`/`usePremeasureSlice` drive the batched
measure pass; `usePremeasureCompletion` marks completion; `useMeasurementWidthInvalidation`
invalidates when the panel width changes.

### Conventions

Batches stay bounded (`INITIAL_PREMEASURE_BATCH_ROWS`) so first paint is not blocked.

### Invariants And Boundaries

Premeasure must not change rendered content; it only feeds the measurement cache.

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
| The premeasure hooks. | `useStoredMeasurements`; `usePremeasureSlice`; `usePremeasureCompletion` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelinePremeasure.ts:25-39; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelinePremeasure.ts:115-156; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelinePremeasure.ts:157-193 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  premeasure module extracted from `ConversationTimeline.tsx`. Verification pinned
  to the leaf base until closeout stamps the code commit.
