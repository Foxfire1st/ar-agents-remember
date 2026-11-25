# mcp/src/agents_remember/cli/leaf_enclosure_start.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Creates a missing leaf enclosure through a short-lived process of the same AR build.

## Code Commentary

The dashboard cannot directly write tool-server-owned worktree stores. `start_leaf_enclosure_in_child` launches this build with the selected config and canonical task context. The child checks its expected roots before it runs the worktree start route. The parent checks the typed reply and exit status. A successful start may carry a file-brief advisory back, and the caller rereads the addressed enclosure contract through status.

## Current Contract — Scoped Launch And Settings Changes

The child enters tolerate_unreadable_review only around worktree_start_tool, after identity/config/root checks and together with stdout redirection. Context variables do not cross exec, so the launch-only diagnostic read must be re-established in this process.

This is not a public worktree-reader relaxation or permission to erase broken review evidence. The fallback isolates invalid review lanes; other task identity remains strict and raw evidence survives serialization. A root mismatch ends the child with a typed `leaf_enclosure_roots_differ` refusal before it enters the launch-only scope or starts a backend. The child’s 800-character JSON message keeps the no-start sentence and every differing root label. Path detail uses the remaining space, with the settings path last.

## Evidence

- Root validation and refusal precede the child-local diagnostic scope. [4]
- Only review-lane validation failures can be isolated. [5]
- Incidental publication retains raw broken evidence. [6]



- Frozen implementation of start_leaf_enclosure_in_child supporting the stated file behavior. [1]


- The private child budgets the typed no-start message for every differing label. [2]

- The child records a separate loaded and requested pair for each differing root. [3]

## MIK-R95 Native Recovery Passthrough

The child replies now carry the native owner's recovery fields (`nextOperation`, `nextTool`, `nextArgs`, `nextRequiredArgs`, `nextStep`) and a `recovery` block beside the error, so a blocked stale-source preflight arrives at the caller as the owner's own blocked state with its required `stale_base_choice` rather than a reduced missing-contract error. The child keeps its root checks, writer admission and cut-off policy.
