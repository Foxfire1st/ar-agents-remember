# dashboard/src/panels/review/intentMarkerScope.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/intentMarkerScope.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The review workspace's scope for MIK-R34's per-hunk intent markers:** which tree comparison they describe, each
changed file's classification (read once per surface and shared by every pane of the file), and the one followed
marker the reader can return to. Only a tree comparison provides a scope; a dataset review provides none, and every
diff renders exactly as before, as does any diff rendered outside a review workspace.

## Code Commentary

### Logic

- **Types.** `MarkerAt` (the path, the pane that drew the marker and the owner hunk it marks); `MarkerMoves`
  (`capture` records the reading position and returns what puts it back, `open` selects a target; the workspace
  supplies them, `markerNavigation.ts`); `MarkRead` (a lane read, `none`, or `unlisted`); `IntentMarkerScopeValue`;
  the `IntentMarkerScope` context (default `null`).
- **The inventory (`markerInventory`; review R1 F5, R2).** The change inventory's listed paths, and `partial` when the
  inventory is `partial` **or not `measured` at all**, so a changed file may be unlisted.
- **The scope (`useIntentMarkerScope`).** `null` when the payload names no comparison. Otherwise: `listed(path)`;
  `classify` and `peek` from the cache; `origin` and `target` (the followed marker and the target it opened) and
  `returning` (the marker a return is bringing the reader to), each only for the same repo, master, leaf and
  comparison, so a marker of another comparison (the reader refreshed onto a new one) is never offered. `follow`
  records the position through `moves.capture()`, clears any return and opens the target; `back` clears the followed
  marker, starts the return and restores the position; `settle` ends the return once the pane has drawn and focused the
  mark; a return whose mark is never drawn stops after `RETURN_WINDOW_MS` (15 s). The followed target stays until
  Back (review R1 N3, accepted).
- **The cache (`useClassificationCache`).** Asks `readFileClassification` only for a listed path (review R1 F4, N11),
  keeps one pending promise per path, keeps a `ready` answer for the life of the scope key and forgets a failed one,
  so reopening the file asks again.
- **A pane's read (`useMarkClassification`).** `none` outside a scope or for an inactive (unchanged) path; the
  caller's own classification when given (the lane's full file, one read for the whole lane view); for a path a
  partial inventory does not list, `unlisted` (said, never silent), and under a complete inventory `none`, because
  such a file is unchanged; otherwise the answer this hook's read gave for this path and this `classify`, else what the
  scope already holds (`peek`), else `loading` (`shownRead`). An answer is kept with the read that gave it, so another
  path's or comparison's never draws.

### Conventions

- React context and hooks only; the one request is `data/reviewLane.readFileClassification`.
- `markerInventory` is the one place the partial rule lives; the workspace calls it (review R2).

### Invariants And Boundaries

- **Part of the candidate invariant "every intent marker comes from L32's per-file classification response"**
  (recorded on `hunkMarkers.ts.md`): the scope reads only that response, once per changed file per surface; the
  surface case asserts one read per file with `comparison=2`, and `intentMarkerScope.test.ts` asserts an unlisted path
  is never asked about.
- A dataset review has no scope, so no read and no mark.
- A missing classification is `none`, `unlisted`, `loading` or `unavailable`, never an empty list of marks.

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
| The module's own statement: a tree comparison provides the scope; a dataset review or a diff outside the workspace has none. | "Only a tree comparison provides a scope." | dashboard/src/panels/review/intentMarkerScope.ts:1-6 |
| Where a followed marker sat, the workspace's moves, a pane's read and the scope's value. | `MarkerAt`; `MarkerMoves`; `MarkRead`; `IntentMarkerScopeValue` | dashboard/src/panels/review/intentMarkerScope.ts:18-22; dashboard/src/panels/review/intentMarkerScope.ts:26-29; dashboard/src/panels/review/intentMarkerScope.ts:34-35; dashboard/src/panels/review/intentMarkerScope.ts:37-52 |
| A return that never finds its mark stops waiting. | `RETURN_WINDOW_MS` | dashboard/src/panels/review/intentMarkerScope.ts:57-57 |
| A partial or unmeasured inventory counts as partial (review R2). | `markerInventory` | dashboard/src/panels/review/intentMarkerScope.ts:68-76 |
| The scope: listed paths, origin, target and return only for the same comparison; follow, back and settle. | `useIntentMarkerScope` | dashboard/src/panels/review/intentMarkerScope.ts:91-129 |
| One read per listed path per scope; a failed read forgotten. | `useClassificationCache` | dashboard/src/panels/review/intentMarkerScope.ts:133-172 |
| A pane's read: the caller's classification, `unlisted` under a partial inventory, the kept answer, or loading. | `useMarkClassification`; `shownRead` | dashboard/src/panels/review/intentMarkerScope.ts:176-211; dashboard/src/panels/review/intentMarkerScope.ts:214-221 |
| The workspace that provides it. | "<IntentMarkerScope.Provider value={markers}>" | dashboard/src/panels/review/ReviewWorkspace.tsx:281-281 |
| The scope cases: one read per surface, never an unlisted path; partial and unmeasured inventories. | "classifies a listed path once per surface, and never an unlisted one"; "counts an inventory that is partial, or not measured at all, as partial (review R2)" | dashboard/src/panels/review/intentMarkerScope.test.ts:22-76 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`ReviewWorkspace.tsx`) moved with the leaf's inserted lines: 1 row(s) re-pointed by the installed fixer (its generated bullets kept); 6 passing row(s) normalised by the fixer. The fixer's normalisation also re-measured ranges into files this leaf did not change (`intentMarkerScope.ts`). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:22:07+00:00: Generated citation repair: "<IntentMarkerScope.Provider value={markers}>" repointed to dashboard/src/panels/review/ReviewWorkspace.tsx:281-281. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new marker scope MIK-R34 adds, recording review R1 F4 (N11, the changed-path gate), F5 (the partial inventory), N3 (the target kept until Back) and the review R2 gap on unmeasured inventories. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
