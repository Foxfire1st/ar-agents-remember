# dashboard/src/panels/engine-room/EngineFxOverlay.tsx

## Governing Overview

[Engine Room overview](overview.md)

## Purpose

Renders the Engine Room's repeating decorative SVG effects in a sparse sibling overlay while the
structural enclosure canvas remains unchanged.

## Code Commentary

### Logic

`EngineFxOverlay` receives the already-derived surge positions, reindex gauge geometry, attention
state, and shared SVG dimensions. It renders only the animated surge lines, reindex divisions and
spine, and attention badge. Existing style recipes and `data-fx` selectors are reused so
`useEngineTimeline` preserves the original choreography.

### Conventions

The overlay is presentation-only, `aria-hidden`, and shares the structural canvas view box and
aspect-ratio contract.

### Invariants And Boundaries

- No projected engine data is re-derived here.
- Structural nodes, hit targets, and labels stay in `EnclosureCanvas`.
- Effect classes and selectors remain the same animation contract.
- The split isolates repeated transforms without changing visual ordering.

### Todos

Hangar/Engine Room steady-state CPU work is explicitly deferred by the developer and is not part
of this file's current acceptance gate.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Timeline selectors and choreography. [1]
- Visual isolation regressions. [2]

### Cross-Repo References

No meaningful cross-repository references found.
