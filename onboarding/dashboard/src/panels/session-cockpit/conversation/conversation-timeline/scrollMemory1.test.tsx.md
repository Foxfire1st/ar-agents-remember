# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory1.test.tsx

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The first scroll-memory suite split from `renderer.test.tsx` by the 260731-EFA-L8 test split.
Pins the F-ac scroll-memory matrix: middle/top and bottom restoration, later inflow at bottom,
geometry settling, and the persistent latest control. Fake-timer cases explicitly unmount and
discard pending callbacks before returning to real time, matching the shared fixture's hermetic
teardown contract.

## Code Commentary

### Logic

Uses the describe-scoped geometry/timer shim (`scrollMemory.test-utils.tsx`) to drive restore
scenarios deterministically. Each explicit fake-timer `finally` performs `cleanup` and
`clearAllTimers` before `useRealTimers`, so a TanStack scroll debounce cannot be promoted into the
next case or the destroyed jsdom environment.

### Invariants And Boundaries

Assertions preserved from the monolithic suite. Timer restoration must follow render cleanup.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The first scroll-memory suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
