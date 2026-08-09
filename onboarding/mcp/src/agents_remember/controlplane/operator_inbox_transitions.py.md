# mcp/src/agents_remember/controlplane/operator_inbox_transitions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/operator_inbox_transitions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T01:21+02:00 |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484` |
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

What one inbox row's next snapshot says: the policy over the operator inbox log.

## Code Commentary

### Logic

Module-level surface:

- `AdapterReceipt` (class, lines 55-64) — What the vendor adapter reported about one delivery attempt: the state it returned, the request it acknowledged, the vendor's own correlation id, when it accepted the payload, and any detail.
- `DeliveryAttempt` (class, lines 68-76) — One attempt to put a pending row in front of its addressee: the outcome, the session it was pasted into, the human-readable detail, and the adapter's receipt for the same attempt.
- `InboxRenewal` (class, lines 80-87) — What a re-firing condition refreshes on the one row it already has: the response text, the subject the row now concerns, and -- when the routed owner has moved on -- the owner to readdress it to.
- `RedeliveryFloor` (class, lines 91-100) — The rate limit on re-recording a delivery, and the row snapshot it is measured against.
- `AdapterCompletion` (class, lines 104-110) — The terminal evidence a vendor adapter reported for one row: the vendor's own correlation id and whatever detail came with the terminal result.
- `RungAdvance` (class, lines 114-123) — The ladder rung to stamp and, when that rung re-addresses, the owner the row moves to.
- `_readdress_fields` (function, lines 132-141) — Move a row's delivery address onto ``owner`` and record it as the routed owner.
- `_require_entry` (function, lines 144-156) — The row ``entry_id`` names, from the supplied fold or a fresh one.
- `record_delivery` (function, lines 160-214) — Append a delivery-status snapshot for one pending entry; a state-signal row that lands (delivered+accepted at a boundary) gets `nextAttemptAt=None` so no further attempt is scheduled.
- `record_adapter_completion` (function, lines 212-234) — Persist terminal adapter evidence without consuming the durable inbox row.
- `mark_escalated` (function, lines 237-252) — Stamp ``escalatedAt`` once the ladder (HFX2-L4) escalates an unacked row.
- `advance_rung` (function, lines 255-285) — Stamp the ladder's next rung (260707-HFX2-L4, R1/R2): re-anchors ``escalatedAt`` to ``now`` so the NEXT rung's SLA is measured from this transition, not the row's original creation.
- `renew` (function, lines 288-316) — Refresh one still-pending row in place: same id, bumped ``ts``, optionally refreshed ``response``.
- `mark_ladder_resolved` (function, lines 319-341) — Terminally resolve a ladder-complete row without treating it as an ack.

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
| Defines the function `_readdress_fields` (lines 132-141) — Move a row's delivery address onto ``owner`` and record it as the routed owner.. | `_readdress_fields` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:132-141 |
| Defines the function `_require_entry` (lines 144-156) — The row ``entry_id`` names, from the supplied fold or a fresh one.. | `_require_entry` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:144-156 |
| Defines the function `record_delivery` (lines 159-209) — Append a delivery-status snapshot for one pending entry.. | `record_delivery` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:159-209 |
| Defines the function `record_adapter_completion` (lines 212-234) — Persist terminal adapter evidence without consuming the durable inbox row.. | `record_adapter_completion` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:212-234 |
| Defines the function `mark_escalated` (lines 237-252) — Stamp ``escalatedAt`` once the ladder (HFX2-L4) escalates an unacked row.. | `mark_escalated` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:237-252 |
| Defines the function `advance_rung` (lines 255-285) — Stamp the ladder's next rung (260707-HFX2-L4, R1/R2): re-anchors ``escalatedAt`` to ``now`` so the NEXT rung's SLA is measured from this transition, not the row's original creation. | `advance_rung` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:255-285 |
| Defines the function `renew` (lines 288-316) — Refresh one still-pending row in place: same id, bumped ``ts``, optionally refreshed ``response``. | `renew` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:288-316 |
| Defines the function `mark_ladder_resolved` (lines 319-341) — Terminally resolve a ladder-complete row without treating it as an ack.. | `mark_ladder_resolved` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:319-341 |

## Update History

- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded `record_delivery`'s landed
  state-signal handling — `nextAttemptAt=None` when `state_signal_landed` holds after the
  attempt (terminal on the relay path, no backoff reschedule). Verification metadata pinned
  until closeout stamps the 260713-TES-L2 commit.
- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: completed truncated docstring summaries for adapter receipts, deliveries, renewals, and ladder-rung transitions against the frozen source; normalized decorator-inclusive citation ranges via scoped --fix.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
