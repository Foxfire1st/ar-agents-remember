# dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The palette-command registration hook. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
