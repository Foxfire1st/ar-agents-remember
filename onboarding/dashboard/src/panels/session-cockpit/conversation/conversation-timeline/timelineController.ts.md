# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineController.ts

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The data/effect orchestration of the Conversation Timeline, extracted from
`ConversationTimeline.tsx` by the 260731-EFA-L8 split. `useTimelineData` prepares
the feed rows and metadata; `useTimelineEffects` wires the scroll/follow/restore
effects into the component.

## Code Commentary

#

- 260731-EFA-L7 (trace delta): the controller imports and uses `groupDisplayRows` from `../collapse` for the live-thinking pipeline; the L7 live-thinking change was re-applied onto the L8 split.
## Logic

`useTimelineData` folds the conversation items into display rows with stable item
keys; `useTimelineEffects` composes the ref-keyed scroll listener (attach-once,
handler via ref mirror), the follow-on-growth effect, and the restore machinery.

### Conventions

Hook composition stays here; rendering stays in `timelineFeed.tsx`.

### Invariants And Boundaries

Effects must keep the stable `TimelineRefs` object; the listener attaches once.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The controller hooks. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
