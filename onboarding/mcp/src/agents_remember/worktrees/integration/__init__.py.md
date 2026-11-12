# mcp/src/agents_remember/worktrees/integration/__init__.py

## Governing Overview

[worktrees/integration route overview](overview.md)

## Purpose

Package marker for the integration-branch authority and ref-transaction modules (260815-DAG master
full-gate repair): a one-line docstring only — the package has no re-export surface.

## Code Commentary

The module is a single docstring (`"""Integration-branch authority and ref-transaction
modules."""`); the package's modules are imported by their full paths
(`agents_remember.worktrees.integration.integration_branch_authority`, etc.), not re-exported here.

### Invariants And Boundaries

- No `__all__` and no re-exports: importers name the module explicitly.

## Evidence

### Repo-Internal References

- The package marker docstring. [1]

### Cross-Repo References

No cross-repo boundary applies.

No meaningful cross-repo references found.
