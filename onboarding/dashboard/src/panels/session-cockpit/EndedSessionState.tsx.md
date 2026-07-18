# dashboard/src/panels/session-cockpit/EndedSessionState.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/EndedSessionState.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate |  2026-07-18T07:47:42+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Cross-Repo References

The ended-state projection uses repository-local session/state grammar only; no cross-repository source applies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Host and inspectability boundary. | [PtySurface.tsx](PtySurface.tsx) |

## Update History

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 ended-versus-landed presentation; verification
  metadata remains blank until commit.
