# mcp/test_support/agents_remember_test_support/code_quality/quality_subprocess_environment.py

## Governing Overview

[Python quality verification overview](overview.md)

## Purpose

Owns the environment boundary between one admitted quality-wrapper invocation and the candidate
tests/rails it launches, including checkout-local import-root construction.

## Code Commentary

### Logic

`child_environment` removes a closed set of outer-wrapper execution controls: retry disable/cache,
retry forcing identities, and the progress-report path. Candidate tests still inherit semantic
facts such as CI invocation, Dagger admission attestation, attempt nonce, memory cap, and ordinary
process environment. `build` then prepends source import roots and selects the active Coverage.py
database for the child rail.

`source_import_roots` resolves file and directory coverage targets to stable package parents while
deduplicating order. It was extracted from the oversized wrapper so environment construction has
one owner and nested wrapper tests cannot mutate the outer run's evidence locations.

### Invariants And Boundaries

- Only the five named outer-invocation controls are stripped; there is no prefix or unknown-value
  fallback.
- Admission, invocation, nonce, and memory-limit semantics survive into candidate tests.
- The outer retry cache and progress path cannot be overwritten by a nested quality-wrapper test.
- The module builds subprocess inputs only; it does not execute or admit a rail.

### Todos

None.

## Evidence

### Docs References

No external domain documentation governs this repository-owned process boundary.

### Repo-Internal References

- The closed outer-only set and child filtering are explicit. [1]
- Child construction preserves semantics while setting checkout import roots and coverage output. [2]
- Import roots are derived from product file/directory targets once. [3]
- Focused forcing proves only outer controls disappear. [4]

### Cross-Repo References

None.
