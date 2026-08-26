# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree-integration overview](../overview.md)

## Purpose

Owns journal-retained closeout-door publication intent/proof and the resulting disposable-projection
refresh effects for lifecycle operations.

## Code Commentary

Only closeout and direct-landing records may carry door intent. An unfinished intent must settle
before another is accepted. Publication re-reads configured authority under the task-publication
lock; the journal retains the accepted proof before downstream projections are refreshed.

## Invariants And Boundaries

- Door intent/proof survives queue invalidation and enclosure-local retries.
- Projection refresh is downstream and may not weaken accepted canonical publication.
- No second evidence reader or successor-intent compatibility WAL is permitted.

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-door owner relocation to `integration.closeout.door`; journal-owned publication and projection refresh semantics are unchanged.
- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final journal-door control owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
