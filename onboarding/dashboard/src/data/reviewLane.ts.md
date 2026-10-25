# dashboard/src/data/reviewLane.ts

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The dashboard adapter of the unexplained-changes lane (MIK-R32).** It carries the server's one classification
(`models/knowledge/review_lane.py`) as TypeScript types, snake_case as served, and reads it through the tree view
route (`serving/review_trees.py`): `useReviewLane` asks `lane=files` for the two destinations.
MIK-R34's per-hunk intent markers read one path's `file=<path>` answer through `readFileClassification`,
a single read without a hook that their scope keeps per surface. The
entry's own count (`ReviewLaneSummary`) travels on the changed-intent summary (`reviewIntentSummary.ts`). The lane hook asks nothing when its comparison argument is undefined; the adapter does not inspect a dataset kind.

`data/reviewLane.ts` carries the unexplained-changes lane of a tree comparison: per-file buckets, per-hunk classes, and the two destinations, all classified once by the server. In W03 the per-file classification hook is gone; the single-shot read remains for the intent markers, and destinations are consumed through the change-set filter instead of a focused lane view.
## Code Commentary

### Logic

- **Types.** `LaneBucket`, `LaneHunkClass`, `LaneSideName`, `LaneMembershipState`; `ReviewLaneSummary` (its
  `unmeasured` list, and totals only when counted); the hunk facts (`ReviewLaneSpan`, `ReviewLaneLink` with
  `invariant_key`, `invariant_revision_key` and family occurrences (`ReviewLaneFamilyOccurrence`, including optional `reason`), `ReviewLaneUnknown`, `ReviewLaneHunk`); the file
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
  `undefined`. There is no `useReviewFileClassification` export or focused lane-view hook.
- **`readFileClassification(repo, master, leaf, comparison, path)` (MIK-R34).** The same `file=<path>` read as a
  promise rather than a hook: it resolves to `ready` or `unavailable` through `readOf`, and a thrown transport error
  becomes `unavailable` with `reviewProblemFromCause`, never a rejection. The inspected marker-scope caller (`panels/review/intentMarkerScope.ts`) caches pending reads and successful answers for listed changed paths within its scope; unavailable answers are removed from the pending cache and may be retried. It supplies no read while comparison is undefined.

### Conventions

- Only the answer is carried; nothing here classifies, counts or filters. The per-hunk markers take their hunks, links
  and family occurrences from this answer unchanged (review ruling Q2 kept L32's response as it is).
- The surface makes the lane read once (`ReviewSurface.ReviewPanes`, review R1 F1) and hands it down.

### Invariants And Boundaries

- Request suppression follows comparison availability: `useReviewLane` uses a null URL when comparison is undefined. `ReviewPanes` derives that argument from the payload's `review:trees:<n>` limitation token, and the marker scope also checks comparison availability.
- `LaneRead` never holds a value and a problem at once.

### Todos

No additional work is asserted by this card.

`useReviewLane` still reads a comparison's `lane=files` answer through the tree-view route and picks the lane payload; `readFileClassification` still fetches one path's `file=` classification as a single read for the per-hunk intent markers. This module exports no `useReviewFileClassification` hook. The inspected `ReviewPanes` passes its shared lane read to the workspace, details and change-page context, and opens `ChangeSetViewer` for the change overlay. The candidate manifest omits the exact `dashboard/src/panels/review/LaneFileFocus.tsx` path; that absence does not establish removal of all equivalent behavior. Bucket, hunk and destination shapes are preserved from BASE; `ReviewLaneFamilyOccurrence` additionally carries optional `reason?: string`, matching the server field whose validator requires a reason exactly for `membership_unknown`.
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

- The lane hook asks nothing without a comparison; one-file classification remains a single-shot marker read, not a hook. [7]

- One file's classification as a single read for the intent markers; a transport failure is `unavailable`. [8]
- The server's shapes this file mirrors. [11]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
- The lane is read per comparison through the tree-view route [12]
- useIntentMarkerScope supplies readFileClassification only when comparison is defined. Its cache refuses unlisted paths, reuses pending reads, retains ready answers and removes unavailable answers from pending so later calls can retry. This is observed caller evidence, not an exhaustive caller catalog. [9]



- The lane read is acquired once by the reading surface's change-set hook, with the comparison number that hook resolved or `undefined`, and the surface carries that one read into the open change page without asking for the lane itself. [10]


- laneUrl constructs the comparison-bound tree-view request. useReviewLane suppresses the request when comparison is undefined and selects the lane answer otherwise. This module retains readFileClassification as a single-shot file read and declares no exported useReviewFileClassification hook; these local targets do not prove global focused-view removal. [14]
- ReviewLaneFamilyOccurrence preserves optional family identity/revision fields and required membership state, adding optional reason; ReviewLaneLink continues to carry these occurrences. The server declares the corresponding reason field and validates its presence exactly for membership_unknown. This is DTO carriage and server validation, not evidence that every carried field renders. [15]



- `treeComparisonNumber` returns the number in the first `review:trees:<digits>` limitation token and `undefined` when there is none; the surface uses it to number the comparison it shows and to check an evidence destination against it, never branching on dataset kind. [16]
