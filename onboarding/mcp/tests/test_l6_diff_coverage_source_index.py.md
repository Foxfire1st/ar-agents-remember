# mcp/tests/test_l6_diff_coverage_source_index.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_source_index.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:21:02+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for citation source-index edge branches: close/paths, open-and-validate, build-and-publish branches, tree bounds, and reclamation.

## Code Commentary

### Logic

- `TestCloseAndPaths` covers idempotent close and cache-root-in-code refusals.
- `TestOpenAndValidate` covers snapshot integrity, stale root mismatch, and exhausted build attempts.
- `TestBuildAndPublishBranches` covers index-byte limits and temporary-database failure.
- `TestTreeAndBounds` covers nested-memory exclusion, identity changes before/during a stable read, and count/aggregate bounds over `Identity` values. It invokes `source_index_state.check_source_bounds` and patches limits on that canonical state owner; these focused helper cases complement the snapshot suite's actual Git acquisition and pre-hash refusal tests.
- `TestReclamation` covers legacy cache-root reclaim, remove-tree, and time-remaining checks.

### Conventions

Fixtures isolate code, memory and cache roots. Fault injection targets the owner of the policy or boundary being exercised.

### Invariants And Boundaries

Source-bound helper tests receive `Identity` values and enforce canonical state-layer count/byte limits. Candidate acquisition and direct-resolution proof remain in the snapshot companion.

### Todos

None recorded.

## Docs References

No Domain Documentation entries are configured for this memory root. These test contracts are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain authority is asserted. | — | — |

## Repo-Internal References

The focused fixtures exercise publication/cache branches and the shared state-layer bound policy; actual candidate hashing and readiness preservation are covered in the snapshot companion.

| Finding | Anchor | Source |
| --- | --- | --- |
| Close is idempotent and an in-code cache root refuses. | `TestCloseAndPaths` | mcp/tests/test_l6_diff_coverage_source_index.py:51-64 |
| Frozen-integrity requests, root mismatch and exhausted source-change retries are forced. | `TestOpenAndValidate` | mcp/tests/test_l6_diff_coverage_source_index.py:67-96 |
| Index publication capacity and temporary-database validation failures refuse. | `TestBuildAndPublishBranches` | mcp/tests/test_l6_diff_coverage_source_index.py:99-131 |
| Nested memory and unstable reads remain excluded; shared state bounds reject excess count or bytes. | `TestTreeAndBounds` | mcp/tests/test_l6_diff_coverage_source_index.py:134-180 |
| Reclamation failures and exhausted time budgets remain explicit. | `TestReclamation` | mcp/tests/test_l6_diff_coverage_source_index.py:183-225 |
| Actual candidate acquisition refuses capacity before Git hashing. | `test_candidate_size_cap_refuses_before_hashing_tracked_or_dirty_oversized_members`; `test_candidate_population_caps_refuse_before_hashing_and_preserve_prior_readiness` | mcp/tests/test_memory_citation_source_index_snapshot.py:688-722; mcp/tests/test_memory_citation_source_index_snapshot.py:724-751 |

## Cross-Repo References

The exercised owners and temporary fixtures belong to this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository implementation boundary is exercised. | — | — |

## Update History

- 2026-09-06T00:21:02+00:00 — CCR L30 candidate-index recovery: reconciled shared Identity-based source-bound ownership and refreshed branch-test evidence.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
