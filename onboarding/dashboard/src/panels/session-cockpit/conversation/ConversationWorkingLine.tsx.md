# dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.tsx

## Governing Overview

[Conversation renderer overview](overview.md)

## Purpose

Renders the SSE-preferred working cue for a focused live harness conversation.

## Code Commentary

### Logic

The line reads active-conversation stream/status evidence and renders only a current working cue,
optional elapsed duration, and an explicit stale marker. It owns no stop control; the controlled
session composer renders that exact-turn action beside Send from the same evidence.

### Conventions

It is selected by `SessionsView` only for a live harness stream. Catalog `WorkingLine` remains the
fallback for raw sessions and the stream connect/reconnect interval.

### Invariants And Boundaries

The component must never present a stop button or invent a working turn when stream/status evidence
is absent. Its status wording is a cue, not a second control surface.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation entries are configured in `system/sources.md`.

No relevant domain documentation was found.

### Repo-Internal References

- SSE status drives working, elapsed, and stale rendering without any control. [1]
- Stage composition selects this only for a live harness stream. [2]
- Focused tests pin cue-only behavior. [3]

### Cross-Repo References

No cross-repository boundary is owned here.

No cross-repository evidence applies.
