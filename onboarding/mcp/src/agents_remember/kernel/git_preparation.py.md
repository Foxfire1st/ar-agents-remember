# mcp/src/agents_remember/kernel/git_preparation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/git_preparation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../../../overview.md` |

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

## Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is configured. | N/A | N/A |

## Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| Existing observations bind raw HEAD/tree and the additional memory-content subject. | `memory_content_tree` | mcp/src/agents_remember/kernel/git_preparation.py:44-44 |
| Private paths, object identities, hook policy, and operation identity are validated before capability use. | `PrivateGitPreparationCapability` | mcp/src/agents_remember/kernel/git_preparation.py:88-98 |
| The sealed private capability revalidates the binding and invokes its live owner. | n/a | [mcp/src/agents_remember/kernel/git_preparation.py](mcp/src/agents_remember/kernel/git_preparation.py) |
| File modes and exact no-follow blob bytes are checked, including replacement during observation. | n/a | [mcp/src/agents_remember/kernel/git_preparation.py](mcp/src/agents_remember/kernel/git_preparation.py) |
| Only explicit memory observations omit root memory.md from physical membership. | `require_physical_tree` | mcp/src/agents_remember/kernel/git_preparation.py:162-211 |
| The runner requires a memory content subject and proves its entries against the actual raw tree. | n/a | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Documented the typed existing-output binding, strict code/private proof, and exact memory-cache projection with an independently asserted content tree. Source SHA-256 `da69f0edb15f0013510e79062f54bf213d3dac633a7b448d7f0498e208e17392`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
