# mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675`|
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
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
| No external domain source is configured. | — | — |

## Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The observer excludes cache status and binds actual HEAD/tree plus the certified content subject. | `observe_existing_memory_proof`; `head_tree` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py:19-63 |
| The exact raw HEAD tree is checked before projected content is inspected. | `_require_existing_preparation`; `content_tree` | mcp/src/agents_remember/kernel/git_command.py:451-465; mcp/src/agents_remember/kernel/git_command.py:472-472 |
| Only root memory.md is removed when proving equality with a required memory certificate subject. | `_existing_preparation_entries`; `_require_existing_preparation` | mcp/src/agents_remember/kernel/git_command.py:468-486; mcp/src/agents_remember/kernel/git_command.py:451-465 |
| The closed record hashes the raw and certified identities separately. | `ExistingMemoryPreparationProof` | mcp/src/agents_remember/models/lifecycles/preparation.py:43-69 |
| The shared exact Git pathspec names only the derived root cache. | `MEMORY_CACHE_EXCLUDE` | mcp/src/agents_remember/kernel/memory_ledger.py:25-27 |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Replaced ledger/mapping authority with read-only current-HEAD reuse and independently bound cache-free content; cache-only staging no longer creates a memory output. Source SHA-256 `e76443ad8abc02674ccbbe5993104ab93f8f74601e9ed051545ed22dd419bbc8`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
