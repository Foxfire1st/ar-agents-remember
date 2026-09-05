# mcp/tests/test_task_intent_coverage_edges.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_intent_coverage_edges.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00|
| governingOverview      | `overview.md`                             |

## Governing Overview

[test suite overview](overview.md)

## Purpose

Focused branch coverage for canonical task-intent consumers (CCR-R02@v2): the operation model's
intent-state coherence rules, lifecycle projection/control legacy-intent blocking, direct-landing
replay currentness, curator-coherence translation, the closeout task-intent addressing seams, door
and admission refusals, lifecycle store legacy retirement, legacy bridge intent binding, queue
projection-member intent sources, route-review translation, and the legacy census internal/bounded
matrices.

## Code Commentary

### Logic

- `test_operation_model_refuses_every_incoherent_task_intent_state` (line 79) and
  `test_operation_model_compares_legacy_intent_to_every_door_publication` (line 105) pin the
  model rules: integrate operations carry no intent, commit operations require it, and operation
  and door publication intents must agree (missing/mismatched rows refuse).
- `test_operation_projection_split_preserves_each_existing_decision` (line 126) and
  `test_operation_projection_rejects_non_mapping_public_results` (line 221) guard the L25-split
  projection helpers.
- The direct-landing rows (lines 260-390) prove claimed replay requires current canonical intent,
  the waiting/input-required refusal boundaries, and typed error translation of current door intent
  failures; `test_curator_coherence_translates_projection_and_currentness_errors` (line 392)
  covers the coherence owner.
- `test_contract_task_intent_candidate_refuses_each_addressing_failure` (line 459) forces every
  refusal of the exact candidate resolver; `test_closeout_door_and_admission_refuse_missing_or_mismatched_intent`
  (line 522) covers door + admission; the store/bridge/queue/route-review rows (lines 555-791)
  cover legacy retirement failure, candidate/legacy replacement, bridge intent refusal, projection
  member translation, and route-review confinement translation.
- The census rows (lines 809-1002) cover the internal failure matrix, the canonical task-owner
  edge matrix, and per-container malformed classification.

### Conventions

Helpers come from `test_task_intent_consumers_and_legacy` (shared payload builders) plus local
`SimpleNamespace` stubs; tests invoke production owners, never duplicated state machines.

### Invariants And Boundaries

- Absence (`MissingTaskIntent`) is never reusable, replayable, or retryable for closeout and
  direct-landing generations.
- Exit-proven cancellation-pending state remains cancelable; only terminal generations expose
  `retire-and-republish`.
- Nothing here treats queue rows, task documents, or decision prose as lifecycle authority.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty; no external documentation claim is made.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Operation-model intent coherence refusal rows. | `test_operation_model_refuses_every_incoherent_task_intent_state`; `test_operation_model_compares_legacy_intent_to_every_door_publication` | mcp/tests/test_task_intent_coverage_edges.py:79-101; mcp/tests/test_task_intent_coverage_edges.py:105-123 |
| Claimed direct-landing replay requires current canonical intent. | `test_claimed_direct_landing_replay_requires_current_canonical_intent` | mcp/tests/test_task_intent_coverage_edges.py:251-305 |
| Closeout door and admission missing/mismatched-intent refusals. | `test_closeout_door_and_admission_refuse_missing_or_mismatched_intent` | mcp/tests/test_task_intent_coverage_edges.py:513-543 |
| Legacy store retirement failure and bridge intent-binding boundary rows. | `test_lifecycle_store_legacy_retirement_failure_matrix`; `test_legacy_bridge_preserves_task_intent_refusal` | mcp/tests/test_task_intent_coverage_edges.py:546-632; mcp/tests/test_task_intent_coverage_edges.py:634-687 |
| Census internal and per-container classification matrices. | `test_legacy_census_internal_failure_and_bounded_input_matrix`; `test_legacy_census_scanners_classify_every_malformed_current_container` | mcp/tests/test_task_intent_coverage_edges.py:800-855; mcp/tests/test_task_intent_coverage_edges.py:897-993 |
| Shared payload builders the suite imports. | `_closeout_record_payload`; `_door_payload`; `_route_review_payload` | mcp/tests/test_task_intent_consumers_and_legacy.py:1-700 |

## CCR-R02@v2 Normative Task-Intent Identity

This suite is the focused consumer-coverage evidence for CCR-R02@v2
(`requirements/CCR-R02-v2-normative-task-intent-identity.md`). It proves every consumer returns
the exact unavailable/stale reason and never synthesizes a digest, and that the L25 repair's
missing-intent recover/retry blocking holds across projection and public control. Part of the
landed `99dc249b` commit.

## CCR-R18@v1 Cancellable And Incoherent-Result Forcing

260831-CCR-L18 updated this suite to the new `_operation_cancellable` contract: it now asserts the record-free signature (contract present + exact `cancel` control), drops the removed closeout-generation-retained / irreversible-boundary heuristics, and documents that a no-contract projection never advertises cancel. The non-mapping public result forcing changed from a raised `RuntimeError` to the bounded incoherent envelope: `operation_projection(record)` returns `status == "incoherent"` with the `lifecycle-projection-incoherent` result carrying the expected/observed facts, and empty legal controls, no recommendedAction, and `cancellable: false`.

## Update History

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the cancellable-signature and incoherent-envelope forcing updates. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  created this card for the new focused task-intent consumer edge suite; documented the model
  coherence rows, direct-landing/coherence/door/admission refusals, store retirement, bridge
  binding, queue/route-review translation, and census matrices. Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.
