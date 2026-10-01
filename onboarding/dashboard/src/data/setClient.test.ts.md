# dashboard/src/data/setClient.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

End-to-end unit contract for the set-control I/O driver and its store-visible honesty semantics.

## Code Commentary

### Logic

Exercises exact wire routes and bodies; all acceptance outcomes; clamp, unknown, unsupported, and
route-error state; superseded responses; focused announcements; snapshot classification and
single-flight; queued/unknown promotion; serialized pair success, refusal, and route termination;
effort cycling; and turn/focus watcher triggers.

### Conventions

Fetch is mocked at the boundary while the real reducers and store are used, so assertions cover
the state that UI consumers actually receive.

### Invariants And Boundaries

Tests distinguish requested, pending, echo-evidenced effective, and readback-confirmed values.
They also prove that pair effort cannot POST before model evidence and that route failures cannot
fabricate effectiveness.

### Todos

The final reviewer PASS retains the production sev-4 observations recorded in `setClient.ts.md`;
they are not release blockers for this leaf.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Set, snapshot, promotion, pair, cycling, and watcher cases. [1]
- Driver under test. [2]
- Shared deterministic fixtures. [3]
- The shared `observerEvent` builder supplies `schema`/`id`/`trust`/`actor` defaults to every event it creates. [4]
- The R4 promotion-watcher test routes the turn-ended L2 SEAT-EVENT through `applySeatEvent` using the shared observer-event fixture. [5]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
