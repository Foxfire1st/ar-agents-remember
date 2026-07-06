# dashboard/src/cockpit/Cockpit.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/cockpit/Cockpit.test.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-07T10:50+02:00                           |
| lastVerifiedCommitHash | `6ea2a422210b4b9797d2c7c8df5f9994813f9331`       |
| lastVerifiedCommitDate | 2026-07-06T21:07:46+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Vitest + `@testing-library/react` render test pinning the slice 5f S1 full-bleed behaviour: the
machine-map views drop the cockpit rails while the others keep them. The first component-render test in
the dashboard suite (prior tests are pure logic/selector). Slice L5 adds the right-rail River⇄Chat toggle
and (L5 fix 1) a regression that the rail chat keys by the leaf the detail panel is **displaying**: after
drilling into a master's sub-task the rail heading is the drilled **leaf** id, not the master.

## Code Commentary

### Logic

L15 adds the servingBuild stamp assertions (renders commit + boot time when present; absent-field tolerance for old payloads).

A local `seed(stateName)` applies a `GALLERY` fixture projection to the real Zustand store
(`dashboardStore.getState().applySnapshot(...)`) — the same hydration the dev bench uses. The lazy
`../panels/Terminal` is mocked to a jsdom-safe stub so toggling the rail to chat never pulls xterm (a
canvas probe) into jsdom. `afterEach` runs RTL `cleanup`, resets the `sessions` store, and resets the
dashboard store.

- "rails the Operations view but goes full-bleed for the Engine Room" — seeds `engine-fleet`, renders
  `<CockpitShell />`, asserts the default Operations view has `.shell__body[data-fullbleed="false"]`
  plus both `.rail--left`/`.rail--right`; clicks the `role="radio"` "Engine Room" mode-bar toggle and
  asserts `data-fullbleed="true"`, both rails gone, and the room's `engine-room-header` +
  `engine-room-diagnostics` zones present.
- "keeps the rails for Operations and Memory" — switching to Memory stays railed (`data-fullbleed="false"`).
- "keeps <Chats> mounted (hidden) on other views and shows the same node on Chats" (slice 6e-4) —
  asserts `[data-testid="chats"]`'s parent layer is `display:none` on the default Operations view,
  clicks the "Chats" mode-bar radio and asserts the **same** DOM node is now `display:flex` (never
  remounted), then switching back to Operations hides it again — pinning that a view switch never tears
  down the live terminal.
- "toggles the right rail between the Event River and the leaf chat" (slice L5) — on a railed view the
  default `rail--right` shows the Event River; clicking the `rail-toggle-chat` `role="radio"` segment
  swaps in the single-instance `RailChat` (`rail-chat` testid), and clicking `rail-toggle-river` swaps
  the Event River back, pinning the `railView` switch without unmounting the railed body.
- "rail chat keys by the drilled leaf, not the master" (L5 fix 1) — a local `seedDrillableMaster` (+ a
  `taskDoc` factory) seeds a lifecycle-bound master with one authored, drillable leaf. The test selects
  the master, toggles the rail to chat, and asserts the master overview shows no leaf slot yet
  (`rail-chat-no-leaf`); drilling into the master's `subtask-open-1` then makes the `rail-chat-heading`
  contain the **leaf** id (`leaf-one`) and not the master id (`master-x`) — pinning that the rail keys off
  the displayed leaf (via `DetailPanel.onViewLeaf` → the shell's `viewedLeafKey`).

### Invariants And Boundaries

Relies on the shared jsdom stubs in `test/setup.ts` (`matchMedia` for `useShouldAnimate`, `ResizeObserver`
for React Aria). The ModeBar items are queried by `role="radio"` (React Aria `ToggleButtonGroup`,
single-select), driven by `fireEvent.click`. Uses plain `container.querySelector` + vitest `expect`
(no `@testing-library/jest-dom`). Pure render assertions — no network, no live stream.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `CockpitShell` under test (full-bleed rails-hide). | L124-L205 | [Cockpit.tsx](Cockpit.tsx) |
| `GALLERY` fixtures + the `applySnapshot` hydration pattern. | — | [dev/fixtures.ts](../dev/fixtures.ts) |
| The shared jsdom stubs the render relies on. | — | [test/setup.ts](../test/setup.ts) |

## Update History

- 2026-07-07T10:50+02:00 — L15: servingBuild stamp tests added. Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-07T05:26+02:00 — 260703-L15 S3: added the serving-build stamp describe — the muted
  stamp renders the snapshot's commit short-hash + "up <boot time>", falls back to `v<version>`
  when the stamp has no commit, and renders NOTHING when the wire carries no `servingBuild`
  (a pre-L15 server; never faked).
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: added a `seedDrillableMaster` (+ `taskDoc` factory) and a "rail chat keys by
  the drilled leaf, not the master" case — drilling a master's sub-task makes the `rail-chat-heading` the
  leaf id, not the master, pinning the displayed-leaf key (L5 fix 1). Also mocked the lazy
  `../panels/Terminal` (jsdom-safe) and reset the `sessions` store in `afterEach`. Verification metadata
  pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added a right-rail River⇄Chat toggle case — clicking the
  `rail-toggle-chat` radio swaps the Event River for the single-instance `RailChat` and
  `rail-toggle-river` swaps it back, pinning the `railView` switch on a railed view. Verification metadata
  pinned until closeout stamps the L5 commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: added the "Chats persistence across view switches" describe — pins that `<Chats>` stays mounted (its parent layer toggles `display` none↔flex) across a view switch and is the **same** DOM node throughout, so the live terminal is never re-created. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-16T02:30 — Created for slice 5f S1: render test pinning the full-bleed rails-hide (Engine
  Room / Topology) vs railed (Operations / Memory) behaviour. Verification metadata pinned until
  closeout stamps the S1 code commit.
