# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/test-utils.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/test-utils.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The shared conversation-item fixture builder for the split timeline test files,
extracted from `renderer.test.tsx` by the 260731-EFA-L8 split. `msg` builds a typed
`ConversationItem` with the required `itemId`/`globalOrdinal`.

## Code Commentary

### Logic

`msg` fills required wire fields with typed overrides, so the split suites author
feed rows through one typed factory.

### Conventions

Test-only; typed through the conversation wire types.

### Invariants And Boundaries

Never imported by production code.

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
| The shared item builder. | `msg` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/test-utils.tsx:17-29 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the shared
  test fixture extracted from `renderer.test.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
