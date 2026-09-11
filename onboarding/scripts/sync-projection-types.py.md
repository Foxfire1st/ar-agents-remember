# scripts/sync-projection-types.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `scripts/sync-projection-types.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[overview](../overview.md)

## Purpose

Generate or check the dashboard projection schema and TypeScript contract.

## Code Commentary

### Logic

Module-level surface:

- `parse_args` (function, lines 20-40)
- `check` (function, lines 43-51)
- `main` (function, lines 54-65)

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
| Defines the function `parse_args` (lines 20-40). | `parse_args` | scripts/sync-projection-types.py:20-40 |
| Defines the function `check` (lines 43-51). | `check` | scripts/sync-projection-types.py:43-51 |
| Defines the function `main` (lines 54-65). | `main` | scripts/sync-projection-types.py:54-65 |

## PDLS Wave 005 Current Delta

The script now adds both `mcp/src` and `mcp/test_support` to its explicit import path, then imports
the projection generator from its verification owner. This preserves the repository script entry
point without shipping test-evidence machinery as product runtime code.

## Update History

- 2026-08-28T06:40+02:00 — Routed projection synchronization through the dedicated verification
  package with both source roots declared explicitly.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
