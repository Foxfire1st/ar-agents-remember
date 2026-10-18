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
  with the comparison, each knowledge side, each reopened code side, the per-side currentness
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
- `ReviewTreeSide`: repository and tree with optional `commit`/`ref` addresses. The recorded-side contract
  uses a commit or pin; this DTO has no validator enforcing their exclusivity and performs no Git read.
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
- `ReviewWorklistView` keeps `source` (`computed`, `persisted` or `absent`), `bound`, state/detail,
  item/history documents, gate linkage `changes` and `incomplete`. The actual owner projects item/history
  keys to snake_case; this is not byte-verbatim source transport. It now adds gate-owned `item_states`
  keyed by item identity, with `answered`/`open`/`undecided` and optional witness, row ID and reason.
  The model does not compute these answers or authenticate the binding. Its optional `code_changes`
  attribute is excluded from worklist serialization and is an internal carrier for the leaf-wide owner.
- `ReviewTreesResult.code_changes` is the new public projection of those implementation facts, separate
  from worklist judgments, authored record changes and on-demand family views. `ReviewCodeChanges`
  declares facts/unavailable, detail and invariant facts with implementation state, proof/range flags,
  evidence and unknown reasons; these DTO fields are not a CODE or MEMORY approval.
- The actual leaf-wide composer carries the worklist and its code facts onto the root result.
  `_worklist_view` consumes the isolated child's `_review` output, validates its typed values and
  refuses a complete live child result bound to a different comparison. This wrapper is not an
  independent second gate predicate.
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
- Constructor shape is not full state admission: these DTOs do not independently enforce that a
  refusal, optional result fields, bound flag or item verdict actually came from a particular read.
  The owning readers/gate establish that context.
- `same_trees` compares task/leaf, repository/tree pairs and converted base, not commit/ref spellings,
  record number or timestamp.

### Todos

- **Resolved by MIK-L31 (review F9):** the embedded currentness and worklist documents are re-keyed to snake_case at
  the route boundary (`application/review_tree_knowledge.py`, `snake_keys`), so the whole body follows the model
  fields' convention.

`ReviewTreesResult` has no `knowledge_diff` field at either the actual c861abfe BASE or freeze07.
Its earlier removal is preserved context, not a new removal in this source delta. The standalone diff models
`ReviewKnowledgeFileChange`, `ReviewKnowledgeRecordGroup`, `ReviewKnowledgeSourceGroup` and
`ReviewKnowledgeTreeDiff` remain available for shared consumers; their presence does not put patches
back into the route answer. Comparison records, side/index states, code sides, currentness, worklist,
per-selection entries and focused lane/file answers retain their distinct contracts.
## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R25@v1` with its rulings in `25_reviewer-on-git-trees.json`; they live outside the code and memory
repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The comparison schema and dedicated review-ref namespace. [1]

- The side state vocabulary distinguishes available, unavailable-history and legacy-unavailable. [2]

- A side names repository/tree and optional commit/ref; this declaration does not enforce exclusive presence. [3]

- Conversion context records its source commit, format version, anchoring code commit and resulting tree. [4]

- Comparison identity uses task, leaf, repository/tree pairs and converted base rather than timestamp, number or commit/ref spelling. [5]

- Knowledge sides carry index state/problems; reopened code sides distinguish available from unavailable history. [6]

- Standalone memory-diff carriers group file changes by record/source and retain history/other populations. [7]

- The worklist carries documents, bound/source metadata, typed gate verdicts and an excluded internal code-facts attribute. [8]

- The public result has route states, comparison/sides/currentness/worklist, new code facts and optional focused entry/lane/file payloads. [9]

- The reopened-code-side carrier remains available, independently of standalone diff shapes. [10]

- The result keeps per-side currentness beside its side descriptors. [11]

- The result retains the worklist and separately adds the public code-facts projection. [12]

- The shared standalone diff carriers remain public exports. [13]

- Shared standalone file/record/source/tree diff definitions survive; they do not imply an embedded leaf-wide patch field. [14]

- The root result has no knowledge_diff field at BASE or current source; its added field is code_changes. [15]

- The actual worklist owner validates child review parts, projects document keys and rejects a complete live result bound to another comparison. [16]

- Gate verdict and implementation-fact DTOs retain different states and optional evidence/reason fields; neither is a review approval. [17]

### Cross-Repo References

No external-system boundary is implemented by this value model. All cited owners are in the same repository.
