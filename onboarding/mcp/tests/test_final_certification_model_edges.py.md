# mcp/tests/test_final_certification_model_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_certification_model_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:42:13+00:00 |
| lastVerifiedCommitHash | `16d1a4d6d6f8e8572b4bca10b8a4a84485449604` |
| lastVerifiedCommitDate | 2026-09-04T00:55:21+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

CCR-R08 forcing suite for the closed final-certification model and application refusal edges:
the `final_certification.models` validators, the bounded `FinalCertificationError`
`response_fields` projection, and the controller's final-full-catalog pair-identity guard.
Every negative construction asserts a refusal rather than a fallback; shared fixtures are
imported from `test_final_full_memory_coherence_certification`. The suite is explicitly
registered in the `integration` lane of `test-evidence-lanes.toml`.

## Code Commentary

### Logic

- Item-result edges: `test_item_result_refuses_blocked_without_blocked_by` (131-138),
  `test_item_result_refuses_passing_with_findings` (141-148), and
  `test_item_result_refuses_not_applicable_with_findings` (151-158).
- Plan edges: `test_catalog_plan_refuses_wrong_plan_digest` (166-177) and
  `test_catalog_plan_refuses_duplicate_items` (180-192).
- Attestation edges: `test_attestation_refuses_inexact_planned_population` (200-206),
  `test_attestation_refuses_derived_status_counts_mismatch` (209-214), and
  `test_attestation_refuses_ok_without_red_or_blocked` (217-222).
- Result edges: memory-tree binding (`test_result_refuses_attested_memory_tree_mismatch`
  230-234), plan-digest binding (`test_result_refuses_plan_digest_mismatch` 237-246),
  non-git-tree memory input (`test_result_refuses_non_git_tree_memory_input` 249-252),
  unbound memory value (`test_result_refuses_unbound_memory_input_value` 255-258), and
  red/blocked finalization eligibility (`test_result_refuses_red_finalization_eligibility`
  261-264); the green result additionally requires a fully passing catalog, assembled Gate-5
  inputs, a current coherence record, reused Gates 1-4, and eligibility (314-347).
- Wire edges: `test_final_certification_error_response_fields_bounded` (355-373) forces the
  bounded `response_fields` projection of `FinalCertificationError`, and
  `test_controller_projection_requires_exact_pair_identity` (381-390) forces the
  controller's `_attach_final_full_catalog` guard to refuse without the exact pair identity.

### Conventions

The `green` (59-61), `_inputs` (64-72), `_rebuild_plan` (75-103), `_red`
(106-123) and `_green_variant` (275-311) builders provide valid mutation bases; every
mutation asserts `ValueError` or the exact refusal.

### Invariants And Boundaries

- Models stay closed and immutable; digest, population, and status-shape invariants are forced.
- Only a green certification is finalization-eligible.
- The final-full-catalog projection on the controller is pair-identity-bound.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Item-result, plan, and attestation validators refuse wrong shapes. | `test_item_result_refuses_blocked_without_blocked_by`; `test_catalog_plan_refuses_wrong_plan_digest`; `test_attestation_refuses_inexact_planned_population` | mcp/tests/test_final_certification_model_edges.py:131-138; mcp/tests/test_final_certification_model_edges.py:166-177; mcp/tests/test_final_certification_model_edges.py:200-206 |
| Final-certification binding and green-state edges. | `test_result_refuses_attested_memory_tree_mismatch`; `test_green_result_refuses_non_passing_catalog` | mcp/tests/test_final_certification_model_edges.py:230-234; mcp/tests/test_final_certification_model_edges.py:314-327 |
| The bounded typed error projection and controller pair-identity guard. | `test_final_certification_error_response_fields_bounded`; `test_controller_projection_requires_exact_pair_identity` | mcp/tests/test_final_certification_model_edges.py:355-373; mcp/tests/test_final_certification_model_edges.py:381-390 |
| The suite is registered in the integration lane of the evidence manifest. | "mcp/tests/test_final_certification_model_edges.py" | mcp/tests/test-evidence-lanes.toml:407-407 |

## Update History

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 closed model/application refusal-edge forcing suite
  delivered in code commit 16d1a4d6; anchors and ranges derived from the current worktree source
  and pinned to that commit. The suite entered the `integration` lane of
  `test-evidence-lanes.toml` in the same change.
