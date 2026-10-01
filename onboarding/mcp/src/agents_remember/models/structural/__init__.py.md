# mcp/src/agents_remember/models/structural/__init__.py

## Governing Overview

[Structural wire models](overview.md)

## Purpose

Marks the strict structural model package without re-exporting legacy exact-id schemas.

## Code Commentary

### Logic

Package marker only.

### Conventions

Import the concrete model module that owns the wire family.

### Invariants And Boundaries

Do not add compatibility exports for removed public exact-id models.

### Todos

None.

## Evidence

### Docs References


### Repo-Internal References

- Public agent and gate models live in explicit sibling modules. [1]

### Cross-Repo References
