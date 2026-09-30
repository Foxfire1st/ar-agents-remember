# dashboard/src/data/reviewTrees.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewTrees.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The client adapter of the reviewer's tree view (MIK-R25): `GET /api/review/trees`, typed after
`models/knowledge/review_trees.py` and served by `serving/review_trees.py`.** For a leaf whose memory is converted,
a review comparison is four Git trees and each memory side is read through the derived index of its tree. The
landed review adapter (`data/review.ts`) keeps its shape and behaviour — only its data source changed (rule 6).
This adapter carries what that payload does not: the comparison (four trees and the pinning refs), each knowledge
side's state and index state, the reopened code sides, the Git diff of the memory trees grouped by record and by
source path, each invariant's MIK-R03 currentness per side, and the MIK-R08 worklist view. Since MIK-L31 it also
carries every realization and proof entry of a selection, located on both code sides (`ReviewTreeEntry`), for the
focused expression cards, and the leaf-wide read the knowledge panel and the cards' planning marks use.

## Code Commentary

### Logic

- `reviewTrees(repo, master, leaf, address)` builds the query: `comparison=<n>` for a recorded comparison,
  `history=recorded` for the latest record, `invariants=<a,b,…>` for one selection's entries (MIK-L31, ruling
  2026-09-30T05:36:19 Q2), never a path or a tree id; the request goes through the shared `getReviewJson`.
- `treeComparisonNumber(limitations)` reads the recorded tree comparison a landed review payload was composed over
  from its `review:trees:<n>` limitation token; a payload without it is a dataset review, for which no tree read is
  made at all.
- `useReviewTreeEntries(repo, master, leaf, comparison, invariants)` reads one selection's entries from the
  comparison the payload names, keeps the answer with the question it answers (so a superseded selection never
  draws its cards), and returns `null` when there is no comparison number or no invariant (the dataset path).
- `reviewTreesRead` keeps three answers apart: `trees` (only with its comparison), `not-converted` (the dataset
  review applies; nothing here does) and `unavailable` with the owner's refusal; any other body is
  `unreadableAnswer`, in the shared review vocabulary.
- `degradedKnowledgeSides` returns a side that is not `available`, and also an `available` side read from a
  `partial` index, so neither is presented as complete. `invariantCurrentness` reads one invariant's state on each
  side. `unexplainedHunks` lists the hunks the gate linked to no recorded knowledge.
- `useReviewTrees` keys the read by task context and address and drops a superseded answer by sequence number. Its
  `enabled` flag (MIK-L31) makes no request and returns `null` when false; the workspace passes
  `{ comparison }` with the payload's own number and enables it only for a tree comparison (review F11).
- `ReviewTreesResult.code_sides` is present on a reopened comparison (review F4).

### Conventions

- The types mirror the Python model faithfully. Every key is snake_case (MIK-L25 review F9, settled by MIK-L31: the
  server re-keys the owners' camelCase documents), so `code_tree.tree_id`, `stale_members`, `index_state`,
  `unverifiable_reason` and `file_level` replace the old camelCase fields. `ReviewWorklistItem` (with MIK-R11's
  `planning` and `satisfied_by`) and `ReviewWorklistHistoryRow` (with `owner_kind`) are named types now.

### Invariants And Boundaries

- Rendered since MIK-L31: `panels/review/LeafKnowledgeChanges.tsx` renders rules 2 and 3 and
  `panels/review/ExpressionCards.tsx` renders the entries (ruling 22:22:37 Q2 carried to L31).
- **Candidate invariant (not ingested): dataset reviews make no tree read.** Realized by `treeComparisonNumber`
  returning `undefined` without the token, `useReviewTrees`'s `enabled` flag and `useReviewTreeEntries` returning
  `null`. Proved by `ReviewSurface.gitTrees.test.tsx` ("leaves a dataset review exactly as it was: no tree read") and
  the reviewer's mutation (the flag forced true fails 15 tests).

### Todos

- **Resolved by MIK-L31 (ruling 22:22:37 Q2; review F9):** the panel and the cards render this view, and the key
  casing is one convention.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` and its rulings
(`25_reviewer-on-git-trees.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The side states and the comparison record's client type. | `ReviewTreeSideState`; `ReviewTreeComparison` | dashboard/src/data/reviewTrees.ts:38-38; dashboard/src/data/reviewTrees.ts:54-65 |
| A knowledge side and a reopened code side. | `ReviewKnowledgeSide`; `ReviewCodeSide` | dashboard/src/data/reviewTrees.ts:67-74; dashboard/src/data/reviewTrees.ts:77-82 |
| The tree view's answer, with a selection's entries on the cards read. | "export interface ReviewTreesResult" | dashboard/src/data/reviewTrees.ts:224-238 |
| The worklist's items, history rows and view, snake_case. | `ReviewWorklistItem`; `ReviewWorklistHistoryRow`; `ReviewWorklistView` | dashboard/src/data/reviewTrees.ts:156-185 |
| One entry on both code sides, and one side's state, range, excerpt, authored fields and MIK-R03 state. | `ReviewEntryRangeState`; `ReviewTreeEntrySide`; `ReviewTreeEntry` | dashboard/src/data/reviewTrees.ts:191-222 |
| The request, addressed by number, `recorded` or a selection's invariants, never by path. | "export interface ReviewTreesAddress"; "export const reviewTrees" | dashboard/src/data/reviewTrees.ts:242-248; dashboard/src/data/reviewTrees.ts:250-262 |
| Three answers kept apart; anything else is unreadable. | `ReviewTreesRead`; `reviewTreesRead` | dashboard/src/data/reviewTrees.ts:265-269; dashboard/src/data/reviewTrees.ts:273-279 |
| Degraded sides, per-side currentness, unexplained hunks. | `degradedKnowledgeSides`; `invariantCurrentness`; `unexplainedHunks` | dashboard/src/data/reviewTrees.ts:283-287; dashboard/src/data/reviewTrees.ts:290-300; dashboard/src/data/reviewTrees.ts:303-311 |
| The comparison a payload names; a selection's entries kept with their question; the leaf-wide hook with its `enabled` flag. | `treeComparisonNumber`; `useReviewTreeEntries`; "export function useReviewTrees(" | dashboard/src/data/reviewTrees.ts:316-322; dashboard/src/data/reviewTrees.ts:326-352; dashboard/src/data/reviewTrees.ts:356-384 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Purpose and Logic record the entry types, `invariants=` (ruling 05:36:19 Q2), `treeComparisonNumber`, `useReviewTreeEntries`, the `enabled` flag and the payload-pinned leaf-wide read (review F11 at 06:10:21), and the one snake_case convention (MIK-L25 review F9); the "no component renders this view" boundary is replaced by a candidate invariant (dataset reviews make no tree read) and the L31 Todo is marked resolved. **Reopened claims reworded and re-anchored:** the `ReviewTreesResult`, request and hook rows, now on line-exact quotes; this pass's three generated bullets for them were removed. Two rows added (the worklist types, the entry types).
- 2026-09-30T07:50:14+00:00: Generated citation repair: `ReviewTreesRead`; `reviewTreesRead` repointed to dashboard/src/data/reviewTrees.ts:265-269; dashboard/src/data/reviewTrees.ts:273-279. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T07:50:14+00:00: Generated citation repair: `degradedKnowledgeSides`; `invariantCurrentness`; `unexplainedHunks` repointed to dashboard/src/data/reviewTrees.ts:283-287; dashboard/src/data/reviewTrees.ts:290-300; dashboard/src/data/reviewTrees.ts:303-311. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new adapter MIK-R25 adds, recording ruling 22:22:37 Q2 and review F4 and F9. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
