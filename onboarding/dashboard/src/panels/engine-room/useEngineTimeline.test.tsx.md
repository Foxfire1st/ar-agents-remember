# dashboard/src/panels/engine-room/useEngineTimeline.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/engine-room/useEngineTimeline.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation entries are configured in `system/sources.md`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The harness uses a real engine scenario and a minimal tagged SVG circle. | L10-L35 | [useEngineTimeline.test.tsx](useEngineTimeline.test.tsx) |
| Tests pin transform animation, non-scaling stroke, and the effects-off no-op. | L45-L72 | [useEngineTimeline.test.tsx](useEngineTimeline.test.tsx) |
| Timeline implementation installs the non-scaling stroke and transform tween. | L41-L77 | [useEngineTimeline.ts](useEngineTimeline.ts) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-07-24T13:17:17Z — Curator: created the timeline-substrate test sidecar. It is uncommitted,
  so verification fields are intentionally blank until closeout stamps the code commit.
