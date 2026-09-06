# mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Executes and aggregates only the exact incremental subset admitted by CCR-R07: runs the missing
affected units, reuses byte-identical passing units supplied by exact result identity, and
publishes one complete content-addressed closure aggregate that can never promote incremental
success to final acceptance.

## Code Commentary

### Logic

`IncrementalCheckerExecutor` (`affected_execution.py:32-42`) is the protocol for one runner
bound to the exact execution registry (a `registry_version` property plus `execute(plan,
unit)`). `RangeResolutionAffectedExecutor` (`affected_execution.py:67-130`) is the sole proven
executor: it validates that the live roots equal the plan roots, that the unit names
`range_resolution.CHECK_NAME`, and that the live citation source-index snapshot equals the unit
lease. It also requires the lease to select `unit.codeTree` before any checker starts, then calls `range_resolution.check_onboarding_root` with `only=unit.document` and `Trees(candidate_tree=unit.codeTree)`.
`plan_affected_subresult_reuse` (`affected_execution.py:133-180`) selects only byte-identical
passing units by exact result identity, refuses two different prior results claiming the same
unit, and returns the reused/execute/ignored partition. `execute_affected_closure`
(`affected_execution.py:183-250`) revalidates the candidate authority before and after, verifies
the executor registry version, runs missing units and reuses valid ones, forces every evidence
payload through canonical JSON plus identity/status/finding-count shape checks (`_unit_result`,
`_require_result_identity`, `_checker_observation`, `_canonical_evidence`, lines 253-422),
derives member results (`_member_results`, lines 425-450), aggregates status (blocked > fail >
pass), and sets `incrementalMemoryReady` only when every unit passes.
`_require_current_candidate` (`affected_execution.py:488-502`) refuses a candidate that moved
after planning. Refusals are typed `GateFiveClosureRefusedError` (`_refuse`, lines 505-515).

### Conventions

Execution never guesses: a malformed or unproven checker result refuses instead of being coerced
into a pass/fail, and there is no newest-result search in subresult selection.

### Invariants And Boundaries

- Reused units must be byte-identical passing results under the same exact unit identity.
- `closeoutReady` and `acceptanceEligible` stay `False`; `fullFinalRequired` stays `True`.
- Executor registry version and live candidate are revalidated around execution.

### Todos

The R08 final full Gate-5 certification of the complete population remains mandatory before
finalization; this module only executes the affected subset.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for subresult reuse.

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Required Behavior"; "Failure And Recovery") requires retaining unchanged valid memory
subresults, resuming/reusing exact subresults on an unchanged interrupted closure, and no
newest-result search.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The sole proven executor runs the selected-document citation-range checker on one planned unit. | `RangeResolutionAffectedExecutor`; `execute` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:67-130 |
| Reuse selects only byte-identical passing units by exact result identity. | `plan_affected_subresult_reuse` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:133-180 |
| Closure execution revalidates candidate and executor, then publishes the complete aggregate. | `execute_affected_closure` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:183-250 |
| Evidence shape is canonicalized and proven before a unit result can be published. | `_unit_result`; `_canonical_evidence`; `_checker_observation` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:253-422 |
| The focused suites prove execution, reuse, and typed refusal edges. | `test_r07_unchanged_interruption_reuses_exact_passes_without_executing`; `test_r07_memory_change_reuses_only_units_with_identical_dependency_inputs`; `test_r07_range_executor_uses_one_planned_document_and_exact_live_index` | mcp/tests/test_memory_incremental_scope_compiler.py:1004-1025; mcp/tests/test_memory_incremental_scope_compiler.py:1026-1076; mcp/tests/test_memory_incremental_scope_model_edges.py:431-471 |
| The actual range checker composes with the real Git candidate census; a wrong tree refuses before checker execution. | `test_r07_real_range_checker_uses_only_the_candidate_source_population`; `test_r07_range_executor_refuses_another_candidate_before_checker_start` | mcp/tests/test_memory_incremental_scope_model_edges.py:512-568; mcp/tests/test_memory_incremental_scope_model_edges.py:571-594 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The executor delegates to the same-repository citation range-resolution checker. | `range_resolution` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:44-64 |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Bound the selected-document executor to the exact Git candidate lease and recorded real checker composition and pre-execution refusal coverage; verified against 97e8ed2e1fae21756c3ad995c30613d4fbfcc503.

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References row as prose.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card for the new affected-closure executor and subresult reuse engine; no prior sidecar existed.
