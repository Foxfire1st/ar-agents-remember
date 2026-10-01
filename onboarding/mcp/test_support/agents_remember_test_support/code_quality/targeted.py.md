# mcp/test_support/agents_remember_test_support/code_quality/targeted.py

## Governing Overview

[Quality verification overview](overview.md)

## Purpose

Derives every leaf-edge Python rail from one candidate diff and the canonical test-consumer graph.
It is a thin projection owner: dependency meaning belongs to `dependency_ownership.py` rather than
being reimplemented here.

## Code Commentary

### Logic

`changed_paths` reads the complete ACMRD diff against the caller's explicit base. The current
Python subset drives Ruff, formatting, file-size, and product-only coverage/CRAP. `derive_targeted_scope` passes the same explicit base revision into graph resolution, so historical catalog changes participate in impact selection. A single
`DependencyOwnershipGraph` supplies module identity, reverse-import type closure, affected tests,
selection reasons, completeness, explicit global invalidators and unresolved input decisions. `TargetedScopeResult` retains all of this
evidence for scope reporting and conversion to `GateScope`.

Product measurement authority is resolved separately from that consumer graph through the
repository's exhaustive `product_package_roots` / `verification_package_roots` declaration. Only
changed Python below a declared product root enters `coverage_paths`, and only product package
roots become `--cov` module arguments. Verification packages remain in the changed-path, lint,
type, size, dependency-selection, and structural evidence planes without recursively becoming
behavioral product scope.

### Conventions

The targeted route narrows only from repository truth. Callers cannot pass a hand-written test list
or claim their own dependency completeness.

### Invariants And Boundaries

- Deleted paths participate in test impact even though absent files cannot be linted or typed.
- Coverage/CRAP paths contain changed product modules only; tests and shared support still execute,
  lint, type-check, and influence selection without becoming scored product code.
- Importability never implies product ownership. Missing, overlapping, or stale package authority
  refuses through the shared configured-authority reader instead of falling back to directory
  placement.
- An incomplete or ambiguous graph retains unresolved inputs with `complete=False`. Explicit
  global invalidators select the full population; proven dependency fan-out can also reach every test.
- Large import fan-out is a truthful ownership result, not a reason to silently cap selection.

### Todos

None.

## Evidence

### Docs References

No external domain documentation governs this repository-local scope contract.

### Repo-Internal References

- The result carries exact rail scope plus typed ownership evidence. [1]
- The diff includes deletions and refuses Git failures. [2]
- One graph derives closure and affected tests while explicit package authority derives product measurement scope. [3]
- Consumer semantics, explicit global invalidation and unresolved-input decisions live at the canonical owner without deciding product ownership. [4]

### Cross-Repo References

No cross-repository graph participates in targeted selection.
