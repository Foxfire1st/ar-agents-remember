# dashboard/src/panels/SessionList.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/SessionList.test.tsx`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T23:56:42+02:00                           |
| lastVerifiedCommitHash | `278a7bf789ceca4378b0de44ba9fae4ec2f1d4b2`       |
| lastVerifiedCommitDate | 2026-07-06T13:30:12+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest render + interaction tests for `SessionList` (slice 6e-2c). Because the switcher is pure +
presentational (no backend, no lazy xterm), the tests drive it directly — unlike the Chats render-only
tests, which must never click a launch button (that would Suspense-load xterm into jsdom).
Task 11 adds a render assertion for the optional lifecycle tag badge. Task 22 adds non-running status
badge coverage; the Task 22 follow-up removes the old local Hide assertion and keeps only destructive
Terminate action coverage. The L5 fix pass adds **hover-title (fix 4)** coverage: a long label exposes its
full text through a `title` so the row's CSS ellipsis stays readable, and a bound session's `title` also
appends the resolved leaf name. 260703-L14 adds a second describe, **"SessionList command tree
(L14)"**, driving the grouped rendering with hand-built `SessionGroup` fixtures (membership
derivation is covered separately in `data/sessionGroups.test.ts`).

## Code Commentary

### Logic

Seven cases over a two-session fixture: (1) a row renders per session and the active row carries React
Aria's `data-selected`; (2) an attached session renders its `lifecycleId`; (3) a non-running session
renders its status tag; (4) `fireEvent.click` on a row reports the new id via `onSelect`; (5) a long
label is truncated but its full text is exposed via a hover `title` — `getByTitle(longLabel)` resolves
(fix 4); (6) a bound session passes a `leafNameFor` resolver and `getByTitle("Claude Code 1 · Sidebar
chat")` proves the `title` appends the resolved leaf name (fix 4); (7) Terminate reports `onTerminate`
separately and does not select the row.
`fireEvent.click` is the repo idiom for driving
React Aria interaction (see `Cockpit.test.tsx` / `DetailPanel.test.tsx`).

The L14 command-tree describe adds six grouped cases over a `group()` fixture builder: (1) group
headers render chevron + insignia + name + counts (`aria-expanded`, `data-rank-tier`/`data-rank-size`
hooks, the commanded master section carrying `data-nested` and containing its member row); (2) the
landed archive is collapsed by default (rows unmounted, no insignia) and each header click toggles
`aria-expanded`/row mounting; (3) a default-collapsed group holding the ACTIVE session auto-expands,
and the user's explicit collapse still wins afterwards; (4) ungrouped sessions render outside every
`chats-group-*` section (the flat placement below); (5) a zero-group model renders the pre-L14 flat
list (no `chats-session-tree`, selection intact); (6) a `spawnRole` session renders its
`chats-session-role-{id}` chip and a role-less one renders none.

### Invariants And Boundaries

Render + interaction only; no backend, no WebSocket, no xterm. The selection assertion reads React
Aria's emitted `data-selected` rather than a CSS class, so it tracks the primitive's real state.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | — | [SessionList.tsx](SessionList.tsx) |

## Update History

- 2026-07-06T23:56:42+02:00 — 260703-L14 (visual hierarchy + chat grouping): added the "SessionList
  command tree (L14)" describe — grouped headers with insignia + counts, landed default-collapse +
  toggle, the active-session auto-expand exception, ungrouped-flat-below, the zero-group flat
  fallback, and spawn-role chip coverage. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: added two hover-title (fix 4) cases — a long label exposes its full text via
  a `title` (`getByTitle(longLabel)`) so the row ellipsis stays readable, and a bound session's `title`
  appends the `leafNameFor`-resolved leaf name (`"Claude Code 1 · Sidebar chat"`). Verification metadata
  pinned until closeout stamps the L5 commit.
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
