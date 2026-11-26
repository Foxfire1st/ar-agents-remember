# mcp/tests/test_sync_commit_check.py

## Governing Overview

[MCP tests](overview.md)

## Purpose

Behavioral protection for continued code-side sync commits and staged memory-side sync merges that run a repository's commit check. The cases drive hanging, mutating, passing, absent, and disabled hooks against real retained syncs and assert the typed stop, retained log, pinned `HEAD`/`MERGE_HEAD`/index rollback, conditional `Commit-Check-Pass` stamping, integration reuse without a second hook run, and tree-mismatch re-checking.

## Code Commentary

The cases build a small repository with a retained code-side merge (and, for stamping cases, a paired memory merge) and a hook whose behavior they control. `test_rule4_silent_hanging_hook_times_out_kills_group_and_resumes_cleanly` proves that a silent hook and its child are stopped at a short bound and that a later continue commits once. The mutation cases distinguish an exit-0 mutation, a nonzero mutation and a timeout mutation; each restores the pinned index tree and refuses a blind continue while worktree bytes remain. The provenance cases cover a published commit that landed before an escaped holder timed out, a timeout with no `MERGE_HEAD` and no proven head, an empty staged diff, a stale `index.lock`, and the named surviving escaped PIDs. The refusal text is asserted for the limit, the retained log path and every changed tracked path. The stamping cases assert that continued code sync and hooked memory sync commits carry `Commit-Check-Pass` matching the published tree and hook so `_require_landing_commit_check` skips a second hook run (`test_r8_synced_leaf_integrates_without_second_hook_run`), that a commit carrying a `Commit-Check-Pass` trailer for a different tree is still checked and refused on hook failure (`test_r8_stamped_tree_mismatch_is_still_checked_at_integration`), and that absent or disabled (`0o644`) hooks write no `Commit-Check-Pass` trailer on either code or memory sync commits (`test_r8_sync_commit_without_runnable_hook_carries_no_stamp`).

## Relationships

The cases use the real sync transaction, the shared runner in `worktrees/modules/commit_check_process.py`, `commit_check_fact`/`commit_check_trailer` from `worktrees/modules/landing_commit_check.py`, and `_require_landing_commit_check` from `worktrees/integration/integration_ref_transaction.py`; only the four synthetic timeout-race/escaped-PID cases monkeypatch `run_bounded_command`. The hook script they write stands for the repository's pre-commit hook. The lane and lifecycle catalogs own their selection; this card claims no execution.

## Evidence

- A silent hanging hook is stopped with its group at the bound, and the sync continues and commits once. [1]
- A staged tracked-file mutation on timeout is rolled back to the pinned index. [2]
- Surviving escaped output holders are named by PID in the refusal. [3]
- A changed tracked file outside the staged set is named in the refusal summary. [4]

- Stamped continued code sync and hooked memory sync commits pass integration's commit-check gate without running either pre-commit hook a second time. [5]
- A commit carrying a `Commit-Check-Pass` trailer for a different tree is still checked at integration and refused when the hook fails. [6]
- Sync commits carry no `Commit-Check-Pass` trailer when the repository's pre-commit hook is absent or disabled (`0o644`). [7]
