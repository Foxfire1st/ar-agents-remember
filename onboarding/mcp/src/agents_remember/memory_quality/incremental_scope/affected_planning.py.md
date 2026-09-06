# mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `993953760ef65c4670a40c63a6d6ef0fbcddbe3b`|
| lastVerifiedCommitDate | 2026-09-03T02:13:10+02:00|
| governingOverview | `../overview.md` |

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
(`_compile_units`/`_unit`/`_dependency_closure`, lines 239-331), builds the member population
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

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts
below close the informational gap for the planning boundary.

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Invalidation Boundaries"; "Exclusions And Forbidden Overreach") forbids a whole-memory
fallback disguised as incremental and any memory work before Gate 4 is green; a code/profile
change uses R21 invalidation and cannot be mislabeled memory-only. Leaf L07
(07_incremental-affected-closure-validation.md, "S2 — Implement only CCR-R07") delivered
exact affected-closure planning, selected execution, typed results, pending-full visibility,
and exact subresult reuse without fallback.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Planning observes live candidate authority and validates the R06 scope against the current checker registry. | `compile_affected_closure_plan`; `_validate_scope`; `_validate_scope_registry` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:65-130; mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:133-183 |
| R21 admits the exact Gate 1-4 prefix and requires a memory-only Gate-5 start. | `_admit_gate_certificates` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:196-236 |
| One unit per incremental document/checker is compiled with a transitive reverse dependency closure. | `_compile_units`; `_unit`; `_dependency_closure` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:239-331 |
| Planning-edge refusals are proven by the focused suites. | `test_r07_planning_refuses_stale_scope_registry_edges_and_gate_prefix`; `test_r07_planning_closure_targets_are_complete_and_canonical` | mcp/tests/test_memory_incremental_scope_model_edges.py:942-1047; mcp/tests/test_memory_incremental_scope_model_edges.py:1050-1091 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate certificate and reuse contracts come from the R21 owners inside this repository. | `GateCertificate`; `plan_certificate_reuse` | mcp/src/agents_remember/certification/certificate_models.py:221-240; mcp/src/agents_remember/certification/certificate_invalidation.py:124-164 |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Corrected incoming references and schema ownership against the reviewed candidate; unchanged source retains its genuine verification stamp.

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References rows as prose.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card for the new affected-closure planner; no prior sidecar existed.
