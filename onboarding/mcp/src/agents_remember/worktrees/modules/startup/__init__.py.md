# mcp/src/agents_remember/worktrees/modules/startup/__init__.py

## Governing Overview

[worktree modules overview](../overview.md)

## Purpose

Declares the worktree-start package for contract, provider, leaf-reference, and result collaborators.

## Code Commentary

### Logic

The marker groups the start collaborators below the `start.py` coordinator without adding another start entrypoint.

### Conventions

Contract derivation and start result shaping stay separate from the coordinating mutation flow.

### Invariants And Boundaries

- Do not restore the removed flattened module paths through compatibility exports.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this package marker.

### Repo-Internal References

- The package docstring names start contract, provider, leaf-ref, and result collaborators. [1]

### Cross-Repo References

No cross-repository boundary is owned here.
