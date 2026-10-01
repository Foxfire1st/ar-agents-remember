# mcp/src/agents_remember/serving/inbox_delivery.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Delivers one persisted inbox row through the hosted adapter and records correlated acceptance. It
re-resolves ordinary structural addresses to the current occupant immediately before delivery.

## Code Commentary

The availability gate is enforced by `messageKind`: every state-signal waits for a turn boundary even if the caller did not request boundary gating. A correlated adapter acceptance at that boundary may land the row; queued acknowledgement alone cannot. Redelivery of an already-correlated request reconciles its existing identity without sending the message again. cit:([`_delivery_refusal`; `_redelivery`; `_record_receipt`], mcp/src/agents_remember/serving/inbox_delivery.py:113-168; mcp/src/agents_remember/serving/inbox_delivery.py:232-255; mcp/src/agents_remember/serving/inbox_delivery.py:265-291).

### Logic

`target_session_for_entry` exact-pins only dispatch briefs; ordinary task-document-and-role rows use
`_structural_target`, which delegates incumbent/staged-heir choice and ambiguity refusal to the
shared `current_seat_occupant` selector. Delivery
submits the whole message once with the durable entry id as request correlation. Accepted delivery at
a turn boundary records formal landing; queued/busy delivery remains pending on its durable schedule.

### Conventions

Adapter receipt and reconciliation are acknowledgement authority. Terminal paste is not used as a
fallback for protocol delivery.

### Invariants And Boundaries

- Persistence happens before this module runs.
- Ordinary messages are replacement-aware at delivery time.
- One row is one whole-message boundary.
- Model completion/consume cannot acknowledge or trigger a second wake.
- Delivery does not own a duplicate replacement-selection algorithm.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Delivery records adapter acceptance and boundary-aware landing. [1]
- Structural delivery target selection consumes the one canonical seat selector. [2]
- Dispatch brief is the sole exact-pinned targeting exception. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
