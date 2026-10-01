# mcp/src/agents_remember/serving/dispatch_brief.py

## Governing Overview

[overview.md](overview.md)
## Purpose

Governs the first durable message to a newly dispatched child. It is the sole internally exact-pinned
inbox delivery because the brief belongs to that newly created occupant.

## Code Commentary

### Logic

The gate requires the exact target to be running and ready, starts the brief expectation, and verifies
delivery against the same session correlation. Prompt keywords are applied only to this initial brief.
Ordinary relationship traffic does not use this exact-pin rule.

The default readiness check now waits through one bounded ten-second spawn-to-bridge startup window.
Expiry does not trigger a second dispatch or readiness call: the exact-pinned durable brief remains
pending for the ordinary notifier path, preserving one-call spawn semantics.

### Conventions

Exact session identity is private transaction evidence. The agent-facing dispatch request supplies
only task document, role, brief, and optional label.

### Invariants And Boundaries

- Initial brief delivery never rebinds to a replacement.
- Persistence precedes delivery.
- Failure leaves no silently live unbriefed child; the structural application performs rollback.
- Briefed truth comes from correlated delivery evidence, not model completion.
- Startup convergence is bounded once inside the gate; timeout never becomes an external retry loop
  or a second child/brief operation.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Dispatch target admission requires the exact hosted target. [1]
- Dispatch brief is explicitly the exact-pinned exception. [2]
- Brief expectation fulfillment reads durable delivery evidence. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
