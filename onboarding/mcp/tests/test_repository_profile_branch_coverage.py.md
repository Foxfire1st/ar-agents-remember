# mcp/tests/test_repository_profile_branch_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_repository_profile_branch_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Branch-forcing suite for repository-profile validation: every fail-closed validation branch of
catalog/selection/rail/selector/planning/authority/execution/decoder validation is exercised with
an exact expected finding code, and the L19 selection-result reader boundary is loaded from the
Dagger quality source and forced independently.

## Code Commentary

### Logic

The suite builds one canonical fixture profile and mutates a single surface per case, asserting
`validate_repository_profile` emits the expected finding code. `test_profile_selection_validation_reports_each_fail_closed_branch`
and `test_profile_rail_validation_reports_each_fail_closed_branch` own the selection/rail
branch matrices. L19 adds the `duplicate-selector-field` branch (duplicate external inputs).

The L19 reader cases load `.dagger/src/agents_remember_quality/selection_result.py` by file
location and prove its `parse_selection_result` refuses a stale candidate identity and an
unreasoned population, tying the Dagger-side selector reader to the canonical v2 contract. The
suite also forces rejections in the selector-result components (noncanonical or misclassified
values), path/gate selection models, canonical profile and semantic inputs, planning
order/identity/digest drift, typed planning/selection/semantic-input failures, executor/decoder
confinement, and profile-authority schema/semantics/filesystem edges.

### Invariants And Boundaries

- Each case mutates exactly one surface and asserts the exact finding code.
- The Dagger selector reader is loaded as source, never imported from a released package.
- All refusals are typed and fail closed; no branch falls through to a partial result.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; CCR-R19@v2 is the governing packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R19 packet requires typed ownership failure and no silent broadening. | "Required Behavior"; "Failure And Recovery" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R19-v2-exact-test-selection-ownership.md:23-49 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selection and rail validation branches each emit the expected code. | `test_profile_selection_validation_reports_each_fail_closed_branch`; `test_profile_rail_validation_reports_each_fail_closed_branch` | mcp/tests/test_repository_profile_branch_coverage.py:167-212; mcp/tests/test_repository_profile_branch_coverage.py:214-275 |
| The Dagger selector reader refuses stale identity and unreasoned population. | `test_dagger_selector_reader_refuses_stale_identity_and_unreasoned_population` | mcp/tests/test_repository_profile_branch_coverage.py:278-370 |
| Selector-result components and planning/authority surfaces refuse every invalid branch. | `test_selector_result_components_refuse_noncanonical_or_misclassified_values`; `test_profile_plan_refuses_order_identity_and_digest_drift` | mcp/tests/test_repository_profile_branch_coverage.py:372-449; mcp/tests/test_repository_profile_branch_coverage.py:505-527 |
| The production validator under branch forcing. | `validate_repository_profile` | mcp/src/agents_remember/certification/repository_profiles/validation.py:57-126 |

## Cross-Repo References

The Dagger source reader is loaded from the in-repo `.dagger` tree, not an external package.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 additions — the `duplicate-selector-field` branch and the Dagger selector-reader
  identity/population refusal cases. Verification is pinned to the owning commit.
