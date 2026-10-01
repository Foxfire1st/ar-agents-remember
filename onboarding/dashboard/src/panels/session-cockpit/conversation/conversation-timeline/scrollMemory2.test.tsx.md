# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/scrollMemory2.test.tsx

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The second scroll-memory suite split from `renderer.test.tsx` by the 260731-EFA-L8 test split.
Pins the remaining F-ac matrix: hidden-collapse clamps, trusted-user override, virtual measurement
shifts, and late-clamp protection. Its explicit fake-timer cases follow the shared suite rule:
unmount and discard pending callbacks before real timers return.

## Code Commentary

### Logic

Drives the geometry shim for clamp/override/measurement-shift scenarios and asserts the scroll
position never fights trusted input. Both `finally` blocks clean their render and fake-timer queue
before `useRealTimers`, preventing a pending Virtualizer debounce from crossing test teardown.

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

- The second scroll-memory suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
