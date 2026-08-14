# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineScroll.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineScroll.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The scroll geometry, listener, and trusted-input hooks of the Conversation Timeline,
extracted from `ConversationTimeline.tsx` by the 260731-EFA-L8 split.

## Code Commentary

### Logic

`useScrollGeometry` tracks scrollTop/atBottom and measurement boxes;
`useScrollListener` attaches the ref-keyed listener once; `useTrustedInput` records
operator-owned wheel/touch/pointer/scroll events so programmatic clamps never cancel
a user's scroll. `scrollEchoAllowed` filters clamp echoes.

### Conventions

Listeners read the latest handler through the ref mirror.

### Invariants And Boundaries

ArrowDown is deliberately absent from operator scroll handling (the surface hijacks
it into the agents line).

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
| The scroll hooks. | `useScrollGeometry`; `useScrollListener`; `useTrustedInput` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineScroll.ts:91-190 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the scroll
  module extracted from `ConversationTimeline.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
