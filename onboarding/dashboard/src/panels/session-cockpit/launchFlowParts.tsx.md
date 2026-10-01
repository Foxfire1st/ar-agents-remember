# dashboard/src/panels/session-cockpit/launchFlowParts.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The launch-flow dialog render parts of the session cockpit, extracted from
`LaunchFlow.tsx` by the 260731-EFA-L8 split. Owns the harness section, model/effort
pickers, capability body, optional fields, launch footer, leaf-taken/conflict
outcomes, and the `LaunchFlowDialog` composition.

## Code Commentary

### Logic

`HarnessSection` renders the per-harness section; `ModelPicker`/`EffortPicker` render
the BOTH-knobs-or-NEITHER launch selection; `LeafTakenOutcome`/`ConflictOutcome`
render the fail-loud verbatim refusal states; `LaunchFlowDialog` composes them with
the overlay.

### Conventions

Presentational parts; launch state machines stay in `data/launchFlow.ts`.

### Invariants And Boundaries

No launch mutation here — outcomes render only what the flow machine reported.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The dialog parts. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
