# dashboard/src/panels/session-cockpit/ — Sessions Cockpit Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/session-cockpit/`          |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-17T06:20+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src/panels overview](../overview.md)

## Purpose

`session-cockpit/` is the **Sessions cockpit view** (260715-FEUI-L1, the react-tui-cockpit series
foundation leaf): the terminal-first sessions surface registered as the last mode-bar view. It is a
full-bleed, **keep-alive** view — `Cockpit.tsx` mounts it once as a persistent CSS-hidden layer
(the Chats pattern, `sessionsLayer = chatsLayer`) so the future xterm buffers + WebSockets (L6)
survive view switches; `active={view === "sessions"}` gates the window-level key bindings so the
hidden layer never grabs keys. The view root carries **`[data-view="sessions"]`** — simultaneously
the WebTUI scope root (S1, `styles/webtui.css` + the build-time prefixer) and the keyboard layer's
home. L1 shipped the SHELL: a react-resizable-panels rail/stage/inspector group with the
narrow-width rules and the ~80-col floor chip (S2), the cmdk command palette over the extensible
registry (S3), and the tinykeys keyboard-zone/focus wiring (S4). **260715-FEUI-L2 fills the
panels**: the rail hosts `SessionRail` — the RULED role-driven hierarchy (flat command spine,
per-leaf clusters with the active seat on top, per-master completed folders + bulk end) plus fleet
attention, gate/brief markers, poll-health banner, and the bus footer; the stage hosts the
`SessionStage` container + `HeaderStrip` (identity → EMPTY ModelEffortControl slot → grammar
state → leaf/seat → diagnostics; reserved WorkingLine slot); the inspector hosts the read-only
`SeatInspector` provenance card; and `StateDot` renders the ONE seat-state grammar
(`data/stateGrammar.ts` — 2.4 s ease-in-out pulse, never steps()). **260715-FEUI-L6 fills the
stage surface and the lifecycle actions**: `PtySurface` renders keep-alive real xterm panes
(DOM renderer BY MEASUREMENT, two server-truth archetypes — controlled line-log vs legacy raw),
`WorkingLine` is the single home of turn theater in the stage's reserved slot, `InteractionBar`
is the ONE structured-interaction axis (gate-channel answers only — never a terminal write),
`StopResidualNotes` renders informational stop residuals, and `lifecycleCopy.ts` centralizes
every lifecycle/interaction copy string (honest terminate confirms naming session · leaf · state).
**260715-FEUI-L3 adds the launch layer**: the palette-opened `LaunchFlow` overlay dialog
(capability-catalog-driven model/effort launch under the BOTH-knobs-or-NEITHER rule, uniform
fail-loud response paths incl. both 409s and the F9 outcome-unknown reconciliation), the
`FailedLaunchBanner` for focused failed seats (verbatim bridgeError, Retire + 'Launch
corrected…', no auto-retry), and launch-evidence tiers derived from row control-state truth
(`data/launchEvidence.launchTier`) rendered by `grammar/EvidenceBadge` in the header provenance
chip and the inspector. Remaining scaffolding: L4 the controls, L5 the real composer (CM6) +
queue, L7 the tabbed inspector/status line. All pure derivations live in `data/` (`railModel`,
`stateGrammar`, `catalogPoll`, `seatEvents`, `sessionCockpitStore`, the L6
`interactionAnswer`/`sessionLifecycle`/`ptyHarvest`, and the L3
`capabilityCatalog`/`launchEvidence`/`launchFlow`); this route holds DOM + wiring only.

## Route Model

- `SessionsView.tsx` — the view shell + the L2 derivation seam. Root = the scope/testid/marker
  carrier (`sessions--view`, `data-view="sessions"`). A `PanelGroup`
  (`autoSaveId="cockpit.sessions.panels"`) of rail (collapsible, ~280px target via a one-shot
  percentage calibration) / stage (min 35%) / inspector (24%, collapsible), a status-line footer
  with reopen buttons, the non-portal `CommandPalette`, and the `useKeyboardZones` binding. Owns
  the command registry instance + the `CommandContext` actions (panel toggles, focus moves, the
  LIVE alt+↑/↓ `switchSession` over `railCycleOrder`, honest L4/L5 stubs), the narrow-width
  auto-collapse (pure decisions in `data/sessionLayout.ts`), the ~80-col floor chip re-measured
  from every width-changing path (`onLayout` + a stage-observing `ResizeObserver`), and — L2 —
  the shared poll-driver/mirror subscriptions, the ONCE-derived rail model + attention rollup
  (shared between rail and palette), R9 smart-default focus + F17 reason-bearing focus handoff,
  the one-way layout/palette store mirrors, and the dynamic palette commands (tree toggle,
  attention.jump, bulk-end mirrors with counts+names in the title, question triage). **L6 fills
  the stage body**: `StopResidualNotes` + `PtySurface` (or the explained placeholder for the
  EMPTY stage only) + `InteractionBar` directly above the still-L5-placeholder composer; the
  floor chip now prefers the pane's REAL column count (`pane N cols (< 80)`) over the pixel
  estimate; the `workingLine` prop fills the stage slot; `turn.stop` joins the palette gated on
  the WorkingLine's OWN grammar predicate (`seatVisualState().key === "working"`) with the
  honest "unavailable: interrupt requires UA-7" title; triage now focuses the bar in place; and
  `startRetireResidualSweep()` is mounted beside the cockpit mirror (residual capture is
  data-layer, focus-independent — fix round F1). L3 appends (pure inserts, no L1/L2 node
  reshaped): the `session.launch` palette command + `launch` state, the `FailedLaunchBanner`
  block for any focused failed seat (above the pty surface), and the `<LaunchFlow>` overlay
  mounted after the palette.
- `SessionRail.tsx` (L2) — the rail renderer over `data/railModel`: ruled row anatomy (dot ·
  role(3) · title · attention-slot · status · End; only the status chip elides, truth in the row
  tooltip), flat spine, hairline-indented leaf clusters (active seat on top), per-master
  collapsed completed folders, master+sprint bulk end with honest NAMING previews, the
  zero-state-suppressed attention strip with live-derived highlight expiry, gate badges +
  two-state brief markers in the reserved attention-marker slot, the poll-stale banner, the
  anchored bus footer, and the spawn-edge provenance tree toggle. **L6**: the End action is an
  arm→confirm→execute flow whose confirm NAMES session · leaf · state (arming never kills); a
  FAILED terminate POST renders the server's words verbatim inline (`role="alert"`) with
  retry + dismiss — never a silent disarm; the landed-cleanup route's own outcome (closed +
  skipped with reasons) renders after bulk end; legacy-raw bell → attention marker with a text
  equivalent (cleared by focusing the seat); OSC title/turn HINTS join the row tooltip clearly
  labeled — never the grammar dot.
- `PtySurface.tsx` (L6) — the keep-alive PTY stage surface: mirrors Chats' mountedIds /
  display:none / aria-hidden layer idiom (prune on tombstone only — scrollback survives focus
  switches), lazy-loads the SAME `panels/Terminal.tsx`, renders the two archetypes off server
  truth (`isControlledSession`; harvesting hooks wired ONLY for legacy raw), holds the measured
  `PTY_RENDERER = "dom"` decision record (webgl = lazy escalation path), the reserved EMPTY
  `scrollback — paused` badge slot, the reserved-chord filter (filters ONLY bound reserved
  chords; Ctrl+Shift+C passes to the harness), the persisted per-pane screen-reader-mode toggle
  (applied live, cost named), bell acknowledge-on-focus, and the real-cols wiring for the floor
  chip.
- `InteractionBar.tsx` (L6) — the ONE interaction axis, rendered above the composer (never
  replacing it): kind-aware (choices→buttons, no-choices→composer answer-mode, no
  interactionId→honest "unrepresentable" pointing at the inspector's verbatim payload); the
  SOLE answer path is the landed gate channel (`data/interactionAnswer.ts` →
  `POST /api/actions/approve`, answer as decision note — ZERO terminal writes); store-backed
  round trip (`answering…` → verbatim error + retry with the SAME answer → "answered — waiting"
  poll-bounded copy); always-present honesty hint; never steals focus, returns focus to the
  invoker; `role="alert"` announce.
- `WorkingLine.tsx` (L6) — the SINGLE home of turn theater, mounted into the stage's reserved
  slot: renders ONLY while `seatVisualState(session).key === "working"`; real activity form when
  known else plain "working" (typed seam — never whimsy); `~`-labeled tabular-nums elapsed from
  L2's client turnClock (omitted when unobserved); the stop control WELDED at the fixed end
  position, disabled with the stated UA-7 reason; the slow-pulse `◐` glyph pinned to the ruled
  `pulseSlow 2.4s ease-in-out infinite` literal. No turn theater renders per rail row.
- `StopResidualNotes.tsx` (L6) — dismissable INFORMATIONAL `role="status"` residual lines on the
  stage (control-stop details from terminate responses + retire-time stop errors, fed by
  `data/sessionLifecycle.ts`'s notice store); never auto-dropped, never styled as failure.
- `lifecycleCopy.ts` (L6) — the ONE lifecycle/interaction copy module: terminate confirm
  (session · leaf · state), cleanup-outcome lines, "(informational)" residual copy, answered /
  honesty-hint / stop-disabled-reason strings, `paneAccessibleName` (label + harness + state),
  `isControlledSession` (the archetype switch off the server's `controlState`), and the
  screen-reader-mode cost note.
- `SessionStage.tsx` + `HeaderStrip.tsx` (L2) — the stage container's RULED layer order
  (HeaderStrip → `data-slot="working-line"` — FILLED by L6 via the additive `workingLine` prop →
  surface → composer; explained empty identity, F17 handoff note; the empty-state copy points at
  the palette's "Launch session…" command) and the §1.2 header anatomy (identity → EMPTY
  `data-slot="model-effort-control"` for L4 → grammar state → leaf/seat → diagnostics-first
  elision; honest `ws —`/quiet freshness). L3 (R7): the provenance chip's tier is DERIVED from
  row control-state truth via `data/launchEvidence.launchTier(session)` — not the L2 store
  default — and renders a `grammar/EvidenceBadge` (`size="sm"`) beside the requested pair.
- `LaunchFlow.tsx` (L3) — the launch overlay dialog (non-portal, in-scope-root, the palette's
  posture), opened by the `session.launch` palette command: harness list from
  `GET /api/harnesses` (detected-gating; the adapter `control` word rendered visibly in the
  button), models/efforts EXCLUSIVELY from the live capability envelope (`data/capabilityCatalog`
  — zero options before the daemon answers; hidden rows excluded; non-selectable rows disabled
  with the catalog's own fact), explicit vendor-defaults option (sends NEITHER knob), effortless
  models honestly pairless, efforts in advertised order with zero emphasis, R2 miss-cost copy on
  loading/refresh, verbatim capability-route errors with retry, and the full R5 response fan
  (200 → pending-tier evidence + focus; 400/409s verbatim; transport/unrecognized → F9
  outcome-unknown with catalog reconciliation by the caller-minted id, watch gated on `open`,
  dismiss clears the watch — never a blind re-POST).
- `FailedLaunchBanner.tsx` (L3, R6) — the uniform starting→failed surface for a focused failed
  seat: the sweep-projected `bridgeError` VERBATIM (non-string shapes serialized, absence stated,
  never reworded), the refused pair labeled "requested provenance — never validated" beside an
  EvidenceBadge 'refused', and actions exactly Retire (armed inline confirm naming session label
  + leaf; the operator `/terminate` route — see the upstream actor-identity ask) and 'Launch
  corrected…' (prefill from the refused pair, only where still advertised). NO timer, NO
  auto-retry; the row stays visible until retired.
- `StateDot.tsx` (L2) — the ONLY renderer of `data/stateGrammar` visuals (rail + header +
  inspector; StatusLine joins in L7); Panda-literal 2.4 s ease-in-out pulse pinned to
  `PULSE_ANIMATION`, steady under reduced motion, frozen by effects-off.
- `SeatInspector.tsx` (L2, extended by L6) — the read-only provenance card in the inspector pane
  (spawn role/level/requested pair at its honest tier, spawned-by, landed/retired reasons,
  liveness evidence; L6 adds the pane archetype line, retire stop-error residuals for retired
  rows, and the VERBATIM raw interaction payload the unrepresentable-interaction notice points
  at); replaced by the L7 tabbed inspector. L3: the tier is the same `launchTier(session)`
  derivation as the header, plus the honest "vendor defaults — no selection sent" model fact
  for pairless harness rows.
- `CommandPalette.tsx` — the cmdk palette, deliberately **not a portal** (the overlay stays inside
  the scope root; focus return stays local). Two pages: `commands` renders the live registry (the
  one options source); `keys` renders the SAME chord tables tinykeys binds (`data/keymap`), so the
  `?` reference can never drift from the real bindings. Backspace-on-empty returns to commands.
- `useKeyboardZones.ts` — the thin React binding: tinykeys at the window, capture phase, default
  ignore disabled (the zone contract owns suppression), one composed handler per chord string, all
  routing decisions deferred to `data/keymap`.
- `SessionsView.test.tsx` — end-to-end jsdom coverage: zones resolved from real DOM markers,
  tinykeys at the window, palette pages, F6 cycle, PTY non-interception via preventDefault
  observation, floor-chip re-measure paths, and rail calibration; +3 L2 integration cases (R9
  entry focus, F17 handoff, alt+↑/↓ cycling) — all 21 L1 cases pass against the real rail/stage;
  + the L6 block (bar above the composer never replacing it, `turn.stop` gating on the
  WorkingLine's own grammar incl. the disappearance case, the UNFOCUSED retire residual, the
  real surface carrying the `data-kbzone="pty"` contract). xterm stays OUT of jsdom
  (`vi.mock("../Terminal")` here and in `PtySurface.test.tsx`); +2 L3 integration cases (the
  banner on the FLEET failed scout; corrected-launch opens the flow pre-selected).
- `SessionRail.test.tsx` + `HeaderStrip.test.tsx` (L2) — the jsdom rail-state matrix (every
  fixture row's dot ≡ grammar), the anatomy-order and model-leakage DOM negatives, hierarchy /
  attention / joins / completed-folder / bulk-end / footer-honesty coverage, the cross-surface
  dot consistency case, and the HeaderStrip/SessionStage anatomy + honesty cases — over the
  shared `test/fixtures/catalogRows.ts` FLEET; + the L6 rail block (arm/confirm never kills,
  verbatim terminate failure + retry, cleanup outcome, bell marker/tooltip hints, dot purity).
  L3 rewrote the HeaderStrip R7 provenance assertion onto a purpose-built claude/ready row
  (derived `(model-validated)` + badge) and added the starting→`(requested)`/pending pin.
- `PtySurface.test.tsx` + `InteractionBar.test.tsx` + `WorkingLine.test.tsx` +
  `SeatInspector.test.tsx` (L6) — the jsdom suites over the L6_* fixtures: archetype hook
  presence, keep-alive layers, badge slot, chord filter, accessible names; the 13 InteractionBar
  cases (exact URL+body, verbatim failure + same-answer retry, in-flight disable, no blind POST,
  focus both ways, stale-answered clear); the WorkingLine state matrix (working-only render,
  UA-7-disabled stop, no whimsy, elapsed omission, pulse literal pin); the inspector
  residual/provenance/raw-payload cases (residual copy never says "fail").
- `LaunchFlow.test.tsx` + `FailedLaunchBanner.test.tsx` (L3) — the launch jsdom suites: the
  gated-promise dynamic-only proof (ZERO options pre-answer), re-gate on model switch,
  explicit-choice gating, advertised order, effortless honesty, vendor-defaults wire ABSENCE,
  verbatim error + retry, the full R5 response fan (incl. both 409s and the
  transport-then-row-appears reconciliation + dismiss-ends-watch regressions), visible adapter
  status; banner verbatim ×3 harnesses, refused-not-validated label, prefill, honest confirm +
  single terminate POST, decline sends nothing, absent bridgeError stated.

## Invariants And Boundaries

- **`[data-view="sessions"]` stays on the view root** — it is the WebTUI scope; nothing outside it
  may receive WebTUI styling, and the palette overlay must stay inside it.
- **The view is never unmounted** — `Cockpit.tsx` owns the keep-alive layer; this route must stay
  mount-once-safe (no mount-time effects that assume visibility; a 0-width measure of the hidden
  layer is ignored, never acted on).
- **Pure logic lives in `data/`** — the registry (`data/commands.ts`), the layout decisions
  (`data/sessionLayout.ts`), and the whole keymap contract (`data/keymap/`) are React- and
  xterm-free; this route holds only DOM composition and wiring. L6's xterm
  `attachCustomKeyEventHandler` must consume `data/keymap/reserved.matchReservedChord`, not a copy.
- `data-kbzone` markers define keyboard-zone ownership; `data-region`/`data-focus-target`/
  `data-stage-header` define the focus model. Later leaves fill panels WITHOUT moving these
  markers (L2 kept them all).
- **One grammar, one renderer** (L2, R14): every seat state visual comes from
  `data/stateGrammar.ts` through `StateDot`; no surface derives its own words/colors/pulse. The
  only animation added is the RULED 2.4 s ease-in-out `pulseSlow` (never steps()) — frozen by
  `html[data-effects="off"]` and steady under reduced motion.
- **Honesty invariants** (L2): the rail never shows model/effort (R6 — DOM-negative-tested);
  requested pairs read "(requested)" until the evidence tier proves better (R7); freshness is
  absent (`ws —`) rather than faked (R15); the brief column is strictly two-state (R8); the
  attention strip renders NOTHING at zero state (R12); bulk end always NAMES what it removes
  (R17); the bus footer states "supervisor has not ticked" rather than faking numbers.
- **Open developer ruling** (review sev-3): the status-chip vocabulary renders the real catalog
  words `stale`/`exited`/`retired`/`starting` beyond the closed six-word §1.6b list — honest
  mirroring kept pending the developer's call; the one-switch remap point is
  `data/stateGrammar.ts`.
- **L6 honesty invariants**: ONE answer path — every structured-interaction answer rides the
  landed gate channel (`POST /api/actions/approve`, answer as decision note); NOTHING in the
  answer path writes to a terminal. Two archetypes derive from server truth
  (`controlState !== undefined && !== "unsupported"`), never a heuristic; harvesting
  (`data/ptyHarvest.ts` — bell, OSC 0/2 title, OSC 133/9;4 turn hints) is client-side,
  observe-only, and wired ONLY for legacy-raw panes. Stop residuals are INFORMATIONAL
  (`role="status"`, "(informational)", the word "fail" never appears) and are never silently
  discarded — capture is data-layer and focus-independent. Retire is NOT an operator action from
  the cockpit (the route requires an authorized actor SEAT the dashboard doesn't have) — the
  cockpit terminates with the honest confirm and RENDERS retirement. The renderer decision is
  BY MEASUREMENT: `PTY_RENDERER = "dom"` holds a locked 60 Hz budget at 12 concurrent line-log
  panes (headless webgl rows were SwiftShader software GL — caveat recorded in the code); webgl
  stays a lazy escalation path with DOM fallback. Screen-reader mode is a prominent per-pane
  opt-in with its cost named, applied live without teardown; every pane carries an accessible
  name (label + harness + state).
- **Launch honesty invariants** (L3): the flow is DYNAMIC-ONLY — zero model/effort options
  before the daemon answers, no fallback catalog anywhere, the envelope is dropped (not staled)
  on any capability error; the launch selection is BOTH knobs or NEITHER (a partial pair is
  unrepresentable — `data/launchFlow.launchSelectionBody` throws); every capability/open error
  and every `bridgeError` renders VERBATIM (never reworded, absence stated); failed rows are
  never hidden and never auto-retried; evidence tiers come only from
  `data/launchEvidence.launchTier` over row control-state truth — a Claude launch pair can NEVER
  read `readback` (no launch-effort echo), and nothing promotes without proof.
- **Retire from the banner = the operator `/terminate` route** (reviewer-accepted): a true
  provenance-recording `/retire` needs an `actor_session` identity the dashboard operator does
  not have — an upstream decision, recorded as an ask, not a defect.

## Hot Path Summary

The Sessions cockpit view: a keep-alive full-bleed rail/stage/inspector panel group under the
`[data-view="sessions"]` WebTUI scope root — the rail renders the ruled role hierarchy (flat
spine, active-first leaf clusters, completed folders + naming bulk end) with fleet attention, one
shared state grammar (2.4 s ease-in-out dot pulse, blocked-on-human steady), and an honest
arm→confirm End flow (verbatim failure + retry); the stage renders the HeaderStrip, the
WorkingLine turn theater (working-only, welded UA-7-gated stop), keep-alive real xterm panes
through PtySurface (DOM renderer by measurement, controlled vs legacy-raw archetypes, per-pane
screen-reader opt-in, real-cols floor chip), informational stop-residual notes, and the
InteractionBar above the composer whose ONLY answer path is the gate channel; the inspector a
read-only provenance card (+ archetype, retire residuals, verbatim raw payloads); narrow widths
auto-collapse on threshold crossings (reopenable), ctrl+k/ctrl+; open the cmdk palette (attention
jump, bulk-end mirrors, question triage focusing the bar, grammar-gated turn.stop), alt+↑/↓
cycles the rail order, F6 cycles regions, and the PTY zone passes every key through except
exactly the bound reserved set (clipboard chords stay reserved-unbound). "Launch session…"
(palette) opens the L3 LaunchFlow overlay — pick a detected harness, then a model/effort pair
exclusively from the live capability envelope (or explicit vendor defaults), POST the
both-or-neither selection, and land on the new row at tier 'pending'; a failed seat surfaces the
FailedLaunchBanner (verbatim refusal, Retire / Launch corrected…), and the header/inspector wear
the derived evidence tier through EvidenceBadge.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The shell that registers the view + owns the keep-alive hidden layer and `active` gating. | [cockpit/Cockpit.tsx](agents-remember/dashboard/src/cockpit/Cockpit.tsx) |
| The pure command registry + default command set the palette and chords dispatch into. | [data/commands.ts](agents-remember/dashboard/src/data/commands.ts) |
| The pure narrow-width/floor/calibration decisions the shell feeds measured widths into. | [data/sessionLayout.ts](agents-remember/dashboard/src/data/sessionLayout.ts) |
| The pure keyboard contract (reserved set, zones, chords, focus cycle) this route binds. | [data/keymap/](agents-remember/dashboard/src/data/keymap/reserved.ts) |
| The one WebTUI mapping file scoped to this route's view root. | [styles/webtui.css](agents-remember/dashboard/src/styles/webtui.css) |
| The pure rail/attention/focus/join derivations the L2 surfaces render. | [data/railModel.ts](agents-remember/dashboard/src/data/railModel.ts) |
| The one seat-state grammar + pulse ruling behind every dot. | [data/stateGrammar.ts](agents-remember/dashboard/src/data/stateGrammar.ts) |
| The cockpit client store (focus, evidence tiers, freshness, poll health, toggle). | [data/sessionCockpitStore.ts](agents-remember/dashboard/src/data/sessionCockpitStore.ts) |
| The shared poll driver + seat-event reconciler feeding this view's rows. | [data/catalogPoll.ts](agents-remember/dashboard/src/data/catalogPoll.ts) |
| The full catalog wire mirror the rows are typed by. | [types/terminalCatalog.ts](agents-remember/dashboard/src/types/terminalCatalog.ts) |
| The gate-channel answer path (find gate, kind-awareness, NOT-YET vs CANNOT copy). | [data/interactionAnswer.ts](agents-remember/dashboard/src/data/interactionAnswer.ts) |
| Terminate/landed-cleanup detailed helpers, the residual notice store, the retire sweep. | [data/sessionLifecycle.ts](agents-remember/dashboard/src/data/sessionLifecycle.ts) |
| The client-side legacy-raw harvesting store + pure OSC parsers. | [data/ptyHarvest.ts](agents-remember/dashboard/src/data/ptyHarvest.ts) |
| The one xterm component PtySurface lazy-loads (fit rules, renderer seam, named landmark). | [panels/Terminal.tsx](agents-remember/dashboard/src/panels/Terminal.tsx) |
| The in-repo renderer measurement harness behind the DOM decision (/dev/pty-bench). | [dev/PtyRenderBench.tsx](agents-remember/dashboard/src/dev/PtyRenderBench.tsx) |
| The memory-only capability-envelope store the flow's options come from (L3). | [data/capabilityCatalog.ts](agents-remember/dashboard/src/data/capabilityCatalog.ts) |
| The pure launch machines + classifying open client behind the flow (L3). | [data/launchFlow.ts](agents-remember/dashboard/src/data/launchFlow.ts) |
| The pure launch-evidence tier machine the header/inspector derive from (L3). | [data/launchEvidence.ts](agents-remember/dashboard/src/data/launchEvidence.ts) |
| The five-glyph tier badge rendered in the provenance chip, inspector, and banner (L3). | [grammar/EvidenceBadge.tsx](agents-remember/dashboard/src/grammar/EvidenceBadge.tsx) |
| The capability-envelope wire mirror (`CapabilityCatalogResult.to_json()`) (L3). | [types/harnessCapabilities.ts](agents-remember/dashboard/src/types/harnessCapabilities.ts) |

## Update History
- 2026-07-17T06:20+02:00 — 260715-FEUI-L3 (capability catalog client and launch flow; review
  FINAL PASS after two fix rounds): the route gains `LaunchFlow` (the palette-opened
  catalog-driven launch overlay) and `FailedLaunchBanner` (+ their jsdom suites); `SessionsView`
  registers `session.launch`, mounts the banner for focused failed seats and the flow after the
  palette (pure appends); `HeaderStrip`/`SeatInspector` derive the R7 evidence tier from row
  control-state truth via `data/launchEvidence.launchTier` and render `grammar/EvidenceBadge`;
  `SessionStage`'s empty-state copy points at the palette launcher. Pure logic landed at `data/`
  (`capabilityCatalog`, `launchEvidence`, `launchFlow`) with wire mirrors at
  `types/{harnessCapabilities,terminalOpen}.ts` — see the `dashboard/src/` overview. Upstream
  ask recorded: an operator retire actor identity if provenance-recording retire is wanted from
  the dashboard. Verification metadata pinned to the leaf base until closeout stamps the L3 code
  commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (PTY stage surface, structured interactions, session
  lifecycle actions; review FINAL PASS after a 1×sev-3 + 5×sev-4 fix round, all CLOSED): the
  route gains `PtySurface`, `InteractionBar`, `WorkingLine`, `StopResidualNotes`,
  `lifecycleCopy.ts` (+ the PtySurface/InteractionBar/WorkingLine/SeatInspector jsdom suites);
  the stage body is filled (keep-alive real xterm panes, two server-truth archetypes, gate-only
  interaction answers, informational stop residuals), the rail gains the honest End
  arm→confirm flow with verbatim failure + retry, cleanup outcomes, and bell/hint markers, and
  the reserved WorkingLine slot is filled. Renderer decision by measurement: `PTY_RENDERER =
  "dom"` (12-pane 60 Hz lock; headless webgl rows are SwiftShader software GL — caveat
  recorded; webgl kept as lazy escalation). Retire stays render-only (no actor seat in the
  dashboard — upstream ask recorded); gates on lifecycle-less seats are honestly unanswerable
  (gate-id-only projection = upstream ask). Pure logic landed at `data/` (`interactionAnswer`,
  `sessionLifecycle`, `ptyHarvest`) — see the `dashboard/src/` overview. Verification metadata
  pinned to the leaf base until closeout stamps the L6 code commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 (session data layer, rail, and stage container; review
  FINAL PASS after a 5×sev-4 fix round): the route gains `SessionRail`, `SessionStage`,
  `HeaderStrip`, `StateDot`, and `SeatInspector` (+ the `SessionRail`/`HeaderStrip` jsdom suites),
  and `SessionsView` becomes the derivation seam (once-derived model/rollup, smart-default focus +
  handoff, dynamic palette commands, live alt+↑/↓). Pure logic landed at `data/` (`railModel`,
  `stateGrammar`, `catalogPoll`, `seatEvents`, `sessionCockpitStore`) — see the `dashboard/src/`
  overview. One open sev-3 developer ruling: chip vocabulary width
  (`stale`/`exited`/`retired`/`starting` beyond the closed six-word list, honest mirror kept).
  Verification metadata pinned to the leaf base until closeout stamps the L2 code commit.
- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 (view shell, WebTUI spike, keyboard/palette
  foundation): the new `panels/session-cockpit/` child route — SessionsView (rail/stage/inspector
  PanelGroup + narrow rules + ~80-col floor chip + one-shot ~280px rail calibration),
  CommandPalette (cmdk, non-portal, commands/keys pages), useKeyboardZones (tinykeys binding over
  `data/keymap`), and the end-to-end jsdom suite. Includes the review round-2 fixes (floor chip
  re-measured via `onLayout` + stage observation; rail percentage calibration). Verification
  metadata pinned to the task base until closeout stamps the L1 code commit.
