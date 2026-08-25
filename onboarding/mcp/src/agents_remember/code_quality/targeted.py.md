# mcp/src/agents_remember/code_quality/targeted.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/targeted.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../../../overview.md` |

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
selection reasons, completeness, and safe-full fallback. `TargetedScopeResult` retains all of this
evidence for scope reporting and conversion to `GateScope`.

### Conventions

The targeted route narrows only from repository truth. Callers cannot pass a hand-written test list
or claim their own dependency completeness.

### Invariants And Boundaries

- Deleted paths participate in test impact even though absent files cannot be linted or typed.
- Coverage/CRAP paths contain changed product modules only; tests and shared support still execute,
  lint, type-check, and influence selection without becoming scored product code.
- An incomplete or ambiguous graph selects the safe full Python test population with a printed
  reason; it never guesses a narrow subset.
- Large import fan-out is a truthful ownership result, not a reason to silently cap selection.

### Todos

None.

## Docs References

No external domain documentation governs this repository-local scope contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The result carries exact rail scope plus typed ownership evidence. | `TargetedScopeResult` | mcp/src/agents_remember/code_quality/targeted.py:19-42 |
| The diff includes deletions and refuses Git failures. | `changed_paths` | mcp/src/agents_remember/code_quality/targeted.py:54-73 |
| One graph derives closure, product coverage, and affected tests. | `derive_targeted_scope` | mcp/src/agents_remember/code_quality/targeted.py:86-125 |
| Consumer semantics and fail-closed fallback live at the canonical owner. | `DependencyOwnershipGraph` | mcp/src/agents_remember/code_quality/dependency_ownership.py:190-411 |

## Cross-Repo References

No cross-repository graph participates in targeted selection.

## Update History

- 2026-08-25T01:56+02:00 — Replaced duplicated selector logic with the canonical dependency-owned
  graph and separated product coverage from executable test/support scope.
- 2026-08-12T15:19+02:00 — L23 curator retained the prior source-backed targeted contract.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 created deterministic change-set scoping.
