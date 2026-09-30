# dashboard/src/panels/review/markerNavigation.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerNavigation.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement: a tree position of the mounted workspace, selected the way the rail selects it. | "selected the way the rail selects it" | dashboard/src/panels/review/markerNavigation.ts:1-8 |
| The recorded reading position. | `Position` | dashboard/src/panels/review/markerNavigation.ts:15-22 |
| Capture and open, as the scope's moves. | `workspaceMarkerMoves` | dashboard/src/panels/review/markerNavigation.ts:24-42 |
| Following: close the file, select the invariant with its member context. | `openTarget` | dashboard/src/panels/review/markerNavigation.ts:44-55 |
| The return: subject, then lane, opened path, layout and full file; the tree's focus request cleared. | `restore`; "state.focusSelection.current = null;" | dashboard/src/panels/review/markerNavigation.ts:57-74 |
| The workspace that passes them to its scope. | "moves: workspaceMarkerMoves(state, navigation)," | dashboard/src/panels/review/ReviewWorkspace.tsx:278-278 |
| The moves' cases. | "selects the invariant's own review at its member row of the named family"; "restores the subject, then the lane, the opened file, the layout and the full-file choice" | dashboard/src/panels/review/markerNavigation.test.ts:43-94 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`ReviewWorkspace.tsx`) moved with the leaf's inserted lines: 1 row(s) re-pointed by the installed fixer (its generated bullets kept). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:22:15+00:00: Generated citation repair: "moves: workspaceMarkerMoves(state, navigation)," repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:278-278. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new workspace-moves module MIK-R34 adds, recording ruling 2026-09-30T16:19:34 Q1 (the visible Back control only). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
