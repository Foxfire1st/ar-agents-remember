# mcp/src/agents_remember/models/knowledge/review_trees.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_trees.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
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
  and the worklist view.

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

### Conventions

- Every model is a frozen `KnowledgeModel` with bounded strings and Git object patterns; the record's `schema`
  field uses the alias `schema`.

### Invariants And Boundaries

- The record names trees, commits and refs only, never a database path.

### Todos

- **L31 (review F9, ruling 23:15:34):** the model fields are snake_case while the embedded currentness and worklist
  documents are camelCase; unify when the panel renders them.

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
| The record schema and the one ref namespace pins live under. | `REVIEW_TREE_COMPARISON_SCHEMA`; `REVIEW_REF_NAMESPACE` | mcp/src/agents_remember/models/knowledge/review_trees.py:53-59 |
| The three states a side can resolve to when read back. | `ReviewTreeSideState` | mcp/src/agents_remember/models/knowledge/review_trees.py:61-68 |
| One tree, kept alive by a commit or a pinning ref. | `ReviewTreeSide` | mcp/src/agents_remember/models/knowledge/review_trees.py:71-81 |
| The conversion an unconverted base was read as, recorded by its inputs and tree id. | `ReviewConvertedBase` | mcp/src/agents_remember/models/knowledge/review_trees.py:84-95 |
| The record, and one comparison being the same task, leaf, four trees and converted base. | `ReviewTreeComparisonRecord`; `same_trees` | mcp/src/agents_remember/models/knowledge/review_trees.py:98-138 |
| A knowledge side with its index state and problems; a reopened code side. | `ReviewKnowledgeSide`; `ReviewCodeSide` | mcp/src/agents_remember/models/knowledge/review_trees.py:141-163 |
| The diff of the memory trees, grouped by record and by source path. | `ReviewKnowledgeRecordGroup`; `ReviewKnowledgeSourceGroup`; `ReviewKnowledgeTreeDiff` | mcp/src/agents_remember/models/knowledge/review_trees.py:176-211 |
| The worklist view: items, history rows without a mark, gate linkage. | `ReviewWorklistView` | mcp/src/agents_remember/models/knowledge/review_trees.py:214-231 |
| The route's answer: trees, not converted, or refused. | `ReviewTreesState`; `ReviewTreesResult` | mcp/src/agents_remember/models/knowledge/review_trees.py:234-254 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new file MIK-R25 adds, recording review F4 and F9 (23:15:34) and ruling 02:32:42 (a) on `same_trees`. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
