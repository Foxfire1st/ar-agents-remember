# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree-integration overview](../overview.md)

## Purpose

Validates external terminal archive/receipt proof and the exact predecessor authority required to
publish a successor enclosure.

## Code Commentary

Archive paths are fixed by the publication request and must be outside the old enclosure root.
Digest, receipt, and the pre-deletion locator must match. A surviving terminal contract may advance
only from archive-ready to the exact cleanup-completed state; restart requires a restartable
tombstone and exact terminal predecessor identity.

## Invariants And Boundaries

- A missing or deleted enclosure is never sufficient successor evidence.
- Archive, receipt, locator, and predecessor proofs must agree byte-for-byte.
- Successor publication is part of the terminal enclosure transaction, not a standalone WAL.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final terminal-enclosure authority. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
