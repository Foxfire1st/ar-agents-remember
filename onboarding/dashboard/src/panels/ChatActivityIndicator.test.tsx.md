# dashboard/src/panels/ChatActivityIndicator.test.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

Focused Vitest coverage for Operations chat activity identity, state mapping, aggregation and omission rules.

## Code Commentary

### Logic

The fixture creates live harness sessions bound to a canonical task-document reference. Tests pin
busy, awaiting-input, stale/missing, multi-seat deterministic detail, exact task-document isolation
before lifecycle fallback, lifecycle-only fallback, and omission when no live bound harness exists.

### Conventions

The test uses a local session builder and pure Vitest summary assertions without the session poller. Removed JSX/Testing Library assertions no longer prove DOM accessibility, title or role=status; row presentation has separate tests.

### Invariants And Boundaries

- Tests must distinguish chat turn state from task state and inbox acknowledgment.
- Unknown values are not silently treated as idle or working.
- Sessions with another task-document claim, terminal kind, landed status, or missing status do not invent activity.

### Todos

None.

### 2026-07-24 Curator Delta

The summary tests pin ready-without-turn as idle and starting-without-turn as unknown, preventing the
fresh-chat path from returning to a stale or alarmed label.

## Evidence

### Docs References

No relevant domain documentation was configured in the resolved `system/sources.md`.

No domain reference was available for this UI-local test contract.

### Repo-Internal References


- Implementation under test. [1]


### Cross-Repo References

No meaningful cross-repository reference exists.

No cross-repo reference.
