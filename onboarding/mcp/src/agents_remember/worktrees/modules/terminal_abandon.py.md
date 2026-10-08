# mcp/src/agents_remember/worktrees/modules/terminal_abandon.py

## Governing Overview

[modules overview](overview.md)

## Purpose

The admitted abandon transaction, with host archival of the leaf's agents before any destructive
output. It preserves the existing abandon admission, terminal archive authority, series publication
and result shape while adding the archive report.

## Code Commentary

### Logic

`_abandon_with_guard` is the extracted body of the admitted abandon transaction. After terminal
admission succeeds and the terminal authority is re-read, its `publish` step archives the current
contract's leaf agents through `archive_terminal_agents` before calling the abandon outputs, wraps
the terminal archive result, and merges the non-empty `agentArchive` report into the payload. A
series contract still publishes under `publish_atomic_series_terminal_under_authority`; failures
still return the `abandon-blocked` result with the preserved cache and the helper reason.

### Invariants And Boundaries

- Archival happens after terminal admission and before worktree, branch and directory removal.
- A refused terminal admission returns before any archive or destructive output.
- The archive report never changes the abandon state or its blockers.

## Evidence

- Archival runs inside the admitted publish step before destructive outputs. [1]
