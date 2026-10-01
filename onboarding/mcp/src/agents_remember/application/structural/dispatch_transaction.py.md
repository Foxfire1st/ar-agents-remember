# mcp/src/agents_remember/application/structural/dispatch_transaction.py

## Governing Overview

[Structural application services](overview.md)

## Purpose

Owns the idempotent spawn-and-brief transaction for one canonical
`(task_document_ref, role)` seat.

## Code Commentary

### Logic

`execute_dispatch_transaction` admits a first spawn, recognizes an already occupied seat, and
reconciles that occupant against its durable catalog receipt and exact-pinned inbox brief. A viable
brief converges on the existing generation. A missing catalog receipt is repaired from the brief;
a retained catalog receipt survives bounded inbox compaction. A generation proven to have failed
before briefing is retired and retried once. Contradictory, unreadable, or otherwise ambiguous
evidence refuses without retirement. Receipt repair is delegated to `DispatchBriefReceiptStore`,
which composes with the terminal catalog atomic lock/read/write unit without widening the general
`TerminalCatalog` lifecycle surface.
`execute_serialized_dispatch` owns the seat-scoped lock plus transaction execution and translates
only serializer setup/acquisition failure. This keeps the public application composition small
without moving reconciliation or introducing a second lock policy.

For the polymorphic reviewer seat, `expected_structural_parent` makes the dispatching plane part of
reconciliation. Reusing an already-running reviewer succeeds only when its generation is stamped
with that same parent document and role. A reviewer owned by another review seam returns
`structural-parent-conflict`; the caller must retire that generation before opening the next seam.
The sole migration exception is an unstamped pre-polymorphic leaf reviewer, whose historical
manager owner is deterministic. It never guesses a master- or sprint-level owner.

### Conventions

The transaction receives typed owners and callbacks. It may inspect a private occupant id while
reconciling, but all returned payloads contain only the structural document-and-role address.

### Invariants And Boundaries

- One invocation performs at most one replacement retry.
- A manual or unattributed live occupant is never retired merely because it lacks dispatch evidence.
- A catalog receipt and a present pinned brief must agree.
- A live polymorphic reviewer generation cannot be rebound from one structural parent to another.
- Unstamped legacy migration is bounded to the old leaf-reviewer shape; higher-altitude ownership
  always requires a plane stamp.
- A successful retry never exposes the replaced or current runtime id.
- `None` from evidence reconciliation is positive proof of no viable brief; exceptions and
  contradictions are unknown state and cannot authorize rollback.
- Serialization is supplied by `serving/structural_dispatch.py`; this module owns reconciliation,
  not lock implementation.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; this repository-owned transaction and its forcing
suite are the authority.

- The dispatch transaction has one bounded reconciliation-and-retry loop. [1]

### Repo-Internal References

- Existing generation evidence is loaded, repaired, and classified before retirement. [2]
- Contradictory evidence produces the stable typed reconciliation refusal. [3]
- Reviewer reconciliation refuses a current generation owned by a different structural parent. [4]
- Serialized dispatch has one transaction entry point; no end-to-end concurrency pass is inferred from source inspection. [5]

### Cross-Repo References

No cross-repository dependency governs this unit.
