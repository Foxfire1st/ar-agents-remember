# mcp/tests/test_memory_incremental_scope_model_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_incremental_scope_model_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:21:02+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Protects the R06 scope vocabulary and R07 affected-closure models, planning, execution and subresult storage. Alongside model and refusal cases, the suite composes actual Git candidate observation, a leased citation index, R06 dependency compilation and the production range checker for one affected document.

## Code Commentary

### Logic

The R06 cases exercise canonical Git changes and tree deltas, exact task/index roots and candidate namespaces, node and edge reason evidence, optional typed-error authority fields, and checker-registry population/policy drift. The R07 model cases retain exact input identities and complete plan, result, reuse and aggregate populations.

Subresult-store tests exercise exact digest lookup, concurrent identical publication, bounded object capacity and atomic readback; malformed, wrongly addressed, colliding, nonregular or unreadable objects refuse. Planning tests reject stale scope, registry, edges and gate prefixes, and require a complete canonical set of closure targets. Checker failures and contradictory selected-document counts retain typed refusals.

The range-executor forwarding fixture asserts one planned document, the already leased index and `Trees` carrying `unit.codeTree`; it does not request another frozen snapshot. Wrong roots or source generations refuse. A separate wrong-policy/wrong-tree fixture preserves the snapshot identity but asserts `checker-source-index-candidate-mismatch` before the checker is called.

`test_r07_real_range_checker_uses_only_the_candidate_source_population` creates actual code/memory Git candidates in a linked checkout. It composes `observe_git_nodes`, `observe_source_index`, citation-edge extraction, dependency snapshot construction, scope compilation, affected planning and `RangeResolutionAffectedExecutor` with the actual range checker. A valid source range succeeds; a wrong source range reports `citation_anchor_absent_from_range`; a citation to ignored generated output reports `citation_source_vanished`. The wrong-range diagnostic must name the tracked source and omit the generated file's competing symbol.

### Conventions

Model/refusal fixtures inject authority or fault seams where needed; store operations and the checker composition use their production owners. The actual checker case still obtains admission/gate-prefix facts from `_r07_admission` and task facts from a fixture. It therefore proves library composition and candidate-bounded range checking, not production admission, full Gate-5 execution or lifecycle acceptance.

### Invariants And Boundaries

- Digests, roots, node identities and edge reasons must satisfy the exercised canonical contracts; affected plan/result populations must agree with their R06 selection.
- The range executor receives only the planned document and exact leased source snapshot and candidate tree.
- Matching indexed bytes or snapshot identity alone cannot authorize a different candidate policy/tree.
- Actual checker success in the fixture supplies no final/full certification or acceptance authority.

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

These source anchors distinguish model/refusal coverage, store behavior, forwarding assertions and actual Git/index/checker composition.

| Finding | Anchor | Source |
| --- | --- | --- |
| R06 Git/candidate shapes and registry policy are constrained. | `test_git_change_accepts_every_exact_shape_and_canonical_none`; `test_candidate_requires_exact_namespaces_roots_and_tree_changes`; `test_registry_rejects_population_and_policy_contract_drift` | mcp/tests/test_memory_incremental_scope_model_edges.py:144-153; mcp/tests/test_memory_incremental_scope_model_edges.py:232-260; mcp/tests/test_memory_incremental_scope_model_edges.py:327-357 |
| Store publication is exact and bounded; range execution forwards the selected document, candidate Trees and live index. | `test_r07_subresult_store_is_exact_atomic_bounded_and_has_no_latest_lookup`; `test_r07_range_executor_uses_one_planned_document_and_exact_live_index` | mcp/tests/test_memory_incremental_scope_model_edges.py:385-415; mcp/tests/test_memory_incremental_scope_model_edges.py:431-471 |
| Actual Git/index/R06/R07 composition constrains checker diagnostics to the candidate population. | `test_r07_real_range_checker_uses_only_the_candidate_source_population` | mcp/tests/test_memory_incremental_scope_model_edges.py:520-568 |
| A wrong candidate policy/tree refuses before checker start. | `test_r07_range_executor_refuses_another_candidate_before_checker_start` | mcp/tests/test_memory_incremental_scope_model_edges.py:572-594 |
| Plan, reuse and aggregate populations must retain exact state. | `test_r07_closure_plan_model_refuses_incomplete_or_rebound_populations`; `test_r07_result_and_reuse_models_refuse_inconsistent_exact_state`; `test_r07_aggregate_model_refuses_incomplete_or_inconsistent_result` | mcp/tests/test_memory_incremental_scope_model_edges.py:758-817; mcp/tests/test_memory_incremental_scope_model_edges.py:839-881; mcp/tests/test_memory_incremental_scope_model_edges.py:884-933 |
| Stale planning authority and incomplete registry populations refuse. | `test_r07_planning_refuses_stale_scope_registry_edges_and_gate_prefix`; `test_r07_execution_registry_refuses_incomplete_population` | mcp/tests/test_memory_incremental_scope_model_edges.py:942-1047; mcp/tests/test_memory_incremental_scope_model_edges.py:1094-1099 |
| Nonregular or unreadable stored objects refuse exact lookup. | `test_r07_subresult_store_refuses_nonregular_or_unreadable_objects` | mcp/tests/test_memory_incremental_scope_model_edges.py:1140-1154 |

## Cross-Repo References

No cross-repository implementation boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| The exercised Git, index, checker, model and store owners belong to this repository. | — | — |

## Update History

- 2026-09-06T00:21:02+00:00 — CCR L30 candidate-index recovery: documented actual R06/R07 range-checker composition, exact candidate forwarding/refusal and retained admission-fixture limits; reconciled shifted model/store citations.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card covering the R06 model shapes and the R07 affected-closure plan/executor/store model edges added by this commit; no prior sidecar existed.
