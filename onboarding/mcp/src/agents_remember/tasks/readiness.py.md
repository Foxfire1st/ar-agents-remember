# mcp/src/agents_remember/tasks/readiness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/readiness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `CompletionBlocker` — one exact declared work unit that prevents terminal completion. | "class CompletionBlocker" | mcp/src/agents_remember/models/task_document.py:23-31 |
| Defines the function `completion_blockers` (lines 26-61) — Return every unresolved declared unit; an empty document is ready vacuously.. | `completion_blockers` | mcp/src/agents_remember/tasks/readiness.py:14-49 |
| Defines the function `missing_unresolved_master_rows` (lines 64-73) — Unresolved ``(number, file)`` rows lost from a candidate, including duplicates.. | `missing_unresolved_master_rows` | mcp/src/agents_remember/tasks/readiness.py:52-61 |
| Defines the function `completed_master_rows_to_validate` (lines 76-101) — Rows whose terminal claim is new, explicitly targeted, or in a terminal master.. | `completed_master_rows_to_validate` | mcp/src/agents_remember/tasks/readiness.py:64-89 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
