# mcp/src/agents_remember/application/lifecycle/__init__.py

## Governing Overview

[application overview](../overview.md)

## Purpose

Declares the application-layer package that owns public lifecycle admission, controls, status projection, and detached-worker coordination.

## Code Commentary

### Logic

This marker makes the package boundary explicit; it intentionally exports no compatibility aliases.

### Conventions

Application adapters belong here, while durable journal and Git authority remain in `worktrees/integration/lifecycle`.

### Invariants And Boundaries

- Do not turn the package marker into a second lifecycle authority or fallback import surface.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal package marker.

### Repo-Internal References

- The docstring declares lifecycle admission, control, status, and worker application ownership. [1]

### Cross-Repo References

No cross-repository boundary is owned here.
