# dashboard/src/panels/engine-room/styles.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/engine-room/styles.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-07T08:19Z |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `sceneSvg` is now static layout only — the global `& g,& rect,…{ transition }` substrate is removed (05k). | `sceneSvg` | dashboard/src/panels/engine-room/stage.styles.ts:5-11 |
| `engineCharge` is fill-only colour-as-state (Motion owns the scaleY/opacity boot-fill); `engineReindexCharge` lost `animation: chargeSweep` (GSAP `data-fx='reindex'`). | `engineCharge` | dashboard/src/panels/engine-room/stage.styles.ts:125-138 |
| `worktreeWire` (05k, NEW) — carries NO opacity so Motion owns the wire's opacity (a className opacity shadows Motion under `initial=false`). | `worktreeWire` | dashboard/src/panels/engine-room/stage.styles.ts:184-189 |
| `warpSurge` is plain `css` (GSAP `data-fx='surge'`); `warpCouplerG` removed (Motion owns coupler opacity). | `warpSurge` | dashboard/src/panels/engine-room/stage.styles.ts:240-246 |
| `refusedConduit` — the `polarity` amber/red variants over an `opacity: 0` base; the recipe carries colour only, and the polarity it is keyed on is derived from `edge.state` by the canvas. | `refusedConduit` | dashboard/src/panels/engine-room/flow.styles.ts:65-75 |
| `refusedPolarityOf` — the caller that derives that polarity (`failed`→red, `stale`→amber) with no polarity field read. | `refusedPolarityOf` | dashboard/src/panels/engine-room/geometry.ts:124-134 |
| `EngineProcessEdge` declares no polarity field and never documented a `refused` state. | "class EngineProcessEdge" | mcp/src/agents_remember/observer/projection.py:785-785 |
| `attnBadge`/`stopBar`/`dissolveShell` lost their `animation`/`transition` — GSAP `data-fx='breath'`/`'stop'` + Motion own them. | `attnBadge` | dashboard/src/panels/engine-room/flow.styles.ts:127-131 |
| `engineGaugeOut` — **FLAT** gold bezel (05o dropped the base amber glow; `down`/fault keeps the red bezel + red glow); `enginePetal` is constant gold (05o — amber on `base`, opacity-only variants). `engineCharge`/`warpCouplerBar`/`flowConduit running`/`flowPacket`/`gateBar` keep their state-coloured `drop-shadow` glows (settled lanes glow-less). | `engineGaugeOut` | dashboard/src/panels/engine-room/stage.styles.ts:81-102 |
| `closeoutTrainLabel` — `ink` 10px (was `muted` 9px) for legibility as a bare caption on the textured backdrop; `cleanupRecord` is an absolute overlay (5k F6). | `closeoutTrainLabel` | dashboard/src/panels/engine-room/flow.styles.ts:207-207 |
| Fleeting-banner atoms (`fleetingBanner`/`fleetingLabel`/`fleetingReason`/`fleetingChoice(s)`). | `fleetingBanner` | dashboard/src/panels/engine-room/layout.styles.ts:401-409 |
| The `healthDot` / fact-state / runtime-state axes (colour-as-state); the only remaining `animation:` is the app-wide `pulse`. | `healthDot` | dashboard/src/panels/engine-room/layout.styles.ts:194-215 |
| The GSAP hook + the canvas that read these now-static recipes and drive the motion. | "export function useEngineTimeline", "export function EnclosureCanvas" | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:42-42; dashboard/src/panels/engine-room/useEngineTimeline.ts:168-168 |

## 260727-CHATS-IM-L2 Current Delta

`fxOverlaySvg` positions a pointer-transparent sibling over the full structural scene at the same
size and view box. It introduces no new effect paint recipe; surge, reindex, and attention keep
their established classes.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: re-mapped the engineRoomStyles.ts sidecar to the engine-room/styles.ts barrel and added the L8 Split Layout section; per-domain style sidecars carry the current recipe detail. Verification pinned to the leaf base until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: replaced the `n/a` table rows with
  exact anchors and ranges, and converted the history projection-py citations; exact non-fixing
  check returns zero findings.

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the two
  `observer/projection.py` citations — the reference row and the restatement in the 10:44 entry
  below. `L752-L771` → `L762-L781`; read there: `class EngineProcessEdge` cit:(["class EngineProcessEdge"], mcp/src/agents_remember/observer/projection.py:785-785),
  `model_config = ConfigDict(extra="forbid")` cit:([`model_config`], mcp/src/agents_remember/observer/projection.py:777-777), the nine-state comment (L778) above
  the nine-state comment above `state: str`, and the last field `detail` cit:(["class EngineProcessEdge"], mcp/src/agents_remember/observer/projection.py:785-785). No body claim changed.

- 2026-08-01T10:44+02:00 — 260731-EFA-L4 curator: corrected the `refusedConduit` commentary. Polarity is
  no longer "read off the projection (`edge.state` failed→red / stale→amber, **or `edge.refusedPolarity`**)"
  — the second source is gone and the field never existed on the server model (`EngineProcessEdge`,
  `extra="forbid"`, `observer/projection.py` L762-L781). Polarity is derived from `edge.state` alone by
  `EnclosureCanvas::refusedPolarityOf`. Also retitled the amber case: the T9C lane is CGC-seed-**stale**,
  the reducer's actual reroute state, not "seed-refused"; "refused" now names only the beat
  (`data-fx='refuse'`, the `refusedConduit` recipe). The recipe itself is unchanged — the diff touched
  only its comment — so this is a body correction, not a style change. Repaired seven citations that had
  drifted wholesale: `sceneSvg` L595-L605 → L603-L613, `engineCharge` L663-L695 → L704-L749,
  `worktreeWire` L732-L743 → L782-L791, `warpSurge` L786-L795 → L838-L844,
  `attnBadge`/`stopBar`/`dissolveShell` L931-L967 → L1069-L1120, `closeoutTrainLabel`/`cleanupRecord`
  L1001-L1028 → L1121-L1150, and the state-axis row L74-L260 → the five `pulse` sites plus `healthDot`.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: added `fxOverlaySvg`, the
  pointer-transparent sibling layer aligned to the structural 1200x660 scene. Existing effect
  recipes remain the paint authority. Verification metadata remains pinned until closeout.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: extended Engine Room fact-state styling for visibly distinct stale landing observations.

- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: added `missing` runtime variants for the engine gauge outer, charge, and petals so missing provider slots are visible but not confused with nominal or indexing engines. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T09:53+02:00 - Body review for closeout: documented the slice-16 `stackList`
  intrinsic-height behavior in Code Commentary so the existing style change is not represented as a
  history-only onboarding refresh.
- 2026-06-24T07:44+02:00 — fixed the Engine Room left enclosure stack sizing: `stackList` now sets
  `alignContent: start` and `alignItems: start` so grid rows keep their intrinsic card height when the
  left panel has extra vertical room. A single enclosure entry no longer stretches to fill the whole panel,
  while the existing vertical-scroll and ellipsis behavior remains intact.
- 2026-06-22T11:00+02:00 — slice 05o remaining failure-mode primitives: added three more spec-driven atoms for the
  modes the earlier 05o passes left open. **`refusedConduit`** — the shared refused-conduit flash (T9B / T9C /
  T14C): a `cva` keyed on a `polarity` variant (`red` = fault/conflict — the T9B GrepAI seed fault + the T14C
  integration conflict; `amber` = reroute/fallback — the T9C CGC-seed-refused → reindex lane), each a matching
  `stroke` + 4px `drop-shadow` glow over a `base` resting at `opacity:0` (a one-shot flash with no settled
  state); GSAP (`data-fx='refuse'`, `repeat:0`) owns the sweep+fade, polarity read off the projection
  (`edge.state`/`edge.refusedPolarity`), never a class alone. **`engineDropout`** — a static alarm-toned dashed
  halo (`stroke: alarm`, `5 5`, `opacity:0.5`, 4px alarm glow) marking an UNLIT worktree engine slot as HELD
  for T7B (the provider-plan block), distinct from the build-up's not-yet-present engine; no animation. And the
  **moved-indicator** trio `movedBadge` / `movedTriangle` / `movedText` — the soft-cyan ▲ up-triangle pill for
  T12B live-sync announcing the upstream memory ref advanced (`origin/mem-main` moved while the worktree holds
  local commits), mirroring `reasonBadge`/`reasonDot`/`reasonText` geometry but in the soft cyan register (a
  sync-CHOICE notification, not the alarm gate that escalates a beat later). Verification metadata pinned until
  closeout stamps the 05o code commit.
- 2026-06-22T10:42+02:00 — slice 05o T1B: added `prunedNode` — the dormant/desaturated treatment for the stale
  code base node (the spec §3 pruned/retired register: `dormant` stroke + dark muted fill `oklch(0.18 0.02
  25)` + dashed `3 3` at `0.8`, projection-driven onto the stale base node, static; distinct from
  `planned`/`missing`) — and the FLEETING-block box trio `fleetingBox` / `fleetingBoxTitle` /
  `fleetingBoxReason` (the big red provisional enclosure, podstage `.fbox`, REPLACING the old HTML fleeting
  banner + the dashed-amber `enclosureBorder` for a born-blocked stale-base/pre-contract enclosure). The box
  fill was tuned to `opacity 0.82` plus a soft alarm `drop-shadow` glow (brighter than the prototype's `.55`)
  so it reads as a clear red panel over the dashboard's blueprint backdrop video. The `scanRing` +
  `ghostedLane` atoms were documented in the prior 05o T3B entry. Verification metadata pinned until closeout
  stamps the 05o code commit.
- 2026-06-22T00:29+02:00 — slice 05o T3B: added two failure-mode primitive atoms backing the engine-room
  visual-language spec §10. **`scanRing`** — the cyan pre-block verify sweep (`fill:none` / cyan `stroke` 2px
  / 4px cyan `drop-shadow` / `opacity:0` at rest), transient like `flowPacket`/`warpSurge`; GSAP
  `data-fx='scan'` drives the r/opacity expand-fade and the `<circle>` is rendered only while `animate`.
  **`ghostedLane`** — `opacity:0.32` + `filter:grayscale(0.45)`, a static `css` applied projection-driven to
  the inner conduit `<path>` of a gated memory lane (real-but-held, distinct from `planned`); applied to the
  inner `<path>` not the Motion group so it never shadows Motion's group opacity. Same slice — an **engine-gauge
  de-glow + gold petals** pass (developer call, spec §6 updated first): `engineGaugeOut` dropped its base
  `drop-shadow(amber)` (the gold bezel is now FLAT; `down`/fault keeps its red bezel + red glow, and the
  now-redundant `filter:"none"` on `configured`/`unknown` was removed), and `enginePetal` became **constant
  gold** (amber `stroke` moved to `base`; the per-state variants carry only `opacity`) so the petals are
  structural line-art like `engineSpine` rather than runtime-coloured. Verification metadata pinned until
  closeout stamps the 05o code commit.
- 2026-06-21T23:35+02:00 — slice 5o glow pass + legibility/overlay fixes. `engineGaugeOut` reworked to a **constant
  GOLD bezel** (base `stroke: amber` / `strokeWidth: 2` / `drop-shadow(amber)`; the body charge + petals carry
  runtime state, not the frame) — `nominal`/`indexing` now empty variants, `configured` dims it (`opacity 0.5`,
  `filter: none`), `down` is the lone exception that re-colours the frame red (`stroke: alarm` + alarm glow).
  Added state-coloured `drop-shadow` glows to `engineCharge` (mint/cyan/alarm; `configured`/`unknown`
  glow-less), `warpCouplerBar` (2px amber), `flowConduit running` (3px cyan; settled/planned lanes stay
  glow-less), `flowPacket` (5px cyan), and `gateBar` (7px alarm). `closeoutTrainLabel` re-toned for legibility on
  the textured backdrop — `muted` 9px → `ink` 10px (letterSpacing 0.08em → 0.06em), it being a bare caption with
  no chip plate. Also captured the **5k F6** `cleanupRecord` change (absolute overlay over the canvas top —
  `position: absolute`/`top/left/right: 0`/`zIndex: 3`/`backgroundColor: bgPanel` — so the banner no longer
  pushes the canvas down). The fault motion is now the gentle ~1.7s breathe (paired note in `useEngineTimeline`),
  not the old ≤3/s flicker. Verification metadata pinned until closeout stamps the 5o commit.
- 2026-06-21T09:57+02:00 — slice 05n: `flowConduit` `running` dropped `strokeDasharray:"100 100"` → solid cyan
  (GSAP DrawSVG now owns the draw-on dasharray/offset, and `pathLength` was removed from the paths, so a CSS
  dash + pathLength normalization would fight it); `planned` dash re-tuned `"3 5"` → `"9 7"` (real units, since
  pathLength no longer normalizes to 100); `flowPacket` comment updated — the dot now rides its conduit via GSAP
  MotionPath off `data-path` (no CSS `offset-path`). Verified on the bench (running solid, planned dashed `9 7`).
  Verification metadata pinned until closeout stamps the 05n commit.
- 2026-06-21T02:27+02:00 — slice 05k: stripped the interim CSS motion to reach the `05f` §8 end state
  (GSAP + Motion, CSS static). Removed the `sceneSvg` global transition, the `landingEnter` atom, the
  `closeoutBeatG` (`closeoutSweep`) atom, and `warpCouplerG`; dropped the `animation`s on `engineGaugeOut
  down` (pulse), `engineReindexCharge` (chargeSweep), `attnBadge` (attnBreath), `stopBar` (stopFlash), and
  the `dir` `cva` on `warpSurge` (warpSurgeUp/Down) → plain `css`; reverted `engineCharge` to fill-only
  (Motion owns the scaleY/opacity); removed the `opacity` from `enclosureBorder` + the `opacity`/`filter`/
  `transition` from `dissolveShell` (Motion owns them); dropped the `transition` from `remoteChip`/`prBadge`/
  `ledgerButton`. **ADDED `worktreeWire`** — deliberately carries no `opacity` so Motion owns the wire's
  opacity (a className opacity would shadow Motion's animated value under `initial=false`). Verification
  metadata pinned until closeout stamps the 05k code commit.
- 2026-06-19T23:58+02:00 — slice 5i: added the build-up/tear-down motion substrate — `sceneSvg` gained a
  global `transition` (stroke-dashoffset excluded), a new `landingEnter` atom (`landingIn` keyframe in
  `index.css`); reworked `engineCharge` from the `chargeSweep` keyframe to a `scaleY`-level boot-fill (drained
  → charged, eased by the sceneSvg transition); and dropped `flowConduit running`'s `conduitDraw` animation
  (GSAP now owns the draw-on). The `sceneSvg` transition + `landingIn` keyframe are CSS motion slice 05k
  removes per `05f` §8. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T15:00+02:00 — slice 5h H3 readability + connectors (feedback): bumped the chip type to branch-node-peer sizes (`remoteChipLabel` 15px, `remoteChipState`/`prBadgeSub` 12px, `prBadgeLabel` 14px — the first cut at 9–10.5px was unreadable at the 0.76× canvas scale) and added the wiring recipes `remoteStripHeader` (centred band label), `remoteConnector` (solid amber code chain), `remoteConnectorCarry` (dashed carryover handoff). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T13:57+02:00 — slice 5h H3: added the remote/PR strip recipes — `remoteChip`/`remoteChipLabel`/`remoteChipState` (`cva` on `tone` planned/live/done) and `prBadge`/`prBadgeLabel` (`cva` on `state` open/merged) — for the upstream landing strip beyond the official line (T15 code PR+push, T16 carryover). Only motion is the gated fill/stroke transition (frozen under data-effects=off); the colour-as-state honesty law holds (planned never shown live). Verification metadata pinned until closeout stamps the 5h H3 code commit.
- 2026-06-18T21:48+02:00 — slice 5h Tier 2 (frame extend, feedback): `ledgerScroll` became a `cva` keyed on `expanded` — collapsed caps at a compact `13rem`, expanded extends the frame to `min(72vh, 46rem)` so the popover grows to the full window (inner scroll only on overflow). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2: added the 6-column row recipes `ledgerDate` / `ledgerMsg` (ellipsis truncation) / `ledgerHashCode` / `ledgerHashMem` (mono, centre-meeting) / `ledgerSeam`, and widened `ledgerCard` `maxWidth` to `min(92vw, 46rem)`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: added the coupler-popover recipes — `ledgerButton`/`ledgerButtonLabel` (the SVG label-as-button trigger), `ledgerCard`/`ledgerCardHead`/`ledgerTable`/`ledgerRowCss` (popover content + highlighted row), `ledgerScroll` (expanded-rows scroll), `ledgerShowMore` (the expand control), `ledgerMore` (the file footer). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:50+02:00 — slice 5h cleanup pass (feedback): `backdropVideo` gained a centre radial vignette (`maskImage`/`WebkitMaskImage`) scoped to the `<video>` so its faded edges fall back to the dark stage (the SVG scene above is untouched). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T13:01+02:00 — slice 5h coupler fix: added `warpLinkGlyph` (the drawn chain-link icon) + `warpSurge` (`cva` dir up/down — the warp-core surge bands) for the ledger coupler. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T11:55+02:00 — slice 5h H2: added the closeout-train recipes `closeoutBeat`/`closeoutBeatG`/`closeoutBeatLabel`/`closeoutRail`/`closeoutTrainLabel` (the T13 derived closeout-order strip; mint = settled/done, `closeoutBeatG` runs the `closeoutSweep` fill). Verification metadata pinned until closeout stamps the 5h H2 code commit.
- 2026-06-17T22:45+02:00 — 5g G6 + engine-room visual-parity pass: added the atmospheric backdrop atoms
  (`backdrop`/`backdropVideo`/`stageContent` — the effects-gated blueprint-boomerang `<video>` layer) and the
  decal atoms `engineSpine` + `enginePetal` (runtime-coloured), `officialWire`, `canopyStroke` (HUD canopy),
  and `laneFlag`/`laneFlagText` (lane-annotation plates). `diagPanel` is now `flex: 1` (+ `alignContent: start`) so the right zone's diagnostics box stretches to the column floor while the boot timeline stays fixed. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-17T16:15+02:00 — slice 5g G5 + engine palette + side-panel fix: the engine recipes
  (`engineGaugeOut`/`engineCharge`/`engineSilhouette`) now read **green** (`mint`) for an active `nominal`
  engine and empty/`dormant` for `configured`/`unknown` (active=green · off=empty · boot=cyan · fault=red ·
  reindex=amber via the new `engineReindexOut`); added the G5 overlay atoms `stopBar`/`stopText` (t14c
  terminal STOP) + `dissolveShell`/`abandonRecord` (t18 abandon); the left rail now scrolls vertically only
  (`stackList` `overflowX: hidden` + `minWidth: 0`, threaded down `stackItem`/`stackItemHead`) with a new
  `stackRepo` line. Verification metadata pinned until closeout stamps the G5 code commit.
- 2026-06-17T15:00+02:00 — slice 5g G4: `engineGaugeOut` `down` now flickers (`pulse` — the isolated engine fault,
  distinct from the steady gate); added `engineReindexCharge` (amber center-out reindex pulse, t9c
  seedFallback); `phaseChip` gained `whiteSpace: nowrap` (stack-item head fix). Verification metadata pinned
  until closeout stamps the G4 code commit.
- 2026-06-17T14:00+02:00 — slice 5g G3: added the failure-overlay recipes — `gateBar` (steady red lane gate),
  `attnBadge`/`attnText` (breathing attention parity), `reasonBadge`/`reasonDot`/`reasonText` (local reason
  pill), `svgChip`/`svgChipText` (recovery chips). Verification metadata pinned until closeout stamps the G3
  code commit.
- 2026-06-17T13:30+02:00 — slice 5g G2: gave the bird's-eye recipes their boot motion — `engineCharge` center-out
  `chargeSweep` (transform-box: fill-box), `flowConduit` running draw-on (`conduitDraw`), conduit colour
  fidelity (`complete` → faint amber, not mint), and the new `flowPacket` travelling-dot atom. Verification
  metadata pinned until closeout stamps the G2 code commit.
- 2026-06-17T12:47+02:00 — slice 5g G1: added the pod-stage bird's-eye recipes (`sceneSvg`, `worldLabel`,
  `enclosureBorder`, `svgNodeBox`/`svgNode*`, `engineGaugeOut`/`engineCharge`/`engineDiv`/`engineGaugeLabel`,
  `warpCoupler*`, `flowConduit`) for the two-world SVG scene `EnclosureCanvas` renders — static (no
  keyframes); the draw-on / packet / center-out motion lands in G2. Verification metadata pinned until
  closeout stamps the G1 code commit.
- 2026-06-16T03:40+02:00 — slice 5f S4: added the `conduitChevron` flow-packet atom (the travelling energy packet GSAP runs along a running conduit, T8/T9 power-up). Verification metadata pinned until closeout stamps the S4 code commit.
- 2026-06-16T03:05+02:00 — slice 5f S2: added the fleeting-banner atoms (`fleetingBanner`/`fleetingLabel`/
  `fleetingReason`/`fleetingChoices`/`fleetingChoice`) for the provisional pre-contract blocked-start
  enclosure (§2.1). Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-16T02:30+02:00 — slice 5f S1: replaced the 2-col `roomLayout`/`detailColumn` atoms with the §4.2
  full-bleed room layout (`roomShell`/`roomGrid`/`roomStage`/`roomZone`/`roomHeader*`/`roomCaution`).
- 2026-06-16T01:55+02:00 — slice 5f S0: replaced the `conduit` `background`-gradient `<span>` recipe with the
  SVG conduit pair `conduitSvg` + `conduitLine`.
- 2026-06-15T19:35+02:00 — Created for slice 5e: Panda recipes: one per semantic axis (health/factState/conduit/engine); colour carries state (note 08). Verification metadata pinned until closeout stamps the 5e code commit.
