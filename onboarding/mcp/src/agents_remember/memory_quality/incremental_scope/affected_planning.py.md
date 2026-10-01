# mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Compiles one exact CCR-R07 affected-closure plan — for a candidate that carries the green Gate 1-4
certificate prefix — naming every affected R06 checker/document unit, its transitive dependency
closure, the pending full-only checkers, and the affected coherence subrecords, without ever
substituting a full scan or broadening the selection.

## Code Commentary

### Logic

`AffectedClosureAdmission` (`affected_planning.py:47-54`) bundles the live `ScopeAuthority`,
the R06/R21 certification admission, the Gate 1-4 certificates, and the R21 certificate input
changes. `compile_affected_closure_plan` (`affected_planning.py:65-130`) observes the candidate
authority, validates the R06 scope (candidate digest, source-index identity, self-verifying
manifest digest, complete current checker registry with full-only dispositions,
`_validate_scope`/`_validate_scope_registry`, lines 133-183), checks every selected edge endpoint
(`_validate_scope_edges`, lines 185-193), admits the exact green Gate 1-4 prefix through R21
(`_admit_gate_certificates`, lines 196-236: prefix order, code-candidate match, reuse of exactly
those identities with `firstGateToRun == 5` and `invalidatedGates == (5,)`), compiles one
`AffectedUnitPlan` per incremental document-by-checker pair with the reverse dependency closure
(`_compile_units`/`_unit`/`_dependency_closure`, lines 239-331) excludes historical Git-tree
members from executable document units while retaining them in the member population and
dependency graph, then builds the member population
(`_compile_members`, lines 334-348), keeps pending full-only dispositions visible, unions the
affected coherence subrecords from the R21 changes, and refuses if the candidate moved during
planning (`candidate-moved-during-affected-planning`, line 124-129). All refusals are typed
`GateFiveClosureRefusedError` (`_refuse`, lines 375-385).

### Conventions

Planning admits non-certifying Gate-5 work only; every refusal is typed and names the exact
failure (missing/stale registry, edge outside the population, gate prefix incomplete, certificate
code mismatch, R21 currentness unproven, non-memory-only Gate-5 start).

### Invariants And Boundaries

- A memory-only repair requires the exact green Gate 1-4 prefix; a code/profile change cannot be
  mislabeled memory-only.
- The plan's units equal every proven incremental document/checker; full-only checkers remain
  pending.
- The candidate, roots, and trees in the plan are the live observed ones; any motion during
  planning refuses.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts
below close the informational gap for the planning boundary.

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Invalidation Boundaries"; "Exclusions And Forbidden Overreach") forbids a whole-memory
fallback disguised as incremental and any memory work before Gate 4 is green; a code/profile
change uses R21 invalidation and cannot be mislabeled memory-only. Leaf L07
(07_incremental-affected-closure-validation.md, "S2 — Implement only CCR-R07") delivered
exact affected-closure planning, selected execution, typed results, pending-full visibility,
and exact subresult reuse without fallback.


### Repo-Internal References

- Planning observes live candidate authority and validates the R06 scope against the current checker registry. [1]
- R21 admits the exact Gate 1-4 prefix and requires a memory-only Gate-5 start. [2]
- One unit per incremental document/checker is compiled with a transitive reverse dependency closure. [3]
- Affected planning remains production-owned; deleted fixture coverage does not constitute current admission evidence. [4]

| Historical Git-tree members remain in attention while `_compile_units` excludes them from execution. | `_compile_units` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:239-270 |

### Cross-Repo References

No cross-repository implementation boundary is owned here.

- Gate certificate and reuse contracts come from the R21 owners inside this repository. [5]
