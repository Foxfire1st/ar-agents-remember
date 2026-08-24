# mcp/tests/test_random_order.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_random_order.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

The scheduled random-order path is deterministic and therefore reproducible.

## Code Commentary

### Logic

Module-level surface:

- `RandomOrderTests` (class, lines 10-26)

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
| Defines the class `RandomOrderTests` (lines 10-26). | `RandomOrderTests` | mcp/tests/test_random_order.py:10-26 |

## 260824-PDLS Route Impact

The deterministic shuffle owner moved from `mcp/tests/_random_order.py` to
`agents_remember.testing.random_order` so shared pytest bootstrap can use it without importing the
test tree. Existing seed/order behavior remains unchanged.

## Update History

- 2026-08-24T21:23+02:00 — Updated the production-owner reference after the shared-route move.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
