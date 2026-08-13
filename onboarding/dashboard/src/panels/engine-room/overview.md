# dashboard/src/panels/engine-room/ — Engine Room Process Map Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/engine-room/`              |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-08-01T15:10+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`       |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `../overview.md`                                 |

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
- `engineRoomStyles.ts` — Panda recipes: the semantic-axis `cva`s, the SVG conduit recipe
  (`conduitSvg`/`conduitLine`), the §4.2 full-bleed room layout atoms, and the §2.1 fleeting-banner atoms.
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The server composer of the process nodes the client renders. | "def build_analytics("; "def _start_process_node(entry: dict[str"; "def _process_edges(" | mcp/src/agents_remember/observer/reducer_impl/_metrics.py:129-129; mcp/src/agents_remember/observer/reducer_impl/_processes.py:124-124; mcp/src/agents_remember/observer/reducer_impl/_processes.py:543-543 |
| The served `EngineProcessNode` / `Analytics.engineProcesses` contract. | `EngineProcessNode` | mcp/src/agents_remember/observer/projection.py:832-900 |
| The honest-motion gate the GSAP/Motion read. | `useShouldAnimate` | dashboard/src/panels/engine-room/useShouldAnimate.ts:19-37 |
| The cockpit shell that hides the rails for the Engine Room view (§4.1). | "const fullBleed =" | dashboard/src/cockpit/Cockpit.tsx:446-446 |
| `EngineProcessEdge` (`extra="forbid"`) with the documented `kind` and `state` vocabularies the flash derives from. | `EngineProcessEdge` | mcp/src/agents_remember/observer/projection.py:785-804 |
| "def _seed_edge_state(" and "_DECISIVE_SETUP_EDGE_STATES: dict[str" — the only producers of a seed lane's state, including the "metrics=_metrics(lifecycles" reroute. | "def _seed_edge_state("; "_DECISIVE_SETUP_EDGE_STATES: dict[str" | mcp/src/agents_remember/observer/reducer_impl/_processes.py:631-631; mcp/src/agents_remember/observer/reducer_impl/_processes.py:638-638; mcp/src/agents_remember/observer/reducer.py:73-73 |
| The client mirror of the edge, which no longer declares a polarity field. | `EngineProcessEdge` | dashboard/src/types/projection.ts:162-170 |

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

## Update History
- 2026-08-12T20:20+02:00 — L23 curator: documented lineage projection and blocked-state rendering in Engine Room; verification remains closeout-owned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: added the L8 Change section (style-domain split, canvas siblings, fixtures trim). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired and normalized the scoped engine-room citation claims; final exact frozen-snapshot check is clean.
- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the
  `observer/projection.py` citations in the 12:50 entry below. The range `L752-L771` → `L762-L781`
  (`class EngineProcessEdge` L762, `extra="forbid"` L770, last field `detail` L781), and the two
  inner line references the same restructure moved: the nine-state comment L768 → **L778** and
  `state: str` L769 → **L779**. Those two were missed by the derived correction list and are
  recorded here so the next reader does not re-derive them. No body claim changed.

- 2026-08-01T12:50+02:00 — 260731-EFA-L4 route impact (wire contracts and typed vocabularies): added
  the "Derived Refused-Conduit Polarity" section and the matching invariant, and corrected the Purpose
  paragraph's two stale mode descriptions — T9B's "refused clone lane" is the `failed` lane and T9C's
  amber flash rides the `stale` seed lane. Evidence for the whole change: `EngineProcessEdge`
  cit:([`EngineProcessEdge`], mcp/src/agents_remember/observer/projection.py:785-804) is `extra="forbid"`, declares no `refusedPolarity`, and its state
  comment (L778, above `state: str` at L779) lists
  nominal/running/blocked/failed/stale/skipped/complete/planned/unknown with no
  `refused`; `git log --all -S 'state="refused"'` returns 0 commits in all of history; and
  cit:(["_DECISIVE_SETUP_EDGE_STATES: dict[str", "def _seed_edge_state("], mcp/src/agents_remember/observer/reducer_impl/_processes.py:631-631; mcp/src/agents_remember/observer/reducer_impl/_processes.py:638-638) is what makes `stale` a state the helper really returns. Recorded that the scenario ID
  `engine-cgc-seed-refused` is unchanged on purpose because "refused" now names the beat, not a state,
  and that `EnclosureProcessMap.test.tsx`'s `data-refused-polarity` `toBeNull()` is the guard against
  reintroducing the field. Kept the `integration`/`integration-mem` arms documented with their ACTUAL
  justification (`integration` is in the model's own `kind` list at L765-L767 and the lane is
  fixture-authored/test-covered) rather than as forward-compatibility — I checked both reducer edge
  builders, cit:(["def _process_edges(", "def _start_process_node(entry: dict[str"], mcp/src/agents_remember/observer/reducer_impl/_processes.py:124-124; mcp/src/agents_remember/observer/reducer_impl/_processes.py:543-543), and neither emits
  either kind. Added three two-cell `Repo-Internal References` rows in the existing two-column shape.
  Evidence: the engine-room suites run green. Verification metadata remains pinned until closeout.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: repeating surge, reindex,
  and attention transforms now render in `EngineFxOverlay`, a sparse sibling SVG aligned to the
  unchanged structural canvas. The shared timeline queries both roots and preserves the original
  selectors, geometry, paint, and choreography. This is the accepted visual/performance boundary;
  further steady-state Hangar/Engine Room CPU work is developer-deferred. Verification metadata
  remains pinned until closeout.

- 2026-07-24T13:17:17Z — Curator: documented the hidden-room CPU contract, narrowed subscriptions,
  and transform-safe SVG effects. Verification metadata remains pre-commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: Engine Room now types and visibly renders stale landing facts, exposes their age, and suppresses stale/missing landing motion while retaining the node.

- 2026-06-28T03:21+02:00 — Task 31 route impact: `BootTimeline`, `EnclosureCanvas`, and the shared
  recipes now render `ProviderBootNode.runtimeState` / `factState` values of `missing`, so an expected
  CGC/GrepAI role can stay visible as missing when no provider row is observed. The route still renders
  server-composed `analytics.engineProcesses`; it does not infer provider existence in the browser.
  Verification metadata pinned until closeout stamps the task-31 code commit.
- 2026-06-24T09:53+02:00 - Slice 16: the Engine Room left stack keeps entries at intrinsic height even
  when only one enclosure is present; `engineRoomStyles.stackList` starts grid content/items at the top
  while `EnclosureStackList` remains the React Aria listbox keyed by `worktreeGroup`.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the Engine Room route now treats the official line as the projected integration/source branch, updates coupler wording from task `contract.md` to series contract, and keeps stable enclosure identity on `worktreeGroup` while leaf ids are projected separately. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T13:45+02:00 — Task 11: engine-room model/view now carries projected `GateNode`; the process
  map/canvas receive it as identity data (`data-gate-kind`), and diagnostics renders the compact shared
  `GateResponder` for worktree-bound gates while non-gate actions stay display-only. Verification metadata
  pinned until closeout stamps the task-11 code commit.
- 2026-06-22T11:00 — slice 05o **completed the failure-mode library**: the engine room now drives **all eight**
  `podstage.html` failure modes, the remaining six landing on three new shared primitives — the
  **refused-conduit flash** (`refusedConduit` cva red/amber + the `data-fx='refuse'` one-shot, tracing the
  refused seed/return lane via the shared `conduitPathD`), **`engineDropout`** (the static alarm dashed halo
  over an unlit worktree engine), and **`movedBadge`** (the soft ▲ "upstream moved" notification). **T7B
  provider-plan block** — a node-anchored gate on the worktree CODE node + `engineDropout` halos over the
  unlit engines; derived ABOVE `fleeting` (`&& !providerPlanBlocked`) so it stays OUT of the big red
  `FleetingEnclosure` box. **T9B seed-fault** — a red refused-conduit flash + the GrepAI engine
  down-flicker. **T9C reindex-reroute** — an amber refused flash + reindex (soft). **T12B live-sync** — a soft
  `MovedBadge` (▲) first, then the memory ledger-map lane gates + ghosts while the code lane keeps running.
  **T14C integration-conflict** — a red refused flash escalating to the terminal `TerminalStop` (no recovery
  chips). **T18 abandon** — the enclosure dissolves to a dim record. All indicators stay node-anchored in the
  topmost overlay with the shared `alertProps` Motion enter/exit transitions; `docs/design`'s §10 Failure
  modes is now complete. Detail in the per-file sidecars. Verification metadata pinned until closeout stamps
  the 05o code commit.
- 2026-06-22T10:45 — slice 05o **Mode 2 (T1B stale-base block)** + a cross-mode indicator anchoring/z-order/
  transition pass. Mode 2 lands the net-new **`prunedNode`** primitive (the disposed/stale code base reads
  **dormant** — desaturated dormant stroke + dark muted fill, distinct from `planned`/`missing` dotted and
  from a live amber box; projection-driven, static; mirrors the spec §3 `.node.pruned`), the **stale-base
  player scenario** + two `boot-demo` boot fixtures, and the **§10 Mode-2 spec note**. The cross-mode pass
  (applies to T3B too): the **verify scan** and the **block gate/reason** now anchor ON the checked repository
  **node rectangle** (not the connector lane) and render in the **topmost overlay layer**; the fleeting
  born-blocked block moved from an HTML banner into a big red canvas **`fleetingBox`** `FleetingEnclosure`
  (the prototype's `.fbox` — dark-red dashed box over the worktree footprint, REPLACING the dashed-amber
  `enclosureBorder`, with the BLOCKED title/reason + recovery chips); and every failure overlay now **fades
  and pops in/out via Motion + `AnimatePresence`** (gated by `useShouldAnimate`). Detail in the per-file
  sidecars. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T00:29 — slice 05o T3B (engine-room failure modes, mode 1): added the **scan ring**
  (`scanRing` + GSAP `data-fx='scan'`) and **ghosted lane** (`ghostedLane`, projection-driven on the held
  memory conduit) primitives across `engineRoomStyles`/`useEngineTimeline`/`EnclosureCanvas`; two `boot-demo`
  block fixtures (`engine-boot-memory-verify`/`-blocked`) + the `dev/` **`memory-block`** player arc (verify →
  block → reconcile → **provider clone (copy-arrows)** → nominal, mirroring `podstage.html` T3B M0→M7); +
  render/scenario tests. Coupled **engine-gauge polish** (spec §6 first): `engineGaugeOut` flat gold bezel (no
  glow; `down`/fault keeps the red bezel + glow) and `enginePetal` constant gold. The `docs/design/`
  living spec gained a §10 Failure modes section. Detail in the per-file sidecars. Verification metadata pinned
  until closeout stamps the 05o code commit.
- 2026-06-21T23:35+02:00 — slice 05k tear-down + design-review refinements. **Tear-down sequence** (5k F2/F4):
  `BootTimeline` switches to a dispose checklist (`teardownSteps`/`disposeFrontier`) during the landing/teardown
  phases; **power-down diagnostics** (5k F3): `DiagnosticsPanel` reads "powering down" + de-emphasizes stale
  lines at cleanup/abandon; **active-vs-settled flow language** (`engineRoomStyles`/`useEngineTimeline`: the
  departing clone-arc/lane retract is stroke-locked cyan before erasing). Design-review refinements on
  `EnclosureCanvas`: the **second-scenario-loop engine-fill bug** fixed (the charge rect's fill is now owned by
  the `engineCharge` class, the powerup is a Motion opacity pulse — no stuck CSS `forwards` fill-lock); the
  **three middle columns re-spaced + aligned** via `COL_MAIN_CX`/`COL_FEAT_CX`/`COL_WT_CX` centre constants (all
  node/coupler/chip/conduit/wire/flow/enclosure coords derived from them; remote chips centred on their columns →
  vertical landing flows); the **closeout train** made legible (`ink` 10px) + relocated to a bottom breadcrumb;
  and a **memory integration arrow** (`integration-mem` edge, memory worktree → feat memory, mirroring code).
  `index.css` dropped the `@keyframes powerup` (now a Motion pulse). Also: **`docs/design/` brought into
  onboarding scope** (a `docs/design`-scoped `pathRules` rule adds `.html`+`.md` there; `sources.md` registers it
  as Domain Documentation) — the engine-room visual-language living spec + the podstage prototype are now
  onboarded under `onboarding/docs/design/engine-room/`. Detail in the per-file sidecars. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-21T09:57+02:00 — slice 05n: migrated the engine-room draw-on to GSAP **DrawSVGPlugin** and the flow
  packet to **MotionPathPlugin** (replacing the manual `strokeDashoffset` sweep + CSS `offset-path`), fixing two
  CSS→GSAP-port regressions a /design-review surfaced: the draw-on re-swept on every beat step (now one-shot per
  lane via a `data-drawn` guard — **F11**) and the packet dots were dead (the old `attr:{offsetDistance}` tween
  targeted a non-existent SVG attribute — **F12**). Touched `useEngineTimeline.ts` + `EnclosureCanvas.tsx`
  (packet `data-path`/`animate`-gate, `pathLength` removed) + `engineRoomStyles.ts` (`flowConduit` running solid,
  planned dash `9 7`) + a jsdom SVG-geometry stub in `test/setup.ts`. Property-split holds (GSAP: stroke reveal +
  packet transform; Motion: node opacity/transform). Verification metadata pinned until closeout stamps the 05n commit.
- 2026-06-21T02:26+02:00 — slice 05k: the canvas motion reached the 05f §8 property-split end-state — removed
  the interim 5i CSS (the `sceneSvg` transition + the `landingIn` keyframe + the nine canvas `@keyframes`) and
  moved it onto a NEW `useEngineTimeline.ts` GSAP hook (`strokeDashoffset` draw-ons by `data-draw` + the
  repeating fx by `data-fx`) + Motion (`motion.*` opacity/transform + `AnimatePresence` enter/exit); CSS is
  static (the app-wide `pulse`/`flicker` kept, plus the `effects=off` freeze). `engineRoomStyles` added the
  `worktreeWire` recipe carrying **no** opacity so Motion owns the wire (fixes the dangling worktree-wire).
  Gated by `useShouldAnimate` → instant end-state under `effects=off`/reduced-motion, no GSAP ticker (the 71
  vitest tests stay green). **Known follow-up:** at D5 (`cleanup-pending`) the landing-tier — the feat ▸ source
  tier, the `worktree-add`/`ledger-map` conduits, and the carry/push-mem flows — does not yet retract because
  `cleanup-pending ∈ LANDING_PHASES` keeps `showLanding` true (confirmed in real Chrome: feat ~0.98, conduits
  0.6, flows ~0.9 at settled D5); tracked for a `!retiring` gate (feat + flows, frontend) plus a conduit
  reducer determination (pending live-data validation). Detail in the `EnclosureCanvas.tsx` /
  `engineRoomStyles.ts` / `index.css` / `EnclosureProcessMap.tsx` / `EnclosureProcessMap.test.tsx` /
  `useEngineTimeline.ts` / `fixtures.ts` sidecars + the `dev/` sidecars. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-19T23:58+02:00 — slice 5i: the canvas became a moving build-up/tear-down stage driven by the dev
  scenario player — GSAP draw-on (conduits + `LandingFlows`) + Motion `AnimatePresence` (closeout train) + the
  `sceneSvg` CSS transition; three-tier landing (`main ◂ feat ◂ worktree`); build-up materialisation gates +
  `detaching` cleanup drift; cross-stage clone arcs + `worktree-wire`; the repositioned remote/landing dock
  (superseding the 5h H3 row + the `lane-landing-source` flag). Fixtures renumbered B0→B5 and the tear-down
  split into D4/D5/D6 (added `engine-retired`). The CSS-driven parts (`sceneSvg` transition + `landingIn`) are
  slice 05k's correction target. Detail in the `EnclosureCanvas.tsx` / `engineRoomStyles.ts` / `fixtures.ts` /
  `EnclosureProcessMap.tsx` / `EnclosureProcessMap.test.tsx` sidecars + the `dev/` sidecars. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-19T15:50+02:00 — slice 5h H4 cleanup teardown + landing-source fix: a `cleanup-pending` enclosure now de-materialises (the `.dissolve` + a success `CleanupRecord` + the historical chip + a `back into main` seam), distinct from abandon. Coupled fix: `landingSource` drops unresolved (`missing`/`unknown`) refs and `LaneFlag` truncates, so a completed enclosure with a deleted source branch no longer leaks a stale overflowing `▸ origin/feat · unknown`. Detail in the `EnclosureProcessMap.tsx` / `EnclosureCanvas.tsx` / `engineRoomStyles.ts` / `fixtures.ts` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T15:00+02:00 — slice 5h H3 readability + connectors (feedback): the remote/PR chips were unreadably small (≈8px at the 0.76× canvas scale) with overflowing two-line state — reworked to branch-node-peer sizing (readable label + terse status word, full detail on hover) and **wired** the strip (solid amber code chain + dashed carryover handoff), centring the band header. Detail in the `EnclosureCanvas.tsx` / `engineRoomStyles.ts` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T13:57+02:00 — slice 5h H3: rendered the **remote/PR strip** on `EnclosureCanvas` — `RemoteStrip`/`RemoteChip`/`PrBadge` over H1's `landing[]`, in the governed code-first/memory-after D3→D4 order (`origin-feat → PR → origin-main → origin-mem-main`); each ref a colour-as-state chip (planned=dashed/muted · live=amber · landed=mint) with an open→merged PR badge, shown only while an enclosure is landing and dropping `missing` probe refs. Added the `remoteChip`/`prBadge` recipes (`engineRoomStyles`) + 4 render cases; closes the remote-strip deferral. Detail in the `EnclosureCanvas.tsx` / `engineRoomStyles.ts` / `EnclosureProcessMap.test.tsx` sidecars. Verification metadata pinned until closeout stamps the 5h H3 code commit.
- 2026-06-19T06:39+02:00 — No route impact: crash fix — the `lane-landing-source` read is now null-safe (`node.landing?.find`) so a projection that omits the slice-5h `landing` field renders the scene with no landing flag instead of crashing; the engine-room route model is unchanged — detail in the `EnclosureCanvas.tsx` + `EnclosureProcessMap.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:27 — No route impact: a dev-bench tab trim (mirroring task 5's `b3f2491`) removed the unused `engine-empty` scenario from `fixtures.ts` (empty `processes`, no consumer — the dev gallery dropped it, the `EnclosureProcessMap` render tests reference only named live scenarios). The engine-room route model + process-map behavior this overview describes are unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:48+02:00 — slice 5h Tier 2 (frame extend + position, feedback): the popover grows **downward**, extending its frame to the available height when expanded (instead of upward into a short scroll box), and anchors high in the scene so it keeps its upper position. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2 (commit messages + date-time): the popover row is now the mirrored 6-column layout (`date · message · code-hash ⇄ memory-hash · message · date`). The per-side commit message + committer date are probed best-effort in the observer I/O layer (one batched `git log` per repo per coupler; absent → hash-only, never faked); `compactDate` string-slices the ISO to `MM-DD HH:mm`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover (both couplers): each coupler label is a clickable button opening the memory.md lookup table (this enclosure's row highlighted; default-8 → "show N more" → bounded-25 scroll → "+N more in memory.md"). Worktree coupler from `EngineProcessNode.ledgerRows`, official coupler from `LedgerNode.rows` (resolved in `EngineRoom`); the window is read in the observer I/O layer so the reducer stays pure. Full-history viewer deferred to `#88` (post-ship). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:50+02:00 — slice 5h cleanup pass (feedback): tightened the `EnclosureCanvas` conduit wiring (chevron `marker-end` only on a running flow + the `er-chev` `refX` tip so the arrowhead lands on the line end, provider conduits box-edge-midpoint → engine corner, the `sync` lane collinear with `worktree-add`, symmetric petals), vignetted the backdrop video (`engineRoomStyles`), trimmed the bench gallery tabs (`engine-boot-*` filtered, `engine-empty` dropped), and added the conduit-wiring-polish render guards. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T13:01+02:00 — slice 5h coupler fix (feedback): the warp couplers now read as the **memory.md ledger** link — `EnclosureCanvas` `WarpCoupler` shows a `code ⇄ memory` hash-pair label (each its own, via `short`) + a drawn `warpLinkGlyph` chain-link + the `warpSurge` warp-core bands (recipes in `engineRoomStyles`, keyframes in `index.css`); dropped the misleading `contract · taskId`. The `ledger ▸ maps merge` flag is left as-is (open question). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T11:55+02:00 — slice 5h H2: rendered the landing arc on `EnclosureCanvas` — a `CloseoutTrain` (T13 derived closeout-order strip on closeout-pending), the `integration` conduit bending for `replay` vs straight `ff-only` (T14/T14b), the `lane-landing-source` official-line tip, the `closeout*` recipes (`engineRoomStyles`) + the `closeoutSweep` keyframe (`index.css`), and the `engine-landing-closeout` fixture. The remote/PR strip + carryover is H3. Verification metadata pinned until closeout stamps the 5h H2 code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1 (data substrate; the render is H2+): `fixtures.ts` gained the `landingRef` helper + the `engine-landing-ffonly` / `engine-landing-merged` scenarios, and `types/projection.ts` mirrored `LandingRefNode` + `EngineProcessNode.landing`/`integrationStrategy` (the server side landed in `observer/` + the new `worktrees/modules/landing.py` probe). Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-17T22:45 — 5g G6 + engine-room visual-parity + fill-height layout: landed the atmospheric backdrop
  (`backdrop`/`backdropVideo`/`stageContent` + the cockpit Effects/Calm toggle) and restored the prototype's
  SVG decal layer in `EnclosureCanvas` — canopy HUD frame, engine spine + petals, the left official-line
  engines (from `model.workspaceEngines`, threaded `EngineRoom` → `EnclosureProcessMap` → `EnclosureCanvas`)
  + conduits + official coupler, and the worktree lane annotations; plus the `Panel fill` variant that binds
  the room to a fixed height (canvas + right panel no longer resize per selection; side columns scroll).
  `REMOTE · ORIGIN` deferred to the live-data extension. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-17T16:15 — slice 5g G5 + engine palette + side-panel fix: the bird's-eye gained the live/teardown
  states (t12b recoverable sync gate, t14c terminal integration STOP with no recovery chips, t18 abandon
  dissolve-to-record) — all render-only against existing projection fields (`phase` + `sync`/`integration`
  edges). Engine gauges now read **green** when active (`nominal` → `mint`; empty off, cyan booting, red
  fault, amber reindex), and the enclosure rail scrolls vertically only with the repo label off the chip
  row. The successful-landing choreography (T13–T17, needs a `projection.py` addition) is split to `05h`.
  Verification metadata pinned until closeout stamps the G5 code commit.
- 2026-06-17T15:00 — slice 5g G4 (Batch B) + UX fixes: the engine **fault flicker** (an isolated `down`
  engine pulses; the steady gate is now blocked-edges-only) + the **reindex reroute** (`seedFallback` → an
  amber center-out pulse on CGC, not red) + a `retryArgs` retry chip. Fixes: branch text truncates with a
  hover `<title>`; the boot/cloning fixtures' provider runtime now matches the running conduit; `phaseChip`
  no longer wraps. Verification metadata pinned until closeout stamps the G4 commit.
- 2026-06-17T14:00 — slice 5g G3: the bird's-eye gained its failure overlays (Batch A) — a steady `Gate`
  over each blocked/failed lane, a local `ReasonBadge` (the node summary), the breathing `Attention` parity,
  and `RecoveryChips` (`nextAction` + enabled actions); a fleeting pre-contract block keeps its
  `FleetingBanner`. blocked = STEADY (the fault flicker is G4). Verification metadata pinned until closeout
  stamps the G3 commit.
- 2026-06-17T13:30 — slice 5g G2: the bird's-eye gained its boot motion — `engineCharge` center-out
  `chargeSweep` (indexing engines), `flowConduit` running draw-on + the `flowPacket` travelling dot, and
  conduit colour fidelity (`complete` → faint amber, not mint); the keyframes live in `index.css`, frozen
  by effects=off. Verification metadata pinned until closeout stamps the G2 commit.
- 2026-06-17T12:47 — slice 5g G1: reworked the render into the prototype's bird's-eye — extracted the static
  two-world canvas (`EnclosureCanvas`: branch nodes, podracer gauges, warp coupler, flow conduits) out of the
  linear-lane `EnclosureProcessMap` (now the promote-in-place shell); added the `engineRoomStyles` scene
  recipes; retargeted `EnclosureProcessMap.test.tsx` to the scene. Static frame — G2 adds the choreography.
  Verification metadata pinned until closeout stamps the G1 commit.
- 2026-06-16T03:40 — slice 5f S4 (power-up T8/T9): `SvgConduit` renders a gated GSAP `conduit-flow` packet that travels along a running (clone/seed) conduit; `engineRoomStyles` gained the `conduitChevron` atom. Engine seeding/fault stay on the `engineSilhouette` indexing/down variants. Verification metadata pinned until closeout stamps the S4 commit.
- 2026-06-16T03:35 — slice 5f S3 (T4 promotion morph + alarm parity): `EnclosureProcessMap` gained a gated `layout` morph and moved the `FleetingBanner` into `AnimatePresence`, so a fleeting node solidifies **in place** into the real enclosure (keyed by `worktreeGroup`, S0); the blocked-start alarm parity flows from S6's reducer `_start_attention` and renders in `AttentionQueue` (new `AttentionQueue.test.tsx` pins it). Verification metadata pinned until closeout stamps the S3 commit.
- 2026-06-16T03:05 — slice 5f S2 (birth motion): `EnclosureProcessMap` became a `motion.div` with a gated
  enter, the `SvgConduit`s draw on via gated GSAP, and a `FleetingBanner` renders provisional pre-contract
  blocked-start nodes (§2.1); `engineRoomStyles` gained the fleeting atoms; added `EnclosureProcessMap.test.tsx`.
  The fleeting→real morph + alarm parity is S3. Verification metadata pinned until closeout stamps the S2 commit.
- 2026-06-16T02:30 — slice 5f S1: the room moved to a full-width §4.2 3-zone layout (the cockpit rails-hide
  lives in `cockpit/`).
- 2026-06-16T01:55 — slice 5f S0: added `useShouldAnimate.ts` (+ test) honest-motion gate; SVG conduits;
  `worktreeGroup` keying.
- 2026-06-15T19:35 — Created for slice 5e: the enclosure-centered Engine Room process-map module
  (pure `buildEngineRoomModel` + Panda/React Aria components + scenario fixtures). Verification metadata pinned until closeout stamps the 5e code commit.
