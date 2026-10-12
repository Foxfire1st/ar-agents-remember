# dashboard/src/panels/review/markerNavigation.test.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The workspace's moves for an intent marker (`markerNavigation.ts`, requirement MIK-R34). Recording stand-ins for the workspace state's setters and for the navigation's `onSelect` show exactly what a follow selects and what a return restores, in order. 5 cases.

## Code Commentary

- `workspace()` builds a stand-in workspace state whose setters record each call as a line; `navigation(calls)` builds a navigation whose `onSelect` records the subject and the family context.
- **Following (2 cases).** A follow first sets the opened path to `null`, then selects the invariant's own review at its member row of the named family: `onSelect` with `{ kind: 'invariant', id }` and `{ familyId, memberRevisionId }`. When no family records the invariant, it selects the invariant with no context.
- **The return (2 cases).** A return selects the captured subject and family context, then restores the `worklist` boolean through `setWorklist`, the opened path, the layout and the full-file choice, and leaves the workspace's focus request cleared. Without a navigation it restores the family selection directly.
- **The walked tree (1 case).** A follow and the return from it each call the navigation's `onSelect` once, with exactly two arguments: a subject and a family context, and no selection options. A selection without options starts the walked family tree afresh (requirement MIK-R39 rule 9); only a selection of a tree row passes `keepTree`.

### Logic

- **Following (2).** The invariant's own review at its member row of the named family (`onSelect` with
  `{ kind: 'invariant', id }` and `{ familyId, memberRevisionId }`, after `setOpenPath null`); the invariant alone when
  no family records it.
- **The return (2).** The subject and family, then the `worklist` boolean, the opened file, the layout and the full-file choice, with
  the tree's focus request cleared; without navigation the family selection is restored directly.

### Conventions

- `workspace()` and `navigation()` record each call as a line.

### Invariants And Boundaries

- Pins ICR-R34 rules 2 and 3's workspace moves (mutation M8).

### Todos

No additional work is asserted by this card.

## Evidence

- The recorded return restores the worklist boolean after the subject before file, layout and full-file state. [12]


- The recording stand-ins. [6]

- Following a marker. [7]

- The return. [8]

- A follow and its return select with two arguments only, so both start the walked tree afresh. [9]

- The moves under test. [10]

- The options a selection would have to pass to keep the tree. [11]

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

### Cross-Repo References

No cross-repo boundary is crossed by this file.
