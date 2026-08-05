# mcp/src/agents_remember/memory_quality/style/citations/work_order.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/work_order.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Group declined citation repairs into one work order per document.

## Code Commentary

### Logic

Module-level surface:

- `Item` (class, lines 18-45) — One declined citation and the edit that clears it.
- `orders` (function, lines 48-67) — One entry per document, in tree order, each holding its own items in line order.
- `counted` (function, lines 70-75) — Every decline reason with its count, worst first -- the complete list (L6-R15).

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
| Defines the class `Item` (lines 18-45) — One declined citation and the edit that clears it.. | `Item` | mcp/src/agents_remember/memory_quality/style/citations/work_order.py:18-45 |
| Defines the function `orders` (lines 48-67) — One entry per document, in tree order, each holding its own items in line order.. | `orders` | mcp/src/agents_remember/memory_quality/style/citations/work_order.py:48-67 |
| Defines the function `counted` (lines 70-75) — Every decline reason with its count, worst first -- the complete list (L6-R15).. | `counted` | mcp/src/agents_remember/memory_quality/style/citations/work_order.py:70-75 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
