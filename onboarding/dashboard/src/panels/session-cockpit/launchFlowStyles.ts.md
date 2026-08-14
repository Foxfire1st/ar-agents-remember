# dashboard/src/panels/session-cockpit/launchFlowStyles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/launchFlowStyles.ts`  |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The Panda CSS recipes of the launch-flow dialog, extracted from `LaunchFlow.tsx` by
the 260731-EFA-L8 split. Owns the overlay/box, heading, option rows, note/error
lines, footer, launch/quiet buttons, and outcome box.

## Code Commentary

### Logic

Static atoms; `errorLine` alarm pre-wrap for verbatim refusal text; `launchButton`
the golden primary; `outcomeBox` the settled outcome surface.

### Conventions

Tokens; no animation.

### Invariants And Boundaries

Error lines must render verbatim server text without truncation surprises
(`whiteSpace: pre-wrap`).

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
| The dialog recipes. | `overlay`; `optionButton`; `errorLine`; `launchButton` | dashboard/src/panels/session-cockpit/launchFlowStyles.ts:3-155 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the launch
  flow styles module extracted from `LaunchFlow.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
