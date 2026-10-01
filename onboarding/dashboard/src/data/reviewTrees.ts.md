# dashboard/src/data/reviewTrees.ts

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

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` and its rulings
(`25_reviewer-on-git-trees.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The side states and the comparison record's client type. [1]
- A knowledge side and a reopened code side. [2]
- The tree view's answer, with a selection's entries on the cards read. [3]
- The worklist's items, history rows and view, snake_case. [4]
- One entry on both code sides, and one side's state, range, excerpt, authored fields and MIK-R03 state. [5]
- The request, addressed by number, `recorded` or a selection's invariants, never by path. [6]
- Three answers kept apart; anything else is unreadable. [7]
- Degraded sides, per-side currentness, unexplained hunks. [8]
- The comparison a payload names; a selection's entries kept with their question; the leaf-wide hook with its `enabled` flag. [9]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
