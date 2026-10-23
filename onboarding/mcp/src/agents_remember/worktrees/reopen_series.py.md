# mcp/src/agents_remember/worktrees/reopen_series.py

## Governing Overview

[mcp/src/agents_remember/worktrees/overview.md](overview.md)

## Purpose

Series handling for reopened worktrees.

## Code Commentary

The owner keeps a reopened leaf's series membership and history-file target consistent while the new attempt proceeds. Projection scope construction passes each prepared document with its actual JSON path to the shared task-fact owner rather than assuming an unlocated document tuple.

Master reopen plans from the master's own refs against the sprint that commands it. A missing series source branch is reported with that sprint's recorded status when the sprint is no longer `inProgress` (`_commanding_sprint_state`), because a master's branches are restored from the sprint's integration branch: "this branch does not exist" alone leaves the reader guessing whether the sprint still owns the lane. The rest of the re-cut order and the adoption/reconstruction rules are unchanged.

### A completed master whose cleanup never ran reopens

`cleanup: pending` on a finished closeout is housekeeping left undone, not a lifecycle state: the enclosure root is still on disk and the successor generation a reopen publishes cannot be reserved until it is collected. `_collect_completed_uncleaned` therefore runs the same terminal collection `worktree_cleanup` runs — through `cleanup_result`, so the archive stays the one authority over the contract — and then reopens exactly as for a cleaned master (`_admitted_series_reopen`). It acts only on `kind: series` with `cleanup: pending` plus a completed closeout and a completed integration; a master that is still in flight keeps its refusal, and the collection rewrites the contract, so the plan is built from `load_contract`'s reload rather than the copy read before it ran. Sending the operator away to clean up by hand was the refusal this behaviour removed (ruling 7dc3b6d2, defect (b)). The removed-memory-mode refusal still comes first, and `dry_run` collects nothing.

## Evidence

- The file realizes its current contract at the corrected candidate. [1]

## Current source evidence


- Series reopen passes source-path/document pairs to the existing scope owner. [2]
