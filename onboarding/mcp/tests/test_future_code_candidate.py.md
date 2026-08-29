# mcp/tests/test_future_code_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_future_code_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T05:17+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Provides the focused mutation and refusal matrix for exact future-code candidate identity.

## Code Commentary

### Logic

The primary case constructs a real temporary Git repository whose index intentionally differs from
the working tree, then combines staged and unstaged content, deletion, rename, eligible untracked,
and ignored paths. It compares production capture with an independently materialized add-all tree
and proves the real index bytes remain unchanged. Adjacent cases force content/base/HEAD
invalidation, prove the closeout snapshot consumes the exact identity, force concurrent captures,
mid-observation HEAD movement, route exclusion, strict schema rejection, and identity immutability.

### Conventions

Fixtures use real Git commands for tree semantics and narrow mocks only for the otherwise
nondeterministic mid-observation HEAD race. No test reproduces the production tree algorithm as an
acceptance owner; the independent tree is only an oracle inside the fixture repository.

### Invariants And Boundaries

- Ignored files never enter the candidate; eligible untracked files do.
- The working-tree version wins over an earlier staged version because closeout uses add-all.
- The production capture cannot mutate the primary index.
- Concurrent captures use distinct indexes and leave no enclosure residue.
- Missing/extra identity fields and route drift fail closed.
- An issued identity cannot be mutated in place.
- These tests are certifying only when executed by the lifecycle-owned Dagger route.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root; the regression contract is
repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is needed for this focused Git-boundary suite. | — | — |

## Repo-Internal References

The suite directly targets the future-code owner and verifies its full required input matrix.

| Finding | Anchor | Source |
| --- | --- | --- |
| The add-all mutation matrix covers staged/unstaged content, deletion, rename, untracked, ignored, and unchanged real-index bytes. | `test_capture_uses_an_isolated_full_add_all_tree_without_mutating_the_real_index` | mcp/tests/test_future_code_candidate.py:76-112 |
| The leaf closeout adapter consumes the exact future-code tree and observed HEAD. | `test_leaf_closeout_snapshot_consumes_the_exact_future_code_identity` | mcp/tests/test_future_code_candidate.py:115-124 |
| Concurrent captures use distinct temporary indexes and leave no residue. | `test_concurrent_capture_uses_distinct_temporary_indexes` | mcp/tests/test_future_code_candidate.py:127-135 |
| Changed content and bound route fields invalidate reuse. | `test_recomputation_invalidates_changed_candidate_content`; `test_recomputation_invalidates_changed_bound_route_identity` | mcp/tests/test_future_code_candidate.py:138-162 |
| Mid-capture HEAD movement and non-leaf use have typed refusals. | `test_capture_refuses_when_head_moves_during_observation`; `test_future_code_capture_refuses_the_existing_commit_route` | mcp/tests/test_future_code_candidate.py:165-182; mcp/tests/test_future_code_candidate.py:213-219 |
| The strict schema rejects missing and caller-invented fields. | `test_future_code_schema_forbids_missing_identity_fields`; `test_future_code_schema_forbids_caller_extra_identity_fields` | mcp/tests/test_future_code_candidate.py:222-229; mcp/tests/test_future_code_candidate.py:232-241 |
| An issued identity is immutable. | `test_future_code_identity_is_immutable` | mcp/tests/test_future_code_candidate.py:244-252 |

## Cross-Repo References

No meaningful cross-repository boundary applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The test uses only temporary repositories and the target package. | — | — |

## Update History

- 2026-08-29T05:17+02:00 — A003 self-review repair: added real concurrent-capture cleanup and
  frozen-identity regression cases, then refreshed exact symbol ranges.

- 2026-08-29T04:55+02:00 — Added the focused closeout-snapshot consumption assertion and
  refreshed the test-symbol ranges before freezing the successor candidate.

- 2026-08-29T04:55+02:00 — Citation maintenance: normalized all evidence tables to the
  canonical finding/anchor/source contract after the first full memory-quality pass.

- 2026-08-29T04:55+02:00 — Created for the exact future-code route identity, isolated add-all
  semantics, stale-input matrix, and no-real-index-mutation proof. Verification metadata remains
  empty until lifecycle closeout.
