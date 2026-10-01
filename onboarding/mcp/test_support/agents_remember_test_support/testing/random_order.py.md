# mcp/test_support/agents_remember_test_support/testing/random_order.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Provides deterministic pytest collection-order randomization shared by both testing routes. It
moved from the test tree so production plugins do not depend on test helpers.

## Code Commentary

`shuffle_items` uses a local `random.Random(seed)` instance and changes only the supplied item
list, preserving reproducibility without mutating the process-global RNG.

## Invariants And Boundaries

- The reported seed reproduces the exact order.
- No process-global random state is changed.

## Evidence

### Repo-Internal References

- Collection order uses a local seeded RNG. [1]
