# dashboard/src/data/reviewLane.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewLane.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:14:26+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter's own statement: the server classifies once and this file only carries the answer. | "server classifies once and this adapter only carries the answer" | dashboard/src/data/reviewLane.ts:1-16 |
| The entry's count: totals only when counted. | `ReviewLaneSummary` | dashboard/src/data/reviewLane.ts:39-47 |
| A link's keys and family occurrences; the per-file response. | `ReviewLaneLink`; `ReviewFileClassification` | dashboard/src/data/reviewLane.ts:61-73; dashboard/src/data/reviewLane.ts:123-134 |
| A destination, one path's bucket, and the lane with `paths`. | `ReviewLaneDestination`; `ReviewLanePath`; `ReviewUnexplainedLane` | dashboard/src/data/reviewLane.ts:150-156; dashboard/src/data/reviewLane.ts:159-162; dashboard/src/data/reviewLane.ts:164-176 |
| The read states, and an answer without its value read as unavailable. | `LaneRead`; `readOf` | dashboard/src/data/reviewLane.ts:190-193; dashboard/src/data/reviewLane.ts:204-209 |
| One answer kept with its URL; `null` asks nothing. | `useLaneAnswer` | dashboard/src/data/reviewLane.ts:218-236 |
| The two reads: the lane (none for a dataset review) and one file. | `useReviewLane`; `useReviewFileClassification` | dashboard/src/data/reviewLane.ts:248-257; dashboard/src/data/reviewLane.ts:279-291 |
| One file's classification as a single read for the intent markers; a transport failure is `unavailable`. | `readFileClassification` | dashboard/src/data/reviewLane.ts:259-276 |
| Its one caller: the marker scope's per-surface cache, only for a tree comparison. | "comparison === undefined ? null : readFileClassification(repo, master, leaf, comparison, path)," | dashboard/src/panels/review/intentMarkerScope.ts:96-98 |
| The one lane read of the surface. | "const laneRead = useReviewLane(" | dashboard/src/panels/review/ReviewSurface.tsx:335-340 |
| The server's shapes this file mirrors. | `ReviewUnexplainedLane`; `ReviewFileClassification` | mcp/src/agents_remember/models/knowledge/review_lane.py:284-312; mcp/src/agents_remember/models/knowledge/review_lane.py:223-235 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): **body updated for MIK-R34's `readFileClassification`** (Purpose, Logic, Conventions; two rows added), the single per-file read the per-hunk intent markers' scope keeps per surface. The generated repair above re-points the two hook rows by the 19 inserted lines; no claim changed.
- 2026-09-30T18:04:49+00:00: Generated citation repair: `useReviewLane`; `useReviewFileClassification` repointed to dashboard/src/data/reviewLane.ts:248-257; dashboard/src/data/reviewLane.ts:279-291. No content impact: mechanical anchor-range projection bound to citation source snapshot dd511ab0f1e150e6e017fdffb93a370d587225cb8c691b071ace179d457746ab; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new data adapter MIK-R32 adds, recording ruling 2026-09-30T12:19:20 Q1 (`paths`) and review R1 F1 (one lane read, made by the surface). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
