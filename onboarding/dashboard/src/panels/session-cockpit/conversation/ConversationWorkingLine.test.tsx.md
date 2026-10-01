# dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx

## Governing Overview

[Conversation renderer overview](overview.md)

## Purpose

Pins the SSE working line as a pure status cue.

## Code Commentary

### Logic

Projection helpers seed stream, turn state, timestamps, and freshness. The suite asserts the live
working cue, bounded elapsed/stale rendering, suppression when evidence is insufficient, and absence
of a line-hosted stop control.

### Conventions

Tests read the active-conversation store rather than reproducing a separate status model.

### Invariants And Boundaries

The stop action must remain in `SessionComposer`; this suite guards against moving it back into a
status line because that would duplicate controlled-seat controls.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation entries are configured in `system/sources.md`.

No relevant domain documentation was found.

### Repo-Internal References

- The fixed-anatomy case pins the live working cue and elapsed value derived from `stateSince`. [1]
- The remaining cases pin canonical working states, live/working gating, elapsed omission, stale rendering, and the absence of a line-hosted stop control. [2]
- Component under test. [3]
- Controlled stop owner. [4]

### Cross-Repo References

No cross-repository boundary is owned here.

No cross-repository evidence applies.
