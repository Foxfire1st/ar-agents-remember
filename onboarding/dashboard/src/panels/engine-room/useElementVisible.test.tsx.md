# dashboard/src/panels/engine-room/useElementVisible.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/engine-room/useElementVisible.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation entries are configured in `system/sources.md`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The mock captures per-element observer callbacks and teardown removes the shim. | `MockIntersectionObserver` | dashboard/src/panels/engine-room/useElementVisible.test.tsx:10-22 |
| The two cases pin visible fallback and hide/show/disconnect transitions. | "stays visible when IntersectionObserver is unavailable (the jsdom default — a no-op gate)"; "flips false on hide and true on re-show, and stops observing on unmount" | dashboard/src/panels/engine-room/useElementVisible.test.tsx:56-60; dashboard/src/panels/engine-room/useElementVisible.test.tsx:62-77 |
| Implementation under test. | `useElementVisible` | dashboard/src/panels/engine-room/useElementVisible.ts:15-27 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 3 citation claims; scoped result 0 findings.

- 2026-07-24T13:17:17Z — Curator: created coverage onboarding for the new visibility gate. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
