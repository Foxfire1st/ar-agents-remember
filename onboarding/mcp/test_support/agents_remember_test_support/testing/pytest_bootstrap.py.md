# mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns route-neutral pytest hooks: process declaration, cache isolation, deterministic order, and
owned-global leak restoration.

## Code Commentary

The plugin begins the declared test process at import, exposes the random-order seed option/header,
shuffles collection deterministically when configured, isolates per-process cache, restores and
reports owned global leaks, and ends the process at pytest unconfigure. Before and after each test
module, an automatic module fixture resets already-loaded reset owners from the closed state
register. Per-test snapshots remain confined to restored rows; constant-for-tests rows survive
deferred imports rather than being erased at module boundaries.

## Invariants And Boundaries

- This module imports no Dagger admission, worktree service, or provider code.
- Both routes receive identical shared pytest behavior.
- Global restoration precedes leak failure.
- Module-boundary resets run in a `finally` path and never import a product owner.

## Evidence

### Repo-Internal References

- Shared hooks own ordering and process cleanup. [1]


- Already-loaded process state is reset before and after each module. [2]
- Per-test restoration runs before leak failure. [3]
