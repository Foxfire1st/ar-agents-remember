# mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Read-only proof of an actual existing memory HEAD and its separately certified content tree.

## Code Commentary

### Logic

Status excludes only root `memory.md`; real memory-content changes return no reuse proof and leave creation to the output owner. Cache-only edits, forced staging, or cache index flags do not select a write. The observer reads the actual repository identity, logical branch, HEAD commit, and raw HEAD tree without replacing them with a normalized tree.

An `ExistingGitPreparationBinding` supplies both that raw tree and the independent certified content tree in the explicit memory domain. The kernel proves the raw HEAD/ref identity, removes only the cache entry for content comparison, and checks every remaining index entry, flag, and physical blob. The returned closed proof binds `logicalHeadCommit`, `logicalHeadTree`, and `certifiedContentTree` into its digest, with physical reproof around construction.

There is no ledger parser, code-to-memory mapping lookup, or historical mapped-commit selection here. Reuse retains current HEAD whether or not a newer code commit has attribution; it never invents a new memory commit or stages cache maintenance.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870`. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

The memory-domain content projection cannot be used as the raw HEAD tree. Cache bytes are irrelevant to reuse, but a changed real file, wrong repository/ref, hidden real-content flag, or mismatched certificate subject still refuses. This function is read-only.

### Todos

No additional source-local TODO is asserted by this maintenance pass.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

- The observer excludes cache status and binds actual HEAD/tree plus the certified content subject. [1]
- The exact raw HEAD tree is checked before projected content is inspected. [2]
- Only root memory.md is removed when proving equality with a required memory certificate subject. [3]
- The closed record hashes the raw and certified identities separately. [4]
- The shared exact Git pathspec names only the derived root cache. [5]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.
