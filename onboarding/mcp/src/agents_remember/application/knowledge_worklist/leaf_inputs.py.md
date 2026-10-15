# mcp/src/agents_remember/application/knowledge_worklist/leaf_inputs.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Defines immutable explicit code/memory operands shared by leaf capture and completion.

## Code Commentary

CandidateTrees holds the already captured C and K_C Git trees, preventing a gate from recapturing working directories as substitutes. CapturedBase holds paired B/K_B and the immutable converted read_tree. ExplicitSides carries repositories, base revisions and a memory candidate that may be a revision or directory; a missing code_candidate explicitly selects capture from code_worktree. Its optional scope, owner, conversion cache, expected effects, coordination root and held base tree preserve the caller’s admitted comparison context.

## Invariants And Boundaries

These frozen dataclasses describe selected operands. Constructing them neither captures Git state nor grants authority; a held converted K_B and a memory base revision are distinct fields.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Defines immutable explicit code/memory operands shared by leaf capture and completion. These frozen dataclasses describe selected operands. Constructing them neither captures Git state nor grants authority; a held converted K_B and a memory base revision are distinct fields. [1]
