# mcp/tests/test_l6_diff_coverage_projection_types.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_projection_types.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T19:04+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for projection-types generator edge branches: primitive validation, schema allowed/type validation, and state-partition mapping.

## Code Commentary

- `TestPrimitiveValidation` covers object/string handling, reference names and nullability, and JSON literal/enum values.
- `TestSchemaAllowedAndType` covers allowed-keyword flags, unexpected-keyword refusals, vocabulary blocks, and stale generated files.
- Its named-literal case proves a local `$defs` enum reference resolves to the exact closed
  vocabulary and that a referenced non-enum remains a loud generation failure.
- `TestStatePartition` covers non-enum states and bucket-mapping mismatches.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestPrimitiveValidation` (lines 37-76). | `TestPrimitiveValidation` | mcp/tests/test_l6_diff_coverage_projection_types.py:37-76 |
| Defines the class `TestSchemaAllowedAndType` (lines 79-150). | `TestSchemaAllowedAndType` | mcp/tests/test_l6_diff_coverage_projection_types.py:79-150 |
| Defines the class `TestStatePartition` (lines 153-176). | `TestStatePartition` | mcp/tests/test_l6_diff_coverage_projection_types.py:195-218 |

## 260821-CLIVE-L2 Union Generator Coverage

Coverage now distinguishes non-null unions from nullable unions, proves preservation of outer
annotations, accepts multiple surviving non-null variants, renders the lifecycle-operation status
union exactly, and rejects the all-null case. These assertions close the generated projection
fallout without weakening the schema vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Primitive coverage exercises intact, optional multi-variant, annotated, and invalid all-null unions. | `test_ref_name_and_nullable` | mcp/tests/test_l6_diff_coverage_projection_types.py:54-88 |

## Update History

- 2026-08-29T19:04+02:00 — Added the Python 3.13 named-literal success/refusal forcing case exposed
  by closeout generation 11. Verification remains closeout-owned.

- 2026-08-28T06:40+02:00 — No content impact: moved projection-type verification helpers out
  of the product package and into `agents_remember_test_support`; the branch coverage is unchanged.
- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
