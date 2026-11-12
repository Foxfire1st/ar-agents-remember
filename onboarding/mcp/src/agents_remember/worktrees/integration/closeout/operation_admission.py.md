# mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py

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

## Evidence

### Docs References

See task `260821-CLIVE-L1` L1-R2, L1-R3, L1-R5, and L1-R6.

### Repo-Internal References

- Raw admission becomes stable validated admission before authority observation. [1]
- Duplicates retain their accepted plan. [2]
- Recovery identity admits only the accepted candidate state or the exact finalized contract hash. [3]
- Currentness re-assertion for retained closeout candidates. [4]
- The door-intent currentness source. [5]
- The candidate binding field carrying the exact intent into the durable fingerprint. [6]

### Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Contract

The current source seams include `CloseoutOperationAdmission`, `CloseoutAdmissionSnapshot`, `ValidatedCloseoutAdmission`. Admission keeps normalized input, fingerprint, candidate, bases, and approval immutable for one generation. Retry reuses them; evidence-safe revision publishes one distinct successor and cannot launder changed intent into the active generation.

### Reconciled Source Evidence

- The current module exposes `CloseoutOperationAdmission`, `CloseoutAdmissionSnapshot`, `ValidatedCloseoutAdmission` at this ownership boundary. [7]

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
