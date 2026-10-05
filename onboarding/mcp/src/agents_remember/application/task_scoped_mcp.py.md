# mcp/src/agents_remember/application/task_scoped_mcp.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Derives immutable call-local MCP repository roots for an admitted canonical leaf reader request.

## Code Commentary

Without task_context readers retain configured Projects roots. With context, repository must match, task must be a canonical leaf with exactly one bound enclosure, configured-contract admission must be current, and roots must exist. Caller supplies task/contract identity, never roots. A valid context for another leaf remains admissible; launch binding is not a second reader-scope gate.

## Evidence

- Frozen implementation of task_scoped_mcp_config_for_reader supporting the stated file behavior. [1]
- Frozen implementation of _admit_task_scope supporting the stated file behavior. [2]
- Frozen implementation of _canonical_leaf_contract supporting the stated file behavior. [3]
- Alternating/concurrent registered base and leaf calls preserve their source/memory roots; wrong repository, canonical contract and malformed pairs refuse. [4]
