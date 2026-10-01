# mcp/src/agents_remember/kernel/git_preparation.py

## Governing Overview

[Owning overview](../../../overview.md)

## Purpose

Typed Git preparation bindings, sealed private capabilities, and exact physical content proof.

## Code Commentary

### Logic

The private binding keeps the logical repository/ref and expected old commit separate from the preparation parent, admitted tree, and journal-named private root. Its live authorization callback governs create, materialize, and commit commands through the sole Git runner. Private creation remains strict: every admitted file, mode, and byte must match, and extra or missing content refuses.

`ExistingGitPreparationBinding` also names the actual immutable HEAD/tree. In the memory domain it additionally supplies `memory_content_tree`; the runner proves that this certificate subject equals the raw tree with only root `memory.md` removed. Code bindings leave `allow_memory_cache` false and do not carry a memory-content assertion. The optional field's type accommodates code bindings; a memory binding without that field is refused by the runner.

`require_physical_tree` reads no-follow bytes and modes and checks directory stability. Only an explicitly selected memory domain removes `memory.md` from expected and observed membership. Other ignored paths, similarly named files, submodules, missing files, and checkout transformations remain subject to the exact checks.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870`. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

The cache exception is confined to the literal root cache path and never changes a commit or its raw tree identity. It is not a general Git-ignore exemption. Newly created private memory outputs are still proved against their complete admitted cache-free tree; the logical memory observer is where the cache projection applies.

### Todos

No additional source-local TODO is asserted by this maintenance pass.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

- Existing observations bind raw HEAD/tree and the additional memory-content subject. [1]
- Private paths, object identities, hook policy, and operation identity are validated before capability use. [2]
- The sealed private capability revalidates the binding and invokes its live owner. [3]
- File modes and exact no-follow blob bytes are checked, including replacement during observation. [4]
- Only explicit memory observations omit root memory.md from physical membership. [5]
- The runner requires a memory content subject and proves its entries against the actual raw tree. [6]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.
