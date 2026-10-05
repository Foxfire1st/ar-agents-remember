# operations/closeout.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Coordinate the existing authorized paired code/memory transaction and verify its exact outcome.

## Current Contract

Manager or Orchestrator coordinates closeout with supplied AR task authority. In a flat run, Architect may coordinate only under existing delegated c-09/c-12 authority. Worker, Reviewer and Curator do not perform this operation.

Read the current preview and authority contract; bind the exact task/contract, code and memory worktrees, candidate tips, changed paths, checks and required reports. Targeted failures and unrun checks remain visible. Required curation/coherence and real conflict/authority checks still govern the transaction.

## Conventions

Canonical skills/l-01-agent-lifecycles/operations/closeout.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

The existing AR owner validates and applies the paired transaction. Raw Git does not reproduce that owner’s logic. Do not claim commit, integration, push or acceptance before reading the owner result and verifying the exact pair; human-pinned decisions remain with their authority.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| Authorized owner, exact paired inputs, visible checks and owner-result readback. | lines 3-7 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/closeout.md:3-7 |
