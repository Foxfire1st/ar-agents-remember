# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineController.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineController.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                  |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `../overview.md`                                            |

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

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 curator (trace delta): body verified against the current code and updated (260731-EFA-L7 (trace delta): the controller imports and uses `groupDisplayRows` from `../collapse` f...). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: the L7 live-thinking re-application onto the L8 split: imports and uses `groupDisplayRows` from `../collapse` for the timeline row pipeline. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  controller module extracted from `ConversationTimeline.tsx`. Verification pinned
  to the leaf base until closeout stamps the code commit.
