# dashboard/src/panels/session-cockpit/interactionParts.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/interactionParts.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The structured-interaction render parts of the session cockpit, extracted from
`InteractionBar.tsx` by the 260731-EFA-L8 split. Owns the questions body, announce
region, interaction head/body/status row, and hint.

## Code Commentary

### Logic

`QuestionsBody` renders the gate-question options; `InteractionAnnounce` is the live
announce region; `InteractionBody`/`InteractionStatusRow` render the answer state and
its honest status (answered/error/working).

### Conventions

Answers ride the landed gate channel; these parts never write to the terminal.

### Invariants And Boundaries

The interaction parts render the decision record only; no submit machinery here.

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
| The interaction render parts. | `QuestionsBody`; `InteractionAnnounce`; `InteractionBody` | dashboard/src/panels/session-cockpit/interactionParts.tsx:138-196; dashboard/src/panels/session-cockpit/interactionParts.tsx:197-220; dashboard/src/panels/session-cockpit/interactionParts.tsx:258-315 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  interaction parts module extracted from `InteractionBar.tsx`. Verification pinned
  to the leaf base until closeout stamps the code commit.
