# mcp/src/agents_remember/controlplane/seats.py

## Governing Overview

[overview](overview.md)

## Purpose

What the control plane needs to know about a seat, declared by the control plane.

## Code Commentary

### Logic

Named command-seat classification includes architect, orchestrator, and manager as roles whose
identity must be structurally qualified. `SeatRow` exposes primary, replacement, and binding
identity as `TaskDocumentRef`; it does not expose leaf or sprint keys. It also exposes the optional
reviewer structural-parent document+role pair required by routing and retirement consumers. This
classification remains separate from
notifier subordinate membership: wake supervision uses direct manager spawn topology and therefore
admits reviewer, curator, and future subordinate role names without changing this finite set.

ARSPAWN-L2 adds the shared `current_seat_occupant` selector. It validates primary and staged-heir
cardinality independently, prefers one incumbent while present, and promotes the staged heir only
after the incumbent leaves. Duplicate claimants raise `SeatOccupancyError`; consumers may translate
or locally suppress that ambiguity, but may never choose the first row.

Module-level surface:

- `SeatRow` (class, lines 36-90) — One seat's row, as the control plane reads it.
- `SeatDirectory` (class, lines 93-106) — The seat catalog, as the control plane reads it: two pure reads and nothing else.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- Control-plane consumers compare repository-qualified task-document values, not reconstructed
  leaf/sprint strings.
- The protocol is read-only; catalog implementations own persistence and mutation.
- `replacement_for_task_document_ref` is a staged generation of the same canonical seat, not a
  second namespace.
- Exactly one selector owns incumbent/heir precedence across the repository.
- Structural parent fields are read-only canonical address facts; they do not turn runtime ids into
  hierarchy authority.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `SeatRow` (lines 36-90) — One seat's row, as the control plane reads it.. [1]
- Defines the read-only catalog protocol consumed by structural selectors. [2]
- Resolves one canonical current generation and fails closed on duplicate primaries or heirs. [3]

## 260713-TES-L5 Completion Round — Fix-Round Docstring

The module docstring no longer names "the routing, ladder and orphan predicates" — the L5
fix round rewrote it to "The routing and rebind predicates in this package" (the escalation
ladder and orphan-policy modules are deleted; dead-owner rows surface through the rebind
machinery). `SeatRow`/`SeatDirectory` behavior is unchanged: pure catalog reads of the seat
shape declared by the control plane.
