# mcp/src/agents_remember/memory_quality/style/citations/editing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/editing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Byte-preserving edits shared by citation migration and steady-state repair.

## Code Commentary

### Logic

Module-level surface:

- `Site` (class, lines 9-15) — The exact span of one claim's source list, in one line of one document.
- `Documents` (class, lines 18-27) — The memory documents one run reads, split so that rejoining is lossless.
- `spliced` (function, lines 30-34) — ``line`` with the source list replaced and the cell's own padding untouched.
- `rewritten` (function, lines 37-42) — ``lines`` with each site's source list replaced, right to left so offsets hold.

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
| Defines the class `Site` (lines 9-15) — The exact span of one claim's source list, in one line of one document.. | `Site` | mcp/src/agents_remember/memory_quality/style/citations/editing.py:9-15 |
| Defines the class `Documents` (lines 18-27) — The memory documents one run reads, split so that rejoining is lossless.. | `Documents` | mcp/src/agents_remember/memory_quality/style/citations/editing.py:18-27 |
| Defines the function `spliced` (lines 30-34) — ``line`` with the source list replaced and the cell's own padding untouched.. | `spliced` | mcp/src/agents_remember/memory_quality/style/citations/editing.py:30-34 |
| Defines the function `rewritten` (lines 37-42) — ``lines`` with each site's source list replaced, right to left so offsets hold.. | `rewritten` | mcp/src/agents_remember/memory_quality/style/citations/editing.py:37-42 |

## Update History

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
