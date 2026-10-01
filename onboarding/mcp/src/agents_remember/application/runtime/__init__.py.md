# mcp/src/agents_remember/application/runtime/__init__.py

## Governing Overview

[runtime overview](overview.md)

## Purpose

Marks the cohesive application package for runtime startup, installation, and skill deployment.

## Code Commentary

The initializer carries only the package docstring. Public operations remain defined in
`install.py`, `startup.py`, and `skills.py`; adding re-exports here would create a second facade and
blur the direct domain imports used by MCP registration and payload builders.

## Invariants And Boundaries

- Keep this initializer declarative and free of process startup or installation side effects.
- Import the focused runtime module that owns an operation rather than routing through this file.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The package docstring names the three owned runtime concerns. [1]

### Cross-Repo References

No cross-repository implementation dependency governs this package marker.
