# dashboard/src/cockpit/Cockpit.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/cockpit/Cockpit.test.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `../overview.md`                                |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Vitest + Testing Library coverage for production cockpit composition, persistent layers, selection
routing, takeovers, and store updates. The FEUI-L8 cases pin Operations as initial, one Chats item,
no Sessions item or legacy Chats layer, persistent Chats mounting, shell-level reconciliation, and
accepted-id-only highlight routing.

## Code Commentary

### Logic

L15 adds the servingBuild stamp assertions (renders commit + boot time when present; absent-field tolerance for old payloads).

260712-TRH-L1 adds a shape-accurate Operations projection and fetch stub for the permanently mounted
cockpit surfaces. It clicks a direct leaf, master, drilled subtask, and lifecycle-bound row while
changing only summary projection objects; each path proves one body request for the unchanged revision
and renders the complete objective after resolution. A second case holds task A, switches to task B,
resolves A late, and proves A cannot contaminate B; B remains one request and hydrates only after its
own response. The fetch fixture returns the response shapes required by the mounted file, harness,
terminal, change-set, and notes surfaces, modeling composition rather than adding production fallback
behavior.

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
- "Sessions view: full-bleed keep-alive layer" (260715-FEUI-L1 R1) — seeds `engine-fleet` and pins
  the Chats keep-alive pattern for the new Sessions view: the `sessions-view` node is mounted from
  the start inside a `display:none` + `aria-hidden="true"` layer, already carrying the
  `data-view="sessions"` WebTUI scope marker while hidden; clicking the "Sessions" mode-bar radio
  goes full-bleed (`data-fullbleed="true"`, no `.rail--left`) and reveals the **same** DOM node
  (`display:flex`, `aria-hidden="false"` — React renders aria booleans literally); leaving hides it
  again without unmounting.
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
(no `@testing-library/jest-dom`). Older cases are pure render assertions; the new body cases stub
browser `fetch` and drive `dashboardStore.applyDelta("analytics", ...)` to reproduce analytics churn
and selection timing.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `CockpitShell` under test (full-bleed rails-hide). | L124-L205 | [Cockpit.tsx](Cockpit.tsx) |
| `GALLERY` fixtures + the `applySnapshot` hydration pattern. | — | [dev/fixtures.ts](../dev/fixtures.ts) |
| The shared jsdom stubs the render relies on. | — | [test/setup.ts](../test/setup.ts) |
| The L1 composition cases cover all four reader entry paths, unchanged-revision analytics churn, and late A-to-B response discard. | L329-L434 | [Cockpit.test.tsx](Cockpit.test.tsx) |

## FEUI-L8 Reviewed Candidate Delta

Pins the L8 product cutover: Operations is the initial route, the mode bar has one Chats item and no Sessions item, and one persistent Chats layer survives route changes. Highlight delivery switches/focuses only the accepted exact session.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T00:25+02:00 — 260715-FEUI-L1 (R1): added the "Sessions view: full-bleed keep-alive
  layer" describe — same-node identity across switches, display/aria-hidden toggling, full-bleed
  rails-hide, and the scope marker present while hidden. Pure addition; no existing case changed.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
- 2026-07-12T16:45+02:00 — 260712-TRH-L1 reopen correction: added Operations click-to-detail
  composition coverage for direct leaf, master, drilled, and lifecycle-bound readers under analytics
  summary churn, plus a pending A-to-B switch with late A resolution. Verification metadata remains
  blank until closeout stamps the code commit.

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
