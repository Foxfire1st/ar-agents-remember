# dashboard/src/panels/session-cockpit/EndedSessionState.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/EndedSessionState.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

Renders an explicit focused-stage overview for exited or retired chats that have catalog evidence but
no inspectable terminal.

## Code Commentary

Shows the normalized state word, label, retirement/exit evidence, and the honest absence of live
terminal and messaging. It is focusable as a stage region but is not a PTY keyboard zone.

## Invariants And Boundaries

Ended rows must never create a socket or empty terminal. Landed rows are different: their existing
PTY remains mounted read-only for transcript inspection.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Cross-Repo References

The ended-state projection uses repository-local session/state grammar only; no cross-repository source applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Host and inspectability boundary. | `isInspectable`; `PtySurface` | dashboard/src/panels/session-cockpit/PtySurface.tsx:132-134; dashboard/src/panels/session-cockpit/PtySurface.tsx:136-336 |

## Update History

- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the scoped ended-session citation claim; final exact frozen-snapshot check is clean.
- 2026-07-18T07:22+02:00 — Created for FEUI-L8 ended-versus-landed presentation; verification
  metadata remains blank until commit.
