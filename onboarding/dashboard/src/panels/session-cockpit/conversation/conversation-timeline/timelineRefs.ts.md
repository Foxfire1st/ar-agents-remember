# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineRefs.ts

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The shared ref container of the Conversation Timeline, extracted from
`ConversationTimeline.tsx` by the 260731-EFA-L8 split. `TimelineRefs` holds the
viewport/scroll refs and mirrors; `useTimelineRefs` builds the stable memoized object
the effects and controls share.

## Code Commentary

### Logic

The stable object prevents effect re-subscription: the scroll listener attaches once
and reads the latest handler through the ref mirror.

### Conventions

Refs are created once per component lifetime.

### Invariants And Boundaries

The container must stay stable across renders; never rebuilt per keystroke.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The stable ref container. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
