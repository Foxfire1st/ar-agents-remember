# mcp/src/agents_remember/controlplane/operator_inbox_records.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Defines the append-only operator-inbox record and its structural address, routed owner, subject, and
delivery evidence. Task-document plus role is stable; exact agent/lifecycle/session fields are
private correlations.

## Code Commentary

### Logic

`InboxRouting` couples the current delivery address with its derived owner. `InboxSubject`
records what seat a message concerns. `OperatorInboxEntry` persists both structural fields and
adapter evidence; folding never lets a later stale pending snapshot reverse a terminal row.
`consume_operator_inbox_entry` is attribution only and does not drive delivery or terminality.

### Conventions

Whole ask/response messages are one durable row. Landed truth comes from correlated adapter
acceptance at a turn boundary.

### Invariants And Boundaries

- Ordinary messages remain structurally addressable across replacement.
- Dispatch brief is the only internally exact-pinned message kind.
- Model consume is optional attribution, not acknowledgement authority.
- Persistence precedes delivery attempts.

### Todos

Named legacy escalation fields remain parse-only until their durability schema is migrated.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Address, owner, subject, and message are explicit value objects. [1]
- The durable row separates structural identity from delivery correlations. [2]
- Consume preserves state and only stamps attribution. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
