# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineScroll.ts

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The scroll geometry, listener, and trusted-input hooks of the Conversation Timeline,
extracted from `ConversationTimeline.tsx` by the 260731-EFA-L8 split.

## Code Commentary

### Logic

`useScrollGeometry` tracks scrollTop/atBottom and measurement boxes;
`useScrollListener` attaches the ref-keyed listener once; `useTrustedInput` records
operator-owned wheel/touch/pointer/scroll events so programmatic clamps never cancel
a user's scroll. `scrollEchoAllowed` filters clamp echoes.

### Conventions

Listeners read the latest handler through the ref mirror.

### Invariants And Boundaries

ArrowDown is deliberately absent from operator scroll handling (the surface hijacks
it into the agents line).

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The scroll hooks. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
