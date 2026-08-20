# dashboard/src/panels/session-cockpit/sessions-view/stageSurface.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/stageSurface.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The stage-surface suite split from `SessionsView.test.tsx` by the 260731-EFA-L8 test
split. Pins the L6 stage surface: WorkingLine, InteractionBar, and stop-residual
behavior.

## Code Commentary

### Logic

Seeds a live session and asserts the stage renders the working line, the
interaction bar answers ride the gate channel, and stop residuals survive cleanup.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The stage-surface suite. | `describe` | dashboard/src/panels/session-cockpit/sessions-view/stageSurface.test.tsx:57-180 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## 260815-DAG Master Full-Gate Repair

Added an async `afterEach` that flushes the conversation timeline virtualizer's 150 ms scroll debounce (200 ms real-timer settle) before jsdom teardown.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: async `afterEach` flushes the timeline virtualizer debounce before teardown. Verified at code commit e5cb139f.


- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  stage-surface suite split from `SessionsView.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
