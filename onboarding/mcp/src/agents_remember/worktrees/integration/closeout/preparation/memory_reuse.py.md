# mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is configured. | N/A | N/A |

## Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The observer excludes cache status and binds actual HEAD/tree plus the certified content subject. | `head_tree` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py:42-42 |
| The exact raw HEAD tree is checked before projected content is inspected. | `content_tree` | mcp/src/agents_remember/kernel/git_command.py:472-472 |
| Only root memory.md is removed when proving equality with a required memory certificate subject. | n/a | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| The closed record hashes the raw and certified identities separately. | n/a | [mcp/src/agents_remember/models/lifecycles/preparation.py](mcp/src/agents_remember/models/lifecycles/preparation.py) |
| The shared exact Git pathspec names only the derived root cache. | n/a | [mcp/src/agents_remember/kernel/memory_ledger.py](mcp/src/agents_remember/kernel/memory_ledger.py) |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Replaced ledger/mapping authority with read-only current-HEAD reuse and independently bound cache-free content; cache-only staging no longer creates a memory output. Source SHA-256 `e76443ad8abc02674ccbbe5993104ab93f8f74601e9ed051545ed22dd419bbc8`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
