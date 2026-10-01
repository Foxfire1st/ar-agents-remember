# dashboard/src/data/setAcceptance.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Exhaustive pure tests for the SetResult reducer, attention/clamp classification, HTTP boundary,
snapshot promotion, and turn-ended re-fetch predicate.

## Code Commentary

### Logic

The suite runs every acceptance and edge row for both model and effort, distinguishes evidence
from transport, preserves exact provider-qualified comparisons, proves Codex both-queued
resolution on one snapshot, and keeps inflight/unconfirmed queued states untouched.

### Conventions

Shared fixtures carry the wire vocabulary; tables are preferred over one-off examples.

### Invariants And Boundaries

Test-only; driver single-flight and actual I/O sequencing live in `setClient.test.ts`.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Pure reducer and promotion implementation. [1]
- Clamp, queued, and unknown fixture extensions. [2]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo evidence applies.
