# mcp/src/agents_remember/kernel/atomic_write.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/atomic_write.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Publish file content atomically through the package's single owner.

## Code Commentary

### Logic

Module-level surface:

- `_temp_path_for` (function, lines 21-29) — The private temp this module writes before it replaces ``path``.
- `_fsync_directory` (function, lines 32-48) — Flush ``directory``'s own entries so a completed rename survives a host loss.
- `atomic_write_bytes` (function, lines 51-70) — Publish ``payload`` at ``path``: readers see the old file or the new one, never both.
- `atomic_write_text` (function, lines 73-75) — :func:`atomic_write_bytes` for text. The encoding is explicit, never the locale's.
- `atomic_replace` (function, lines 78-92) — Move an already-written ``source`` onto ``destination`` atomically and durably.

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
| Defines the function `_temp_path_for` (lines 21-29) — The private temp this module writes before it replaces ``path``.. | `_temp_path_for` | mcp/src/agents_remember/kernel/atomic_write.py:21-29 |
| Defines the function `_fsync_directory` (lines 32-48) — Flush ``directory``'s own entries so a completed rename survives a host loss.. | `_fsync_directory` | mcp/src/agents_remember/kernel/atomic_write.py:32-48 |
| Defines the function `atomic_write_bytes` (lines 51-70) — Publish ``payload`` at ``path``: readers see the old file or the new one, never both.. | `atomic_write_bytes` | mcp/src/agents_remember/kernel/atomic_write.py:51-70 |
| Defines the function `atomic_write_text` (lines 73-75) — :func:`atomic_write_bytes` for text. The encoding is explicit, never the locale's.. | `atomic_write_text` | mcp/src/agents_remember/kernel/atomic_write.py:73-75 |
| Defines the function `atomic_replace` (lines 78-92) — Move an already-written ``source`` onto ``destination`` atomically and durably.. | `atomic_replace` | mcp/src/agents_remember/kernel/atomic_write.py:78-92 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
