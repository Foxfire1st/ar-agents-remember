# mcp/src/agents_remember/models/knowledge/review_trees.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_trees.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The two shapes of MIK-R25: a review comparison as four Git trees, and the reviewer's tree view of it.**

- `ReviewTreeComparisonRecord` (`ar-review-tree-comparison/v1`) is the durable record of one comparison
  (rule 1): the task id (the task directory name), the leaf id, the number `<n>`, the four sides and, for a before
  side that was unconverted when compared, the conversion it was read as. It is written under
  `notes/reports/review-comparisons/<leaf>/<n>.json` by `application/review_tree_comparison.py`.
- `ReviewTreesResult` is what `GET /api/review/trees` returns for one leaf: `trees`, `not-converted` or `refused`,
  with the comparison, each knowledge side, each reopened code side, the knowledge diff, the per-side currentness
  and the worklist view; or, for a cards read that names invariants (MIK-R31), the comparison, the sides and
  `entries` only (`ReviewTreeEntry`, `models/knowledge/review_tree_entries.py`); or, since MIK-L32, for a lane read
  (`lane=files`) the comparison, the sides and `lane`, or for a file read (`file=<path>`) `file_classification`
  (`ReviewUnexplainedLane` and `ReviewFileClassification`, `models/knowledge/review_lane.py`).

No database copy is part of either shape: each knowledge side is the derived index of its tree (MIK-R23), rebuilt
from the tree and never retained with the comparison.

## Code Commentary

### Logic

- `REVIEW_REF_NAMESPACE = "refs/ar/review"`: outside `refs/heads` and `refs/remotes`, so nothing fetches, pushes
  or merges a pin, and the archive hook finds every pin of a task with one `for-each-ref` over
  `refs/ar/review/<task-directory>/`.
- `ReviewTreeSideState`: `available`, `unavailable-history` (Git can no longer produce the tree; it is named and
  nothing is substituted) or `legacy-unavailable` (a knowledge side recorded before the repository's conversion).
- `ReviewTreeSide`: repository, tree, and exactly one of `commit` (a committed side) or `ref` (the pin of an
  uncommitted side) on a side the reviewer recorded.
- `ReviewConvertedBase`: the memory commit, the pinned conversion version, the code commit it was anchored at and
  the tree it produced; a reopen re-derives it and checks the tree id rather than pinning it.
- `ReviewTreeComparisonRecord.same_trees` compares the task, the leaf, the four `(repository, tree)` pairs and the
  converted base. Comparing `task_id` and `leaf_id` is the 2026-09-30T02:32:42 change: a record written under
  another naming (the earlier `task.json` id) is never reused, and its pins are never re-created under the old name.
  Number `0` marks a closed leaf's recorded committed endpoints, which need no ref and no record of their own.
- `ReviewKnowledgeSide` carries `index_state` (`complete` or `partial`) and `problems`, so a side read from a
  partial index is never presented as complete (Failure and Recovery). `ReviewCodeSide` (review F4) marks a
  reopened code tree `available` or `unavailable-history`.
- The diff shapes: `ReviewKnowledgeFileChange` (path, old path, status, patch, truncated),
  `ReviewKnowledgeRecordGroup` (files and the changed entries naming the record as `(entry id, source path,
  change)`), `ReviewKnowledgeSourceGroup` and `ReviewKnowledgeTreeDiff` (records, sources, history, other).
- `ReviewWorklistView`: `source` (`computed`, `persisted` or `absent`), `bound`, the items verbatim, the history rows
  without a currency mark (MIK-R09 owns that rule), the gate linkage `changes` and `incomplete`.
- `ReviewTreesResult.entries` (MIK-L31) defaults to `()`: the leaf-wide view never carries entries, because every
  entry's excerpt leaf-wide measured 637 KB on the real repository; only the on-demand cards read fills it.
- `ReviewTreesResult.lane` and `ReviewTreesResult.file_classification` (MIK-L32) default to `None`: only a lane read
  or a file read fills the one it asked for, and the leaf-wide view carries neither. A file read the application
  refuses is `state: "refused"` with the comparison and the refusal.

### Conventions

- Every model is a frozen `KnowledgeModel` with bounded strings and Git object patterns; the record's `schema`
  field uses the alias `schema`.

### Invariants And Boundaries

- The record names trees, commits and refs only, never a database path.

### Todos

- **Resolved by MIK-L31 (review F9):** the embedded currentness and worklist documents are re-keyed to snake_case at
  the route boundary (`application/review_tree_knowledge.py`, `snake_keys`), so the whole body follows the model
  fields' convention.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R25@v1` with its rulings in `25_reviewer-on-git-trees.json`; they live outside the code and memory
repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The record schema and the one ref namespace pins live under. | `REVIEW_TREE_COMPARISON_SCHEMA`; `REVIEW_REF_NAMESPACE` | mcp/src/agents_remember/models/knowledge/review_trees.py:58-60; mcp/src/agents_remember/models/knowledge/review_trees.py:64-64 |
| The three states a side can resolve to when read back. | `ReviewTreeSideState` | mcp/src/agents_remember/models/knowledge/review_trees.py:73-73 |
| One tree, kept alive by a commit or a pinning ref. | `ReviewTreeSide` | mcp/src/agents_remember/models/knowledge/review_trees.py:76-86 |
| The conversion an unconverted base was read as, recorded by its inputs and tree id. | `ReviewConvertedBase` | mcp/src/agents_remember/models/knowledge/review_trees.py:89-100 |
| The record, and one comparison being the same task, leaf, four trees and converted base. | `ReviewTreeComparisonRecord`; `same_trees` | mcp/src/agents_remember/models/knowledge/review_trees.py:103-143 |
| A knowledge side with its index state and problems; a reopened code side. | `ReviewKnowledgeSide`; `ReviewCodeSide` | mcp/src/agents_remember/models/knowledge/review_trees.py:146-159; mcp/src/agents_remember/models/knowledge/review_trees.py:162-168 |
| The diff of the memory trees, grouped by record and by source path. | `ReviewKnowledgeRecordGroup`; `ReviewKnowledgeSourceGroup`; `ReviewKnowledgeTreeDiff` | mcp/src/agents_remember/models/knowledge/review_trees.py:181-192; mcp/src/agents_remember/models/knowledge/review_trees.py:195-200; mcp/src/agents_remember/models/knowledge/review_trees.py:203-216 |
| The worklist view: items, history rows without a mark, gate linkage. | `ReviewWorklistView` | mcp/src/agents_remember/models/knowledge/review_trees.py:219-236 |
| The route's answer: trees, not converted, or refused; the cards' entries, empty on the leaf-wide view (MIK-R31); the lane or one file's classification, only when asked (MIK-R32). | `ReviewTreesState`; `ReviewTreesResult`; "file_classification: ReviewFileClassification" | mcp/src/agents_remember/models/knowledge/review_trees.py:239-239; mcp/src/agents_remember/models/knowledge/review_trees.py:242-264 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): **body update for MIK-R32.** Purpose and Logic record `ReviewTreesResult.lane` and `file_classification` (filled only by a lane or file read). The route-answer row is reworded for them and re-measured: the installed fixer's normalisation had added `239-239` and kept the old `235-235`, which now holds neither anchor, so that range is dropped and the row cites `239-239; 242-264`. The other rows moved by the new import were re-pointed by the installed fixer (its bullet kept) or by the exact shift. No verification stamp was advanced.
- 2026-09-30T12:07:44+00:00: Generated citation repair: `ReviewTreeSideState` repointed to mcp/src/agents_remember/models/knowledge/review_trees.py:73-73. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Purpose and Logic record `ReviewTreesResult.entries` for the on-demand cards read (ruling 05:36:19 Q2; empty on the leaf-wide view); the F9 Todo is marked resolved (the route re-keys the embedded documents). The `ReviewTreesResult` row is reworded for the new field.
- 2026-09-30T07:53:29+00:00: Generated citation repair: `REVIEW_TREE_COMPARISON_SCHEMA`; `REVIEW_REF_NAMESPACE` repointed to mcp/src/agents_remember/models/knowledge/review_trees.py:54-56; mcp/src/agents_remember/models/knowledge/review_trees.py:60-60. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T07:53:29+00:00: Generated citation repair: `ReviewTreeSideState` repointed to mcp/src/agents_remember/models/knowledge/review_trees.py:69-69. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new file MIK-R25 adds, recording review F4 and F9 (23:15:34) and ruling 02:32:42 (a) on `same_trees`. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
