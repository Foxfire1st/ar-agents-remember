# mcp/tests/test_semantic_topology_scaling.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_semantic_topology_scaling.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves semantic-topology graph binding, population reads, mutation isolation, and work accounting
remain one-time and bounded across broad, dense, shared-lump, multi-leaf, and drifted populations.

## Code Commentary

### Logic

The suite checks exact non-composed work bounds, one graph resolution before all candidate reads,
snapshot stability under later source mutation, whole-graph duplicate/cycle admission, recursive
immutability and serialization, queue refusal after mutation, mutable authoring drafts, mismatch
refusal, validation-byte accounting, incident-edge reads, and unknown-leaf drift accounting.

### Conventions

- Population builders use canonical production task and graph models.
- Scaling assertions use named exact work counters and typed refusals, never wall-clock thresholds.

### Invariants And Boundaries

- Scaling claims use exact counters and forced populations, not wall-clock timing.
- One immutable graph generation feeds all candidate projections.
- Persisted authoring objects remain mutable; only the bound runtime context is frozen.
- These are ordinary architecture regressions, not durable acceptance evidence.

### Todos

None.

## Docs References

No configured external source is needed for these repository-owned regressions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Broad/dense populations and single binding have exact bounded work. | `test_broad_and_dense_populations_have_exact_noncomposed_work_bounds`; `test_separate_graph_resolutions_are_bound_once_before_population_reads` | mcp/tests/test_semantic_topology_scaling.py:151-220 |
| Snapshot, whole-graph admission, and recursive immutability are independently forced. | `test_snapshot_then_valid_source_mutation_cannot_change_index_generation`; `test_whole_graph_admission_refuses_duplicate_edges_and_cycles_before_fingerprint`; `test_bound_graph_is_recursively_immutable_and_serialization_preserving` | mcp/tests/test_semantic_topology_scaling.py:222-348 |
| Queue mutation, authoring mutability, mismatch, byte work, incident reads, and drift are all bounded. | `test_queue_adapter_refuses_mutated_source_and_never_returns_stale_bound_bytes`; `test_all_task_doc_graph_authoring_mutations_retain_mutable_validated_drafts`; `test_one_time_graph_binding_refuses_a_mismatched_resolution`; `test_one_time_graph_validation_bytes_are_inside_the_enforced_work_budget`; `test_shared_lump_and_multi_leaf_segment_account_for_candidate_incident_reads`; `test_unknown_leaf_drift_is_counted_and_only_the_explicit_work_budget_refuses` | mcp/tests/test_semantic_topology_scaling.py:350-609 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the semantic-topology scaling card.
  Verification remains closeout-owned.
