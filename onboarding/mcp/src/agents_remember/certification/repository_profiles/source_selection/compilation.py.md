# mcp/src/agents_remember/certification/repository_profiles/source_selection/compilation.py

## Governing Overview

[Source applicability overview](overview.md)

## Purpose

Compiles a declared rail’s applicability from an already observed candidate/base path census.

## Code Commentary

### Logic

`compile_source_applicability` computes literal prefix matches, marks full mode or any match applicable, and binds the declaration, source observation and mode into the selection identity. Applicable decisions retain the supplied population; non-applicable decisions have no population and retain the declared reason. The final payload is validated by `RailSourceSelection` with its complete decision digest.

`requires_source_selection` checks whether any rail in the selected gate/rail population declares source applicability, so callers observe Git only for a selected owner that needs the input.

### Conventions

Pass the existing repository population and exact admitted declaration; the compiler owns deterministic decision serialization.

### Invariants And Boundaries

- Compilation is pure: it does not observe Git, write evidence or start a rail.
- No posthoc skip or full-population fallback is introduced by this compiler.
- Full mode remains applicable even when its declared path matches are empty.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned selection contract.

No configured domain documentation applies.

### Repo-Internal References

- The compiler binds applicability, identity and decision digest; the predicate checks selected rail identities. [1]

### Cross-Repo References

No cross-repository implementation boundary is owned by this file.

No cross-repository reference is required.
