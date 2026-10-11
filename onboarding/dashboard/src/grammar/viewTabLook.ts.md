# dashboard/src/grammar/viewTabLook.ts

## Governing Overview

[Shared primitives overview](overview.md)

## Purpose

Owns the one view-tab look shared by the cockpit's ModeBar and the role launcher's selectors, chips and action buttons.

## Code Commentary

`viewTabMetrics` holds the shared typography, spacing, border and corner metrics; height follows the padding/font rather than a second fixed-height declaration. `viewTabButton` preserves the tab's selected and keyboard-focus conditions. `launcherButton` uses the selected look for Start and the unselected look for Refresh and the other actions, while retaining launcher-specific disabled and focus behavior.

`launcherSelect` derives the same metrics but retains the source's letter case, a drawn arrow and ellipsis for long values. The renderer, not this style recipe, supplies the complete value and provenance in hover text. `launcherChip` holds informational mode, instruction and permission-feature labels; whole-control placement and wrapping belong to RoleLauncher. ModeBar retains its local phone-width spacing overrides.

## Boundaries

This module styles controls; it does not supply launch choices, resolve permissions, save defaults or decide which controls are available. Keep one shared visual authority rather than copying tab metrics into a launcher-local recipe. React Aria selection behavior remains ModeBar's.

## Evidence

- Shared visual metrics feed both tab and launcher recipes. [1]
- The tab class and selected launcher action retain the shared selected treatment; the complete small module contains both consumers and their common selected-look definition. [2]
- The common launcher selector retains source spelling, arrow and ellipsis. [3]
- ModeBar consumes the shared tab class without changing its single-select behavior. [4]
