# mcp/tests/test_global_state_isolation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_global_state_isolation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

The suite identifies the test that leaks an explicitly-owned mutable global.
The expected owner is the kernel checkout-execution declaration, whose normal pytest baseline is
`{"mode": "test"}`; a leaked dashboard/MCP role is restored to that explicit mode before failure.

## Code Commentary

### Logic

Module-level surface:

- `GlobalStateLeakDetectionTests` (class, lines 14-38)

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
| Defines the class `GlobalStateLeakDetectionTests` (lines 14-38). | `GlobalStateLeakDetectionTests` | mcp/tests/test_global_state_isolation.py:14-38 |

## 260824-PDLS Route Impact

The production owner moved from `mcp/tests/_global_state.py` to
`agents_remember.testing.global_state`. This suite still expects root certifying bootstrap to have
declared the normal `test` mode, deliberately leaks dashboard mode, and proves restoration happens
before failure. It is therefore a Dagger-suite contract, not a valid standalone raw-host test.

## Update History

- 2026-08-24T20:55+02:00 — Updated imports and route expectations after shared state ownership
  moved into production testing.

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: updated leak diagnostics and ownership enumeration for
  the kernel-owned checkout execution mode and explicit pytest baseline. Verification metadata
  remains pinned until approved closeout.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
