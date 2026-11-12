# mcp/tests/test_quality_subprocess_environment.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pure regression proof that nested candidate tests cannot inherit and overwrite an outer
quality-wrapper invocation's retry cache or progress evidence.

## Code Commentary

### Logic

The test constructs one representative environment containing every outer-only retry/report
control plus the Dagger admission, CI invocation, attempt nonce, memory cap, and ordinary `PATH`.
It asserts the closed outer-only set is absent from the child and every semantic/process value is
preserved exactly.

### Invariants And Boundaries

- The assertion compares the complete child mapping, so silently stripping an additional semantic
  value fails.
- The proof is pure and isolated from the admission-bound wrapper suite.
- Environment isolation prevents evidence-location collision; it does not change retry identity or
  candidate semantics.

### Todos

None.

## Evidence

### Docs References

No external domain documentation governs this repository-owned process boundary.

### Repo-Internal References

- Only outer retry/report controls are removed while admission and semantic values survive. [1]
- The production owner defines the exact closed set. [2]

### Cross-Repo References

None.
