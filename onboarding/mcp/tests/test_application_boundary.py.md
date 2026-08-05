# mcp/tests/test_application_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_application_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

The MCP adapter cannot bypass the application layer (L6-R7).

## Code Commentary

### Logic

Module-level surface:

- `ApplicationBoundaryRuleTests` (class, lines 23-201)
- `RepositoryApplicationBoundaryTests` (class, lines 204-247)

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
| Defines the class `ApplicationBoundaryRuleTests` (lines 23-201). | `ApplicationBoundaryRuleTests` | mcp/tests/test_application_boundary.py:23-201 |
| Defines the class `RepositoryApplicationBoundaryTests` (lines 204-247). | `RepositoryApplicationBoundaryTests` | mcp/tests/test_application_boundary.py:204-247 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
