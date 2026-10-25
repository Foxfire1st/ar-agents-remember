# dashboard/src/topology/constel.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Current renderer boundary

The imperative canvas renderer consumes the pure constellation model and draws the workspace, repository and active worktree enclosure nodes. Provider satellites, provider orbits/edges and provider engine-state colours are removed. The model's node kinds are `ws|repo|wt` and its statuses are `core|ok|warn|idle`. `constelColors` remains a total `Record<ConstelStatus,string>` with literal CSS-token fallbacks, and `statusColor` indexes that map without a healthy-default branch. The former five-status/sixth-status explanation is historical; the source comment still says “sixth” but the present tuple has four entries. [1] [2] [3]

Every node is positioned from `ang` and `rf`; the renderer has no `PROV_R` parent-orbit branch. The rings are CHECKOUTS and ENCLOSURES. It draws stars, rings, ordinary parent edges, unfrozen comets, core, nodes and labels. A non-ok worktree edge uses its supplied status colour. `buildTopology` supplies workspace/repository/worktree nodes only and derives worktree status from the bound TaskEntry's shared status/tone; it supplies no provider status. [3] [4]

Resize and data updates still paint synchronously, so an occluded tab does not depend on rAF for its first/current frame. `destroy` cancels rAF, disconnects the observer and removes listeners. React owns mount/sizing and supplies model updates. The renderer truncates supplied labels and copies model-provided detail/sub-lines into the tooltip; the L184 limited-word, clockless form and detail ownership remains in `model.ts::worktreeFields` and shared status helpers. Source inspection renews no browser, test or execution acceptance. [2] [6]

| Current claim | Source witness | Existing reference |
| --- | --- | --- |
| Four-colour total palette and direct lookup. | `dashboard/src/topology/constel.ts:31-37,73` | [1] [2] |
| Only workspace/repository/worktree nodes and four statuses; worktree label, word and limit detail stay model-owned. | `dashboard/src/topology/model.ts:23-28,82-109,111-188` | [3]  |
| Uniform layout, two rings and ordinary edges, with no provider draw stage. | `dashboard/src/topology/constel.ts:90-98,189-225,291-305` | [2] |
| Synchronous resize/update paint, teardown and model-owned tooltip data. | `dashboard/src/topology/constel.ts:321-349,381-449` | [2] [6] |

## Historical source account

The original card below preserves its source epoch, references and dated history. Its superseded provider display, start, status and consumer claims are not the current operative account. Retained internal mechanisms grant no removed public operation.

<details>
<summary>Original card and source-epoch evidence</summary>

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
someone picks its hue), and the current `statusColor(scene, status: ConstelStatus)` indexes `scene.colors[status]` with **no `??`**. The missing fallback is deliberate: the renderer consumes the package’s own `ConstelStatus` model, so the palette lookup is total and a default would re-introduce the guess. The earlier contrast with a wire-state lookup in `model.ts` is historical; the current model uses bound TaskEntry status/tone for worktrees and provider engine state for satellites.

`mountConstel({canvas, wrap, tip}, initial, {onSelect})` grabs the 2D context, builds its `CssVarReader`
over `getComputedStyle(document.documentElement)`, calls `constelColors(v)` once, and returns a handle
with `update()` + `destroy()`. `layout()` positions nodes: providers orbit their **parent** node at
`PROV_R` (`par.px + cos(poff+provSpin)*PROV_R`); every other node sits at `cx + cos(ang)*rf*R`. `render()`
clears, then draws stars → ring guides (CHECKOUTS/ENCLOSURES — two rings, `RF.repo`/`RF.wt`; the TASKS
ring is gone) → edges → comets (non-frozen) → provider nodes → central glow → other nodes → labels →
"WORKSPACE". Edge colour: provider edges are faint; the `wt` (enclosure) edge is status-coloured when its
model status is not `ok` (for a bound worktree this comes from the entry’s shared task-status tone, not a lifecycle fold); all other edges
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
- The status palette is TOTAL and carries no fallback. `statusColor` must keep indexing `Record<ConstelStatus,
  string>` directly; adding a `?? COLORS.ok` back is the original defect, because a status the palette
  cannot answer would then paint as healthy work.
- Every status must own a distinct hue and its own `--token`, and every token must carry a real
  literal fallback — an empty fallback renders a node with no fill, which reads as "nothing here" as
  wrongly as the cyan did. `constel.test.ts` pins all three.
- `constelColors` must stay outside `mountConstel` and take its reader as a parameter, so the totality
  it claims is executable in jsdom.

### Todos

No open file-local todos.


**L184 — INV-XZYGEB, ownership corrected.** This renderer paints the labels it is given, truncates them to the space available and copies the supplied detail and sub-line into the tooltip: it presents and propagates what the model hands it. The limited word, its clockless form and the choice of detail are decided in `model.ts::worktreeFields` with the shared status helpers, not here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source and tests.

No relevant external documentation found.

### Repo-Internal References

The renderer consumes the `ConstelStatus` produced by `model.ts`: the workspace is `core`, repositories are `ok`, a worktree uses its bound TaskEntry’s shared `taskStatusKey`/`statusTone` (`wait` → `warn`, `gone` → `idle`, otherwise `ok`) and an unbound worktree is `idle`. Provider satellites use engine state (`down` → `crit`, `indexing` → `idle`, otherwise `ok`). `constelColors` maps these statuses to token-backed hex colours; it does not interpret lifecycle states. Both model and palette are cited so the seam remains traceable.

- `CssVarReader` and the total `constelColors(cssVar): Record<ConstelStatus, string>`, extracted from `mountConstel` so the palette is reachable without a canvas. [1]
- `mountConstel` builds its token reader and stores `constelColors(v)` in the scene once; `statusColor` indexes the resulting total map without a fallback. [2]

- `CONSTEL_STATUSES` and the derived `ConstelStatus` this palette is keyed by — the single vocabulary shared with the model. [3]


> Retained earlier citation wording: - `worktreeStatus` maps a worktree row through the shared status and tone and returns `idle` when the row is unbound; `worktreeFields` supplies the node's label, word and limit detail, and `buildTopology` separately supplies workspace/repository and provider statuses. [4]

- `constel.test.ts` executes the palette's totality, hue-uniqueness, and token/fallback shape without a canvas. [5]

- The React wrapper that mounts this renderer once and pushes new models through `update()`. [6]


### Cross-Repo References

No meaningful cross-repo references found. The behavior is within the `agents-remember` dashboard
projection/model/render boundary.

No meaningful cross-repo references found.

</details>

- `worktreeStatus` maps a worktree row through shared `taskStatusKey`/`statusTone`, returns `idle` when unbound, and maps `wait` to `warn`, `gone` to `idle`, otherwise `ok`. `worktreeFields` supplies the label, status word and full limit detail using shared status/limit helpers; a limited node's detail contains the word plus every `limitLines` row, with no canvas clock. `buildTopology` creates only workspace, repository and worktree nodes: workspace is `core`, `addRepositories` supplies repository `ok`, and worktrees use that shared derived status and those fields. Search-provider satellites and their status mapping are absent. [4]
