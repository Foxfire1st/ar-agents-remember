# mcp/tests/test_quality_gate_public_contract_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_gate_public_contract_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T13:30+02:00 |
| lastVerifiedCommitHash | `eb05a872780112640359232063168639d20fa87b` |
| lastVerifiedCommitDate | 2026-09-03T06:19:25+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Self-contained closeout-readiness coverage companion to the public-contract module
(`test_quality_gate_public_contract.py`). It carries the negative fixtures that complete diff
coverage of `certification/readiness.py` and `certification/readiness_models.py` without
pushing the public-contract module past the 1,200-line file-size hard limit (CCR-R09@v3 successor
repair 260831-CCR-L27 S2.2, closing the Run-3 Gate-3 python-diff-coverage defect). The module is
fully standalone: it inlines its own scenario scaffold over the production certification models
and never imports test-support or fixture modules, so the evidence-lifecycle catalog observes no
transitive test-support consumers here.

## Code Commentary

### Logic

The scenario builder `_readiness_scenario` (`test_quality_gate_public_contract_coverage.py:354-399`)
constructs the canonical registry -> plan -> repository plan -> admission -> five manifests ->
five certificates -> finalization tower using `_readiness_registry`
(`test_quality_gate_public_contract_coverage.py:171-202`), `_readiness_manifest`
(`test_quality_gate_public_contract_coverage.py:283-336`), and `_readiness_admission`
(`test_quality_gate_public_contract_coverage.py:252-280`); `_complete_readiness_input`
(`test_quality_gate_public_contract_coverage.py:402-428`) assembles the green
`CloseoutReadinessInput`. Thirteen focused contract tests then force the compiler and models
fail closed: `test_project_closeout_readiness_refuses_unknown_surface`
(`test_quality_gate_public_contract_coverage.py:484-488`); `test_closeout_readiness_requires_the_exact_certifying_plan`
(`test_quality_gate_public_contract_coverage.py:491-501`); `test_profile_state_requires_exact_repository_plan_authority`
(`test_quality_gate_public_contract_coverage.py:504-562`); `test_gate_order_and_result_disposition_contracts_fail_closed`
(`test_quality_gate_public_contract_coverage.py:565-590`); `test_current_certificate_contradictions_fail_closed`
(`test_quality_gate_public_contract_coverage.py:593-618`); `test_gate_manifest_and_rail_result_contracts_fail_closed`
(`test_quality_gate_public_contract_coverage.py:621-680`); `test_report_only_pass_rail_preserves_typed_state`
(`test_quality_gate_public_contract_coverage.py:683-709`); `test_certificate_chain_and_gate_five_inputs_fail_closed`
(`test_quality_gate_public_contract_coverage.py:712-731`); `test_gate_prerequisite_must_be_current_green_before_start`
(`test_quality_gate_public_contract_coverage.py:734-762`); `test_diagnostic_catalog_candidate_and_gate_rails_fail_closed`
(`test_quality_gate_public_contract_coverage.py:765-862`); `test_finalization_lifecycle_contracts_fail_closed`
(`test_quality_gate_public_contract_coverage.py:865-904`); `test_readiness_observation_validators_refuse_incoherent_shapes`
(`test_quality_gate_public_contract_coverage.py:907-950`); and `test_readiness_projection_digest_verification_refuses_tampering`
(`test_quality_gate_public_contract_coverage.py:953-958`). Digest-rebinding helpers
(`_rebuilt_rail_result` at `test_quality_gate_public_contract_coverage.py:458-462`,
`_rebuilt_manifest` at `test_quality_gate_public_contract_coverage.py:465-472`,
`_manifest_with_registry_digest` at `test_quality_gate_public_contract_coverage.py:475-481`)
keep mutated fixtures content-addressable so the compiler's identity checks stay meaningful.

### Conventions

Every refusal asserts an exact finding code via `_readiness_codes`
(`test_quality_gate_public_contract_coverage.py:431-432`); the module is pragmatic-coverage
only and never imports test-support.

### Invariants And Boundaries

- Only negative fixtures live here; green-path parity stays in the public-contract module.
- No test-support or fixture-module imports, so no transitive evidence-lifecycle dependency.
- Mutated rail results and manifests are re-bound to their exact content digests before compilation.
- The suite targets readiness compilation and model validation, never repository-profile execution.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; CCR-R09@v3 and the 260831-CCR-L27 successor
repair manifest are the governing artifacts.

| Finding | Anchor | Source |
| --- | --- | --- |
| Expected verification evidence requires red-gate, stale-certificate, invalid-profile, diagnostic, generic-exception, and mixed-generation negative fixtures. | `test_gate_prerequisite_must_be_current_green_before_start` | mcp/tests/test_quality_gate_public_contract_coverage.py:734-762 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The scenario tower builds exact registry/plan/admission/finalization authority for negative fixtures. | `_readiness_scenario`; `_complete_readiness_input` | mcp/tests/test_quality_gate_public_contract_coverage.py:354-428 |
| Compiler refusals are forced across plan, admission, profile, gate, certificate, barrier, diagnostic, and lifecycle contracts. | `test_gate_order_and_result_disposition_contracts_fail_closed`; `test_finalization_lifecycle_contracts_fail_closed` | mcp/tests/test_quality_gate_public_contract_coverage.py:565-590; mcp/tests/test_quality_gate_public_contract_coverage.py:865-904 |
| Model validators refuse incoherent observation shapes and tampered projection digests. | `test_readiness_observation_validators_refuse_incoherent_shapes`; `test_readiness_projection_digest_verification_refuses_tampering` | mcp/tests/test_quality_gate_public_contract_coverage.py:907-958 |
| The companion module keeps the public-contract module under the file-size hard limit. | `test_closeout_readiness_is_lossless_on_every_surface` | mcp/tests/test_quality_gate_public_contract.py:592-607 |
| The suite is standalone; the evidence-lifecycle catalog records no transitive test-support consumer. | `_ReadinessScenario` | mcp/tests/test_quality_gate_public_contract_coverage.py:98-107 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| The coverage companion is repository-local and exercises production certification owners through its focused refusal tests. | `test_project_closeout_readiness_refuses_unknown_surface` | mcp/tests/test_quality_gate_public_contract_coverage.py:484-490 |

## Update History

- 2026-09-03T14:00+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the
  standalone-suite row to the test that actually exercises the production owners, and
  pinned lastVerifiedCommitHash to the leaf base commit eb05a872 (the recorded tree
  object was not a commit; the owning commit stamp remains closeout-owned).

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: created for the focused
  closeout-readiness coverage companion (CCR-R09@v3 successor repair S2.2): thirteen negative
  fixtures completing diff coverage of readiness.py/readiness_models.py, standalone scenario
  scaffold with digest-rebinding helpers. Verification is pinned to the staged candidate tree
  `74d188bbee`; the final commit stamp is closeout-owned.
