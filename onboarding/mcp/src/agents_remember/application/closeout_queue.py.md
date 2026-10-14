# mcp/src/agents_remember/application/closeout_queue.py

## Governing Overview

[application overview](overview.md)

## Purpose

This is the request-declared application boundary for the sprint closeout queue. It builds a
structural `QueueActor` from the caller's canonical role/document declaration and delegates
authorization and scheduling to the queue owner. A declaration is assertion, not host identity
proof; restricting who can reach the server remains a deployment responsibility.

## Code Commentary

### Logic

`closeout_queue_tool` passes `_declared_queue_actor(request)` to the retained queue operation.
A missing `caller` raises `closeout-queue-caller-required`; a present caller contributes exactly
its role and task-document reference. This module performs no terminal-seat lookup, hosted-seat
precedence or hosted/declaration conflict fallback. The queue's own role/document authorization
still governs every operation.

### Conventions

The application layer owns declaration-to-actor construction; scheduling and authorization stay
in `worktrees/queue/closeout_queue.py`.

### Invariants And Boundaries

- A reachable caller may assert a role/document; the queue validates that pair, not a proof of
  host identity. This does not add authority beyond the pair's existing queue permissions.
- Missing caller declaration is a typed refusal. No removed seat/plane compatibility reader is
  installed, and canonical grade provenance remains the queue owner's concern.
- This module does not mutate task documents or Git refs directly.

### Todos

None recorded.

## Evidence

- The required request declaration is passed as the structural queue actor; scheduling and authorization stay with the queue. [1]

## 260821-CLIVE-L2 Public Failure Boundary

Historical CLIVE behavior separated hosted-seat availability errors. R113 removes that resolution
path; current behavior is only the explicit request declaration described above. This historical
section does not promise a hosted-seat fallback or a currently reachable seat-resolution error.

- The former ambient-seat failure distinction is historical, not an active R113 call path.
