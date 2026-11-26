# mcp/src/agents_remember/worktrees/modules/commit_check_process.py

## Governing Overview

[Worktree lifecycle implementation modules](overview.md)

## Purpose

Shared bounded process, output-log and timeout ownership for the repository's commit checks. A closeout landing and a continued code-side sync commit run the same repository-owned pre-commit hook under `orchestration.landing.commitCheckTimeoutSeconds`, in a session of their own, with one retained log and a typed stop when the bound is reached.

## Code Commentary

`resolve_commit_check_timeout_seconds` reads the user settings file, the checkout's `system/settings.json` and, in a linked worktree, the primary checkout's settings; it requires a positive whole number and otherwise returns the 900-second default. Unknown `orchestration.landing` keys fail closed. `run_bounded_command` allocates or accepts a log in the repository's common Git directory, keeps the newest twenty logs, spawns the command alone in a new session with combined stdout/stderr and `stdin=DEVNULL`, and copies output in bounded chunks until the command exits or the bound passes.

Past the bound, `run_process_to_log` asks the process group to stop with `SIGTERM`, gives it 30 seconds, then stops it with `SIGKILL`. If an escaped descendant still holds the output pipe after the drain grace, `stop_escaped_pipe_holders` asks it to close, then kills and verifies it through at most three rounds; it returns the stopped PIDs and any survivor instead of claiming a live holder stopped. The log keeps a footer with the elapsed time and the outcome. `format_timeout_outcome` and `format_sync_commit_check_summary` name the limit, the retained log, the judged staged paths, any tracked file the hook changed, and the surviving escaped PIDs, and they offer `continue` or `cancel` as the following calls.

## Relationships

The landing path reaches this module through `landing_commit_check.py`; the continued sync path reaches it through `sync_transaction_git/_code_merge_commit.py`, which supplies the Git argv from `kernel/git_command.py`. `sync_transaction._commit_check_stopped` turns the typed `SyncCommitCheckStop` into the public `sync-commit-check-failed` answer. The module owns no Git commit, no task acceptance and no closeout state.

## Evidence

- The timeout resolves from the layered settings files and defaults to 900 seconds. [1]
- One bounded run owns the session-isolated spawn, the common-directory log, the timeout and the elapsed footer. [2]
- The process group is stopped after the bound and output is drained within a fixed grace. [3]
- Escaped pipe holders are stopped or named alive, never assumed stopped. [4]
- The public refusal names the limit, log, judged paths, changed files and recovery calls. [5]
