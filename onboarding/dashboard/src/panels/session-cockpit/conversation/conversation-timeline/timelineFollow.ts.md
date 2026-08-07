# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineFollow.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineFollow.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The follow/prepend/anchor hooks. | `useFollowLayout`; `usePrependAnchor`; `useMeasureAnchorCommit` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineFollow.ts:54-84; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineFollow.ts:159-210; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineFollow.ts:282-320 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  follow/anchor module extracted from `ConversationTimeline.tsx`. Verification
  pinned to the leaf base until closeout stamps the code commit.
