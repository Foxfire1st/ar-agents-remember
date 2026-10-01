# mcp/src/agents_remember/worktrees/integration/lifecycle/worker/launch.py

## Governing Overview

[worktree integration overview](../../overview.md)

## Purpose

Stable failure publication for detached lifecycle-worker launch.

## Code Commentary

### Logic

The public surface is `launch_or_fail`. Worker authority remains durable until exact process identity and termination are proven. Signal, permission, launch, or observation failure records a termination-required/public recovery result and blocks replacement instead of optimistically clearing the PID or lease.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

### CCR private preparation boundary

A failed worker launch preserves a closeout generation with retained private preparation as `input-required` and uses the exact recovery phase. Its next action is recovery, not replacement/retry of a fresh generation; the private-preparation phase does not imply consumed approval.

- The current `launch_or_fail` boundary implements the preparation contract above. [1]

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `launch_or_fail` as its public seam. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
