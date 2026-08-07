# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/intentLock.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/intentLock.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The intent-lock suite split from `renderer.test.tsx` by the 260731-EFA-L8 test
split. Pins the B3 intent lock, follow-on-growth, and latest-chip behavior of the
timeline.

## Code Commentary

### Logic

Asserts that streamed growth follows the live bottom only while the user intent is
locked to bottom, and that the latest chip remains reachable.

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
| The intent-lock suite. | `describe` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/intentLock.test.tsx:8-120 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  intent-lock suite split from `renderer.test.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
