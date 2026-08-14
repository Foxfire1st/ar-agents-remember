# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/upscrollAnchor.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/upscrollAnchor.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The upscroll-anchor suite split from `renderer.test.tsx` by the 260731-EFA-L8 test
split. Pins the B3 upscroll anchor preservation: the reader's visible row survives
older-page prepends and measurement changes.

## Code Commentary

### Logic

Prepends older pages while the reader is scrolled up and asserts the anchored row
stays at the same visual position.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

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
| The upscroll-anchor suite. | `describe` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/upscrollAnchor.test.tsx:8-120 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  upscroll-anchor suite split from `renderer.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
