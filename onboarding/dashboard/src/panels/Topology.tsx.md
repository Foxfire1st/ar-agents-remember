# dashboard/src/panels/Topology.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The radial constellation hero (mc2 harvest #4): a React-wrapped imperative `<canvas>`. React owns the
projection→model adapter (a pure, memoised `buildTopology`) + mount; the renderer (`topology/
constel.ts`) stays imperative.

## Code Commentary

### Logic

Reads `lifecycles`, `enclosures`, `providers`, and `activeWorktreeGroups` from the store. Builds the
model with `useMemo`: it first calls `activeTopologyInputs(lifecycles, enclosures, activeWorktreeGroups)`
to bound the inputs to live worktree groups, then `buildTopology(active.lifecycles, active.enclosures,
providers)` — so the constellation shows active work only while the shared store maps keep all-time
history for other views. `mountConstel` runs ONCE (refs to canvas/wrap/tip), and new models
are pushed via `handle.update(model)` so the rAF loop keeps running (no remount-on-tick reset). The
container/tip/legend are Panda `css()`; the legend dots a `legdot` `cva`. The renderer styles the tip
via `.style` (refs), so migrating the classNames is safe. The canvas is **absolutely positioned**
(`position:absolute; top:0; left:0; width/height:100%`) filling the `position:relative` wrap — out of
flow so its DPR-scaled buffer can't feed back into layout (an in-flow `height:100%` had let an
indefinite-height ancestor drive a ResizeObserver × DPR growth loop). The `Panel` is rendered with
**`fill`** (its flex-column variant) so the wrap fills the slot below the header instead of collapsing
to its `min-height` (the shell is `display:block` by default, which left the wrap's `flex:1` inert).

### Invariants And Boundaries

Mount-once + `update()` (never remount on data tick). Clicking a node couples back into Operations.
Halts to a static frame under `?effects=off`. The renderer depends on the refs, not classNames. The
canvas fills the wrap **out of flow** (no layout-feedback loop), and the `Panel` must stay **`fill`**
for the wrap to fill its slot.

## Evidence

### Repo-Internal References

- The imperative renderer (refs + `.style`, no className dep). [1]
- The pure model adapter. [2]
