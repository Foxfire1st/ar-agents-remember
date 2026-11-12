# mcp/src/agents_remember/worktrees/integration/lifecycle/worker/state.py

## Governing Overview

[worktree integration overview](../../overview.md)

## Purpose

Reconcile durable worker bindings with exact live process identity.

## Code Commentary

### Logic

The public surface is `reconcile_worker_exit`, `project_worker_exit`, `release_worker_after_exit`. Worker authority remains durable until exact process identity and termination are proven. Signal, permission, launch, or observation failure records a termination-required/public recovery result and blocks replacement instead of optimistically clearing the PID or lease.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `reconcile_worker_exit`; `project_worker_exit`; `release_worker_after_exit` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
