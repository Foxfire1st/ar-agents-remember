# mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675`|
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Private code creation or genuine existing-code observation.

## Code Commentary

### Logic

Enabled preparation uses the journal-bound private executor. The no-write route constructs an `ExistingGitPreparationBinding` for the logical root, repository identity, exact branch, old commit, and admitted raw tree. It uses the strict code domain: no cache exception or memory-content assertion is supplied.

Both routes retain exact raw output bytes and reobserve the current selection. They do not discover an arbitrary commit, synthesize a message for a no-write output, create a private checkout for existing code, or publish the logical ref.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870`. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

A code path named memory.md is ordinary code-side content. The memory-domain filtering rule must never be inferred from a filename in this route.

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
| None | `observe_code_output`; `prepare_code_output` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py:20-36; mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py:39-48 |
| None | `prepare_code_output`; "retain_code_output(selected, raw)" | mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py:39-48 |
| None | `inspect_existing_git_preparation`; `_require_existing_preparation`; `_require_preparation_index` | mcp/src/agents_remember/kernel/git_command.py:390-427; mcp/src/agents_remember/kernel/git_command.py:451-465; mcp/src/agents_remember/kernel/git_command.py:489-498 |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Reconciled the typed existing-code binding and its deliberately strict code domain; private execution and raw-output retention remain unchanged. Source SHA-256 `3dc4afdacd6deb7c741ba3a9419e3778ea0bfc9132a8ba20594ec8b1205d4f71`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
