# mcp/src/agents_remember/worktrees/modules/contract_reader.py

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

`worktrees/modules/contract_reader.py` (260731-EFA-L9) is the worktree-backed contract reader
bound into the kernel coordination resolver. The kernel resolver declares `ContractReaderPort`;
this adapter implements it with the worktree contract-file primitives (contract loading,
task-root and leaf-enclosure path resolution).

## Code Commentary

### Logic

`WorktreeContractReader` (cit:(["class WorktreeContractReader"], mcp/src/agents_remember/worktrees/modules/contract_reader.py:27-27)) loads the leaf series contract and
resolves the task root and enclosure paths the resolver needs. The reader degrades cleanly on
reader failure so the resolver can report the missing/unreadable contract rather than crashing.

### Invariants And Boundaries

- The resolver only consumes the declared port; this adapter is the one production binding.
- `__all__` exports only `WorktreeContractReader`.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- The kernel resolver declares the port this adapter implements. [1]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
