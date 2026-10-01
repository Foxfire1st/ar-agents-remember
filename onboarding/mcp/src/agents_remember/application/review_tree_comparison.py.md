# mcp/src/agents_remember/application/review_tree_comparison.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**A review comparison as four Git trees, pinned by Git refs and reopened from its tree ids (MIK-R25 rules 1, 2
and 4).** With knowledge as text in Git (D18), every committed state of both repositories is already a tree, so
a review compares four trees and copies nothing:

- **B**, the code base: the contract's `code_base_commit`, peeled to its tree;
- **C**, the code candidate: the leaf's code worktree captured through the landed private-index capture (the
  same tree the dataset review already binds);
- **K_B**, the memory base: the memory commit the MIK-R08 worklist pairs with B (`paired_memory_commit`), so the
  reviewer and the worklist compare the same sides (worker item 7, accepted under ruling 22:22:37 Q7, "accepted as listed");
- **K_C**, the memory candidate: the leaf's memory worktree captured through a private index.

Each memory side is then opened through the MIK-R23 derived index of its tree. That index is a dataset of the
store's schema, so the landed review composition runs over it unchanged (rule 6) and **no database copy is
created, retained or read** (ruling 22:22:37 Q1: the derived index is the permitted read path).

## Code Commentary

### Logic

- **Applicability.** `memory_converted(contract)` is true when the memory worktree holds the layout marker or
  the official memory line's tip does (`official_line_converted`). Before the cutover (MIK-R37) neither holds for
  a production leaf, so `live_review_trees` returns `None` and the dataset review runs byte for byte as before.
- **The live draft.** `_live_draft` resolves B (`_require` refuses a revision that names nothing), K_B through
  `paired_memory_commit` (its failure is raised as `TreeSideUnreadable("memory base", …)`, named rather than
  guessed), captures K_C (`_capture`, a private index in a temporary directory) and asks `converted_base_side`
  whether K_B must be read as its conversion. The draft record's `task_id` is `review_task_id(task_root)`.
- **The review-ref namespace is the task directory name only.** `review_task_id(task_root)` returns
  `task_root.name` and reads nothing (ruling 2026-09-30T02:32:42 (a)). Pins, the recorded-range comparison
  (`review_legacy_comparison`) and the archive hook (`review_artifact_cleanup`, through `request.task_name`) all
  name the namespace this way, so no file under the task folder — not even `task.json`'s `id` — can move a pin,
  or its archival, into another task's namespace. This replaced the fix round's `task.json`-id function (F5,
  23:15:34) and the confirmed-id rule (01:37:42, 02:12:06), which now serve only the legacy cleanup targets.
  `review_ref` refuses a segment that is empty, contains `/` or `\`, or is `.`/`..`.
- **Committed or pinned.** `_candidate_side` marks a candidate committed only when the durable source line's tip
  holds exactly its tree (worker item 8, accepted under ruling 22:22:37 Q7); then it records the commit and needs no ref. Any other candidate is
  pinned.
- **Recording and pinning (rule 1).** `_record` reuses the latest record when `same_trees` holds (same task, leaf,
  four trees and converted base), re-creating a pin that has gone; otherwise it numbers the comparison one past
  every recorded number and every existing ref number, pins, and only then writes
  `notes/reports/review-comparisons/<leaf>/<n>.json` atomically. `_pin` is create-only (`update-ref <ref> <tree>
  <zero>`): a pin already naming its tree is kept, a ref naming anything else is never moved, and on any failure
  the pins this call made are removed and the comparison is refused by `_pin_refusal`, naming the repository and
  the ref (Failure and Recovery).
- **The converted base (rule 4, MIK-R24 rule 7).** When K_B lacks the layout marker and K_C has it,
  `converted_base_side` converts K_B at its own paired code commit (else B) and the pinned conversion version,
  through the worklist's converted-base cache, and `write_files_tree` writes the files as blobs and trees into the
  memory repository's object store (`hash-object -w`, recursive `mktree`): objects only, no ref, no index and no
  working tree, and the same files always give the same tree id. The record names the conversion's inputs
  (`ReviewConvertedBase`); a reopen re-derives it and checks the id instead of pinning it.
- **Opening the sides (rule 2).** `_open_sides`/`_open_side` open each memory tree through
  `KnowledgeIndexCache.for_git_tree`; an index failure makes that side `unavailable-history` with the reason, and a
  partial index carries `index_state` and `problems` (Failure and Recovery).
- **Reopen (rule 4).** `reopen_review_trees` picks the named or latest record; `reopened_trees` marks each
  memory tree Git can no longer produce as `unavailable-history` (`_missing_tree` names the tree and the
  repository), re-derives a missing converted base and compares its id (`_before_state`), and — review F4 — reports
  both code trees through `_code_sides` as `available` or `unavailable-history`. Today's tree is never substituted.
- **What the landed composition reads.** `tree_resolution` builds the landed `ReviewCandidateResolution` over the
  two index files and the two code trees, with `trees` set; an unavailable side names a path under
  `.review-knowledge-unavailable/` that is never created, so no read can reach a database in its place.
  `tree_sides_refusal` and `tree_limitations` are the refusal and the declared facts
  (`review:trees:<n>`, `history:intent:<side>:<state>`, `knowledge-index:<side>:<state>`, and
  `history:code:<side>:unavailable-history:<tree>`).
- `recheck_memory_candidate` recaptures a live memory worktree before publication and refuses when it moved.

### Conventions

- Every Git call goes through `_git` with the metadata timeout; a failed call answers `None` and the caller names
  the side.
- The record schema is `ar-review-tree-comparison/v1` (`models/knowledge/review_trees.py`).

### Invariants And Boundaries

- **Candidate invariant (not ingested): a review comparison pins its candidates before it is shown, and a repeat
  read writes nothing.** Realized by `_record` (reuse on `same_trees`, write after pinning) and `_pin`
  (create-only, keep a pin naming its tree, roll back on failure). Proved by
  `test_a_live_review_is_four_trees_with_its_uncommitted_candidates_pinned_and_reused`,
  `test_committed_candidates_need_no_ref_and_a_failed_pin_refuses_naming_repository_and_ref` and
  `test_a_read_writes_only_review_refs_and_comparison_objects_and_a_repeat_writes_nothing` (every ref, every object
  and every record file byte-identical after the repeat reads). Ruling 22:22:37 Q5 and review F6 (23:15:34) accept
  that a review GET writes, confined to `refs/ar/review/`, the objects the comparison needs, the task's
  comparison record and the index and converted-base caches, all idempotent.
- **Candidate invariant (not ingested): review refs are named by the task directory name only.** Realized by
  `review_task_id`. Proved by `test_pins_are_named_by_the_task_directory_and_archival_removes_them`, and on real
  data by the reviewer's R6 probes V10, V12, V13 and V14 (only the task's own `refs/ar/review/<dir>/…` deleted).
- **Candidate invariant (not ingested): a tree Git can no longer produce is reported `unavailable-history`, never
  substituted.** Realized by `reopened_trees`, `_missing_tree`, `_before_state`, `_code_sides` and
  `tree_sides_refusal`. Proved by
  `test_a_comparison_reopens_from_its_tree_ids_and_names_a_tree_git_can_no_longer_produce` (memory and code
  repositories garbage-collected; the refusal's offending input is `after:unavailable-history:<tree>`) and the
  worker's real `reopen-run.txt`.
- **Candidate invariant (not ingested): unconverted memory reads are unchanged.** `live_review_trees` and
  `reopen_review_trees` return `None` for an unconverted leaf, so the dataset path runs as before. Proved by
  `test_an_unconverted_leaf_keeps_the_dataset_review` and by the base-against-worktree comparison of 29 payloads,
  byte-identical (worker `unconverted-compare.txt`; reviewer R6 item 8).
- The code and memory repositories must differ: the ref path is the same in both (worker item 9, accepted as listed under ruling 22:22:37 Q7: not
  handled, since no real deployment shares them).

### Todos

- **L31 (ruling 22:22:37 Q2):** the panel that renders rules 2 and 3.
- **L37 (ruling 22:22:37 Q4):** the cutover notes state that the tree review, and the archive hook, apply once
  this build is installed.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R25@v1` of task `260928_maintained-invariant-knowledge`, with its architect rulings in the leaf document
`25_reviewer-on-git-trees.json` (2026-09-29T22:22:37, 23:15:34; 2026-09-30T00:08:39, 01:00:07, 01:37:42, 02:12:06,
02:32:42); they live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The comparison and each memory side's index, with the live flag and the reopened code sides. [1]
- A leaf's review is a tree review when its memory worktree or its official line holds the layout marker. [2]
- The review-ref task segment is the task directory name, and nothing read from the folder. [3]
- The ref name, refusing a segment that could leave its place. [4]
- Where a leaf's records live, and every readable record by number. [5]
- Capture, pin and record a live leaf's four trees; none for an unconverted leaf. [6]
- The four sides of a live draft, K_B through the worklist's pairing. [7]
- A live memory candidate that moved during composition is refused. [8]
- Committed only when the durable line's tip holds exactly this tree. [9]
- An unconverted memory base read as its conversion, written as a Git tree. [10]
- Reuse on the same trees, else number, pin, then write the record. [11]
- Create-only pins, rolled back and refused naming repository and ref. [12]
- Each memory side opened through its tree's index; an index failure is `unavailable-history`. [13]
- Reopen from the recorded tree ids, marking every tree Git can no longer produce, code trees included. [14]
- A missing converted base is re-derived and its id checked; a missing tree is named. [15]
- The refusal and the declared facts of a tree comparison. [16]
- The landed resolution over two index files; an unavailable side names no file. [17]
- Pins, reuse and the refused pin. [18]
- A repeat read writes nothing. [19]

### Cross-Repo References

The module writes refs and objects into the leaf's own code and memory repositories, the two its series contract
names; it reaches no other repository.

No cross-repo boundary is crossed by this file.
