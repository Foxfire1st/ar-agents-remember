# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory1.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory1.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The first scroll-memory suite split from `renderer.test.tsx` by the 260731-EFA-L8
test split. Pins the F-ac scroll-memory matrix: middle/top and bottom restoration,
later inflow at bottom, geometry settling, and the persistent latest control.

## Code Commentary

### Logic

Uses the describe-scoped geometry shim (`scrollMemory.test-utils.tsx`) to drive
restore scenarios deterministically.

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
| The scroll-memory suite. | `describe` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory1.test.tsx:12-220 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the first
  scroll-memory suite split from `renderer.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
