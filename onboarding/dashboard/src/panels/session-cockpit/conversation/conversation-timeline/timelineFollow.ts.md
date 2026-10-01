# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineFollow.ts

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The bottom-follow, streamed-growth, prepend-anchor, and measurement-anchor hooks of
the Conversation Timeline, extracted from `ConversationTimeline.tsx` by the
260731-EFA-L8 split.

## Code Commentary

### Logic

`useFollowLayout` keeps the feed pinned to the live bottom; `useStreamedGrowthCount`
and `useFollowOnGrowth` handle follow-on growth; `usePrependAnchor` preserves the
reader's visible row across older-page prepends; `useMeasureAnchor` /
`useMeasureAnchorCommit` keep measurement anchors stable during virtual-row size
changes.

### Conventions

Follow/restore intent is explicit and cancellable by trusted user input.

### Invariants And Boundaries

Restores arm only until honest geometry can contain them; user input cancels any
pending restore.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The follow/prepend/anchor hooks. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
