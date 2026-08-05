# mcp/src/agents_remember/memory_quality/style/changed_lines.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/changed_lines.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../overview.md` |

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `ChangedLines` (lines 20-29) — Lines added or modified against HEAD, per absolute path.. | `ChangedLines` | mcp/src/agents_remember/memory_quality/style/changed_lines.py:20-29 |
| Defines the function `changed_lines` (lines 32-50) — The lines under ``root`` that differ from HEAD, staged or not, plus untracked files.. | `changed_lines` | mcp/src/agents_remember/memory_quality/style/changed_lines.py:32-50 |
| Defines the function `anchored` (lines 53-55) — Make ``root`` absolute without collapsing worktree symlinks.. | `anchored` | mcp/src/agents_remember/memory_quality/style/changed_lines.py:53-55 |
| Defines the function `repository_root` (lines 58-72) — The work tree ``root`` sits in, or ``None`` when it has no history to diff against.. | `repository_root` | mcp/src/agents_remember/memory_quality/style/changed_lines.py:58-72 |
| Defines the function `collect_diff_lines` (lines 75-103) — Collect added lines from staged and unstaged diffs, with rename detection.. | `collect_diff_lines` | mcp/src/agents_remember/memory_quality/style/changed_lines.py:75-103 |
| Defines the function `diff_target` (lines 106-111) — The new-side path of a ``+++`` header, or ``None`` for a deletion.. | `diff_target` | mcp/src/agents_remember/memory_quality/style/changed_lines.py:106-111 |
| Defines the function `collect_untracked_lines` (lines 114-135) — A file git has never seen is new in full, so every line of it is in scope.. | `collect_untracked_lines` | mcp/src/agents_remember/memory_quality/style/changed_lines.py:114-135 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
