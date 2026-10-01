# mcp/test_support/agents_remember_test_support/__init__.py

## Governing Overview

[Python verification infrastructure](overview.md)

## Purpose

Marks the verification-only Python package without exporting a convenience facade.

## Code Commentary

### Logic

The file is intentionally empty. Callers import the narrow `code_quality` or `testing` owner they
need, which keeps bootstrap fan-out and policy ownership observable.

### Conventions

Do not add package-level re-exports.

### Invariants And Boundaries

- Product code must not import this package.
- Empty initialization must remain side-effect free.

### Todos

None.

## Evidence

### Docs References

No external documentation governs this repository-local package boundary.

### Repo-Internal References

The explicit package classification is in `pyproject.toml`; the import firewall is forced by
`mcp/tests/test_gate_scope.py`.

### Cross-Repo References

No cross-repository boundary applies.
