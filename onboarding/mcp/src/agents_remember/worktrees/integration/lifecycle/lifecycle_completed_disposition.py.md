# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_completed_disposition.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_completed_disposition.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[integration overview](../overview.md)

## Purpose

Owns fail-closed authorization for retiring or superseding a completed, still-unintegrated closeout generation.

## Code Commentary

### Logic

`require_completed_disposition` first refuses while an accepted integration journal claim remains active. It then requires the exact active closeout generation, retained evidence, the finalized contract hash, completed closeout status, unintegrated contract state, and a cleared worker PID.

### Conventions

Refusals use typed `LifecycleControlError` codes and advertise recovery or cancellation rather than mutating evidence optimistically.

### Invariants And Boundaries

- A completed generation is not disposable while integration owns a live claim.
- Retire/supersede requires exact generation ownership and proven worker exit.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this lifecycle authority rule.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Active integration publication blocks disposition and returns exact recovery arguments. | L29-L57 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_completed_disposition.py` |
| Completed disposition requires retained exact ownership, unintegrated state, and no authoritative worker PID. | L58-L84 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_completed_disposition.py` |

## Cross-Repo References

No cross-repository boundary is owned here.

## 260821-CLIVE Exact Completed-Door Ownership

Retire and supersede are permitted only for the exact completed, unintegrated door owner. Direct
landing is included when its proven claimed door exactly equals the contract. Completion by itself
is insufficient: the active generation, retained output, integration state, and door ownership must
all agree.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented exact claimed-door ownership for completed disposition. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the missing strict sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.
