# mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Owns closeout-specific admission before lifecycle conflict observation. It turns raw message intent plus a lease-stable candidate into validated immutable durable input, then decides whether the request is a duplicate of an accepted generation or a legal next generation.

## Code Commentary

### Logic

Prevalidation captures contract and candidate state, resolves and normalizes the plan, then rechecks the snapshot before producing a durable candidate fingerprint. For an existing generation, the submitted request is normalized against the already accepted plan; this prevents a retry after partial mutation from changing enabledness or laundering an invalid first request. Retained generations additionally require exact recovery identity: the original or canonical finalized contract hash and the accepted candidate output.

A new generation is allowed only after the prior one is terminal and exact contract/candidate state has advanced. Active same-kind and cross-kind lifecycle compatibility is intentionally decided later, while the contract lifecycle lease is held, so malformed input cannot learn or disturb operation state.

### Invariants And Boundaries

- Ordering is lease-stable candidate/plan normalization, then lifecycle compatibility, then journal/worker.
- Task documents and queue projection are not input authorities.
- Duplicate validation uses the immutable accepted plan and fingerprint.
- A broad “completed” flag is insufficient to create a new generation.

### Todos

Public retry/recover/revise commands and broader liveness controls are L2.

## Docs References

See task `260821-CLIVE-L1` L1-R2, L1-R3, L1-R5, and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Raw admission becomes stable validated admission before authority observation. | `prevalidate_closeout_operation_admission` | mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py:70-100 |
| Duplicates retain their accepted plan. | `resolve_closeout_operation_admission` | mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py:103-116 |
| Recovery identity admits only original or exact finalized publication. | `_require_recovery_identity` | mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py:219-236 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Contract

The current source seams include `CloseoutOperationAdmission`, `CloseoutAdmissionSnapshot`, `ValidatedCloseoutAdmission`. Admission keeps normalized input, fingerprint, candidate, bases, and approval immutable for one generation. Retry reuses them; evidence-safe revision publishes one distinct successor and cannot launder changed intent into the active generation.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `CloseoutOperationAdmission`, `CloseoutAdmissionSnapshot`, `ValidatedCloseoutAdmission` at this ownership boundary. | `CloseoutOperationAdmission`; `CloseoutAdmissionSnapshot`; `ValidatedCloseoutAdmission` | mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py:45-68 |

## 260821-CLIVE Door-Bound Admission Identity

Closeout admission now requires a door and binds the exact door generation id through
`LifecycleOperationCandidateBinding`. The generation fingerprint therefore changes when the door
changes even if code tree and other inputs do not. Existing-generation replay compares the
journal-retained door publication id; a projection member cannot substitute for it.

## Update History

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: added the exact door-generation component of operation admission identity. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; verification metadata is deliberately unstamped.
