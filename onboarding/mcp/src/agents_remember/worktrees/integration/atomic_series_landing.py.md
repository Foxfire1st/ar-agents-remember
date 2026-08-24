# mcp/src/agents_remember/worktrees/integration/atomic_series_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/atomic_series_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktree-integration overview](overview.md)

## Purpose

Enforces canonical protected-ref exclusion across active atomic series at landing time.

## Code Commentary

`require_atomic_landing_authority` compares repository identity and protected branch for both code
and external memory across nonterminal canonical series. A distinct series that owns an
intersecting target blocks landing. Present-but-unreadable, non-regular, or invalid series
authority fails closed.

## Invariants And Boundaries

- This is a current-authority check, not a persistent queue blocker.
- No judgment-controlled release or abort state is created.
- Code and external-memory protected targets are compared independently and exactly.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Atomic landing exclusion is computed from canonical active-series authority. | `require_atomic_landing_authority` | `mcp/src/agents_remember/worktrees/integration/atomic_series_landing.py` |

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final landing-authority owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
