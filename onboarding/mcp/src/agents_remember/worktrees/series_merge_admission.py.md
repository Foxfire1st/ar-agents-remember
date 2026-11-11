# mcp/src/agents_remember/worktrees/series_merge_admission.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Prove one step of a master's spine: the history the step adds may be only official positions, sync-produced heads, a landed leaf's own history, or a pull-request merge that published one recorded landing; anything else refuses as `atomic-series-leaf-chain-invalid`. `series_closeout.py` walks the spine and calls this proof per step.

## Code Commentary

`_merge_admission` collects, for one side, the sync-produced heads (`codeHeadTo`/`memoryHeadTo`; an entry without one sets `legacy`), each landed leaf's (leaf id, base, landing) range, the leaves' publication authority ranges, the official positions and the landing workflow. `_landing_source_positions` takes the series' recorded base and, from the series contract and every ordered leaf, each sync entry's `codeBaseTo`/`memoryBaseTo` and the `codeSourceCommit`/`memorySourceCommit` a repository-default sync recorded.

`_require_admitted_step` passes a step that `_publication_merge_admits` recognises. Otherwise the start must be an ancestor of the end; the step's non-merge commits are enumerated (memory excludes root `memory.md`) and each must be a recorded position or reached by a position inside the step; then `_require_admitted_merges` judges the merges. `_positions_inside_the_step` keeps the positions the step's end reaches and its start does not, so a line merged in from the side counts and a position descending from the step does not; `_reached_by_the_official_positions` walks their history in one rev-list.

`_require_admitted_merges` lists every merge in the step. A merge passes as a recorded sync head, through the publication rule (`publication_admission.publication_merge_admitted`, which admits only under the `pull-request` workflow), as a published landing by shape (`_published_landing`), inside a landed leaf's range, or as an ancestor of a recorded position; with legacy entries, a merge already inside recorded history stays silent. Foreign merges are named with the remedy.

`_published_landing` recognises a merge by its shape alone: exactly two parents, the second a landed leaf commit H, the first an ancestor of H, and the merge's tree equal to H's tree. `_publication_merge_admits` admits a step ending at such a merge when it starts at H, or at the merge's first parent when that is H's recorded base.

Every Git read goes through `_proof_read`, `_commit_tree` or `_chain_ancestry`, so a failed read refuses naming the side and never admits; `_landing_workflow` turns an unreadable or invalid landing setting into `atomic-series-landing-workflow-invalid`.

## Relationships

`series_closeout.py` imports `_leaf_points`, `_merge_admission`, `_require_admitted_step`, `_SpineStep` and `_sync_entry_pairs`. `publication_admission.py` supplies `landing_workflow`, `publication_merge_admitted` and `publication_ranges`; refusals are `queue.closeout_queue.CloseoutQueueError`. The chain-proof tests (`test_master_chain_offenders.py`, `test_landing_unreadable_inputs.py`, `test_landing_workflow_setting.py`, `test_publication_merge_admission.py`, `test_publication_merge_shape.py`) import its private names.

## Evidence

- Merge admission collects heads, leaf ranges, authority ranges, positions and the workflow. [1]
- Recorded bases and a default sync's source tips are official positions. [2]
- A step adds only recorded positions or history a position inside the step reaches. [3]
- Inside means reached by the step's end and not by its start. [4]
- A pull-request merge is recognised by its two parents and its tree. [5]
- Every merge in the step needs an admission; foreign merges are named. [6]
- A failed Git read refuses naming the side. [7]
- A sync entry names its from, to and source pairs. [8]
