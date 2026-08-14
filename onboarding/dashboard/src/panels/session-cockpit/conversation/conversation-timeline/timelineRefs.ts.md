# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineRefs.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineRefs.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The stable ref container. | `TimelineRefs`; `useTimelineRefs` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineRefs.ts:5-60 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the refs
  module extracted from `ConversationTimeline.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
