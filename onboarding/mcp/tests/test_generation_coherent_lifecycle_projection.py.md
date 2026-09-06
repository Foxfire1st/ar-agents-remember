# mcp/tests/test_generation_coherent_lifecycle_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_generation_coherent_lifecycle_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:42:13+00:00 |
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The CCR-R18 (260831-CCR-L18) forcing suite for generation-coherent lifecycle operation
projection. It pins the state matrix, the atomic projection envelope, journal-revision
discipline, worker/approval observations, recommended-action guidance, cross-task next-step
bounding, and the store/cleanup guards introduced by the L18 change-set. The module registers in
`mcp/tests/test-evidence-lanes.toml` as explicit `unit-regression` evidence.

## Code Commentary

### Logic

The suite is built around standalone fixture helpers inlined at the top of the module (they import
only `agents_remember.*` production sources, never pre-existing `mcp/tests` support modules):

- `start_closeout_operation` routes a durable-input fixture through canonical raw, lease-bound
  admission, bypassing only the first-ready scheduling projection when the fixture owns a
  synthetic waiting door.
- `ensure_fixture_waiting_door` / `_fixture_waiting_door` publish one typed test-only source
  generation (`test-fixture:` provenance) for below-queue lifecycle suites that need a real door
  or the synthetic scheduling fence.

The behavioral forcing covers, among others:

- `test_every_lifecycle_status_projects_one_bound_matrix_cell` and
  `test_state_matrix_exhausts_status_and_phase_vocabularies` pin every public status/phase cell to
  exactly one `STATE_MATRIX` rule and assert the matrix exhausts the Literal vocabularies.
- `test_state_matrix_exhaustiveness_failure_is_raised` proves the import-time exhaustiveness
  guard trips when the matrix is desynced (monkeypatched vocabulary).
- Healthy-live, real-termination-recovery, exit-proven-cancellation, and generation-11/15
  contradiction tests (`test_healthy_live_worker_is_legal_to_cancel_but_recommended_to_observe`,
  `test_real_termination_recovery_recommends_its_exact_legal_cancel`,
  `test_exit_proven_cancellation_keeps_only_same_generation_cancel`,
  `test_generation_11_and_15_contradictions_refuse_without_controls`) exercise the
  `validate_projection_state` refusal cells and the recommended-action derivation.
- `test_adjacent_revision_race_refuses_stale_result_approval_and_worker_facts` and
  `test_adjacent_generation_candidate_fact_cannot_splice_into_current_projection` prove
  revision/generation splicing refuses through the identity + bindings guards.
- Store discipline: `test_store_revision_is_monotonic_and_stale_cas_cannot_publish`,
  `test_store_revision_discipline_guards_are_enforced` cover the exact-once record-revision
  advance, no-op short-circuits, and revision-1 creation gate.
- Guidance: `test_cross_task_next_step_is_omitted_while_exact_and_external_guidance_remain`
  exercises `bound_next_step` in `application/tool_response.py`;
  `test_projection_rejects_recommendation_or_control_for_another_task`,
  `test_projection_rejects_live_cancel_guidance_and_invalid_control_matrix`, and
  `test_recommendation_must_match_one_exact_mutating_legal_control` pin the envelope validator.
- Envelope cells: `test_projection_owned_decision_rebinds_every_component_and_clears_controls`,
  `test_projection_envelope_refusal_cells_are_bounded`,
  `test_incoherent_envelope_refuses_advertised_authority`,
  `test_component_bindings_helper_refuses_missing_identity`,
  `test_coherent_components_require_an_explicit_worker_observation`, and
  `test_task_address_validation_requires_an_identity` cover
  `bind_projection_result` / `bind_projection_decision` and the private
  `_require_*` guards.
- `test_terminal_archive_uses_observed_exit_without_rewriting_audit_identity` pins the
  terminal-enclosure archive's use of `project_worker_exit` for `_require_archivable_operation`.
- Worker cells: `test_worker_binding_projection_guards_refuse_incoherent_cells` exercises
  `_require_all_or_none_worker_binding` / `_termination_bound_worker_observation`;
  `test_cancel_request` matrix refusal is covered by
  `test_validate_projection_state_refuses_cancel_request_outside_termination`.
- `test_projection_cell_refuses_non_cancel_controls_on_termination_required` pins the
  termination-required control cell.

### Conventions

Each test drives real production paths through real task contracts and durable journal records;
only subprocess/lifecycle mutation endpoints and the first-ready scheduling fence are mocked at
their external boundary. New matrix cells are asserted through the production
`validate_projection_state`, never by re-implementing the matrix in the test.

### Invariants And Boundaries

- One readable envelope binds one exact journal revision; stale result/approval/worker facts from
  an adjacent revision refuse.
- An incoherent envelope never advertises mutating authority (recommendedAction, legal controls,
  cancellable all empty/false).
- Record revision advances exactly once per accepted store mutation; new generations begin at
  revision 1.
- Guidance naming another task address is omitted or refused; developer-decision and
  would-supersede previews rebind every component digest.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for this repository-owned suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs this test module. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection state matrix and envelope contracts under test. | `STATE_MATRIX`; `LifecycleOperationProjection`; `validate_projection_state` | mcp/src/agents_remember/models/lifecycles/operation_projection.py:116-388 |
| The projection construction and bind helpers exercised by the suite. | `operation_projection`; `bind_projection_result`; `bind_projection_decision`; `operation_projection_identity` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:81-330 |
| The record-revision store discipline under test. | `LifecycleOperationStore`; `_advance_record_revision`; `_validate_identity_and_evidence_transition` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:310-375; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:471-765 |
| The cross-task next-step bounding exercised by the suite. | `bound_next_step` | mcp/src/agents_remember/application/tool_response.py:24-56 |
| The terminal-archive observed-exit guard under test. | `_require_archivable_operation`; `project_worker_exit` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:531-543 |
| The explicit unit-regression lane registration. | "mcp/tests/test_generation_coherent_lifecycle_projection.py" | mcp/tests/test-evidence-lanes.toml:82-82 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository forcing suite; nothing crosses repositories. | — | — |

## Update History

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.
- 2026-09-05T06:24:16+00:00: Generated citation repair: "mcp/tests/test_generation_coherent_lifecycle_projection.py" repointed to mcp/tests/test-evidence-lanes.toml:81-81. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: created for the new
  generation-coherent lifecycle projection forcing suite (state matrix, envelope bindings,
  revision discipline, worker/approval observations, recommended action, cross-task next-step
  bounding, terminal-archive observed exit). Verified at code commit
  f93ac631ca161e5880db3a937728cb256686b13b.
