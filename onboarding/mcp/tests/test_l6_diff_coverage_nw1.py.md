# mcp/tests/test_l6_diff_coverage_nw1.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_nw1.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout diff-coverage batch NW1: source_index_cache residual branches. Covers the exact lines and branches listed in `/tmp/l6-cov-NW1.json` for `mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py`; every test runs against tmp_path-only state and never touches the shared frozen citation index.

## Code Commentary

- `TestOpenSharedNamespace` covers non-directory and symlink namespace refusals.
- `TestTerminalGuard` covers preview/completion, tombstone-move, and restore branches.
- `TestTerminalNamespaceGuardContext` covers contract-path mismatch and tombstone restore in `finally`.
- `TestAcquisitionAndValidation` covers legacy transitions, stale contracts, and active-owner validation.
- `TestControlStateValidation` covers fixed-bound, authority, lifecycle, phase, and outcome validation.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestOpenSharedNamespace` (lines 79-94). | `TestOpenSharedNamespace` | mcp/tests/test_l6_diff_coverage_nw1.py:79-94 |
| Defines the class `TestTerminalGuard` (lines 97-142). | `TestTerminalGuard` | mcp/tests/test_l6_diff_coverage_nw1.py:97-142 |
| Defines the class `TestTerminalNamespaceGuardContext` (lines 145-190). | `TestTerminalNamespaceGuardContext` | mcp/tests/test_l6_diff_coverage_nw1.py:145-190 |
| Defines the class `TestAcquisitionAndValidation` (lines 193-284). | `TestAcquisitionAndValidation` | mcp/tests/test_l6_diff_coverage_nw1.py:193-284 |
| Defines the class `TestControlStateValidation` (lines 287-334). | `TestControlStateValidation` | mcp/tests/test_l6_diff_coverage_nw1.py:287-334 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
