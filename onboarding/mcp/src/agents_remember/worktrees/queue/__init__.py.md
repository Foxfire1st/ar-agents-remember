# mcp/src/agents_remember/worktrees/queue/__init__.py

## Governing Overview

[worktrees/queue route overview](overview.md)

## Purpose

Package marker for the closeout-queue modules (260815-DAG master full-gate repair): a one-line
docstring only — the package has no re-export surface.

## Code Commentary

The module is a single docstring (`"""Closeout-queue modules for task-derived sprint
scheduling."""`); the package's modules are imported by their full paths
(`agents_remember.worktrees.queue.closeout_queue`, etc.), not re-exported here.

### Invariants And Boundaries

- No `__all__` and no re-exports: importers name the module explicitly.

## Evidence

### Repo-Internal References

- The package marker docstring. [1]

### Cross-Repo References

No cross-repo boundary applies.

No meaningful cross-repo references found.
