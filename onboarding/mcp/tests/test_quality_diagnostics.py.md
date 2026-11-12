# mcp/tests/test_quality_diagnostics.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Proves that diagnostic metric findings remain visible without blocking delivery.

## Code Commentary

### Logic

Two tests inject a measured zero-percent diff result and a production CRAP score of 72. The real post-coverage reporting functions return zero while printing the findings and review threshold 20. Measurement/calculation are mocked; these cases prove result interpretation, not real Git diff parsing or actual coverage collection. They also reject a required-branch-coverage prescription.

### Conventions

These are focused unit cases under the canonical evidence-lane manifest. Reuse their behavior
boundary when changing policy rather than adding duplicate metric or collection assertions.

### Invariants And Boundaries

There is **no per-declaration default budget**: `mcp/tests/conftest.py` registers the two ini names with `addini` and carries no `default=`, and the enforced pair lives once, in the repository-root `pyproject.toml` under `[tool.pytest.ini_options]` — **2300 unit / 400 integration** when this was written; read it there, it moves. Coverage is diagnostic; production
CRAP 20 triggers review without failing delivery. Full suites and whole-candidate review occur at
master completion. A green unit result is not a certification certificate.

### Todos

Verification metadata remains closeout-owned; this card records source inspection only.

## Evidence

### Docs References

No Domain Documentation source is configured; this behavior is repository-owned.

No external domain claim is needed.

### Repo-Internal References

The exact functions below establish the tested boundary and its test doubles.

- Proves that diagnostic metric findings remain visible without blocking delivery. [1]
- Proves that diagnostic metric findings remain visible without blocking delivery. [2]

### Cross-Repo References

No cross-repository protocol is exercised by these unit cases.

No external boundary is claimed.
