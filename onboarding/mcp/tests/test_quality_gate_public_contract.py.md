# mcp/tests/test_quality_gate_public_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_gate_public_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:11:59+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Tests selected immutable quality-result rendering, strict public quality paths, and lossless closeout-readiness projections with separate fixture scopes for publication and wire compilation.

## Code Commentary

### Logic

The selected-code fixture runs the real integration journal and publication owners over an injected executor. Pointer rotation replaces its current report pointer with another real fixture generation; rendering the supplied original selection must return the same result and original immutable decoder path without changing that pointer. A decoder definition changed under the same generation identity must refuse. Recovery does not rediscover authority through the current pointer or mint a replacement certificate.

The response-model test preserves both the mutable enclosure `reportPath` and immutable `publishedResultPath` through final tool-response validation and generated schema, while rejecting an undeclared quality-result field.

The readiness family separately constructs canonical registry, plans, admissions, Gate 1–5 manifests, certificates and finalization authority from typed compiler fixtures. It requires identical projection bytes on every declared surface and retains report-only failures and planned non-applicability. Stale certificates, invalid profiles and pre-admission states remain non-green; mixed revisions, contradictory lifecycle states, missing rail catalogs, a running gate after a red barrier, generic terminal replacement and diagnostic promotion refuse.

### Conventions

The selected-publication tests use actual temporary Git, stored original references and filesystem report generations with injected execution. The readiness fixtures use synthetic candidate and evidence identities and compiler-generated objects: they establish schema and projection behavior, not actual memory checks, Gate-5 execution or installed finalization authority. The public response-model dictionary is wire-shape input only.

### Invariants And Boundaries

- Selected rendering retains one original publication even when the current pointer names another generation.
- Same-generation decoder drift cannot alter selected publication semantics.
- Public response validation preserves both path meanings and rejects extra vocabulary.
- Readiness surfaces retain exact revision, gate, rail and certificate states; diagnostic results cannot become certification authority.
- Compiler-only finalization fixtures do not prove lifecycle completion or production Gate-5 success.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to these repository-internal forcing tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Decoder byte drift under an unchanged generation refuses selected rendering. | `test_recovery_refuses_same_id_decoder_byte_drift` | mcp/tests/test_quality_gate_public_contract.py:81-100 |
| Pointer rotation cannot replace the supplied original generation or alter its result. | `test_recovery_uses_one_manifest_generation_when_the_pointer_rotates` | mcp/tests/test_quality_gate_public_contract.py:102-117 |
| Strict response models retain both quality paths and reject unmodeled fields. | `test_public_worktree_response_models_and_retains_both_quality_paths` | mcp/tests/test_quality_gate_public_contract.py:119-163 |
| Typed compiler fixtures create the readiness chain and finalization input; they do not execute rails. | `_readiness_scenario` | mcp/tests/test_quality_gate_public_contract.py:424-469 |
| All readiness surfaces serialize the same complete projection. | `test_closeout_readiness_is_lossless_on_every_surface` | mcp/tests/test_quality_gate_public_contract.py:505-519 |
| Matching diagnostic rails retain their distinct plan and non-certifying role. | `test_diagnostic_readiness_stays_non_certifying_with_matching_rails` | mcp/tests/test_quality_gate_public_contract.py:522-542 |
| Stale certificates and invalid profile state remain non-green. | `test_stale_certificates_and_invalid_profile_remain_non_green` | mcp/tests/test_quality_gate_public_contract.py:545-584 |
| Missing admission and contradictory lifecycle authority refuse. | `test_admission_authority_and_lifecycle_contradictions_fail_closed` | mcp/tests/test_quality_gate_public_contract.py:587-647 |
| Red barriers, generic terminal replacement and mixed revisions refuse. | `test_red_gate_generic_replacement_and_mixed_revision_fail_closed` | mcp/tests/test_quality_gate_public_contract.py:650-699 |
| Incomplete rail catalogs and diagnostic promotion refuse. | `test_catalog_and_diagnostic_promotion_fail_closed` | mcp/tests/test_quality_gate_public_contract.py:702-722 |
| Invalid transitions and translated skipped state are rejected. | `test_readiness_states_and_transitions_refuse_translation` | mcp/tests/test_quality_gate_public_contract.py:725-739 |

## Cross-Repo References

The sample repository and selected-code repositories are isolated test fixtures; this file defines no separate cross-repository protocol.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## 260824-PDLS Snapshot Evidence Proof

The current recovery regression uses the supplied frozen run and original typed terminal publications. It preserves their verified decoder path through pointer rotation; readiness compiler fixtures and response dictionaries cannot substitute for those selected originals.

## Update History

- 2026-09-06T15:11:59+00:00 — L33 pending candidate curation: Re-read the prepared source, documented supplied original publication rendering and pointer independence, and restored the readiness family with an explicit compiler-fixture boundary and current anchors. Verification names the real prepared source commit c69d5171187fa1957025e393270db9f5a864ab14; this entry does not claim CCR acceptance.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the `ReportBindings`-based publication in the public quality-gate contract suite and the schema-v3.1 manifest shape it forces.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the two
  public-contract test citations to their current definitions (pointer-rotation 131-205,
  response-models 207-251) after the readiness coverage companion moved later test content.
  Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile-identity field coverage in the public gate contract tests.


- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the clean-executor and quality-gate package relocations; public recovery and response-model contracts are unchanged.
- 2026-08-24T21:23+02:00 — Added candidate-tree and one-snapshot certifying evidence proof.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for one-snapshot recovery and strict public quality-result regressions. Verification remains blank until architect-owned closeout stamps the code commit.
