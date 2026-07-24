# dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Conversation renderer overview](overview.md)

## Purpose

Pins the SSE working line as a pure status cue.

## Code Commentary

### Logic

Projection helpers seed stream, turn state, timestamps, and freshness. The suite asserts the live
working cue, bounded elapsed/stale rendering, suppression when evidence is insufficient, and absence
of a line-hosted stop control.

### Conventions

Tests read the active-conversation store rather than reproducing a separate status model.

### Invariants And Boundaries

The stop action must remain in `SessionComposer`; this suite guards against moving it back into a
status line because that would duplicate controlled-seat controls.

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
| Helpers and cases pin working, elapsed, stale, and cue-only behavior. | L1-L126 | [ConversationWorkingLine.test.tsx](ConversationWorkingLine.test.tsx) |
| Component under test. | L47-L98 | [ConversationWorkingLine.tsx](ConversationWorkingLine.tsx) |
| Controlled stop owner. | L660-L715 | [SessionComposer.tsx](../../SessionComposer.tsx) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-07-24T13:17:17Z — Curator: created the SSE working-cue regression-suite sidecar. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
