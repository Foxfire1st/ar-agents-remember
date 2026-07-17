# dashboard/src/panels/session-cockpit/SessionsView.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionsView.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **sessions cockpit view** (260715-FEUI-L1 S2 shell, FILLED by 260715-FEUI-L2, PTY stage +
interactions by 260715-FEUI-L6, launch surfaces by 260715-FEUI-L3): rail / stage / inspector as
a react-resizable-panels group with the narrow-width rules (inspector auto-collapses <~1100px,
rail <~900px — both reopenable) and the ~80-col PTY floor hint chip. **L2 fills the panels**:
the rail hosts `SessionRail` (the ruled role hierarchy + fleet attention), the stage the
`SessionStage` container + `HeaderStrip` (empty ModelEffortControl slot for L4), and the
inspector the read-only `SeatInspector` provenance card (the L7 tabbed inspector replaces it).
**L6 fills the stage body**: the focused seat renders a real `PtySurface` pane (carrying the
`data-kbzone="pty"` contract), `StopResidualNotes` above it, the `InteractionBar` directly above
the composer (never replacing it), and the `WorkingLine` into the stage's reserved slot; the PTY
placeholder now renders ONLY for the empty stage (no focused session), and the composer textarea
remains L5's placeholder (now ref-exposed to the bar's answer-mode). **L3 appends the launch
surfaces**: the `session.launch` palette command opens the `LaunchFlow` overlay, and a focused
FAILED seat renders the `FailedLaunchBanner` inside the stage children above the pty surface.
The view owns the L2 derivation seam: rail model + attention rollup are derived ONCE per render
and shared between the rail and the palette commands. The root div carries
**`[data-view="sessions"]`** — the WebTUI scope root (S1) and the keyboard layer's home — plus
`sessions--view` and the marker classes and `sessions-*` testids.

## Code Commentary

### 260715-FEUI-L6 PTY Stage, Interactions, And Lifecycle Wiring

- **Stage body fill** (L622-L649): `SessionStage` now receives `workingLine`
  (`<WorkingLine session={focused} cockpit={perSession[focused.id]}>` — L2's reserved slot,
  rendered only with a focused seat) and children in the ruled order: `<StopResidualNotes />`
  (the dismissable informational stop-residual lines), then `<PtySurface focused={…}
  onVisibleCols={setPtyCols}>` for a focused seat OR the explained placeholder (copy updated:
  "no focused session — the terminal renders here once a seat is focused…") — the placeholder is
  now the EMPTY-stage identity only, and the real surface carries the same `data-kbzone="pty"`
  contract (jsdom-tested both ways; no L1 zone test weakened), then
  `<InteractionBar session={focused} composerRef={composerRef}>` directly ABOVE the composer —
  the composer is never replaced (R4; position pinned by test), and the textarea now carries
  `ref={composerRef}` (L646) so the bar's no-choices answer-mode can mark it and read its text.
- **R8 floor chip prefers pane truth** (L205, L606-L619): `ptyCols` state is fed by the VISIBLE
  pane's real column count (`PtySurface`'s `onVisibleCols`, from `Terminal`'s post-fit
  `onResizeCols`); when a pane reports, the chip renders `pane N cols (< 80)` with the measured
  count in the tooltip — the L1 pixel estimate (`stageNarrow`) remains the pane-less fallback
  only.
- **F1 retire-residual sweep** (L229, L279): `useEffect(() => startRetireResidualSweep(), [])`
  mounts the focus-independent data-layer sweep beside the poll driver/mirror — the former
  focused-handoff residual-capture block is REMOVED (ownership moved to
  `data/sessionLifecycle.ts`; an unfocused/tombstoned seat's `retireControlStopError` still
  surfaces, and resurfaces after a reload).
- **`turn.stop` palette command** (L317-L331): registered UA-7-honest — the title names the gap
  (`Stop turn — unavailable: <STOP_TURN_DISABLED_REASON>`), the `when` gate is the WorkingLine's
  OWN render condition `seatVisualState(focused).key === "working"` (review finding F3 — never
  `turnState` directly, which would offer a command whose control is not on screen), and `run()`
  focuses the welded disabled `working-line-stop` control so the reason is seen where the
  control lives (design §9.7). The registration effect's deps gained `focused`.
- **Triage focuses the bar in place** (L364-L376): the L2 per-seat question-triage commands now
  focus the seat AND then the `interaction-bar` button — answering was the user's explicit
  palette intent, so this is the invoked action, not a focus steal (R4's never-steal rule is
  about spontaneous arrival).

- **The shared feed** (L212-L215): `startCatalogPollDriver()` + `startCockpitMirror()` —
  refcounted, shared with Cockpit's unconditional subscription, so the keep-alive layer never
  double-polls.
- **One derivation, two surfaces** (L218-L235): `masterLabels(taskDocuments)` →
  `buildRailModel(sessions, labels)` and
  `attentionRollup(sessions, {unackedIds, criticalBus})` (unacked joined from the cockpit store's
  unacknowledged set ledgers; critical bus from `criticalBusSessionIds(pickups, sessions)`) are
  memoized ONCE and passed to `SessionRail` as props AND consumed by the palette commands —
  same-snapshot consistency by construction.
- **R9 smart-default focus + F17 handoff** (L242-L270): refocus happens ONLY when nothing is
  focused or the focused seat stopped running UNDER us — a user deliberately inspecting a landed
  row is never fought. When the focused seat retires/lands, a reason-bearing handoff note is set
  (`<label> landed/retired — <why> · focus handed off`) and focus moves by `smartDefaultFocus`
  priority; a null focus with live seats picks the smart default on entry.
- **Store mirrors** (L272-L278): the view-owned `railCollapsed`/`inspectorCollapsed` and
  `palette.open` are mirrored ONE-WAY into `sessionCockpitStore` (design §4.3 — the view keeps
  ownership via its imperative panel handles).
- **L2 palette commands** (L280-L344): dynamic registrations over the shared registry — the tree
  toggle (title flips with state), `attention.jump` (when-gated on a live target), sprint- and
  per-master bulk-end mirrors whose titles carry the HONEST counts + names (`End N completed —
  sprint: a, b, …` — the palette row IS the preview), and per-seat question triage
  (`Answer pending question — <label>: “<preview>”`, newest first; since L6, selecting focuses
  the seat AND its InteractionBar in place). All disposed and re-registered per dependency change.
- **Live `switchSession`** (L404-L416): alt+↑/↓ now cycles `railCycleOrder(model)` around the
  focused seat (the former L1 stub replaced — command ids/chords unchanged).

### 260715-FEUI-L3 Launch Surfaces (pure appends — no L1/L2 node reshaped or reordered)

- **The `launch` state** (L213-L217): `{open, prefill?}` — the LaunchFlow dialog's open state,
  set by the palette command or the banner's corrected-launch prefill.
- **The `session.launch` palette command** (L287-L296): one self-contained registry effect
  ("Launch session…") — the palette is the flow's entry point (design §7.1); no chord minted
  (consistent with L2's chord-audit posture).
- **FailedLaunchBanner for a focused FAILED seat** (L589-L597): mounted inside the stage children
  BEFORE the pty placeholder when `focused?.controlState === "failed"` (R6 — the refusal renders
  verbatim, never hidden, never auto-retried); `onLaunchCorrected` opens the flow pre-filled.
  NOTE for the L6 sync-merge: this insert sits textually adjacent to the pty placeholder L6 owns —
  structurally additive; resolution is "banner above pty surface" (review finding 5, no-action).
- **`<LaunchFlow>`** (L687-L693): mounted after `<CommandPalette>` with the live `sessions` list
  (the F9 unknown-outcome reconciler watches it) and `focusSession` as the focus sink.

### Logic

- **Panel group** (L364-L465): `PanelGroup` `autoSaveId="cockpit.sessions.panels"` with rail
  (collapsible, `collapsedSize=0`, `defaultSize=RAIL_FALLBACK_PERCENT`, min 12 / max 40 — the
  bounds shared with calibration), stage (`defaultSize=54`, `minSize=35`), inspector
  (collapsible, `defaultSize=24`, min 14 / max 40). An explicit `defaultSize` on EVERY panel
  keeps the group's layout state complete before any DOM measurement — the imperative
  collapse/expand handles depend on it. `onCollapse`/`onExpand` mirror panel state into
  `railCollapsed`/`inspectorCollapsed`; the status-line footer surfaces `☰ rail` / `◫ inspector`
  reopen buttons while collapsed (R3 reopenable), alongside the `ctrl+k palette · ? keys · F6
  regions` hint.
- **Command wiring** (L206-L296): one memoized `registerDefaultCommands(createCommandRegistry())`
  instance; `buildContext` supplies live actions (palette open/close, panel toggles via the
  imperative refs, focus moves) and the honest L2/L4/L5 stubs — routed through a `contextRef` so
  `dispatch(commandId)` always runs against fresh state; `useKeyboardZones({ active, dispatch })`
  installs the chords.
- **Palette focus discipline** (L235-L251): `openPalette` records the ORIGINAL invoker only on a
  closed→open transition (an in-palette page switch keeps it); `closePalette` returns focus to
  the invoker when still connected (R7).
- **F6 cycle** (L218-L233): availability filters collapsed panels out, the current region is
  resolved from `document.activeElement`'s `[data-region]` host, and `data/keymap/focus.nextRegion`
  decides.
- **The ~80-col floor chip** (L300-L326, L410-L418): `measureStage()` sets `stageNarrow` from
  `stageBelowPtyFloor(stage.clientWidth)`. Review round 2 (finding 1) wired it into EVERY
  width-changing path: `PanelGroup onLayout={handlePanelLayout}` (divider drags AND
  collapse/expand, incl. palette/button-driven — none of which resize the view root; also the
  deterministic jsdom-testable path) plus the ResizeObserver observing the STAGE element alongside
  the root. The chip carries the honest tooltip ("a squeezed hosted TUI is a layout fact, not
  harness misbehavior").
- **~280px rail calibration** (L309-L319, review round 2 finding 4): `calibrateRail(rootWidth)` is
  ONE-SHOT on the first non-zero root measurement (a 0-width hidden-layer measure does not consume
  it), skipped entirely when `hasPersistedPanelLayout` reports a saved layout, applied via
  `railRef.resize(railDefaultPercent(...))`; `defaultSize` stays the 22% reference fallback for
  the unmeasured case.
- **Narrow-width rules** (L330-L355): the root-measuring effect ignores 0-width (the hidden
  keep-alive layer must never react), records `lastWidthRef`, and drives collapse/expand through
  `autoCollapseTransition`'s edge semantics — a collapse triggered here re-enters via `onLayout`,
  so the post-layout re-measure always lands last (the round-1 read-before-collapse ordering flaw
  is structurally gone).

### Conventions

Co-located Panda `css()` with token names (`bgPanel`, `grid`, `amber`, `muted`); marker classes
kept via `cx`; `data-testid` on every interactive/assertable element; `data-region` +
`data-focus-target` + `data-stage-header` carry the focus model; `data-kbzone="pty"/"composer"`
carry zone ownership. The resize-handle hover transition follows the existing DualPane idiom
(frozen by the global effects freeze).

### Invariants And Boundaries

- `[data-view="sessions"]` must stay on THIS root — the WebTUI scope and the palette overlay
  anchor (`position: relative`).
- The component must stay safe as a never-unmounted hidden layer: 0-width measures are ignored;
  `active` (from `Cockpit.tsx`) gates all key bindings.
- The keyboard-zone contract (`data-kbzone="pty"/"composer"`) survives the L6 fill: the real
  `PtySurface` carries the pty zone marker (tested), the placeholder keeps it for the empty
  stage, and the composer textarea (L5's placeholder, now ref-exposed) keeps the composer zone.
- All decisions (thresholds, floor, calibration percentages) live in `data/sessionLayout.ts`, and
  ALL rail/attention/focus derivations live in `data/railModel.ts` — this file only measures,
  derives once, and wires.
- Focus handoff must never fight a deliberate landed-row inspection (the F17 only-under-us rule).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Panel group, floor chip, calibration, narrow rules, palette + keyboard wiring. | L192-L660 | [SessionsView.tsx](SessionsView.tsx) |
| The L6 stage fill: sweep mount, `turn.stop` + triage-bar focus, pane-cols chip, workingLine + surface/bar/notes children. | L205-L206; L229; L317-L331; L364-L376; L601-L649 | [SessionsView.tsx](SessionsView.tsx) |
| The pane surface the stage mounts per focused seat (archetypes, keep-alive, cols reporting). | L110-L244 | [PtySurface.tsx](PtySurface.tsx) |
| The one interaction axis rendered above the composer. | L79-L293 | [InteractionBar.tsx](InteractionBar.tsx) |
| The turn theater rendered into the stage's reserved slot (its grammar gate is the `turn.stop` gate). | L76-L126 | [WorkingLine.tsx](WorkingLine.tsx) |
| The dismissable informational stop-residual lines above the surface. | — | [StopResidualNotes.tsx](StopResidualNotes.tsx) |
| The focus-independent retire-residual sweep this view mounts (F1). | L47-L146 | [../../data/sessionLifecycle.ts](../../data/sessionLifecycle.ts) |
| The shell that mounts this view as a keep-alive hidden layer and gates `active`. | — | [../../cockpit/Cockpit.tsx](../../cockpit/Cockpit.tsx) |
| The pure decisions this shell feeds widths into. | L5-L85 | [../../data/sessionLayout.ts](../../data/sessionLayout.ts) |
| The registry + default commands the context actions serve. | L56-L179 | [../../data/commands.ts](../../data/commands.ts) |
| The F6 cycle + focus selectors used by `cycleRegion`/`focusStageHeader`/`focusTerminal`. | L8-L34 | [../../data/keymap/focus.ts](../../data/keymap/focus.ts) |
| The end-to-end suite: structure, chip re-measure paths, calibration, palette, zones, focus, + the L2 entry-focus/handoff/cycling cases. | L14-L300 | [SessionsView.test.tsx](SessionsView.test.tsx) |
| The one WebTUI mapping file whose scope root this component carries. | L17-L42 | [../../styles/webtui.css](../../styles/webtui.css) |
| The rail renderer receiving the once-derived model/rollup as props. | L364-L372 | [SessionRail.tsx](SessionRail.tsx) |
| The stage container + header line the stage panel mounts. | L46-L87 | [SessionStage.tsx](SessionStage.tsx) |
| The inspector provenance card the inspector panel mounts. | L45-L110 | [SeatInspector.tsx](SeatInspector.tsx) |
| The pure derivations this view memoizes once per render. | L131-L464 | [../../data/railModel.ts](../../data/railModel.ts) |
| The cockpit store (focus, mirrors, perSession) + the catalog mirror this view starts. | L107-L309 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The shared poll driver subscription. | L60-L77 | [../../data/catalogPoll.ts](../../data/catalogPoll.ts) |
| The L3 launch dialog this view opens (palette command / corrected-launch prefill). | L165-L613 | [LaunchFlow.tsx](LaunchFlow.tsx) |
| The L3 failed-launch banner mounted above the pty placeholder for a failed focused seat. | L70-L182 | [FailedLaunchBanner.tsx](FailedLaunchBanner.tsx) |

## Update History

- 2026-07-17T06:10+02:00 — 260715-FEUI-L3 (R5/R6): launch surfaces appended — the `launch` state,
  the `session.launch` palette registration, the FailedLaunchBanner block for a focused failed
  seat (prepended inside the stage children before the pty placeholder; L6-adjacency merge note
  recorded — post-merge resolution: banner above the pty surface), and the `<LaunchFlow>` element
  after the palette. Pure appends — no existing L1/L2 node reshaped or reordered
  (reviewer-verified hunk by hunk). Verification metadata pinned to the leaf base until closeout
  stamps the L3 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (incl. review fix round F1/F3): the stage body is
  FILLED — `PtySurface` for the focused seat (placeholder now empty-stage-only, zone contract
  carried by the real surface), `StopResidualNotes` above it, `InteractionBar` above the
  never-replaced composer (textarea ref-exposed for answer-mode), `WorkingLine` into the
  reserved slot; the ~80-col chip prefers the visible pane's REAL cols (`pane N cols (< 80)`)
  over the pixel estimate; `startRetireResidualSweep()` mounted focus-independent (the
  handoff-effect capture block removed — F1); `turn.stop` palette command gated on the
  WorkingLine's own grammar state (F3) with the UA-7 gap named in the title and run() focusing
  the welded control; triage commands now focus the InteractionBar in place. Verification
  metadata pinned to the leaf base until closeout stamps the L6 code commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2: the shell's panels are FILLED — SessionRail (model +
  rollup derived once and shared with the palette), SessionStage + HeaderStrip (floor chip moves
  into `headerExtra`), SeatInspector in the inspector pane; added the shared poll-driver/mirror
  subscriptions, R9 smart-default focus + F17 reason-bearing focus handoff (never fighting a
  deliberate landed-row inspection), one-way layout/palette store mirrors, the dynamic L2 palette
  commands (tree toggle, attention.jump, bulk-end mirrors with counts+names in the title,
  question triage), and the live alt+↑/↓ `switchSession` over `railCycleOrder`. Verification
  metadata pinned to the leaf base until closeout stamps the L2 code commit.
- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S2 (R3), including the review round-2
  fixes: the rail/stage/inspector shell with edge-transition auto-collapse + reopen affordances,
  the ~80-col floor chip re-measured from every width path (`onLayout` + stage ResizeObserver —
  finding 1), the one-shot ~280px rail percentage calibration that never overrides a persisted
  layout (finding 4), the command-context wiring, palette invoker focus-return, and the F6 cycle.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
