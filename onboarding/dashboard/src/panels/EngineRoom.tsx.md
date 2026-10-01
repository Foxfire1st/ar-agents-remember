# dashboard/src/panels/EngineRoom.tsx

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

## Evidence

### Repo-Internal References

- `buildEngineRoomModel` (pure model: joins, lifts workspace stack, sets `enclosureKey`/`usesFallback`). [1]
- §4.2 3-zone room (`Panel fill` → `roomShell` → header + `roomGrid` [stack \| `roomStage` \| `roomZone`]). [2]
- `EngineRoomHeader` (health/phase/nextAction + master-caution from `selectQueue`). [3]
- `OfficialStrip` groups official workspace providers by label + runtime state, renders duplicate peers as counted chips, and exposes grouped repo labels via `title`/`aria-label`. [4]
- Official-strip regression tests pin seven same-state CGCs into one `7 CGC · nominal` chip, keep mixed CGC states separate, and assert hover-title repo lists. [5]
- The bounded-height panel variant the room uses. [6]
- `groupEngines` (fallback) + `engineState` + `selectQueue`. [7]
- The per-worktree provider + enclosure-process read (surface 4 / `engineProcesses`). [8]
- The shared chat-routed gate responder rendered by diagnostics. [9]

## Current L5I Maintenance

The keep-alive Engine Room now subscribes only to the `engineProcesses` and `ledgers` analytics
slices with `stableEquals`, memoizes its pure room model, and memoizes the component itself. An
unrelated analytics replacement or a cockpit tab switch therefore does not rebuild the large room.
The header pulse additionally stops while its observed element is hidden, so a mounted-but-hidden
room does not keep a Motion frame loop alive.
