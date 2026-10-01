# mcp/tests/task_reopen_test_support.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Centralizes the real Git, enclosure, runtime-config, and task-document fixtures shared by task
reopen tests. It keeps reopening authority tests focused on their rule instead of repeating a
large terminal-predecessor world in every module.

## Code Commentary

### Logic

The helper publishes a terminal predecessor enclosure, constructs a completed leaf branch chain,
binds a repository-scoped runtime configuration, creates external-memory directories, and writes
leaf/master task documents with controlled identity/status variations.

### Conventions

Fixtures use real repository branches and canonical task/enclosure writers. Parameters expose only
the identity or status fact a forcing test needs to vary.

### Invariants And Boundaries

- This module is test support, not a production reopen or task-publication API.
- A reopen predecessor is terminalized through the same enclosure publication shape production
  readers consume.
- Branch lineage and task-document identity are explicit; tests must not replace them with an
  unqualified filename or guessed default branch.
- Shared construction must not weaken the assertions owned by the individual forcing modules.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source governs these repository-owned fixtures.

### Repo-Internal References

The source file is the direct evidence for the shared fixture boundary.

- The helper publishes an exact terminal predecessor and real super-to-leaf branch chain. [1]
- Runtime configuration and external-memory directories are built from the contract identity. [2]
- Leaf and master documents expose controlled lifecycle, topology, and row-status variants. [3]

### Cross-Repo References

No real adjacent repository is involved; all repositories are temporary test fixtures.
