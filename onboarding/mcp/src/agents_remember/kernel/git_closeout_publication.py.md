# mcp/src/agents_remember/kernel/git_closeout_publication.py

## Governing Overview

[Owning overview](../../../overview.md)

## Purpose

Expected-old publication capability and exact prepared commit proof for one Git ref.

## Code Commentary

### Logic

Publication has a separate sealed capability from private preparation. The binding names the operation, generation, logical branch, expected old commit, and exact prepared commit/tree. Raw commit validation recomputes the complete object identity and requires the declared raw tree; a new prepared commit must have the sole expected-old parent. Observations distinguish old, new, and existing states.

`allow_memory_cache` is false by default. The memory publication owner selects it explicitly so the runner can omit only root `memory.md` from logical index, flag, and physical-content checks. This never changes `prepared_tree` or the hash/parent checks over raw commit bytes. The runner refuses a newly published memory commit that actually includes the cache. Lifecycle approval, cancellation, and selected-journal ownership remain caller responsibilities.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870`. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

An existing or already-new observation does not authorize another ref mutation. Cache filtering is specific to memory content; code publication remains strict. The binding does not turn an ignored cache into a third output or a commit-authority record.

### Todos

No additional source-local TODO is asserted by this maintenance pass.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

- The binding records exact ref/commit/tree facts and the explicit memory-only cache option. [1]
- Raw commit identity, raw tree, and sole expected-old parent are independently enforced. [2]
- Capability use reopens the caller-owned authority. [3]
- Result records preserve before/after observations and any actual Git command result. [4]
- The runner rejects cache-bearing new memory output and checks the exact old/new ref states. [5]
- Publication issues one expected-old CAS and does not rerun already-new or existing output. [6]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.
