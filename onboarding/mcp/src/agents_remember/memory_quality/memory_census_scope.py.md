# mcp/src/agents_remember/memory_quality/memory_census_scope.py

## Governing Overview

[Memory quality overview](overview.md)

## Purpose

Captures the exact route-owned code and memory Git scope used by the structural memory census. It binds the canonical memory candidate pair, supports future-code and current-head modes, and records working, committed, and memory path changes without accepting them.

## Code Commentary

### Logic

`MemoryCensusCodeInput` validates the route mode and pair-owned code identities. `MemoryCensusScope` serializes the exact scope facts and exposes working, committed, and memory path projections. `capture_memory_census_scope` rechecks pair and memory-tree stability around the capture; `_diff` derives bounded Git path changes from exact trees.

**The comparison base (L37 fix round P1b).** `capture_memory_census_scope(contract, *, code_input=None,
comparison=_baseline_itself)` takes a `MemoryComparison`: `(memory repository, baseline commit, candidate tree)
-> comparison tree-ish`. The memory diff is taken against what it returns, and the scope records it as
`memory_comparison_tree`. By default that is the baseline commit itself. The application binds the converted
base (`application/memory_quality/census_base.census_comparison`), which this layer cannot reach. The payload
carries `memoryComparisonTree` only when it differs from the baseline, so an unconverted leaf's payload is
unchanged.

### Invariants And Boundaries

- The route derives candidate identity from the admitted contract and does not accept a caller-selected future tree.
- Pair, contract, and memory-tree changes during capture fail closed.
- Scope capture supplies structural evidence only; it does not mint semantic repair or certification authority.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

- Scope capture is repository-owned and exact-tree based. [1]

### Repo-Internal References

- Code-input modes and pair-owned candidate fields are strict. [2]
- Scope identity exposes stable serialized and path-change observations. [3]
- The route captures exact changes and refuses movement during the observation. [4]

- The scope is captured against a comparison tree the caller supplies; the baseline itself by default. [5]
- The scope records what the memory candidate was compared with. [6]

### Cross-Repo References

None; the scope owner uses the local contract and pair authorities.
