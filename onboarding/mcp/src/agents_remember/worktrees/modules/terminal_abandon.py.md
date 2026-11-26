# mcp/src/agents_remember/worktrees/modules/terminal_abandon.py

## Governing Overview

[modules overview](overview.md)

## Purpose

The admitted abandon transaction: validates task-stage binding, prepares task-folder move-out and seat archival through `prepare_terminal_group`, blocks (`abandon-blocked`) before destructive output when any folder, move-out, or seat blocker exists, and attaches `agentArchive` and `terminalArchive` to the result.

## Code Commentary

### Logic

`_abandon_with_guard` plans the abandoned task stage before terminal admission and repeats stage planning under refreshed terminal authority inside `publish`. It then calls `prepare_terminal_group(current, dry_run=args.dry_run, teardown_providers=True)` to preview folder removal, close/archive recorded leaf or modern series seats, and run move-out. If `prepared.blockers` is non-empty, `publish` returns `state: "abandon-blocked"` with `directories` and `blockers` before any destructive output; otherwise it runs `_abandon_terminal_outputs` and `_abandon_outputs_result`, wraps the terminal archive result, and merges any non-empty `agentArchive` report. Series contracts still publish under `publish_atomic_series_terminal_under_authority`.

### Invariants And Boundaries

- Group preview, seat archival, and move-out run after terminal admission and before provider, worktree, branch, and folder removal.
- A refused terminal admission returns before any archive or destructive output.
- Unresolved seats (`owed`, `leftAlone`), archive failures, or an unbound archive service with existing launch receipts block abandon (`state: "abandon-blocked"`) before deletion.

## Evidence



- Archival runs inside the admitted publish step before destructive outputs. Anchor: `_abandon_with_guard` [1]



## Current source evidence



- Task-stage binding is checked before terminal work and again before archival/destructive outputs under current authority. Anchor: abandon preflight order [2]
