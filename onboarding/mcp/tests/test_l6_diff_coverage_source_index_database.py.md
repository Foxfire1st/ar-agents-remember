# mcp/tests/test_l6_diff_coverage_source_index_database.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_source_index_database.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:21:02+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for citation source-index database branches: metadata validation, database error branches, and pack/unpack posting helpers.

## Code Commentary

### Logic

- `TestMetadataValidation` validates generation metadata against `ReadyGeneration`. Its default filesystem fixture explicitly supplies an empty `candidate_tree` field. Missing that field is malformed metadata; a different candidate tree refuses even when the remaining generation identity agrees. Schema, readiness state, roots, integer bounds and application-digest errors retain separate assertions.
- `TestDatabaseBranches` covers insert-no-id, missing-metadata, missing-file, and flush-threshold branches.
- `TestPackUnpack` covers posting packing, extent unpacking, digest values, marks, and short-postings validation.

### Conventions

Small metadata and connection fixtures isolate serialized identity and corruption branches. Actual Git acquisition and frozen candidate leases are exercised in the snapshot companion.

### Invariants And Boundaries

Ordinary filesystem mode is explicit in database metadata as an empty candidate field. Absence of that field cannot silently assume the policy, and a different tree cannot match the ready generation.

### Todos

None recorded.

## Docs References

No Domain Documentation entries are configured for this memory root. These test contracts are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain authority is asserted. | — | — |

## Repo-Internal References

These focused database tests validate serialized identity and error branches. The snapshot suite separately exercises real Git candidate acquisition and frozen lease policy/tree separation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Generation metadata requires an explicit candidate field and refuses a different candidate, obsolete schema, wrong identity/roots or malformed application digest. | `test_generation_metadata_errors` | mcp/tests/test_l6_diff_coverage_source_index_database.py:74-94 |
| Database operations refuse absent file identifiers, size metadata and referenced files; posting buffers flush at the configured threshold. | `TestDatabaseBranches` | mcp/tests/test_l6_diff_coverage_source_index_database.py:97-136 |
| Posting, extent, digest, word-map and short-posting encodings reject the exercised corrupt shapes. | `TestPackUnpack` | mcp/tests/test_l6_diff_coverage_source_index_database.py:139-175 |

## Cross-Repo References

The exercised owners and temporary fixtures belong to this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository implementation boundary is exercised. | — | — |

## Update History

- 2026-09-06T00:21:02+00:00 — CCR L30 candidate-index recovery: documented required candidate metadata, missing-field and wrong-candidate refusal; refreshed source anchors.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
