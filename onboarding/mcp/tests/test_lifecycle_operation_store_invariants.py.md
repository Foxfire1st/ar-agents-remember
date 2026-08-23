# mcp/tests/test_lifecycle_operation_store_invariants.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operation_store_invariants.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Provides the focused forcing matrix for strict schema-3.0 lifecycle persistence, single-writer recovery, immutable identity, monotonic mutation evidence, phase-bound finalization, and exact integration retention.

## Code Commentary

### Logic

The suite drives real `LifecycleOperationStore` updates rather than validating models in isolation. It checks strict read/revalidation, claim exclusivity, valid terminal replacement, post-proof recovery refusal, immutable identity/status, pre-boundary cancellation, every legal/illegal evidence transition, fill-only recovery, finalization-hash phase rules, complete external tuples, and exact completed-integration parameters. Closeout commit proof makes clearing the derived irreversible flag model-impossible and public cancellation refuses. A valid integrate operation started through the typed generic route enters its real irreversible boundary; both direct store clearing and public cancellation then refuse. Finalization tests construct typed `LifecycleOperationRecoveryCommits` tuples, so test-only raw dictionaries cannot bypass the public/model boundary. After valid closeout finalization, an illegal public runtime attempt to move back to `quality` is refused by the finalization lifecycle evidence; the full typed record and its journal bytes remain exactly unchanged. Cases removed from the store are proven preempted at model or fill-only public boundaries instead of being silently untested.

### Invariants And Boundaries

- Only schema `3.0` records are readable; extra/legacy shapes fail closed.
- Accepted input, identity, repository leg, and proven facts cannot be replaced.
- Recovery is single-writer and fill-only.
- Cancellation stops at mutation/finalization evidence, not arbitrary phase labels.
- File-record publication is atomic; external Git sequences are not.
- Closeout irreversibility is derived from commit-proven evidence; integrate irreversibility is a typed runtime fact, and neither may be cleared through generic store writes.
- Published closeout-finalization evidence prevents later phase regression without partially rewriting either the model or journal file.

## Docs References

See task `260821-CLIVE-L1` L1-R4 through L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Strict schema, recovery ownership, replacement, and claim/cancellation boundaries are forced. | `test_store_reads_one_schema_and_revalidates_every_update`, `test_store_refuses_claim_boundary_and_ambiguous_cancellation` | mcp/tests/test_lifecycle_operation_store_invariants.py:126-139; mcp/tests/test_lifecycle_operation_store_invariants.py:175-189 |
| Model-derived closeout clearing and valid integrate clearing/cancellation both refuse at their respective irreversible boundaries. | `test_store_refuses_clearing_or_cancelling_commit_boundary`, `test_integrate_boundary_cannot_be_cleared_or_cancelled` | mcp/tests/test_lifecycle_operation_store_invariants.py:192-215; mcp/tests/test_lifecycle_operation_store_invariants.py:218-244 |
| Evidence monotonicity and fill-only preemption are forced. | `test_store_checks_mutation_evidence_monotonicity`, `test_commit_change_is_preempted_by_model_and_recovery_fill_only` | mcp/tests/test_lifecycle_operation_store_invariants.py:257-309; mcp/tests/test_lifecycle_operation_store_invariants.py:391-398 |
| Typed recovery tuples keep finalization phase rules and completed integration parameters exact; illegal public progress after finalization preserves the entire record and journal bytes. | `test_finalization_hash_transition_is_phase_bound_and_immutable`, `test_external_finalization_requires_complete_recovery_tuple`, `test_completed_integration_retains_its_exact_parameters` | mcp/tests/test_lifecycle_operation_store_invariants.py:421-484; mcp/tests/test_lifecycle_operation_store_invariants.py:487-502; mcp/tests/test_lifecycle_operation_store_invariants.py:505-523 |

## Cross-Repo References

No sibling repository owns this store; external paths appear only as repository identities inside the record.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_proven_integration_claim_timestamp_is_nonempty_and_strictly_read`, `test_store_reads_one_schema_and_revalidates_every_update`, `test_store_replacement_and_recovery_require_valid_terminal_identity`, `test_store_refuses_immutable_identity_and_status_transitions`. The L2 additions force locator-rooted journal access, legal task-addressed controls, write-ahead successors, exact worker termination, total expected-failure projection, and same-generation convergence.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_proven_integration_claim_timestamp_is_nonempty_and_strictly_read`, `test_store_reads_one_schema_and_revalidates_every_update`, `test_store_replacement_and_recovery_require_valid_terminal_identity`, `test_store_refuses_immutable_identity_and_status_transitions`. | L95-L123; L126-L139; L142-L156; L167-L172 | `mcp/tests/test_lifecycle_operation_store_invariants.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: retained prior store-boundary forcing and added full-record plus journal-byte invariance when public runtime progress attempts an illegal phase after valid finalization, against accepted tree `4241908c`; first verification stamp remains governed-closeout-owned.
