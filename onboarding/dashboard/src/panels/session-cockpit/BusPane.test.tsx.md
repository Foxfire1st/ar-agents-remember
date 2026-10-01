# dashboard/src/panels/session-cockpit/BusPane.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Pins the Bus pane's fleet/filter honesty, supervisor facts, authoritative reverse-address request,
and reply-state persistence across filtering and more-than-100-row virtualization.

## Code Commentary

### Logic

- Covers the fleet-global default, sender-to-owner and redelivery facts, exact focused-seat
  filtering, non-health empty copy, and reset when focus disappears.
- Proves the exact operator-inbox request body for coherent sender pairs plus sender-agent-only and
  sender-role-only rows. Lifecycle-only targets perform zero POSTs and target lifecycle never leaks.
- A 120-row case drives virtual unmount/remount and async success/failure settlement, proving that
  each `entryId` retains its own open, draft, posted, or error state.

### Invariants And Boundaries

- Tests must assert both positive request shape and prohibited addressing fields.
- Large-list coverage protects interaction continuity, not merely row-count performance.

### Todos

None recorded; browser-level long-list/off-tab smoke remains a leaf integration residual.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Fleet, filter, focus-loss, and draft persistence cases. [1]
- Exact POST and lifecycle-only zero-write cases. [2]
- Virtualized per-entry async state case. [3]
- Shared coherent and legacy fixture pack. [4]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.

## 260815-DAG Master Full-Gate Repair

`afterEach` is now async and flushes the virtualizer's 150 ms scroll-observer debounce (fake-timer clear + real-timer 200 ms settle) before jsdom teardown so orphaned callbacks cannot fire without a `window`.
