# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineControls.ts

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The virtualizer and keyboard-control hooks of the Conversation Timeline, extracted
from `ConversationTimeline.tsx` by the 260731-EFA-L8 split. `useTimelineFocus` keeps
the focused/default-last article mounted; `useTimelineVirtualizer` builds the
`@tanstack/react-virtual` instance; `useTimelineControls` owns the widget-scoped
keyboard navigation.

## Code Commentary

### Logic

`handleTimelineKeyDown` implements the scroll-key contract and `ownsHomeEnd`
deferral for labeled overflow regions. Home/End defer to labeled regions/selections;
ArrowDown is not an operator scroll key.

### Conventions

Keyboard nav is widget-scoped and printable-suppression-safe.

### Invariants And Boundaries

A tabbable article is always mounted (focused or default-last) so keyboard users
never skip the feed.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The virtualizer and keyboard hooks. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
