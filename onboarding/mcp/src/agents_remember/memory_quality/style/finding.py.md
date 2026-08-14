# mcp/src/agents_remember/memory_quality/style/finding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/finding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview](../overview.md)

## Purpose

Shared finding record for memory-layer style checks.

## Code Commentary

### Logic

Module-level surface:

- `QualityFinding` (class, lines 14-43)
- `check_result` (function, lines 46-68) — Package findings into the uniform runner result ``memory_quality.check`` expects.

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
| Defines the class `QualityFinding` (lines 14-43). | `QualityFinding` | mcp/src/agents_remember/memory_quality/style/finding.py:14-43 |
| Defines the function `check_result` (lines 46-68) — Package findings into the uniform runner result ``memory_quality.check`` expects.. | `check_result` | mcp/src/agents_remember/memory_quality/style/finding.py:46-68 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
