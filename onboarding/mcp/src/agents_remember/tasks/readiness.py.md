# mcp/src/agents_remember/tasks/readiness.py

## Governing Overview

[overview](overview.md)

## Purpose

One terminal-readiness contract for task documents and their public writers.

## Code Commentary

### Logic

Module-level surface:

- `CompletionBlocker` (class, lines 15-23) — One exact declared work unit that prevents terminal completion.
- `completion_blockers` (function, lines 26-61) — Return every unresolved declared unit; an empty document is ready vacuously.
- `missing_unresolved_master_rows` (function, lines 64-73) — Unresolved ``(number, file)`` rows lost from a candidate, including duplicates.
- `completed_master_rows_to_validate` (function, lines 76-101) — Rows whose terminal claim is new, explicitly targeted, or in a terminal master.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `CompletionBlocker` — one exact declared work unit that prevents terminal completion. [1]
- Defines the function `completion_blockers` — Return every unresolved declared unit; an empty document is ready vacuously. A master row counts as resolved when it is `Completed` **or** `abandoned`, so `RESOLVED_MASTER_ROW_STATUSES` is the only membership test here. [2]
- Defines the function `missing_unresolved_master_rows` — Unresolved ``(number, file)`` rows lost from a candidate, including duplicates. [3]
- Defines the function `master_is_terminal` — the one terminal-readiness predicate: `abandoned`, or `Completed` with no blockers. It replaces the removed `completed_master_rows_to_validate` row scan, which re-derived terminality from individual rows and stayed complete only while `DocStatus` was closed. [4]
