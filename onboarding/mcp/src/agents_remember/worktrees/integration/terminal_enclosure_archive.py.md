# mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

L2 fail-closed boundary before L5 owns terminal enclosure archival.

## Code Commentary

### Logic

The public surface is `terminal_archive_required_result`. This is intentionally a fail-closed L2 hook. Retirement preserves the enclosure, journal, branches, commits, reports, approval, and history; cleanup may not delete canonical evidence until L5 supplies external terminal archive proof and deletion ordering.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module defines `terminal_archive_required_result` as its public seam. | L15-L103 | `mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Crash-Safe External Terminal Archive

This module now publishes and observes the bounded canonical archive before enclosure-root deletion.
Every operation must be terminal with no live worker, ambiguous mutation, or incomplete publication.
The transaction writes exact archive bytes, then an external receipt, then the terminal locator;
retries must prove the identical request and bytes. `terminal_contract_authority_if_present`
returns strict archive authority only and never guesses a live fallback.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: replaced the former refusal stub with the final archive/receipt/locator transaction. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
