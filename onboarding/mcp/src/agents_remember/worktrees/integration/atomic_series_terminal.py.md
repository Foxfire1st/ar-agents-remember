# mcp/src/agents_remember/worktrees/integration/atomic_series_terminal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/atomic_series_terminal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T17:23+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktree-integration overview](overview.md)

## Purpose

Issues the ephemeral capability required to clean up or abandon an atomic series enclosure.

## Code Commentary

The permit binds the exact canonical series address, operation, contract, active context, and
current thread. Children must already be retired unless a retry is backed by exact archived
terminal authority. The permit is deliberately unforgeable and valid only inside the bounded
terminal transaction that created it.

## Invariants And Boundaries

- A permit cannot be serialized, reused, or treated as queue-held terminal authority.
- Retry authority comes from exact archived terminal proof, not missing worktree state.
- Cleanup and abandon must prove the same series and transaction context.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Terminal series authority is an ephemeral context-bound capability. | `AtomicSeriesTerminalPermit` | mcp/src/agents_remember/worktrees/integration/atomic_series_terminal.py:24-28 |

## Update History

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 local type-parameter migration for terminal publication and confirmed that atomic-series authority and cleanup/abandon behavior remain as documented. Verification remains closeout-owned.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final terminal-capability owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
