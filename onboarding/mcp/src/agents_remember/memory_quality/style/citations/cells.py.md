# mcp/src/agents_remember/memory_quality/style/citations/cells.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/cells.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Parse the table citation form ``| Finding | Anchor | Source |``.

## Code Commentary

### Logic

Module-level surface:

- `CitationTable` (class, lines 24-36) — One table this check claims, whether or not it is in the current format.
- `parse_row` (function, lines 39-48)
- `scan_tables` (function, lines 51-53) — Parse every GFM table once for reuse by citation checks.
- `table_lines` (function, lines 56-64) — Every zero-based line index a table occupies -- what :mod:`prose` must not read.
- `citation_tables` (function, lines 67-101) — Every evidence table in one document, current format or not.

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
| Defines the class `CitationTable` (lines 24-36) — One table this check claims, whether or not it is in the current format.. | `CitationTable` | mcp/src/agents_remember/memory_quality/style/citations/cells.py:24-36 |
| Defines the function `parse_row` (lines 39-48). | `parse_row` | mcp/src/agents_remember/memory_quality/style/citations/cells.py:39-48 |
| Defines the function `scan_tables` (lines 51-53) — Parse every GFM table once for reuse by citation checks.. | `scan_tables` | mcp/src/agents_remember/memory_quality/style/citations/cells.py:51-53 |
| Defines the function `table_lines` (lines 56-64) — Every zero-based line index a table occupies -- what :mod:`prose` must not read.. | `table_lines` | mcp/src/agents_remember/memory_quality/style/citations/cells.py:56-64 |
| Defines the function `citation_tables` (lines 67-101) — Every evidence table in one document, current format or not.. | `citation_tables` | mcp/src/agents_remember/memory_quality/style/citations/cells.py:67-101 |

## Update History

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullet and Finding line numbers with the scoped fixer's generated decorator-inclusive range for `CitationTable`; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
