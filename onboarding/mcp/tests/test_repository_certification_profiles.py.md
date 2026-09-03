# mcp/tests/test_repository_certification_profiles.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_repository_certification_profiles.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Forcing suite for the repository-owned certification profile contract: two-language distinct
fixture profiles compile the same four-gate protocol, the Agents Remember profile preserves its
complete approved gate inventory, selection/plan identity is digest-bound and reorder-stable, and
the L19 selector-result contract is canonical and content-addressed.

## Code Commentary

### Logic

The suite builds profiles through `repository_profile_test_support` and exercises admission,
plan compilation, gate-identity stability, semantic-input closures, and every noncanonical refusal
branch. L19 additions force the v2 selector-result contract directly: the result digest binds
candidate/population/reasons/outputs and changes under any candidate edit; unreasoned outputs and
targeted-to-full expansion refuse; declared external selector inputs change the profile digest; and
the Node and Rust fixture scripts emit `repository-selector-result/v2` JSON accepted by
`RepositorySelectionResult.model_validate_json`. The agents-remember profile's selector
configuration digest is asserted equal to `profile_selection.ownership_configuration_digest()`.

### Invariants And Boundaries

- Canonical digests are deterministic across reorderings; every digest mismatch refuses.
- Later-gate edits retain earlier-gate plan identities (the aggregate profile digest is excluded
  from per-gate semantic identity).
- A selector result must reason every output and never broaden a targeted result to full.
- The suite exercises production owners through the shared fixture builder.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; CCR-R19@v2 is the governing packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R19 packet requires canonical selection schemas/digests and at least one non-Python selector fixture. | "Expected Implementation Evidence"; "Expected Verification Evidence" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R19-v2-exact-test-selection-ownership.md:76-89 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The agents-remember profile preserves the complete approved gate inventory and binds the selector configuration digest. | `test_agents_remember_profile_preserves_the_complete_approved_gate_inventory`; `test_profile_edit_changes_profile_and_plan_identity` | mcp/tests/test_repository_certification_profiles.py:150-169; mcp/tests/test_repository_certification_profiles.py:261-299 |
| The selector-result digest binds candidate, population, reasons, and outputs. | `test_selector_result_digest_binds_candidate_population_reasons_and_outputs` | mcp/tests/test_repository_certification_profiles.py:568-598 |
| Unreasoned outputs and targeted-to-full expansion refuse; external inputs change the profile digest. | `test_selector_result_refuses_unreasoned_output_and_targeted_full_expansion`; `test_profile_digest_binds_declared_external_selector_inputs` | mcp/tests/test_repository_certification_profiles.py:601-638; mcp/tests/test_repository_certification_profiles.py:640-648 |
| Non-Python fixture selectors emit the canonical generic v2 result. | `test_non_python_selector_fixture_emits_the_canonical_generic_result` | mcp/tests/test_repository_certification_profiles.py:651-684 |
| The v2 selector contract under test. | `RepositorySelectionResult`; `build_repository_selection_result` | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:89-130; mcp/src/agents_remember/certification/repository_profiles/selection_results.py:203-241 |

## Cross-Repo References

None; the suite is repository-local and the fixtures are non-Python but in-tree.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 v2 selector-result forcing — digest binding, unreasoned-output/targeted-full refusals,
  external-input digest coupling, identity-bound fixture emission, and the ownership
  configuration-digest equality assertion. Verification is pinned to the owning commit.
