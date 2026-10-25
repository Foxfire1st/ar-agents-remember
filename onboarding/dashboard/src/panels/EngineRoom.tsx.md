# dashboard/src/panels/EngineRoom.tsx

## Governing Overview

[panels/ overview](overview.md)

## 260731-EFA-L8 Change

The engine-room style module split moved `engineRoomStyles` imports to the new
`engine-room/styles` barrel (which re-exports the six style domains); rendering and
data flow are unchanged.


## Current enclosure-only composition

EngineRoom reads process/ledger slices only; buildEngineRoomModel takes processes alone. `BoundTaskStatus` finds the first entry in the shared tasks map whose `worktrees` contain the node’s enclosure, then renders its shared `TaskStatusWord`; no match renders nothing. Ledger coupling and gen-keyed canvas remount remain; no lifecycle subscription or provider fallback.

### Maintenance boundaries

Preserve enclosure-only composition and ledger couplers. Native task status is separate from projected landing-operation phases/gates; source inspection is not fresh visual or execution proof.

Source/test/fixture inspection is not a fresh mounted capture or a passing test run.
Historical provider-shaped input data and retained compatibility definitions do not
restore removed provider visuals or tool exposure.


## Historical superseded account (non-operative)

The prior onboarding below is retained for provenance and unrelated design history.
It is not current provider-render, fallback, prototype-parity or execution guidance.
Current behavior and its limits are the operative contract above.



The engine room (note 08 twin-engine pod): each worktree's provider stack = CGC (its code repo) +
GrepAI (its memory repo). It builds a render model with `buildEngineRoomModel` and surfaces the
shared workspace (official/main) stack as an official-line strip on top, plus every worktree's own
enclosure process. As of slice 5f S1 the room owns a **full-width 3-zone layout** (§4.2): a header
strip over [enclosure stack list | pod stage (process map) | boot timeline + diagnostics on the
RIGHT]. A legacy `groupEngines` fallback still renders flat provider stacks for older projections.

## Code Commentary

### Logic

The panel builds a pure process model from engineProcesses alone. A missing selectedGroup falls back to the first process, not a legacy provider stack. `BoundTaskStatus` finds the first entry in the shared tasks map whose `worktrees` contain the node’s enclosure, then renders its shared `TaskStatusWord`; no match renders nothing.

The process branch renders stack selection, process canvas and boot progress; no selected process renders the honest no-active-enclosures message.

Panel fill bounds the room so its side columns scroll independently. officialLedger matches the selected repo; the worktree coupler reads node.ledgerRows. The process canvas retains operation evidence and does not become a gate responder.

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
test.

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


- §4.2 3-zone room (`Panel fill` → `roomShell` → header + `roomGrid` [stack \| `roomStage` \| `roomZone`]). [2]


- `EngineRoomHeader` (health/phase/nextAction + master-caution from `selectQueue`). [3]

- The bounded-height panel variant the room uses. [6]
- The per-worktree provider + enclosure-process read (surface 4 / `engineProcesses`). [8]

## Current L5I Maintenance

The keep-alive Engine Room now subscribes only to the `engineProcesses` and `ledgers` analytics
slices with `stableEquals`, memoizes its pure room model, and memoizes the component itself. An
unrelated analytics replacement or a cockpit tab switch therefore does not rebuild the large room.
The header pulse additionally stops while its observed element is hidden, so a mounted-but-hidden
room does not keep a Motion frame loop alive.
