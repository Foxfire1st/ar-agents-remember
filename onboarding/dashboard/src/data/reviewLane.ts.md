# dashboard/src/data/reviewLane.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewLane.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The dashboard adapter of the unexplained-changes lane (MIK-R32).** It carries the server's one classification
(`models/knowledge/review_lane.py`) as TypeScript types, snake_case as served, and reads it through the tree view
route (`serving/review_trees.py`): `useReviewLane` asks `lane=files` for the two destinations, and
`useReviewFileClassification` asks `file=<path>` for one changed path. The entry's own count
(`ReviewLaneSummary`) travels on the changed-intent summary (`reviewIntentSummary.ts`). A dataset review asks this
adapter nothing.

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

### Conventions

- Only the answer is carried; nothing here classifies, counts or filters.
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
| The entry's count: totals only when counted. | `ReviewLaneSummary` | dashboard/src/data/reviewLane.ts:37-47 |
| A link's keys and family occurrences; the per-file response. | `ReviewLaneLink`; `ReviewFileClassification` | dashboard/src/data/reviewLane.ts:61-73; dashboard/src/data/reviewLane.ts:122-134 |
| A destination, one path's bucket, and the lane with `paths`. | `ReviewLaneDestination`; `ReviewLanePath`; `ReviewUnexplainedLane` | dashboard/src/data/reviewLane.ts:147-176 |
| The read states, and an answer without its value read as unavailable. | `LaneRead`; `readOf` | dashboard/src/data/reviewLane.ts:189-209 |
| One answer kept with its URL; `null` asks nothing. | `useLaneAnswer` | dashboard/src/data/reviewLane.ts:216-236 |
| The two reads: the lane (none for a dataset review) and one file. | `useReviewLane`; `useReviewFileClassification` | dashboard/src/data/reviewLane.ts:246-272 |
| The one lane read of the surface. | "const laneRead = useReviewLane(" | dashboard/src/panels/review/ReviewSurface.tsx:335-340 |
| The server's shapes this file mirrors. | `ReviewUnexplainedLane`; `ReviewFileClassification` | mcp/src/agents_remember/models/knowledge/review_lane.py:284-312; mcp/src/agents_remember/models/knowledge/review_lane.py:223-235 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new data adapter MIK-R32 adds, recording ruling 2026-09-30T12:19:20 Q1 (`paths`) and review R1 F1 (one lane read, made by the surface). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
