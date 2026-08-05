# mcp/src/agents_remember/memory_quality/style/document_shape/diff_markers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/document_shape/diff_markers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Report diff prefixes left at column zero in memory Markdown.

## Code Commentary

### Logic

Module-level surface:

- `check_onboarding_root` (function, lines 30-38)
- `check_file` (function, lines 41-48)
- `line_finding` (function, lines 51-80)
- `marker_finding` (function, lines 83-98)

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
| Defines the function `check_onboarding_root` (lines 30-38). | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/document_shape/diff_markers.py:30-38 |
| Defines the function `check_file` (lines 41-48). | `check_file` | mcp/src/agents_remember/memory_quality/style/document_shape/diff_markers.py:41-48 |
| Defines the function `line_finding` (lines 51-80). | `line_finding` | mcp/src/agents_remember/memory_quality/style/document_shape/diff_markers.py:51-80 |
| Defines the function `marker_finding` (lines 83-98). | `marker_finding` | mcp/src/agents_remember/memory_quality/style/document_shape/diff_markers.py:83-98 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
