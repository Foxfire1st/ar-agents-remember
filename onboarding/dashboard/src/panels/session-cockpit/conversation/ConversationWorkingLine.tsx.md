# dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Conversation renderer overview](overview.md)

## Purpose

Renders the SSE-preferred working cue for a focused live harness conversation.

## Code Commentary

### Logic

The line reads active-conversation stream/status evidence and renders only a current working cue,
optional elapsed duration, and an explicit stale marker. It owns no stop control; the controlled
session composer renders that exact-turn action beside Send from the same evidence.

### Conventions

It is selected by `SessionsView` only for a live harness stream. Catalog `WorkingLine` remains the
fallback for raw sessions and the stream connect/reconnect interval.

### Invariants And Boundaries

The component must never present a stop button or invent a working turn when stream/status evidence
is absent. Its status wording is a cue, not a second control surface.

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
| SSE status drives working, elapsed, and stale rendering without any control. | L1-L98 | [ConversationWorkingLine.tsx](ConversationWorkingLine.tsx) |
| Stage composition selects this only for a live harness stream. | L1199-L1230 | [../SessionsView.tsx](../SessionsView.tsx) |
| Focused tests pin cue-only behavior. | L63-L126 | [ConversationWorkingLine.test.tsx](ConversationWorkingLine.test.tsx) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-07-24T13:17:17Z — Curator: created the SSE working-cue sidecar. It is uncommitted, so
  verification fields are intentionally blank until closeout stamps the code commit.
