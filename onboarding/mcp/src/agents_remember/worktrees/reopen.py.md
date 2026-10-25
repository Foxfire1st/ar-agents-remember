# mcp/src/agents_remember/worktrees/reopen.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Plans and publishes a task reopen transition under the existing repository, contract and recovery admission.

## Code Commentary

`_plan_leaf_doc_reset` resolves the canonical leaf document, resets status/lifecycle fields and appends its reopen decision without publishing. `_plan_master_index_reset` updates its exact master row. `_publish_reopen_transition` owns the paired publication and recovery artifacts; `_restore_reopen_artifacts` restores those on failure. Series dispatch delegates to `reopen_series.py`, which retains its own document/review-reset helpers; their relocation is not retirement or permission to reset an active review. A reader of this card may not edit task state or invoke reopen outside its admitted workflow.

### Logic

`reopen_task` requires a leaf whose closeout, integration, and cleanup are completed and whose code/memory worktrees are gone — except a leaf that already carries the reopen tombstone (`cleanup: reopened` with `restartable_predecessor_contract`), which answers `reopened` again with the same next step and changes nothing. It resolves the exact parent series, proves accepted memory ancestry through `require_integrated_memory_ancestry`, and uses the recorded integrated code/memory outputs as the terminal lineage position. It never reads a cache mapping or uses an integrated ledger commit.

The repeat answer is tried first (`_already_reopened_result`) and returns before the preflight, the memory-ancestry proof and every publication: no document is reset, `frozenLanding` is a dry-run clear and `projectionEffects` is empty. It declines when either worktree still exists, because a started generation is live work rather than a reset that has not happened; `_reopen_blockers` shares that one `_live_worktree_blockers` list so the two answers cannot disagree.

**The master is resolved by the one rule (MIK-R38, ruling 2026-09-30T12:33:07 Q2).** All three writers use master_json_path_from_ref for named masters and folder_master_json_path for unnamed leaves. An unnamed `subTask` still finds its folder master (the row returns to `planning`, `masterIndex: reset`). A `light` document is itself the folder's `task.json`: the old fallback resolved it to itself and refused it as "not a master", and now `_plan_master_index_reset` reports `no-master`. The public route cannot reach that case, because `reopen_task`'s integration-branch preflight (`require_parent_series`) already refuses a leaf contract whose folder has no master; when that parent file is absent the refusal names it (`missing at <path>`), so the reader can see what to restore. The master demotion is now called as `master_sync.demote_completed_master_if_unresolved` (a module-qualified import, so this file, already over 1,200 lines at base, did not grow).

**Both documents reopen rewrites must be in place (review R1 finding 1, rulings 2026-09-30T13:11:32 and 13:35:32).** `_plan_leaf_doc_reset` and `_plan_master_index_reset` call `tasks/leaf_doc.require_task_document_in_place` after their existing checks, so a leaf or master that the store would write to another file (a hand-made `light` leaf `01_x.json`, a hand-made master `other.json`, both written as the folder's `task.json`) is refused as `blocked`, in the preview and under the publication CAS, before any write. On base the misnamed light leaf crashed with `duplicate task document write target`, and the misnamed master silently replaced the series `task.json`. Correctly placed documents reopen exactly as before.

Preview and protected publication supply the shared scope owner with each prepared document's explicit JSON path. The frozen landing observation clear, leaf/master task updates, and contract reset publish in one task-fact CAS batch. Apply reloads and repeats the terminal/source checks inside that publication. Original artifacts support rollback of a failed canonical write; derived projection refresh happens afterward. Recreating worktrees remains worktree_start's responsibility.

**The series half shares the terminal path's publication route.** The series half uses the same tombstone proof, the same guards and the same archive citation as the terminal path — there is no second publication route.

### Invariants And Boundaries

- Leaf identity is stable across reopen.
- A leaf naming no master is resolved by the same rule as the master sync and the finalizer (`folder_master_json_path`), and a leaf or master whose read path differs from the store's write target for it is refused before any write (MIK-R38).
- The leaf route refuses in-flight leaves and leaves with live worktrees. Series contracts dispatch to their separately guarded `reopen_series` plan; they are not categorically refused by this entry.
- Recorded landing commits must be ancestors of current source tips; behind-tip cleaned leaves reopen under the same id and worktree_start recreates from current tips, without suggesting sync of absent worktrees.
- A task/ref race cannot overwrite newer task facts or leave an old completed landing projection current.

### Todos

No new file-local follow-up is identified by this source reconciliation.


## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.


### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.


- `_plan_leaf_doc_reset` owns the current boundary described above. [18]

- `_plan_master_index_reset` owns the current boundary described above. [19]

- `_publish_reopen_transition` owns the current boundary described above. [20]
- `_restore_reopen_artifacts` owns the current boundary described above. [21]


- Terminal preflight, accepted memory ancestry, and integrated source-position checks. [22]

- Contract reset preserves identity while clearing two-output provenance. [23]
- Frozen observation, task plans, and canonical publication remain coordinated. [24]

- `_reopen_master_path` resolves an unnamed leaf's master through the shared folder rule and a named reference through the shared `master_json_path_from_ref` resolver, refusing a reference that leaves the task folder. [25]

- The master reset refuses a misplaced master before planning its row, and keeps the demotion rule. [26]
- The leaf reset refuses a misplaced leaf before planning its reset. [27]

- The shared rule. [28]

- Parent lineage compares exact prestart output positions to the configured parent source. [29]
- The series half shares the terminal path's tombstone proof, guards and archive citation. [30]


### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

## Current source evidence


- Leaf reopen supplies actual path/document pairs in preview and under the existing publication authority. [31]
