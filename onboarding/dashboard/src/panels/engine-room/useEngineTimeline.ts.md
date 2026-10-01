# dashboard/src/panels/engine-room/useEngineTimeline.ts

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

## Evidence

### Repo-Internal References

This is a same-repository motion hook; the proving evidence is the source plus the gate and the render that
produces the `data-draw`/`data-fx` elements. The `system/sources.md` registry lists no Domain Documentation
entries, so the GSAP/Motion library docs are not cited here — the split is proven by the in-repo code.

- `phaseStage` / `fxSignature` / `buildFx` + the `useEngineTimeline` context (retract + draw-on + fx, gated). [1]
- `fxSignature`'s refused fold-in now filters `failed`/`stale` only. [2]
- `_seed_edge_state` — the states a seed edge can actually carry; `refused` is not among them. [3]
- `EngineProcessEdge`'s documented `state` vocabulary, which never listed `refused`. [4]
- RETRACT phase (5o) — departing lanes erased tail-to-tip, stroke locked cyan via `gsap.set` before the tween, `clearProps` stroke/filter on complete. [5]
- Draw-on stamps `data-drawn` on `onComplete` (5o StrictMode fix); the `refuse` one-shot and the gentle ~1.7s sine `fault` breathe. [6]
- The honest-motion gate that suppresses the whole hook under effects-off/reduced-motion. [7]
- The canvas that renders the `data-draw='on'` / `data-fx=…` elements + wires this hook to the `<svg>` root. [8]
- `EngineProcessNode` / `EngineProcessEdge` (the `phase` / `edges` / `landing` / `providers` / `seedFallback` / `memoryMode` it reads; `EngineProcessEdge` no longer declares `refusedPolarity`). [9]
- The GSAP-gate determinism tests that pin the no-ticker-under-effects-off contract. [10]

## Current L5I Maintenance

The GSAP hook now gives a stroked scan ring `vector-effect="non-scaling-stroke"` before animating
its radius-equivalent scale, and animates surge bands by `scaleY` from the link origin. Its scoped
context pauses every tween while the observed canvas is hidden and resumes the same context on
re-show, including a context rebuilt during the hidden interval.

## 260727-CHATS-IM-L2 Current Delta

`useEngineTimeline` accepts an optional effects-root ref and combines selectors from both SVG
roots. The same timeline and visibility hooks own all targets, so splitting the DOM does not
create a second ticker or alter choreography.
