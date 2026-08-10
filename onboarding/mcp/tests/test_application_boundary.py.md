# mcp/tests/test_application_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_application_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
