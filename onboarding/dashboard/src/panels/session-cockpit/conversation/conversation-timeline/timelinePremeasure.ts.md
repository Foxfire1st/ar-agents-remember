# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelinePremeasure.ts

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The premeasure hooks. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
