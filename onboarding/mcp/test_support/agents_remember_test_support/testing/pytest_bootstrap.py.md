# mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns route-neutral pytest hooks: process declaration, cache isolation, deterministic order, and
owned-global leak restoration.

## Code Commentary

The plugin begins the declared test process at import, exposes the random-order seed option/header,
shuffles collection deterministically when configured, isolates per-process cache, restores and
reports owned global leaks, and ends the process at pytest unconfigure.

## Invariants And Boundaries

- This module imports no Dagger admission, worktree service, or provider code.
- Both routes receive identical shared pytest behavior.
- Global restoration precedes leak failure.

## Evidence

### Repo-Internal References

- Shared hooks own ordering and process cleanup. [1]
