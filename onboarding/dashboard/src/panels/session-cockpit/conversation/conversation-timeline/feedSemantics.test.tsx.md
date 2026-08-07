# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/feedSemantics.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/feedSemantics.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The feed-semantics suite. | `describe` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/feedSemantics.test.tsx:7-7 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  feed-semantics suite split from `renderer.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
