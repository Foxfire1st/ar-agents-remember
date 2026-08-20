# dashboard/src/panels/session-cockpit/conversation/ConversationSurface.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationSurface.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Conversation renderer overview](overview.md)

## Purpose

Tests the surface-level wiring for hidden keep-alive behavior, current-position navigation, and
scroll-memory handoff into the timeline.

## Code Commentary

### Logic

The suite seeds active projections and rerenders visibility/geometry states. It checks suppressed
announcements while hidden, the explicit latest action, current empty/welcome composition, and
scroll-memory persistence across the surface-to-timeline boundary.

### Conventions

The test keeps data setup in small projection helpers and uses the real active-conversation store.

### Invariants And Boundaries

Hidden surfaces keep tracking but do not announce. The latest control is an explicit user action,
not a reason to silently override a reader's saved position.

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
| Helpers seed projection/visibility variants for the surface. | `seed` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.test.tsx:59-70 |
| Hidden gating, latest chip, and scroll wiring are covered. | "ConversationSurface hidden keep-alive gating (F-j)"; "ConversationSurface — latest chip (B3)"; "ConversationSurface — the scroll-up trap" | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.test.tsx:89-122; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.test.tsx:124-184; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.test.tsx:186-314 |
| Implementation under test. | `ConversationSurface` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:269-341 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## 260815-DAG Master Full-Gate Repair

`afterEach` is now async and flushes the conversation timeline virtualizer's 150 ms scroll debounce (fake-timer clear + real-timer 200 ms settle) before jsdom teardown.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: async `afterEach` flushes the timeline virtualizer debounce before teardown. Verified at code commit e5cb139f.


- 2026-08-03T02:38:40+02:00 — W3-B01 curator: curated 3 Repo-Internal table citations with exact test helper, regression-suite, and implementation anchors. Verification metadata remains unchanged for closeout.
- 2026-07-24T13:17:17Z — Curator: created the conversation-surface regression-suite sidecar. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
