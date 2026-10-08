# mcp/src/agents_remember/cli/leaf_enclosure_start.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Creates a missing leaf enclosure through a short-lived process of the same AR build.

## Code Commentary

The dashboard cannot directly write tool-server-owned worktree stores. start_leaf_enclosure_in_child launches this build with the selected config and canonical task context; the child calls the existing worktree start route and returns bounded written/refused facts. Parent verifies reported roots/identity before using them and refuses noncompletion or disagreement.

## Evidence

- Frozen implementation of start_leaf_enclosure_in_child supporting the stated file behavior. [1]

- Frozen implementation of run supporting the stated file behavior. [2]
- Frozen implementation of _differing_roots supporting the stated file behavior. [3]

## MIK-R95 Native Recovery Passthrough

The child replies now carry the native owner's recovery fields (`nextOperation`, `nextTool`, `nextArgs`, `nextRequiredArgs`, `nextStep`) and a `recovery` block beside the error, so a blocked stale-source preflight arrives at the caller as the owner's own blocked state with its required `stale_base_choice` rather than a reduced missing-contract error. The child keeps its root checks, writer admission and cut-off policy.
