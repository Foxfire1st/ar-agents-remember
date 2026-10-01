# mcp/src/agents_remember/models/tools/__init__.py

## Governing Overview

[models overview](../overview.md)

## Purpose

Declares the package that owns registered tool request and response models.

## Code Commentary

### Logic

This marker groups the tool registry and strict response-model vocabulary without re-exporting the former flat module paths.

### Conventions

Tool wire models remain separate from application response projection and MCP registration.

### Invariants And Boundaries

- Do not add compatibility imports for the removed `models.tool_registry` or `models.tool_response` paths.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this package marker.

### Repo-Internal References

- The package docstring names registered tool request and response models as its scope. [1]

### Cross-Repo References

No cross-repository boundary is owned here.
