# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Provides strict atomic enclosure-local storage and transition validation for long lifecycle operations.

## Code Commentary

### Logic

Recovery-cell monotonicity now protects only `codeCommit` and `memoryContentCommit`. The store has no immutable direct-ledger intent transition; immutable task/operation identity, exact mutation evidence, private preparation, publication proof, and record revisions remain the durable validation boundary.

It validates immutable identity, worker authority, mutation, door, quality, publication, recovery, repair, migration, and finalization transitions under exclusive access.

Since 260831-CCR (commit `99dc249b`) the store makes canonical task intent part of the durable
generation contract and preserves legacy bytes on retirement:

- `_validate_identity_and_evidence_transition` includes `taskIntent` in the compared identity
  field set, so an intent change is a distinct successor, not a silent replay.
- `_retire_missing_intent_generation` is the legacy cutover: when the current
  closeout/direct-landing generation lacks intent and a successor is being applied,
  the store preserves the exact legacy bytes to
  `{stem}.legacy-missing-intent-generation-{generation}.json` (atomic, idempotent, contradiction-
  checked, rolled back on write failure) and then publishes the validated intent-bound successor —
  so a legacy record stays readable but is replaced by one canonical generation.
- `_write` refuses any closeout/direct-landing record whose `taskIntent` is not a canonical
  identity, translating `TaskIntentError` into a loud `RuntimeError`; writers
  cannot emit the sentinel.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

#### Invariants And Boundaries

- Updates are monotonic and generation-bound; evidence cannot disappear or change identity; invalid/corrupt records raise the shared read/schema failure API.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- Legacy missing-intent bytes are archived verbatim before any intent-bound successor is written;
  the archive is the only retained copy of the old generation.
- No new or republished lifecycle record may carry the missing-intent sentinel.

### Todos

None recorded.

### CCR private preparation boundary

Private preparation is selected after generation creation, never injected into a new record. Starting a private command requires the same fully identified active running worker, no cancellation and a validated preparation transition. A preparation update cannot simultaneously publish mutation/history/recovery tuples, consume approval, enter the irreversible boundary or finalize the contract. Retained preparation blocks retirement/supersession or terminal replacement without an explicit proved disposition; completed status requires finalization proof, and cancellation requires unchanged logical-ref evidence.

- The current `_validate_private_preparation_transition` boundary implements the preparation contract above. [1]

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `_validate_recovery_commits_transition` prevents proven code/memory recovery commits from disappearing or changing. [2]
- `_validate_identity_and_evidence_transition` preserves generation identity and monotonic mutation/publication state. [3]

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- Task intent joins the compared generation identity. (`_validate_identity_and_evidence_transition`) [4]
- Legacy missing-intent generation archive + successor write. (`_retire_missing_intent_generation`) [5]
- The write-side identity requirement for closeout/direct-landing records. (`_write`) [6]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No additional cross-repository evidence applies.

## CCR-R02@v2 Legacy Retirement In The Store

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, a legacy container with
`missing-intent` remains readable only so its owner can report the exact stale/unavailable state
and republish. The store's `_retire_missing_intent_generation` preserves the exact legacy bytes and
publishes one canonical intent-bound successor generation; the enclosed archive is then owned,
adopted, and terminally archived by the related enclosure/archive seams. Part of the landed L25
candidate `99dc249b`.


## 260831-CCR-L15 Meaningful Revision Advance Rules

The store now advances two monotonic revisions at the one canonical journal writer boundary:
`recordRevision` advances on every durable write, while the CCR-R15
`meaningfulRevision` advances only when the meaningful projection subset changed.
`_validate_identity_and_evidence_transition` asserts the exact rule
(`updated.meaningfulRevision == current.meaningfulRevision + int(meaningful_state_changed(
current, updated))`) and refuses a transform that advances the cursor on
heartbeat/current-command/log/history writes; `_advance_record_revision` assigns both
revisions after validation and refuses transforms that pre-assign either. The successor and
supersede writers bump `meaningfulRevision` alongside the generation/record-revision
advance, so a successor is always visible to an old-generation waiter.

- Exactly-once cursor validation on the meaningful subset. (`_validate_identity_and_evidence_transition`) [7]
- Both revisions assigned at the canonical writer boundary. (`_advance_record_revision`) [8]
- The canonical journal writer increments recordRevision on every write and meaningfulRevision only for meaningful state changes. (`_advance_record_revision`) [9]
- A terminal successor archives its exact predecessor before publishing the next generation. (`replace_terminal`) [10]
- The shared meaningful-change comparison. (`meaningful_state_changed`) [11]
