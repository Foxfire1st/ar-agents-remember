# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/styles.ts

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The Panda CSS recipes of the Conversation Timeline, extracted from
`ConversationTimeline.tsx` by the 260731-EFA-L8 split. Owns the viewport well,
feed inner column, row shell, latest chip, older bar, and the collapsed unknown-run
gutter styles.

## Code Commentary

### Logic

`viewport` carries the FB7 terminal well (`background: well` + grid border +
radius + horizontal inset); `feedInner` centers a `maxWidth:100ch` column;
`rowShell` uses line-grid spacing without per-article hairlines; the run rows render
the dim mono gutter line.

### Conventions

Tokens only; the feed stays virtualizer-safe (no per-row heavy styling).

### Invariants And Boundaries

`latestChip` remains outside the scroller so it stays reachable.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The feed viewport/row recipes. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
