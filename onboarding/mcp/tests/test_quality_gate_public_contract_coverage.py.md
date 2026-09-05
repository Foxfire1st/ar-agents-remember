# mcp/tests/test_quality_gate_public_contract_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_gate_public_contract_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T07:08:26+00:00 |
| lastVerifiedCommitHash | `cb906188f2572c643eac12842a68f8ddf87101e2` |
| lastVerifiedCommitDate | 2026-09-03T18:04:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Self-contained closeout-readiness test companion to `test_quality_gate_public_contract.py`.
Its thirteen focused cases cover compiler refusals, a successful report-only projection, and
readiness-model validation. The source header records why this coverage was split out: keep
the public-contract module within the file-size limit while exercising readiness branches.
That rationale is not a current measured coverage result.

## Code Commentary

### Logic

`_readiness_scenario` builds a registry, certification plan, repository plan, admission,
five gate manifests, five certificates and finalization through production domain compilers.
`_complete_readiness_input` assembles a complete input from those fixtures. The identities,
results and artifact evidence are synthetic test data; this construction does not execute
repository-profile gates.

The tests vary plan and profile authority, gate order and result disposition, certificate and
manifest identities, evidence, diagnostic catalogs, prerequisites, memory inputs, and lifecycle
finalization. Digest-rebinding helpers reconstruct mutated rail results and manifests so that
the intended contract contradiction is tested with a consistent content digest.

`test_report_only_pass_rail_preserves_typed_state` is a positive compilation case: the
projection retains `report-only-pass`, while `certificationReady` remains false. The
observation-validator and digest-tampering cases instead expect Pydantic `ValidationError`.

### Conventions

Compiler-refusal cases inspect specific finding codes through `_readiness_codes`. Model
validation cases assert `ValidationError`; they do not all assert a compiler finding code.
The module defines its fixtures locally and imports production owners directly, with no
test-support or fixture-module imports.

### Invariants And Boundaries

- Both negative contract cases and one successful report-only case live here.
- Rebound content digests keep deliberate fixture contradictions distinct from incidental stale hashes.
- Synthetic certificate/finalization fixtures exercise readiness compilation and model validation.
  They are not evidence that the production gate, closeout path or repository execution passed.
- This card records source review; no new coverage measurement or test execution is claimed.

### Todos

None recorded in this source.

## Docs References

No external Domain Documentation source is configured for this internal route. The source header
records the local split rationale; historical CCR-L27 curation remains in Update History.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module owns its fixture scaffold and imports production owners directly; the split rationale is recorded in its source header. | "Self-contained closeout-readiness coverage companion to the public-contract module." | mcp/tests/test_quality_gate_public_contract_coverage.py:1-96 |
| Synthetic registry, repository profile, admission, five gate manifests/certificates and finalization form the test scenario. | `_readiness_registry`; `_readiness_admission`; `_readiness_manifest`; `_readiness_scenario`; `_complete_readiness_input` | mcp/tests/test_quality_gate_public_contract_coverage.py:171-202; mcp/tests/test_quality_gate_public_contract_coverage.py:252-280; mcp/tests/test_quality_gate_public_contract_coverage.py:283-336; mcp/tests/test_quality_gate_public_contract_coverage.py:354-428 |
| Mutated rail results and manifests are reconstructed with matching content digests. | `_rebuilt_rail_result`; `_rebuilt_manifest`; `_manifest_with_registry_digest` | mcp/tests/test_quality_gate_public_contract_coverage.py:458-481 |
| Compiler refusals cover unknown surfaces, exact certifying-plan identity and repository-profile admission authority. | `test_project_closeout_readiness_refuses_unknown_surface`; `test_closeout_readiness_requires_the_exact_certifying_plan`; `test_profile_state_requires_exact_repository_plan_authority` | mcp/tests/test_quality_gate_public_contract_coverage.py:484-562 |
| Gate order, result disposition, certificate contradictions and manifest/rail evidence fail closed. | `test_gate_order_and_result_disposition_contracts_fail_closed`; `test_current_certificate_contradictions_fail_closed`; `test_gate_manifest_and_rail_result_contracts_fail_closed` | mcp/tests/test_quality_gate_public_contract_coverage.py:565-680 |
| A valid report-only rail remains typed report-only-pass while the projection is not certification-ready. | `test_report_only_pass_rail_preserves_typed_state` | mcp/tests/test_quality_gate_public_contract_coverage.py:683-709 |
| Certificate chains, Gate-5 memory inputs and prerequisites require current matching authority. | `test_certificate_chain_and_gate_five_inputs_fail_closed`; `test_gate_prerequisite_must_be_current_green_before_start` | mcp/tests/test_quality_gate_public_contract_coverage.py:712-762 |
| Diagnostic catalog/candidate/rail identity and finalization lifecycle contradictions are refused. | `test_diagnostic_catalog_candidate_and_gate_rails_fail_closed`; `test_finalization_lifecycle_contracts_fail_closed` | mcp/tests/test_quality_gate_public_contract_coverage.py:765-904 |
| Observation models reject incoherent shapes and tampered projection digests with ValidationError. | `test_readiness_observation_validators_refuse_incoherent_shapes`; `test_readiness_projection_digest_verification_refuses_tampering` | mcp/tests/test_quality_gate_public_contract_coverage.py:907-958 |
| Compiler-refusal assertions collect typed finding codes through one helper. | `_readiness_codes` | mcp/tests/test_quality_gate_public_contract_coverage.py:431-432 |

## Cross-Repo References

No cross-repository evidence is required.

## Update History

- 2026-09-05T07:08:26+00:00 — L31 full-card source review against frozen code
  `ea35964985f30080488270e71ac81657ac40682b`: read all 962 source lines and corrected the
  negative-only description, finding-code convention, and distinction between synthetic domain
  fixtures and production execution evidence. Removed unsupported current coverage and catalog
  measurement claims while preserving the recorded split rationale. The previous verification
  stamp `eb05a872780112640359232063168639d20fa87b` predates this file. Refreshed to its actual
  source-owning commit `cb906188f2572c643eac12842a68f8ddf87101e2`; that commit and frozen HEAD
  share source blob `69e29205b27693df1660b2ebe638e678cb2f39cc`. Prior dated entries are retained
  as historical provenance. This source review is not test execution or gate acceptance.


- 2026-09-03T14:00+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the
  standalone-suite row to the test that actually exercises the production owners, and
  pinned lastVerifiedCommitHash to the leaf base commit eb05a872 (the recorded tree
  object was not a commit; the owning commit stamp remains closeout-owned).

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: created for the focused
  closeout-readiness coverage companion (CCR-R09@v3 successor repair S2.2): thirteen negative
  fixtures completing diff coverage of readiness.py/readiness_models.py, standalone scenario
  scaffold with digest-rebinding helpers. Verification is pinned to the staged candidate tree
  `74d188bbee`; the final commit stamp is closeout-owned.
