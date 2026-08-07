# dashboard/src/topology/constel.ts

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `dashboard/src/topology/constel.ts`         |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-08-01T09:24+02:00                      |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`|
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The renderer sits at the end of one grammar that starts in `model.ts`: a lifecycle state becomes a
`ConstelStatus` there and a hex string here. Both halves are cited so the seam is traceable in either
direction.

| Finding | Anchor | Source |
| --- | --- | --- |
| `CssVarReader` and the total `constelColors(cssVar): Record<ConstelStatus, string>`, extracted from `mountConstel` so the palette is reachable without a canvas. | `CssVarReader`; `constelColors`; `mountConstel` | dashboard/src/topology/constel.ts:16-16; dashboard/src/topology/constel.ts:31-39; dashboard/src/topology/constel.ts:408-468 |
| `mountConstel` builds its reader over `getComputedStyle`, calls `constelColors(v)` once, and `col` indexes the result with no `??` fallback. | `mountConstel` | dashboard/src/topology/constel.ts:408-468 |
| `CONSTEL_STATUSES` and the derived `ConstelStatus` this palette is keyed by — the single vocabulary shared with the model. | `CONSTEL_STATUSES`; `ConstelStatus` | dashboard/src/topology/model.ts:16-16; dashboard/src/topology/model.ts:18-18 |
| `lifecycleStatus` is the only producer of the statuses this file paints; its `UNCLASSIFIED_STATUS` is why an unrecognised state no longer arrives here as `undefined`. | `lifecycleStatus`; `UNCLASSIFIED_STATUS` | dashboard/src/topology/model.ts:68-68; dashboard/src/topology/model.ts:85-93 |
| `constel.test.ts` executes the palette's totality, hue-uniqueness, and token/fallback shape without a canvas. | "gives every status in the vocabulary a colour of its own"; "declares no colour for a status the vocabulary does not contain"; "asks for a themed token per status and offers a concrete fallback for each" | dashboard/src/topology/constel.test.ts:21-30; dashboard/src/topology/constel.test.ts:32-39; dashboard/src/topology/constel.test.ts:41-57 |
| The React wrapper that mounts this renderer once and pushes new models through `update()`. | `Topology` | dashboard/src/panels/Topology.tsx:82-155 |

## Cross-Repo References

No meaningful cross-repo references found. The behavior is within the `agents-remember` dashboard
projection/model/render boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: removed duplicated Source ranges
  from the constel/model rows; exact non-fixing check returns zero findings.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 12 citation finding(s); scoped recheck clean.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-01T09:24+02:00 — 260731-EFA-L4 curator: documented the palette migration. This file was the
  un-migrated twin of `model.ts`'s headline defect — `COLORS: Record<string, string>` read through
  `col = (status) => COLORS[status] ?? COLORS.ok`, the same "unknown reads healthy" shape one surface
  further down, and the place an unclassified state's `undefined` became a cyan healthy fill. It is
  now the exported `constelColors(cssVar: CssVarReader): Record<ConstelStatus, string>`, total by
  type and lifted out of `mountConstel` so jsdom can execute the totality it claims; `col` indexes it
  with no `??` (deliberate — the key here is a `ConstelStatus` `buildTopology` produced, not wire
  data). Added the matching invariants and the missing `Docs References`/`Cross-Repo References`
  prose. Repaired the Repo-Internal citations:
  both rows linked `agents-remember/dashboard/src/...`, which resolves under the sidecar's own folder
  and pointed at nothing — now `../panels/Topology.tsx` and `model.ts`, with ranges containing
  `constelColors`, `mountConstel`/`col`, `CONSTEL_STATUSES` and `lifecycleStatus`. Verification
  metadata left pinned; closeout stamps the code commit.
- 2026-06-28T07:30+02:00 — Task 33: the renderer no longer draws a TASKS ring; ring guides are now
  CHECKOUTS + ENCLOSURES (`RF.repo`/`RF.wt`). The `task`-kind edge branch was removed; the `wt`
  (enclosure) edge is now status-coloured when its folded lifecycle status is not `ok`, preserving the
  signal the old task-rim edge gave. No `task` nodes exist in the model anymore. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-23T13:35 — Created (slice 12, render-robustness): documents the imperative renderer and that
  `render()` now runs synchronously from `resize()`/`update()` (not only under rAF), so the canvas paints
  in a backgrounded tab where `requestAnimationFrame` is throttled. Verification metadata pinned until
  closeout stamps the slice-12 code commit.
