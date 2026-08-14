# mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Resolve every exact anchor location through one immutable source snapshot index.

## Code Commentary

### Logic

Module-level surface:

- `Location` (class, lines 32-40) — One range in one file that satisfies an anchor.
- `Sightings` (class, lines 44-78) — Where one anchor exists in the code tree, and how much of it fitted.
- `_Batch` (class, lines 82-106) — One anchor's accumulating result while the walk is in progress.
- `locate` (function, lines 109-122) — Every location from the shared snapshot index, preserving direct-resolver order.
- `_located` (function, lines 125-133)
- `locate_uncached` (function, lines 136-144) — Direct source resolver retained as the semantic parity oracle for the index.
- `walk` (function, lines 147-154) — Every readable code file, with the path text a ``Source`` would spell it as.
- `_visit` (function, lines 157-167) — Record every anchor this one file holds, reading and deriving it at most once.
- `described` (function, lines 170-182) — The tree-wide half of a finding: every location, or the fact that there are none.

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
| Defines the class `Location` (lines 32-40) — One range in one file that satisfies an anchor.. | `Location` | mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py:32-40 |
| Defines the class `Sightings` (lines 44-78) — Where one anchor exists in the code tree, and how much of it fitted.. | `Sightings` | mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py:44-78 |
| Defines the class `_Batch` (lines 82-106) — One anchor's accumulating result while the walk is in progress.. | `_Batch` | mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py:82-106 |
| Defines the function `locate` (lines 109-122) — Every location from the shared snapshot index, preserving direct-resolver order.. | `locate` | mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py:109-122 |
| Defines the function `_located` (lines 125-133). | `_located` | mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py:125-133 |
| Defines the function `locate_uncached` (lines 136-144) — Direct source resolver retained as the semantic parity oracle for the index.. | `locate_uncached` | mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py:136-144 |
| Defines the function `walk` (lines 147-154) — Every readable code file, with the path text a ``Source`` would spell it as.. | `walk` | mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py:147-154 |
| Defines the function `_visit` (lines 157-167) — Record every anchor this one file holds, reading and deriving it at most once.. | `_visit` | mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py:157-167 |
| Defines the function `described` (lines 170-182) — The tree-wide half of a finding: every location, or the fact that there are none.. | `described` | mcp/src/agents_remember/memory_quality/style/citations/symbol_index.py:170-182 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
