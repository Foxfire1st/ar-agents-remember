# mcp/src/agents_remember/models/lifecycles/__init__.py

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

Marks the package that owns lifecycle request, response, finalization, and durable-operation models.

## Code Commentary

The initializer is deliberately declarative. Callers import the focused model module so the package
does not become a compatibility facade or create model import cycles.

## Invariants And Boundaries

- Keep the initializer free of model definitions and runtime side effects.
- Add lifecycle wire vocabulary to the focused owner and update the response registry/importers.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The package docstring identifies lifecycle request/response ownership. [1]

### Cross-Repo References

No cross-repository implementation dependency governs this package marker.
