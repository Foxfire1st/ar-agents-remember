# dashboard/src/panels/engine-room/useElementVisible.ts

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

## Evidence

### Docs References

No Domain Documentation entries are configured in `system/sources.md`; no external documentation was
used for this repository-local hook.

No relevant domain documentation was found.

### Repo-Internal References

- The hook defaults visible, observes an element when supported, and disconnects at cleanup. [1]
- The GSAP owner consumes this signal to pause, rather than rebuild, a scoped animation context. [2]
- Focused tests cover observer-unavailable visibility, hide/show transitions, and disconnect on unmount. [3]

### Cross-Repo References

No cross-repository boundary is owned here.

No cross-repository evidence applies.

- 2026-07-24T13:17:17Z — Curator: created the sidecar for the new Engine Room visibility gate.
  It is uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
