# dashboard/src/topology/constel.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The imperative constellation renderer (ported from mc2's `buildConstel`/`layout`/`frame`): it draws the
pure `ConstelNode[]` model (`model.ts`) onto a `<canvas>` — starfield, ring guides, parent→child edges,
comets on live edges, provider satellites, pulsing nodes — and owns hover hit-testing + click-through.
React (`panels/Topology.tsx`) owns mount, sizing, and the projection→model adapter; this stays imperative.

## Code Commentary

### Logic

**The status → colour palette (260731-EFA-L4).** `constelColors(cssVar: CssVarReader):
Record<ConstelStatus, string>` is the exported, total map from a constellation status to the token it
paints with: `core → --ink`, `ok → --cyan`, `warn → --amber`, `crit → --alarm`, `idle → --dormant`,
each with a concrete `#rrggbb` literal to fall back to. `CssVarReader` (`(name, fallback) => string`)
is the injected reader, so the palette is reachable **without a canvas** — the previous totality claim
lived inside `mountConstel`, which jsdom cannot run, and a totality claim nothing can execute is one
nothing can check.

This replaced the un-migrated twin of `model.ts`'s defect. The palette was
`const COLORS: Record<string, string>` read through `const col = (status: string) => COLORS[status] ??
COLORS.ok` — the same "unknown reads healthy" shape, one map further down the pipeline, and the place
the `undefined` from an unclassified state landed and came out cyan. Two things changed: the map is
keyed by `ConstelStatus` (a sixth entry in `CONSTEL_STATUSES` stops the object literal compiling until
someone picks its hue), and `col` is now `(status: ConstelStatus): string => COLORS[status]` with **no
`??`**. The missing fallback is deliberate and is the opposite ruling from `model.ts`: there the index
key is wire data, here it is a `ConstelStatus` this package's own `buildTopology` produced, so the
lookup really is total and a default would be re-introducing the guess.

`mountConstel({canvas, wrap, tip}, initial, {onSelect})` grabs the 2D context, builds its `CssVarReader`
over `getComputedStyle(document.documentElement)`, calls `constelColors(v)` once, and returns a handle
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

Canvas colours come from the design tokens via `getComputedStyle(documentElement)` (read once at mount)
and are funnelled through `constelColors`, never read ad hoc per draw call; the buffer is DPR-scaled
with a `setTransform(dpr…)` so draw coords stay in CSS pixels. `frozen`
(`documentElement.dataset.effects === "off"`, the Calm toggle) renders a single static frame and starts
no rAF loop. `EDGE` and `MUTED` are chrome, not status, so they stay outside the status palette.

### Invariants And Boundaries

- React mounts the renderer **once**; new models arrive via `update(next)` (swap `nodes`, drop in-flight
  comets, re-layout/render) so the rAF loop never resets between projection ticks.
- A paint happens on resize and on every data update regardless of rAF — a backgrounded tab (rAF
  throttled) must not be blank.
- `destroy()` cancels the rAF, disconnects the ResizeObserver, and removes the wrap listeners.
- Pure model in/imperative draw out: this file never builds the model (that is `model.ts`).
- The status palette is TOTAL and carries no fallback. `col` must keep indexing `Record<ConstelStatus,
  string>` directly; adding a `?? COLORS.ok` back is the original defect, because a status the palette
  cannot answer would then paint as healthy work.
- Every status must own a distinct hue and its own `--token`, and every token must carry a real
  literal fallback — an empty fallback renders a node with no fill, which reads as "nothing here" as
  wrongly as the cyan did. `constel.test.ts` pins all three.
- `constelColors` must stay outside `mountConstel` and take its reader as a parameter, so the totality
  it claims is executable in jsdom.

### Todos

No open file-local todos.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source and tests.

No relevant external documentation found.

### Repo-Internal References

The renderer sits at the end of one grammar that starts in `model.ts`: a lifecycle state becomes a
`ConstelStatus` there and a hex string here. Both halves are cited so the seam is traceable in either
direction.

- `CssVarReader` and the total `constelColors(cssVar): Record<ConstelStatus, string>`, extracted from `mountConstel` so the palette is reachable without a canvas. [1]
- `mountConstel` builds its reader over `getComputedStyle`, calls `constelColors(v)` once, and `col` indexes the result with no `??` fallback. [2]
- `CONSTEL_STATUSES` and the derived `ConstelStatus` this palette is keyed by — the single vocabulary shared with the model. [3]
- `lifecycleStatus` is the only producer of the statuses this file paints; its `UNCLASSIFIED_STATUS` is why an unrecognised state no longer arrives here as `undefined`. [4]
- `constel.test.ts` executes the palette's totality, hue-uniqueness, and token/fallback shape without a canvas. [5]
- The React wrapper that mounts this renderer once and pushes new models through `update()`. [6]

### Cross-Repo References

No meaningful cross-repo references found. The behavior is within the `agents-remember` dashboard
projection/model/render boundary.

No meaningful cross-repo references found.
