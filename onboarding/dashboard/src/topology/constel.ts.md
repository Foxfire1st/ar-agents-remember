# dashboard/src/topology/constel.ts

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `dashboard/src/topology/constel.ts`         |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-06-23T13:35                            |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                            |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The imperative constellation renderer (ported from mc2's `buildConstel`/`layout`/`frame`): it draws the
pure `ConstelNode[]` model (`model.ts`) onto a `<canvas>` — starfield, ring guides, parent→child edges,
comets on live edges, provider satellites, pulsing nodes — and owns hover hit-testing + click-through.
React (`panels/Topology.tsx`) owns mount, sizing, and the projection→model adapter; this stays imperative.

## Code Commentary

### Logic

`mountConstel({canvas, wrap, tip}, initial, {onSelect})` grabs the 2D context, reads the state colours
from CSS custom properties (`--cyan`/`--amber`/`--alarm`/`--dormant`/`--ink`) once, and returns a handle
with `update()` + `destroy()`. `layout()` positions nodes: providers orbit their **parent** node at
`PROV_R` (`par.px + cos(poff+provSpin)*PROV_R`); every other node sits at `cx + cos(ang)*rf*R`. `render()`
clears, then draws stars → ring guides (CHECKOUTS/ENCLOSURES — two rings, `RF.repo`/`RF.wt`; the TASKS
ring is gone) → edges → comets (non-frozen) → provider nodes → central glow → other nodes → labels →
"WORKSPACE". Edge colour: provider edges are faint; the `wt` (enclosure) edge is status-coloured when its
folded lifecycle status is not `ok` (the signal the removed task-rim edge used to carry); all other edges
are the neutral `EDGE` colour. `frame()` is the rAF loop (`T += 16`,
`provSpin`, then `layout()+render()` when `cw && nodes.length`). `resize()` measures the **wrap** rect,
sets `canvas.{width,height} = wrapSize × min(dpr,2)` and `ctx.setTransform(dpr…)`, then rebuilds stars,
lays out, and renders. A `ResizeObserver` on the wrap re-runs `resize()`. `hit()`/`onMove()`/`onClick()`
do nearest-node hover (tip) + click-through (`onSelect` for nodes carrying an `id`).

`render()` is called from **`resize()` and `update()` unconditionally** (not only in `frozen` mode), so a
frame is always painted on mount / resize / data update — independent of the rAF loop. This matters
because Chrome throttles `requestAnimationFrame` to ~0 in a hidden/occluded tab, and a monitoring
dashboard is often backgrounded; without the synchronous paint the canvas stayed blank there.

### Conventions

Canvas colours come from the design tokens via `getComputedStyle(documentElement)` (read once at mount);
the buffer is DPR-scaled with a `setTransform(dpr…)` so draw coords stay in CSS pixels. `frozen`
(`documentElement.dataset.effects === "off"`, the Calm toggle) renders a single static frame and starts
no rAF loop.

### Invariants And Boundaries

- React mounts the renderer **once**; new models arrive via `update(next)` (swap `nodes`, drop in-flight
  comets, re-layout/render) so the rAF loop never resets between projection ticks.
- A paint happens on resize and on every data update regardless of rAF — a backgrounded tab (rAF
  throttled) must not be blank.
- `destroy()` cancels the rAF, disconnects the ResizeObserver, and removes the wrap listeners.
- Pure model in/imperative draw out: this file never builds the model (that is `model.ts`).

### Todos

No open file-local todos.

## Docs References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The React wrapper that mounts this renderer, sizes the canvas, and pushes models. | L77-L147 | [panels/Topology.tsx](agents-remember/dashboard/src/panels/Topology.tsx) |
| The pure model this renderer draws. | — | [topology/model.ts](agents-remember/dashboard/src/topology/model.ts) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-28T07:30+02:00 — Task 33: the renderer no longer draws a TASKS ring; ring guides are now
  CHECKOUTS + ENCLOSURES (`RF.repo`/`RF.wt`). The `task`-kind edge branch was removed; the `wt`
  (enclosure) edge is now status-coloured when its folded lifecycle status is not `ok`, preserving the
  signal the old task-rim edge gave. No `task` nodes exist in the model anymore. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-23T13:35 — Created (slice 12, render-robustness): documents the imperative renderer and that
  `render()` now runs synchronously from `resize()`/`update()` (not only under rAF), so the canvas paints
  in a backgrounded tab where `requestAnimationFrame` is throttled. Verification metadata pinned until
  closeout stamps the slice-12 code commit.
