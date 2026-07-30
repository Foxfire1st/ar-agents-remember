# dashboard/src/panels/engine-room/EngineFxOverlay.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/engine-room/EngineFxOverlay.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Structural canvas and overlay placement. | [EnclosureCanvas.tsx](agents-remember/dashboard/src/panels/engine-room/EnclosureCanvas.tsx) |
| Timeline selectors and choreography. | [useEngineTimeline.ts](agents-remember/dashboard/src/panels/engine-room/useEngineTimeline.ts) |
| Visual isolation regressions. | [EnclosureProcessMap.test.tsx](agents-remember/dashboard/src/panels/engine-room/EnclosureProcessMap.test.tsx) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for the
  sparse effects overlay and recorded that it preserves existing choreography and structural
  ownership. Verification metadata remains blank until commit.
