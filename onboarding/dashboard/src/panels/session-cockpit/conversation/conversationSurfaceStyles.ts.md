# dashboard/src/panels/session-cockpit/conversation/conversationSurfaceStyles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversationSurfaceStyles.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The Panda CSS recipes of the conversation surface, extracted from
`ConversationSurface.tsx` by the 260731-EFA-L8 split. Owns the surface shell,
toolbar, toggles, agent-focus note, and agent-history error styling.

## Code Commentary

### Logic

Static atoms; `toggle` for the toolbar pivot; `agentFocusNote` the agents-line
notice; `agentHistoryError` the honest error banner tone.

### Conventions

Tokens; no animation.

### Invariants And Boundaries

The surface shell must preserve the feed's vertical scroll context.

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
| The surface recipes. | `surface`; `toolbar`; `agentHistoryError` | dashboard/src/panels/session-cockpit/conversation/conversationSurfaceStyles.ts:3-54 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the surface
  styles module extracted from `ConversationSurface.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
