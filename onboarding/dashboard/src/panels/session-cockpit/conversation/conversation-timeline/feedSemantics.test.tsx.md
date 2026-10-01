# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/feedSemantics.test.tsx

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The feed-semantics suite split from `renderer.test.tsx` by the 260731-EFA-L8 test
split (42-name set reconciled item-for-item). Pins the one navigable `role="feed"`,
server-ordinal `aria-posinset`, honest `aria-setsize`/`total unknown`, and
`aria-live="off"` streaming rows.

## Code Commentary

### Logic

Mounts a feed with known/unknown totals and asserts the ARIA honesty rules plus the
latest-chip and older-bar surfaces.

### Invariants And Boundaries

`aria-posinset` is the server ordinal, never the array index.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The feed-semantics suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
