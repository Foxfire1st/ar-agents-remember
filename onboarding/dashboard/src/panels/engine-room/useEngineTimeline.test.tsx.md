# dashboard/src/panels/engine-room/useEngineTimeline.test.tsx

## Governing Overview

[Engine Room overview](overview.md)

## Purpose

Tests the GSAP timeline substrate directly on a minimal SVG harness, separating tween-contract
checks from the larger canvas rendering suite.

## Code Commentary

### Logic

The harness supplies the same tagged stroked scan circle as the canvas. Cases assert transform scale
instead of `r` attribute animation, `non-scaling-stroke` while effects are enabled, and no tween or
attribute mutation when the effects gate is off.

### Conventions

Each test removes the effects dataset before mounting and `cleanup` reverts the GSAP context after
mount. The scenario fixture supplies a real verify-stage engine node rather than an invented shape.

### Invariants And Boundaries

The scan ring may scale only if its stroke is protected from that scale; otherwise a radius-equivalent
motion turns into an expanding thick outline. Effects-off must be a true no-motion path.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation entries are configured in `system/sources.md`.

No relevant domain documentation was found.

### Repo-Internal References

- The harness uses a real engine scenario and a minimal tagged SVG circle. [1]
- Tests pin transform animation, non-scaling stroke, and the effects-off no-op. [2]
- Timeline implementation installs the non-scaling stroke and transform tween. [3]

### Cross-Repo References

No cross-repository boundary is owned here.

No cross-repository evidence applies.
