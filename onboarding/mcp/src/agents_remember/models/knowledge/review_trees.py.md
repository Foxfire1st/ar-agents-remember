# mcp/src/agents_remember/models/knowledge/review_trees.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R25@v1` with its rulings in `25_reviewer-on-git-trees.json`; they live outside the code and memory
repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The record schema and the one ref namespace pins live under. [1]
- The three states a side can resolve to when read back. [2]
- One tree, kept alive by a commit or a pinning ref. [3]
- The conversion an unconverted base was read as, recorded by its inputs and tree id. [4]
- The record, and one comparison being the same task, leaf, four trees and converted base. [5]
- A knowledge side with its index state and problems; a reopened code side. [6]
- The diff of the memory trees, grouped by record and by source path. [7]
- The worklist view: items, history rows without a mark, gate linkage. [8]
- The route's answer: trees, not converted, or refused; the cards' entries, empty on the leaf-wide view (MIK-R31); the lane or one file's classification, only when asked (MIK-R32). [9]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
