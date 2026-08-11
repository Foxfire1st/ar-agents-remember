# dashboard/src/panels/engine-room/EnclosureCanvas.tsx

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `dashboard/src/panels/engine-room/EnclosureCanvas.tsx` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated | 2026-08-01T15:10+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`             |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                          |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `EnclosureCanvas` — the two-world SVG scene (the only export; `node` + `workspaceEngines`). | `EnclosureCanvas` | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:42-93 |
| `BranchNode` / `EngineGauge` (spine + petals) / `WarpCoupler` (`x`/`testid`) / `Conduit` sub-components. | `BranchNode`; `EngineGauge`; `WarpCoupler`; `Conduit` | dashboard/src/panels/engine-room/conduits.tsx:70-136; dashboard/src/panels/engine-room/engines.tsx:72-128; dashboard/src/panels/engine-room/engines.tsx:136-195; dashboard/src/panels/engine-room/ledger.tsx:210-282 |
| `CanopyFrame` (HUD housing) + `LaneFlag` (lane annotations) decals. | `CanopyFrame`; `LaneFlag` | dashboard/src/panels/engine-room/badges.tsx:41-58; dashboard/src/panels/engine-room/badges.tsx:284-308 |
| `RemoteStrip` / `RemoteChip` / `PrBadge` + `remoteTone` — the remote/landing dock (`landing[]` refs; 5i positions them by `REMOTE_POS`, PR as a merge-arrow). | "export function RemoteChip({ refNode }: { refNode: LandingRefNode }) {"; "export function PrBadge({ refNode }: { refNode: LandingRefNode }) {"; "export function RemoteStrip({ refs }: { refs: LandingRefNode[] }) {"; "export function remoteTone(ref: LandingRefNode): RemoteTone {" | dashboard/src/panels/engine-room/geometry.ts:210-214; dashboard/src/panels/engine-room/geometry.ts:221-226; dashboard/src/panels/engine-room/remote.tsx:26-51; dashboard/src/panels/engine-room/remote.tsx:56-78; dashboard/src/panels/engine-room/remote.tsx:84-102 |
| `LandingFlows` / `LandingFlow` + `landingFlowState` (`FlowState` active/settled/hidden) — the directional push/pull/carry flows wiring the dock to the branch nodes (cyan-active / amber-settled, GSAP draw-on); paths derived from the column centres. | "export function LandingFlows({ refs }: { refs: LandingRefNode[] }) {"; "function LandingFlow({ d"; "function landingFlowState(refs: LandingRefNode[]" | dashboard/src/panels/engine-room/conduits.tsx:192-192; dashboard/src/panels/engine-room/conduits.tsx:139-139; dashboard/src/panels/engine-room/conduits.tsx:184-184 |
| `COL_MAIN_CX`/`COL_FEAT_CX`/`COL_WT_CX` define the main, feat, and worktree column centres; `ENGINE` declares the fixed engine-pod positions in the geometry constants. | `COL_MAIN_CX`; `COL_FEAT_CX`; `COL_WT_CX`; `ENGINE` | dashboard/src/panels/engine-room/geometry.ts:47-49; dashboard/src/panels/engine-room/geometry.ts:61-65 |
| The consumer sites apply those centres to remote chips and PR placement, landing-flow paths, official/worktree wires and couplers, and the enclosure border. | "export function RemoteStrip({ refs }: { refs: LandingRefNode[] }) {"; "export function LandingFlows({ refs }: { refs: LandingRefNode[] }) {"; "export function EnclosureCanvas({" | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:42-93; dashboard/src/panels/engine-room/conduits.tsx:192-205; dashboard/src/panels/engine-room/remote.tsx:84-102 |
| `EDGE_GEOM["integration-mem"]` (memory-lane y=403 worktree→feat mirror of `integration`) + `Conduit`'s widened `isReplay` check + the `retiring` fade. | "export const EDGE_GEOM: Record<string"; "export type ConduitState ="; "function isReplayLane("; "export function Conduit(" | dashboard/src/panels/engine-room/geometry.ts:70-70; dashboard/src/panels/engine-room/geometry.ts:12-12; dashboard/src/panels/engine-room/conduits.tsx:22-22; dashboard/src/panels/engine-room/conduits.tsx:70-70 |
| `chargeMotion` + the `booting` one-shot opacity pulse (`onAnimationComplete` + timer backstop) — Motion owns scaleY/opacity, the `engineCharge` class owns fill (second-cycle fill fix). | "export const engineCharge = cva({"; "export function chargeMotion(runtime: RuntimeState): { scaleY: number; opacity: number } {"; "const [booting"; "export function EngineGauge({ at" | dashboard/src/panels/engine-room/stage.styles.ts:125-125; dashboard/src/panels/engine-room/geometry.ts:268-268; dashboard/src/panels/engine-room/engines.tsx:151-151; dashboard/src/panels/engine-room/engines.tsx:136-136 |
| `branchEnter` maps fact state to branch-node opacity/x materialisation. | `branchEnter` | dashboard/src/panels/engine-room/geometry.ts:141-155 |
| `useEngineTimeline(rootRef, node, fxRootRef)` wires the structural SVG root and sparse sibling `EngineFxOverlay` into one GSAP selector scope: `useEngineTimeline` owns draw-on/retract selection, `buildFx` selects `data-fx` markers, the overlay renders repeating surge/reindex/breath primitives, and Motion owns structural opacity/transform. | "import { EngineFxOverlay } from \"./EngineFxOverlay\";"; "function buildFx(q: gsap.utils.SelectorFunc): void {"; "export function useEngineTimeline(" | dashboard/src/panels/engine-room/sceneLayers.tsx:30-30; dashboard/src/panels/engine-room/useEngineTimeline.ts:83-83; dashboard/src/panels/engine-room/useEngineTimeline.ts:168-168 |
| `refusedPolarityOf` derives the flash polarity from `edge.state` alone (`failed`→red, `stale`→amber); the full rationale comment records the two current edge builders, their documented-kind distinction, fixture/test coverage, and why the integration arms remain despite no served payload driving them. | "export function refusedPolarityOf("; "Any other kind/state → no flash." | dashboard/src/panels/engine-room/geometry.ts:124-124; dashboard/src/panels/engine-room/geometry.ts:110-110 |
| `refusedEdges` — the `(edge, polarity)` list that drives the topmost flash; `RefusedConduit` renders it and stamps `data-polarity`/`data-refused-polarity` from the DERIVED polarity (the conduit itself carries neither). | "<RefusedOverlay fleeting={scene.fleeting} refusedEdges={scene.refusedEdges} />"; "export function RefusedConduit(" | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:85-85; dashboard/src/panels/engine-room/badges.tsx:265-281 |
| `Conduit` carries `data-kind`/`data-state`/`data-strategy`/`data-ghosted` and no polarity attribute. | `Conduit` | dashboard/src/panels/engine-room/conduits.tsx:70-136 |
| `EngineProcessEdge`'s documented `kind` and `state` vocabularies — `integration` is in one, `refused` in neither, and there is no `refusedPolarity` field. | `EngineProcessEdge` | mcp/src/agents_remember/observer/projection.py:785-804 |
| `_process_edges` emits only worktree-add, cgc-seed, ledger-map, grepai-clone and sync, so no served payload reaches the integration arms. | "def _process_edges(" | mcp/src/agents_remember/observer/reducer_impl/_processes.py:539-539 |
| `_start_process_node` — the other edge builder, checked for the same reason and emitting the same four kinds. | "def _start_process_node(entry: dict[str" | mcp/src/agents_remember/observer/reducer_impl/_processes.py:122-122 |
| Current `data-fx` marker ownership is split by renderer: `EngineGauge` renders `fault` and the structural reindex charge; `EngineFxOverlay` renders repeating `surge`/`reindex`/`breath`; `Conduit` and `LandingFlow` render `packet` dots; `TerminalStop` renders `stop`. | `EngineFxOverlay`; `EngineGauge`; `Conduit`; `LandingFlow`; `TerminalStop` | dashboard/src/panels/engine-room/EngineFxOverlay.tsx:127-149; dashboard/src/panels/engine-room/badges.tsx:237-258; dashboard/src/panels/engine-room/conduits.tsx:70-136; dashboard/src/panels/engine-room/conduits.tsx:139-164; dashboard/src/panels/engine-room/engines.tsx:136-195 |
| `AnimatePresence` enter/exit (05k) on the feat-tier source nodes + the landing dock + the closeout train. | "export function EnclosureCanvas({"; "export function CloseoutTrain({ x" | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:42-93; dashboard/src/panels/engine-room/badges.tsx:315-342; dashboard/src/panels/engine-room/EnclosureCanvas.tsx:22-22 |
| `shouldAnimate` returns false for the effects-off or reduced-motion conditions, and `useShouldAnimate` resynchronizes that gate; `useEngineTimeline` is the GSAP consumer while `EngineGauge`/`Conduit`/`LandingFlow` are Motion consumers that use the boolean to render the end state. | "export function shouldAnimate(): boolean {"; "export function useShouldAnimate(): boolean {"; "export function useEngineTimeline("; "export function EngineGauge({ at"; "export function Conduit({ edge"; "function LandingFlow({ d" | dashboard/src/panels/engine-room/useShouldAnimate.ts:12-12; dashboard/src/panels/engine-room/useShouldAnimate.ts:19-19; dashboard/src/panels/engine-room/useEngineTimeline.ts:168-168; dashboard/src/panels/engine-room/engines.tsx:136-136; dashboard/src/panels/engine-room/conduits.tsx:70-70; dashboard/src/panels/engine-room/conduits.tsx:139-139 |
| Left official-line engines + `officialWire` conduits + official coupler (from `workspaceEngines`). | `EnclosureCanvas` | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:42-93 |
| The `engineState` selector that derives each workspace engine's runtime. | `engineState` | dashboard/src/data/selectors.ts:123-127 |
| The bird's-eye recipes it renders with (incl. `engineSpine`/`enginePetal`/`officialWire`/`canopyStroke`/`laneFlag`). | `engineSpine`; `enginePetal`; `officialWire`; `canopyStroke`; `laneFlag` | dashboard/src/panels/engine-room/stage.styles.ts:151-167; dashboard/src/panels/engine-room/stage.styles.ts:171-177; dashboard/src/panels/engine-room/stage.styles.ts:194-194; dashboard/src/panels/engine-room/stage.styles.ts:199-207 |
| Projection types `EngineProcessEdge`/`EngineProcessNode`. | `EngineProcessEdge`; `EngineProcessNode` | dashboard/src/types/projection.ts:152-160; dashboard/src/types/projection.ts:162-202 |
| Projection types `CommitRefNode`/`ProviderBootNode`/`LandingRefNode`, and `ProviderNode`. | `CommitRefNode`; `ProviderBootNode`; `LandingRefNode`; `ProviderNode` | dashboard/src/types/projection.ts:121-129; dashboard/src/types/projection.ts:239-249; dashboard/src/types/projection.ts:328-333; dashboard/src/types/projection.ts:335-346 |
| 05o T3B — `checking`/`memGated` derivations + the `scanRing` `<circle data-fx="scan">` + `Conduit ghosted` (the `ghostedLane` inner-`<path>` ghost). | "flowConduit"; `EnclosureCanvas` | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:42-93; dashboard/src/panels/engine-room/conduits.tsx:70-136; dashboard/src/panels/engine-room/conduits.tsx:8-8 |
| The `scanRing` recipe is the full cyan stroked, transparent, glow style; `ghostedLane` is the full dim/desaturate style; `Conduit` applies `ghostedLane` to the inner path through `cx(flowConduit(...), ghosted && ghostedLane)`. | "export const scanRing = css({"; "export const ghostedLane = css({ opacity: \"0.32\", filter: \"grayscale(0.45)\" });" | dashboard/src/panels/engine-room/conduits.tsx:70-136; dashboard/src/panels/engine-room/flow.styles.ts:40-46; dashboard/src/panels/engine-room/flow.styles.ts:54-54; dashboard/src/panels/engine-room/conduits.tsx:8-8; dashboard/src/panels/engine-room/conduits.tsx:10-10 |
| The design prototype supplies the ported canopy bracket geometry, provider wire/flow links, and engine spine/petal decals: its canopy path, `wire`/`flow-g` links, provider geometry, and `.e-spine`/`.e-petal` recipes are present in the prototype. | "class=\"canopy\""; "M58 22 L22 22 L22 58"; "class=\"wire\" id=\"w-m-cgc\""; "class=\"flow-g\" id=\"flow-int-code\""; "id=\"m-cgc\" transform=\"translate(81,102)\""; ".prov .e-spine{stroke:var(--amber);stroke-width:.8;opacity:.28}"; ".prov .e-petal{stroke:var(--amber);stroke-width:1.4;opacity:0;stroke-linecap:round}" | dashboard/public/_proto/podstage.html:76-77; dashboard/public/_proto/podstage.html:186-186; dashboard/public/_proto/podstage.html:189-189; dashboard/public/_proto/podstage.html:208-208; dashboard/public/_proto/podstage.html:240-240; dashboard/public/_proto/podstage.html:270-270 |

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

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the responsibility split into engine-room sibling modules. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T13:15:12+02:00 — 260731-EFA-L6 S18-B02 curator: narrowed the column-geometry claim to its definitions, kept consumer sites in their own finding, and regenerated the final range with the scoped fixer.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: resolved both developer-owned semantic
  findings: column centres govern a scoped set of x geometry rather than every coordinate, and the
  current source-node label is `Integration line` with no `mainRef` helper. New ranges are explicit
  normalized by the scoped fixer.

- 2026-08-03T07:46:25+02:00 — 260731-EFA-L6 W3-B12 curator (same-reviewer row-384 ownership correction, developer residuals): resolved 46 of 50 manifest findings (40 table findings across 20 rows and 6 prose findings), preserved the two original substantive Tier-3 rows in the accepted pending-developer form, and retained the four honest residual diagnostics (two `citation_anchor_missing` and two `citation_source_malformed`). Corrected row 384 to the current three-argument `useEngineTimeline` ownership: the hook owns draw-on/retract selection, `buildFx` selects `data-fx` markers, `EngineFxOverlay` renders repeating surge/reindex/breath primitives, and Motion owns structural opacity/transform; rows 385, 391, 393, 400, and 401 remain corrected against current source truth. All 25 surviving numeric table rows retain fixer-generated final source ranges, and developer decisions remain required for rows 380 and 383.

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the two observer/projection.py citations — the reference row and the restatement in the 10:32 entry below. The current model definition, forbidden-extra configuration, kind vocabulary, state vocabulary, and detail field are cited in cit:([`EngineProcessEdge`], mcp/src/agents_remember/observer/projection.py:785-804); every named symbol is inside the generated range. No body claim changed.

- 2026-08-01T10:32+02:00 — 260731-EFA-L4 curator: corrected the `refusedPolarityOf` description, which claimed a third arm — "a `refused` lane → its explicit `edge.refusedPolarity` (default amber)" — that no longer exists and never could have fired. Verified: `EngineProcessEdge` declares no refusedPolarity field and its state vocabulary has no refused in cit:(["class EngineProcessEdge(BaseModel):"], mcp/src/agents_remember/observer/projection.py:791-791); `git log --all -S 'state="refused"'` returns zero commits ever. Also corrected the claim that Conduit carries data-refused-polarity; `RefusedConduit` stamps data-polarity/data-refused-polarity from the derived polarity in cit:(["export function refusedPolarityOf(edge: EngineProcessEdge)", "export function RefusedConduit("], dashboard/src/panels/engine-room/geometry.ts:124-134; dashboard/src/panels/engine-room/badges.tsx:265-281). The kept integration/integration-mem arms have their actual justification: integration is in the model's documented kind vocabulary and the lane is fixture-authored and test-covered, not forward-compatibility. Both reducer edge builders are checked in cit:(["def _process_edges(", "def _start_process_node(entry: dict[str"], mcp/src/agents_remember/observer/reducer_impl/_processes.py:122-122; mcp/src/agents_remember/observer/reducer_impl/_processes.py:539-539; mcp/src/agents_remember/observer/projection.py:785-785); neither emits either kind. The in-code comment now names both real builders; related useEngineTimeline and projection-type citation rows were repaired in their current cards.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: documented the sparse sibling
  `EngineFxOverlay`: animated surge/reindex/attention primitives move out of the text-heavy
  structural SVG only while effects are enabled; the effects-off/static canvas remains intact.
  Shared classes, view box, geometry, and timeline selectors preserve the existing visual
  choreography. Verification metadata remains pinned until closeout.

- 2026-07-24T13:17:17Z — Curator: documented full-geometry surge bands for transform-owned motion;
  verification fields remain pre-commit.

- 2026-07-12T17:30+02:00 — 260712-TRH-L7: stale landing facts now render with an explicit stale tone/state and age, and stale or missing facts are excluded from landing-flow motion so the UI remains visible but motion-inert while projection stays fresh.

- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: `runtimeState` now accepts `missing`, allowing expected provider slots to render as explicit missing gauges instead of disappearing or becoming generic unknown. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:09+02:00 — Engine Room leaf identity: the SVG root `aria-label` now names the selected leaf when `leafId` is present, keeping the canvas accessibility label aligned with the rail and header. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the official-line branch nodes no longer hardcode `main`; they render the projected integration/source branch, and the coupler prose now names the series contract rather than `contract.md`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T13:45+02:00 — Task 11: added optional `gateNode` prop and `data-gate-kind` on the SVG root,
  preserving the canvas as a visual scene while exposing projected gate identity for diagnostics/tests.
  Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-22T16:00 — slice 05o T14C review fix to `TerminalStop`: the terminal integration-conflict STOP no
  longer renders its conflict words ON the `integration` lane midpoint (the bright red conduit line bisected the
  on-lane glyphs → illegible). The reason now renders as a **legible banner** lifted clear into the band ABOVE
  the lane (`by = cy − 58`) using the SAME combo as the recoverable reason badges — the `reasonBadge` dark pill +
  red border + light `reasonText` — with the ⛔ no-entry glyph carrying the STOP identity. A compact red on-lane
  STOP **bar** (`stopBar`, `data-fx='stop'`) sized to the ~66px feat↔worktree gap (`x = cx − 33`, width 66) marks
  the conflict point WITHOUT colliding with the worktree node (the old 128px pill overran it). That bar carries
  `data-testid="terminal-stop-bar"` and NOT `data-testid="gate"` (terminal, not a recoverable `Gate`).
  Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T13:00 — slice 05o wired the six remaining failure modes (T7B provider-plan block · T9B/T9C/T14C
  refused-conduit flashes · T12B memory moved/sync), keeping the node-anchored + topmost-pointer +
  `alertProps`-transition doctrine. Added the shared helpers `conduitPathD(edge)` (one source of the lane
  path string — straight / clone-arc BOW) and `refusedPolarityOf(edge)` (`failed`→red, `stale`→amber,
  `refused`→`edge.refusedPolarity`, default amber, else null). New components: `RefusedConduit` (the one-shot
  `data-fx='refuse'` flash over each `refusedEdges` lane — `cgc-seed`/`grepai-clone`/`integration`/
  `integration-mem` — resting at opacity 0 so it is present-but-absent under effects-off) and `MovedBadge`
  (the soft cyan ▲ "moved" pill on the memory worktree node). New derivations off the projection:
  `providerPlanBlocked` / `providerChecking` / `providerScanAt` (T7B — per the dev directive the `ProviderBlock`
  component draws a VERTICAL alarm bar attached to the LEFT side of the worktree CGC provider engine slot + the
  reason badge on the enclosure's TOP edge + the `engineDropout` halos over the two UNLIT worktree engines; NOT
  a node gate on the code worktree), with `fleeting`
  **tightened to `&& !providerPlanBlocked`** so T7B never renders the big red `FleetingEnclosure`; `scanCenter`
  (`scanAt ?? providerScanAt`); `memMoved`/`movedAt` (the T12B soft notification) + `memSyncMoved` (the gate,
  **restricted to a blocked `ledger-map` edge** so the existing `engine-sync-needed` gallery fixture's blocked
  `sync` edge is untouched); `refusedEdges`; and an extended `blockNode` (T1B / T12B / T3B). The `Conduit`
  `ghosted` condition was broadened to `(memGated || memSyncMoved) && edge.kind === "ledger-map"`, and
  `Conduit` now carries `data-refused-polarity`. All the new overlays render in the TOPMOST layer.
  Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T12:00 — slice 05o T1B (stale-base block) + an indicator anchoring/z-order/transition pass: (1)
  `BranchNode` gained a `pruned` prop applying `prunedNode` to the stale code-base node, driven by
  `baseStale = codeSource.behindSource > 0 && isBlocked && fleeting` (the local `cx` node-centre **shadows**
  Panda's `cx`, so the pruned class is combined by hand). (2) The verify `scanRing` and the block gate +
  reason badge now anchor **ON the checked REPOSITORY NODE rectangle**, never the connector-lane midpoint —
  `scanAt` centres the scan on the node (code base `y=281` for T1B, memory base `y=403` for T3B) and a new
  `NodeBlock` component draws the steady gate bar at the node's top edge with the reason badge above it,
  driven by `baseChecking`/`memChecking` (verify) and `blockNode` (block). (3) Those node-anchored POINTERS
  (scan + `NodeBlock`) now render in the **TOPMOST overlay layer** (dead last in the SVG), because SVG paint
  order equals document order and painting a node-centred pointer before the node let the opaque rect cover
  it. (4) A fleeting born-blocked enclosure now renders the big red `FleetingEnclosure` box (podstage
  `.fbox`) over the worktree footprint (BLOCKED title + reason + recovery chips) and **suppresses the
  dashed-amber enclosure border** — replacing the HTML banner that used to live in `EnclosureProcessMap`. (5)
  A new `alertProps` helper + `AnimatePresence` give every failure overlay (gate, reason, attention, chips,
  terminal STOP, scan ring, the block pointer) a Motion fade + subtle scale-pop on ENTER/EXIT, gated by
  `useShouldAnimate` (instant end-state under effects-off). Verification metadata pinned until closeout stamps
  the 05o code commit.
- 2026-06-22T00:29 — slice 05o T3B (memory/ledger block): wired the two new failure primitives off the
  projection. Added `checking` (a `ledger-map` edge `running` + memory worktree not materialised → the cyan
  `scanRing` `<circle data-fx="scan">` at the ledger-map lane midpoint `COL_FEAT_CX,403`, gated on `animate`)
  and `memGated` (memory worktree `factState==="missing"` OR a `ledger-map` edge `blocked`), passing
  `ghosted={memGated && edge.kind==="ledger-map"}` into `Conduit` — which applies `ghostedLane` to its **inner
  `<path>`** (via `cx`, imported from `styled-system/css`) + sets `data-ghosted`, so the held memory lane
  dims+desaturates while the code lane stays solid. The steady `Gate`/`Attention`/`RecoveryChips` already
  cover the block. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T23:29 — layout + fill rework (four-part pass): (1) **second-cycle engine-fill fix** — removed the
  `booting`/CSS-`powerup` machinery; the charge rect's FILL is now owned 100% by the `engineCharge` CVA class
  (cyan `indexing` → mint `nominal`), never by Motion or a CSS animation, and the powerup is a one-shot Motion
  OPACITY pulse `[0.85,1,0.55]` reset via `onAnimationComplete` + a `booting`-keyed timer backstop — fixing the
  "engines stay green / never go cyan on the second loop" bug (stale CSS `forwards` fill-lock + an
  `onAnimationEnd` that never fired on a `motion.rect`). (2) **Column re-space** — three centre constants
  `COL_MAIN_CX=365 / COL_FEAT_CX=595 / COL_WT_CX=835`, with **every** dependent coordinate (POS x, both
  couplers, `REMOTE_POS`, `PR_CX`, `EDGE_GEOM`, the engine→node wires, the four `LandingFlow` paths, the
  enclosure border) derived from them — even ~72px middle-column gaps, chips on their column centrelines, clean
  vertical flow paths. (3) **Closeout train** relocated to a bottom-left breadcrumb (`x=260, y=600`, on the
  bottom gate-row baseline) with a legible caption. (4) **Memory integration arrow** — new
  `EDGE_GEOM["integration-mem"]` (y=403, worktree→feat mirror of `integration`) + the `Conduit` `isReplay`
  check widened to cover it. Same pass also added the `Conduit` `retiring` fade (worktree conduits → 0 at
  cleanup), the `LandingFlow` `FlowState` active/settled/hidden rework (`landingFlowState`, cyan-active /
  amber-settled), and the 5o predictive-boot read. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-21T09:57+02:00 — slice 05n: `Conduit`'s flow packet now carries its conduit path on `data-path`
  (no inline `style.offsetPath`) and renders only when `animate`, so `useEngineTimeline` rides it via GSAP
  MotionPath (F12 — restores the dead travelling dots). Dropped `pathLength={100}` from both draw paths
  (`Conduit` + `LandingFlow`) — DrawSVG owns the dasharray/offset and measures the real stroke length, so the
  hand-rolled normalization fought it. No render-structure change otherwise; the draw-replay fix + the DrawSVG
  migration itself live in `useEngineTimeline.ts`. Verification metadata pinned until closeout stamps the 05n commit.
- 2026-06-21T02:27+02:00 — slice 05k: split the canvas motion onto GSAP timelines + Motion (CSS static, `05f`
  §8). Wired `useEngineTimeline(rootRef, node)` to the `<svg>` root (one `gsap.context` owning the
  `[data-draw='on']` draw-ons + the `[data-fx=…]` repeating fx) and **removed the per-component `gsap.fromTo`/
  `gsap.context`** from `Conduit`/`LandingFlow` + the inline `pktRun` packet animation — components now just
  mark `data-draw`/`data-fx`. Converted every animated element to `motion.*` (Motion owns opacity/transform/
  `chargeMotion` scaleY/fill); wrapped the feat-tier source nodes + the landing dock in `AnimatePresence`
  (replacing the deleted `landingEnter` CSS atom; the closeout train keeps its). All gated by
  `useShouldAnimate` (no GSAP context/ticker + `initial={false}` under effects-off). Reads the new
  `engine-landing-pushed` D3 fixture like any landing arc. Verification metadata pinned until closeout stamps
  the 05k code commit.
- 2026-06-19T23:58+02:00 — slice 5i: the canvas became a moving build-up/tear-down stage. Added the motion
  substrate (GSAP `gsap.context` draw-on in `Conduit` + the new `LandingFlow`, keyed on `edge.state`/`show`,
  gated by `useShouldAnimate`; `AnimatePresence` enter/exit on the closeout train; the `sceneSvg` CSS
  transition easing frame-to-frame), the three-tier landing (`mainRef` always-`main` official line + the
  `featCode`/`featMemory` source tier shown during landing via `landingIn`), the build-up materialisation
  gates (`branchEnter`, `EngineGauge present`, `WarpCoupler visible`, `LaneFlag visible`, enclosure-border
  opacity, `detaching` drift), the cross-stage provider **clone arcs** (`cgc-seed`/`grepai-clone` official→worktree,
  transient) + the persistent `worktree-wire`, and reworked the remote/landing dock (`REMOTE_POS` positioned
  chips, `PrBadge` merge-arrow, `LandingFlows` push/pull/carry/push-mem) — removing `REMOTE_ORDER`/
  `remoteConnector(Carry)`/`prBadgeSub` and the `lane-landing-source` flag. The CSS-driven parts (`sceneSvg`
  transition, `landingIn`) are slice **05k**'s correction target. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-19T15:50+02:00 — slice 5h H4 cleanup teardown + landing-source fix: the `contract · historical` chip now fires on cleanup-pending too (`retiring`), plus a `lane-back-into-main` seam reading the resolved `origin-main` tip (`cleanupTip`). Fixed a related bug — `landingSource` now drops unresolved refs (`resolvedRef`: `factState:"missing"` / `state:"unknown"`) so a completed enclosure with a deleted source branch stops leaking a stale `▸ origin/feat · unknown` flag, and `LaneFlag` truncates its label (full text on hover) so it can't overflow. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T15:00+02:00 — slice 5h H3 readability + connectors (feedback): the chips were unreadably small (≈8px at the 0.76× canvas scale) with an overflowing two-line state — reworked to **branch-node-peer sizing** (a readable single label + one terse `remoteStateWord`, full detail on hover `<title>`) and **wired** the strip with `remoteConnector` (solid amber, code chain) + `remoteConnectorCarry` (dashed, carryover handoff), centring `remoteStripHeader` between the corner labels. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T08:49+02:00 — slice 5h H3: added the **remote/PR strip** beyond the official line — `RemoteStrip` + `RemoteChip` + `PrBadge` (+ the pure `remoteTone`), rendered when `node.landing?.length` in the governed D3→D4 order (origin-feat → PR → origin-main → origin-mem-main). Each ref is a state chip (planned=dashed/muted · live=amber · landed=mint); the PR badge flips open→merged; `origin-mem-main` stays dashed "after carryover" until the PR merges, then settles "carryover done" — the code-first/memory-after order legible in a single frozen frame. Only motion is the gated fill/stroke transition (frozen under data-effects=off). Consumes H1's `landing[]`; no projection change. Verification metadata pinned until closeout stamps the 5h H3 code commit.
- 2026-06-19T06:39+02:00 — engine-room crash fix: the `landingSource` read is now null-safe (`node.landing?.find`) — a projection produced before the slice-5h `landing` field omits it, which was crashing the scene on entry; it now degrades to no `lane-landing-source` flag. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:48+02:00 — slice 5h Tier 2 (frame extend + position, feedback): the expanded card grows **downward** and extends its frame to the available height (`ledgerScroll({ expanded })`) instead of upward into a short scroll box; the popover anchors **high in the scene** (a fixed invisible SVG `anchorRef`, `placement="bottom"`, `shouldFlip={false}`) so it keeps its old upper position rather than dropping down to the coupler. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2: `LedgerTable` rows are now the mirrored 6-column layout (`codeDate │ codeSubject │ codeHash ⇄ memHash │ memSubject │ memDate`); added `compactDate` (committer-ISO string-slice → `MM-DD HH:mm`, no Date/TZ conversion). Messages truncate (full in `title`); a row with no probed metadata keeps its hash with empty message/date cells (honest fallback). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover (both couplers): each `WarpCoupler` label is now a clickable `ledgerButton` opening a React-Aria popover (`LedgerTable`) over the memory.md lookup table — this enclosure's row highlighted, default-8 → "▾ show N more" → ≤25 scroll → "+N more in memory.md"; worktree coupler from `node.ledgerRows`, official coupler from the new `officialLedger` prop. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:50+02:00 — slice 5h cleanup pass (feedback): conduit wiring tightened — `markerEnd` chevron only on a `running` flow (action), the `er-chev` `refX` moved to the chevron's visual tip so the arrowhead lands on the line end (no overshoot into the engine), provider conduits wired box-edge-midpoint → engine inner corner (+ mirrored `officialWire`s), symmetric `enginePetal` flanks, and the `sync` lane made collinear with `worktree-add` (one centred line, not an off-centre double). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T13:01+02:00 — slice 5h coupler fix: `WarpCoupler` re-framed as the memory.md ledger link (not the task contract) — a drawn `warpLinkGlyph` chain-link + a `short(code) ⇄ short(memory)` label per coupler (via the new `short` helper) + bound-only `warp-surge` bands. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T11:55+02:00 — slice 5h H2: added the landing-arc render — a `CloseoutTrain` (T13 derived closeout-order strip on closeout-pending), `Conduit` gained an `integrationStrategy` prop bending the `integration` lane for `replay` (T14b) vs straight `ff-only` (T14), and a `lane-landing-source` flag advancing the official line to its `landing[]` source tip. Verification metadata pinned until closeout stamps the 5h H2 code commit.
- 2026-06-17T22:45 — engine-room visual-parity pass: restored the prototype's SVG decal layer above the G6
  backdrop. `EnclosureCanvas` gains a `workspaceEngines` prop and renders the **left official-line engines**
  (`ENGINE.mcgc`/`mgrep`, runtime via `engineState`) with `officialWire` conduits + an `OFFICIAL_COUPLER_X`
  coupler; `WarpCoupler` is parameterized by `x`/`label`/`testid`; `EngineGauge` gains the `engineSpine` +
  six `enginePetal` flank lines; `CanopyFrame` (bevel rim + corner brackets + edge ticks) and `LaneFlag`
  (`ledger ▸ maps merge` / `contract · historical`) are added. Corrected the prior "official-line engines are
  out of scope" boundary — they now render here. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-17T16:15 — slice 5g G5 + engine palette: added the `integration` return-lane geometry + a
  `TerminalStop` (the t14c terminal conflict STOP — replaces the `Gate` and suppresses recovery chips when
  `phase === "integration-blocked"`); the reindex gauge now uses the amber `engineReindexOut` outer (was the
  nominal stroke) so a rerouting engine reads amber, not the new green. Engine `nominal` is now green
  (active); the t18 abandon dissolve lives in `EnclosureProcessMap`. Verification metadata pinned until
  closeout stamps the G5 code commit.
- 2026-06-17T15:00 — slice 5g G4: a `down` provider's `EngineGauge` flickers (the isolated fault — the
  steady `Gate` is now blocked-edges-only); `reindex` prop renders the amber reindex pulse (`seedFallback`);
  the reason badge anchors beside a faulting engine when there's no blocked lane; `retryArgs` adds a retry
  chip; `BranchNode` truncates the branch to the box + a `<title>` with the full string. Verification
  metadata pinned until closeout stamps the G4 code commit.
- 2026-06-17T14:00 — slice 5g G3: added the failure overlays — `Gate` (steady red bar at a blocked/failed
  edge's midpoint), `Attention` (breathing alarm parity), `ReasonBadge` (local cyan-dot reason pill), and
  `RecoveryChips`; a fleeting pre-contract block defers the scene gate to the `FleetingBanner`. Verification
  metadata pinned until closeout stamps the G3 code commit.
- 2026-06-17T13:30 — slice 5g G2: `Conduit` now wraps its `<path>` (`pathLength=100` for the draw-on) in a
  `<g>` and renders a `flowPacket` `<circle>` (offset-path = the conduit path) on running edges; the
  center-out charge + conduit colour fidelity ride on the recipes. Verification metadata pinned until
  closeout stamps the G2 code commit.
- 2026-06-17T12:47 — Created for slice 5g G1: the Engine Room bird's-eye — the live `EngineProcessNode`
  rendered as the prototype's two-world canvas (branch nodes, podracer engine gauges, warp coupler, flow
  conduits), extracted from `EnclosureProcessMap`. Static frame; choreography is G2+. Verification metadata
  pinned until closeout stamps the G1 code commit.
