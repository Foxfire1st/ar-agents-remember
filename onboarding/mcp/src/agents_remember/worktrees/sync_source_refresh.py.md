# mcp/src/agents_remember/worktrees/sync_source_refresh.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_source_refresh.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file centralizes the bounded pre-lock upstream refresh shared by direct sync and atomic-series
selecting admission. It updates remote-tracking evidence without confusing fetch results with local
protected-source authority.

## Code Commentary

### Logic

`fetch_source_upstreams` builds the code target and optional external-memory target, resolves each
source branch's configured upstream, and reports `no-upstream`, `fetched`, or `failed` per side.
Offline or remote-less state is returned as evidence; later sync proceeds from exact local branch
facts pinned only after repository integration authority is acquired.

### Conventions

Fetch is best-effort and result-shaped, never a mutation admission decision. The shared helper avoids
duplicating subtly different pre-lock fetch loops across selecting and explicit sync surfaces.

### Invariants And Boundaries

- This helper never reads or moves a local work/source branch.
- A failed fetch is not silently treated as a successful refresh.
- Local source tips, not remote-tracking refs, remain transaction authority.

### Todos

Final call sites are reconciled to the frozen source; verification remains empty until the real
code commit exists.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selecting admission refreshes before acquiring integration authority and then re-reads the contract. | `activate_atomic_series_contract` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:41-79 |
| The sync module consumes fetched evidence while pinning local sources under authority. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:72-100 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of bounded pre-lock source refresh call
  sites; no local selection or mutation authority is claimed.

- 2026-08-26T02:55+02:00 — Drafted shared source-refresh onboarding; final source inventory and
  verification remain open.