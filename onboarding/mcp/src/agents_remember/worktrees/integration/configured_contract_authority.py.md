# mcp/src/agents_remember/worktrees/integration/configured_contract_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/configured_contract_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

Current configured-contract authority at a mutation boundary.

## Code Commentary

### Logic

The public surface is `reread_configured_contract`, `require_configured_contract_repositories`. The mutation owner re-reads the already admitted configured contract under its existing serialization and compares exact repository authority. It translates expected reread failures through the shared admission refusal projector; it does not become a second public admission API or add a common lock.

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
| The module defines `reread_configured_contract`; `require_configured_contract_repositories` as its public seam. | L33-L91; L94-L118 | `mcp/src/agents_remember/worktrees/integration/configured_contract_authority.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Live Versus Terminal Authority

Configured repository identity is now separated from candidate-worktree presence.
`require_configured_terminal_contract_repositories` validates configured code/external-memory
repositories and their separation for an archived-terminal retry without requiring worktrees that
cleanup already deleted. Ordinary live mutations still require the candidate code and leaf-memory
identities. Terminal mode is a narrow finalization authority, never a generic fallback.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented the exact archived-terminal repository check without weakening live mutation authority. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
