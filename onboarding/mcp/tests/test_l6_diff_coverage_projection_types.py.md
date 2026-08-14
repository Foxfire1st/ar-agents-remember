# mcp/tests/test_l6_diff_coverage_projection_types.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_projection_types.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for projection-types generator edge branches: primitive validation, schema allowed/type validation, and state-partition mapping.

## Code Commentary

- `TestPrimitiveValidation` covers object/string handling, reference names and nullability, and JSON literal/enum values.
- `TestSchemaAllowedAndType` covers allowed-keyword flags, unexpected-keyword refusals, vocabulary blocks, and stale generated files.
- `TestStatePartition` covers non-enum states and bucket-mapping mismatches.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestPrimitiveValidation` (lines 37-76). | `TestPrimitiveValidation` | mcp/tests/test_l6_diff_coverage_projection_types.py:37-76 |
| Defines the class `TestSchemaAllowedAndType` (lines 79-150). | `TestSchemaAllowedAndType` | mcp/tests/test_l6_diff_coverage_projection_types.py:79-150 |
| Defines the class `TestStatePartition` (lines 153-176). | `TestStatePartition` | mcp/tests/test_l6_diff_coverage_projection_types.py:153-176 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
