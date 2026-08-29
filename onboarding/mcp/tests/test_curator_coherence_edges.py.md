# mcp/tests/test_curator_coherence_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_coherence_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T16:10+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
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
| Authority loading, exact candidate identity, topology, containment, and status are independently forced. | `test_authority_loader_rejects_wrong_paths_bytes_digests_and_projection`; `test_current_validator_rejects_source_and_task_identity_drift`; `test_status_distinguishes_source_absence_staleness_and_current_authority` | mcp/tests/test_curator_coherence_edges.py:396-606 |
| Publish-time CAS and atomicity checks refuse changed authority or partial output. | `test_publish_rechecks_predecessor_contract_replay_authority_and_source`; `test_projection_and_atomic_publication_edges_refuse_without_partial_output` | mcp/tests/test_curator_coherence_edges.py:607-760 |
| Every recorded evidence reference is reopened and revalidated. | `test_recorded_judgments_report_unreadable_evidence_and_recheck_every_item` | mcp/tests/test_curator_coherence_edges.py:761-790 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Tests operate on temporary local repositories and configured task roots. | — | — |

## Update History

- 2026-08-29T16:10+02:00 — Created for MCAR-L02's adversarial coherence-authority edge matrix.
  Verification remains closeout-owned.
