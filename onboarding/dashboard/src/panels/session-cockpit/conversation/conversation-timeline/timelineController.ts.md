# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineController.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineController.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The data/effect orchestration of the Conversation Timeline, extracted from
`ConversationTimeline.tsx` by the 260731-EFA-L8 split. `useTimelineData` prepares
the feed rows and metadata; `useTimelineEffects` wires the scroll/follow/restore
effects into the component.

## Code Commentary

### Logic

`useTimelineData` folds the conversation items into display rows with stable item
keys; `useTimelineEffects` composes the ref-keyed scroll listener (attach-once,
handler via ref mirror), the follow-on-growth effect, and the restore machinery.

### Conventions

Hook composition stays here; rendering stays in `timelineFeed.tsx`.

### Invariants And Boundaries

Effects must keep the stable `TimelineRefs` object; the listener attaches once.

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
| The controller hooks. | `useTimelineData`; `useTimelineEffects` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineController.ts:44-131; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineController.ts:133-165 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  controller module extracted from `ConversationTimeline.tsx`. Verification pinned
  to the leaf base until closeout stamps the code commit.
