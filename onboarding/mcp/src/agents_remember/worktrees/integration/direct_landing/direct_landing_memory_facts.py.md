# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_memory_facts.py

## Governing Overview

[overview](../overview.md)

## Purpose

Read-only external-memory branch evidence for direct landing.

## Code Commentary

`_memory_facts` returns only the mode for non-external contracts. External mode requires the configured memory repository, reads the accepted work branch through `branch_commit`, and returns mode/branch/HEAD. Missing authority and named unreadable-ref errors remain distinct; public failure evidence records the stage, side, branch name and exception type without inventing a memory output. This observer writes no ref or content.

## Invariants And Boundaries

The extracted helper retains its caller-owned operation and refusal boundary; this card is source inspection, not a new product execution or publication grant.

## Evidence

- Read-only external-memory branch evidence for direct landing. [1]
