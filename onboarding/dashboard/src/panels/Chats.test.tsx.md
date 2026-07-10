# dashboard/src/panels/Chats.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Chats.test.tsx`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`       |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Render tests for the **Chats** view's per-harness launch buttons (slice 6e-2b): proves a launch
button appears for each **detected** harness and not for undetected ones, and that ＋ Terminal is
always present (including when no backend reports harnesses). Slice 6e-4 / task 22 now cover
session-tab **persistence** through mount-on-first-selection: only the active restored session is mounted
initially, and switching active sessions mounts the selected row while keeping the previously visited
terminal mounted.
Task 11 adds coverage for attaching the active untagged hosted session to the selected lifecycle. Task
22 adds coverage for durable catalog hydration, exited restored rows, backend-backed terminate, and
cross-tab catalog refresh after another tab ends the last session. The Task 22 follow-up adds a stale
catalog echo regression so a remote terminate with `sessionId` cannot resurrect a ghost row. Slice L5
adds leaf-attach coverage: a `200` attach binds the leaf, a `409` is rejected with a "leaf already has a
chat" note, and the session-row leaf label resolves a task-doc title with an id fallback. L9 adds
attached-chat move coverage and live catalog refresh coverage for `"leaf"` invalidations from another
browser tab or agent-facing reassignment.

## Code Commentary

### 260707-HFX2-L17 Chats Role-Selection Proof

Attach/move interaction now chooses a role before a leaf, verifies the role-bearing backend call,
and checks role-specific same-pair conflict feedback.

### Logic

Two `@testing-library/react` cases stub the global `fetch` (the `GET /api/harnesses` call `Chats`
makes on mount). The first returns three harnesses (claude+codex detected, pi not) and asserts (via
`findByTestId`, awaiting the async detection) that `chats-new-harness-claude` / `-codex` render with
their names and `chats-new-harness-pi` does not, while `chats-new-terminal` stays. The second rejects
`fetch` (no backend) and asserts only ＋ Terminal renders. The persistence case (slice 6e-4 / task 22)
mocks the lazy `./Terminal` to a jsdom-safe stub, seeds two sessions in the `sessions` store, and
asserts only the active restored `term-*` stub is mounted at first; a `setActive` then mounts the newly
selected row and keeps the previously visited terminal mounted but hidden. This pins the restored-harness
fix without losing tab-switch buffers.
The Task 11 case renders `<Chats selectedLifecycleId="LC1">` with one active untagged session, clicks
`chats-attach-lifecycle`, and asserts the session store now carries `lifecycleId: "LC1"`. Task 22 adds
URL-aware fetch mocks because `Chats` now calls both `/api/harnesses` and `/api/terminal/sessions` on
mount: one case hydrates a running catalog row and asserts the restored terminal layer mounts active;
one case hydrates an exited row and asserts a status panel renders with no terminal; one case dispatches
a remote `BroadcastChannel` terminate event with `sessionId` after changing the mocked catalog to an
empty successful response and asserts the local row disappears; one case keeps the mocked catalog stale
with the same row and asserts the remote terminate still does not resurrect it; and one case clicks
Terminate, waits for the backend success path before the row disappears, and asserts an id-bearing
catalog-change broadcast is posted.
Slice L5 adds leaf-attach cases. The decoupled flow is driven through the **"Attach to leaf ▾" picker**
(`chats-attach-leaf-picker`) via `fireEvent.change`, with `kind:"subTask"` leaf docs in `taskDocuments`:
the key case renders `<Chats taskDocuments=…>` with **NO `selectedLeafKey`** and an active untagged session,
asserts the projected leaf is listed in the picker, and a stubbed `200` from
`/api/terminal/{id}/attach-leaf` binds `leafKey` on the store row (and posts a catalog-change broadcast) —
proving attach works from anywhere; a stubbed `409` leaves the session unbound and renders the
`chats-leaf-attach-error` "leaf already has a chat" note. A separate case asserts the `＋ Terminal`/harness
launch buttons are enabled with nothing selected (free-chat creation is never gated). A leaf-name case
asserts a bound session's `chats-leaf-badge` / `chats-session-leaf-*` shows the matching task-doc title, and
falls back to the leaf id (`leafIdFromKey`) when no doc title resolves.
L9 adds a second task leaf fixture and two reassignment cases: an already-attached session still shows the
leaf picker, selecting another leaf updates the store on a stubbed `200`, and a remote `"leaf"`
BroadcastChannel invalidation causes the view to re-fetch `/api/terminal/sessions` and hydrate the moved
`leafKey`.
**HFX2-L11** adds two landed-archive cases. The `Terminal` mock is extended to forward `readOnly` as a
`data-readonly` attribute so tests can observe it. The first hydrates a catalog row with
`status:"landed"` and asserts its `Terminal` mounts with `data-readonly="true"`, with no status badge or
composer rendered for it (a landed row is a read-only inspection attachment, not an interactive session).
The second seeds a landed row and a running row via both the store and a stubbed catalog `GET`, clicks
the group's `chats-group-cleanup-landed` control, and asserts: the backend `POST
/api/terminal/landed-cleanup` receives only the landed row's id, the local store drops the closed row
(only `"active"` remains) once the stubbed response reports `closed:1`, a `chats-landed-cleanup-status`
node renders the "1 closed · 0 skipped" summary, and a `terminal-catalog-changed`/`"terminate"`
broadcast is posted so other tabs converge.

### Conventions

The harness-button cases are **render-only — they never click a launch button**, because opening a
session would Suspense-load the lazy `Terminal` and pull xterm (a canvas probe) into jsdom. The 6e-4
persistence case *does* open sessions, but `vi.mock("./Terminal")` swaps the lazy terminal for a stub
so xterm stays out of jsdom. `afterEach` runs `cleanup` + `vi.unstubAllGlobals`, clears localStorage,
resets the `sessions` store to its current shape (`sessions`, `activeId`, `count`), and resets the test
`FakeBroadcastChannel`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Chats view under test keeps the picker visible for attached sessions, handles attach/move outcomes, and rehydrates catalog changes. | L256-L275; L303-L318; L374-L388 | [Chats.tsx](Chats.tsx) |
| The L9 tests add a second leaf, move an attached chat on `200`, and rehydrate a `"leaf"` catalog invalidation from another tab. | L8-L31; L354-L381; L405-L451 | [Chats.test.tsx](Chats.test.tsx) |
| The `fetchHarnesses` / catalog hydrate / terminate client the view drives. | L253-L315 | [data/terminal.ts](../data/terminal.ts) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: updated Chats attach coverage for explicit role
  selection and pair-scoped conflict copy.

- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive): added ~129 lines of coverage for the
  landed-archive view — a `status:"landed"` row renders as non-live/inspectable with landing
  reason/timestamp/provenance, mounts its `Terminal` with `readOnly` (no write affordances/composer),
  and the "Close landed archive" group-cleanup control invokes the backend endpoint and surfaces
  closed/skipped counts. Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-02T17:04+02:00 — L9: added coverage that an attached chat still renders the leaf picker and
  moves to another leaf on server `200`, plus a BroadcastChannel `"leaf"` invalidation case that rehydrates
  the moved catalog binding. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: reworked the leaf-attach cases to drive the **"Attach to leaf ▾" picker**
  (`fireEvent.change`, `kind:"subTask"` docs) — the key case now asserts attach works with **no
  `selectedLeafKey`** (any-leaf, from anywhere), plus a case that the launch buttons are enabled with nothing
  selected. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added leaf-attach coverage — a `200` attach binds `leafKey` (and posts
  a catalog broadcast), a `409` keeps the session unbound and shows the "leaf already has a chat" note,
  and the session-row leaf label resolves a task-doc title with a leaf-id fallback. Verification metadata
  pinned until closeout stamps the L5 commit.
- 2026-06-27T03:04+02:00 — Task 22 follow-up: removed local Hide coverage, required terminate
  broadcasts to include `sessionId`, and added a stale-catalog echo regression proving another tab's
  terminate cannot repaint the row.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: added a `FakeBroadcastChannel`, a remote empty-catalog
  refresh case proving another tab's terminate clears this tab's stale chat row, and a sender assertion
  that backend-confirmed End posts a terminate invalidation. Verification metadata pinned until closeout
  stamps the task-22 follow-up code commit.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: reset the new session-store reserved-label state between
  Chats render tests; label allocator behavior itself is covered in `data/sessions.test.ts`.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: changed the session-tab persistence test to assert
  mount-on-first-selection plus kept mounted visited terminals, preventing hidden restored terminals
  from hydrating broken TUIs without losing tab-switch buffers.
- 2026-06-26T23:05+02:00 — Task 22: added URL-aware fetch mocks for catalog hydration, running-row
  terminal restore, exited-row status rendering, local Hide, backend-backed Terminate, and localStorage
  cleanup between cases. Verification metadata pinned until closeout stamps the task-22 code commit.
- 2026-06-23T13:45+02:00 — Task 11: added active-session attach coverage for `selectedLifecycleId`.
  Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: added a session-tab persistence test (`vi.mock("./Terminal")` stub + seeded `sessions` store) asserting every open session's terminal stays mounted and switching only flips which `chats-terminal-layer-*` is shown. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-18T21:27 — Created for task 6 slice 6e-2b: covers the detection-driven harness launch
  buttons in `Chats.tsx` (a button per detected harness; ＋ Terminal always present). Verification
  metadata pinned to the task base until closeout stamps the 6e-2b code commit.
