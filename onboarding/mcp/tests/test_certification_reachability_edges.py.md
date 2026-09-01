# mcp/tests/test_certification_reachability_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_certification_reachability_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T11:33+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves prospective pre-allocation refusal, raw-declaration refusal, exact artifact-query
composition, incomplete measurement, and bounded cycle-safe reachability behavior.

## Code Commentary

### Logic

The suite measures accepted and hostile generated registries, forces raw admission one unit over
the shared budget, exercises singleton-to-shared query promotion, replaces each search owner with
an explicit incomplete result, and calls both graph searches with reservations that fail at every
storage and operation boundary.

### Conventions

Direct calls to underscored search seams are narrow forcing evidence for the generic bounded-work
owner. Portable graph builders remain centralized in `certification_registry_test_support.py`.

### Invariants And Boundaries

- Prospective storage is refused before digest/query allocation and reports zero traversal work.
- Valid admitted measurements retain exact dependency answers; unmeasured pairs and refused
  registries cannot answer reachability queries.
- Raw declarations over budget stop before cross-reference and graph work.
- Repeating one artifact query is idempotent; a second consumer promotes it once to shared state.
- Incomplete search remains an explicit incomplete measurement rather than a partial answer.
- Both search directions reserve storage and operation units, terminate across cycles, and retain
  unreachable targets.

### Todos

Keep budget forcing deterministic and independent of wall-clock timing.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Prospective and raw-declaration refusals occur before expensive reachability work while admitted answers remain queryable. | `test_prospective_budget_is_the_preallocation_refusal_and_valid_answers_survive`; `test_raw_declaration_overflow_refuses_before_cross_reference_or_graph_work` | mcp/tests/test_certification_reachability_edges.py:29-60 |
| Artifact queries are idempotent before shared promotion, and both resolver owners publish incomplete measurements explicitly. | `test_identical_artifact_query_is_idempotent_before_shared_promotion`; `test_singleton_resolver_publishes_incomplete_measurement`; `test_shared_resolver_publishes_incomplete_measurement` | mcp/tests/test_certification_reachability_edges.py:63-109 |
| Prerequisite and dependant traversal cover reservation refusal, cycles, self-targets, exhaustion, and unreachable targets. | `test_prerequisite_search_refuses_each_budget_boundary`; `test_dependant_search_is_cycle_safe_and_retains_unreachable_targets` | mcp/tests/test_certification_reachability_edges.py:112-208 |

## Cross-Repo References

No external repository implementation is consumed.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every graph fixture is repository-neutral and generated in process. | `certification_registry_test_support` | mcp/tests/test_certification_reachability_edges.py:13-18 |

## Update History

- 2026-09-01T11:33+02:00 — Created for CCR-L11 Attempt 10 bounded reachability and refusal-edge
  evidence. Verification remains closeout-owned until the source candidate is committed.
