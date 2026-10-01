# mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py

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
after planning. When a checker raises before publishing evidence, the executor now preserves
the selected document, exception type, and exception detail in the typed
`checker-execution-failed` refusal (`affected_execution.py:212-219`) instead of reducing the
diagnostic to the exception type alone. Refusals are typed `GateFiveClosureRefusedError`
(`_refuse`, lines 505-515).

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for subresult reuse.

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Required Behavior"; "Failure And Recovery") requires retaining unchanged valid memory
subresults, resuming/reusing exact subresults on an unchanged interrupted closure, and no
newest-result search.


### Repo-Internal References

- The sole proven executor runs the selected-document citation-range checker on one planned unit. [1]
- Reuse selects only byte-identical passing units by exact result identity. [2]
- Closure execution revalidates candidate and executor, then publishes the complete aggregate. [3]
- Evidence shape is canonicalized and proven before a unit result can be published. [4]
- The executor refuses mismatched roots, checker, source-index snapshot or Git candidate tree before checker execution. [5]
- The executor refuses mismatched roots, checker, source-index snapshot or Git candidate tree before checker execution. [6]

| An unexpected checker exception is refused with its selected document and exception detail. | "checker-execution-failed" | mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:212-219 |

### Cross-Repo References

No cross-repository implementation boundary is owned here.

- The executor delegates to the same-repository citation range-resolution checker. [7]
