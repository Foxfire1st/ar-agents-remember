# mcp/src/agents_remember/worktrees/integration/integration_quality_checkout.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Materializes a temporary detached checkout at the accepted candidate commit for the integration quality gate.

## Code Commentary

`integration_quality_checkout` now accepts an optional `commit`; a leaf with no commit reuses the ordinary worktree, while a pinned commit yields a detached exact-candidate checkout.

`integration_quality_checkout` creates an isolated temporary worktree from the exact journaled code candidate, yields it to the gate, and removes it afterward. Atomic series gates therefore test the candidate itself rather than whichever branch the repository-root checkout happens to own.

## Invariants And Boundaries

- Quality input is commit-addressed and detached from ambient checkout state.
- Temporary checkout cleanup is part of the context-manager boundary.
- This helper does not authorize or move integration refs.

## Evidence

### Repo-Internal References

- The context manager creates and tears down the exact candidate checkout. [1]

### Documentation References

No configured domain-documentation or cross-repository source applies to this file.
