# mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns closeout-specific admission before lifecycle conflict observation. It turns raw message intent plus a lease-stable candidate into validated immutable durable input, then decides whether the request is a duplicate of an accepted generation or a legal next generation.

## Code Commentary

### Logic

Prevalidation captures contract and candidate state, resolves and normalizes the plan, then rechecks the snapshot before producing a durable candidate fingerprint. For an existing generation, the submitted request is normalized against the already accepted plan; this prevents a retry after partial mutation from changing enabledness or laundering an invalid first request. Retained generations additionally require exact recovery identity: the original or canonical finalized contract hash and the accepted candidate output.

A new generation is allowed only after the prior one is terminal and exact contract/candidate state has advanced. Active same-kind and cross-kind lifecycle compatibility is intentionally decided later, while the contract lifecycle lease is held, so malformed input cannot learn or disturb operation state.

Since 260831-CCR (commit `99dc249b`) admission binds canonical task intent into the candidate
identity and refuses legacy absence:

- `prevalidate_closeout_operation_admission` (lines 85-121) obtains the current door task intent
  (`current_door_task_intent(contract)`, line 106) and feeds it into the
  `LifecycleOperationCandidateBinding.task_intent` so the durable candidate fingerprint covers the
  exact intent bytes (line 116).
- `resolve_closeout_operation_admission` (lines 122-152) treats a missing-intent current generation
  as not resumable: once it is completed/failed/cancelled, the missing-intent branch becomes
  unreusable (lines 134-137).
- `_validate_existing_closeout_request` (lines 162-209) propagates the candidate task intent into
  the recovered candidate (lines 191-191) and the rebuilt binding (lines 205-205).
- `_current_operation_task_intent` (lines 319-330) re-asserts exact currentness, raising
  `lifecycle-operation-task-intent-stale` with `next_action=retire-and-republish` when the
  retained generation binds different intent.

### Invariants And Boundaries

- Ordering is lease-stable candidate/plan normalization, then lifecycle compatibility, then journal/worker.
- Task documents and queue projection are not input authorities.
- Duplicate validation uses the immutable accepted plan and fingerprint.
- A broad "completed" flag is insufficient to create a new generation.
- A closeout generation without canonical task intent can never be admitted or reused as current.

### Todos

None recorded.

## Docs References

See task `260821-CLIVE-L1` L1-R2, L1-R3, L1-R5, and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Raw admission becomes stable validated admission before authority observation. | `prevalidate_closeout_operation_admission` | mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py:79-115 |
| Duplicates retain their accepted plan. | `resolve_closeout_operation_admission` | mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py:122-152 |
| Recovery identity admits only the accepted candidate state or the exact finalized contract hash. | `_require_recovery_identity` | mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py:255-272 |
| Currentness re-assertion for retained closeout candidates. | `_current_operation_task_intent` | mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py:319-330 |
| The door-intent currentness source. | `current_door_task_intent` | mcp/src/agents_remember/worktrees/integration/closeout/task_intent_identity.py:70-86 |
| The candidate binding field carrying the exact intent into the durable fingerprint. | `task_intent` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py:26-37 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Contract

The current source seams include `CloseoutOperationAdmission`, `CloseoutAdmissionSnapshot`, `ValidatedCloseoutAdmission`. Admission keeps normalized input, fingerprint, candidate, bases, and approval immutable for one generation. Retry reuses them; evidence-safe revision publishes one distinct successor and cannot launder changed intent into the active generation.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `CloseoutOperationAdmission`, `CloseoutAdmissionSnapshot`, `ValidatedCloseoutAdmission` at this ownership boundary. | `CloseoutOperationAdmission`; `CloseoutAdmissionSnapshot`; `ValidatedCloseoutAdmission` | mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py:53-78 |

## 260821-CLIVE Door-Bound Admission Identity

Closeout admission no longer requires a door. `_current_door_generation_id` returns the live door's
generation id or `None`, so a fresh admission with no live door binds no generation id and the
operation's own journal supplies one once it publishes; the generation fingerprint therefore still
changes when the door changes, even if the code tree and other inputs do not. Existing-generation
replay compares the journal-retained door publication id; a projection member cannot substitute
for it.

## CCR-R02@v2 Intent-Bound Admission

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, admission binds exact current
task intent into the durable candidate identity and refuses absent/mismatched intent with the exact
stale/unavailable reason and `retire-and-republish` route. Part of the landed L25 candidate
`99dc249b`.

## Current Landed Composition

The immutable operation input includes the supplied typed corrective dispositions. Existing-generation reuse accepts the door publication only when the canonical door classifier says `published`; a matching door identifier alone is insufficient. Exact accepted input equality and recovery identity remain required.

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): every line number in this
  card was off, and the previous entry's "the cited ranges still hold" was therefore wrong —
  recorded plainly rather than quietly overwritten. Re-read the frozen source and repointed all of
  them: `prevalidate_closeout_operation_admission` 85-121 (call at 106, binding at 116),
  `resolve_closeout_operation_admission` 122-152 (unreusable branch 134-137),
  `_validate_existing_closeout_request` 162-209 (191, 205), `_require_recovery_identity` 255-272,
  `_current_operation_task_intent` 319-330, and `current_door_task_intent` at
  `task_intent_identity.py:70-86`. The claims themselves are unchanged. Verification metadata
  remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit — a fresh admission no longer requires a door and the recovery
  identity no longer admits the door-publication contract hash. Corrected the recovery-identity
  reference row and the door-bound admission section; the cited ranges still hold. Verification
  metadata remains closeout-owned.
- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=3df722ca9b22167bf059068105a0de4468d1624744fd1999f25f75eec678b33e; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): named the `task_intent` field anchor instead of the dotted attribute span.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  closeout admission now includes canonical task intent in the candidate fingerprint, refuses
  reusable/missing-intent generations, and re-asserts currentness on retained candidates
  (`_current_operation_task_intent`). Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: added the exact door-generation component of operation admission identity. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; verification metadata is deliberately unstamped.
