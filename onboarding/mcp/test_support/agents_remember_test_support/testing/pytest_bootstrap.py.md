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
- The closed-register reset visits already-loaded owners without importing them. The module-boundary fixture also imports the lightweight worktree service holder explicitly, and resets it before the module and in its `finally` path.


The module-boundary fixture resets the worktree service holder as well as the closed mutable-state register, before the module and in its `finally` cleanup. The holder is one object rather than a module-level collection the syntactic scanner discovers; an earlier module's server supplier cannot serve the next module's worktree operation.

## Evidence

### Repo-Internal References

- Shared hooks own ordering and process cleanup. [1]


- Already-loaded process state is reset before and after each module. [2]
- Per-test restoration runs before leak failure. [3]

- The module-boundary fixture resets the worktree service holder as well as the closed mutable-state register, before the module and in its `finally` cleanup. The holder is one object rather than a module-level collection the syntactic scanner discovers; an earlier module's server supplier cannot serve the next module's worktree operation. [4]
