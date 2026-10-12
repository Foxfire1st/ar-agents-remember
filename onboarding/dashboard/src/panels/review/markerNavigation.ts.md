# dashboard/src/panels/review/markerNavigation.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**How the review workspace moves for a per-hunk intent marker (MIK-R34 rules 2 and 3):** following one selects its
target in the tree through the rail's own selection, and the return puts the reading position back as it was.

## Code Commentary

### Logic

- **Following (`openTarget`).** Closes the file the marker sat in (`setOpenPath(null)`, without the focus move a
  centre open makes), then selects `{ kind: 'invariant', id: invariantKey }` through the navigation's `onSelect`, with
  the family context `{ familyId, memberRevisionId }` when the target names a family, so the invariant's own review
  opens at its member row (shared, before-only or removed memberships alike); without a family the invariant is
  selected alone (`No recorded family`, or the unknown state the target carries). A workspace without navigation sets
  the family selection directly.
- **The return (`restore`).** `capture` records the subject, the family selection, the worklist-open flag, the opened
  path, the diff layout and the full-file choice. The restore selects the subject and family again and **clears
  `focusSelection`**, so focus goes to the originating marker and not to the tree's selection; then the worklist flag (after the
  subject selection), the opened path, the layout and
  the full-file choice.
- **Back navigation.** The reviewer has no in-reviewer back history, so the way back is the visible `Back to <file>`
  control only; there is no browser-history integration.

### Conventions

- Plain functions over `WorkspaceState` and `ReviewNavigationState`; `workspaceMarkerMoves` is the one export, called by
  the workspace for the scope.

### Invariants And Boundaries

- A target is reached only through the rail's own selection, so it is a tree position of the mounted workspace, never
  a family on its own (ICR-R34 rule 2).
- **A follow and its return are outside selections.** Both call the navigation's `onSelect` with a subject and a
  family context and no selection options. A selection without options starts the walked family tree afresh
  (requirement MIK-R39 rule 9), so a follow shows the families of the marker's subject alone and the return brings no
  kept family back.
- **Part of the candidate invariant "Back returns focus to the originating marker with its hunk in view"** (recorded on
  `MarkerTargetState.tsx.md`): the restore leaves no pending selection focus to take focus from the marker.

### Todos

No additional work is asserted by this card.

- `restore` re-selects the captured subject and choice (clearing the tree's focus request so focus returns to the originating marker, not the tree selection), then restores the worklist flag, path, layout and full-file flag after the subject. There is no lane destination in the recorded position.
## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: a tree position of the mounted workspace, selected the way the rail selects it. [1]
- The captured position records a worklist boolean, not a lane destination, alongside subject, choice, path, layout and full-file state. [2]

- Capture takes the current worklist boolean and returns the restore closure; open delegates to the marker target selection. [3]

- Following: close the file, select the invariant with its member context. [4]
- Return restores subject, worklist flag, opened path, layout and full file with selection focus cleared; no lane destination is captured. [5]
- The workspace that passes them to its scope. [6]
- The marker move cases follow the subject and restore setWorklist before path, layout and full-file choice. The return title retains the word lane, but its current assertion is the worklist setter. [7]

- A follow and its return select with two arguments only, so both start the walked tree afresh. [8]
- The options a selection would have to pass to keep the tree. [9]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
- Capture/open pair built from workspace state [10]

- Restores the captured subject and chosen context, clears the selection focus request for marker return, then restores worklist, open path, diff layout and full-file mode. [12]
