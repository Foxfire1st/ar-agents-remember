# dashboard/src/panels/review/workspaceState.ts

## Governing Overview

[review route overview](overview.md)

## Purpose

Hold mounted review choices for family context, query, open reading groups, worklist visibility and numbered selection-focus intent.

## Code Commentary

`useWorkspaceState` starts with no chosen family, empty query/groups, hidden worklist and tree intent zero with keep false. setChosen also closes the worklist. toggleGroup immutably adds/removes one group; openGroup preserves the existing set when already open. Those choices survive subject reads within the mount and do not persist across review openings.

`beginSelection` alone increments the tree-intent number and records explicit keep. `FocusRequest` carries the originating element, earlier intent number and optional scrollOnly/answered/failureLanded flags for ReviewWorkspace's consumption rule; the interface itself moves nothing. Code context is remembered by reading/codeContextPreference.ts and diff layout follows reading-column width through useReadingLayout. No state callback here scrolls the page.

## Evidence

- workspaceState.ts current behavior at this source owner. [7]
- workspaceState.ts current behavior at this source owner. [8]
