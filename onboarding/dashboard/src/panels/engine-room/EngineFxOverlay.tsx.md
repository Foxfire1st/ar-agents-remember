# dashboard/src/panels/engine-room/EngineFxOverlay.tsx

## Governing Overview

[Engine Room overview](overview.md)


## Current enclosure-only composition

EngineFxOverlayProps now contains attention and surgeXs only; sparse sibling SVG renders SurgeLines and AttentionGroup. ReindexGroup and dimensions/reindexAt were removed; fixed shared viewBox and aria-hidden remain.

### Maintenance boundaries

Delete reindex geometry/spine/divisions and unchanged-choreography claims for that removed effect. Describe only ledger-coupler surge and attention breathing, selector ownership in timeline and surviving structural hit targets. Do not retire the whole overlay.

Source/test/fixture inspection is not a fresh mounted capture or a passing test run.
Historical provider-shaped input data and retained compatibility definitions do not
restore removed provider visuals or tool exposure.

- EngineFxOverlayProps now contains attention and surgeXs only; sparse sibling SVG renders SurgeLines and AttentionGroup.  — source ownership, not executed visual proof. [3]
- EngineFxOverlayProps now contains attention and surgeXs only; sparse sibling SVG renders SurgeLines and AttentionGroup.  — source ownership, not executed visual proof. [4]
- EngineFxOverlayProps now contains attention and surgeXs only; sparse sibling SVG renders SurgeLines and AttentionGroup.  — source ownership, not executed visual proof. [5]

## Historical superseded account (non-operative)

The prior onboarding below is retained for provenance and unrelated design history.
It is not current provider-render, fallback, prototype-parity or execution guidance.
Current behavior and its limits are the operative contract above.



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
