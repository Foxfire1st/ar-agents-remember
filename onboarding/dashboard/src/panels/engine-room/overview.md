# dashboard/src/panels/engine-room/ — Engine Room Process Map Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/engine-room/`              |

## Governing Overview

[panels/ overview](../overview.md)

## 260731-EFA-L8 Change

`engineRoomStyles.ts` (1,287 lines) was ruled a split-by-semantic-axis case (R6:
no exemption list) and divided into `layout.styles.ts`, `stage.styles.ts`,
`ledger.styles.ts`, `flow.styles.ts`, `remote.styles.ts`, and `backdrop.styles.ts`,
with `styles.ts` as the re-export barrel. `EnclosureCanvas.tsx` was split into
`geometry.ts`, `scene.ts`, `badges.tsx`, `engines.tsx`, `ledger.tsx`, `conduits.tsx`,
`remote.tsx`, and `sceneLayers.tsx`. `fixtures.ts` was trimmed to 1,197 physical
lines (FL1). The scene model and motion contracts are unchanged.

## Purpose

`engine-room/` is the enclosure-centered, state-backed Engine Room process map (slice 5e). The server
composes the semantics (`analytics.engineProcesses`, one node per enclosure with observed/derived/planned/
missing fact-state honesty); this module joins, lays out, and renders. Slice 5f animates it as a
worktree-lifecycle state machine: **S0** foundations (honest-motion gate, SVG conduits, `worktreeGroup`
keying), **S1** the full-width 3-zone layout (§4.2), **S2** birth motion (conduit draw-on + map enter) and
the **fleeting** (pre-contract blocked-start) rendering (§2.1), and **S3** the fleeting→real promotion
morph (T4: Motion `layout` + the ghost banner's `AnimatePresence` exit) + the blocked-start alarm parity,
and **S4** power-up flow packets (T8/T9: a travelling energy packet along a seeding/cloning conduit).
Slice **5g** reworks the render into the design prototype's bird's-eye: **G1** extracts the static
two-world canvas (`EnclosureCanvas`) — official line ↔ worktree enclosure, podracer engine gauges, warp
coupler, flow conduits — out of the lane-based map; **G2** gives it the boot choreography (center-out engine charge, conduit
draw-on + travelling packet) + conduit colour fidelity. **G3** adds the failure overlays — a steady gate over a blocked lane + a local reason badge, the
alarm-parity attention badge, and recovery chips. **G4** adds the engine fault flicker (an isolated `down`
engine) + the reindex reroute (`seedFallback`, amber — a fallback, not a failure). **G5** adds the
live/teardown states (render-only): **t12b** sync block (a recoverable gate + `worktree_sync`), **t14c**
integration conflict (a **terminal** STOP, no recovery chips), and **t18** abandon (the enclosure dissolves
to a dim record). G5 also reworks the **engine palette to green=active** (`nominal` → `mint`; empty when
off, cyan booting, red fault, amber reindex) and fixes the left rail (vertical-scroll-only, repo off the
chip row). The successful-**landing** choreography (closeout train, PR/push, carryover — needs a
`projection.py` addition) is split to **`05h`**; the coupler surge remains. A **visual-parity pass** then
lands the atmospheric **backdrop** (5g G6: the effects-gated blueprint-boomerang video + the cockpit
Effects/Calm toggle) and restores the prototype's full SVG **decal layer** above it — the canopy HUD frame,
the engine spine + petals, the **left official-line engines** (real `workspaceEngines`) with their conduits
and the official coupler, and the worktree landing-lane annotations — plus the `Panel` `fill` fix that binds
the room to a fixed height (the centre canvas + right panel stop resizing per selection; the side columns
scroll). The full remote-PR strip render lands in **5h H3** (below; the `landing[]` projection
itself landed in 5h H1). Slice **5h** lands the successful-landing arc: H1 added the `landing[]` /
`integrationStrategy` projection + the live `landing.py` probe; **H2** renders the T13 **closeout train**
(the derived closeout-order strip on `closeout-pending`) and the T14/T14b **integration conduit** (straight
`ff-only` vs a `replay` bend around parallel work), plus the official source line advancing to its landing tip. A **coupler-semantics fix** then re-frames the
warp couplers as the **memory.md ledger** link (the `code ⇄ memory` hash pair they map, NOT the task
series contract): a drawn chain-link glyph + the two linked short-hashes as the label + the restored
warp-core surge. A **cleanup pass** then tightens the conduit wiring (chevrons only on a running flow, the
arrowhead landing on the line end rather than overshooting into the engine, the provider conduits into the
box-edge midpoints, and the `sync` lane collinear with `worktree-add` — one centred line) and vignettes the
backdrop video; the dev bench gallery trims its stale tabs (the `engine-boot-*` step-through is component-
test-only, and `engine-empty` is dropped). A **ledger popover** then makes each warp coupler legible: its
label becomes a clickable button opening the **memory.md lookup table** (the `code ⇄ memory` rows, this
enclosure's row highlighted) — default-8, "▾ show N more" → the bounded **25**-row served window; the
popover anchors high in the scene and grows **downward**, extending its frame to the available height
(scroll only if it still overflows), "+N more in memory.md" beyond. The worktree coupler reads `node.ledgerRows`; the official coupler
reads the repo's `LedgerNode.rows` (resolved in `EngineRoom`); the window is read in the observer's I/O
layer (`snapshots`) so the reducer stays pure. **Tier 2** renders each row as **6 columns** —
`date · message · code-hash ⇄ memory-hash · message · date` — with the per-side commit message + committer
date probed best-effort from the local repos in that same I/O layer (absent → the row keeps just its hash,
never faked). The full-history viewer is the post-ship `#88`. **H3** then renders the **remote/PR strip**
beyond the official line — the upstream the official line reports into (`origin/feat → PR → origin/main`,
then `origin/mem-main` after carryover) — from H1's live `landing[]` probe, in the governed
**code-first / memory-after** D3→D4 order: each ref a colour-as-state chip (planned = dashed/muted · live =
amber · landed = mint) plus a distinct **open→merged PR badge**, the chips sized as **branch-node peers**
(readable single label + a terse status word, full detail on hover) and **wired** — solid amber along the
code chain feat→PR→main, dashed for the carryover handoff into origin/mem-main — shown only while an
enclosure is landing and dropping any `missing` (unprobed) ref (honest-motion §4). This closes the
remote-strip deferral noted above. **H4** then renders the **cleanup teardown**: a `cleanup-pending` (landed)
enclosure de-materialises back into the official line — the same `.dissolve` as abandon, but with a
success-toned `CleanupRecord`, the `contract · historical` chip, and a `▸ back into main` seam reading the
`origin-main` tip. A coupled honesty fix retired a real bug: the H2 landing-source flag leaked on completed
enclosures whose source branch was deleted post-merge (state `unknown`) and overflowed — `landingSource` now
drops unresolved (`missing`/`unknown`) refs and `LaneFlag` truncates with the full label on hover. Slice
**5i** then turns the canvas into a **moving build-up / tear-down stage** driven by the dev scenario player
(`dashboard/src/dev/`): `EnclosureCanvas` gains a motion substrate (GSAP `gsap.context` draw-on for the
conduits + the new directional landing flows; Motion `AnimatePresence` enter/exit for the closeout train;
the `sceneSvg` global CSS transition easing the rest frame-to-frame), the **three-tier landing** (the
official line is always `main`; the feat/fix source appears in the gap during landing → `main ◂ feat ◂
worktree`), **build-up materialisation gates** (the enclosure shell + worktree engines + coupler + lane
flags fade in only once their worktree ref/provider materialises; a worktree node `detaching` drifts out at
cleanup), cross-stage provider **clone arcs** (official engine → worktree engine, transient) + the
persistent `worktree-wire`, and a reworked remote/landing **dock** (positioned chips: origin/feat ▸ PR
merge-arrow ▸ origin/main at the top, origin/mem-main mirrored to the bottom, wired by push/pull/carry/
push-mem flows) — superseding the 5h H3 row layout + the `lane-landing-source` flag. The boot fixtures are
renumbered **B0 (main-only) → B5 (nominal)** and the tear-down split into **D4** (`integration-pending`,
intact), **D5** (`engine-cleanup-pending`, de-materialise), **D6** (`engine-retired`, stack removed). The
CSS-driven parts of this (the `sceneSvg` transition + the `landingIn` keyframe) are the correction target of
slice **05k** (CSS → GSAP-timeline + Motion, per `05f` §8); the scenario player + transport live in
`dev/scenarios.ts` / `dev/ScenarioPlayer.tsx` / `dev/Bench.tsx`. Slice **05o** opens the **failure-mode**
choreography (lifting the `podstage.html` non-happy-path scenes the dashboard didn't yet drive, one mode at a
time: doc → renderer primitive → animated player scenario). **Mode 1 (T3B memory/ledger block)** adds two
projection-driven primitives in `engineRoomStyles`/`EnclosureCanvas`/`useEngineTimeline` — the **scan ring**
(the cyan pre-block ledger-verify sweep, GSAP `data-fx='scan'`, transient) and the **ghosted lane** (the held
memory conduit dims+desaturates while the code lane stays solid) — plus two `boot-demo` block fixtures and the
`dev/` **`memory-block`** player arc (verify → block → reconcile → provider clone → nominal, mirroring the
prototype's T3B M0→M7 so the recover boots the engines on-screen). A coupled engine-gauge polish (developer
call, spec §6 first) makes the gold bezel **flat (no glow)** and the petals **constant gold** structural
line-art (state stays on the body fill). docs/design's living spec gained a **§10 Failure modes** section.
**Mode 2 (T1B stale-base block)** then drives the case where the local official base is behind upstream: it
adds the net-new **`prunedNode`** primitive (the disposed/stale code base node reads **dormant** — a
desaturated dormant stroke + a dark muted fill, distinct from the dotted `planned`/`missing` not-yet states
and from a live amber box; projection-driven on the stale base node, static; mirrors the spec §3
`.node.pruned`), a **stale-base player scenario** + two `boot-demo` block fixtures, and a **§10 Mode-2 spec
note**. Riding alongside it, a **cross-mode indicator anchoring / z-order / transition pass** (it also covers
T3B): the pre-block **verify scan** and the **block gate + reason badge** now anchor ON the checked
repository **node rectangle** (not the connector lane) and render in the **topmost overlay layer** so they sit
clear of the scene; the fleeting born-blocked block leaves its HTML banner for a big red canvas
**`fleetingBox`** `FleetingEnclosure` (the prototype's `.fbox` — a dark-red dashed box over the worktree
footprint that REPLACES the dashed-amber `enclosureBorder`, centring the BLOCKED title + reason with the
recovery chips along the bottom); and every failure overlay now **fades and pops in/out via Motion +
`AnimatePresence`**, gated by `useShouldAnimate` (instant end-state under `effects=off` / reduced-motion).
**05o then completes the failure-mode library** — the engine room now drives **all eight** `podstage.html`
failure modes, the remaining six landing on three new shared primitives: the **refused-conduit flash**
(`refusedConduit` cva red/amber + the `data-fx='refuse'` one-shot GSAP flash, tracing the EXACT lane geometry
via the shared `conduitPathD` so the spark follows the seed/return conduit), **`engineDropout`** (a static
alarm dashed halo over an unlit worktree engine), and **`movedBadge`** (the soft ▲ up-triangle "upstream
moved" notification). The modes: **T7B provider-plan block** — both worktrees on disk but no providers booted
and the runtime setup config missing, so the gate anchors ON the worktree CODE node with `engineDropout`
halos over the dark CGC/GrepAI engines; derived ABOVE `fleeting` (`&& !providerPlanBlocked`) so it never falls
into the big red `FleetingEnclosure` despite sharing the "contract not yet written" fact. **T9B seed-fault** —
a red `refusedConduit` flash on the `failed` clone lane + the GrepAI engine down-flickering. **T9C
reindex-reroute** — an amber `refusedConduit` flash on the `stale` seed lane + reindex (soft, a fallback
not a failure); since 260731-EFA-L4 both polarities are DERIVED from the served `edge.state` rather than
read from a field — see "Derived Refused-Conduit Polarity" below. **T12B
live-sync** — the soft `MovedBadge` shows first (running, `memMoved`), then the memory ledger-map lane gates +
ghosts (`memSyncMoved`) while the CODE lane keeps advancing. **T14C integration-conflict** — a red
`refusedConduit` flash escalating to the terminal `TerminalStop` (all-or-nothing, no recovery chips). **T18
abandon** — the enclosure dissolves to a dim record. All indicators stay **node-anchored** in the topmost
overlay and enter/exit via the shared `alertProps` Motion transitions. `docs/design`'s living spec §10
Failure modes is now complete; detail per primitive lives in the per-file sidecars — read the source under the
route before editing.

## Route Model

- `buildEngineRoomModel.ts` — pure seam: collections → `EngineRoomModel`; joins lifecycle, exposes
  `gate: lifecycle?.gate`, lifts the workspace stack, exposes `enclosureKey` (= `worktreeGroup`), legacy
  `groupEngines` fallback.
- `engineRoomTypes.ts` — `EngineRoomModel` + `EngineProcessView` (node, lifecycle, `gate`,
  `enclosureKey`).
- `styles.ts` — the re-export barrel over the six semantic-axis style domains (`layout`, `stage`,
  `ledger`, `flow`, `remote`, `backdrop`), so callers keep one import surface; the SVG conduit recipe
  (`conduitSvg`/`conduitLine`) lives in `layout.styles.ts` and the flow atoms, including the
  fleeting-banner ones, in `flow.styles.ts`.
- `useShouldAnimate.ts` — the honest-motion gate; also used by the cockpit rail transition.
- `useEngineTimeline.ts` — the **05k/05n** GSAP motion substrate: one `gsap.context` per enclosure (scoped to
  the `<svg>` root) that draws `[data-draw='on']` lanes with **DrawSVG** (05n — once per lane via a `data-drawn`
  guard, so a beat step never re-sweeps a drawn arc), rides the `[data-fx='packet']` dot along its conduit with
  **MotionPath** (05n — off the element's `data-path`), and builds the repeating fx
  (`[data-fx='fault'|'reindex'|'surge'|'breath'|'stop'|'packet']`, the former CSS keyframes); gated by
  `useShouldAnimate` (no context/ticker under `effects=off`), re-running on the fx signature + `worktreeGroup`.
- `EnclosureProcessMap.tsx` — the pod-stage **shell** (5g G1): a `motion.div` that fades in + `layout`-
  morphs (T4) and carries the `FleetingBanner` (in `AnimatePresence`) for provisional blocked-start nodes,
  delegating the scene to `EnclosureCanvas`; Task 11 threads the projected `GateNode` through it as data.
  Deterministic under `data-effects=off`.
- `EnclosureCanvas.tsx` — the **bird's-eye** scene (5g G1): the live `EngineProcessNode` as the prototype's
  two-world canvas — branch nodes (fact-state), podracer engine gauges (runtime), the warp coupler, and the
  flow conduits (edge state) — plus the visual-parity **decal layer** (canopy HUD, engine spine + petals, the
  left official-line engines from `workspaceEngines` + conduits + official coupler, lane annotations). The
  official/source branch nodes render the projected integration/source branch, not a hardcoded `main`, so a
  master series can show its integration branch while protected targets remain outside the leaf worktree. Since
  **5i** it is a **moving build-up/tear-down stage** (GSAP draw-on + `LandingFlows`, Motion `AnimatePresence`,
  three-tier landing, materialisation gates, clone arcs, the repositioned
  dock), all gated by `useShouldAnimate` / `data-effects=off`. **05k** completed the property-split — the motion
  now runs on the `useEngineTimeline` GSAP hook (draw-ons + fx) + Motion (`motion.*` + `AnimatePresence`), CSS
  static (the `sceneSvg` transition + `landingIn` + the canvas `@keyframes` removed). Task 11 adds
  `data-gate-kind` on the SVG root from the projected `GateNode`; no response UI is rendered inside the canvas.
- `EnclosureStackList.tsx` — React Aria `ListBox` of enclosures (keyed by `worktreeGroup`); its
  `stackList` grid starts content and items at the top so a single enclosure entry keeps card height
  instead of stretching through the whole left panel.
- `BootTimeline.tsx` — the right-panel sequence. During build-up it is the ordered **boot** checklist; during
  the landing/teardown phases (`DISPOSE_PHASES`: closeout/integration/carryover/cleanup-pending + abandoned) it
  switches to a **tear-down dispose** sequence (`teardownSteps` + `disposeFrontier`, driven by the same
  `landing[]` ref progression the canvas flows use) so the panel reads forward instead of reverting boot items
  to "pending" (5k F2/F4; `data-mode` attribute).
- `DiagnosticsPanel.tsx` — facts panel: commit refs + fact-state chips, setup/phase lines, the Missing
  observability notice, source files, and the secondary worktree-gate `GateResponder` when a projected
  closeout/push/integration/cleanup gate is present; otherwise action availability remains display-only
  `Affordance`. During power-down
  (`cleanup-pending`/`abandoned`) it reads **"powering down"** and de-emphasizes the now-stale provider /
  completed-phase lines (mint ✓ → muted ◦) — derived from `phase` on the frontend (5k F3; the pre-05m runtime
  sends no power-down signal).
- `fixtures.ts` — `ENGINE_ROOM_SCENARIOS` (the 5i-renumbered B0→B5 boot build-up; the pre-contract-blocked /
  memory-blocked fleeting scenarios; the 5h `engine-landing-*` arc via `landingRef`; and the 5i tear-down
  beats — `engine-landing-merged` (D4 intact) / `engine-cleanup-pending` (D5 de-materialise) /
  `engine-retired` (D6 stack-removed)); consumed by the dev scenario player + the render tests.
- `buildEngineRoomModel.test.ts` — vitest for the pure builder.
- `useShouldAnimate.test.ts` — vitest pinning the `shouldAnimate()` gate truth table.
- `EnclosureProcessMap.test.tsx` — render test pinning the fleeting banner + the bird's-eye scene (conduits,
  gauges, coupler, branch nodes), motion frozen.

> The parent `EngineRoom.tsx` (in `panels/`) composes these into the §4.2 3-zone room; the cockpit
> rails-hide (§4.1) lives in `cockpit/Cockpit.tsx`.

### 260712-TRH-L7 stale landing rendering

The process map keeps stale landing facts inspectable with explicit stale styling, state text, and age, but excludes stale and missing refs from directional landing motion. This preserves honest visible state without presenting an unavailable remote observation as current.

## Invariants And Boundaries

- **Semantics live on the server** — the client renders `analytics.engineProcesses`, never infers.
- **Honest motion (5f)** — JS GSAP/Motion consult `useShouldAnimate()` and render the After state under
  `data-effects=off` / reduced-motion; GSAP owns orchestrated tweens (conduit draw-on), Motion owns
  enter/exit — never both on the same property/element (§8.1). *(Slice 05k reached that §8 end state: the
  interim 5i CSS — the `sceneSvg` transition, the `landingIn` keyframe, and the nine canvas `@keyframes` — is
  removed; the canvas motion now runs on GSAP timelines (`useEngineTimeline`) + Motion, with CSS static.)*
- **Provisional ≠ fake (§2.1)** — a fleeting (pre-contract blocked-start) node renders in the ghost/alarm
  register stating the block + recovery choice; it is visually distinct from a live enclosure. The
  fleeting→real morph is S3.
- **Stable enclosure identity** — keyed by `worktreeGroup` (`enclosureKey`), not the node `id`.
- **Provider-slot honesty** — expected provider roles remain visible when runtime evidence is absent:
  observed providers render from live provider nodes, configured-only roles render as configured, and
  expected-but-missing CGC/GrepAI roles render in the missing register instead of collapsing the container.
- **Action boundary** — ordinary action availability remains display-only. Task 11's exception is the
  chat-routed `GateResponder`, which injects instructional text into an AR-hosted chat; no clock / no git
  in the browser.
- **Refused-conduit polarity is DERIVED, never carried (260731-EFA-L4).** `EnclosureCanvas::refusedPolarityOf`
  reads `edge.state` alone — `failed` → red fault, `stale` → amber reroute, on seed/integration kinds
  only. There is no `refused` edge state and no `refusedPolarity` field; the conduit stamps no
  `data-refused-polarity` (only the topmost `RefusedConduit` overlay carries `data-polarity`). This is
  presentation derived from a served state, not a semantic the client invents, so it sits inside the
  server-semantics rule rather than against it. `EnclosureProcessMap.test.tsx`'s T9C case is the guard:
  it asserts `data-state="stale"` AND `data-refused-polarity` `toBeNull()` on the conduit. Reintroduce a
  polarity field and that null assertion is what breaks.

## Evidence

### Repo-Internal References

- The server composer of the process nodes the client renders. [1]
- The served `EngineProcessNode` / `Analytics.engineProcesses` contract. [2]
- The honest-motion gate the GSAP/Motion read. [3]
- The cockpit shell that hides the rails for the Engine Room view (§4.1). [4]
- `EngineProcessEdge` (`extra="forbid"`) with the documented `kind` and `state` vocabularies the flash derives from. [5]
- "def _seed_edge_state(" and "_DECISIVE_SETUP_EDGE_STATES: dict[str" — the only producers of a seed lane's state, including the "metrics=_metrics(lifecycles" reroute. [6]
- The client mirror of the edge, which no longer declares a polarity field. [7]

## Current L5I Route State

Engine Room visibility is now an execution boundary, not merely a visual one. Hidden keep-alive
layers pause GSAP/Motion/video work through a shared observer gate; the room also narrows analytics
subscriptions and memoizes its model so unrelated snapshot changes do not rebuild the dense map.
SVG effects use composited transforms with non-scaling stroke protection where a scaled ring stands
in for radius animation.

## 260727-CHATS-IM-L2 Route Impact

The structural scene and repeating effects now occupy sibling SVG roots with one shared view box.
`EnclosureCanvas` remains structural authority; `EngineFxOverlay` owns only surge, reindex, and
attention transforms; `useEngineTimeline` queries both through one timeline. Effects-off behavior
and visual choreography remain unchanged. Further steady-state Hangar/Engine Room CPU work is
developer-deferred and is not a blocker for this leaf.

## Derived Refused-Conduit Polarity (260731-EFA-L4)

The T9B/T9C/T14C refused-conduit flash no longer reads a polarity off the projection. Four files moved
together and the visual result is unchanged; what changed is that the lane can now only be driven by a
payload the server can actually send.

- **The derivation.** `EnclosureCanvas::refusedPolarityOf` keeps its kind guard (`cgc-seed`,
  `grepai-clone`, `integration`, `integration-mem`) and then maps state alone: `failed` → red,
  `stale` → amber, anything else → no flash. The `edge.state === "refused"` arm is gone, and with it
  `EngineProcessEdge.refusedPolarity` from `types/projection.ts`, the `data-refused-polarity` attribute
  from `Conduit`, the `cgcRefused` flag from the fixture `EdgeStates`, and the `refused` term from
  `useEngineTimeline::fxSignature`'s re-arm filter (now `failed`/`stale` only).
- **Why that is a correction, not a loss of coverage.** `observer/projection.py::EngineProcessEdge` is
  `extra="forbid"`, declares no `refusedPolarity`, and its state comment lists
  nominal · running · blocked · failed · stale · skipped · complete · planned · unknown — no `refused`.
  `git log --all -S 'state="refused"'` returns zero commits, so no served payload has ever carried the
  state the removed arm was written for. The fixture that fed it was a body the server would have
  rejected, and the branch it reached was unreachable in production.
- **The T9C scenario now models the reroute the reducer emits.** `engine-cgc-seed-refused` seeds
  `edges({ cgc: "stale", … })`; `reducer.py::_seed_edge_state` returns `stale` verbatim through
  `_DECISIVE_SETUP_EDGE_STATES` when the setup run itself is stale, and the amber is derived from that.
  The scenario ID is deliberately unchanged: **"refused" now names only the visual beat** — the
  `refusedConduit` recipe and the `data-fx='refuse'` one-shot — never an edge state. Its `currentPhase`
  and `summary` copy were retimed to match, saying the seed went stale and is rerouting rather than that
  it was refused.
- **The `integration` / `integration-mem` arms are kept on purpose and are dead against today's
  reducer.** Both edge builders (`_process_edges`, `_start_process_node`) emit only `worktree-add`,
  `cgc-seed`, `ledger-map`, `grepai-clone` and `sync`, so no served node reaches either arm. They stay
  because `integration` IS in `EngineProcessEdge`'s own documented `kind` vocabulary and the whole
  integration lane — geometry, the T14C conflict scenario, the `replay` strategy bend — is
  fixture-authored and test-covered. That is the reason; it is **not** forward-compatibility, and
  nothing is scheduled to start emitting them. `integration-mem` is not itself in the documented list
  and lives or dies with `integration`. Delete the lane and its coverage together, or not at all.

## L23 Source-Lineage Diagnostic

Engine Room now receives a strict source-lineage projection on each applicable
process node. Diagnostics renders the aggregate state/summary, and the route's
test seeds a blocked projection to prove visibility before an agent consumes
stale enclosure context.
