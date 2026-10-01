# dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx

## Governing Overview

[Conversation renderer overview](overview.md)

## Purpose

Renders the restrained empty-conversation welcome inside the persistent timeline well without
claiming that a harness link is ready unless process evidence proves it.

## Code Commentary

### Logic

The component derives neutral, connecting, or ready presentation from its harness and optional
process-state inputs. The ready dot/copy is gated by a real connected state; unavailable, exited,
failed, or unknown process state does not inherit confidence from SSE liveness alone.

### Conventions

It is presentation-only and receives state from `ConversationSurface`; it neither opens streams nor
infers server readiness itself.

### Invariants And Boundaries

An open event stream is not proof that the underlying harness is ready. The empty well must stay
honest when the process is disconnected or no current process state exists.

### Todos

None recorded.

## Evidence

### Repo-Internal References

- The component gates its welcome state on optional `processState`, selecting `UNKNOWN_LINK` when it is undefined and otherwise `LINK_STATES[processState]`. [1]
- The surface supplies harness and current process state only for an empty live timeline. [2]
- Focused cases cover each readiness wording. [3]
