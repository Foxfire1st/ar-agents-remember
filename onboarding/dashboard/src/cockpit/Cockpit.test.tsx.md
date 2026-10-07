# dashboard/src/cockpit/Cockpit.test.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`Cockpit.test.tsx` proves the production shell's standing contracts: the Operations detail hydration
and rollup, the serving-build stamp, the full-bleed/railed layout flip, rail keep-alive across view
switches, the right-rail River/Chat toggle and its persistence, and the resizable rails.

## Code Commentary

### Logic

- The suite mounts `CockpitShell`. MIK-R79 moved the opening view from Operations to Chats, so cases
  that need the railed Operations context now mount `CockpitShell initialView="operations"`.
- The full-bleed case now switches to **File Viewer** and asserts the File Viewer pane is present;
  the Engine Room's removed dashboard entry is covered instead by the initial-view matrix, which
  mounts `memory`, `hangar`, `engine` and `topology` through `initialView` and asserts each page
  renders with its expected `data-fullbleed` and rail visibility.
- Keep-alive, rail-toggle, persistence and rail-width assertions are otherwise unchanged.

### Conventions

Vitest + Testing Library; views are selected by their radio name; fixtures come from the gallery.

### Invariants And Boundaries

The suite binds the shell's default view, the layout bleed set, the hidden-not-unmounted layer
behavior and the retained pages' layout through injected views. It does not re-test the Knowledge
reader's own behavior.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The requirement packet
`MIK-R79@v1` (rules 1 and 16) fixes the opening view, the product bar and the retained pages; it
lives outside the code and memory repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The suite mounts the shell and switches views through the mode bar. [13]
- The layout matrix sources the retained pages only through their injected views. [14]
- The view list the bar renders. [15]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
