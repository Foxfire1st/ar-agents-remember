# mcp/src/agents_remember/worktrees/activation/__init__.py

## Governing Overview

[activation overview](overview.md)

## Purpose

Package marker for the focused atomic-series selection and source-reconciliation authority.

## Code Commentary

### Logic

The module intentionally contains only its package docstring. It establishes the canonical import
home for the selector store, selecting transaction, exact release owner, and terminal bridge; it
does not re-export the old flat paths or introduce a second public API.

### Conventions

Consumers import the focused owner they need. Keep this marker free of compatibility aliases and
side effects.

### Invariants And Boundaries

- Package placement is structural; lifecycle ownership remains in the four focused modules.
- No old-path forwarding module or aggregate state owner is created here.

### Todos

The package boundary is reconciled to the frozen source; verification metadata awaits the real
code commit.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The package docstring names selection and source reconciliation as the route authority. [1]
- The route overview maps this route's concrete package owners. [2]

### Cross-Repo References

No cross-repository source is configured for this memory root.
