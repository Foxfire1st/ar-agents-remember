# dashboard/src/panels/review/markerNavigation.test.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The workspace's moves for an intent marker (`markerNavigation.ts`, requirement MIK-R34). Recording stand-ins for the workspace state's setters and for the navigation's `onSelect` show exactly what a follow selects and what a return restores, in order. 5 cases.

## Code Commentary

- `workspace()` builds a stand-in workspace state whose setters record each call as a line; `navigation(calls)` builds a navigation whose `onSelect` records the subject and the family context.
- **Following (2 cases).** A follow first sets the opened path to `null`, then selects the invariant's own review at its member row of the named family: `onSelect` with `{ kind: 'invariant', id }` and `{ familyId, memberRevisionId }`. When no family records the invariant, it selects the invariant with no context.
- **The return (2 cases).** A return selects the captured subject and family context, then restores the lane, the opened path, the layout and the full-file choice, and leaves the workspace's focus request cleared. Without a navigation it restores the family selection directly.
- **The walked tree (1 case).** A follow and the return from it each call the navigation's `onSelect` once, with exactly two arguments: a subject and a family context, and no selection options. A selection without options starts the walked family tree afresh (requirement MIK-R39 rule 9); only a selection of a tree row passes `keepTree`.

## Evidence

- The recording stand-ins. [6]
- Following a marker. [7]
- The return. [8]
- A follow and its return select with two arguments only, so both start the walked tree afresh. [9]
- The moves under test. [10]
- The options a selection would have to pass to keep the tree. [11]
