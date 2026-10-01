# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineFeed.tsx

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The feed renderer entry. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
