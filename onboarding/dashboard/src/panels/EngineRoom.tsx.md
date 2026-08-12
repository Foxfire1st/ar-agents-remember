# dashboard/src/panels/EngineRoom.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/EngineRoom.tsx`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`       |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## 260731-EFA-L8 Change

The engine-room style module split moved `engineRoomStyles` imports to the new
`engine-room/styles` barrel (which re-exports the six style domains); rendering and
data flow are unchanged.

## Purpose

The engine room (note 08 twin-engine pod): each worktree's provider stack = CGC (its code repo) +
GrepAI (its memory repo). It builds a render model with `buildEngineRoomModel` and surfaces the
shared workspace (official/main) stack as an official-line strip on top, plus every worktree's own
enclosure process. As of slice 5f S1 the room owns a **full-width 3-zone layout** (§4.2): a header
strip over [enclosure stack list | pod stage (process map) | boot timeline + diagnostics on the
RIGHT]. A legacy `groupEngines` fallback still renders flat provider stacks for older projections.

## Code Commentary

### Logic

The panel reads `analytics`, `providers`, and `lifecycles` from the store and calls
`buildEngineRoomModel(engineProcesses, providers, lifecycles)` — a pure seam that joins each
server-composed enclosure process to its live lifecycle, lifts the workspace-scoped engines, sets each
view's `enclosureKey` (= worktreeGroup), and flags `usesFallback`. The render branches on the model:

- `model.usesFallback` (no `engineProcesses`, but worktree providers exist) → `FallbackStacks`, the
  legacy `groupEngines`-derived view (`engine-stack` / `engine-unit` testids).
- no selected process → empty state (`engine-room-empty`).
- otherwise → the §4.2 `roomShell`: `EngineRoomHeader` over a `roomGrid` of `EnclosureStackList`
  (zone 1), the `roomStage` `pod-stage` holding `EnclosureProcessMap` (zone 2), and a `roomZone`
  `engine-room-diagnostics` stacking `BootTimeline` + `DiagnosticsPanel` (zone 3, right). The selected
  process is resolved by `view.node.worktreeGroup === selectedGroup`, falling back to the first.

The room's `<Panel>` is rendered with **`fill`** (the new bounded-height variant) so the 3-zone grid
resolves against a fixed height — the centre canvas + right diagnostics no longer resize per selection and
the side columns scroll on their own. `EnclosureProcessMap` is passed `model.workspaceEngines` so the
bird's-eye renders the **left** official-line engines from the same real provider stack the
`OfficialStrip` summarises above the body. Slice 5h also resolves the **official ledger** for the OFFICIAL
coupler popover: the panel reads `analytics.ledgers` and finds the `LedgerNode` whose `repository` matches
the selected enclosure's `repoName`, passing it down as `officialLedger` (the worktree coupler reads its
window straight off `node.ledgerRows`, so it needs no prop). Task 11 also passes `selected.gate` into
`EnclosureProcessMap` and passes `selected.lifecycle?.id` + `selected.gate` into `DiagnosticsPanel`, making
diagnostics the Engine Room's secondary Gate Respond surface for worktree-bound projected gates.

Slice 5o keys the centre canvas by the store **generation counter**: the panel reads `state.gen` and
passes `key={gen}` to `EnclosureProcessMap`. When the dev bench switches scenario it calls `store.reset()`,
which bumps `gen`, so the new key forces React to **remount** the canvas cleanly — preventing an exiting
Motion failure-overlay from the previous mode (e.g. `FleetingEnclosure`) from orphaning mid-`AnimatePresence`
and bleeding through into the next scenario's view (which surfaced behind the scenario dropdown). In
production `gen` is constant (`0`), so the canvas is never remounted by it there; the remount is dev-bench-only.

`EngineRoomHeader({ node })` shows the selected enclosure's leaf label (`leafId || taskName`) · health dot + health ·
`phaseChip(phase)` · parent `taskName` when a leaf is present · `repoName`, the optional `nextAction`, and — pushed right by a spacer — the
**master-caution** badge (`roomCaution({ sev })`, `⚠ N waiting`) read from `selectQueue` (§4.1: an
alarm is never hidden by a full-bleed view; mirrors the always-visible top-bar caution). Slice 5f S5: the
`phaseChip` is a `motion.span` that **pulses** while `node.phase ∈ LIFECYCLE_PHASES` (the human-gated
landing beats — sync / closeout / commit-approval / integration / cleanup, T12–T18) — gated by
`useShouldAnimate`, instant under `data-effects=off`; the header also carries `data-phase-active` for the
test. `OfficialStrip` renders `model.workspaceEngines` above the body and groups that official workspace
stack by provider label + `engineState`: duplicate same-state peers render as a counted chip
(`7 CGC · nominal`), while singletons keep the ordinary label (`GrepAI · nominal`, `CGC · down`). Each chip
uses the grouped runtime state for `engineSilhouette` and puts the grouped mainline repos in its `title` /
`aria-label`; the repo label comes from `repoId`, falling back to `id` because `repoId` is optional in the
projection contract. `engineLabel` maps `role==="memory"` → GrepAI, else CGC.

### Invariants And Boundaries

The server composes the enclosure-centered process nodes with their fact-state honesty, so this seam
does no inference — no clock, no git, no safety derivation. Selection is keyed by `worktreeGroup`
(`enclosureKey`), stable across a fleeting→real promotion. State is carried by colour + silhouette; the
down state pulses (≤3/s). The room's 3-zone layout assumes the full body width the cockpit gives it in
the (rail-less) Engine Room view (5f §4.1); the `Panel fill` keeps it at that body's fixed height. The
official strip aggregation is presentational only: `EnclosureProcessMap` still receives the full
`workspaceEngines` array, and the `engine-stack` / `engine-unit` testids live only on the fallback path and
must be kept for the legacy projection tests.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `buildEngineRoomModel` (pure model: joins, lifts workspace stack, sets `enclosureKey`/`usesFallback`). | `buildEngineRoomModel` | dashboard/src/panels/engine-room/buildEngineRoomModel.ts:33-66 |
| §4.2 3-zone room (`Panel fill` → `roomShell` → header + `roomGrid` [stack \| `roomStage` \| `roomZone`]). | `roomShell` | dashboard/src/panels/EngineRoom.tsx:252-279; dashboard/src/panels/EngineRoom.tsx:284-292 |
| `EngineRoomHeader` (health/phase/nextAction + master-caution from `selectQueue`). | `EngineRoomHeader` | dashboard/src/panels/EngineRoom.tsx:137-171 |
| `OfficialStrip` groups official workspace providers by label + runtime state, renders duplicate peers as counted chips, and exposes grouped repo labels via `title`/`aria-label`. | `OfficialStrip` | dashboard/src/panels/EngineRoom.tsx:109-132 |
| Official-strip regression tests pin seven same-state CGCs into one `7 CGC · nominal` chip, keep mixed CGC states separate, and assert hover-title repo lists. | "7 CGC · nominal" | dashboard/src/panels/EngineRoom.test.tsx:162-178; dashboard/src/panels/EngineRoom.test.tsx:180-204 |
| The bounded-height panel variant the room uses. | `fill` | dashboard/src/grammar/Panel.tsx:59-59 |
| `groupEngines` (fallback) + `engineState` + `selectQueue`. | `groupEngines` | dashboard/src/data/selectors.ts:37-46; dashboard/src/data/selectors.ts:123-127; dashboard/src/data/selectors.ts:147-165 |
| The per-worktree provider + enclosure-process read (surface 4 / `engineProcesses`). | "def read_engine_process_facts(" | mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:238-238 |
| The shared chat-routed gate responder rendered by diagnostics. | `GateResponder` | dashboard/src/panels/GateResponder.tsx:720-780 |

## Current L5I Maintenance

The keep-alive Engine Room now subscribes only to the `engineProcesses` and `ledgers` analytics
slices with `stableEquals`, memoizes its pure room model, and memoizes the component itself. An
unrelated analytics replacement or a cockpit tab switch therefore does not rebuild the large room.
The header pulse additionally stops while its observed element is hidden, so a mounted-but-hidden
room does not keep a Motion frame loop alive.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the engine-room styles barrel import change. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 9 citation rows with exact anchors and ranges: buildEngineRoomModel.ts L26-L66, the roomShell/header/OfficialStrip extents in EngineRoom.tsx, the official-strip test cases, grammar/Panel.tsx fill variant, data/selectors.ts selector triple, observer/snapshots.py `read_engine_process_facts` L639-L700, and GateResponder.tsx L217-L236. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-24T13:17:17Z — Curator: documented the narrowed analytics subscriptions, memoized room
  model/component, and visibility-gated header pulse. Verification fields remain pinned until the
  uncommitted code is committed at closeout.

- 2026-06-24T08:09+02:00 — Engine Room leaf identity: the selected-room header now titles the active leaf (`leafId || taskName`) and keeps the parent series task in the metadata line when a leaf is present. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:19+02:00 — Official-line strip aggregation: `OfficialStrip` now groups workspace providers
  by provider label + `engineState`, counts duplicate same-state CGCs (e.g. `7 CGC · nominal`), and exposes
  grouped mainline repos in the hover/title text. Regression coverage added in `EngineRoom.test.tsx`.
  Verification metadata pinned until closeout stamps the official-strip aggregation code commit.
- 2026-06-23T13:45+02:00 — Task 11: threaded `EngineProcessView.gate` into `EnclosureProcessMap` and
  `DiagnosticsPanel`; diagnostics now renders the compact shared responder for worktree-bound gates.
  Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-22T16:00 — slice 5o canvas remount on scenario switch: the panel reads the store generation counter (`state.gen`) and passes `key={gen}` to `EnclosureProcessMap`. The dev bench's `store.reset()` bumps `gen` on a scenario switch, forcing a clean remount of the centre canvas so a previous mode's exiting Motion failure-overlay (e.g. `FleetingEnclosure`) can't orphan mid-`AnimatePresence` and bleed through the scenario dropdown; `gen` is constant (0) in production, so the canvas is never remounted by it there. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: resolves the official `LedgerNode` from `analytics.ledgers` by the selected enclosure's `repoName` and passes it down as `officialLedger` for the official coupler popover. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-17T22:45 — engine-room visual-parity + fill-height layout: the room's `<Panel>` is rendered with
  `fill` (the bounded-height variant) so the centre canvas + right panel stop resizing per selection and the
  side columns scroll; `EnclosureProcessMap` now receives `model.workspaceEngines` so the bird's-eye renders
  the left official-line engines from the same real stack the `OfficialStrip` summarises. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-16T03:50 — slice 5f S5 (lifecycle T12–T18): the header `phaseChip` became a `motion.span` that pulses while the selected enclosure is in a human-gated lifecycle phase (`LIFECYCLE_PHASES`: sync / closeout / commit-approval / integration / cleanup); the header carries `data-phase-active` (new `EngineRoom.test.tsx` pins it). Gated, instant under `data-effects=off`. Verification metadata pinned until closeout stamps the S5 code commit.
- 2026-06-16T02:30 — slice 5f S1: replaced the 2-col `roomLayout`/`detailColumn` with the §4.2
  full-width 3-zone room — an `EngineRoomHeader` (selected enclosure · health · phase · next action +
  master-caution mirror from `selectQueue`) over `roomGrid` [stack list \| pod stage \| boot+diagnostics
  on the right]. Verification metadata pinned until closeout stamps the S1 code commit.
- 2026-06-16T01:55 — slice 5f S0: enclosure selection keyed by `worktreeGroup` (`selectedGroup` +
  `selected.enclosureKey`) instead of `node.id`, matching `EnclosureStackList`'s new `selectedKey` prop.
- 2026-06-15T19:35 — slice 5e: rewritten for slice 5e: builds buildEngineRoomModel and renders the enclosure stack list + process map + boot timeline + diagnostics (official-line strip on top); keeps groupEngines fallback + engine-stack/engine-unit testids.
- 2026-06-15T17:00 — Created for slice 5d: migrated onto `Panel` + state-keyed Panda cvas (no
  descendant selectors). Verification metadata pinned until closeout stamps the 5d code commit.
