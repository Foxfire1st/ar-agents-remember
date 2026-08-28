# mcp/test_support/agents_remember_test_support/code_quality/targeted.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/targeted.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Derives every leaf-edge Python rail from one candidate diff and the canonical test-consumer graph.
It is a thin projection owner: dependency meaning belongs to `dependency_ownership.py` rather than
being reimplemented here.

## Code Commentary

### Logic

`changed_paths` reads the complete ACMRD diff against the caller's explicit base. The current
Python subset drives Ruff, formatting, file-size, and product-only coverage/CRAP. A single
`DependencyOwnershipGraph` supplies module identity, reverse-import type closure, affected tests,
selection reasons, completeness, and an explicit conservative-full decision. `TargetedScopeResult` retains all of this
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
- An incomplete or ambiguous graph selects the full Python test population with a printed
  reason; it never guesses a narrow subset.
- Large import fan-out is a truthful ownership result, not a reason to silently cap selection.

### Todos

None.

## Docs References

No external domain documentation governs this repository-local scope contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The result carries exact rail scope plus typed ownership evidence. | `TargetedScopeResult` | mcp/test_support/agents_remember_test_support/code_quality/targeted.py:19-42 |
| The diff includes deletions and refuses Git failures. | "def changed_paths(" | mcp/test_support/agents_remember_test_support/code_quality/targeted.py:60-91 |
| One graph derives closure and affected tests while explicit package authority derives product measurement scope. | `derive_targeted_scope` | mcp/test_support/agents_remember_test_support/code_quality/targeted.py:103-147 |
| Consumer semantics and the fail-closed full-population decision live at the canonical owner without deciding product ownership. | `DependencyOwnershipGraph` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:81-301 |

## Cross-Repo References

No cross-repository graph participates in targeted selection.

## Update History

- 2026-08-27T14:04+02:00 — Corrected targeted product measurement to consume the same explicit
  package-authority declaration as full mode; verification packages remain statically checked but
  cannot become Coverage.py, CRAP, or changed-lines product scope merely by being importable.
- 2026-08-25T01:56+02:00 — Replaced duplicated selector logic with the canonical dependency-owned
  graph and separated product coverage from executable test/support scope.
- 2026-08-12T15:19+02:00 — L23 curator retained the prior source-backed targeted contract.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 created deterministic change-set scoping.
