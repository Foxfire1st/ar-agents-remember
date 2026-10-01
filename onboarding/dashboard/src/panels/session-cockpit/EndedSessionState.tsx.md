# dashboard/src/panels/session-cockpit/EndedSessionState.tsx

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

No configured Domain Documentation source exists for this file.

### Cross-Repo References

The ended-state projection uses repository-local session/state grammar only; no cross-repository source applies.

No applicable cross-repository source was found.

### Repo-Internal References

- Host and inspectability boundary. [1]
