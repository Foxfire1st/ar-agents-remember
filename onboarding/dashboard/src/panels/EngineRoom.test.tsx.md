# dashboard/src/panels/EngineRoom.test.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Vitest + `@testing-library/react` render test for slice 5f S5's lifecycle-phase motion: the Engine Room
header flags `data-phase-active` when the selected enclosure is in a human-gated lifecycle phase (sync /
closeout / integration / cleanup, T12–T18), so the room reads as a machine being synced / landed / retired.
Task 11 adds a render assertion that a projected worktree gate surfaces the compact responder in
diagnostics and threads `data-gate-kind` into the canvas. The official-strip coverage now also pins
workspace provider aggregation: same-state CGC providers collapse into one counted chip, mixed CGC states
stay separate, grouped hover titles expose mainline repo labels, and GrepAI remains separately visible. The
leaf-identity regression seeds two browser-dashboard leaves under one parent series so the rail/header must
show the active leaf name first and keep the parent task as context.

## Code Commentary

### Logic

Seeds the real store from a `GALLERY` projection (`applySnapshot`) and renders `<EngineRoom />` with motion
frozen (`data-effects=off`), so the assertion is the structural flag, not the pulse.

- "marks the header phase-active for a human-gated lifecycle phase" — `engine-cleanup-pending` (the
  selected node is `cleanup-pending`) → `engine-room-header[data-phase-active="true"]`.
- "does not mark phase-active for a freshly started worktree" — `engine-bootstrap` (`worktree-started`) →
  `data-phase-active="false"`.
- "renders the projected gate responder..." builds a local cleanup-gate projection, then asserts
  `engine-gate-responder` renders and `enclosure-canvas[data-gate-kind] === "cleanup-approval"`.
- "aggregates same-state official CGC engines..." seeds seven nominal workspace CGCs plus one GrepAI and
  asserts the strip shows one `7 CGC · nominal` aggregate whose title includes the repo labels.
- "keeps official CGC aggregate chips separated by runtime state" seeds nominal, indexing, and down CGCs
  and asserts the strip keeps one chip per state/color while preserving GrepAI as its own chip.
- "renders leaf enclosure identity ahead of the parent series task name" seeds cleanup-pending leaf 15 and
  active leaf 16 under `260610_browser-dashboard`, then asserts the active leaf row/header render before the
  cleanup sibling and the parent task remains secondary context.

### Invariants And Boundaries

Pure render assertion — relies on the shared `test/setup.ts` jsdom stubs. It pins the *which-phases-pulse*
contract (`LIFECYCLE_PHASES`), not the animation; the pulse itself is gated and visual. The official-strip
tests stay inside the top `EngineRoom` strip by seeding `providers` directly on the gallery projection; they
do not assert or reshape the enclosure canvas' workspace-engine rendering.

## Evidence

### Repo-Internal References

- The `EngineRoomHeader` + `LIFECYCLE_PHASES` under test. [1]
- `OfficialStrip` groups official workspace providers by label + runtime state and exposes grouped repo labels via hover/title. [2]
- The local provider fixture helpers and official-strip assertions pin counted same-state CGCs, mixed-state separation, and GrepAI visibility. [3]
- The `GALLERY` projection seed + the store `applySnapshot`. [4]
- The honest-motion gate the pulse reads. [5]

## Current L5I Maintenance

The focused suite now delegates to the real model builder through a spy and proves the performance
boundary: unchanged render inputs and unrelated analytics deltas do not rebuild the room, while a
real `engineProcesses` change does.

## L23 Lineage Rendering Regression

The suite seeds a blocked Engine Process projection and proves Diagnostics
renders both the compact state and the full server summary. This is the
operator-visible acceptance edge for refusing structural work before enclosure
context is consumed.
