# mcp/src/agents_remember/memory/carryover_evidence.py

## Governing Overview

[Memory area overview](overview.md)

## Purpose

Supplies read-only Git code-landing evidence and memory merge-base resolution for carryover.

## Code Commentary

### Evidence ordering

A path absent at official code is not-landed. Exact-landed-commit requires every relevant source-path commit to be ancestral to official code; one landed commit is insufficient. Otherwise compare stable path patch IDs, then final content. A changed path with no equivalence is same-path-changed, not automatic proof.

### Read-only boundary

Git uses the shared guarded runner with input_text for patch-id. Failed required commands raise. Changed-path selection uses ACMRT; object-ID lookup handles the root route as ref^{tree}. The memory merge base resolves the source memory HEAD within the target object database and returns None when unavailable. No memory bytes, stamps, commits, refs or ledger are written by this module.

## Evidence

- Evidence ordering: A path absent at official code is not-landed. Exact-landed-commit requires every relevant source-path commit to be ancestral to official code; one landed commit is insufficient. Otherwise compare stable path patch IDs, then final content. A changed path with no equivalence is same-path-changed, not automatic proof. [1]
- Read-only boundary: Git uses the shared guarded runner with input_text for patch-id. Failed required commands raise. Changed-path selection uses ACMRT; object-ID lookup handles the root route as ref^{tree}. The memory merge base resolves the source memory HEAD within the target object database and returns None when unavailable. No memory bytes, stamps, commits, refs or ledger are written by this module. [2]
