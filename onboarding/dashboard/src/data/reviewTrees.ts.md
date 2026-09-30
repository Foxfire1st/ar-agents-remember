# dashboard/src/data/reviewTrees.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewTrees.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
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
source path, each invariant's MIK-R03 currentness per side, and the MIK-R08 worklist view.

## Code Commentary

### Logic

- `reviewTrees(repo, master, leaf, address)` builds the query: `comparison=<n>` for a recorded comparison,
  `history=recorded` for the latest record, never a path or a tree id; the request goes through the shared
  `getReviewJson`.
- `reviewTreesRead` keeps three answers apart: `trees` (only with its comparison), `not-converted` (the dataset
  review applies; nothing here does) and `unavailable` with the owner's refusal; any other body is
  `unreadableAnswer`, in the shared review vocabulary.
- `degradedKnowledgeSides` returns a side that is not `available`, and also an `available` side read from a
  `partial` index, so neither is presented as complete. `invariantCurrentness` reads one invariant's state on each
  side. `unexplainedHunks` lists the hunks the gate linked to no recorded knowledge.
- `useReviewTrees` keys the read by task context and address and drops a superseded answer by sequence number.
- `ReviewTreesResult.code_sides` is present on a reopened comparison (review F4).

### Conventions

- The types mirror the Python model faithfully, including its mixed key casing (review F9).

### Invariants And Boundaries

- No component renders this view yet: the adapter and hook are the leaf's delivery within its Scope (ruling 22:22:37 Q2). The worker's knip run lists `useReviewTrees` and the new types as unused exports.

### Todos

- **L31 (ruling 22:22:37 Q2; review F9):** the panel that renders rules 2 and 3, and unifying the key casing.

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
| The side states and the comparison record's client type. | `ReviewTreeSideState`; `ReviewTreeComparison` | dashboard/src/data/reviewTrees.ts:33-60 |
| A knowledge side and a reopened code side. | `ReviewKnowledgeSide`; `ReviewCodeSide` | dashboard/src/data/reviewTrees.ts:62-77 |
| The tree view's answer. | `ReviewTreesResult` | dashboard/src/data/reviewTrees.ts:166-179 |
| The request, addressed by number or `recorded`, never by path. | `ReviewTreesAddress`; `reviewTrees` | dashboard/src/data/reviewTrees.ts:183-199 |
| Three answers kept apart; anything else is unreadable. | `ReviewTreesRead`; `reviewTreesRead` | dashboard/src/data/reviewTrees.ts:202-216 |
| Degraded sides, per-side currentness, unexplained hunks. | `degradedKnowledgeSides`; `invariantCurrentness`; `unexplainedHunks` | dashboard/src/data/reviewTrees.ts:220-248 |
| The hook, dropping a superseded answer. | `useReviewTrees` | dashboard/src/data/reviewTrees.ts:252-277 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new adapter MIK-R25 adds, recording ruling 22:22:37 Q2 and review F4 and F9. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
