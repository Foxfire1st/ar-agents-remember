# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Lifecycle operation integration overview](overview.md)

## Purpose

Provides strict atomic enclosure-local storage and transition validation for long lifecycle operations.

## Code Commentary

### Logic

It validates immutable identity, worker authority, mutation, door, quality, publication, recovery, repair, migration, and finalization transitions under exclusive access.

Since 260831-CCR (commit `99dc249b`) the store makes canonical task intent part of the durable
generation contract and preserves legacy bytes on retirement:

- `_validate_identity_and_evidence_transition` includes `taskIntent` in the compared identity
  field set (line 326), so an intent change is a distinct successor, not a silent replay.
- `_retire_missing_intent_generation` (line 638-668) is the legacy cutover: when the current
  closeout/direct-landing generation lacks intent (line 625-628) and a successor is being applied,
  the store preserves the exact legacy bytes to
  `{stem}.legacy-missing-intent-generation-{generation}.json` (atomic, idempotent, contradiction-
  checked, rolled back on write failure) and then publishes the validated intent-bound successor —
  so a legacy record stays readable but is replaced by one canonical generation.
- `_write` refuses any closeout/direct-landing record whose `taskIntent` is not a canonical
  identity (line 681-689), translating `TaskIntentError` into a loud `RuntimeError`; writers
  cannot emit the sentinel.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The current `_validate_private_preparation_transition` boundary implements the preparation contract above. | "def _validate_private_preparation_transition" | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:398-444 |

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `_OWNERSHIP` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:1-710 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `_OWNERSHIP` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:1-710 |
| Task intent joins the compared generation identity. | `_validate_identity_and_evidence_transition` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:310-355 |
| Legacy missing-intent generation archive + successor write. | `_retire_missing_intent_generation` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:822-849 |
| The write-side identity requirement for closeout/direct-landing records. | `_write` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:740-758 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_OWNERSHIP` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:1-710 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Exactly-once cursor validation on the meaningful subset. | `_validate_identity_and_evidence_transition` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:311-340 |
| Both revisions assigned at the canonical writer boundary. | `_advance_record_revision` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:447-470 |
| The canonical journal writer increments recordRevision on every write and meaningfulRevision only for meaningful state changes. | "def _advance_record_revision" | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:447-470 |
| A terminal successor archives its exact predecessor before publishing the next generation. | "def replace_terminal" | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:755-820 |
| The shared meaningful-change comparison. | `meaningful_state_changed` | mcp/src/agents_remember/models/lifecycles/operation.py:559-565 |

## Update History

- 2026-09-07 — Reconciled the preparation contract introduced by 245057 against surviving d361 source; retained prior history and verification pins.

- 2026-09-06T22:41:21+00:00: Generated citation repair: `_retire_missing_intent_generation` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:822-849. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `_advance_record_revision` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:447-470. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `meaningful_state_changed` repointed to mcp/src/agents_remember/models/lifecycles/operation.py:559-565. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-05T07:19:22+00:00 — L31-MR-02 history recovery: restored the original dated L18 entry verbatim from memory commit fd41221f11dfe5ac2993520c0d7176ada59ce2ba (its recorded code provenance: f93ac631ca161e5880db3a937728cb256686b13b). This preserves sibling curation history; current body and verification metadata are unchanged.


- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `_retire_missing_intent_generation` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:702-729. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `_write` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:740-758. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the store's dual-revision advance rules (`recordRevision` every write, `meaningfulRevision` exactly once per meaningful state change) and the successor/supersede cursor bumps.
- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the store-owned monotonic `recordRevision` advance (exactly once per accepted mutation, no-op short-circuit, revision-1 creation gate, successor +1/+2 arithmetic). Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the lifecycle operation store now includes `taskIntent` in generation identity, refuses
  intent-less closeout/direct-landing writes, and archives + replaces legacy missing-intent
  generations via `_retire_missing_intent_generation`. Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
