# mcp/src/agents_remember/controlplane/operator_inbox_transitions.py

## Governing Overview

[overview](overview.md)

## Purpose

Owns pure next-snapshot policy for durable inbox rows, including accepted-at-boundary landing,
redelivery scheduling, explicit terminal states, and structural owner rebinding.

## Code Commentary

L23 extracts `expiry_transition` as a pure transition factory shared by single-row expiry and batch notifier writes; the transition still changes only pending rows.

### Logic

`record_delivery` records adapter evidence and writes `landed` only when correlated acceptance
occurs at a target turn boundary. Otherwise the pending row receives restart-durable backoff.
`rebind_entry` atomically rewrites both address and routed owner to the current qualified
task-document-and-role seat.

### Conventions

The adjacent store owns locks and appends; transition functions compute policy from a folded row.

### Invariants And Boundaries

- Delivered outside a turn boundary is evidence, not terminality.
- Rebinding changes current occupant correlation while preserving message identity.
- A stale delivery cannot reverse an existing terminal transition.
- No transition depends on model-authored consume.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Delivery records terminal landing only on accepted boundary delivery. [1]
- Explicit landing remains idempotent and terminal. [2]
- Sweep-time rebinding rewrites address and owner together. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
