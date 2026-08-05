# mcp/tests/test_l6_diff_coverage_source_index.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_source_index.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for citation source-index edge branches: close/paths, open-and-validate, build-and-publish branches, tree bounds, and reclamation.

## Code Commentary

- `TestCloseAndPaths` covers idempotent close and cache-root-in-code refusals.
- `TestOpenAndValidate` covers snapshot integrity, stale root mismatch, and exhausted build attempts.
- `TestBuildAndPublishBranches` covers index-byte limits and temporary-database failure.
- `TestTreeAndBounds` covers memory-inside-code skipping, stable reads, and source bounds.
- `TestReclamation` covers legacy cache-root reclaim, remove-tree, and time-remaining checks.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestCloseAndPaths` (lines 53-66). | `TestCloseAndPaths` | mcp/tests/test_l6_diff_coverage_source_index.py:53-66 |
| Defines the class `TestOpenAndValidate` (lines 69-98). | `TestOpenAndValidate` | mcp/tests/test_l6_diff_coverage_source_index.py:69-98 |
| Defines the class `TestBuildAndPublishBranches` (lines 101-133). | `TestBuildAndPublishBranches` | mcp/tests/test_l6_diff_coverage_source_index.py:101-133 |
| Defines the class `TestTreeAndBounds` (lines 136-188). | `TestTreeAndBounds` | mcp/tests/test_l6_diff_coverage_source_index.py:136-188 |
| Defines the class `TestReclamation` (lines 191-233). | `TestReclamation` | mcp/tests/test_l6_diff_coverage_source_index.py:191-233 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
