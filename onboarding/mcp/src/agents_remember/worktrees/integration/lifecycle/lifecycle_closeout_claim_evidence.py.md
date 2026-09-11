# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_closeout_claim_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_closeout_claim_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T16:57+02:00 |
| lastVerifiedCommitHash | `8dcf0645fdbc3aa490132d5947b22227d45ff302` |
| lastVerifiedCommitDate | 2026-08-26T16:57:26+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree-integration overview](../overview.md)

## Purpose

Builds the immutable closeout-preview argument map from the accepted operation input. Only enabled
code, memory, and ledger legs contribute their explicit commit-message fields.

## Code Commentary

The helper translates one accepted closeout input into the corrected public preview call. It does not
own door ancestry, cancellation release, queue selection, or operation replacement.

## Invariants And Boundaries

- Preview arguments are authority-free immutable inputs until the owning transaction validates them.
- Disabled commit legs never acquire synthesized messages.
- Door, queue, cancellation, and replacement authority stay with their owning lifecycle transactions.

## Update History

- 2026-08-26T16:57+02:00 — Removed the obsolete claimed-predecessor resolver after
  cancelled-generation replacement was returned to current door truth plus journal-owned worker-exit
  evidence. The module now owns only preview argument projection.
- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final claim-evidence helper. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
