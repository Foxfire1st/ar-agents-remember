# mcp/src/agents_remember/certification/repository_profiles/source_selection/models.py

## Governing Overview

[Source applicability overview](overview.md)

## Purpose

Defines immutable repository declarations, exact candidate/base path observations and self-validating rail applicability decisions.

## Code Commentary

### Logic

`SourcePathApplicability` binds a selector identity/version, canonical sorted unique dependency prefixes, an evidence path and a declared non-applicability reason. `_require_relative` rejects absolute, traversal, backslash, NUL and noncanonical repository paths. `CandidateSourceSelection` binds the exact base commit/base tree and candidate tree to sorted unique changed paths and verifies the full observation digest.

`RailSourceSelection` recomputes selected paths from the declaration and source observation, checks applicability and selection identity, and verifies its complete decision digest. Full mode is always applicable; targeted mode is applicable when any declared prefix matches. A targeted empty selection must carry the repository-declared reason.

### Conventions

Use canonical repository-relative paths and ordered unique tuples; preserve the declaration, source observation and mode together.

### Invariants And Boundaries

- Prefix matching is literal `startswith`; use a trailing slash when the declaration intends a directory boundary.
- Selection is fixed before execution. It cannot be inferred from a test exit or rewritten after a failure.
- A model validates the supplied observation, not whether Git actually produced it; the Git owner supplies that proof.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned selection contract.

No configured domain documentation applies.

### Repo-Internal References

- Declarations and observations enforce canonical inputs; decisions recompute matching and both digest domains. [1]

### Cross-Repo References

No cross-repository implementation boundary is owned by this file.

No cross-repository reference is required.
