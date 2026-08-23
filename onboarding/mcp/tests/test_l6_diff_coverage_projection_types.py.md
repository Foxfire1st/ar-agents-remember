# mcp/tests/test_l6_diff_coverage_projection_types.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_projection_types.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
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

## 260821-CLIVE-L2 Union Generator Coverage

Coverage now distinguishes non-null unions from nullable unions, proves preservation of outer
annotations, accepts multiple surviving non-null variants, renders the lifecycle-operation status
union exactly, and rejects the all-null case. These assertions close the generated projection
fallout without weakening the schema vocabulary.

| Finding | Source |
| --- | --- |
| Primitive coverage exercises intact, optional multi-variant, annotated, and invalid all-null unions. | mcp/tests/test_l6_diff_coverage_projection_types.py:54-90 |

## Update History

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
