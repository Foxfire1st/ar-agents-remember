# mcp/src/agents_remember/certification/repository_profiles/source_selection/__init__.py

## Governing Overview

[Source applicability overview](overview.md)

## Purpose

Identifies the package for repository-declared source applicability fixed before plan compilation.

## Code Commentary

### Logic

The module contains a package docstring only. Concrete observation, validation, compilation and reading APIs live in their named modules; importing the package performs no selection or execution.

### Conventions

Import the required observation, compiler, validation or reader from its concrete module.

### Invariants And Boundaries

- No re-export, registration or applicability decision occurs during package import.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned selection contract.

No configured domain documentation applies.

### Repo-Internal References

- Package initialization is documentation-only. [1]

### Cross-Repo References

No cross-repository implementation boundary is owned by this file.

No cross-repository reference is required.
