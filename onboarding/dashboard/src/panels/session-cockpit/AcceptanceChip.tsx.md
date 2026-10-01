# dashboard/src/panels/session-cockpit/AcceptanceChip.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Shared accessible renderer for one typed set/pair/route chip.

## Code Commentary

### Logic

Renders the model's literal evidence text, tone, optional slow spinner, and owner-supplied
acknowledge or retry actions. Test ids and data attributes expose chip kind and acceptance without
reclassifying the evidence in the component.

### Conventions

The acceptance word is always present in visible text; tone is supplemental. The spinner follows
the 2.4-second pulse ruling and disables animation under reduced motion.

### Invariants And Boundaries

Only `demandsAck` chips may receive mark-seen behavior and only retryable route chips may receive
retry behavior. This component never owns either side effect.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Chip rendering and action boundary. [1]
- Typed presentation models and acceptance words. [2]
- Primary live-control owner. [3]
- Background outcome owner. [4]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
