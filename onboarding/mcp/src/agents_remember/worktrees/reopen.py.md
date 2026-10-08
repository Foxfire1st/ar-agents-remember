# mcp/src/agents_remember/worktrees/reopen.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Plans and publishes a task reopen transition under the existing repository, contract and recovery admission.

## Code Commentary

`_plan_leaf_doc_reset` resolves the canonical leaf document, resets status/lifecycle fields and appends its reopen decision without publishing. `_plan_master_index_reset` updates its exact master row. `_publish_reopen_transition` owns the paired publication and recovery artifacts; `_restore_reopen_artifacts` restores those on failure. The old series-document and review-state helper names are retired, not permissions to reset an active review. A reader of this card may not edit task state or invoke reopen outside its admitted workflow.

## Evidence

### Repo-Internal References

- `_plan_leaf_doc_reset` owns the current boundary described above. [18]
- `_plan_master_index_reset` owns the current boundary described above. [19]
- `_publish_reopen_transition` owns the current boundary described above. [20]
- `_restore_reopen_artifacts` owns the current boundary described above. [21]
