# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_binding.py

## Governing Overview

[Closeout](overview.md)

## Purpose

Builds and checks the shared dependency binding of a curator-coherence record.

## Code Commentary

The dependency set binds the candidate code and memory trees, task topology and intent, complete quality evidence, and its measured quality identities. Stored assessment content addresses are direct dependencies.

A live record with either measured identity missing or different is stale and asks for publication. Historical readability and stored-generation integrity remain separate from this live freshness check.

## Relationships

The publisher and the shared reader use this module so status, validation, the quality check and closeout apply the same binding.

## Evidence

- The shared builder names quality and assessment dependencies. [1]
- Missing or unequal measured identities require publication. [2]
