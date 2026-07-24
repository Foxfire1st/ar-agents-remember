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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The mock captures per-element observer callbacks and teardown removes the shim. | L7-L53 | [useElementVisible.test.tsx](useElementVisible.test.tsx) |
| The two cases pin visible fallback and hide/show/disconnect transitions. | L55-L77 | [useElementVisible.test.tsx](useElementVisible.test.tsx) |
| Implementation under test. | L15-L27 | [useElementVisible.ts](useElementVisible.ts) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-07-24T13:17:17Z — Curator: created coverage onboarding for the new visibility gate. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
