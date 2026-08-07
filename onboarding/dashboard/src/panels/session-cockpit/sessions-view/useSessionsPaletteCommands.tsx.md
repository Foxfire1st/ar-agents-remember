# dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

All palette-command registration for the Sessions view, extracted from
`SessionsView.tsx` by the 260731-EFA-L8 split. `useSessionsPaletteCommands` registers
the launch, model/effort, chats-stage, triage, and rail commands into the cockpit
command palette.

## Code Commentary

### Logic

Each sub-hook (`useLaunchPaletteCommand`, `useModelEffortPaletteCommands`,
`useChatsStagePaletteCommands`, `registerTriageCommands`, `useRailPaletteCommands`)
returns palette command rows wired to the controller handlers; the exported hook
merges them.

### Conventions

Commands only register; execution delegates to controller handlers.

### Invariants And Boundaries

No command may mutate state directly; all actions go through the view handlers.

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
| The palette-command registration hook. | `useSessionsPaletteCommands` | dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:241-305 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the palette
  hook module extracted from `SessionsView.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
