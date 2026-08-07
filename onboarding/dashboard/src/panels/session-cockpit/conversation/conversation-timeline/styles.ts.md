# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/styles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/styles.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The feed viewport/row recipes. | `viewport`; `feedInner`; `rowShell`; `latestChip` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/styles.ts:5-104 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the styles
  module extracted from `ConversationTimeline.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
