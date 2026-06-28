# dashboard/src/panels/SessionList.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/SessionList.test.tsx`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T03:04+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest render + interaction tests for `SessionList` (slice 6e-2c). Because the switcher is pure +
presentational (no backend, no lazy xterm), the tests drive it directly — unlike the Chats render-only
tests, which must never click a launch button (that would Suspense-load xterm into jsdom).
Task 11 adds a render assertion for the optional lifecycle tag badge. Task 22 adds non-running status
badge coverage; the Task 22 follow-up removes the old local Hide assertion and keeps only destructive
Terminate action coverage.

## Code Commentary

### Logic

Five cases over a two-session fixture: (1) a row renders per session and the active row carries React
Aria's `data-selected`; (2) an attached session renders its `lifecycleId`; (3) a non-running session
renders its status tag; (4) `fireEvent.click` on a row reports the new id via `onSelect`; (5)
Terminate reports `onTerminate` separately and does not select the row.
`fireEvent.click` is the repo idiom for driving
React Aria interaction (see `Cockpit.test.tsx` / `DetailPanel.test.tsx`).

### Invariants And Boundaries

Render + interaction only; no backend, no WebSocket, no xterm. The selection assertion reads React
Aria's emitted `data-selected` rather than a CSS class, so it tracks the primitive's real state.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | — | [SessionList.tsx](SessionList.tsx) |

## Update History

- 2026-06-27T03:04+02:00 — Task 22 follow-up: removed local Hide/onDetach coverage and kept the row
  action test focused on End/Terminate not selecting the row.
- 2026-06-27T00:33+02:00 — Task 22 follow-up: updated action coverage for the visible `Hide` label so
  local-only hiding cannot be mistaken for destructive `End`.
- 2026-06-26T23:05+02:00 — Task 22: updated props from close to detach/terminate, added non-running
  status tag coverage, and split action assertions so destructive Terminate is pinned separately from
  local Detach. Verification metadata pinned until closeout stamps the task-22 code commit.
- 2026-06-23T13:45+02:00 — Task 11: added lifecycle tag render coverage. Verification metadata pinned
  until closeout stamps the task-11 code commit.
- 2026-06-19T14:05 — No content impact: slice 6e-4 only re-pointed the `OpenSession` type import to `../data/sessions` (the store now owns the row shape); the rendered/asserted behavior of these tests is unchanged. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T04:38 — Created for task 6 slice 6e-2c: render + interaction tests for the new `SessionList` switcher (selection reflects `activeId`; row click → `onSelect`; close ✕ → `onClose` without selecting). Verification metadata pinned until closeout stamps the 6e-2c code commit.
