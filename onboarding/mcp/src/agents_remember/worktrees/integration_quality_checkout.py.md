# mcp/src/agents_remember/worktrees/integration_quality_checkout.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration_quality_checkout.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Materializes a temporary detached checkout at the accepted candidate commit for the integration quality gate.

## Code Commentary

`integration_quality_checkout` creates an isolated temporary worktree from the exact journaled code candidate, yields it to the gate, and removes it afterward. Atomic series gates therefore test the candidate itself rather than whichever branch the repository-root checkout happens to own.

## Invariants And Boundaries

- Quality input is commit-addressed and detached from ambient checkout state.
- Temporary checkout cleanup is part of the context-manager boundary.
- This helper does not authorize or move integration refs.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The context manager creates and tears down the exact candidate checkout. | `integration_quality_checkout` | mcp/src/agents_remember/worktrees/integration_quality_checkout.py:14-33 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created exact integration quality checkout onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
