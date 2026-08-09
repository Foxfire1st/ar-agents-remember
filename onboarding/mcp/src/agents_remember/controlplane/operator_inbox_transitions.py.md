# mcp/src/agents_remember/controlplane/operator_inbox_transitions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/operator_inbox_transitions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T06:48+02:00 |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840` |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

What one inbox row's next snapshot says: the policy over the operator inbox log.

## Code Commentary

### Logic

Module-level surface:

- `AdapterReceipt` (class, lines 55-64) — What the vendor adapter reported about one delivery attempt: the state it returned, the request it acknowledged, the vendor's own correlation id, when it accepted the payload, and any detail.
- `DeliveryAttempt` (class, lines 68-78) — One attempt to put a pending row in front of its addressee: the outcome, the session it was pasted into, the human-readable detail, the adapter's receipt, and `landed` — whether the target seat was at a turn boundary when the attempt happened (the N16 gate).
- `InboxRenewal` (class, lines 80-87) — What a re-firing condition refreshes on the one row it already has: the response text, the subject the row now concerns, and -- when the routed owner has moved on -- the owner to readdress it to.
- `RedeliveryFloor` (class, lines 91-100) — The rate limit on re-recording a delivery, and the row snapshot it is measured against.
- `AdapterCompletion` (class, lines 104-110) — The terminal evidence a vendor adapter reported for one row: the vendor's own correlation id and whatever detail came with the terminal result.
- `RungAdvance` (class, lines 114-123) — The ladder rung to stamp and, when that rung re-addresses, the owner the row moves to.
- `ExpiryOptions` (class, lines 128-133) — Why a row expires (`reason`) and, optionally, the inspection mailbox (`readdress_to`) the terminal marker moves to (the N3 architect mailbox of last resort).
- `_readdress_fields` (function, lines 132-141) — Move a row's delivery address onto ``owner`` and record it as the routed owner.
- `_require_entry` (function, lines 144-156) — The row ``entry_id`` names, from the supplied fold or a fresh one.
- `_delivery_evidence_update` (function, lines 205-224) — The delivery-evidence half of one attempt snapshot (delivery state, adapter receipt, attempt count, timestamps), shared by landed and non-landed writes.
- `record_delivery` (function, lines 160-203) — Append a delivery-status snapshot for one pending entry. A correlated ``accepted`` receipt while the target was at a turn boundary (``attempt.landed``) writes the formal ``landed`` terminal state through a lock-held latest-fold transition and clears ``nextAttemptAt``; everything else keeps the durable backoff schedule. A concurrent terminal write wins and the stale landing appends nothing (F1).
- `mark_landed` (function, lines 226-244) — Fold a legacy by-rule landing into the formal ``landed`` state exactly once (N13 migration).
- `mark_superseded` (function, lines 246-271) — Explicitly terminate one overtaken command ``superseded`` without a false ack (R11); always explicit, never inferred from artifacts/branches/task state.
- `mark_unresolved` (function, lines 273-297) — Terminally resolve a row whose delivery attempts hit the ceiling (N3), delivery evidence intact.
- `mark_expired` (function, lines 299-327) — Terminally resolve a row by an expiry clock (rebind grace or retention TTL); ``readdress_to`` optionally moves the marker to an inspection mailbox.
- `rebind_entry` (function, lines 329-357) — Sweep-time rebind (N14): move a pending row onto its current qualified owner, clearing per-attempt adapter correlation and resetting the attempt clock.
- `record_adapter_completion` (function, lines 212-234) — Persist terminal adapter evidence without consuming the durable inbox row.
- `mark_escalated` (function, lines 237-252) — Stamp ``escalatedAt`` once the ladder (HFX2-L4) escalates an unacked row.
- `advance_rung` (function, lines 255-285) — Stamp the ladder's next rung (260707-HFX2-L4, R1/R2): re-anchors ``escalatedAt`` to ``now`` so the NEXT rung's SLA is measured from this transition, not the row's original creation.
- `renew` (function, lines 288-316) — Refresh one still-pending row in place: same id, bumped ``ts``, optionally refreshed ``response``.
- `mark_ladder_resolved` (function, lines 319-341) — Terminally resolve a ladder-complete row without treating it as an ack.

**260713-TES-L4 (N13/N16/F1):** the four `mark_*` terminal transitions and the landed branch of
`record_delivery` are lock-held latest-fold operations (`store.transition`): they re-read and
re-fold under the store lock, refuse any latest state other than `pending`, and append nothing
when the transition returns the same snapshot. Terminal states are not interchangeable (landed
vs superseded vs unresolved vs expired), so a stale sweep snapshot can never overwrite a
concurrent terminal write. `rebind_entry` clears the dead seat's adapter correlation and resets
`attemptCount`/`nextAttemptAt` so the replacement starts a fresh delivery schedule. The ladder
transitions (`mark_escalated`/`advance_rung`/`mark_ladder_resolved`) remain for the dormant
escalation ladder, which L5 deletes; the sweep no longer drives it (N3).

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `AdapterReceipt` (lines 55-64) — What the vendor adapter reported about one delivery attempt: the state it returned, the request it acknowledged, the vendor's own correlation id, when it accepted the payload, and any detail. | `AdapterReceipt` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:54-64 |
| Defines the class `DeliveryAttempt` (lines 68-76) — One attempt to put a pending row in front of its addressee: the outcome, the session it was pasted into, the human-readable detail, and the adapter's receipt for the same attempt. | `DeliveryAttempt` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:67-76 |
| Defines the class `InboxRenewal` (lines 80-87) — What a re-firing condition refreshes on the one row it already has: the response text, the subject the row now concerns, and -- when the routed owner has moved on -- the owner to readdress it to. | `InboxRenewal` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:79-87 |
| Defines the class `RedeliveryFloor` (lines 91-100) — The rate limit on re-recording a delivery, and the row snapshot it is measured against.. | `RedeliveryFloor` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:90-100 |
| Defines the class `AdapterCompletion` (lines 104-110) — The terminal evidence a vendor adapter reported for one row: the vendor's own correlation id and whatever detail came with the terminal result. | `AdapterCompletion` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:103-110 |
| Defines the class `RungAdvance` (lines 114-123) — The ladder rung to stamp and, when that rung re-addresses, the owner the row moves to.. | `RungAdvance` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:113-123 |
| Defines the function `_readdress_fields` (lines 132-141) — Move a row's delivery address onto ``owner`` and record it as the routed owner.. | `_readdress_fields` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:145-154 |
| Defines the function `_require_entry` (lines 144-156) — The row ``entry_id`` names, from the supplied fold or a fresh one.. | `_require_entry` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:157-169 |
| Defines the function `record_delivery` (lines 159-209) — Append a delivery-status snapshot for one pending entry.. | `record_delivery` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:159-209 |
| Defines the function `record_adapter_completion` (lines 212-234) — Persist terminal adapter evidence without consuming the durable inbox row.. | `record_adapter_completion` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:409-431 |
| Defines the function `mark_escalated` (lines 237-252) — Stamp ``escalatedAt`` once the ladder (HFX2-L4) escalates an unacked row.. | `mark_escalated` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:434-449 |
| Defines the function `advance_rung` (lines 255-285) — Stamp the ladder's next rung (260707-HFX2-L4, R1/R2): re-anchors ``escalatedAt`` to ``now`` so the NEXT rung's SLA is measured from this transition, not the row's original creation. | `advance_rung` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:452-482 |
| Defines the function `renew` (lines 288-316) — Refresh one still-pending row in place: same id, bumped ``ts``, optionally refreshed ``response``. | `renew` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:485-513 |
| Defines the function `mark_ladder_resolved` (lines 319-341) — Terminally resolve a ladder-complete row without treating it as an ack.. | `mark_ladder_resolved` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:516-538 |

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the formal terminal vocabulary
  transitions — `DeliveryAttempt.landed` (boundary gate), `record_delivery`'s landed branch,
  `mark_landed`/`mark_superseded`/`mark_unresolved`/`mark_expired` as lock-held latest-fold
  transitions, `ExpiryOptions` (reason + optional architect-mailbox readdress), `rebind_entry`
  (N14: clears adapter correlation, resets attempt clock), and `_delivery_evidence_update`.
  Noted the dormant-ladder posture (N3): the ladder transitions remain but the sweep no longer
  drives them; L5 deletes the module. Verification metadata pinned until closeout stamps the
  260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded `record_delivery`'s landed
  state-signal handling — `nextAttemptAt=None` when `state_signal_landed` holds after the
  attempt (terminal on the relay path, no backoff reschedule). Verification metadata pinned
  until closeout stamps the 260713-TES-L2 commit.
- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: completed truncated docstring summaries for adapter receipts, deliveries, renewals, and ladder-rung transitions against the frozen source; normalized decorator-inclusive citation ranges via scoped --fix.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
