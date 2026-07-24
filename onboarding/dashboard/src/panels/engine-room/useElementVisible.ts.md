# dashboard/src/panels/engine-room/useElementVisible.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/engine-room/useElementVisible.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Engine Room overview](overview.md)

## Purpose

Provides the small reactive visibility gate shared by Engine Room animation substrates. It lets a
heavy cockpit layer remain mounted for state continuity without continuing off-screen animation work.

## Code Commentary

### Logic

The hook starts visible, observes the supplied element when `IntersectionObserver` exists, and
returns the latest intersection state. Missing observer support deliberately leaves the value true,
which makes jsdom and unsupported environments a no-op rather than a falsely hidden UI.

### Conventions

Callers own their pause/resume policy; this hook only reports visibility. Its observer disconnects on
effect cleanup and does not retain elements beyond their mounted lifetime.

### Invariants And Boundaries

The gate must not unmount a cockpit layer or fabricate a visibility result. It is only a signal for
work that is safe to pause, such as GSAP tweens, Motion pulses, and decorative video playback.

### Todos

None recorded.

## Docs References

No Domain Documentation entries are configured in `system/sources.md`; no external documentation was
used for this repository-local hook.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The hook defaults visible, observes an element when supported, and disconnects at cleanup. | L15-L27 | [useElementVisible.ts](useElementVisible.ts) |
| The GSAP owner consumes this signal to pause, rather than rebuild, a scoped animation context. | L96-L134 | [useEngineTimeline.ts](useEngineTimeline.ts) |
| Focused tests model observer availability and explicit hide/show transitions. | L7-L77 | [useElementVisible.test.tsx](useElementVisible.test.tsx) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-07-24T13:17:17Z — Curator: created the sidecar for the new Engine Room visibility gate.
  It is uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
