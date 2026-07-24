# dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Session cockpit overview](overview.md)

## Purpose

Exercises the structured-stage orchestration seams: bridge readiness, per-session mounted surfaces,
epoch attribution, freshness, and the interaction between view switches and scroll geometry.

## Code Commentary

### Logic

The suite mocks only the authority and conversation network edges while retaining the real stores.
It seeds warm projection pages, drives focused-session changes, and proves transient boot retries,
fail-loud bounds, LRU pool eviction, stale-epoch isolation, and view-switch restoration behavior.

### Conventions

Tests use explicit fake-timer windows and mock projection data rather than a live bridge. The PTY and
ambient telemetry are substituted only where their rendering is irrelevant to the stage contract.

### Invariants And Boundaries

A warm surface must remain mounted but hidden; a cold or evicted surface must not be reused. A slow
boot gets bounded transient retries, while terminal answers fail loud rather than being masked.

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
| Harness setup preserves real stores while replacing network edges. | L1-L105 | [ChatsStageBody.test.tsx](ChatsStageBody.test.tsx) |
| Boot, pool, epoch/freshness, scroll-restore, and persistent-layer matrices cover the stage seams. | L106-L981 | [ChatsStageBody.test.tsx](ChatsStageBody.test.tsx) |
| Implementation under test. | L151-L454 | [ChatsStageBody.tsx](ChatsStageBody.tsx) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-07-24T13:17:17Z — Curator: created the structured-stage regression-suite sidecar. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
