# mcp/tests/test_empty_leaf_memory_scope.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Check leaf memory identity before the first onboarding card exists.

## Code Commentary

The tests require the pair, scope and context to retain the leaf's own onboarding path without creating it. Missing memory worktrees, missing Git markers and foreign repository bindings remain refusals. Changeset pairing uses the leaf worktree for working mode and the memory repository for committed mode, without an existence-based alternate root.

## Evidence

- An absent onboarding child does not change the live leaf's identity. [1]
- Missing memory or its Git marker remains refused. [2]
- A memory worktree from another repository remains refused. [3]
- The selected changeset mode determines the root even when both onboarding children are absent. [4]
