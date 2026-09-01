# mcp/tests/test_certification_contract_model_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_certification_contract_model_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T11:33+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves closed-model, digest, plan-catalog, terminal-publication, and typed-error edges that keep the
generic five-gate certification contract exact under adversarial payloads.

## Code Commentary

### Logic

The suite varies applicability payloads, registry/plan/result/manifest digests, execution-wave
graphs, gate and certification plan catalogs, blocker/evidence/artifact identity, terminal
admission, immutable error payloads, and busy-adapter send certainty. Every case consumes the
portable shared registry builders and asserts a stable model or contract refusal.

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
- Unplanned and independently malformed results remain typed findings.
- Contract-error evidence rejects unsafe mutable values and copies byte arrays; a busy adapter
  cannot claim uncertain first-byte state.

### Todos

Keep repository-profile and executor behavior out of this generic model-edge suite.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Applicability, content digests, execution waves, gate catalogs, and certification-plan catalogs have independent refusal cases. | `test_applicability_status_requires_its_exact_payload`; `test_registry_and_plan_digests_reject_content_drift`; `test_execution_waves_cover_fanout_and_reject_a_cycle`; `test_gate_plan_catalog_rejects_each_identity_dimension`; `test_certification_plan_catalog_rejects_each_gate_dimension` | mcp/tests/test_certification_contract_model_edges.py:69-188 |
| Rail-result and gate-manifest identity, status, digest, and catalog dimensions are forced separately. | `test_rail_result_status_rejects_illegal_blocker_payloads`; `test_gate_manifest_rejects_each_terminal_identity_dimension` | mcp/tests/test_certification_contract_model_edges.py:210-290 |
| Plan/result publication preserves typed invalid-registry, unknown-profile, unplanned-result, parent-plan, and sibling-defect failures. | `test_plan_compilation_reports_invalid_registry_and_unknown_profile`; `test_manifest_catalog_reports_each_independent_result_defect` | mcp/tests/test_certification_contract_model_edges.py:293-389 |
| Error evidence rejects unsafe values and possible-send busy state. | `test_contract_error_freezer_rejects_unsafe_values_and_copies_bytearrays`; `test_busy_adapter_error_refuses_uncertain_send_state` | mcp/tests/test_certification_contract_model_edges.py:392-405 |

## Cross-Repo References

No external repository implementation is consumed.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite uses the portable sample registry rather than an Agents Remember rail inventory. | `certification_registry_test_support` | mcp/tests/test_certification_contract_model_edges.py:33-47 |

## Update History

- 2026-09-01T11:33+02:00 — Created for CCR-L11 Attempt 10 closed-model and terminal-publication
  edge evidence. Verification remains closeout-owned until the source candidate is committed.
