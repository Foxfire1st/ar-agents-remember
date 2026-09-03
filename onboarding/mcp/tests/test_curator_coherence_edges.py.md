# mcp/tests/test_curator_coherence_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_coherence_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces the malformed, stale, conflicting, and partial-publication edges around the one canonical
curator-coherence authority that the focused happy-path suite deliberately does not duplicate.

## Code Commentary

### Logic

The suite first pins strict request, attestation, record, and response shapes. It then exercises
configured-contract translation, memory-quality projection, MCP registration, future-code capture,
authority loading, source/task drift, applicability and containment, status classification,
publish-time compare-and-swap rechecks, atomic projection failure, and evidence revalidation.

Under CCR-R03@v1 the attestation edge cases route through a `_QualityAttestationSource` helper that
carries the exact code/memory candidate trees; the attestation boundary refusals
(unreadable, not-ready, wrong pair) are re-driven through that source shape
cit:([`_quality_source`, `test_attestation_topology_and_path_boundaries_fail_with_typed_refusals`,
`test_attestation_rejects_a_different_code_memory_pair`], mcp/tests/test_curator_coherence_edges.py:156-176, 576-606, 621-640).

### Conventions

Small model tests use direct typed values; filesystem and publication edges use temporary exact
artifacts and the existing queue fixture. Every refusal asserts the typed status and observed facts
rather than accepting a generic exception.

### Invariants And Boundaries

- Missing, extra, duplicate, malformed, or stale judgments never become a live authority.
- Publication rechecks predecessor, candidate trees, task topology, attestation, and evidence.
- A projection or atomic-write failure leaves no partially published canonical record.
- The suite never supplies semantic dispositions on behalf of the curator; it verifies their
  identity and evidence envelope only.
- Dagger owns certifying execution.
- Attestation refusal cases are forced through the dependency-aware source shape, so tree
  availability is part of every boundary.

### Todos

None recorded.

## Docs References

No configured external documentation applies; this is repository-owned lifecycle evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for the failure matrix. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Strict models and public translations reject malformed or incomplete authority inputs. | `test_models_refuse_blank_mismatched_and_duplicate_authority_inputs`; `test_request_and_response_shapes_are_total_and_action_specific`; `test_application_projects_domain_and_post_execution_refusals` | mcp/tests/test_curator_coherence_edges.py:156-310 |
| Authority loading, exact candidate identity, topology, containment, and status are independently forced. | `test_authority_loader_rejects_wrong_paths_bytes_digests_and_projection`; `test_current_validator_rejects_source_and_task_identity_drift`; `test_status_distinguishes_source_absence_staleness_and_current_authority` | mcp/tests/test_curator_coherence_edges.py:433-483; mcp/tests/test_curator_coherence_edges.py:486-516; mcp/tests/test_curator_coherence_edges.py:620-659 |
| Publish-time CAS and atomicity checks refuse changed authority or partial output. | `test_publish_rechecks_predecessor_contract_replay_authority_and_source`; `test_projection_and_atomic_publication_edges_refuse_without_partial_output` | mcp/tests/test_curator_coherence_edges.py:692-764; mcp/tests/test_curator_coherence_edges.py:767-843 |
| Every recorded evidence reference is reopened and revalidated. | `test_recorded_judgments_report_unreadable_evidence_and_recheck_every_item` | mcp/tests/test_curator_coherence_edges.py:846-875 |
| R03 dependency-aware attestation source shape. | `_quality_source` | mcp/tests/test_curator_coherence_edges.py:156-176 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Tests operate on temporary local repositories and configured task roots. | — | — |

## MCAR-L03 Pair Edge Cases

Edge coverage requires pair data in every strict record/attestation fixture, rejects a different
attested pair, carries pair observation through publication race checks, and proves named
pair-field/repair-argument projection through the public coherence boundary.

## 260831-CCR-R03 Attestation-Source Edges

The attestation refusal matrix now exercises the source shape carrying exact candidate trees
(worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the dependency-aware `_QualityAttestationSource` routing in the attestation boundary cases; prior model, CAS, and pair edge prose preserved.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: supplied complete pair-address fixture cells and
  separately forced pair, future-code, and generic candidate-read translations.

- 2026-08-29T21:46+02:00 — MCAR-L03: added wrong-pair and typed pair-refusal coherence edge
  coverage. Dagger verification remains closeout-owned.

- 2026-08-29T16:10+02:00 — Created for MCAR-L02's adversarial coherence-authority edge matrix.
  Verification remains closeout-owned.