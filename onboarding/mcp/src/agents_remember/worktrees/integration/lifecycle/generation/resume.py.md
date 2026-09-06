# mcp/src/agents_remember/worktrees/integration/lifecycle/generation/resume.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/generation/resume.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:03:08+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Generation overview](overview.md)

## Purpose

Owns the pure same-generation transition used to retry or recover retained lifecycle intent.

## Code Commentary

### Logic

`requeued_same_generation` requires any current worker-termination record to prove exit, archives that proof, and resets only `reconciled-unchanged` mutation legs to `pre-mutation` while retaining their history. It increments the attempt and clears transient failure/cancellation state. Direct landing receives status `running` and phase `direct-preflight`; other operations receive status `queued`. A retained closeout claim keeps phase `recovering-after-claim`, while other queued operations receive phase `queued`.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Resume requires exited worker proof and archives it. | `requeued_same_generation` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/resume.py:14-63 |
| Only unchanged mutation evidence is reset; attempt and transient execution state advance within the same record. | `requeued_same_generation` | mcp/src/agents_remember/worktrees/integration/lifecycle/generation/resume.py:14-63 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |

## 260821-CLIVE Same-Generation Claim Recovery

A retained closeout claim resumes the same generation in `recovering-after-claim`; it does not
return to generic `queued` phase or create a successor; its status is still `queued`. Leg-specific mutation evidence is reset only
according to the existing recovery rules. Claim identity remains the exact journaled door and
operation generation.

## Update History

- 2026-09-06T15:03:08+00:00 — Added explicit not-applicable Docs/Cross-Repo reference rows required by the file-card template; source claims, verification stamps and all earlier history are unchanged.


- 2026-09-06T14:57:32+00:00 — Independent source review clarified that retained closeout recovery has queued status with recovering-after-claim phase. The same-generation behavior and all prior history remain preserved.

- 2026-09-06T14:48:58+00:00 — Moved the existing resume card with all prior history and CLIVE claim-recovery knowledge to the exact source owner at `c69d5171187fa1957025e393270db9f5a864ab14`; the source AST and transition behavior are unchanged. Source verification does not assert execution or acceptance.


- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout recovery-projection package relocation; retained same-generation resume behavior is unchanged.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: clarified same-generation recovery for retained closeout claims. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the missing strict sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.
