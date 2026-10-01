# dashboard/src/panels/session-cockpit/conversation/conversationSurfaceParts.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The conversation-surface render parts, extracted from `ConversationSurface.tsx` by
the 260731-EFA-L8 split. Owns the projection-failed surface, toolbar, agent-history
error banner, timeline section, and the history-capability resolver.

## Code Commentary

### Logic

`SurfaceToolbar` renders the surface controls; `TimelineSection` hosts the timeline
with its slots; `resolveHistoryCapability` decides whether agent-history rendering
applies; the error banner surfaces honest history failures.

### Conventions

Presentational parts; announcements/paging stay in the surface controller.

### Invariants And Boundaries

The timeline section must keep the feed mounted per the keep-alive rules.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The surface parts. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
