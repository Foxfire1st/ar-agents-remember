# mcp/tests/test_l6_diff_coverage_source_index_database.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_source_index_database.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for citation source-index database branches: metadata validation, database error branches, and pack/unpack posting helpers.

## Code Commentary

- `TestMetadataValidation` covers metadata integer and generation errors.
- `TestDatabaseBranches` covers insert-no-id, missing-metadata, missing-file, and flush-threshold branches.
- `TestPackUnpack` covers posting packing, extent unpacking, digest values, marks, and short-postings validation.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestMetadataValidation` (lines 66-86). | `TestMetadataValidation` | mcp/tests/test_l6_diff_coverage_source_index_database.py:66-86 |
| Defines the class `TestDatabaseBranches` (lines 89-128). | `TestDatabaseBranches` | mcp/tests/test_l6_diff_coverage_source_index_database.py:89-128 |
| Defines the class `TestPackUnpack` (lines 131-167). | `TestPackUnpack` | mcp/tests/test_l6_diff_coverage_source_index_database.py:131-167 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
