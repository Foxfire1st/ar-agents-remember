# dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixed-anatomy case pins the live working cue and elapsed value derived from `stateSince`. | "renders the fixed anatomy on a live working turn" | dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx:64-73 |
| The remaining cases pin canonical working states, live/working gating, elapsed omission, stale rendering, and the absence of a line-hosted stop control. | "shows the canonical wire word for the other working-set states — never an invented verb"; "renders ONLY while the stream is live AND the turn state is in the working set"; "omits elapsed when stateSince is null"; "appends the visible stale marker ONLY on a stale freshness block"; "renders NO stop control (F-at: the ⏹ stop lives in the composer beside send)" | dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx:75-85; dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx:87-97; dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx:99-103; dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx:105-114; dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.test.tsx:116-125 |
| Component under test. | `WORKING_TURN_STATES` | dashboard/src/panels/session-cockpit/conversation/ConversationWorkingLine.tsx:45-45 |
| Controlled stop owner. | "data-disabled-reason" | dashboard/src/panels/sessionComposerParts.tsx:328-328 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: narrowed the existing range to the case it proves and added one provisional binding using the exact five source test names for canonical states, live/working gating, elapsed omission, stale rendering, and cue-only behavior.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-24T13:17:17Z — Curator: created the SSE working-cue regression-suite sidecar. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
