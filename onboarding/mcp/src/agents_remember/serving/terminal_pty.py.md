# mcp/src/agents_remember/serving/terminal_pty.py

## Governing Overview

[overview](overview.md)

## Purpose

One pseudo-terminal and the live client attached to it.

## Code Commentary

### Logic

Module-level surface:

- `PtyProcess` (class, lines 59-75) — A spawned child attached to a PTY master fd, with lifecycle controls.
- `TerminalSession` (class, lines 83-166) — One live terminal client: a tmux-wrapped PTY child plus its lifecycle/worktree correlation.
- `spawn_pty` (function, lines 169-216) — Spawn ``argv`` in ``cwd`` on a fresh PTY; the master fd is left non-blocking.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `PtyProcess` (lines 59-75) — A spawned child attached to a PTY master fd, with lifecycle controls.. [1]
- Defines the class `TerminalSession` (lines 83-166) — One live terminal client: a tmux-wrapped PTY child plus its lifecycle/worktree correlation.. [2]
- Defines the function `spawn_pty` (lines 169-216) — Spawn ``argv`` in ``cwd`` on a fresh PTY; the master fd is left non-blocking.. [3]
