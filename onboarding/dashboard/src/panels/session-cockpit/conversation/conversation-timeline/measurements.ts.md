# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/measurements.ts

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The measurement constants and persisted-measurement cache of the Conversation
Timeline, extracted from `ConversationTimeline.tsx` by the 260731-EFA-L8 split. Owns
`OPERATOR_SCROLL_KEYS`, the premeasure limits, the measurement cache read/write, and
the restore drive bound.

## Code Commentary

### Logic

`readStoredMeasurements` / `storeMeasurements` persist per-cache-id row measurements
under the `cockpit.chats.measurements.v1:` prefix. `OPERATOR_SCROLL_KEYS` deliberately
excludes ArrowDown because the conversation surface hijacks it into the agents line.

### Conventions

Pure storage helpers; no DOM.

### Invariants And Boundaries

The scroll-key set is exported for the keyboard-contract tests; adding ArrowDown back
would break the surface contract.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The measurement cache and constants. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
