# dashboard/src/panels/session-cockpit/sessions-view/styles.ts

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The Panda CSS recipes of the Sessions view, extracted from `SessionsView.tsx` by the
260731-EFA-L8 split. Owns the root layout, panes, stage/inspector sizing, floor chip,
reopen button, resize handle, and the persisted panel constants
(`PANELS_AUTOSAVE_ID`, `INSPECTOR_OPEN_KEY`, `RAIL_MIN_PERCENT`).

## Code Commentary

### Logic

Static atoms are `css({...})`; layout constants are exported for the resize logic and
persistence keys.

### Conventions

Tokens only; no animation.

### Invariants And Boundaries

The inspector/rail percentages and keys must stay in sync with the resize and
persistence code.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The layout recipes and constants. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
