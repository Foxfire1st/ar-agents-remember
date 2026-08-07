# dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `7c56c11d651972515723b4090b8174087eb5236f`|
| lastVerifiedCommitDate |  2026-08-07T20:50:27+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| SSE status drives working, elapsed, and stale rendering without any control. | `ConversationWorkingLine` | dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.tsx:47-98 |
| Stage composition selects this only for a live harness stream. | "const { focused, focusedLive, focusedConversationLive, perSession } = data;"; "<ConversationWorkingLine sessionId={focused.id} />" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:186-186; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:195-195 |
| Focused tests pin cue-only behavior. | "working-line-stop" | dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx:116-124 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:43:37+02:00 — W3-B05 curator: anchored 3 Tier-2 table citations with exact source paths; fixer generated all ranges.
- 2026-07-24T13:17:17Z — Curator: created the SSE working-cue sidecar. It is uncommitted, so
  verification fields are intentionally blank until closeout stamps the code commit.
