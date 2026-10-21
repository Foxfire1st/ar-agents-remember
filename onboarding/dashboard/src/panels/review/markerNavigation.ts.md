# dashboard/src/panels/review/markerNavigation.ts

## Governing Overview

[Review route overview](overview.md)

## Purpose

Adapt intent-marker follow and Back to the review page's own subject selection, and restore the captured subject, family context and worklist state in the required order.

## Code Commentary

`MarkerSelection` is now required. Its current reader supplies subject and optional chosen family; its select function accepts a subject and nullable family context. `workspaceMarkerMoves` captures exactly that subject/context plus the current worklist boolean, and returns a restore closure. It no longer receives an optional navigation object or chooses a navigation-free fallback.

`openTarget` selects the invariant named by the marker, with `{ familyId, memberRevisionId }` when the target names a family and null otherwise. It no longer closes an opened source file here. `restore` first selects the captured subject/context, clears `focusSelection.current` so the selection's tree-focus request does not override marker return, then restores the worklist boolean because selecting a subject leaves the worklist.

The old opened path, diff-layout and full-file fields and setters are gone from this module. Pane disclosure, actual marker focus and editor scroll are separate owners; this module cannot reconstruct those removed fields. It calls the supplied selection adapter rather than directly calling `ReviewNavigationState.onSelect`, so adapter-specific tree-retention policy belongs to the caller's audit.

## Invariants And Boundaries

This bridge restores page selection and worklist state only. It does not implement browser history, read a source file, classify a hunk or itself focus the marker. Nullable family context is distinct from an optional absent selection adapter.

The stored recording-adapter cases establish the local arguments and restoration order. The former separate outside-selection/reset assertion was removed; these cases do not establish the page caller's tree-retention policy.

## Evidence

- Markers follow the page selection and Back restores the selected subject and worklist. [1]
- The captured position contains only subject, chosen family and worklist state. [2]
- Capture reads the required selection adapter and current worklist, while open delegates to the marker target. [3]
- A marker target selects its invariant and named family/member context, or null family context. [4]
- Restore selects subject/context, clears the tree-focus request and only then restores worklist. [5]
- The capture/open pair uses the required page-supplied selection adapter. [10]
- Return unconditionally clears the pending tree-focus request after selecting and before worklist restoration. [12]
- The required adapter exposes current subject/context and selection; removed path/layout/full-file state is not captured. [13]
- Recording-stand-in tests assert named-family and no-family adapter arguments, then subject/context restoration followed by worklist and a cleared focus request; they do not prove a direct-navigation tree reset. [7]

## Historical predecessor account

The former account is retained below as provenance. Removed exports, old restoration fields and old test-world identities are historical where the current account differs; earlier execution statements are not fresh results.

> # dashboard/src/panels/review/markerNavigation.ts
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> **How the review workspace moves for a per-hunk intent marker (MIK-R34 rules 2 and 3):** following one selects its
> target in the tree through the rail's own selection, and the return puts the reading position back as it was.
>
> ## Code Commentary
>
> ### Logic
>
> - **Following (`openTarget`).** Closes the file the marker sat in (`setOpenPath(null)`, without the focus move a
>   centre open makes), then selects `{ kind: 'invariant', id: invariantKey }` through the navigation's `onSelect`, with
>   the family context `{ familyId, memberRevisionId }` when the target names a family, so the invariant's own review
>   opens at its member row (shared, before-only or removed memberships alike); without a family the invariant is
>   selected alone (`No recorded family`, or the unknown state the target carries). A workspace without navigation sets
>   the family selection directly.
> - **The return (`restore`).** `capture` records the subject, the family selection, the worklist-open flag, the opened
>   path, the diff layout and the full-file choice. The restore selects the subject and family again and **clears
>   `focusSelection` when a navigation exists**, so focus goes to the originating marker and not to the tree's selection; a
>   workspace without navigation only sets the chosen subject and clears no request. Then the worklist flag (after the
>   subject selection), the opened path, the layout and
>   the full-file choice.
> - **Back navigation.** The reviewer has no in-reviewer back history, so the way back is the visible `Back to <file>`
>   control only; there is no browser-history integration.
>
> ### Conventions
>
> - Plain functions over `WorkspaceState` and `ReviewNavigationState`; `workspaceMarkerMoves` is the one export, called by
>   the workspace for the scope.
>
> ### Invariants And Boundaries
>
> - A target is reached only through the rail's own selection, so it is a tree position of the mounted workspace, never
>   a family on its own (ICR-R34 rule 2).
> - **A follow and its return are outside selections.** Both call the navigation's `onSelect` with a subject and a
>   family context and no selection options. A selection without options starts the walked family tree afresh
>   (requirement MIK-R39 rule 9), so a follow shows the families of the marker's subject alone and the return brings no
>   kept family back.
> - **Part of the candidate invariant "Back returns focus to the originating marker with its hunk in view"** (recorded on
>   `MarkerTargetState.tsx.md`): the restore leaves no pending selection focus to take focus from the marker.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> - `restore` re-selects the captured subject and choice (clearing the tree's focus request so focus returns to the originating marker, not the tree selection), then restores the worklist flag, path, layout and full-file flag after the subject. There is no lane destination in the recorded position.
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> - The module's own statement: a tree position of the mounted workspace, selected the way the rail selects it. (historical reference 1)
> - The captured position records a worklist boolean, not a lane destination, alongside subject, choice, path, layout and full-file state. (historical reference 2)
>
> - Capture takes the current worklist boolean and returns the restore closure; open delegates to the marker target selection. (historical reference 3)
>
> - Following: close the file, select the invariant with its member context. (historical reference 4)
> - Return restores subject, worklist flag, opened path, layout and full file with selection focus cleared; no lane destination is captured. (historical reference 5)
> - The workspace that passes them to its scope. (historical reference 6)
> - The marker move cases follow the subject and restore setWorklist before path, layout and full-file choice. The return title retains the word lane, but its current assertion is the worklist setter. (historical reference 7)
>
> - A follow and its return select with two arguments only, so both start the walked tree afresh. (historical reference 8)
> - The options a selection would have to pass to keep the tree. (historical reference 9)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.
> - Capture/open pair built from workspace state (historical reference 10)
>
> - Restores the captured subject and chosen context, clears the selection focus request for marker return only when a navigation exists, then restores worklist, open path, diff layout and full-file mode. (historical reference 12)
