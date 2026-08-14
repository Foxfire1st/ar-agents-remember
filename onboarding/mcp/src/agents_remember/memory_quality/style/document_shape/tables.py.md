# mcp/src/agents_remember/memory_quality/style/document_shape/tables.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/document_shape/tables.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Report Markdown table rows whose cell count differs from the header.

## Code Commentary

### Logic

Module-level surface:

- `Row` (class, lines 36-41) — One line of a candidate table: where it was, and how many cells it holds.
- `check_onboarding_root` (function, lines 44-52)
- `check_file` (function, lines 55-60)
- `rows_of` (function, lines 63-66)
- `tables` (function, lines 69-86) — Every GFM table in the file, as its header row and its body rows.
- `starts_table` (function, lines 89-96)
- `read_body` (function, lines 99-112)
- `ragged_findings` (function, lines 119-141)
- `ragged_message` (function, lines 144-168) — Return the complete repair for a short or long table row.

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
| Defines the class `Row` (lines 36-41) — One line of a candidate table: where it was, and how many cells it holds.. | `Row` | mcp/src/agents_remember/memory_quality/style/document_shape/tables.py:36-41 |
| Defines the function `check_onboarding_root` (lines 44-52). | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/document_shape/tables.py:44-52 |
| Defines the function `check_file` (lines 55-60). | `check_file` | mcp/src/agents_remember/memory_quality/style/document_shape/tables.py:55-60 |
| Defines the function `rows_of` (lines 63-66). | `rows_of` | mcp/src/agents_remember/memory_quality/style/document_shape/tables.py:63-66 |
| Defines the function `tables` (lines 69-86) — Every GFM table in the file, as its header row and its body rows.. | `tables` | mcp/src/agents_remember/memory_quality/style/document_shape/tables.py:69-86 |
| Defines the function `starts_table` (lines 89-96). | `starts_table` | mcp/src/agents_remember/memory_quality/style/document_shape/tables.py:89-96 |
| Defines the function `read_body` (lines 99-112). | `read_body` | mcp/src/agents_remember/memory_quality/style/document_shape/tables.py:99-112 |
| Defines the function `ragged_findings` (lines 119-141). | `ragged_findings` | mcp/src/agents_remember/memory_quality/style/document_shape/tables.py:119-141 |
| Defines the function `ragged_message` (lines 144-168) — Return the complete repair for a short or long table row.. | `ragged_message` | mcp/src/agents_remember/memory_quality/style/document_shape/tables.py:144-168 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
