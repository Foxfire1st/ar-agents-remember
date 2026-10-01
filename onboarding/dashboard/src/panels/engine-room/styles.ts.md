# dashboard/src/panels/engine-room/styles.ts

## Governing Overview

[panels/engine-room overview](overview.md)

## 260731-EFA-L8 Split Layout

The 1,287-line `engineRoomStyles.ts` was split by semantic axis into six style
domains under `dashboard/src/panels/engine-room/` (260731-EFA-L8 R6 ruling: split by
semantic axis, no exemption list): `layout.styles.ts` (room shell/grid/stack/health
layout), `stage.styles.ts` (scene SVG, gauges, wires, lanes, coupler), `ledger.styles.ts`
(memory-ledger popover), `flow.styles.ts` (conduits, packets, failure overlays),
`remote.styles.ts` (remote/PR strip), and `backdrop.styles.ts` (atmospheric backdrop).
`styles.ts` is the 15-line barrel that re-exports all six, preserving every importer.
This card's historical recipe commentary documents the pre-split module; current
recipe-level detail is routed to the per-domain sidecars.

## Purpose

This is the visual language for the enclosure-centered Engine Room process map, expressed as Panda `css`/`cva` recipes. State and severity are carried by COLOUR (note 08), never by ad-hoc chrome, so the truth always comes from the model. One recipe per semantic axis — process health, fact state, conduit state, engine runtime — plus the layout, header, fleeting-banner, chip, node, conduit, timeline, and diagnostics styles the panel composes.

## Code Commentary

### Logic

Slice 16 keeps the left enclosure stack from stretching when the panel has spare height:
`stackList` starts both grid content and grid items at the top (`alignContent: "start"` and
`alignItems: "start"`), so a single enclosure row keeps its intrinsic card height instead of filling
the entire stack panel.

Static atoms are plain `css({...})`; stateful styles are `cva({base, variants})` keyed by one semantic axis. Axis recipes: **health** — `stackItem`/`healthDot`/`phaseChip`; **factState** — `factChip`/`nodeBox`; **state** (conduit) — the SVG stroke recipe `conduitLine` + its `conduitSvg` wrapper (5f S0); **runtimeState** — `engineSilhouette`. The **full-bleed room layout** (5f S1, §4.2): `roomShell`/`roomGrid`/`roomStage`/`roomZone`/`roomHeader*` + the `roomCaution` severity `cva`. The **fleeting banner** atoms (5f S2, §2.1) — `fleetingBanner` (dashed-alarm ghost box), `fleetingLabel`, `fleetingReason`, `fleetingChoices`, `fleetingChoice` — style a provisional pre-contract blocked-start enclosure (creation gated, contract not yet written + the recovery choice). The **flow-packet** atom (5f S4, T8/T9) — `conduitChevron` — colours the travelling energy packet GSAP runs along a running conduit during clone/seed. The **pod-stage bird's-eye** atoms (5g G1) — `sceneSvg`, `worldLabel`, `enclosureBorder`, `svgNodeBox` (factState) + `svgNode*` text, `engineGaugeOut`/`engineCharge`/`engineDiv`/`engineGaugeLabel` (the runtimeState podracer gauge), `warpCoupler*` (bound) + `flowConduit` (conduit state on a positioned SVG path) — style the two-world scene `EnclosureCanvas` renders. **5g G2** added the motion: `engineCharge` runs the center-out `chargeSweep` on an indexing engine, `flowConduit` running draws on (`conduitDraw`, needs `pathLength=100`) in cyan, and `flowPacket` is the travelling cyan dot along a running conduit (`pktRun`, offset-path set per-conduit). The **failure-overlay** atoms (5g G3) — `gateBar` (the steady red lane gate), `attnBadge`/`attnText` (the breathing ⚠ attention parity), `reasonBadge`/`reasonDot`/`reasonText` (the local cyan-dot reason pill), and `svgChip`/`svgChipText` (recovery chips) — render a blocked lane's gate + reason + attention + choices; blocked stays STEADY. **5g G4** added the engine fault/reroute: `engineGaugeOut` `down` flickers (`pulse`, the isolated fault ≤3/s — distinct from the steady gate), and `engineReindexCharge` is the AMBER center-out reindex pulse (t9c `seedFallback`, a fallback not a failure). `phaseChip` is now `nowrap` so the stack-item phase never wraps. **5g G5** reworked the **engine palette to a green/go semantic**: `engineGaugeOut`/`engineCharge`/`engineSilhouette` `nominal` is now **green** (`mint`, a clear "powered-on" fill) — active=green, inactive (`configured`/`unknown`)=empty/`dormant`, booting=cyan, fault=red, reindex-fallback=amber (the new `engineReindexOut` amber outer paired with `engineReindexCharge`). G5 also added the live/teardown overlays — `stopBar`/`stopText` (the t14c terminal STOP) and `dissolveShell`/`abandonRecord` (the t18 abandon dissolve) — and the **side-panel fix**: `stackList` is `overflowX: hidden` + `minWidth: 0` (vertical scroll only), `minWidth: 0` threads down `stackItem`/`stackItemHead` so the name ellipsizes and the phase pill never clips, and a `stackRepo` line lifts the repo label off the chip row. All consume tokens via the `token(colors.*)` indirection. **5g G6** added the atmospheric backdrop atoms — `backdrop`/`backdropVideo` (the faint amber-tinted blueprint-boomerang `<video>`, `objectFit: cover` + `mixBlendMode: screen` + `opacity: .14` + a centre **radial vignette mask** — `maskImage`/`WebkitMaskImage`, scoped to the `<video>` so its faded edges fall back to the dark stage and the SVG scene layered above is untouched — mounted only when effects are on) and `stageContent` (the scene layer stacked above it). The **visual-parity** decal atoms then add `engineSpine` (the faint centre line) + `enginePetal` (runtime-coloured flank petals, a `cva` keyed on `runtimeState`), `officialWire` (the official-line provider→branch conduit), `canopyStroke` (the HUD canopy frame — group stroke inherited by its children), and `laneFlag`/`laneFlagText` (the toned lane-annotation plates, `cva` on `ledger`/`historical`). (The Engine Room's fixed-height fill itself is a `Panel` `fill` variant in `grammar/Panel.tsx`, not a style here.) **5h H2** adds the closeout-train recipes — `closeoutBeat`/`closeoutBeatG`/`closeoutBeatLabel` (the T13 closeout-order beat plates; mint = the settled/done look, `closeoutBeatG` carries the `closeoutSweep` sweep), `closeoutRail` (the dashed connector), and `closeoutTrainLabel`. **5h coupler fix** adds the ledger-coupler recipes — `warpLinkGlyph` (the drawn chain-link icon replacing the contract node) and `warpSurge` (a `cva` keyed on `dir: up|down` — the two hot warp-core surge bands; the keyframes live in `index.css`, hidden under effects=off). **5h ledger popover** adds the coupler-popover recipes — `ledgerButton`/`ledgerButtonLabel` (the SVG label-as-button trigger: a faint amber chip that brightens on hover, the label text on top with `pointerEvents:none`), `ledgerCard`/`ledgerCardHead`/`ledgerTable`/`ledgerRowCss` (the HTML popover content + the highlighted current row), `ledgerScroll` (a `cva` keyed on `expanded`: collapsed caps at a compact `13rem`, expanded **extends** the frame to `min(72vh, 46rem)` so the full window shows — the inner scroll kicks in only if it still overflows the viewport), `ledgerShowMore` (the "▾ show N more" expand control), and `ledgerMore` (the "+N more in memory.md" file footer). **5h Tier 2** adds the 6-column row recipes — `ledgerDate` (muted, compact, `tabular-nums`), `ledgerMsg` (max-width + ellipsis truncation), `ledgerHashCode`/`ledgerHashMem` (the `fonts.mono` hashes, right/left-aligned so the two meet the centre seam), and `ledgerSeam` (the ⇄ glyph) — and widens `ledgerCard` `maxWidth` to `min(92vw, 46rem)` for the wider row. **5h H3** adds the **remote/PR strip** recipes beyond the official line: `remoteChip` (a `cva` keyed on `tone`: `planned` = dashed/muted · `live` = amber outline · `done` = mint fill) with `remoteChipLabel` (15px) + `remoteChipState` (12px, the terse status word), and `prBadge`/`prBadgeLabel` (14px) + `prBadgeSub` for the distinct PR pill (`open` = amber outline → `merged` = mint fill) — all sized as **peers of the branch nodes** so the labels read at the 0.76× canvas scale (the first cut at 9–10.5px was unreadable). The strip is **wired** by `remoteConnector` (solid amber, the code chain feat→PR→main) and `remoteConnectorCarry` (dashed muted, the code→memory carryover handoff), with `remoteStripHeader` the centred band label. The only motion is the gated `fill`/`stroke` transition on a projection state flip (frozen to the settled end-state under `data-effects=off`); the same colour-as-state honesty law holds (a `planned` ref is never shown in the `live` register — honest-motion §4). **5h H4** adds `cleanupRecord` — the success-toned counterpart to `abandonRecord` (solid mint vs dashed-dormant) for the cleanup teardown's de-materialisation banner; the `.dissolve` shell (`dissolveShell`) is reused unchanged. **5k F6** then makes `cleanupRecord` an absolute overlay (`position: absolute`, `top/left/right: 0`, `zIndex: 3`, `backgroundColor: token(colors.bgPanel)`) within the relative `stageContent` — instead of sitting in the column flow (which pushed the whole canvas DOWN when the banner popped in) it floats over the canvas top, the panel background keeping it readable over the scene. **5o glow pass** then layers `drop-shadow` glows so a powered engine reads as energised rather than flat — driven by the engine-room visual-language spec (`docs/design/engine-room`): `engineGaugeOut` is reworked to a **constant GOLD bezel** (base `stroke: amber`, `strokeWidth: 2`, `drop-shadow(amber)`) since the body charge + petals carry runtime state, not the frame — `nominal`/`indexing` are now empty (gold bezel), `configured` dims the bezel (`opacity 0.5`, `filter: none`), `unknown` is dashed/dim, and `down` is the ONE exception that re-colours the frame red (`stroke: alarm` + `drop-shadow(alarm)`) so a faulted engine is unmistakable; its fault motion is now a **gentle breathe** (`data-fx='fault'`, ~1.7s sine), never a strobe. `engineCharge` gains state-coloured glows (`nominal` mint, `indexing` cyan, `down` alarm; `configured`/`unknown` stay glow-less = drained). `warpCouplerBar` gets a structural 2px amber glow (spec importance scale). `flowConduit running` glows cyan 3px (the active flow); `blocked`/`failed`/`stale`/`planned` stay glow-less (a connection, not an action). `flowPacket` carries the brighter 5px cyan glow, `gateBar` a 7px alarm glow. **`closeoutTrainLabel`** was re-toned for legibility on the textured backdrop — it is a bare caption with no chip plate, so its fill moved from the dim `muted` 9px to `ink` 10px (and `letterSpacing` 0.08em → 0.06em); the neutral-vs-mint tone still keeps it a caption for the green beats. **5i** added an interim CSS **motion substrate** (`sceneSvg` global transition + a `landingEnter`/`landingIn`
atom + `transform: scaleY()` on `engineCharge`); **slice 05k removes all of it** to reach the `05f` §8 end
state — canvas motion is GSAP (`useEngineTimeline`) + Motion (`EnclosureCanvas`), and these recipes are now
**static** (colour-as-state + layout only). What 05k stripped here, recipe by recipe:

- **`sceneSvg`** — dropped the global `& g,& rect,& line,& path,& circle,& text { transition: … }` substrate
  (ported from podstage.html's `#scene` trick). It now carries layout only (`display`/`width`/`flex`/
  `minHeight`/`overflow`). The comment records why: CSS can't stage a sequence or animate an unmounting node,
  which is what broke the tear-down de-materialise + the conditional landing apparatus.
- **`landingEnter`** — **removed** (the `animation: landingIn …` atom). Motion's `AnimatePresence` enter/exit
  in `EnclosureCanvas` now glides the conditionally-mounted landing elements in.
- **`engineCharge`** — back to **fill-only**: each `runtimeState` variant carries just the colour-as-state
  fill. Task 31 adds a `missing` runtime variant to the gauge outer/charge/petal recipes: missing uses an
  alarm-toned dashed outer, alarm fill, and no petals, so an expected-but-unobserved provider slot is visible
  without looking like a live faulting engine.
  `fill` (cyan charging → mint "went green" → amber/alarm); the `opacity` + `transform: scaleY()` are gone.
  Motion (`chargeMotion` in `EnclosureCanvas`) owns the animated `scaleY` + opacity (the center-out boot-fill
  growth), so CSS and Motion never write the same property; `transformBox: fill-box` + `transformOrigin:
  center` stay so Motion's scaleY grows center-out.
- **`engineReindexCharge`** — dropped `animation: chargeSweep …`; GSAP `data-fx='reindex'` drives the
  amber center-out scaleY/opacity pulse. *(This is the recipe `chargeSweep` actually backed — see the
  `index.css` sidecar's corrected note: `chargeSweep` was NOT orphaned in 5i.)*
- **`engineGaugeOut` `down`** — dropped `animation: pulse …`; the fault flicker is GSAP `data-fx='fault'`
  (≤3/s).
- **`attnBadge`** — dropped `animation: attnBreath …` (GSAP `data-fx='breath'`); **`stopBar`** — dropped
  `animation: stopFlash …` (GSAP `data-fx='stop'`).
- **`warpSurge`** — collapsed from a `cva` keyed on `dir` (`warpSurgeUp`/`warpSurgeDown` animations) to a
  plain `css` (no animation, `opacity: 0` at rest); GSAP `data-fx='surge'` + `data-dir` drive the two bands.
- **`closeoutBeatG`** — **removed** (the `animation: closeoutSweep …` atom); `AnimatePresence` owns the
  closeout-train enter/exit.
- **`dissolveShell`** — dropped `opacity`/`filter: grayscale()`/`transition`; it is now the flex layout
  passthrough only. Motion in `EnclosureProcessMap` owns the abandon opacity + grayscale fade.
- **`warpCouplerG`** — **removed**; Motion owns the coupler group's opacity (the bound dim + the build-up
  `visible` gate).
- **`enclosureBorder`** — dropped `opacity: 0.5`; Motion owns the border's opacity (drawn in on build-up,
  collapsed on teardown).
- Transition removals on otherwise-static recipes: `remoteChip` / `prBadge` bases (`transition: fill/stroke`)
  and `ledgerButton` (`transition: fill`).

**ADDED in 05k — `worktreeWire`** (the worktree engine→branch wiring, the mirror of `officialWire`): a plain
`css` with `fill: none` / amber `stroke` / `strokeWidth: 2` / round caps. It deliberately carries **no
`opacity`** because Motion (`EnclosureCanvas`) owns the wire's opacity (it fades in when the engine
materialises at B3 and out when it powers down at D5). A className `opacity` would **shadow** Motion's
animated value under `initial={false}` (the class wins on a static frame) — exactly the bug that left the
worktree wires dangling with no engine. The 5h H3 `prBadgeSub`/`remoteConnector`/`remoteConnectorCarry`
recipes remain exported but unused (their call sites were removed in the 5i dock rework).

**05o T3B failure-mode primitives.** Two new atoms back the engine-room failure-modes spec (§10,
`docs/design/engine-room/engine-room-visual-language.html`): **`scanRing`** — the cyan pre-block verify
sweep (a `<circle data-fx='scan'>` on the lane under check): `fill: none` / cyan `stroke` / 2px / a 4px
cyan `drop-shadow` glow / **`opacity: 0` at rest** (transient, no settled state like `flowPacket`/`warpSurge`;
GSAP `useEngineTimeline buildFx` drives the r/opacity expand-fade, `repeat:-1`, and the `<circle>` is only
rendered while `animate`, so under effects=off it is absent — not frozen). **`ghostedLane`** — the held-lane
treatment (`opacity: 0.32` + `filter: grayscale(0.45)`): a plain static `css` applied projection-driven to
the **inner conduit `<path>`** of a gated memory lane while its sibling code lane stays solid (real-but-held,
distinct from `planned`'s dashed grey). It is intentionally applied to the inner `<path>`, **not** the
Motion group, so its `opacity` never shadows Motion's group opacity on a static frame (the `worktreeWire`
property-split law). Neither atom animates from CSS (GSAP/Motion own all canvas motion, §8).

**05o T1B pruned node + FLEETING block box.** Two more spec-driven additions: **`prunedNode`** — the
dormant/desaturated treatment for the stale code base node (the spec §3 **pruned/retired** register): a
desaturated `dormant` stroke + a dark muted fill (`oklch(0.18 0.02 25)`) + a dashed `3 3` outline at `0.8`
opacity, projection-driven onto the stale base node when local main is behind upstream (the stale-base
block), and static — distinct from `planned`/`missing` (dotted, not-yet) and from a live amber box; it
mirrors the spec `.node.pruned .box`. And the **FLEETING-block box** trio — **`fleetingBox`** /
**`fleetingBoxTitle`** / **`fleetingBoxReason`** — the big red provisional enclosure (podstage `.fbox`) that
**replaces** the old HTML fleeting banner: a born-blocked (stale-base / pre-contract) enclosure renders as a
dark-red dashed box over the worktree footprint, REPLACING the dashed-amber `enclosureBorder`, with the
BLOCKED title + reason centred and the recovery chips along the bottom, so "this enclosure is gated, not yet
real" reads at a glance. The box fill was tuned brighter than the prototype's `.55` — `opacity 0.82` plus a
soft alarm `drop-shadow` glow — so it reads as a clear red panel over the dashboard's blueprint backdrop
`<video>` (which the prototype lacks); the box rect carries the dim while the title/reason sit above it at
full opacity as siblings. (The `scanRing` + `ghostedLane` atoms were documented in the prior 05o T3B entry.)

**05o remaining failure-mode primitives.** Three more spec-driven atoms cover the modes the earlier 05o
passes left open. **`refusedConduit`** — the shared flash for a conduit that did not take (T9B / T9C /
T14C): a `cva` keyed
on a `polarity` variant (`amber` = a reroute/fallback, the T9C CGC-seed-**stale** → reindex lane; `red` =
a fault/conflict, the T9B GrepAI seed fault + the T14C integration conflict), each carrying the matching
`stroke` + a 4px `drop-shadow` glow, and a `base` that rests at `opacity: 0` (a one-shot flash has no settled
state — it ends GONE, like the prototype's `refused` keyframe ending at opacity 0). The colour sweep + fade
are owned by GSAP (`data-fx='refuse'`, `repeat:0`, CSS stays static per §8); polarity is **derived** from
`edge.state` alone (failed→red / stale→amber) — never a class, and never a field on the edge, because
`EngineProcessEdge` has no polarity field to read. "Refused" is the name of the beat, not an edge state:
the reducer has never emitted `state="refused"`. **`engineDropout`**
— a static alarm-toned dashed halo (`stroke: alarm`, `strokeDasharray: "5 5"`, `opacity: 0.5`, 4px alarm glow)
marking an UNLIT worktree engine slot as HELD for T7B (the provider-plan block — the engines never light
because the runtime config is missing), distinct from the build-up's faded-absent not-yet-present engine; no
animation. And the **moved-indicator** trio — **`movedBadge`** / **`movedTriangle`** / **`movedText`** — the
soft-cyan ▲ up-triangle pill for T12B live-sync that announces the UPSTREAM memory ref advanced
(`origin/mem-main` moved while the worktree holds local commits): it mirrors the `reasonBadge`/`reasonDot`/`reasonText`
geometry but stays in the SOFT cyan register (a notification that a sync CHOICE is needed) rather than the
alarm gate that escalates a beat later — `movedBadge` the dark-cyan pill plate, `movedTriangle` the glowing
cyan pointer, `movedText` the cyan caption.

**05o engine-gauge de-glow + gold petals** (developer call, mirrored into the spec §6 first): `engineGaugeOut`
dropped its base `drop-shadow(amber)` — the gold bezel is now **FLAT** (the body charge carries runtime state,
not the frame); the lone exception is `down` (fault), which still re-colours the frame red **+ keeps its red
glow** so a faulted engine is unmistakable (the redundant `filter:"none"` overrides on `configured`/`unknown`
were dropped with the base glow). `enginePetal` is now **constant gold**: the amber `stroke` moved to `base`
and the per-state variants carry only `opacity` (state is the body fill + bezel, not the petals) — so the
petals read as structural line-art alongside the always-amber `engineSpine`, present on active engines
(`0.6`) and hidden when off (`configured`/`unknown` → `0`).

### Invariants And Boundaries

Each recipe exposes exactly ONE variant group named after its semantic axis; callers pass that axis from
model state, never hard-code chrome. **Canvas recipes are now static** (`05f` §8): no recipe drives a canvas
animation/transition — GSAP (`useEngineTimeline`) owns the **DrawSVG** draw-ons + the **MotionPath** packet
(05n) + the `data-fx` repeating loops, Motion (`EnclosureCanvas`/`EnclosureProcessMap`) owns
opacity/transform/scaleY/fill + enter/exit, both gated by `useShouldAnimate`. So `flowConduit` `running` is now
a **solid** stroke (DrawSVG owns the dasharray; the old `strokeDasharray:"100 100"` + the `pathLength=100`
normalization are gone), its `planned` dash re-tuned to real units (`"9 7"`, was `"3 5"` at pathLength 100),
and `flowPacket` carries no `offset-path` (MotionPath rides it via the element's `data-path`). The only `animation:` left in this module is the app-wide
`pulse` (the health/factState/conduit/stack-item `cva`s flash on `failed`/`running`/`current`), which is
freezable by `html[data-effects="off"]` and is NOT a canvas keyframe. **Property-split law (§8.1):** a
recipe that hands a property to Motion/GSAP must NOT also set it — `worktreeWire`/`enclosureBorder` carry no
opacity, `engineCharge` carries no scaleY/opacity, so a static className can't shadow the inline animated
value under `initial={false}`. The fleeting atoms read in the ghost/alarm register so a provisional
enclosure is visually distinct from a live one (§2.1). Colour-as-state is load-bearing (note 08). This
module exports style objects/recipes only — no React, no data, no panel logic.

### 260712-TRH-L7 fact-state styling

The fact-state recipes include a visibly distinct stale variant used by landing refs. This keeps freshness truth in the semantic style axis instead of hiding it in ad-hoc component chrome.

## Evidence

### Repo-Internal References

- `sceneSvg` is now static layout only — the global `& g,& rect,…{ transition }` substrate is removed (05k). [1]
- `engineCharge` is fill-only colour-as-state (Motion owns the scaleY/opacity boot-fill); `engineReindexCharge` lost `animation: chargeSweep` (GSAP `data-fx='reindex'`). [2]
- `worktreeWire` (05k, NEW) — carries NO opacity so Motion owns the wire's opacity (a className opacity shadows Motion under `initial=false`). [3]
- `warpSurge` is plain `css` (GSAP `data-fx='surge'`); `warpCouplerG` removed (Motion owns coupler opacity). [4]
- `refusedConduit` — the `polarity` amber/red variants over an `opacity: 0` base; the recipe carries colour only, and the polarity it is keyed on is derived from `edge.state` by the canvas. [5]
- `refusedPolarityOf` — the caller that derives that polarity (`failed`→red, `stale`→amber) with no polarity field read. [6]
- `EngineProcessEdge` declares no polarity field and never documented a `refused` state. [7]
- `attnBadge`/`stopBar`/`dissolveShell` lost their `animation`/`transition` — GSAP `data-fx='breath'`/`'stop'` + Motion own them. [8]
- `engineGaugeOut` — **FLAT** gold bezel (05o dropped the base amber glow; `down`/fault keeps the red bezel + red glow); `enginePetal` is constant gold (05o — amber on `base`, opacity-only variants). `engineCharge`/`warpCouplerBar`/`flowConduit running`/`flowPacket`/`gateBar` keep their state-coloured `drop-shadow` glows (settled lanes glow-less). [9]
- `closeoutTrainLabel` — `ink` 10px (was `muted` 9px) for legibility as a bare caption on the textured backdrop; `cleanupRecord` is an absolute overlay (5k F6). [10]
- Fleeting-banner atoms (`fleetingBanner`/`fleetingLabel`/`fleetingReason`/`fleetingChoice(s)`). [11]
- The `healthDot` / fact-state / runtime-state axes (colour-as-state); the only remaining `animation:` is the app-wide `pulse`. [12]
- The GSAP hook + the canvas that read these now-static recipes and drive the motion. [13]

## 260727-CHATS-IM-L2 Current Delta

`fxOverlaySvg` positions a pointer-transparent sibling over the full structural scene at the same
size and view box. It introduces no new effect paint recipe; surge, reindex, and attention keep
their established classes.
