# mcp/tests/test_l6_diff_coverage_source_index_cache.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_source_index_cache.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for managed citation cache authority branches: authority resolution, shared-namespace opening, terminal guard behavior, and reclaim/acquisition transitions.

## Code Commentary

- `TestAuthorityResolution` covers missing roots, resolved-authority errors, and contract-cache authority without memory.
- `TestOpenSharedNamespace` covers create-false-when-absent and capacity-full branches.
- `TestTerminalGuard` covers publish/rollback without namespace, quarantine, tombstone moves, and restore branches.
- `TestReclaimAndAcquisition` covers managed-namespace reclaim, acquisition transitions, control-state reads, and base/remove-tree.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestAuthorityResolution` (lines 53-96). | `TestAuthorityResolution` | mcp/tests/test_l6_diff_coverage_source_index_cache.py:53-96 |
| Defines the class `TestOpenSharedNamespace` (lines 99-126). | `TestOpenSharedNamespace` | mcp/tests/test_l6_diff_coverage_source_index_cache.py:99-126 |
| Defines the class `TestTerminalGuard` (lines 129-189). | `TestTerminalGuard` | mcp/tests/test_l6_diff_coverage_source_index_cache.py:129-189 |
| Defines the class `TestReclaimAndAcquisition` (lines 192-247). | `TestReclaimAndAcquisition` | mcp/tests/test_l6_diff_coverage_source_index_cache.py:192-247 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
