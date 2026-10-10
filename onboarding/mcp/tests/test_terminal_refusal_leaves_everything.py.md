# mcp/tests/test_terminal_refusal_leaves_everything.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

A refused terminal branch retirement changes nothing.

## Code Commentary

MIK-R82 Failure And Recovery Behavior: the cleanup once deleted a fully merged branch and then refused at a later check. Every check that can refuse now runs before the first deletion; a mid-deletion failure is answered as partial completion naming deleted and remaining work, never as a refusal.

## Evidence

- Refusal-before-deletion and honest partial-deletion answers are pinned. [1]
