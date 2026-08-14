# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineFeed.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineFeed.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The virtualized feed renderer of the Conversation Timeline, extracted from
`ConversationTimeline.tsx` by the 260731-EFA-L8 split. `TimelineFeed` renders the
`role="feed"` viewport with honest `aria-posinset`/`aria-setsize`, the row shell,
older bar, latest chip, and the article dispatch.

## Code Commentary

#

- 260731-EFA-L7 (trace delta): the feed carries the `ThinkingItem` import, the "thinking in progress" label branch, and the `<ThinkingItem item={row.item} animated />` render branch for the coalesced live indicator.
## Logic

`FeedSurface`/`FeedViewport` host the virtualizer; `FeedRow` renders one display row
(message, thinking, tool, turn result, or collapsed unknown-vendor run);
`LatestChip` stays outside the scroller. `FeedArticle` owns the stable accessible
name and `aria-live="off"` for streaming rows.

### Conventions

Virtualization keys on the stable item; DOM stays bounded.

### Invariants And Boundaries

`aria-posinset` is the server ordinal; `aria-setsize` appears only with an honest
total.

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
| The feed renderer entry. | `TimelineFeed` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineFeed.tsx:260-331 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 curator (trace delta): body verified against the current code and updated (260731-EFA-L7 (trace delta): the feed carries the `ThinkingItem` import, the "thinking in progress" ...). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: the L7 live-thinking re-application onto the L8 split: carries the `ThinkingItem` import, the "thinking in progress" label branch, and the `<ThinkingItem item={row.item} animated />` render branch. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the feed
  module extracted from `ConversationTimeline.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
