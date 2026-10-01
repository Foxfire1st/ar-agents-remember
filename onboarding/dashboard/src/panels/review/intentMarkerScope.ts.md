# dashboard/src/panels/review/intentMarkerScope.ts

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

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: a tree comparison provides the scope; a dataset review or a diff outside the workspace has none. [1]
- Where a followed marker sat, the workspace's moves, a pane's read and the scope's value. [2]
- A return that never finds its mark stops waiting. [3]
- A partial or unmeasured inventory counts as partial (review R2). [4]
- The scope: listed paths, origin, target and return only for the same comparison; follow, back and settle. [5]
- One read per listed path per scope; a failed read forgotten. [6]
- A pane's read: the caller's classification, `unlisted` under a partial inventory, the kept answer, or loading. [7]
- The workspace that provides it. [8]
- The scope cases: one read per surface, never an unlisted path; partial and unmeasured inventories. [9]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
