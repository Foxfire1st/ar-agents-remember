# mcp/src/agents_remember/worktrees/sync_source_refresh.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_source_refresh.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash |  `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate |  2026-09-14T19:36:04+02:00|
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
| Selecting admission refreshes before acquiring integration authority and then re-reads the contract. | `activate_atomic_series_contract` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:55-100 |
| The sync module consumes fetched evidence while pinning local sources under authority. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:82-110 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (reopened-claim judgement): the checker reopened
  the `sync_contract_under_authority` claim because that construct changed after verification.
  Re-read the claim against `sync_transaction.py`: the function is defined at `:82` and pins the
  local sources under authority through `:110`, so the regenerated range (82-110) is the function
  and the wording stands. Retained; verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 1 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-10T15:06+02:00 — No content impact: mechanical citation re-derivation after the closeout auto-carry change shifted lines in `sync_transaction.py` / `sync_transaction_state.py`; the cited symbols and their meanings are unchanged.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of bounded pre-lock source refresh call
  sites; no local selection or mutation authority is claimed.

- 2026-08-26T02:55+02:00 — Drafted shared source-refresh onboarding; final source inventory and
  verification remain open.