# mcp/src/agents_remember/code_quality/dependency_ownership.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/dependency_ownership.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Builds the single immutable test-consumer graph used by targeted selection, retry proof, and
causal preflight.

## Code Commentary

### Logic

The graph indexes tracked Python module identities/importers and lifecycle-catalog consumers.
`resolve` assigns every changed path a complete set of selected tests and typed reasons: changed
test, import consumer, declared consumer, name/text heuristic, global pytest input, or explicit
safe-full refusal. Reverse import and coverage-root helpers are shared with targeted static scope.

### Conventions

Every selected test retains all reasons; a heuristic can explain an already-owned test without
being mistaken for the cause of the whole population.

### Invariants And Boundaries

- `conftest.py` and root pytest configuration are global.
- Governed fixtures/support use catalog consumers; support also uses real imports.
- Unowned executable/support input, parse/catalog error, ambiguous module identity, and deleted
  tests fail closed to the safe population with a stable reason.
- Broad real import fan-out is preserved; the graph is not optimized to produce a small number.

### Todos

None.

## Docs References

No external documentation owns the repository selection graph.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Typed reason and impact shapes preserve completeness and fallback cause. | `TestImpact` | mcp/src/agents_remember/code_quality/dependency_ownership.py:59-70 |
| One graph resolves tests, support, fixtures, global input, and safe-full refusal. | `DependencyOwnershipGraph` | mcp/src/agents_remember/code_quality/dependency_ownership.py:190-411 |
| Targeted scope consumes the same graph. | `derive_targeted_scope` | mcp/src/agents_remember/code_quality/targeted.py:86-125 |

## Cross-Repo References

No cross-repository ownership graph participates.

## Update History

- 2026-08-25T01:56+02:00 — Created as the sole selection/retry/causal consumer authority.
