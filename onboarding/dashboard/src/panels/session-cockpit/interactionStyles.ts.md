# dashboard/src/panels/session-cockpit/interactionStyles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/interactionStyles.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The Panda CSS recipes for the structured-interaction surface, extracted from
`InteractionBar.tsx` by the 260731-EFA-L8 split. Owns the bar, head row, kind chip,
choices, question grid, hint, status row, and answer/error tones.

## Code Commentary

### Logic

Static atoms only; `errorText` alarm, `answeredText` mint, `announce` the live
region styling.

### Conventions

Tokens; no animation.

### Invariants And Boundaries

The announce region must remain in the accessibility tree.

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
| The interaction recipes. | `bar`; `choicesRow`; `questionsGrid`; `announce` | dashboard/src/panels/session-cockpit/interactionStyles.ts:3-75 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  interaction styles module extracted from `InteractionBar.tsx`. Verification pinned
  to the leaf base until closeout stamps the code commit.
