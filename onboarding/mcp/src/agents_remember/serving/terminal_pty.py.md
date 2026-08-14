# mcp/src/agents_remember/serving/terminal_pty.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/terminal_pty.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `PtyProcess` (lines 59-75) — A spawned child attached to a PTY master fd, with lifecycle controls.. | `PtyProcess` | mcp/src/agents_remember/serving/terminal_pty.py:59-75 |
| Defines the class `TerminalSession` (lines 83-166) — One live terminal client: a tmux-wrapped PTY child plus its lifecycle/worktree correlation.. | `TerminalSession` | mcp/src/agents_remember/serving/terminal_pty.py:83-166 |
| Defines the function `spawn_pty` (lines 169-216) — Spawn ``argv`` in ``cwd`` on a fresh PTY; the master fd is left non-blocking.. | `spawn_pty` | mcp/src/agents_remember/serving/terminal_pty.py:169-216 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
