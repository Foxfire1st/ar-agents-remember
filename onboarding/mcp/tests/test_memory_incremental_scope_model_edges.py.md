# mcp/tests/test_memory_incremental_scope_model_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_incremental_scope_model_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `993953760ef65c4670a40c63a6d6ef0fbcddbe3b`|
| lastVerifiedCommitDate | 2026-09-03T02:13:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Forces the closed-model edges of the incremental memory dependency scope vocabulary: exact
`GitPathChange`/`GitTreeDelta` shapes, canonical task and roots, node/edge identities with
reason evidence, the checker-scope registry contract, and the typed error payload — plus, since
CCR-R07@v3, the full affected-closure model, planning, executor, registry, and subresult-store
refusal edges.

## Code Commentary

### Logic

The R06 model layer (lines 131-314) proves git change shapes reject noncanonical paths and
invalid statuses, tree deltas reject bad roots/order/duplicates, task and index roots must be exact
absolute paths, candidate identity requires exact namespaces/roots/tree changes, node identity and
reason evidence fail closed, scope errors preserve all optional authority evidence, and the
checker registry rejects population and policy contract drift.

The R07 layer (lines 372-1082) proves the affected-closure contracts: the subresult store is
exact, atomic, bounded, and has no latest lookup (line 372); `load` refuses corrupt or
wrongly-addressed bytes (line 405); the range executor uses one planned document and the exact live
index (line 418) and refuses wrong roots or source generations (line 461); invalid plans and
checker exceptions refuse typed (line 499); checker status requires the exact selected-document
count (line 525); evidence refuses every unproven or non-canonical shape (line 590); unit/member
plans refuse non-canonical authority (line 621); the closure plan refuses incomplete or rebound
populations (line 660) and its units retain every exact input identity (line 731); result/reuse
and aggregate models refuse inconsistent exact state (lines 741, 786); planning refuses stale
scope/registry/edges/gate prefix (line 844) and requires complete canonical closure targets (line
952); the execution registry refuses an incomplete population (line 996); and the store refuses
collisions, readback mismatches, wrong addresses (line 1004), and non-regular or unreadable
objects (line 1042).

### Conventions

Every assertion is a strict model `ValueError` or a typed closure refusal; the suite never
re-implements the owners it proves.

### Invariants And Boundaries

- Digests, roots, node ids, and edge reasons are canonical and unique; any drift refuses.
- The affected plan/result populations must exactly match each other and the R06 selection.
- The executor may consume only the planned document with the exact rented source-index
  generation.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts
close the informational gap for the model edges: the CCR-R07@v3 requirement packet (Required
Behavior, Failure And Recovery) requires incomplete closures, stale input, and a missing result
to refuse typed, while an unchanged interruption resumes exact subresults. The closing L07 leaf
task step (S2 - Implement only CCR-R07) added focused verification for required success,
refusal, recovery, concurrency, and forbidden-overreach cases.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| R06 model shapes: git changes, deltas, candidate identity, nodes/edges, source index, error payload, and registry contract. | `test_git_change_accepts_every_exact_shape_and_canonical_none`; `test_candidate_requires_exact_namespaces_roots_and_tree_changes`; `test_registry_rejects_population_and_policy_contract_drift` | mcp/tests/test_memory_incremental_scope_model_edges.py:131-143; mcp/tests/test_memory_incremental_scope_model_edges.py:219-250; mcp/tests/test_memory_incremental_scope_model_edges.py:314-371 |
| R07 store, executor, and registry model edges. | `test_r07_subresult_store_is_exact_atomic_bounded_and_has_no_latest_lookup`; `test_r07_range_executor_uses_one_planned_document_and_exact_live_index`; `test_r07_execution_registry_refuses_incomplete_population` | mcp/tests/test_memory_incremental_scope_model_edges.py:372-404; mcp/tests/test_memory_incremental_scope_model_edges.py:418-460; mcp/tests/test_memory_incremental_scope_model_edges.py:996-1003 |
| R07 plan/result aggregation and reuse consistency edges. | `test_r07_closure_plan_model_refuses_incomplete_or_rebound_populations`; `test_r07_aggregate_model_refuses_incomplete_or_inconsistent_result`; `test_r07_result_and_reuse_models_refuse_inconsistent_exact_state` | mcp/tests/test_memory_incremental_scope_model_edges.py:660-730; mcp/tests/test_memory_incremental_scope_model_edges.py:786-843; mcp/tests/test_memory_incremental_scope_model_edges.py:741-785 |
| R07 planning and subresult store safety edges. | `test_r07_planning_refuses_stale_scope_registry_edges_and_gate_prefix`; `test_r07_subresult_store_refuses_nonregular_or_unreadable_objects` | mcp/tests/test_memory_incremental_scope_model_edges.py:844-951; mcp/tests/test_memory_incremental_scope_model_edges.py:1042-1056 |

## Cross-Repo References

No cross-repository implementation boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite proves repository-owned contract shapes only. | — | — |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card covering the R06 model shapes and the R07 affected-closure plan/executor/store model edges added by this commit; no prior sidecar existed.
