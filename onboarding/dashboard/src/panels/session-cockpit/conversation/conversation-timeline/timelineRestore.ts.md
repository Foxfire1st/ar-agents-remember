# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineRestore.ts

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The view-switch scroll-restore machinery of the Conversation Timeline, extracted
from `ConversationTimeline.tsx` by the 260731-EFA-L8 split. `useRestoreArm`,
`useRestoreApply`, and `useRestoreDriver` arm, apply, and drive restores until honest
geometry can contain them.

## Code Commentary

### Logic

The driver waits for stable frames, ignores box-less/clamp-echo events, and lets
trusted user input cancel any pending restore. `RESTORE_DRIVE_MAX_MS` bounds the
drive.

### Conventions

Restore intent is per-session `{scrollTop, atBottom}`.

### Invariants And Boundaries

A restore must never fight the user: input cancels it.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The restore hooks. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
