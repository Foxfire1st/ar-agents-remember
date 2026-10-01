# mcp/src/agents_remember/mcp/tools/structural_agent.py

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

Adapts strict structural request DTOs to application services for dispatch, parent/child messaging,
retirement, and rename. It replaces the removed public leaf/exact-id addressing adapter.

## Code Commentary

### Logic

Each payload function builds one structural runtime, receives its operation-specific typed request,
invokes the corresponding application tool, and validates an operation-specific structural response.

### Conventions

This module is intentionally thin; authorization and lifecycle behavior stay in the application
and serving layers.

### Invariants And Boundaries

- Do not accept runtime ids through `overrides` or request fields.
- Do not restore the deleted leaf-ref compatibility tool.
- Keep one payload adapter per public operation for registry introspection.

### Todos

None.

## Evidence

### Docs References


### Repo-Internal References

- Six payload adapters expose the structural agent operation family. [1]
- The application service owns authorization and mutation. [2]

### Cross-Repo References
