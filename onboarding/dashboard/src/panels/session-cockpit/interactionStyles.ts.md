# dashboard/src/panels/session-cockpit/interactionStyles.ts

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The interaction recipes. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
