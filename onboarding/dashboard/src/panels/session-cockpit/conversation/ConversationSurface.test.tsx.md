# dashboard/src/panels/session-cockpit/conversation/ConversationSurface.test.tsx

## Governing Overview

[Conversation renderer overview](overview.md)

## Purpose

Tests the surface-level wiring for hidden keep-alive behavior, current-position navigation, and
scroll-memory handoff into the timeline.

## Code Commentary

### Logic

The suite seeds active projections and rerenders visibility/geometry states. It checks suppressed
announcements while hidden, the explicit latest action, current empty/welcome composition, and
scroll-memory persistence across the surface-to-timeline boundary.

### Conventions

The test keeps data setup in small projection helpers and uses the real active-conversation store.

### Invariants And Boundaries

Hidden surfaces keep tracking but do not announce. The latest control is an explicit user action,
not a reason to silently override a reader's saved position.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation entries are configured in `system/sources.md`.

No relevant domain documentation was found.

### Repo-Internal References

- Helpers seed projection/visibility variants for the surface. [1]
- Hidden gating, latest chip, and scroll wiring are covered. [2]
- Implementation under test. [3]

### Cross-Repo References

No cross-repository boundary is owned here.

No cross-repository evidence applies.

## 260815-DAG Master Full-Gate Repair

`afterEach` is now async and flushes the conversation timeline virtualizer's 150 ms scroll debounce (fake-timer clear + real-timer 200 ms settle) before jsdom teardown.
