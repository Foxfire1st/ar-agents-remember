# mcp/tests/test_explainer_worktrees.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A test suite for explainer worktrees.py.md: it drives the behaviour the commentary states and asserts it.

## Code Commentary

Comparison blob tests verify exact binary and empty payloads, memoized success and absence, and a private spool that closes on successful reads, launch errors, timeouts and cancellation.

An explainer checkout is detached, exact and an ordinary writable worktree, witnessed by test_commit_checkout_is_detached_exact_and_ordinary_writable

## Evidence

- An explainer checkout is detached, exact and an ordinary writable worktree, witnessed by test_commit_checkout_is_detached_exact_and_ordinary_writable [1]
