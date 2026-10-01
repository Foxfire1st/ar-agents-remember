# mcp/src/agents_remember/controlplane/expectation_rows.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Stores restart-durable dispatch and gate deadline rows. A subject is structurally identified by task
document plus role, with occupant ids retained only as correlation evidence.

## Code Commentary

`mark_met` and `mark_missed` leave any non-pending row unchanged, so the first terminal transition and its timestamp win. Pending queries fold by id; source lookup additionally filters the optional kind and selects the latest pending row. Missing row ids refuse. These are owner-visible deadlines: the relay does not evaluate or mark them missed. Source: mcp/src/agents_remember/controlplane/expectation_rows.py:127-143.

### Logic

`ExpectationRow` and `ExpectationSubject` preserve document/role alongside optional agent and
lifecycle correlations. Creation is pure; the caller writes the row atomically beside the dispatch
or gate action. The append-only store folds pending/met/missed snapshots and exposes a tolerant
projection read separately from strict decision reads.

### Conventions

Only actual dispatch/gate seams create expectations. Model completion or inbox consume does not.

### Invariants And Boundaries

- Deadlines are durable rows, never in-memory timers.
- Subject occupant replacement does not redefine the task-owned obligation.
- Projection tolerance is not used for decisions or rewrites.

### Todos

Legacy expectation kinds remain parse-only until a separately governed schema migration removes them.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The durable row separates structural subject from runtime correlation. [1]
- Creation records the supplied structural subject. [2]
- Strict and tolerant reads have distinct authority. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
