# dashboard/src/cockpit/Cockpit.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/cockpit/Cockpit.test.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-19T14:05                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Vitest + `@testing-library/react` render test pinning the slice 5f S1 full-bleed behaviour: the
machine-map views drop the cockpit rails while the others keep them. The first component-render test in
the dashboard suite (prior tests are pure logic/selector).

## Code Commentary

### Logic

A local `seed(stateName)` applies a `GALLERY` fixture projection to the real Zustand store
(`dashboardStore.getState().applySnapshot(...)`) — the same hydration the dev bench uses; `afterEach`
runs RTL `cleanup`.

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

- 2026-06-19T14:05 — Task 6 slice 6e-4: added the "Chats persistence across view switches" describe — pins that `<Chats>` stays mounted (its parent layer toggles `display` none↔flex) across a view switch and is the **same** DOM node throughout, so the live terminal is never re-created. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-16T02:30 — Created for slice 5f S1: render test pinning the full-bleed rails-hide (Engine
  Room / Topology) vs railed (Operations / Memory) behaviour. Verification metadata pinned until
  closeout stamps the S1 code commit.
