# dashboard/src/panels/Topology.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Topology.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The imperative renderer (refs + `.style`, no className dep). | `mountConstel` | dashboard/src/topology/constel.ts:59-372 |
| The pure model adapter. | `buildTopology` | dashboard/src/topology/model.ts:117-221 |

## Update History

- 2026-08-03T02:32:28+02:00 — W3-B05 curator: anchored 2 Tier-2 table citations with exact source paths; fixer generated all ranges.

- 2026-06-28T07:30+02:00 — Task 33: the panel now reads `activeWorktreeGroups` from the store and runs
  `activeTopologyInputs(...)` before `buildTopology`, bounding the constellation to active enclosures
  (the rim/all-time enclosures no longer render). Verification metadata pinned until closeout stamps the
  code commit.
- 2026-06-23T13:35 — Slice 12 (render-robustness): the canvas is now absolutely positioned filling the
  relative wrap (was in-flow `width/height:100%`, which let an indefinite-height ancestor drive a
  ResizeObserver × DPR growth loop), and the `Panel` is rendered with `fill` so the constellation fills
  its slot (the section is `display:block` by default, leaving the wrap's `flex:1` inert → half-height).
  Verification metadata stamped at the slice-12 closeout.
- 2026-06-15T17:00 — Created for slice 5d: container/tip/legend migrated to Panda; the imperative
  canvas renderer unchanged. Verification metadata pinned until closeout stamps the 5d code commit.
