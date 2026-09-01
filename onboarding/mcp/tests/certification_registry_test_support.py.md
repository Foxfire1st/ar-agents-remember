# mcp/tests/certification_registry_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/certification_registry_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T11:33+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns the permanent repository-neutral composition vocabulary shared by the five focused
certification contract suites. It supplies generic portable profiles, rail/result builders, plan
rebuilders, and bounded graph families without declaring an Agents Remember production profile.

## Code Commentary

### Logic

`RailSpec` and `ObservationSpec` describe compact test intent. Builders produce valid five-gate
registries, candidate-bound plans, results, and manifests, while specialized graph factories
generate linear, dense, shared-artifact, distinct-artifact, self-query, raw-declaration-overflow,
and exact-budget cases.

### Conventions

Underscored helpers are test-composition seams, not production API. The permanent artifact has
exactly five declared consumers: the registry-contract and plan-authority suites plus the focused
model, reachability, and registry-validation edge suites.

### Invariants And Boundaries

- Fixtures use a sample repository and portable owners; they do not encode Agents Remember rails.
- Valid defaults model all five gates, with Gate 5 memory-domain authority and Gates 1–4
  repository-profile authority.
- Graph and padding builders make scaling and exact-cap assertions reproducible.
- Shared support contains no executable test collection and no fallback registry.

### Todos

Keep new consumers explicit in `mcp/tests/evidence-lifecycle.toml`.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Portable gate classes and authorities are centralized in the generic rail builder. | `_CLASS_BY_GATE`; `_rail` | mcp/tests/certification_registry_test_support.py:44-126 |
| Registry, plan, result, and manifest helpers compose the valid baseline consumed by all five suites. | `_registry`; `_plan`; `_result`; `_manifest` | mcp/tests/certification_registry_test_support.py:145-230 |
| Graph families construct reproducible dependency, raw-overflow, and artifact scaling boundaries. | `_gate_one_graph_registry`; `_artifact_chain_registry`; `_raw_declaration_overflow_registry`; `_artifact_query_cross_product_registry` | mcp/tests/certification_registry_test_support.py:251-446 |
| The plan-authority suite directly imports the permanent support owner. | "from certification_registry_test_support import (" | mcp/tests/test_certification_plan_authority.py:31-52 |
| The registry-contract suite directly imports the permanent support owner. | "from certification_registry_test_support import (" | mcp/tests/test_certification_rail_registry.py:35-52 |
| The contract-model edge suite uses the shared manifest and plan rebuilders for hostile identity cases. | `test_gate_manifest_rejects_each_terminal_identity_dimension`; `test_certification_plan_rejects_a_gate_bound_to_another_candidate` | mcp/tests/test_certification_contract_model_edges.py:191-207; mcp/tests/test_certification_contract_model_edges.py:262-290 |
| The reachability edge suite uses the shared generated graph families for prospective and raw-budget refusal. | `test_prospective_budget_is_the_preallocation_refusal_and_valid_answers_survive`; `test_raw_declaration_overflow_refuses_before_cross_reference_or_graph_work` | mcp/tests/test_certification_reachability_edges.py:29-60 |
| The registry-validation edge suite uses the shared raw-overflow and portable registry builders for typed semantic findings. | `test_validation_budget_refusal_publishes_one_typed_finding`; `test_profiles_report_duplicate_gates_and_every_empty_gate` | mcp/tests/test_certification_registry_validation_edges.py:28-56 |

## Cross-Repo References

No cross-repository implementation is consumed.

| Finding | Anchor | Source |
| --- | --- | --- |
| The support vocabulary intentionally names `sample-repository` and `portable-ci`. | `_registry` | mcp/tests/certification_registry_test_support.py:145-161 |

## Update History

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 extended the permanent support owner to five exact
  consumers and added the raw-declaration-overflow builder used by the two bounded-admission edge
  suites. Verification remains closeout-owned.

- 2026-09-01T03:11+02:00 — Created for the permanent two-consumer certification test-composition
  contract. Verification remains closeout-owned until the source candidate is committed.
