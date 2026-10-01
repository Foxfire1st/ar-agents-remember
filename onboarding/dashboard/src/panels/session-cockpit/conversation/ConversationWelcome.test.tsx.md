# dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.test.tsx

## Governing Overview

[Conversation renderer overview](overview.md)

## Purpose

Pins process-evidenced welcome language for an empty structured conversation.

## Code Commentary

### Logic

Cases render the welcome through its public props and assert that only the connected process form
uses ready copy/dot; starting, disconnected, exited, failed, and absent state remain neutral or
honestly unavailable.

### Conventions

This is a focused renderer test: it does not simulate stream opening because stream liveness is
deliberately not the readiness authority for this component.

### Invariants And Boundaries

Tests must reject a future regression that paints a fresh-online token merely because a conversation
projection happens to be live.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation entries are configured in `system/sources.md`.

No relevant domain documentation was found.

### Repo-Internal References

- Focused cases cover all process readiness variants. [1]
- Component under test. [2]

### Cross-Repo References

No cross-repository boundary is owned here.

No cross-repository evidence applies.
