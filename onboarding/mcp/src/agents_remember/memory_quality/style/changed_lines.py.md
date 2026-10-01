# mcp/src/agents_remember/memory_quality/style/changed_lines.py

## Governing Overview

[overview](../overview.md)

## Purpose

Identify memory lines changed against ``HEAD`` for closeout-scoped style rules.

## Code Commentary

### Logic

Module-level surface:

- `ChangedLines` (class, lines 20-29) — Lines added or modified against HEAD, per absolute path.
- `changed_lines` (function, lines 32-50) — The lines under ``root`` that differ from HEAD, staged or not, plus untracked files.
- `anchored` (function, lines 53-55) — Make ``root`` absolute without collapsing worktree symlinks.
- `repository_root` (function, lines 58-72) — The work tree ``root`` sits in, or ``None`` when it has no history to diff against.
- `collect_diff_lines` (function, lines 75-103) — Collect added lines from staged and unstaged diffs, with rename detection.
- `diff_target` (function, lines 106-111) — The new-side path of a ``+++`` header, or ``None`` for a deletion.
- `collect_untracked_lines` (function, lines 114-135) — A file git has never seen is new in full, so every line of it is in scope.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `ChangedLines` (lines 20-29) — Lines added or modified against HEAD, per absolute path.. [1]
- Defines the function `changed_lines` (lines 32-50) — The lines under ``root`` that differ from HEAD, staged or not, plus untracked files.. [2]
- Defines the function `anchored` (lines 53-55) — Make ``root`` absolute without collapsing worktree symlinks.. [3]
- Defines the function `repository_root` (lines 58-72) — The work tree ``root`` sits in, or ``None`` when it has no history to diff against.. [4]
- Defines the function `collect_diff_lines` (lines 75-103) — Collect added lines from staged and unstaged diffs, with rename detection.. [5]
- Defines the function `diff_target` (lines 106-111) — The new-side path of a ``+++`` header, or ``None`` for a deletion.. [6]
- Defines the function `collect_untracked_lines` (lines 114-135) — A file git has never seen is new in full, so every line of it is in scope.. [7]
