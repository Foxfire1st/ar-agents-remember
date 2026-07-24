# dashboard/src/panels/session-cockpit/conversation/ConversationSurface.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationSurface.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Helpers seed projection/visibility variants for the surface. | L1-L88 | [ConversationSurface.test.tsx](ConversationSurface.test.tsx) |
| Hidden gating, latest chip, and scroll wiring are covered. | L89-L314 | [ConversationSurface.test.tsx](ConversationSurface.test.tsx) |
| Implementation under test. | L55-L226 | [ConversationSurface.tsx](ConversationSurface.tsx) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-07-24T13:17:17Z — Curator: created the conversation-surface regression-suite sidecar. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
