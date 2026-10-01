# dashboard/src/data/reviewLane.ts

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The dashboard adapter of the unexplained-changes lane (MIK-R32).** It carries the server's one classification
(`models/knowledge/review_lane.py`) as TypeScript types, snake_case as served, and reads it through the tree view
route (`serving/review_trees.py`): `useReviewLane` asks `lane=files` for the two destinations, and
`useReviewFileClassification` asks `file=<path>` for one changed path. MIK-R34's per-hunk intent markers read the same
per-file answer through `readFileClassification`, a single read without a hook that their scope keeps per surface. The
entry's own count (`ReviewLaneSummary`) travels on the changed-intent summary (`reviewIntentSummary.ts`). A dataset
review asks this adapter nothing.

## Code Commentary

### Logic

- **Types.** `LaneBucket`, `LaneHunkClass`, `LaneSideName`, `LaneMembershipState`; `ReviewLaneSummary` (its
  `unmeasured` list, and totals only when counted); the hunk facts (`ReviewLaneSpan`, `ReviewLaneLink` with
  `invariant_key`, `invariant_revision_key` and family occurrences, `ReviewLaneUnknown`, `ReviewLaneHunk`); the file
  facts (`ReviewLaneEntryRange`, `ReviewLaneSide`, `ReviewLaneNonText`, `ReviewLaneCounts`,
  `ReviewFileClassification`); the lane (`ReviewLaneFile`, `ReviewLaneDestination`, `ReviewLanePath`,
  `ReviewUnexplainedLane` with `paths`, ruling Q1).
- **Reads.** `laneUrl` builds `/api/review/trees?repo&master&leaf&comparison=<n>` plus `lane=files` or
  `file=<path>`. `useLaneAnswer(url)` fetches through `getReviewJson` and keeps each answer **with the URL it
  answers**, so a superseded answer never draws; `null` asks nothing. `picked` and `readOf` turn the answer into a
  `LaneRead<T>`: `ready` with the value when the route answered `trees` and carried it, `unavailable` with the
  owner's refusal (`reviewProblemFromRefusal`), and otherwise `unavailable` as an unreadable answer (an answer
  without the lane, as the landed git-trees captures give, is never read as an empty lane).
- `useReviewLane(repo, master, leaf, comparison)` returns `null`, and makes no request, when `comparison` is
  `undefined` (a dataset review); `useReviewFileClassification` also when no path is open.
- **`readFileClassification(repo, master, leaf, comparison, path)` (MIK-R34).** The same `file=<path>` read as a
  promise rather than a hook: it resolves to `ready` or `unavailable` through `readOf`, and a thrown transport error
  becomes `unavailable` with `reviewProblemFromCause`, never a rejection. Its one caller is the marker scope's cache
  (`panels/review/intentMarkerScope.ts`), which asks once per changed path per surface and forgets a failed read.

### Conventions

- Only the answer is carried; nothing here classifies, counts or filters. The per-hunk markers take their hunks, links
  and family occurrences from this answer unchanged (review ruling Q2 kept L32's response as it is).
- The surface makes the lane read once (`ReviewSurface.ReviewPanes`, review R1 F1) and hands it down.

### Invariants And Boundaries

- A dataset review names no tree comparison and makes no lane read (the gitTrees dataset case asserts no `/trees`
  request).
- `LaneRead` never holds a value and a problem at once.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The adapter's own statement: the server classifies once and this file only carries the answer. [1]
- The entry's count: totals only when counted. [2]
- A link's keys and family occurrences; the per-file response. [3]
- A destination, one path's bucket, and the lane with `paths`. [4]
- The read states, and an answer without its value read as unavailable. [5]
- One answer kept with its URL; `null` asks nothing. [6]
- The two reads: the lane (none for a dataset review) and one file. [7]
- One file's classification as a single read for the intent markers; a transport failure is `unavailable`. [8]
- Its one caller: the marker scope's per-surface cache, only for a tree comparison. [9]
- The one lane read of the surface. [10]
- The server's shapes this file mirrors. [11]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
