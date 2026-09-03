# mcp/tests/test_certification_contract_model_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_certification_contract_model_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3`|
| lastVerifiedCommitDate | 2026-09-03T00:47:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves closed-model, digest, plan-catalog, terminal-publication, and typed-error edges that keep the
generic five-gate certification contract exact under adversarial payloads, and — since CCR-R05@v3 —
the closed-model edges of the exact-candidate lifecycle records (conflict shapes, durable
finalization legs, prior-red dispositions, and the finalization journal).

## Code Commentary

### Logic

The suite varies applicability payloads, registry/plan/result/manifest digests, execution-wave
graphs, gate and certification plan catalogs, blocker/evidence/artifact identity, terminal
admission, immutable error payloads, and busy-adapter send certainty (`test_applicability_status_requires_its_exact_payload` through `test_busy_adapter_error_refuses_uncertain_send_state`, lines 99-550). The L05 model additions (lines 231-352) force `ExactCandidateObservation` conflict-shape consistency, `DurableFinalizationLeg` state-shape mismatches, `RedCatalogDisposition` direct-repair versus repaired-root shapes, and `FinalizationJournalState` legal order plus `next_leg` semantics. Every case consumes the portable shared registry builders and asserts a stable model or contract refusal.

### Conventions

Local helpers only rebuild deliberately forged digest-bearing models. Stable structured failure
codes and model errors are asserted instead of matching generic lifecycle wrapper text.

### Invariants And Boundaries

- Applicability status determines the exact legal population/reason payload.
- Registry, gate-plan, certification-plan, rail-result, and manifest digests bind their content.
- Gate plans cannot duplicate rails or cross gate/profile identity; certification plans remain
  ordered, prefix-complete, candidate-coherent, and complete for certifying profiles.
- Terminal manifests reject invalid disposition/altitude, duplicate or mixed identities, and a
  gate plan not admitted by their parent certification plan.
- A conflicted exact candidate must name exactly its sorted unique conflicted paths; a durable
  finalization leg's state dictates its exact authority/output payload; a finalization journal
  keeps durable leg order and at most one unfinished write intent.
- Unplanned and independently malformed results remain typed findings.
- Contract-error evidence rejects unsafe mutable values and copies byte arrays; a busy adapter
  cannot claim uncertain first-byte state.

### Todos

Keep repository-profile and executor behavior out of this generic model-edge suite.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
is recorded as prose here (task artifact paths are not repo-relative citations): CCR-R05@v3
finalization journal and prior-red disposition semantics; the added model edges mirror them.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Applicability, content digests, execution waves, gate catalogs, and certification-plan catalogs have independent refusal cases. | `test_applicability_status_requires_its_exact_payload`; `test_registry_and_plan_digests_reject_content_drift`; `test_execution_waves_cover_fanout_and_reject_a_cycle`; `test_gate_plan_catalog_rejects_each_identity_dimension`; `test_certification_plan_catalog_rejects_each_gate_dimension` | mcp/tests/test_certification_contract_model_edges.py:99-209 |
| Rail-result and gate-manifest identity, status, digest, and catalog dimensions are forced separately. | `test_rail_result_status_rejects_illegal_blocker_payloads`; `test_not_applicable_result_cannot_publish_artifacts`; `test_gate_manifest_rejects_each_terminal_identity_dimension` | mcp/tests/test_certification_contract_model_edges.py:362-435 |
| Exact-candidate, finalization-leg, prior-red, and journal closed-model edges are forced. | `test_exact_candidate_rejects_contradictory_conflict_shapes`; `test_finalization_leg_rejects_state_shape_mismatches`; `test_red_disposition_and_journal_reject_noncanonical_shapes` | mcp/tests/test_certification_contract_model_edges.py:238-265; mcp/tests/test_certification_contract_model_edges.py:280-293; mcp/tests/test_certification_contract_model_edges.py:296-352 |
| Plan/result publication preserves typed invalid-registry, unknown-profile, unplanned-result, parent-plan, and sibling-defect failures. | `test_plan_compilation_reports_invalid_registry_and_unknown_profile`; `test_result_construction_refuses_an_unplanned_observation`; `test_manifest_refuses_a_valid_gate_plan_not_admitted_by_its_parent`; `test_manifest_catalog_reports_each_independent_result_defect` | mcp/tests/test_certification_contract_model_edges.py:438-458; mcp/tests/test_certification_contract_model_edges.py:461-471; mcp/tests/test_certification_contract_model_edges.py:473-491; mcp/tests/test_certification_contract_model_edges.py:493-535 |
| Error evidence rejects unsafe values and possible-send busy state. | `test_contract_error_freezer_rejects_unsafe_values_and_copies_bytearrays`; `test_busy_adapter_error_refuses_uncertain_send_state` | mcp/tests/test_certification_contract_model_edges.py:537-550 |

## Cross-Repo References

No external repository implementation is consumed.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite uses the portable sample registry rather than an Agents Remember rail inventory. | `certification_registry_test_support` | mcp/tests/test_certification_contract_model_edges.py:43-57 |

## Update History

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: rewrote the
  Docs References task-artifact row as prose (absolute ar-coordination paths are not
  repo-relative citations and carry no verifiable provenance).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): documented the added R05 lifecycle-model closed edges (exact candidate conflict shapes, finalization legs, prior-red dispositions, finalization journal) and refreshed all citation ranges to the current 550-line file. Verification metadata rebased from `0506b57a` to the L05 owning commit.

- 2026-09-01T11:33+02:00 — Created for CCR-L11 Attempt 10 closed-model and terminal-publication
  edge evidence. Verification remains closeout-owned until the source candidate is committed.
