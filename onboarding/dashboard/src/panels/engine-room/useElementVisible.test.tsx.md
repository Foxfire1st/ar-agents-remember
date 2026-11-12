# dashboard/src/panels/engine-room/useElementVisible.test.tsx

## Governing Overview

[Engine Room overview](overview.md)

## Purpose

Pins the visibility gate's benign fallback and its observer lifecycle without relying on jsdom to
implement browser intersection behavior.

## Code Commentary

### Logic

A controllable `IntersectionObserver` mock stores observed callbacks. The probe records hook state,
then the tests drive hide/show notifications and assert disconnect cleanup after unmount.

### Conventions

The global observer shim is installed only in the explicit-observer case and removed in `afterEach`.
This keeps the default-unavailable case representative of normal jsdom test execution.

### Invariants And Boundaries

The test deliberately proves that unavailable observer support reads as visible; it must not turn
all animation owners off in a non-browser runner.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation entries are configured in `system/sources.md`.

No relevant domain documentation was found.

### Repo-Internal References

- The mock captures per-element observer callbacks and teardown removes the shim. [1]
- The two cases pin visible fallback and hide/show/disconnect transitions. [2]
- Implementation under test. [3]

### Cross-Repo References

No cross-repository boundary is owned here.

No cross-repository evidence applies.
