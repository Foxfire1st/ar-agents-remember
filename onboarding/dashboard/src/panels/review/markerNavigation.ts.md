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
- **The return (`restore`).** `capture` records the subject, the family selection, the lane destination, the opened
  path, the diff layout and the full-file choice. The restore selects the subject and family again and **clears
  `focusSelection`**, so focus goes to the originating marker and not to the tree's selection; then the lane (after the
  subject, because choosing a subject leaves the lane and the return may be into it), the opened path, the layout and
  the full-file choice.
- **Back navigation (ruling 2026-09-30T16:19:34 Q1).** The reviewer has no in-reviewer back history, so "the
  reviewer's back navigation where supported" is the visible `Back to <file>` control only; no browser-history
  integration.

### Conventions

- Plain functions over `WorkspaceState` and `ReviewNavigationState`; `workspaceMarkerMoves` is the one export, called by
  the workspace for the scope.

### Invariants And Boundaries

- A target is reached only through the rail's own selection, so it is a tree position of the mounted workspace, never
  a family on its own (ICR-R34 rule 2).
- **Part of the candidate invariant "Back returns focus to the originating marker with its hunk in view"** (recorded on
  `MarkerTargetState.tsx.md`): the restore leaves no pending selection focus to take focus from the marker.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: a tree position of the mounted workspace, selected the way the rail selects it. [1]
- The recorded reading position. [2]
- Capture and open, as the scope's moves. [3]
- Following: close the file, select the invariant with its member context. [4]
- The return: subject, then lane, opened path, layout and full file; the tree's focus request cleared. [5]
- The workspace that passes them to its scope. [6]
- The moves' cases. [7]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
