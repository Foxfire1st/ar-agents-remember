# mcp/tests/test_unclaimed_entity_sources.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_unclaimed_entity_sources.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Ranked, report-only coverage of sources absent from the entity register.

## Code Commentary

### Logic

Module-level surface:

- `_catalog` (function, lines 26-46)
- `UnclaimedEntitySourceTests` (class, lines 49-218)

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
| Defines the function `_catalog` (lines 26-46). | `_catalog` | mcp/tests/test_unclaimed_entity_sources.py:26-46 |
| Defines the class `UnclaimedEntitySourceTests` (lines 49-218). | `UnclaimedEntitySourceTests` | mcp/tests/test_unclaimed_entity_sources.py:49-218 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
