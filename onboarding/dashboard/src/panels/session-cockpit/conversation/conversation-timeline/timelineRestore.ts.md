# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineRestore.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineRestore.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The restore hooks. | `useRestoreArm`; `useRestoreApply`; `useRestoreDriver` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineRestore.ts:8-140 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the restore
  module extracted from `ConversationTimeline.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
