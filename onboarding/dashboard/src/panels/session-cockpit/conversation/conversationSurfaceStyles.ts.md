# dashboard/src/panels/session-cockpit/conversation/conversationSurfaceStyles.ts

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The surface recipes. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
