# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e`|
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Validates external terminal archive/receipt proof and the exact predecessor authority required to
publish a successor enclosure.

## Code Commentary

### Logic

A restartable predecessor must have no code or memory closeout/integration outputs. The terminal proof no longer tests retired ledger output cells; exact archive, receipt, locator, and predecessor evidence still governs successor publication.

Archive paths are fixed by the publication request and must be outside the old enclosure root.
Digest, receipt, and the pre-deletion locator must match. A surviving terminal contract may advance
only from archive-ready to the exact cleanup-completed state; restart requires a restartable
tombstone and exact terminal predecessor identity.

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

- A missing or deleted enclosure is never sufficient successor evidence.
- Archive, receipt, locator, and predecessor proofs must agree byte-for-byte.
- Successor publication is part of the terminal enclosure transaction, not a standalone WAL.

### Todos

None recorded for the ledger-retirement boundary.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `_restartable_predecessor_contract` requires a terminal restartable contract without recorded code/memory outputs. | `_restartable_predecessor_contract` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py:398-399 |
| `require_successor_generation` validates exact terminal predecessor and successor identities. | `require_successor_generation` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py:343-347 |

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=a92a727ad3fc82423b4e531f64c1059ef6135c9e082a22f1358ba1ae77d185dd. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final terminal-enclosure authority. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
