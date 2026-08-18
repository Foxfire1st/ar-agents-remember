# mcp/src/agents_remember/worktrees/integration_quality_checkout.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration_quality_checkout.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b` |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Materializes a temporary detached checkout at the accepted candidate commit for the integration quality gate.

## Code Commentary

`integration_quality_checkout` now accepts an optional `commit`; a leaf with no commit reuses the ordinary worktree, while a pinned commit yields a detached exact-candidate checkout.

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

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: the detached checkout now accepts an explicit `commit` for the exact final candidate rather than only ambient branch state. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created exact integration quality checkout onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
