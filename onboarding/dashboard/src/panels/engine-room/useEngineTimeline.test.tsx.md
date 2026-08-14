# dashboard/src/panels/engine-room/useEngineTimeline.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/engine-room/useEngineTimeline.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The harness uses a real engine scenario and a minimal tagged SVG circle. | `ScanHarness` | dashboard/src/panels/engine-room/useEngineTimeline.test.tsx:25-33 |
| Tests pin transform animation, non-scaling stroke, and the effects-off no-op. | "touches nothing under data-effects=off (no tween" | dashboard/src/panels/engine-room/useEngineTimeline.test.tsx:65-72 |
| Timeline implementation installs the non-scaling stroke and transform tween. | `useEngineTimeline` | dashboard/src/panels/engine-room/useEngineTimeline.ts:168-247 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History
- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 3 repository-reference citations (3/3 anchored and sourced; scoped citation check clean).

- 2026-07-24T13:17:17Z — Curator: created the timeline-substrate test sidecar. It is uncommitted,
  so verification fields are intentionally blank until closeout stamps the code commit.
