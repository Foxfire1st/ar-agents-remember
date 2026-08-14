# dashboard/src/panels/engine-room/useElementVisible.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/engine-room/useElementVisible.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The hook defaults visible, observes an element when supported, and disconnects at cleanup. | `useElementVisible` | dashboard/src/panels/engine-room/useElementVisible.ts:15-27 |
| The GSAP owner consumes this signal to pause, rather than rebuild, a scoped animation context. | `useEngineTimeline`; `visible` | dashboard/src/panels/engine-room/useEngineTimeline.ts:168-247 |
| Focused tests cover observer-unavailable visibility, hide/show transitions, and disconnect on unmount. | `MockIntersectionObserver`; `fireIntersection`; "stays visible when IntersectionObserver is unavailable"; "flips false on hide and true on re-show"; "expect(observed.size).toBe(0)" | dashboard/src/panels/engine-room/useElementVisible.test.tsx:10-22; dashboard/src/panels/engine-room/useElementVisible.test.tsx:34-41; dashboard/src/panels/engine-room/useElementVisible.test.tsx:56-60; dashboard/src/panels/engine-room/useElementVisible.test.tsx:62-77 |

## Update History

- 2026-08-04T13:54+02:00 — 260731-EFA-L6 S18-B13 curator: reissued whole-claim evidence for observer availability, transitions, and cleanup for same-reviewer closure.

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

- 2026-07-24T13:17:17Z — Curator: created the sidecar for the new Engine Room visibility gate.
  It is uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
