# dashboard/src/panels/session-cockpit/launchFlowStyles.ts

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The dialog recipes. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
