# mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935`|
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain source is configured. | N/A | N/A |

## Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Existing code uses a strict typed binding, while enabled code delegates to the private executor. | L20-L36 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py) |
| Prepared or existing raw code output is retained through the shared selected-output owner. | L39-L48 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_execution.py) |
| The kernel rechecks actual HEAD/ref/tree and physical output around the raw commit read. | L489-L498 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Reconciled the typed existing-code binding and its deliberately strict code domain; private execution and raw-output retention remain unchanged. Source SHA-256 `3dc4afdacd6deb7c741ba3a9419e3778ea0bfc9132a8ba20594ec8b1205d4f71`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
