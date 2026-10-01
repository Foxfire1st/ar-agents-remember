# dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The composed rail/stage/inspector JSX of the Sessions view, extracted from
`SessionsView.tsx` by the 260731-EFA-L8 split. `SessionsViewBody` renders the rail
panel, stage header actions, failed-launch slot, working-line slot, composer slot,
stage working area, stage panel, inspector panel, and overlays from the controller
view.

## Code Commentary

### Logic

Each slot subcomponent renders one surface (rail, stage header, failed launch,
working line, composer, stage, inspector, overlays) from the derived `View`. The
persistent PTY composition and keep-alive mounting rules are honored at the stage
level.

### Conventions

Presentational composition; all data comes from the controller `View`.

### Invariants And Boundaries

The body never fetches or mutates state; it renders the view packet only.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The composed body and its stage/inspector slots. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
