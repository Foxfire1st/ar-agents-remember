# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineControls.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineControls.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The virtualizer and keyboard-control hooks of the Conversation Timeline, extracted
from `ConversationTimeline.tsx` by the 260731-EFA-L8 split. `useTimelineFocus` keeps
the focused/default-last article mounted; `useTimelineVirtualizer` builds the
`@tanstack/react-virtual` instance; `useTimelineControls` owns the widget-scoped
keyboard navigation.

## Code Commentary

### Logic

`handleTimelineKeyDown` implements the scroll-key contract and `ownsHomeEnd`
deferral for labeled overflow regions. Home/End defer to labeled regions/selections;
ArrowDown is not an operator scroll key.

### Conventions

Keyboard nav is widget-scoped and printable-suppression-safe.

### Invariants And Boundaries

A tabbable article is always mounted (focused or default-last) so keyboard users
never skip the feed.

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
| The virtualizer and keyboard hooks. | `useTimelineVirtualizer`; `useTimelineControls` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineControls.ts:37-107; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/timelineControls.ts:150-216 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  controls module extracted from `ConversationTimeline.tsx`. Verification pinned to
  the leaf base until closeout stamps the code commit.
