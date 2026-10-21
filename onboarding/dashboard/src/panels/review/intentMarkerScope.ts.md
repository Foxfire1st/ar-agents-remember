# dashboard/src/panels/review/intentMarkerScope.ts

## Governing Overview

[Review route overview](overview.md)

## Purpose

Keep one comparison-qualified marker scope: its listed changed paths, shared per-file classifications, followed target and pending return. The scope is absent until the comparison identifier is defined. A diff without it draws no review markers.

## Code Commentary

`markerInventory` keeps the listed paths and calls the inventory partial when either its partial flag is set or its state is not measured. The comparison key includes repository, master, leaf and comparison. Only followed/returning values with that key are exposed. Follow captures the supplied reading-position restore closure and opens the target; Back clears the followed value, starts returning and calls that closure; settle clears returning. A return that never settles expires after the declared 15-second return window.

`useClassificationCache` reads only listed paths. It shares the pending promise per path, keeps ready answers for that scope and drops failed promises so a later request may retry. `useMarkClassification` no longer accepts a caller-supplied `given` classification. For an active listed path, it asks the shared cache through `gatedClassify`: when a reading gate exists and the scope has no ready answer, the request runs through that gate; an already held answer or a caller outside the gate takes the direct path. The gate's actual capacity and scheduling belong to its owner, not this helper.

The hook pairs a returned value with both its path and classification function, so another path/comparison's answer is not rendered. It returns none without a scope or when inactive. `listedRead` makes an unlisted path explicit as unlisted under a partial inventory, or none under a complete one. Otherwise `shownRead` uses this matching response, the scope's held answer, or loading. An unresolved classification is not converted to a measured zero or an empty mark list.

## Invariants And Boundaries

All actual classification reads remain `readFileClassification`; scope/caching and gate admission do not create attribution. Inactive is the caller's request condition, not a viewport observer inside this hook. The old lane-supplied classification branch is removed. The return timer bounds the pending return marker, not the lifetime of the followed target.

## Evidence

- A defined comparison creates a scope, while no scope or inactive input produces none for a pane. The pane hook has explicit no-scope/inactive behavior and uses the matching scope read. [1]
- The scope types separate marker position, workspace moves, read states and scope values. [2]
- An unsettled return expires after the declared 15-second return window. [3]
- Partial or unmeasured inventories keep the partial interpretation. [4]
- Follow, Back and return state remain qualified by the comparison key. [5]
- Listed paths share a pending classification and ready result; failed reads are forgotten. [6]
- Pane reads use gated shared classification, explicit unlisted states and only matching path/function answers. [7]
- Classification uses the reading gate only while it lacks a ready cached answer; the given-classification branch is gone. [10]
- Stored scope tests assert one listed-path classification per surface, no unlisted request and the partial-or-unmeasured inventory interpretation. [9]

## Historical predecessor account

The former account is retained below as provenance. Removed exports, old restoration fields and old test-world identities are historical where the current account differs; earlier execution statements are not fresh results.

> # dashboard/src/panels/review/intentMarkerScope.ts
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> **The review workspace's scope for MIK-R34's per-hunk intent markers:** which tree comparison they describe, each
> changed file's classification (read once per surface and shared by every pane of the file), and the one followed
> marker the reader can return to. The hook returns no scope while the comparison identifier is undefined and
> provides a scope when it is defined. A diff without a scope draws no review markers.
>
> ## Code Commentary
>
> ### Logic
>
> - **Types.** `MarkerAt` (the path, the pane that drew the marker and the owner hunk it marks); `MarkerMoves`
>   (`capture` records the reading position and returns what puts it back, `open` selects a target; the workspace
>   supplies them, `markerNavigation.ts`); `MarkRead` (a lane read, `none`, or `unlisted`); `IntentMarkerScopeValue`;
>   the `IntentMarkerScope` context (default `null`).
> - **The inventory (`markerInventory`; review R1 F5, R2).** The change inventory's listed paths, and `partial` when the
>   inventory is `partial` **or not `measured` at all**, so a changed file may be unlisted.
> - **The scope (`useIntentMarkerScope`).** `null` while the input comparison identifier is undefined. Otherwise: `listed(path)`;
>   `classify` and `peek` from the cache; `origin` and `target` (the followed marker and the target it opened) and
>   `returning` (the marker a return is bringing the reader to), each only for the same repo, master, leaf and
>   comparison, so a marker of another comparison (the reader refreshed onto a new one) is never offered. `follow`
>   records the position through `moves.capture()`, clears any return and opens the target; `back` clears the followed
>   marker, starts the return and restores the position; `settle` ends the return once the pane has drawn and focused the
>   mark; a return whose mark is never drawn stops after `RETURN_WINDOW_MS` (15 s). The followed target stays until
>   Back (review R1 N3, accepted).
> - **The cache (`useClassificationCache`).** Asks `readFileClassification` only for a listed path (review R1 F4, N11),
>   keeps one pending promise per path, keeps a `ready` answer for the life of the scope key and forgets a failed one,
>   so reopening the file asks again.
> - **A pane's read (`useMarkClassification`).** `none` outside a scope or for an inactive (unchanged) path; the
>   caller's own classification when given (the lane's full file, one read for the whole lane view); for a path a
>   partial inventory does not list, `unlisted` (said, never silent), and under a complete inventory `none`, because
>   such a file is unchanged; otherwise the answer this hook's read gave for this path and this `classify`, else what the
>   scope already holds (`peek`), else `loading` (`shownRead`). An answer is kept with the read that gave it, so another
>   path's or comparison's never draws.
>
> ### Conventions
>
> - React context and hooks only; the one request is `data/reviewLane.readFileClassification`.
> - `markerInventory` is the one place the partial rule lives; the workspace calls it (review R2).
>
> ### Invariants And Boundaries
>
> - **Part of the candidate invariant "every intent marker comes from L32's per-file classification response"**
>   (recorded on `hunkMarkers.ts.md`): the scope reads only that response, once per changed file per surface; the
>   surface case asserts one read per file with `comparison=2`, and `intentMarkerScope.test.ts` asserts an unlisted path
>   is never asked about.
> - An undefined comparison identifier yields no scope. `useMarkClassification` returns `none` without a scope; this module does not select behavior by review mode.
> - A missing classification is `none`, `unlisted`, `loading` or `unavailable`, never an empty list of marks.
>
> ### Todos
>
> No additional work is asserted by this card.
>
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
> - Where a followed marker sat, the workspace's moves, a pane's read and the scope's value. (historical reference 2)
> - A return that never finds its mark stops waiting. (historical reference 3)
> - A partial or unmeasured inventory counts as partial (review R2). (historical reference 4)
> - The scope: listed paths, origin, target and return only for the same comparison; follow, back and settle. (historical reference 5)
> - One read per listed path per scope; a failed read forgotten. (historical reference 6)
> - A pane's read: the caller's classification, `unlisted` under a partial inventory, the kept answer, or loading. (historical reference 7)
> - The workspace that provides it. (historical reference 8)
> - The scope cases: one read per surface, never an unlisted path; partial and unmeasured inventories. (historical reference 9)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.
>
> - useIntentMarkerScope returns null when comparison is undefined and otherwise returns a scope containing that comparison. IntentMarkerScope defaults to null; useMarkClassification returns none without a scope or when inactive. These implementation checks establish the no-scope boundary without asserting that a dataset review lacks a comparison. (historical reference 1)
