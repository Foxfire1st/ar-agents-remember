# mcp/src/agents_remember/memory_quality/style/citations/__init__.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Package marker for shared citation parsing, symbol bindings and terminal cache fencing; runtime behavior is owned by surviving sibling modules, not a legacy range-resolution checker.

## Code Commentary

### Logic

The file is a package marker; public behavior lives in sibling modules of the same package.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- Keep the package initializer empty unless a concrete import-surface requirement appears.

### Todos

None.

## Evidence

### Repo-Internal References

The package is a marker; the nearest route overview documents the route scope.

- The package docstring names shared citation parsing, symbol bindings and terminal cache fencing. [1]
