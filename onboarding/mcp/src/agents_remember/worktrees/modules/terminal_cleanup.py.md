# mcp/src/agents_remember/worktrees/modules/terminal_cleanup.py

## Governing Overview

[modules overview](overview.md)

## Purpose

The admitted cleanup transaction: publishes empty `TerminalWorktreeCleanupArguments()`, prepares task-folder move-out and seat archival through `prepare_terminal_group`, blocks before destructive output when any folder, move-out, or seat blocker exists, and attaches `agentArchive` and `terminalArchive` to the result.

## Code Commentary

### Logic

`_cleanup_with_guard` obtains terminal archive authority via `terminal_archive_required_result` with empty `TerminalWorktreeCleanupArguments()` and no provider-skip pre-check. After terminal admission succeeds and authority is re-read, `publish` calls `prepare_terminal_group(current, dry_run=args.dry_run)` to preview group removal, close/archive recorded leaf or modern series seats, and run move-out before `_cleanup_terminal_outputs`. If `prepared.blockers` is non-empty, `publish` returns `_group_blocked_result` (`state: "blocked"`) without deleting anything; otherwise it runs `_cleanup_terminal_outputs` and `_cleanup_outputs_result`, wraps the terminal archive result, and merges any non-empty `agentArchive` report. A series contract still publishes under `publish_atomic_series_terminal_under_authority`.

### Invariants And Boundaries

- Group preview, seat archival, and move-out run after terminal admission and before worktree, branch, and folder removal.
- A refused terminal admission returns before any archive or destructive output.
- Unresolved seats (`owed`, `leftAlone`), archive failures, or an unbound archive service with existing launch receipts block cleanup (`state: "blocked"`) before deletion.

## Evidence

- Archival runs inside the admitted publish step before destructive outputs. [1]
