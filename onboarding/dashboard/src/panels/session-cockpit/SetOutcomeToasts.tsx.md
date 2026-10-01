# dashboard/src/panels/session-cockpit/SetOutcomeToasts.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Persistent background-session surface for unacknowledged set outcomes.

## Code Commentary

### Logic

Filters running, unfocused sessions to those with set attention. One affected session renders its
evidence chips; several collapse into one disciplined stack. Each row can focus the seat or use
the explicitly labelled `mark seen` action to acknowledge its evidence.

### Conventions

The focused seat uses its inline chips instead of a duplicate toast. Mark seen acknowledges local
attention; it does not delete server evidence.

### Invariants And Boundaries

Outcomes persist through unrelated focus changes until acknowledged. Several background outcomes
never produce several competing toast stacks.

### Todos

None recorded; shared chip derivation caveats are recorded in `setChips.ts.md`.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Background filtering, collapse, focus, and acknowledgment UI. [1]
- Persistence and collapse regression cases. [2]
- Shared attention and chip derivation. [3]
- Explicit acknowledgment driver. [4]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
