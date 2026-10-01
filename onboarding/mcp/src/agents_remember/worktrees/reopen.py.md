# mcp/src/agents_remember/worktrees/reopen.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Reopen a fully landed leaf — or a terminal atomic series — under its original id by atomically resetting its enclosure and task facts, and re-address a series whose enclosure generation was collected but never re-published.

## Code Commentary

### Logic

`reopen_task` requires a leaf whose closeout, integration, and cleanup are completed and whose code/memory worktrees are gone. It resolves the exact parent series, proves accepted memory ancestry through `require_integrated_memory_ancestry`, and uses the recorded integrated code/memory outputs as the terminal lineage position. It never reads a cache mapping or uses an integrated ledger commit.

The reset clears free-form approval/output/lifecycle provenance with dataclass replacement and changes vocabulary cells through `ContractCells` and `amend_contract`. It preserves the leaf id. Task plans reset the leaf and corresponding master row; `cleanup="reopened"` tells worktree start to recreate the enclosure rather than attach to the old one.

**The master is resolved by the one rule (MIK-R38, ruling 2026-09-30T12:33:07 Q2).** `_reopen_master_path` resolves a named `master` by its own rule and a leaf that names none through `master_sync.folder_master_json_path`, the rule the task-document master sync and the finalizer use, so its private copy of the fallback is gone. An unnamed `subTask` still finds its folder master (the row returns to `planning`, `masterIndex: reset`). A `light` document is itself the folder's `task.json`: the old fallback resolved it to itself and refused it as "not a master", and now `_plan_master_index_reset` reports `no-master`. The public route cannot reach that case, because `reopen_task`'s integration-branch preflight (`require_parent_series`) already refuses a leaf contract whose folder has no master. The master demotion is now called as `master_sync.demote_completed_master_if_unresolved` (a module-qualified import, so this file, already over 1,200 lines at base, did not grow).

**Both documents reopen rewrites must be in place (review R1 finding 1, rulings 2026-09-30T13:11:32 and 13:35:32).** `_plan_leaf_doc_reset` and `_plan_master_index_reset` call `tasks/leaf_doc.require_task_document_in_place` after their existing checks, so a leaf or master that the store would write to another file (a hand-made `light` leaf `01_x.json`, a hand-made master `other.json`, both written as the folder's `task.json`) is refused as `blocked`, in the preview and under the publication CAS, before any write. On base the misnamed light leaf crashed with `duplicate task document write target`, and the misnamed master silently replaced the series `task.json`. Correctly placed documents reopen exactly as before.

The frozen landing observation clear, leaf/master task updates, and contract reset publish in one task-fact CAS batch. Apply reloads and repeats the terminal/source checks inside that publication. Original artifacts support rollback of a failed canonical write; derived projection refresh happens afterward. Recreating worktrees remains worktree_start's responsibility.

#### The series half, and its three deciding facts

The series spelling of the same operation publishes the contract tombstone, the integration refs, the
master document and the successor enclosure generation under the same guards. Three facts decide it,
and the current candidate changed all three (D-58):

- **In flight, not `cleanup`.** `_series_in_flight` reads `closeout_status` and `integration_status`.
  It deliberately does **not** read `cleanup`, because the reopen rewrites that cell as its own first
  durable step — keying the ref rule on it would make the answer depend on whether the reset had
  already been written, which is exactly the difference between a first attempt and its resume.
- **An advanced branch may be the series' own work.** `_series_ref_recut` takes `in_flight` and, when
  the series has not closed out and the recorded source tip is an **ancestor** of the integration
  branch, reports that branch as action `advance`: it is the line the series is landing on, there is
  nothing to re-cut, and refusing would strand it. It is never moved. A completed series keeps its
  refusal, and a diverged or lagging branch is refused in both cases.
- **A live series at a collected address is re-addressed, not refused.** `_series_is_live_unaddressed`
  accepts `cleanup: pending` with both progress cells untouched when the locator at the contract's own
  address reads `terminal-archived`. The locator is the one fact that tells "the generation was
  collected" apart from "somebody is mid-transition", so the call publishes the successor generation
  alone — `mode: publish`, no reset and no ref move — which is the arrival the hand reopen left behind
  and also what a resume of an interrupted publication needs.
- **The review counter is part of the reset.** `_review_state_carries_history` reports whether the
  counter carries anything, and `_plan_series_document_reset` clears `.reviewState` to its pristine
  value when it does — the rounds a completion spent belong to that completion, so a reopened master
  starts at zero instead of billing its next round against a budget it never spent. A document whose
  counter is absent or already all-zero is left untouched, and the reset no longer returns early on a
  document that has left `Completed`.

The applied result payload therefore carries a structured `mode` (`reset` or `publish`) alongside its
`state`, and the two modes report different summaries because they did different things.

### Conventions

This owner lives in worktrees because the enclosure contract is the primary mutated artifact; the task store remains a collaborator. The parent resolver validates parent identity without restoring the deleted child-admission seal. The series half uses the same tombstone proof, the same guards and the same archive citation as the terminal path — there is no second publication route.

### Invariants And Boundaries

- Leaf identity is stable across reopen.
- A leaf naming no master is resolved by the same rule as the master sync and the finalizer (`folder_master_json_path`), and a leaf or master whose read path differs from the store's write target for it is refused before any write (MIK-R38).
- In-flight leaves, series contracts, and leaves with live worktrees cannot reopen.
- Terminal code/memory Git facts replace cache mapping proof; unrelated source movement remains a refusal.
- Vocabulary cells use the typed contract writer.
- A task/ref race cannot overwrite newer task facts or leave an old completed landing projection current.
- The reopen **never moves an existing ref**: it re-cuts an absent one, accepts an advanced one as the series' own work, and refuses divergence.
- A successor generation always cites the exact archived predecessor, and the series' own `cleanup` stays `pending` — `reopened` is itself a terminal series state and would leave the series unable to own the lane.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Terminal preflight, accepted memory ancestry, and integrated source-position checks. [1]
- Contract reset preserves identity while clearing two-output provenance. [2]
- Frozen observation, task plans, and canonical publication remain coordinated. [3]
- Whether a series still owns its integration line, read from the two progress cells a completion writes rather than from `cleanup`. [4]
- Whether a series still owns its integration line, read from the two progress cells a completion writes rather than from `cleanup`. [5]
- A series is live but unaddressed only when the locator at its own address is `terminal-archived` and both progress cells are untouched. [6]
- A series is live but unaddressed only when the locator at its own address is `terminal-archived` and both progress cells are untouched. [7]
- An advanced integration branch is the in-flight series' own landed work: reported as `advance`, never moved; divergence still refuses. [8]
- The reopen clears the review counter a completion spent, and only when the counter carries history. [9]
- The reopen clears the review counter a completion spent, and only when the counter carries history. [10]
- The publication `mode` (`reset` or `publish`) is decided by the arrival, not by a caller flag. [11]
- The publication `mode` (`reset` or `publish`) is decided by the arrival, not by a caller flag. [12]
- An unnamed leaf's master through the shared helper; a named reference by reopen's own rule. [13]
- The master reset refuses a misplaced master before planning its row, and keeps the demotion rule. [14]
- The leaf reset refuses a misplaced leaf before planning its reset. [15]
- The shared rule. [16]
- Parent lineage compares exact prestart output positions to the configured parent source. [17]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
