# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00|
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
| Legacy missing-intent generation archive + successor write. | `_retire_missing_intent_generation` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:638-668 |
| The write-side identity requirement for closeout/direct-landing records. | `_write` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py:676-689 |

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

## CCR-R18@v1 Monotonic Record-Revision Discipline

260831-CCR-L18 made the durable journal revision monotonic and store-owned. `_validate_identity_and_evidence_transition` now refuses any mutation whose `recordRevision` is not exactly `current.recordRevision + 1` (line 316), and `_advance_record_revision` (line 361) is the one canonical writer boundary that assigns the next revision — a transform may not assign one itself. Every accepted `update`/`mutate`/`create`-adjacent write path goes through it, and a transform that leaves the record byte-identical short-circuits as a no-op instead of burning a revision.

`create` refuses any record that does not begin at revision 1 (line 552), and `resume_generation` revalidates the resume contract (attempt increment exactly once, sanctioned status/phase, disposition identity) before any no-op short-circuit. `publish_successor_generation` advances the archived predecessor by one revision while the successor begins at `current.recordRevision + (1 if the current closeout/direct-landing generation is missing task intent else 2)` (lines 648-672), so retire/supersede journal arithmetic is explicit and exact.

## Update History

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the store-owned monotonic `recordRevision` advance (exactly once per accepted mutation, no-op short-circuit, revision-1 creation gate, successor +1/+2 arithmetic). Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the lifecycle operation store now includes `taskIntent` in generation identity, refuses
  intent-less closeout/direct-landing writes, and archives + replaces legacy missing-intent
  generations via `_retire_missing_intent_generation`. Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
