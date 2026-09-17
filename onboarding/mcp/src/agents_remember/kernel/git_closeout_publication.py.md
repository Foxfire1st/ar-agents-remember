# mcp/src/agents_remember/kernel/git_closeout_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/git_closeout_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e`|
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `../../../overview.md` |

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

## Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is configured. | — | — |

## Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The binding records exact ref/commit/tree facts and the explicit memory-only cache option. | `GitCloseoutPublicationBinding` | mcp/src/agents_remember/kernel/git_closeout_publication.py:33-82 |
| Raw commit identity, raw tree, and sole expected-old parent are independently enforced. | `require_prepared_bytes` | mcp/src/agents_remember/kernel/git_closeout_publication.py:61-82 |
| Capability use reopens the caller-owned authority. | `require_authority` | mcp/src/agents_remember/kernel/git_closeout_publication.py:91-95 |
| Result records preserve before/after observations and any actual Git command result. | `GitCloseoutPublicationResult` | mcp/src/agents_remember/kernel/git_closeout_publication.py:105-109 |
| The runner rejects cache-bearing new memory output and checks the exact old/new ref states. | `_observe_closeout_publication` | mcp/src/agents_remember/kernel/git_command.py:688-720 |
| Publication issues one expected-old CAS and does not rerun already-new or existing output. | `publish_git_closeout_ref` | mcp/src/agents_remember/kernel/git_command.py:760-783 |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | — | — |

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Recorded the memory-domain cache option without weakening raw commit/tree/parent proof or changing code publication semantics. Source SHA-256 `d6c8f5f2e7a71bdd9a79cd28b5254bf0d101c839d4b128bdb685348a0779c8e2`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
