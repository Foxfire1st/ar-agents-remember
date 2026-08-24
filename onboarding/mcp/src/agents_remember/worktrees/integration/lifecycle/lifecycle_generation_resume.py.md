# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_generation_resume.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_generation_resume.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[integration overview](../overview.md)

## Purpose

Owns the pure same-generation transition used to retry or recover retained lifecycle intent.

## Code Commentary

### Logic

`requeued_same_generation` requires any current worker-termination record to prove exit, archives that proof, and resets only `reconciled-unchanged` mutation legs to `pre-mutation` while retaining their history. It increments the attempt, clears transient failure/cancellation state, and returns direct landing to running or other operations to queued.

### Conventions

Resume copies the validated record; it does not create a successor generation or replace immutable accepted input.

### Invariants And Boundaries

- Unproven worker termination blocks resume.
- Commit-proven evidence is never reset.
- Same-generation recovery preserves prior mutation and termination history.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this pure transition.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Resume requires exited worker proof and archives it. | L11-L22 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_generation_resume.py` |
| Only unchanged mutation evidence is reset; attempt and transient execution state advance within the same record. | L23-L50 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_generation_resume.py` |

## Cross-Repo References

No cross-repository boundary is owned here.

## 260821-CLIVE Same-Generation Claim Recovery

A retained closeout claim resumes the same generation in `recovering-after-claim`; it does not
return to generic queued state or create a successor. Leg-specific mutation evidence is reset only
according to the existing recovery rules. Claim identity remains the exact journaled door and
operation generation.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: clarified same-generation recovery for retained closeout claims. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the missing strict sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.
