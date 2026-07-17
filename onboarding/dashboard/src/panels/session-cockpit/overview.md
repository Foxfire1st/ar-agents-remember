# dashboard/src/panels/session-cockpit/ — Sessions Cockpit Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/session-cockpit/`          |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176`       |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
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
`SessionStage` container + `HeaderStrip` (identity → live ModelEffortControl → grammar state →
leaf/seat → diagnostics; reserved WorkingLine slot); the inspector is now the accessible
Evidence / Capabilities / Bus tab host; and `StateDot` renders the ONE seat-state grammar
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
chip and the inspector. **260715-FEUI-L4 fills live set controls**: exact-session capability
snapshots supply model rows and per-model session-settable effort menus; requested, pending,
echo-evidenced effective, and readback-confirmed values remain distinct through the five-value
SetResult table; pair changes serialize model → evidence/readback → effort; and shared chips,
ledger/rail attention, background toasts, cycle-effort commands, and polite/assertive live regions
surface the result without color-only meaning. **260715-FEUI-L5 fills the real controlled-session
composer**: shared CodeMirror Markdown editing, epoch-bound whole-message submit/reconcile, one
evidence fold, `QueuePreview`, authoritative Alt+Up withdrawal/pop-back, and revision-safe recovery.
**260715-FEUI-L7 completes the inspector/status integration**: an accessible stable-mounted
three-tab inspector separates the full evidence audit, exact-session capabilities, and fleet Bus;
the Bus preserves per-entry reply state through filtering, virtualization, and off-tab settlement;
and the persistent StatusLine renders its contractual honest segment order and reserved UA-5 slot.
All pure derivations live in `data/` (`railModel`,
`stateGrammar`, `catalogPoll`, `seatEvents`, `sessionCockpitStore`, the L6
`interactionAnswer`/`sessionLifecycle`/`ptyHarvest`, and the L3
`capabilityCatalog`/`launchEvidence`/`launchFlow`, plus L4 `announcer`/`pairChange`/
`sessionCapabilities`/`setAcceptance`/`setChips`/`setClient`/`setControlsCopy`); this route holds
DOM + wiring only.

## Route Model

- `SessionsView.tsx` — the view shell + the L2 derivation seam. Root = the scope/testid/marker
  carrier (`sessions--view`, `data-view="sessions"`). A `PanelGroup`
  (`autoSaveId="cockpit.sessions.panels"`) of rail (collapsible, ~280px target via a one-shot
  percentage calibration) / stage (min 35%) / inspector (24%, collapsible), the real `StatusLine`
  footer with reopen buttons, the non-portal `CommandPalette`, and the `useKeyboardZones` binding. Owns
  the command registry instance + the `CommandContext` actions (panel toggles, focus moves, the
  zone-sensitive alt+↑/↓ (`switchSession` in chrome; authoritative `composer.popBack` in the editor),
  live L4 effort cycle, and live FEUI-L5 submit), the narrow-width
  auto-collapse (pure decisions in `data/sessionLayout.ts`), the ~80-col floor chip re-measured
  from every width-changing path (`onLayout` + a stage-observing `ResizeObserver`), and — L2 —
  the shared poll-driver/mirror subscriptions, the ONCE-derived rail model + attention rollup
  (shared between rail and palette), R9 smart-default focus + F17 reason-bearing focus handoff,
  the one-way layout/palette store mirrors, and the dynamic palette commands (tree toggle,
  attention.jump, bulk-end mirrors with counts+names in the title, question triage). **L6 fills
  the stage body**: `StopResidualNotes` + `PtySurface` (or the explained placeholder for the
  EMPTY stage only) + `InteractionBar` directly above the shared FEUI-L5 composer; the
  floor chip now prefers the pane's REAL column count (`pane N cols (< 80)`) over the pixel
  estimate; the `workingLine` prop fills the stage slot; `turn.stop` joins the palette gated on
  the WorkingLine's OWN grammar predicate (`seatVisualState().key === "working"`) with the
  honest "unavailable: interrupt requires UA-7" title; triage now focuses the bar in place; and
  `startRetireResidualSweep()` is mounted beside the cockpit mirror (residual capture is
  data-layer, focus-independent — fix round F1). L3 appends (pure inserts, no L1/L2 node
  reshaped): the `session.launch` palette command + `launch` state, the `FailedLaunchBanner`
  block for any focused failed seat (above the pty surface), and the `<LaunchFlow>` overlay
  mounted after the palette. **L4** owns the one controlled model/effort popover shared by header
  and palette, mounts the promotion/drift + seat-state announcer watchers, drives alt+,/.
  `cycleEffortRequested`, renders the queued composer hint, and mounts persistent background
  `SetOutcomeToasts` plus `CockpitLiveRegions`. **L7 keeps this packed route narrow**: it selects
  only poll health, projected pickups, and supervisor heartbeat; passes them to `SeatInspector`;
  and composes `StatusLine`. Inspector-domain projection, virtualization, and reply state remain
  in focused files.
- `QueuePreview.tsx` (L5) — the read-only raw-free queue projection beside the composer. It shows
  only explicit server-authoritative `queued` records, never invents a queue position, and points
  the operator to Alt+Up; dispatching, ambiguous, settled, and availability-loss records are not
  rendered as withdrawable work.
- `SessionRail.tsx` (L2) — the rail renderer over `data/railModel`: ruled row anatomy (dot ·
  role(3) · title · attention-slot · status · End; only the status chip elides, truth in the row
  tooltip), flat spine, hairline-indented leaf clusters (active seat on top), per-master
  collapsed completed folders, master+sprint bulk end with honest NAMING previews, the
  zero-state-suppressed attention strip with live-derived highlight expiry, gate badges +
  two-state brief markers + L4's worded `set!` marker in the attention slot, accessible named
  state dots, the poll-stale banner, the
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
  the palette's "Launch session…" command) and the §1.2 header anatomy (identity → the sole
  live `ModelEffortControl` → grammar state → leaf/seat → diagnostics-first
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
- `ModelEffortControl.tsx` + `AcceptanceChip.tsx` (L4) — exact-session trigger/menu and shared
  visible evidence primitive. Popover open re-GETs the session snapshot; staged model changes
  re-gate effort options to that row; apply sends one knob or the serialized pair; fetch errors
  remain verbatim with retry; acceptance words, requested/effective values, spinner, mark-seen,
  and 503 retry all render in text.
- `CockpitLiveRegions.tsx` + `SetOutcomeToasts.tsx` (L4/L7) — persistent auditory and background
  outcome surfaces. The two mounted regions subscribe to polite/assertive stores; unfocused
  outcomes persist until the explicitly labelled `mark seen` action and several sessions collapse
  into one stack. Focusing or viewing never acknowledges.
- `StateDot.tsx` (L2, extended by L4) — the ONLY dot renderer for `data/stateGrammar` visuals
  (rail + header; StatusLine joins in L7; SeatInspector consumes only the grammar word);
  Panda-literal 2.4 s ease-in-out pulse pinned to
  `PULSE_ANIMATION`, steady under reduced motion, frozen by effects-off. L4 adds the optional
  named-image mode for rail dots; redundant header dots stay aria-hidden.
- `SeatInspector.tsx` (L7, carrying L2/L6/L4 evidence) — composition-only accessible tab host for
  Evidence / Capabilities / Bus. Native `hidden` removes inactive controls from layout, the
  accessibility tree, and keyboard traversal while all three panels stay mounted, preserving Bus
  drafts and in-flight settlement. Arrow keys plus Home/End implement roving tab focus. With no
  focused seat, seat-bound panes state their limit while the fleet Bus remains reachable.
- `EvidencePane.tsx` + `InspectorPrimitives.tsx` (L7) — the complete audit surface: launch,
  SetResult, submit receipts/reconciliation, bridge/pane/liveness facts, raw interaction payload,
  and both terminate/retire stop residual classes. Viewing is read-only; `mark seen` is explicit;
  exact `(sessionId, at)` residual dismissal is shared with the stage; fleet residuals survive
  source-row removal and no-focus mode. Primitives keep fact/raw/action semantics consistent.
- `CapabilitiesPane.tsx` (L7) — read-only exact-session snapshot and model-local effort truth,
  deliberately separated from the pre-session harness envelope. Refresh reuses the established
  reads; missing echo stays worded and native-process cost has no invented seconds.
- `BusPane.tsx` + `BusDeveloperReply.tsx` (L7) — fleet-global projected-pending pickup ledger with
  an exact focused-seat filter and separately rendered heartbeat. Entry-keyed reply state lives
  above filters/virtual rows and prunes only against the full authoritative projection. Reverse
  replies use projected sender agent/role only, POST a new operator-inbox message, never copy the
  target lifecycle, and never consume or acknowledge the source row.
- `VirtualizedInspectorList.tsx` (L7) — ordinary DOM list through 100 rows; TanStack virtualized
  rendering above 100 with full logical totals and `aria-posinset`/`aria-setsize`. It is reused by
  Evidence and Bus and never slices the underlying data.
- `StatusLine.tsx` (L7) — persistent order: harness → model/effort + EvidenceBadge → state/observed
  elapsed → leaf/seat → pending sets + queued messages → exact `ctx — / cost — (UA-5 slot)`;
  freshness, reopen actions, and keyboard hint follow. Tabular numbers and explicit absence replace
  fabricated telemetry.
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
- L4 adds focused suites for `ModelEffortControl`, `CockpitLiveRegions`, and `SetOutcomeToasts`,
  while the expanded HeaderStrip/SeatInspector/SessionRail suites pin one mounted control,
  ledger-view acknowledgment with seat-switch isolation, named rail dots, and the worded set
  marker. Data-layer tables cover all five acceptances, exact-session classification, serialized
  pair termination, unknown/queued readback, cycling, and announcement transitions.
- L7 adds focused suites for the Evidence/Capabilities/Bus panes, StatusLine, and the shared
  virtualized list. `SeatInspector.test.tsx` is the integration guard: tab keyboard semantics,
  native hidden behavior, draft/post/error persistence while Bus is inactive, and no-focus fleet
  access. Bus request tests pin sender-only reverse addressing and zero POST for lifecycle-only rows;
  virtualization is pinned at exactly 100/101 rows.

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
- **Set-control honesty invariants** (L4): live menus read only the exact-session snapshot and
  each model row's `sessionSettable` effort options; `configOptions` is never a menu. Requests and
  pendings never move effective markers. Every valid SetResult remains evidence, HTTP failures
  remain route failures, unknown triggers one readback, and pair effort waits for model evidence.
  Unacknowledged outcomes persist until an explicitly labelled mark-seen action; focus, viewing,
  and tab/seat changes never acknowledge. State/acceptance meaning is always present in words. The
  final reviewer PASS retains six
  nonblocking sev-4 observations on rare supersede/coalescing/visual/announcement edges, recorded
  in the governing file cards rather than promoted into false guarantees here.
- **Reliable-submit honesty invariants** (L5): one immutable request id/text/source/epoch survives
  retry and reconcile; only the exact pre-dispatch certificate retries; every response/poll uses the
  same monotonic fold; queue UI contains only authoritative queued rows; Alt+Up asks the server to
  withdraw and restores only by draft-revision CAS. Dispatching, not-found, and generation loss
  never become safe-pop-back evidence, and controlled prompt delivery never falls back to PTY paste.
- **Inspector/status honesty invariants** (L7): Bus is fleet-global pending projection by default,
  never full history or a health verdict; exact-seat filtering never broad-matches; reverse replies
  address only the projected sender and never consume the source; all pane instances stay mounted
  under native `hidden`; capability authorities remain separate; stop residuals survive focus/source
  loss; the status segment order and literal UA-5 absence slot remain contractual.
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
InteractionBar above the shared CodeMirror composer whose ONLY answer path is the gate channel;
the composer submits exact epoch-bound whole messages, shows authoritative queued work, reconciles
ambiguous delivery without resend, and runs server-linearized Alt+Up pop-back with explicit recovery;
the inspector is a stable-mounted accessible Evidence / Capabilities / Bus tab host: the full audit
surface with post-removal stop residuals and explicit mark seen, exact-session capability truth
separate from the launch envelope, and a fleet-first pending Bus with sender-addressed developer
reply; the persistent StatusLine ends the shell with proven pair/state/queue/freshness facts and the
literal empty UA-5 context/cost slot; the header's one L4 model/effort control reads the exact live snapshot, serializes pair
changes, and renders worded acceptance chips; narrow widths
auto-collapse on threshold crossings (reopenable), ctrl+k/ctrl+; open the cmdk palette (attention
jump, bulk-end mirrors, question triage focusing the bar, grammar-gated turn.stop), alt+↑/↓
cycles the rail order, F6 cycles regions, and the PTY zone passes every key through except
exactly the bound reserved set (clipboard chords stay reserved-unbound). "Launch session…"
(palette) opens the L3 LaunchFlow overlay — pick a detected harness, then a model/effort pair
exclusively from the live capability envelope (or explicit vendor defaults), POST the
both-or-neither selection, and land on the new row at tier 'pending'; a failed seat surfaces the
FailedLaunchBanner (verbatim refusal, Retire / Launch corrected…), and the header/inspector wear
the derived evidence tier through EvidenceBadge.
Queued set evidence adds a composer hint and promotes by exact-session readback; alt+,/. cycle the
requested effort without a dialog; background outcomes persist in one toast stack until marked
seen, while persistent polite/assertive regions announce focused set and seat transitions.

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
| Reliable submit transport, evidence fold, authority polling/withdrawal, and retention. | [data/submitClient.ts](agents-remember/dashboard/src/data/submitClient.ts); [data/submitMachine.ts](agents-remember/dashboard/src/data/submitMachine.ts); [data/submissionLifecycleClient.ts](agents-remember/dashboard/src/data/submissionLifecycleClient.ts); [data/submitRetention.ts](agents-remember/dashboard/src/data/submitRetention.ts) |
| The shared composer and authoritative queue projection. | [panels/SessionComposer.tsx](agents-remember/dashboard/src/panels/SessionComposer.tsx); [QueuePreview.tsx](agents-remember/dashboard/src/panels/session-cockpit/QueuePreview.tsx) |
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
| The exact-session capability/menu/effective-marker derivations (L4). | [data/sessionCapabilities.ts](agents-remember/dashboard/src/data/sessionCapabilities.ts) |
| The five-value acceptance/readback table and serialized pair machine (L4). | [data/setAcceptance.ts](agents-remember/dashboard/src/data/setAcceptance.ts), [data/pairChange.ts](agents-remember/dashboard/src/data/pairChange.ts) |
| The sole live set I/O driver plus shared chip/copy/announcement layers (L4). | [data/setClient.ts](agents-remember/dashboard/src/data/setClient.ts), [data/setChips.ts](agents-remember/dashboard/src/data/setChips.ts), [data/setControlsCopy.ts](agents-remember/dashboard/src/data/setControlsCopy.ts), [data/announcer.ts](agents-remember/dashboard/src/data/announcer.ts) |
| The L7 tab host and focused evidence/capability/fleet Bus panes. | [panels/session-cockpit/SeatInspector.tsx](agents-remember/dashboard/src/panels/session-cockpit/SeatInspector.tsx); [panels/session-cockpit/EvidencePane.tsx](agents-remember/dashboard/src/panels/session-cockpit/EvidencePane.tsx); [panels/session-cockpit/CapabilitiesPane.tsx](agents-remember/dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx); [panels/session-cockpit/BusPane.tsx](agents-remember/dashboard/src/panels/session-cockpit/BusPane.tsx) |
| The L7 contractual footer and shared inspector virtualization boundary. | [panels/session-cockpit/StatusLine.tsx](agents-remember/dashboard/src/panels/session-cockpit/StatusLine.tsx); [panels/session-cockpit/VirtualizedInspectorList.tsx](agents-remember/dashboard/src/panels/session-cockpit/VirtualizedInspectorList.tsx) |

## Update History

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 (Round 3 reviewer PASS): replaced the interim inspector
  with stable-mounted Evidence/Capabilities/Bus panes, added the contractual StatusLine, preserved
  per-entry reply state through filter/virtual/off-tab unmount pressure, restricted reverse replies
  to sender identity, surfaced post-removal stop residuals, and documented the 100/101 accessible
  virtualization boundary. Verification metadata remains pinned to the leaf base until closeout.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: replaced the composer/queue stub with the live
  shared CodeMirror surface, exact submit/reconcile lifecycle, QueuePreview, zone-sensitive Alt+Up,
  authoritative withdrawal, response-loss convergence, revision-CAS recovery, and no-PTY-fallback
  invariants.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 (live set controls; final reviewer PASS after three
  fix rounds): filled the header control with exact-session model/effort sourcing, the exhaustive
  SetResult/readback table and serialized pair flow; added shared worded chips/copy, per-seat
  ledger/rail attention, persistent background toasts, queued composer hint, cycle-effort, and
  polite/assertive live regions. The six remaining sev-4 observations are preserved on their
  governing file cards. Verification metadata is pinned to the contract base until the
  uncommitted code lands.
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
