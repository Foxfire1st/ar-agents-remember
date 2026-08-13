# dashboard/src/panels/engine-room/useEngineTimeline.ts

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `dashboard/src/panels/engine-room/useEngineTimeline.ts`   |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated | 2026-08-01T15:10+02:00 |
| lastVerifiedCommitHash |                                                           `1580f92715ff93c988f9a15439ad9bec60ef4c5d`|
| lastVerifiedCommitDate |                                                           2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[engine-room overview](overview.md)

## Purpose

The Engine Room canvas **GSAP motion substrate** (slice 05k, the `05f` §8 correction target). One
`gsap.context` per enclosure, scoped to the `EnclosureCanvas` `<svg>` root, owns ONLY the GSAP-native parts:
the DrawSVG draw-ons (drawn once per lane — 05n), the MotionPath travelling packet, and the repeating fx that used to be CSS `@keyframes`. Motion
(inside `EnclosureCanvas`) owns opacity/transform/scaleY/fill + enter/exit; CSS is static. This split is the
end-state 05k reaches by removing the interim `sceneSvg` CSS transition + the 9 canvas keyframes — the
hook now drives every canvas motion that GSAP should own, so the component renders the structure and this
hook animates it.

## Code Commentary

### Logic

Three exports/helpers. `phaseStage(phase)` maps the projection `phase` string to the choreography stage:
`worktree-started`/`code-worktree`/`contract-written`/`provider-setup` → `power-up`, `closeout-pending` →
`closeout`, `integration-pending` → `integrate`, `cleanup-pending`/`abandoned` → `teardown`, everything else
→ `idle` (the constellation at rest, no timeline). `fxSignature(node)` builds a stable string of everything
the GSAP layer keys on — `node.phase`, the running draw lanes (`edges` filtered to `state === "running"`,
kinds sorted), the resolved landing flows (`landing[]` `kind:state:factState`, sorted), the engine fx states
(`providers` `role:runtimeState`, sorted), the **refused edges** — the local is still called `refused`, but
the filter is now `edges` with `state` ∈ `failed`/`stale` only (`kind:state`, sorted — 05o) —
`seedFallback ? "reindex" : ""`, and `memoryMode` — so
the effect re-runs (revert → rebuild) exactly when a choreography input changes (a `planned → running` lane
re-draws, a cleared fault stops flickering). The fold-in matters because a failed or stale lane is **not** a
`running` lane, so the `draws` segment alone misses it — without it the one-shot `refuse` flash would not re-arm
when the beat lands. A `state === "refused"` arm was removed here: the reducer has no such state (`_seed_edge_state`
returns `failed`/`running`/`stale`/`complete`/`skipped`/`planned`, and `EngineProcessEdge`'s own state comment
never listed `refused`), so the arm could never match a served payload. "Refused" survives as the NAME of the
visual beat — `data-fx='refuse'`, the `refuse` tween, `refusedConduit` — not as an edge state.
`buildFx(q)` builds the repeating loops on whatever `data-fx` elements the
render produced: `fault` (engine down → the red frame **breathes GENTLY** — `opacity 0.5 → 0.95`, `1.7s`
`sine.inOut` yoyo, 5o; never a strobe, so the WCAG 2.3.1 ≤3-flashes/s cap is satisfied with room to spare —
this replaced the old 0.34s `steps(1)` flicker), `reindex` (amber center-out `scaleY` 0.25→1 + opacity pulse — a fallback, not
a fault), `scan` (05o — the pre-block verify sweep: a cyan ring expands + fades, `attr {r}` 6→52 + `opacity` 0.9→0, `1.2s` `power1.out`, `repeat:-1`; transient, gone once the check resolves), `surge` (the two warp-core bands animate their `y1`/`y2` outward + fade, split up/down by
`data-dir`, staggered), `breath` (the attention badge's gentle `sine.inOut` opacity breathing), `stop` (the
terminal-STOP flash, `repeat: 5` = 3 on-beats then steady), `refuse` (05o — the refused-conduit flash on a
seed/integration lane that did not take, i.e. `failed` or `stale`: a **ONE-SHOT** `gsap.timeline` with `repeat: 0`, NOT a loop — cyan
(`oklch(0.85 0.13 200)`) sparks to white (`oklch(0.98 0.04 200)`) over `0.11s`, recolours to the polarity read
off the element's `data-polarity` (`red` → alarm `oklch(0.66 0.2 25)`, else amber `oklch(0.8 0.14 85)`) over
`0.13s`, holds `0.4s`, then fades `opacity → 0` over `0.27s` `power1.in` — ~0.9s total, well under the WCAG
2.3.1 ≤3/s cap; one tween serves both red fault/conflict and amber reroute; mirrors podstage's
`refused`/`refusedred` keyframes), and `packet` (the travelling flow packet riding its
conduit via GSAP MotionPath — 05n, reading the path off the element's `data-path`, replacing the old CSS
`offset-path` + `offsetDistance` tween). The `useEngineTimeline(rootRef, node)` hook reads
`useShouldAnimate()`; in a `useLayoutEffect` it bails when there is no root or `!animate`. Otherwise it runs in
two phases. **(1) RETRACT (5o)** — BEFORE the context, it selects the already-drawn lanes that have left `on`
(`[data-drawn]` filtered to `data-draw !== "on"`), un-stamps them immediately (so a fast re-activation re-picks
them as `fresh` and re-draws), and erases them tail-to-tip: a `gsap.set` first **locks the stroke + filter to
cyan** (`oklch(0.85 0.13 200)` + a 3px cyan drop-shadow) because by the time this runs the CSS class has
already flipped `running → complete` (= amber), so without the lock the retract would play amber instead of the
expected cyan; then `gsap.to(..., { drawSVG: "100% 100%", 0.45s, power2.in, overwrite: true })` shrinks the
visible segment to nothing, and `onComplete` does `clearProps: "strokeDashoffset,strokeDasharray,stroke,filter"`
so each lane settles back at its CSS end-state. **(2) DRAW** — then one `gsap.context` over the root draws each
active lane with DrawSVG **once per lane** (05n — `gsap.from` over `[data-draw='on']` lanes not yet stamped
`data-drawn`, `{ drawSVG: 0, ...DRAW, stagger: 0.1, overwrite: true }`). The stamp is now applied on
**`onComplete`, not eagerly** (5o): StrictMode double-invokes the effect (run → revert → run), and the old eager
stamp made run-1 stamp, the revert kill the draw, and run-2 skip as already-stamped — so the draw-on never
animated; stamping on complete lets the surviving mount actually draw. The stamp (a DOM attribute) survives
`ctx.revert()`, and the retract phase above is what un-stamps a lane that left `on`, so a beat step never
re-sweeps an already-drawn arc (the F11 regression fix). Then `buildFx(q)`; the hook returns `ctx.revert()` for
teardown. The shared `DRAW` = 0.6s `power2.out`, `stagger: 0.1`; the retract tween is 0.45s `power2.in`.
The dependency list is `[rootRef, animate, signature, node.worktreeGroup]` — `signature` already folds in
phase + the draw/fx state, so this re-runs only when the choreography inputs change.

### Conventions

GSAP selects elements by `data-draw` / `data-fx` attributes the component renders, never by querying React
refs per element — the hook is structure-agnostic. Tween constants live as module `const`s (`DRAW`, the
per-fx durations). Comments tie each fx back to the CSS keyframe it replaced.

### Invariants And Boundaries

- **Property-split law (`05f` §8.1):** GSAP owns the stroke reveal (DrawSVG draw-ons + the tail-to-tip retract),
  the travelling packet's transform (MotionPath), and the `data-fx` repeating loops ALONE; Motion owns the
  NODES' opacity/transform/scaleY/fill + enter/exit. The same property/element is never driven by both systems —
  the packet is a GSAP-exclusive `<circle>`, not a Motion element, so MotionPath owning its transform keeps the
  law. The retract's transient `stroke`/`filter` lock is GSAP-only and always `clearProps`-released back to the
  CSS class, so no static colour is left shadowing the recipe.
- **StrictMode-safe stamping (5o):** the draw-on stamps `data-drawn` on `onComplete`, never eagerly, so the
  StrictMode run → revert → run double-invoke can't stamp-then-skip and leave the lane undrawn.
- **Gated by `useShouldAnimate()`:** under `data-effects=off` / `prefers-reduced-motion` the effect returns
  before building anything — no `gsap.context`, no ticker — so the rendered end-state stands and the
  Playwright/vitest snapshots stay deterministic. (`EnclosureProcessMap.test.tsx` spies on `gsap.context` to
  prove this both ways.)
- **Alarm cap:** the `fault` / `stop` flickers stay ≤3 flashes/s (WCAG 2.3.1).
- **`fxSignature` folds in states the reducer can actually emit.** The refused fold-in filters on `failed`
  and `stale`, both of which `_seed_edge_state` returns. Do not re-add `refused`: no reducer path produces
  it, so the arm would be dead on arrival and would make the signature claim a beat that cannot occur.
- **One context per enclosure**, scoped to the SVG root; `ctx.revert()` restores all inline state on
  unmount/re-run, so a re-key (`worktreeGroup`) or a phase change cleanly rebuilds.
- Pure motion driver: it reads the `node` projection + a ref; it renders nothing and owns no DOM structure.

### Todos

None tied to a non-active task.

## Repo-Internal References

This is a same-repository motion hook; the proving evidence is the source plus the gate and the render that
produces the `data-draw`/`data-fx` elements. The `system/sources.md` registry lists no Domain Documentation
entries, so the GSAP/Motion library docs are not cited here — the split is proven by the in-repo code.

| Finding | Anchor | Source |
| --- | --- | --- |
| `phaseStage` / `fxSignature` / `buildFx` + the `useEngineTimeline` context (retract + draw-on + fx, gated). | `phaseStage`; `fxSignature`; `buildFx`; `useEngineTimeline` | dashboard/src/panels/engine-room/useEngineTimeline.ts:32-49; dashboard/src/panels/engine-room/useEngineTimeline.ts:54-76; dashboard/src/panels/engine-room/useEngineTimeline.ts:83-160; dashboard/src/panels/engine-room/useEngineTimeline.ts:168-247 |
| `fxSignature`'s refused fold-in now filters `failed`/`stale` only. | `fxSignature` | dashboard/src/panels/engine-room/useEngineTimeline.ts:54-76 |
| `_seed_edge_state` — the states a seed edge can actually carry; `refused` is not among them. | "def _seed_edge_state(" | mcp/src/agents_remember/observer/reducer_impl/_processes.py:638-638 |
| `EngineProcessEdge`'s documented `state` vocabulary, which never listed `refused`. | `EngineProcessEdge` | mcp/src/agents_remember/observer/projection.py:791-810 |
| RETRACT phase (5o) — departing lanes erased tail-to-tip, stroke locked cyan via `gsap.set` before the tween, `clearProps` stroke/filter on complete. | `clearProps` | dashboard/src/panels/engine-room/useEngineTimeline.ts:194-212 |
| Draw-on stamps `data-drawn` on `onComplete` (5o StrictMode fix); the `refuse` one-shot and the gentle ~1.7s sine `fault` breathe. | `buildFx`; `useEngineTimeline` | dashboard/src/panels/engine-room/useEngineTimeline.ts:83-160; dashboard/src/panels/engine-room/useEngineTimeline.ts:168-247 |
| The honest-motion gate that suppresses the whole hook under effects-off/reduced-motion. | `useShouldAnimate` | dashboard/src/panels/engine-room/useShouldAnimate.ts:19-37 |
| The canvas that renders the `data-draw='on'` / `data-fx=…` elements + wires this hook to the `<svg>` root. | `EnclosureCanvas` | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:42-93 |
| `EngineProcessNode` / `EngineProcessEdge` (the `phase` / `edges` / `landing` / `providers` / `seedFallback` / `memoryMode` it reads; `EngineProcessEdge` no longer declares `refusedPolarity`). | `EngineProcessNode`; `EngineProcessEdge` | dashboard/src/types/projection.ts:152-160; dashboard/src/types/projection.ts:162-202 |
| The GSAP-gate determinism tests that pin the no-ticker-under-effects-off contract. | "EnclosureCanvas — GSAP gate (05f §8.4 — no ticker under effects=off)" | dashboard/src/panels/engine-room/EnclosureProcessMap.test.tsx:55-90 |

## Current L5I Maintenance

The GSAP hook now gives a stroked scan ring `vector-effect="non-scaling-stroke"` before animating
its radius-equivalent scale, and animates surge bands by `scaleY` from the link origin. Its scoped
context pauses every tween while the observed canvas is hidden and resumes the same context on
re-show, including a context rebuilt during the hidden interval.

## 260727-CHATS-IM-L2 Current Delta

`useEngineTimeline` accepts an optional effects-root ref and combines selectors from both SVG
roots. The same timeline and visibility hooks own all targets, so splitting the DOM does not
create a second ticker or alter choreography.

## Update History

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 13 citation items; scoped citation check now passes.

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the
  `observer/projection.py` citation after that module was restructured. cit:([`EngineProcessEdge`], mcp/src/agents_remember/observer/projection.py:791-810),
  read there: cit:([`EngineProcessEdge`], mcp/src/agents_remember/observer/projection.py:791-810),
  the nine-state comment directly above cit:([`EngineProcessEdge`], mcp/src/agents_remember/observer/projection.py:791-810), and the class's last field
  cit:([`EngineProcessEdge`], mcp/src/agents_remember/observer/projection.py:791-810) — so the "no `refusedPolarity` field" half of the claim is provable at the range
  end. No body claim changed.

- 2026-08-01T10:18+02:00 — 260731-EFA-L4 curator: corrected the `fxSignature` description. The refused
  fold-in no longer matches `state === "refused"` — the filter is `failed`/`stale` only. Verified there is
  no reducer path to `refused` (`_seed_edge_state` returns failed/running/stale/complete/skipped/planned;
  `EngineProcessEdge`'s state comment lists nominal|running|blocked|failed|stale|skipped|complete|planned|
  unknown; `git log --all -S 'state="refused"'` returns zero commits ever), so the removed arm was dead
  against every payload the server has ever sent. Recorded that "refused" survives as the name of the
  visual beat (`data-fx='refuse'`, the `refuse` tween) rather than as an edge state, and added the
  invariant against re-adding the arm. Repaired the citations: the whole-file row L22-L165 → L32-L247,
  RETRACT L124-L143 → L194-L212, the draw-on/fx row L73-L162 → L83-L162;L215-L226, and
  `EngineProcessNode` L224-L285 → L538-L608 (the old range fell inside `LifecycleProjection`/
  `EnclosureNode` territory and contained neither engine type).

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: extended the timeline selector
  across the structural SVG and optional sparse effects SVG. One timeline still owns the same
  draw and repeating choreography; only the queried roots changed. Verification metadata remains
  pinned until closeout.

- 2026-07-24T13:17:17Z — Curator: documented composited SVG effects and the hidden-canvas pause
  invariant; verification fields remain pre-commit.

- 2026-06-22T11:00 — slice 05o: `buildFx` gained a **`refuse`** flash — a ONE-SHOT refused-conduit recolour on
  `[data-fx='refuse']` (a rejected seed/integration lane): a `gsap.timeline` with `repeat: 0` (NOT a loop) that
  sparks cyan (`oklch(0.85 0.13 200)`) → white (`oklch(0.98 0.04 200)`) over `0.11s`, recolours to the polarity
  read off `data-polarity` (`red` → alarm `oklch(0.66 0.2 25)`, else amber `oklch(0.8 0.14 85)`) over `0.13s`,
  holds `0.4s`, then fades `opacity → 0` over `0.27s` `power1.in` — ~0.9s total, well under the WCAG 2.3.1 ≤3/s
  cap (one tween serves both red fault/conflict and amber reroute; mirrors podstage's `refused`/`refusedred`
  keyframes). `fxSignature` now also folds in the **refused edges** (`edges` filtered to
  `refused`/`failed`/`stale`, `kind:state`, sorted) so the one-shot flash re-arms when the refuse beat lands — a
  refused lane is not a `running` lane, so the `draws` segment alone misses it. Verification metadata pinned
  until closeout stamps the 05o code commit.
- 2026-06-22T00:29 — slice 05o T3B: `buildFx` gained a **`scan`** loop — the pre-block verify sweep on
  the lane under check: `gsap.fromTo([data-fx='scan'], {attr:{r:6}, opacity:0.9}, {attr:{r:52}, opacity:0,
  duration:1.2, ease:"power1.out", repeat:-1})`. Transient (no settled state; the `<circle>` is rendered only
  while `animate`). `fxSignature` already re-runs the effect when a `ledger-map` edge goes `running`, so the
  scan loop builds/tears down with the verify beat. Verification metadata pinned until closeout stamps the 05o
  code commit.
- 2026-06-21T23:35 — slice 5o retract + StrictMode + gentle fault. Added a **RETRACT phase** ahead of the
  `gsap.context`: departing lanes (`[data-drawn]` filtered to `data-draw !== "on"`) are un-stamped, then erased
  tail-to-tip via `gsap.to(..., { drawSVG: "100% 100%", 0.45s, power2.in })`. A `gsap.set` first **locks the
  stroke + filter to cyan** (`oklch(0.85 0.13 200)` + 3px cyan drop-shadow) because the CSS class has already
  flipped `running → complete` (amber) by then, so the lock keeps the retract cyan; `onComplete` `clearProps`s
  `strokeDashoffset,strokeDasharray,stroke,filter` back to the CSS end-state. Moved the lane un-stamp out of the
  draw context into this retract block. Draw-on now stamps `data-drawn` on **`onComplete`, not eagerly** — the
  StrictMode run → revert → run double-invoke had the eager stamp make run-1 stamp, the revert kill the draw, and
  run-2 skip (already stamped), so the draw never animated; both `gsap.from` (draw) and `gsap.to` (retract) gain
  `overwrite: true`. The `fault` fx is now a **gentle ~1.7s `sine.inOut` breathe** (`opacity 0.5 → 0.95`),
  replacing the old 0.34s `steps(1)` strobe (still well under the WCAG 2.3.1 ≤3/s cap). Verification metadata
  pinned until closeout stamps the 5o commit.
- 2026-06-21T09:57+02:00 — Slice 05n: migrated the draw-on to GSAP **DrawSVGPlugin** and the packet to
  **MotionPathPlugin** (both registered at module scope), replacing the manual `strokeDashoffset` sweep and the
  CSS `offset-path`/`offsetDistance` tween. Draw is now **one-shot per lane**: only `[data-draw='on']` lanes not
  yet `data-drawn` are drawn (`gsap.from(..., { drawSVG: 0, ...DRAW })`), stamped after, the stamp surviving
  `ctx.revert()` and cleared when a lane leaves `on` — so a beat step no longer re-sweeps drawn arcs (the **F11**
  regression). The packet reads its conduit path off `data-path` and rides it via MotionPath
  (`alignOrigin [0.5,0.5]`), rendering only while `animate` (**F12** — the old `attr:{offsetDistance}` tween
  targeted a non-existent SVG attribute, so the dots never moved). Property-split holds (GSAP: stroke reveal +
  packet transform; Motion: node opacity/transform). The effects-on GSAP-gate test exercises DrawSVG/MotionPath
  in jsdom via the `src/test/setup.ts` geometry stub. Live-verified on the bench (dots traverse; no re-sweep
  across B3↔B4) + full gate green; verification metadata pinned until closeout stamps the 05n commit.
- 2026-06-21T02:27+02:00 — Created for slice 05k: the GSAP motion substrate hook. One `gsap.context` per
  enclosure scoped to the SVG root drives the `[data-draw='on']` strokeDashoffset draw-ons (0.6s `power2.out`,
  stagger 0.1) + `buildFx` (the fault flicker ≤3/s, reindex center-out scaleY pulse, warp surge bands,
  attention breath, terminal STOP flash ×3, travelling packet) — the repeating fx that used to be CSS
  `@keyframes`. Gated by `useShouldAnimate` (no context/ticker under effects-off/reduced-motion); re-runs on
  `fxSignature` (phase + running draws + landing + engines + seedFallback + memoryMode) + `node.worktreeGroup`;
  `phaseStage` maps phase → power-up/closeout/integrate/teardown/idle. Property-split with Motion per §8.1
  (GSAP owns stroke-dashoffset + fx; Motion owns opacity/transform/scaleY/fill). Verification metadata pinned
  until closeout stamps the 05k code commit.
