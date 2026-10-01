# dashboard/src/panels/session-cockpit/ModelEffortControl.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Header-mounted live model/effort readout, exact-session picker, staged apply flow, and acceptance
chip surface.

## Code Commentary

### Logic

Opening the controlled popover fetches only the live session snapshot. The trigger reads effective
selection and source; model options are visible snapshot rows, and effort options are re-gated to
the staged model's session-settable row. Model-only and effort-only apply one set; an explicitly
staged pair enters the serialized model-then-effort flow. Fetch errors render verbatim with retry,
while the adjacent chip row exposes pending and completed evidence.

### Conventions

Staged values are requests, not markers, and reset on open/session changes. A staged model's
default effort is only a visual pre-highlight until the user explicitly selects it.

### Invariants And Boundaries

The control renders only for live harness sessions. It never reads the pre-session catalog,
inherits an old row's effort options, or treats a missing echoed effort as an empty menu.

### Todos

- Reviewer sev-4 observation 6: before the first exact-session readback, the trigger fallback is
  visually indistinguishable from an echo-verified effective value even though its accessible
  description names the source.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Trigger, exact-session menus, staging, serialized apply, error, and chip UI. [1]
- Sourcing, corrected menu, apply, and chip regression matrix. [2]
- Live-session client and actions. [3]
- Menu and effective-marker derivation. [4]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.

## Current L5I Maintenance

The trigger shows only a real running model/effort pair: freshest echoed evidence first, then the
launch-resolved value. Missing effort now removes its segment instead of emitting an unsupported
sentinel; the live menu remains the authority for choosing a value.
