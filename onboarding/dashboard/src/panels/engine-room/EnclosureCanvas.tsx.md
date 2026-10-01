# dashboard/src/panels/engine-room/EnclosureCanvas.tsx

## Governing Overview

[engine-room overview](overview.md)

## 260731-EFA-L8 Split

This 1,701-line canvas was split by responsibility into the engine-room sibling
modules (`geometry.ts`, `scene.ts`, `badges.tsx`, `engines.tsx`, `ledger.tsx`,
`conduits.tsx`, `remote.tsx`, `sceneLayers.tsx`, and the six style domains). The
canvas keeps the composition and motion wiring (`useEngineTimeline`, Motion,
AnimatePresence); the scene packet now comes from `scene.resolveScene`. Behavior is
unchanged.

## Purpose

The Engine Room pod-stage **bird's-eye** (5g G1): one `EngineProcessNode` rendered as the two-world canvas
from the design prototype (`dashboard/public/_proto/podstage.html`) — official line ↔ worktree enclosure,
podracer engine gauges, the warp coupler, and the flow conduits. G1 is the **static frame** (the nominal
end-state); the boot/failure choreography (draw-on, travelling packets, center-out fill, gates) is G2+.
Task 11 threads the projected `GateNode` into the canvas as identity data (`data-gate-kind` on the SVG)
without adding a response control here; diagnostics owns the secondary Respond UI.

The **visual-parity pass** then restored the prototype's full HUD **decal layer** that sits above the G6
backdrop video: the canopy frame (bevel rim + corner brackets + edge ticks), the engine **spine + petals**,
the **left official-line engines** (driven by the real `workspaceEngines`) with their conduits and the
official code↔memory coupler, and the worktree landing-lane annotations.

## Code Commentary

### Logic

`EnclosureCanvas({ node, gateNode, workspaceEngines, officialLedger })` is the only export — a single `<svg viewBox="0 0 1200 660">`
(`enclosure-canvas`) whose geometry is ported 1:1 from the prototype. The SVG root carries
`data-gate-kind={gateNode?.kind}` and an `aria-label` based on `node.leafId || node.taskName` so tests and later render work can distinguish a projected gate from
edge-derived visual gate bars. It splits `node.providers` into
code/memory and computes `hasMemory` (`memoryMode === "external"` + a `memoryWorktree`). Sub-components:
`BranchNode` (a `<rect>` + text for a `CommitRefNode`, stroke by `factState`), `EngineGauge` (the podracer
column — outer + charge + divisions + the **spine** + six fanned **petals** + label, coloured by the
normalized `runtimeState`), `WarpCoupler` (the contract bar, bound iff external memory), `Conduit` (one
positioned `<path>` per `EngineProcessEdge`, coloured by `conduitState`, routed by `EDGE_GEOM[edge.kind]`),
`CanopyFrame` (the HUD housing — bevel rim + corner brackets + edge ticks), and `LaneFlag` (a toned lane
plate). Two pure normalizers — `conduitState` / `runtimeState` — clamp the wire strings to the recipe
variant unions; `runtimeState` accepts `missing` so expected-but-unobserved provider engines remain visible
as missing rather than falling through to generic unknown. Geometry constants: `POS` (node boxes), `ENGINE` (gauge translates — `cgc`/`grepai` on the
right, `mcgc`/`mgrep` on the **left**), `COUPLER_X` + `OFFICIAL_COUPLER_X`, and `EDGE_GEOM` (per-kind
conduit endpoints anchored to box edges so a line never crosses a box; **5g G5** added the `integration`
return lane; the **column re-space** below adds the `integration-mem` mirror). **Column re-space (06‑21):** the
three middle columns are now anchored on three centre constants — `COL_MAIN_CX = 365` (official line · main),
`COL_FEAT_CX = 595` (feat/source landing tier in the gap), `COL_WT_CX = 835` (worktree code/memory) — evenly
spaced for ~72px edge-to-edge gaps either side of feat, symmetric about the ~600 stage centre. The
three constants derive the middle-column x positions and the related coupler, edge, remote-chip,
wire, flow, and enclosure-border x geometry. Engine pod positions and the scene's many y coordinates
remain fixed values rather than derivatives of those centres. **5g G5** also adds `TerminalStop` (the t14c integration-conflict STOP, drawn instead of a
`Gate` when `phase === "integration-blocked"`, with recovery chips suppressed) and an engine **palette
shift**: an active (`nominal`) gauge now reads **green** (`mint`), not amber. **5h H2** adds the landing
arc: a `CloseoutTrain` (the T13 derived 5-beat closeout-order strip, rendered on
`phase === "closeout-pending"`); `Conduit` now takes an `integrationStrategy` to select the
replay or ff-only strategy while the integration geometry remains straight; and a
`lane-landing-source` `LaneFlag` advances the official line to its `landing` source tip
(origin-main/origin-feat) while a strategy is recorded — read **null-safe** (`node.landing?.find`) so a
projection produced before the slice-5h `landing` field renders no flag instead of crashing. **5h coupler fix** re-frames `WarpCoupler` as the
**memory.md ledger** link (NOT the task contract): a drawn `warpLinkGlyph` chain-link replaces the node
rect, the label is `short(code) ⇄ short(memory)` (each coupler its own pair, via the new `short` helper),
and — when bound — two `warp-surge` bands render the warp-core surge. **5h cleanup pass** tightens the
conduit wiring: `Conduit` sets `markerEnd` (the `er-chev` chevron) **only on a `running` edge** — a
nominal/complete line is just a connection, never tipped — and the `er-chev` `refX` sits at the chevron's
**visual tip** (geom apex 8.5 + the round join) so a running arrowhead lands ON the line end, not past it
into the target engine. The provider conduits (`cgc-seed`/`grepai-clone`) run from each box's side-edge
**MIDPOINT** into the engine's **inner corner** (the `officialWire`s mirror that on the left), the six
`enginePetal` flanks are symmetric across the gauge centre, and the `sync` lane is **collinear** with
`worktree-add` on the code-intake centreline (one centred line, not an off-centre double).

**5h ledger popover** turns each `WarpCoupler` label into a clickable **button** (`ledgerButton` rect + the
`code ⇄ memory` label + a ▾ caret — a `<button>` can't live in svg, so the rect is the trigger and the
label sits on top, `pointerEvents:none`) that opens a React-Aria `Popover`/`Dialog` (portaled out of the
svg, anchored by `triggerRef`) rendering `LedgerTable` — the memory.md lookup table with THIS enclosure's
row highlighted (prefix-tolerant match against the coupler's current commit). It defaults to the newest
`LEDGER_PREVIEW` (8) rows; "▾ show N more" expands in place to the full served window (≤25). The popover
anchors **high in the scene** (a fixed invisible SVG `anchorRef`, not the coupler button — so it keeps its
upper position and scales with the canvas) and opens **downward** (`placement="bottom"`, `shouldFlip={false}`),
so expanding grows it **down**, **extending the card's frame** to the available height (`ledgerScroll`
`expanded` variant → `min(72vh, 46rem)`) and scrolling only if it still overflows the viewport;
"+N more in memory.md" points at the file beyond that.
The WORKTREE coupler reads
`node.ledgerRows`/`ledgerRowCount`; the OFFICIAL coupler reads the new `officialLedger?: LedgerNode` prop
(`rows` + `closeoutCount`), resolved per repo in `EngineRoom`. A coupler with no rows renders the plain
label (no button). **5h Tier 2** renders each `LedgerTable` row as **6 columns** —
`codeDate │ codeSubject │ codeHash ⇄ memHash │ memSubject │ memDate` — the two hashes meeting the centre
`ledgerSeam`, message + date fanning outward (messages truncate, full text in `title`). `compactDate(iso)`
string-slices the committer ISO to `MM-DD HH:mm` (`iso.slice(5,16).replace("T"," ")`) — no `Date`/timezone
conversion, so it is deterministic + screenshot-stable and shows the committer's recorded offset. A row
whose side wasn't probed (`codeSubject`/`codeDate` absent) shows empty message/date cells while keeping the
hash — the honest fallback, never faked.

The **visual-parity pass** threads a `workspaceEngines?: ProviderNode[]` prop (the official line's real
CGC/GrepAI, runtime via the `engineState` selector) and renders them as the **left** engines
(`ENGINE.mcgc`/`ENGINE.mgrep`) with `officialWire` conduits into the official branch nodes and an
`OFFICIAL_COUPLER_X` coupler (bound iff `hasMemory`); `WarpCoupler` is now parameterized by `x` + an
optional `label` + `testid` (worktree at `COUPLER_X`, official at `OFFICIAL_COUPLER_X` via
`warp-coupler-official`); `EngineGauge` draws the faint `engineSpine` + six `enginePetal` flank lines
(runtime-coloured); `CanopyFrame` renders once at the stage edges; and `LaneFlag` renders the
`ledger ▸ maps merge` annotation (when `hasMemory`) and `contract · historical` (when the enclosure is retiring —
`phase` abandoned **or** cleanup-pending). `LaneFlag` **truncates** its label to the box width (full text on hover),
so a long branch name can never overflow.

**5h H3** adds the **remote/PR strip beyond the official line** (the upstream the official line reports
into) — `RemoteStrip` renders, when `node.landing?.length`, the `landing[]` refs in a canonical D3→D4
order (`REMOTE_ORDER`: `origin-feat` → `pr` → `origin-main` → `origin-mem-main`) as a connected top band
(`REMOTE_X`/`REMOTE_Y`), the chips sized + typed as **peers of the branch nodes** so the labels read at the
same scale. `RemoteChip` draws each branch ref (a state rect + a readable label + one **terse status word**
via `remoteStateWord`; the full ref + detail lives on the hover `<title>`), toned by the pure
`remoteTone(ref)` — `planned` (`factState`/`state` planned) = dashed/muted, a landed `tip`/`merged`/`pushed`
= `done` (mint), else `live` (amber); `PrBadge` is a distinct rounded pill for the `pr` ref (open = amber
outline → merged = mint fill). Consecutive chips are **wired**: `remoteConnector` (solid amber) links the
code chain feat→PR→main and `remoteConnectorCarry` (dashed) marks the code→memory **carryover handoff**
into `origin/mem-main`; the centred `remoteStripHeader` sits in the gap between the OFFICIAL LINE /
WORKTREE ENCLOSURE corner labels. The governed order is legible in a single frozen frame: `origin-mem-main`
stays dashed (`planned`, "after carryover") until the PR merges, then settles `done` — **code-first,
memory-after**. The only motion is a gated `fill`/`stroke` transition on a projection state flip, frozen to
the static end-state under `data-effects=off`.

**5h H4** — cleanup teardown lane annotations: a `cleanup-pending` (landed) enclosure de-materialises like abandon, so
besides the shared `contract · historical` chip (`retiring`) this file adds a **back into main** seam
(`lane-back-into-main`) reading the resolved `origin-main` tip (`cleanupTip`); the dissolve + the success
`CleanupRecord` live in `EnclosureProcessMap`. A related **landing-source honesty fix**: `landingSource` (the H2
official-line advance) now drops **unresolved** refs via `resolvedRef` (`factState: "missing"` or `state: "unknown"`),
so a completed enclosure whose source branch was deleted post-merge no longer leaks a stale `▸ origin/feat/… · unknown`
flag.

**5i — the canvas becomes a moving build-up / tear-down stage** (driven by the dev scenario player; the
structure + colour honesty above are unchanged). The canvas now **animates**, on three layers (this is the
CSS-substrate state slice **05k** then corrects to all-GSAP/Motion):
- **Motion substrate.** GSAP owns the conduit/landing **draw-on** — `Conduit` and the new `LandingFlow`
  each run `gsap.fromTo(strokeDashoffset 100 → 0)` inside a `gsap.context`/`useLayoutEffect` keyed on
  `edge.state`/`show` and gated by `useShouldAnimate` (so a `planned → running` cycle re-draws; under
  `data-effects=off` it never runs and the path rests drawn). Motion owns enter/exit: the closeout train is
  wrapped in `AnimatePresence` (`motion.g` initial/animate/exit + `transition:"none"` to opt out of the CSS
  tween) so it glides in/out instead of vanishing. The `sceneSvg` **global CSS transition** (added in
  `engineRoomStyles`) eases opacity/transform/fill/stroke as the projection advances frame to frame
  (`stroke-dashoffset` excluded — GSAP owns it alone); `data-effects=off` freezes it to the instant
  end-state, so the count/presence tests stay synchronous.
- **Three-tier landing (5f §7.4).** The source nodes render the current `CommitRefNode` under the
  visible label **Integration line**. The feat/fix SOURCE
  the worktree was branched off renders as its own tier in the gap (`POS.featCode`/`featMemory` at x512),
  shown only while landing (`showLanding`), fading in via `landingIn` — so closeout reads
  **main ◂ feat ◂ worktree**, never collapsing main and feat.
- **Build-up materialisation gates (honesty axis).** `branchEnter(factState)` maps `planned` → hidden +
  offset toward main, `observed`/`derived` → in place, `missing`/unknown → dim; the enclosure border, the
  worktree engines (`EngineGauge present`), the worktree coupler (`WarpCoupler visible`), and the worktree
  lane flag (`LaneFlag visible`) fade in only once the matching worktree ref materialises / the provider
  runtime deploys (B1/B3). At cleanup a worktree node `detaching` drifts OUT to the right as it fades (the
  D5 de-materialise direction, vs the build-up's slide-in-from-main).
- **Provider clone arcs (5f §7.2 "cloned-from, not re-indexed").** `cgc-seed`/`grepai-clone` are redrawn as
  cross-stage arcs from the **official engine** to the **worktree engine** (CGC bows over the top, GrepAI
  under the bottom via `dip`) — TRANSIENT (shown only while `running`, gone at idle). The persistent
  worktree-engine → branch link is a separate static `worktree-wire` line (mirroring the left world).
- **Remote/landing dock rework (supersedes the 5h H3 row layout).** Chips are now placed by `REMOTE_POS`
  (code remotes side-by-side at the TOP — origin/feat ▸ PR ▸ origin/main, reading right → left; the memory
  remote mirrored to the BOTTOM), `PrBadge` is a leftward **merge-arrow line** in the gap (PR id + state on a
  line beneath), and the new `LandingFlows`/`LandingFlow` wire the dock to the branch nodes (push ↑ to
  origin/feat, pull ↓ from origin/main, carry ← into local mem, push-mem ↓ to origin/mem-main) so it reads
  as the governed flow. The old `REMOTE_ORDER`/`remoteConnector(Carry)`/`prBadgeSub` and the
  `lane-landing-source` flag are **removed** (the official-line advance now reads through the dock + flows).

**5i — the canvas motion split: CSS → GSAP timelines + Motion (the `05f` §8 end state).** The structure +
colour honesty above are unchanged; only HOW it animates changed, and the property-split law (§8.1) is now
clean: **every animated element is a `motion.*`** (`motion.g`/`motion.rect`/`motion.line`/`motion.path`),
and Motion owns opacity/transform/scaleY + enter/exit; the `engineCharge` class owns fill:
- **`useEngineTimeline` is wired to the `<svg>` root.** A `rootRef` on the `<svg>` is passed to
  `useEngineTimeline(rootRef, node)`, which owns the GSAP side as ONE `gsap.context` scoped to that root —
  the DrawSVG draw-ons (`[data-draw='on']`, one-shot per lane — 05n; `pathLength` is gone, DrawSVG measures
  the real length) + the repeating fx (`[data-fx=…]`). The
  **per-component `gsap.fromTo`/`gsap.context`** that used to live in `Conduit` and `LandingFlow` (the 5i
  draw-on effects) are **removed** — the component now only marks the element (`data-draw={edge.state ===
  "running" ? "on" : undefined}` on a conduit, `data-draw={show ? "on" : undefined}` on a landing flow) and
  the hook drives it.
- **The `data-fx` attributes replace the deleted CSS keyframes.** `EngineGauge` marks the fault rect
  `data-fx='fault'` (down, not reindexing) and the reindex rect `data-fx='reindex'`; `WarpCoupler` marks the
  two surge bands `data-fx='surge'` + `data-dir='up'|'down'`; the attention badge is `data-fx='breath'`, the
  terminal STOP `data-fx='stop'`, and the travelling flow packet **`data-fx='packet'`** — which now carries
  its conduit path on `data-path` (no CSS `offset-path`) and renders only while `animate`. The hook's
  `buildFx` runs each loop, riding the packet along `data-path` via GSAP MotionPath (05n).
- **`Motion` owns the rest, gated.** `EngineGauge` is a `motion.g` (opacity by `present`) whose charge rect
  is a `motion.rect` driven by `chargeMotion(runtime)` (the animated `scaleY` + opacity — Motion owns
  **only** scaleY+opacity; **fill is 100% owned by the `engineCharge` CVA class**, cyan `indexing` → mint
  `nominal`, never by Motion or a CSS animation — see the **second-cycle fill fix** below); `BranchNode` is a
  `motion.g` (`branchEnter` opacity/x + the `landingIn` lift); the
  worktree wire is a `motion.line` (opacity by engine presence — the recipe carries no opacity); the warp
  coupler / clone-arc conduits / dock chips / landing flows all set `initial={animate ? … : false}` so under
  `!animate` they mount at the end-state.
- **`AnimatePresence` owns the conditional enter/exit.** The **feat-tier** source nodes (`featCode`/
  `featMemory`, shown only while `showLanding`) and the **landing dock** (the remote chips + `LandingFlows`,
  shown only with a landing arc) are each wrapped in `AnimatePresence` (replacing the deleted `landingEnter`
  CSS atom), and the **closeout train** keeps its `AnimatePresence`; so they glide in/out instead of
  popping when the phase advances.
- **05k D3 fixture support.** The dock reads the new `engine-landing-pushed` (D3 "code lands") fixture the
  same way as any landing arc — no canvas code change beyond the motion split; the D2/D3 split lives in the
  `fixtures.ts` / `dev/scenarios.ts` data.

**Layout + fill rework (2026-06-21).** A four-part pass — re-spaces the stage, hard-fixes the second-cycle
engine fill, relocates the closeout train, and mirrors the integration arrow:
- **Second-cycle engine-fill fix.** The old `booting`/CSS-`powerup` machinery is **removed**. The charge rect's
  FILL is now owned entirely by the `engineCharge` CVA class (instant cyan `indexing` → mint `nominal` every
  cycle); Motion writes **no** inline fill (Motion 12 can't interpolate oklch, so a stale inline fill would
  override the class). The indexing→nominal "powerup" is now a **one-shot Motion OPACITY pulse**
  (`opacity: [0.85, 1, 0.55]`, `times [0,0.35,1]`, easeOut) gated by a `booting` flag: a new `useEffect`
  watches `prevRuntime` and sets `booting` on the `(not nominal) → nominal` crossing (while `animate`); the
  pulse is torn down by the rect's Motion **`onAnimationComplete`** with a `booting`-keyed `setTimeout(1000)`
  backstop (keyed on `booting` alone so a frame advance never cuts it short). This fixed the bug where the
  engines stayed green / never went cyan on the second scenario loop — a CSS `@keyframes forwards` fill-lock
  plus an `onAnimationEnd` that never fires on a `motion.rect`. A stuck flag is now harmless: the fill is
  class-owned and the pulse just holds its final 0.55 (the nominal rest opacity).
- **Column re-spacing & alignment** (`COL_MAIN_CX`/`COL_FEAT_CX`/`COL_WT_CX`) — see the geometry constants in
  *Logic* above. Net visual result: even ~72px gaps between the three middle columns, remote chips on their
  column centrelines, and the four `LandingFlow` paths now clean verticals/horizontals.
- **Closeout train relocated.** `CloseoutTrain` moves to a **bottom-left breadcrumb** (`x=260, y=600`) on the
  same baseline as the bottom gate/recovery-chip row — left of centre, clear of the left engine (right edge
  135) and the gate chips (start x≈690) — and its caption is legible against the darker lower backdrop.
- **Memory integration arrow.** New `EDGE_GEOM["integration-mem"]` on the memory lane (`y=403`, worktree →
  feat, mirroring the code `integration` edge before the carryover); `Conduit`'s replay check is widened to
  `isReplay = (kind === "integration" || kind === "integration-mem") && strategy === "replay"`.

Two closely-coupled cleanups landed in the same pass: `Conduit` takes a new `retiring` prop that fades
**every worktree conduit to 0** at cleanup (`opacity = retiring ? 0 : …`) so the yellow connectors retract
with the enclosure instead of dangling to disposed nodes (the official `officialWire`s aren't in
`node.edges`, so they persist); and `LandingFlow` is rebuilt around a `FlowState` (`active`/`settled`/`hidden`,
computed by `landingFlowState` from the `landing[]` ref progression push→pull→carry) speaking the cyan=ACTIVE
/ amber=SETTLED language — at most one flow is cyan (DrawSVG draw-on + a travelling `data-fx='packet'` dot),
a completed step drops to a plain amber `nominal` line (no chevron, no dot), unreached steps hidden. Plus a
**5o predictive-boot** read in `EnclosureCanvas`: while `cgc-seed`/`grepai-clone` is `running` and the engine
still `configured`, `codeRuntimePredicted`/`memoryRuntimePredicted` treat it as `indexing` so the fill
animates in sync with the clone arrow instead of after the data flips.

**05o T3B — the memory/ledger-block primitives.** Two projection-driven reads gate the new `scanRing` +
`ghostedLane` recipes (both off `node`, never a class alone): `checking` = a `ledger-map` edge is `running`
AND the memory worktree is not yet materialised (the ledger-verify sweep is in flight) → a `<circle
className={scanRing} data-fx="scan">` renders at the **ledger-map lane midpoint** (`cx={COL_FEAT_CX} cy={403}`,
the same point the `Gate` later draws) gated additionally on `animate` (absent under effects=off, like the
packet); `useEngineTimeline buildFx` rides it. `memGated` = the memory worktree `factState === "missing"` OR a
`ledger-map` edge `state === "blocked"` → the `node.edges.map(Conduit …)` passes `ghosted={memGated &&
edge.kind === "ledger-map"}` so the held memory conduit dims+desaturates (the `Conduit` applies `ghostedLane`
to its **inner `<path>`** via `cx(...)` — not the `motion.g` — and sets `data-ghosted` for the tests) while the
code lane stays solid. The steady `Gate` + `Attention` + `RecoveryChips` (reconciliation) already cover the
block; the scan-ring + ghost are the net-new T3B reads. `cx` is imported from `styled-system/css`.

**05o T1B — the stale-base block plus the indicator-anchoring/z-order/transition pass.** `BranchNode` gains a
`pruned` prop that combines `prunedNode` onto the stale code-base node's fact-state box (driven in the caller
by `baseStale = codeSource.behindSource > 0 && isBlocked && fleeting`), reading DORMANT over the box it
already drew — note the **`cx`-shadow gotcha** flagged in the code: the local `cx` inside `BranchNode` is the
node-centre number, which **shadows the Panda `cx`**, so the `pruned` class is concatenated by hand rather
than via `cx(...)`. The verify SCAN ring and the block GATE + REASON badge now anchor **ON the checked
REPOSITORY NODE rectangle**, never the connector-lane midpoint: `scanAt` centres the scan on the node (code
base `y=281` for T1B, memory base `y=403` for T3B), and a new `NodeBlock` component draws the steady gate bar
straddling the node's top edge with the reason badge above it (driven by `baseChecking`/`memChecking` for the
verify sweep and `blockNode` for the block) — mirroring the prototype where the gate sits on the Code node,
not the wire. Those node-anchored POINTERS (the scan + `NodeBlock`) render in the **TOPMOST overlay layer**
(dead last in the SVG): SVG paint order equals document order, so centring a pointer on a node while painting
it *before* the node let the node's opaque rect cover it. A fleeting **born-blocked** enclosure now renders
the big red `FleetingEnclosure` box (podstage `.fbox`) over the worktree footprint — the BLOCKED title +
reason + recovery chips — and **suppresses the dashed-amber enclosure border**, replacing the HTML banner that
used to live in `EnclosureProcessMap`. Finally a new `alertProps` helper plus `AnimatePresence` give every
failure overlay (gate, reason, attention, chips, terminal STOP, scan ring, the block pointer) a Motion fade +
subtle scale-pop on ENTER and EXIT (`transformBox: fill-box` so the pop grows from the element's own centre),
gated by `useShouldAnimate` — instant end-state under effects-off so the snapshots stay deterministic.

**05o — the six remaining failure modes (T7B/T9·T14C/T12B), keeping the node-anchored + topmost-pointer +
`alertProps`-transition doctrine.** Two shared helpers carry the new lanes: `conduitPathD(edge)` extracts the
conduit path string (straight lane / clone-arc BOW) so `Conduit` and the new refused-flash trace the *exact*
same geometry (no duplicated arc maths), and `refusedPolarityOf(edge)` **derives** the flash polarity from
the edge STATE — a `failed` seed/return lane → red, a `stale` lane → amber — `null` for anything else. It
reads no polarity field: `EngineProcessEdge` has none, and the `refused` state it used to branch on is not
in the model's own documented state vocabulary (`nominal|running|blocked|failed|stale|skipped|complete|
planned|unknown`) and has never been emitted — `git log --all -S 'state="refused"'` returns zero commits.
The `integration` / `integration-mem` kind arms are kept even though today's reducer only emits
worktree-add, cgc-seed, ledger-map, grepai-clone and sync. (Both edge builders were checked:
`reducer.py::_process_edges` and `reducer.py::_start_process_node`. The in-code comment beside
`refusedPolarityOf` used to cite a `_engine_edges` that has never existed in this repository;
260731-EFA-L4 corrected it in place to name the two real builders, so the current source comment
now agrees with `reducer.py`. Do not re-report this: the only remaining occurrences of `_engine_edges`
anywhere are in prose describing the correction.) The honest reason is **not**
forward-compatibility — nothing is scheduled to start emitting them. It is that `integration` IS in
`EngineProcessEdge`'s documented `kind` vocabulary (unlike `refused`, which its state comment never
listed), and that the whole integration lane — geometry, the T14C conflict scenario, the replay strategy —
is authored in the dev fixtures and covered by tests, so the arms are exercised even though the server does
not drive them. `integration-mem` is the memory-side mirror, is NOT itself in that documented list, and
lives or dies with `integration`. Delete the lane and its coverage together, or not at all. New components: `RefusedConduit` (the
one-shot `data-fx='refuse'` GSAP flash over each `refusedEdges` lane — covering `cgc-seed`/`grepai-clone`
seed faults/reroutes and `integration`/`integration-mem` conflicts — resting at opacity 0 so it is
present-but-absent under effects-off while the steady STOP/gate carries the settled state), and `MovedBadge`
(the soft cyan ▲ "moved" pill, mirroring `ReasonBadge` geometry with an up-triangle glyph, anchored on the
memory worktree node). New `EnclosureCanvas`-level derivations, all read off the projection: **T7B** —
`providerPlanBlocked` (the alarm fires when both worktrees materialised but zero providers exist +
`setupState === "blocked"` + a provider-plan/setup-config missing fact). UNLIKE T1B/T3B this does NOT gate a
repository node: the `ProviderBlock` component (dev directive) draws a **VERTICAL alarm bar attached to the
LEFT side of the worktree CGC provider engine slot** (the barred provider runtime — right edge meets the
engine's left edge, full slot height) plus the reason badge riding the **TOP EDGE of the worktree enclosure**
as a containment header, with the `engineDropout` dashed halos over the two UNLIT worktree engine footprints;
`providerChecking` / `providerScanAt` give the P3 verify scan AT the worktree CGC engine centre. Crucially
`fleeting` is **tightened with `&& !providerPlanBlocked`** so a T7B block (which shares the "contract not yet
written" fact) never falls into the big red `FleetingEnclosure` box — it draws the engine-side bar + unlit
engines instead. `scanCenter` (`scanAt ?? providerScanAt`) unifies the source-lane (T1B/T3B) and engine (T7B) verify
rings. **T12B** — `memMoved` / `movedAt` (the soft notification BEFORE the gate: a real memory worktree with
`memorySource.behindSource > 0` and not yet blocked → the `MovedBadge`) and `memSyncMoved` (the escalated
gate, **restricted to a blocked `ledger-map` edge** so it never reclassifies the code-side
`engine-sync-needed` gallery fixture, which has a blocked `sync` edge and keeps its existing edge-gate
render); `blockNode` now branches T1B (stale main CODE base) / T12B (held memory worktree) / T3B (unmappable
memory base). `refusedEdges` is the filtered `(edge, polarity)` list driving the flash. The `Conduit`
`ghosted` condition is broadened to `(memGated || memSyncMoved) && edge.kind === "ledger-map"`. `Conduit`
carries **no** `data-refused-polarity` attribute: polarity is derived by `refusedPolarityOf` at the point
the overlay is built, so there is nothing on the conduit for the flash to read back. All the new
overlays — the refused flash, the engine-dropout halos, the moved badge — render in the **TOPMOST layer**
(after the nodes, with the scan ring + block gate), so a node's opaque rect can never cover a node-anchored
pointer.

**05o T14C — the `TerminalStop` review fix (legibility + non-collision).** The terminal integration-conflict STOP
no longer renders its conflict words ON the `integration` lane midpoint — the bright red conduit line bisected the
on-lane glyphs and read as illegible. The reason now renders as a **legible banner** lifted clear into the band
ABOVE the node row (`by = cy − 58`): the SAME combo as the recoverable reason badges — the `reasonBadge` dark
opaque pill + red border with `reasonText` light text — rather than dark-on-bright-red, with the ⛔ no-entry glyph
carrying the STOP identity. A compact red on-lane STOP **bar** (the `stopBar` recipe, `data-fx='stop'`) sized to
the ~66px feat↔worktree gap (`x = cx − 33`, width 66) now marks the conflict point on the lane WITHOUT colliding
with the worktree node — the old 128px-wide pill centred on that gap overran it. That bar carries
`data-testid="terminal-stop-bar"` and deliberately **NOT** `data-testid="gate"` (it is terminal, not a recoverable
`Gate`); the group keeps `data-testid="terminal-stop"` + `data-kind`. `stopBar`/`reasonBadge`/`reasonText` are the
recipes it composes.

### Invariants And Boundaries

Purely presentational — all data via the `node` (+ `workspaceEngines`) props; **state comes from
the model** (`factState` / `runtimeState` / `edge.state`), never a class name alone — and never a
decorative field on the edge either. `refusedPolarityOf` DERIVES amber/red from `edge.state`; the panel
must not reintroduce an `edge.refusedPolarity`, because the server model (`EngineProcessEdge`,
`extra="forbid"`) has no such field and could never send one. The same rule governs which arms may
exist here: a `kind` arm is legitimate when the kind is in `EngineProcessEdge`'s documented vocabulary
and is exercised by fixtures and tests (that is `integration`, and `integration-mem` riding with it); a
`state` arm for a state the model never documented and the reducer never emits — `refused` — is a dead
branch, and was deleted as one. The canvas **animates**
on two systems only (`05f` §8, post-05k): **GSAP** (`useEngineTimeline`, wired to the `<svg>` `rootRef`) owns
the `strokeDashoffset` draw-ons (`[data-draw='on']`) + the repeating fx (`[data-fx=…]`), and **Motion** owns
opacity/transform/scaleY/fill + `AnimatePresence` enter/exit — never both on the same property/element
(§8.1). There is **no CSS animation/transition** here anymore (the `sceneSvg` transition + the per-component
`gsap.fromTo` are gone). Both systems are gated by `useShouldAnimate()`: under reduced-motion / `data-effects=off`
the hook builds no `gsap.context`/ticker and every `motion.*` mounts at the end-state (`initial={false}`),
so the canvas renders the instant settled state and the count/presence tests stay synchronous.
The memory lane (memory branch nodes + GrepAI gauge + bound coupler + the dashed enclosure border) renders
only when `hasMemory`; otherwise a `memory-lane-absent` note. The **left official-line engines** are now
rendered here too (the visual-parity pass), driven by `workspaceEngines` — so the canvas shows the full
two-world picture; `EngineRoom`'s `OfficialStrip` stays the compact text summary above the stage. The
official `LaneFlag`s are descriptive lane labels (the live status lives in the diagnostics panel + node
fact-states), and `CanopyFrame` is `aria-hidden` (pure chrome). `data-testid` hooks (`enclosure-canvas`,
`branch-node`, `engine-gauge`, `warp-coupler`, `warp-coupler-official`, `conduit`, `canopy-frame`,
`official-wire`, `lane-ledger`, `lane-historical`, `remote-strip`, `remote-chip`, `pr-badge`) plus
`data-runtime`/`data-bound`/`data-kind`/`data-tone`/`data-state` are load-bearing for the render tests. The center-out engine charge, the conduit draw-on, and the travelling
`flowPacket` landed in G2; the failure overlays landed in G3 — a steady `Gate` over each blocked/failed edge,
a local `ReasonBadge` (the node summary), the breathing `Attention` parity, and `RecoveryChips`
(`nextAction` + enabled actions); a fleeting pre-contract block renders `FleetingEnclosure` directly.
**G4** added the engine fault/reroute: a `down` provider's engine flickers
(isolated), `seedFallback` puts the CGC gauge in an amber `reindex` pulse, and `retryArgs` adds a retry chip.
Branch text truncates to the box with the full string in a `<title>` (hover).

### 260712-TRH-L7 stale landing honesty

Landing refs with `factState: stale` remain visible, carry an explicit state word and age, and use alarm-toned styling. `landingFlowState` permits motion only for observed facts, so stale and missing facts do not animate as current while the enclosure remains inspectable.

## Evidence

### Repo-Internal References

- `EnclosureCanvas` — the two-world SVG scene (the only export; `node` + `workspaceEngines`). [1]
- `BranchNode` / `EngineGauge` (spine + petals) / `WarpCoupler` (`x`/`testid`) / `Conduit` sub-components. [2]
- `CanopyFrame` (HUD housing) + `LaneFlag` (lane annotations) decals. [3]
- `RemoteStrip` / `RemoteChip` / `PrBadge` + `remoteTone` — the remote/landing dock (`landing[]` refs; 5i positions them by `REMOTE_POS`, PR as a merge-arrow). [4]
- `LandingFlows` / `LandingFlow` + `landingFlowState` (`FlowState` active/settled/hidden) — the directional push/pull/carry flows wiring the dock to the branch nodes (cyan-active / amber-settled, GSAP draw-on); paths derived from the column centres. [5]
- `COL_MAIN_CX`/`COL_FEAT_CX`/`COL_WT_CX` define the main, feat, and worktree column centres; `ENGINE` declares the fixed engine-pod positions in the geometry constants. [6]
- The consumer sites apply those centres to remote chips and PR placement, landing-flow paths, official/worktree wires and couplers, and the enclosure border. [7]
- `EDGE_GEOM["integration-mem"]` (memory-lane y=403 worktree→feat mirror of `integration`) + `Conduit`'s widened `isReplay` check + the `retiring` fade. [8]
- `chargeMotion` + the `booting` one-shot opacity pulse (`onAnimationComplete` + timer backstop) — Motion owns scaleY/opacity, the `engineCharge` class owns fill (second-cycle fill fix). [9]
- `branchEnter` maps fact state to branch-node opacity/x materialisation. [10]
- `useEngineTimeline(rootRef, node, fxRootRef)` wires the structural SVG root and sparse sibling `EngineFxOverlay` into one GSAP selector scope: `useEngineTimeline` owns draw-on/retract selection, `buildFx` selects `data-fx` markers, the overlay renders repeating surge/reindex/breath primitives, and Motion owns structural opacity/transform. [11]
- `refusedPolarityOf` derives the flash polarity from `edge.state` alone (`failed`→red, `stale`→amber); the full rationale comment records the two current edge builders, their documented-kind distinction, fixture/test coverage, and why the integration arms remain despite no served payload driving them. [12]
- `refusedEdges` — the `(edge, polarity)` list that drives the topmost flash; `RefusedConduit` renders it and stamps `data-polarity`/`data-refused-polarity` from the DERIVED polarity (the conduit itself carries neither). [13]
- `Conduit` carries `data-kind`/`data-state`/`data-strategy`/`data-ghosted` and no polarity attribute. [14]
- `EngineProcessEdge`'s documented `kind` and `state` vocabularies — `integration` is in one, `refused` in neither, and there is no `refusedPolarity` field. [15]
- `_process_edges` emits only worktree-add, cgc-seed, ledger-map, grepai-clone and sync, so no served payload reaches the integration arms. [16]
- `_start_process_node` — the other edge builder, checked for the same reason and emitting the same four kinds. [17]
- Current `data-fx` marker ownership is split by renderer: `EngineGauge` renders `fault` and the structural reindex charge; `EngineFxOverlay` renders repeating `surge`/`reindex`/`breath`; `Conduit` and `LandingFlow` render `packet` dots; `TerminalStop` renders `stop`. [18]
- `AnimatePresence` enter/exit (05k) on the feat-tier source nodes + the landing dock + the closeout train. [19]
- `shouldAnimate` returns false for the effects-off or reduced-motion conditions, and `useShouldAnimate` resynchronizes that gate; `useEngineTimeline` is the GSAP consumer while `EngineGauge`/`Conduit`/`LandingFlow` are Motion consumers that use the boolean to render the end state. [20]
- Left official-line engines + `officialWire` conduits + official coupler (from `workspaceEngines`). [21]
- The `engineState` selector that derives each workspace engine's runtime. [22]
- The bird's-eye recipes it renders with (incl. `engineSpine`/`enginePetal`/`officialWire`/`canopyStroke`/`laneFlag`). [23]
- Projection types `EngineProcessEdge`/`EngineProcessNode`. [24]
- CommitRefNode carries source/worktree commit observations and fact state. [25]
- ProviderBootNode carries the booted provider identity, role and runtime state. [26]
- LandingRefNode carries observed landing state and freshness details. [27]
- ProviderNode carries workspace/worktree provider health and indexing observations. [28]
- 05o T3B — `checking`/`memGated` derivations + the `scanRing` `<circle data-fx="scan">` + `Conduit ghosted` (the `ghostedLane` inner-`<path>` ghost). [29]
- The `scanRing` recipe is the full cyan stroked, transparent, glow style; `ghostedLane` is the full dim/desaturate style; `Conduit` applies `ghostedLane` to the inner path through `cx(flowConduit(...), ghosted && ghostedLane)`. [30]
- The design prototype supplies the ported canopy bracket geometry, provider wire/flow links, and engine spine/petal decals: its canopy path, `wire`/`flow-g` links, provider geometry, and `.e-spine`/`.e-petal` recipes are present in the prototype. [31]

## Series-Contract Notes

The canvas renders the official/source branch from the projected `CommitRefNode` instead of forcing the label to `main`, so a master series leaf can display its integration branch as the official line.

## Current L5I Maintenance

The warp-surge bands now render their full geometry and leave their expanding/retracting motion to
the timeline's composited transform. This avoids per-frame SVG endpoint writes while retaining the
same link-origin choreography.

## 260727-CHATS-IM-L2 Current Delta

When effects are enabled, the repeating surge, reindex, and attention primitives render in a
sparse sibling `EngineFxOverlay`; their structural counterparts are hidden or lose `data-fx`
ownership. With effects off, the original structural SVG renders the static end state. Shared
view-box geometry and style classes preserve the visual composition.
