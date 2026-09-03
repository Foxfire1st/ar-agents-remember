# mcp/tests/test_memory_incremental_scope_compiler.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_incremental_scope_compiler.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `993953760ef65c4670a40c63a6d6ef0fbcddbe3b`|
| lastVerifiedCommitDate | 2026-09-03T02:13:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Proves the content-addressed incremental scope compilation surfaces: the R06 scope
compiler/owners fail-closed edges (dependency completeness, digest stability, checker-population
completeness, source-index and R01/R02 authority, canonical paths, manifest self-verification) and,
since CCR-R07@v3, the affected-closure planning, execution, subresult reuse, and aggregate edges
that keep the closure exact and never promote incremental success.

## Code Commentary

### Logic

The R06 layer (lines 231-610) directly exercises the observer and compiler helpers: direct,
transitive, and reverse-only dependency closure completeness; stable manifest digests across
repeated observation; every current checker having one executable or full-only policy; full-only
checkers staying pending; empty or unknown checker populations, missing edge classes, stale source
indexes, and missing or ambiguous R01/R02 authority all being `scope-unproven`; and added-root /
missing-endpoint / terminated-reverse-closure shapes.

The R07 layer (lines 869-1187) proves the affected closure end to end: the plan executes only
incremental documents and keeps the six full-only checks pending (line 869); the aggregate never
promotes incremental success (line 896); a hard finding stays failed and a malformed result
refuses (line 920); a blocked unit preserves its code and blocks the aggregate (line 964); an
unchanged interruption reuses exact passes without executing (line 1004); a memory change reuses
only units with identical dependency inputs (line 1026); incomplete scope, code repair, and
candidate motion refuse with typed closures (line 1077); the executor registry and post-plan
candidate are revalidated (line 1108); conflicting prior-result authority is never guessed (line
1133); and the plan/aggregate models refuse rebound identity (line 1158).

### Conventions

Every refusal is asserted as a typed `ScopeUnprovenError`/`GateFiveClosureRefusedError` or a
model `ValueError`, never as generic text matching.

### Invariants And Boundaries

- Incremental proof cannot set `closeoutReady`/acceptance; the suite asserts the hard
  `False`/pending-final-full shapes.
- Reuse is exact-result-identity only; a unit cannot be both reused and executed.
- The focused suites assert the same registry and scope authorities the planner uses.

### Todos

R08 final full certification remains out of scope for this suite.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts
close the informational gap for the enforced behaviors: the CCR-R07@v3 requirement packet
(Required Behavior, Exclusions And Forbidden Overreach) fixes the affected-closure contract
to execute only the closure, retain unchanged subresults, allow no implicit full-scan fallback,
and never let incremental proof replace full certification. The closing L07 leaf task step
(S2 - Implement only CCR-R07) recorded the final selected Python suite passing 120 tests with
focused affected coverage.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| R06 scope compile/owner edges: closure completeness, registry completeness, full-only visibility, R01/R02 authority, and canonical roots. | `test_direct_transitive_and_reverse_only_dependencies_are_complete`; `test_every_current_checker_has_one_executable_or_full_only_policy`; `test_missing_or_ambiguous_r01_r02_authority_is_scope_unproven` | mcp/tests/test_memory_incremental_scope_compiler.py:231-251; mcp/tests/test_memory_incremental_scope_compiler.py:267-274; mcp/tests/test_memory_incremental_scope_compiler.py:377-390 |
| The R07 plan executes only incremental documents and keeps full-only checks pending. | `test_r07_plan_executes_only_incremental_documents_and_keeps_six_final_checks_pending`; `test_r07_execution_publishes_every_member_and_never_promotes_incremental_success` | mcp/tests/test_memory_incremental_scope_compiler.py:869-895; mcp/tests/test_memory_incremental_scope_compiler.py:896-919 |
| Interruption and memory-change reuse are exact-identity scoped. | `test_r07_unchanged_interruption_reuses_exact_passes_without_executing`; `test_r07_memory_change_reuses_only_units_with_identical_dependency_inputs` | mcp/tests/test_memory_incremental_scope_compiler.py:1004-1025; mcp/tests/test_memory_incremental_scope_compiler.py:1026-1076 |
| Typed refusals cover incomplete scope, code repair, motion, registry, and conflicting authority. | `test_r07_incomplete_scope_code_repair_and_candidate_motion_refuse_typed`; `test_r07_executor_registry_and_post_plan_candidate_are_revalidated`; `test_r07_conflicting_prior_result_authority_is_not_guessed` | mcp/tests/test_memory_incremental_scope_compiler.py:1077-1107; mcp/tests/test_memory_incremental_scope_compiler.py:1108-1132; mcp/tests/test_memory_incremental_scope_compiler.py:1133-1157 |
| The suite consumes the real scope planner, executor, registry, and store owners. | `compile_affected_closure_plan`; `execute_affected_closure`; `ContentAddressedSubresultStore` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:65-130; mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:171-238; mcp/src/agents_remember/memory_quality/incremental_scope/subresult_store.py:31-119 |

## Cross-Repo References

No cross-repository implementation boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite drives only repository-owned owners. | — | — |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card covering the R06 scope-compile edges and the R07 affected-closure plan/execute/reuse/aggregate edges added by this commit; no prior sidecar existed.
