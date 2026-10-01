# mcp/src/agents_remember/application/closeout_queue.py

## Governing Overview

[application overview](overview.md)

## Purpose

This module is the ambient-authorized application boundary for the sprint closeout queue. It turns
the caller's canonical seat and task-document binding into the structural `QueueActor` used by the
queue service. A plane-injected hosted seat wins when one exists (the seat path is unchanged); a
caller with no plane identity declares its role + task document as request data (L16-R2), and that
declaration is validated by the same queue authorization a seat would face — it grants no
authority beyond the same role/document pair (the L16 F5 trust model).

## Code Commentary

### Logic

`closeout_queue_tool` resolves the ambient seat from the terminal catalog; a hosted seat wins, an
unbound seat refuses, and any `AmbientSeatError` other than `ambient-seat-unavailable` keeps
refusing with its typed status. On `ambient-seat-unavailable`, `_declared_queue_actor` builds the
`QueueActor` from the request-carried `caller` (missing → `closeout-queue-caller-required`), and
`_refuse_hosted_declared_conflict` refuses a request-carried caller that contradicts the hosted
seat (`closeout-queue-caller-conflict`; an identical one is harmless). The declared path builds the
identical `QueueActor` the seat path uses, so every queue authorization (`_authorize_status_scope`,
`_require_sprint_role`, `_authorize_candidate_action`, `_declare_candidate_under_authority`)
validates it identically.

### Conventions

The application layer owns ambient identity resolution; scheduling mechanics stay in
`worktrees/closeout_queue.py`.

### Invariants And Boundaries

- Hosted seat wins; only `ambient-seat-unavailable` triggers the declared-caller fallback; other
  `AmbientSeatError` statuses (stale/invalid/mismatch/unbound) keep refusing.
- A declared caller that contradicts the hosted seat refuses (`closeout-queue-caller-conflict`); a
  matching one is harmless (L16-R2).
- Trust model (L16 F5): the fallback accepts the caller's self-declared identity — any caller able
  to reach the MCP server may claim any role/document and, passing the role/document
  authorization, act with that identity's authority. The mechanism grants no more than a seat with
  the same pair, so the residual risk is deployment-level (who may reach the server); the
  declaration is assertion, not plane proof.
- Grades still resolve byte-exact against canonical register rows (`canonical_grade` is
  actor-independent); the fallback never fabricates judgment provenance (L16-R4).
- Ambient-seat failures retain their typed status through `CloseoutQueueError`.
- This module does not mutate task documents or Git refs directly.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; this is an internal authority boundary.

### Repo-Internal References

- The seat-or-declared caller resolution precedes construction of the structural queue actor. [1]

### Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Public Failure Boundary

Non-availability still permits the existing declared ambient caller path, but every other hosted
seat-resolution failure now preserves only its typed status and returns a bounded public detail.
Backend exception text and caller-sensitive internals no longer cross this application boundary.

- Non-availability and other ambient-seat failures have separate public handling. [2]
