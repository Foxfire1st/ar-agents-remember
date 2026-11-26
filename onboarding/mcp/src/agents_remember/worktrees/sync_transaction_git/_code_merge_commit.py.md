# mcp/src/agents_remember/worktrees/sync_transaction_git/_code_merge_commit.py

## Governing Overview

[Managed-sync Git implementation](overview.md)

## Purpose

Bounded execution and conditional stamping of a continued code-side sync commit. The module captures the pinned staged state, builds commit arguments that stamp `Commit-Check-Pass` via `git commit -m` only when a runnable pre-commit hook will run (falling back to unstamped `git commit --no-edit` when none is runnable), executes the commit through the shared commit-check runner, proves the published commit when it landed, and restores the pinned index and merge sequencer when a hook changes tracked files on either a publishing or non-publishing path.

## Code Commentary

`snapshot_merge_sequencer` and `_capture_code_merge_context` record the staged paths and their task provenance, the expected index tree, the absolute Git directory and the `MERGE_HEAD`, `MERGE_MSG` and `MERGE_MODE` bytes before the commit starts. `sync_merge_commit_args` resolves the pre-commit hook via `resolve_commit_check_hook`: when a runnable hook exists, it strips Git `#` comment lines from `MERGE_MSG` with `_clean_merge_message`, appends `Commit-Check-Pass: tree=<expected_tree> hook=<hook_id>` via `append_commit_check_trailer`, and returns `git commit -m <stamped>`; when no runnable hook exists or the hook is disabled, it returns `git commit --no-edit` with no stamp. `commit_bounded_code_merge` resolves the commit-check bound, wraps those arguments in `git_command_spec`, and runs the commit under `run_bounded_command`; it never passes `--no-verify`.

A nonzero exit or a timeout first checks that the active merge is still the pinned sync merge. If it is, `_restore_nonpublishing_code_merge` compares the current tree and worktree against the captured state and restores `HEAD`, the pinned index tree and the sequencer files when a hook changed them, then raises `BoundedSyncCommitError` with the changed paths. A timeout clears a stale `index.lock`, proves a published commit when `MERGE_HEAD` is gone and the new head has the pinned parents, and otherwise raises the typed stop. A commit that Git created is accepted only when `_verify_published_code_merge` finds no tracked-file mutation and the pinned parents hold, guaranteeing that `HEAD^{tree}` equals `expected_tree` and matches any `Commit-Check-Pass` stamp.

## Relationships

`continue_side_merge` in `_merge.py` delegates the code-side commit here, and `_merge.py::_commit_staged_merge` reuses `sync_merge_commit_args` and `snapshot_merge_sequencer` for staged memory merges. The shared runner and log live in `worktrees/modules/commit_check_process.py`; hook resolution, hook identity and trailer formatting come from `worktrees/modules/landing_commit_check.py`; the Git argv and environment come from `kernel/git_command.py`. `sync_transaction.py` turns the typed error into `sync-commit-check-failed`. The module edits no task, memory or closeout state.

## Evidence

- A hook mutation is restored to the pinned index and merge sequencer before the refusal. [2]
- A timeout clears a stale lock, proves a landed commit, or raises the typed stop. [3]
- A published merge is accepted only when the pinned parents hold and tracked files were not mutated. [4]

- The continued code-side commit runs under the shared bound with conditional `Commit-Check-Pass` stamping and never `--no-verify`. [1]
- `sync_merge_commit_args` stamps `Commit-Check-Pass` onto the comment-stripped `MERGE_MSG` only when a runnable pre-commit hook will run, and otherwise writes no stamp and runs `git commit --no-edit`. [5]
