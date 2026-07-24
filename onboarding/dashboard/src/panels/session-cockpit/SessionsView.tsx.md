# dashboard/src/panels/session-cockpit/SessionsView.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionsView.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The canonical full-page Chats composition seam (internal filename and data-view=sessions marker
retained for implementation/test stability). It renders the role/spawn rail, persistent stage,
reliable composer, interaction/lifecycle surfaces, source-selected working feedback, and optional
Evidence/Capabilities/Bus inspector. Operations is the shell default; this route replaces both the
legacy Chats page and the separate Sessions navigation concept.

FEUI-L8 makes inspector intent default closed and toggleable, separate from responsive geometry;
separates live action/reload routing from landed-row inspection focus; mounts ChatContextBar for
launch/task/leaf duties; keeps PtySurface unconditional across transient focus handoff; gates
controls/composer to live rows; and hosts landed-cleanup recovery outside the rail. The route derives
rail/attention once from the shared data plane and never owns a second catalog.

## Code Commentary

### FEUI MX-FIX-2 Accepted-Only Focus Delegation

The route no longer owns a parallel raw-terminal create callback. `ChatContextBar` performs the
authority check and invokes `focusSession` through `onSessionOpened` only after acceptance. This
keeps SessionsView as the focus/composition owner without letting a caller-minted id bypass the
visible duty-bar failure state.

### FEUI-L9R Reviewed Candidate Delta

Responsive collapse now preserves the sole chat-creation entrance: an empty narrow cockpit expands
the rail rather than applying ordinary auto-collapse, while populated cockpits keep the established
edge-based policy. A collapsed rail is both visually hidden and `aria-hidden`, so off-screen controls
do not remain in the accessibility tree. LaunchFlow remains outside the collapsible panel without
becoming a second entrance. **V11 (260718-CHATS-L5P):** the collapsed rail `<aside>` is now
`display:none` (was `visibility:hidden`), which removes the aside's own ~21px padding/border box — the
0px panel is truly empty, not a dead sliver. The drag min stays `RAIL_MIN_PERCENT` (12%); below it the
panel snaps fully collapsed and the `☰ rail` title-row chip + the in-place resize handle are the
reopen affordances. (The audit's desired ~220px min was left as an open design decision — react-resizable-panels
is percentage-only and the 280px calibration contract is pinned; see the worker report V11 flag.)

### 260715-FEUI-L7 Inspector Composition (superseded status details corrected below)

- **Narrow data seam** (L203-L206): the view selects existing `pollHealth`, projected
  `agentPickups`, and `supervisorHeartbeat` facts; it does not derive inspector-domain rows.
- **Inspector composition** (L735-L740): passes the focused session/cockpit plus fleet pickups and
  heartbeat into `SeatInspector`. The inspector owns its accessible stable-mounted tab host and
  delegates Evidence, Capabilities, and Bus logic to focused files.
- **Current action composition:** focused-session actions and rail/inspector reopen controls render
  on `SessionStage`'s title row. There is no StatusLine footer; detailed evidence remains in the
  inspector and the data stores that own it.
- No L7 list virtualization, reverse-reply, capability, evidence, or clock logic lives in this
  route file; this is intentionally the bounded composition seam for the already large route.

### 260715-FEUI-L4 Set-Control Wiring

- **One control, two entry surfaces** (L236-L239, L329-L355, L665-L672): view-owned
  `controlPopoverOpen` is passed through SessionStage/HeaderStrip to the one
  `ModelEffortControl`; the dynamic `control.setModel` and `control.setEffort` palette commands
  open it only for a live harness session. Focus switches close the prior seat's popover.
- **Promotion and announcements** (L247-L253): refcounted `startSetPromotionWatcher` and
  `startSeatStateAnnouncer` live beside the existing feed/sweep subscriptions, covering
  turn/focus snapshot rechecks and assertive failed/awaiting-input transitions.
- **Attention and cycle wiring** (L262-L268, L519-L527): rail-rollup unacknowledged ids use the
  shared `hasUnackedSetAttention` predicate, and the default effort commands now call
  `cycleEffortRequested` for the focused session instead of the L4 stub.
- **Composer hint and durable outcomes** (L718-L728, L816-L824): queued sets add the exact
  promotion hint adjacent to the composer; `SetOutcomeToasts` persists unfocused results until
  explicit acknowledgment; `CockpitLiveRegions` keeps both urgency channels mounted.

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
  priority; a null focus with live seats picks the smart default on entry. **R6 (260718-CHATS-L5P):**
  `lastFocusRef` now also remembers the focused seat's human LABEL, so once the row is gone from
  `sessions` at handoff time the banner names `previous.label` (the seat the operator knows) and, only if
  that is unavailable too, falls back to `shortId(previous.id)` — never leading with a raw UUID.
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
- **Command wiring**: one memoized `registerDefaultCommands(createCommandRegistry())`
  instance; `buildContext` supplies live actions (palette open/close, panel toggles via the
  imperative refs, focus moves, session switch, and L4 effort cycle) plus the honest L5 composer
  stub — routed through a `contextRef` so
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
- Model/effort palette commands and the header trigger must share one popover; queued hints,
  toasts, rail attention, and live regions must derive from the same cockpit evidence.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Panel group, floor chip, calibration, narrow rules, palette + keyboard wiring. | L192-L660 | [SessionsView.tsx](SessionsView.tsx) |
| The L6 stage fill: sweep mount, `turn.stop` + triage-bar focus, pane-cols chip, workingLine + surface/bar/notes children. | L205-L206; L229; L317-L331; L364-L376; L601-L649 | [SessionsView.tsx](SessionsView.tsx) |
| The pane surface the stage mounts per focused seat (archetypes, keep-alive, cols reporting). | L110-L244 | [PtySurface.tsx](PtySurface.tsx) |
| The one interaction axis rendered above the composer. | L79-L293 | [InteractionBar.tsx](InteractionBar.tsx) |
| The turn theater rendered into the stage's reserved slot (its grammar gate is the `turn.stop` gate). | L76-L126 | [WorkingLine.tsx](WorkingLine.tsx) |
| The focus-independent retire-residual sweep this view mounts (F1). | L47-L146 | [../../data/sessionLifecycle.ts](../../data/sessionLifecycle.ts) |
| The shell that mounts this view as a keep-alive hidden layer and gates `active`. | — | [../../cockpit/Cockpit.tsx](../../cockpit/Cockpit.tsx) |
| The pure decisions this shell feeds widths into. | L5-L85 | [../../data/sessionLayout.ts](../../data/sessionLayout.ts) |
| The registry + default commands the context actions serve. | L56-L179 | [../../data/commands.ts](../../data/commands.ts) |
| The L4 snapshot/set/pair/cycle/promotion driver mounted by this view. | L1-L433 | [../../data/setClient.ts](../../data/setClient.ts) |
| The sole live model/effort UI controlled from this view. | L148-L383 | [ModelEffortControl.tsx](ModelEffortControl.tsx) |
| Persistent background outcomes and screen-reader regions. | L58-L142; L19-L44 | [SetOutcomeToasts.tsx](SetOutcomeToasts.tsx), [CockpitLiveRegions.tsx](CockpitLiveRegions.tsx) |
| The F6 cycle + focus selectors used by `cycleRegion`/`focusStageHeader`/`focusTerminal`. | L8-L34 | [../../data/keymap/focus.ts](../../data/keymap/focus.ts) |
| The end-to-end suite: structure, chip re-measure paths, calibration, palette, zones, focus, + the L2 entry-focus/handoff/cycling cases. | L14-L300 | [SessionsView.test.tsx](SessionsView.test.tsx) |
| The one WebTUI mapping file whose scope root this component carries. | L17-L42 | [../../styles/webtui.css](../../styles/webtui.css) |
| The rail renderer receiving the once-derived model/rollup as props. | L364-L372 | [SessionRail.tsx](SessionRail.tsx) |
| The stage container + header line the stage panel mounts. | L46-L87 | [SessionStage.tsx](SessionStage.tsx) |
| The accessible stable-mounted Evidence / Capabilities / Bus tab host. | L18-L151 | [SeatInspector.tsx](SeatInspector.tsx) |
| The pure derivations this view memoizes once per render. | L131-L464 | [../../data/railModel.ts](../../data/railModel.ts) |
| The cockpit store (focus, mirrors, perSession) + the catalog mirror this view starts. | L107-L309 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The shared poll driver subscription. | L60-L77 | [../../data/catalogPoll.ts](../../data/catalogPoll.ts) |
| The L3 launch dialog this view opens (palette command / corrected-launch prefill). | L165-L613 | [LaunchFlow.tsx](LaunchFlow.tsx) |
| The L3 failed-launch banner mounted above the pty placeholder for a failed focused seat. | L70-L182 | [FailedLaunchBanner.tsx](FailedLaunchBanner.tsx) |
| R9: the conversation projection store this view reads to compute the focused seat's `liveTurnWorking`. | L296-L318 | [../../data/conversation/store.ts](../../data/conversation/store.ts) |
| R9: the seat-state grammar that prefers `liveTurnWorking` over the lagging catalog turn-state. | L106-L115 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

The view now wires the real shared composer to the focused controlled session, injects
`composer.popBack` into the command registry, hands slash query text to the palette, and preserves
the axis ordering PTY → interaction → composer. Gate-only answer mode shares the editor but never
calls prompt submit; raw-session typing remains confined to the PTY surface.

## FEUI-L8 Reviewed Candidate Delta

This is now the canonical Chats composition seam. It separates live action routing from landed inspection focus, mounts `ChatContextBar`, keeps `PtySurface` unconditional across handoff gaps, gates live-only controls, persists default-closed inspector intent separately from responsive collapse, and hosts root-level cleanup recovery.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## 260718-CHATS-L4 Reviewed Candidate Delta (structured Chats renderer)

The stage body composition changed: the previously **unconditional** `PtySurface` body is replaced by
`<ChatsStageBody>` for the focused seat (+77/−8). SUPERSEDES the FEUI-L8 "keeps `PtySurface`
unconditional" claim above — a controlled seat now defaults to the structured `ConversationSurface`,
and `PtySurface` survives only inside the default-off read-only terminal-diagnostics drawer and as the
legacy-raw primary body (both composed by `ChatsStageBody`, not this file). The keep-alive/handoff
discipline still holds for whichever PTY does mount.

New view-owned wiring:
- **Stage-mode state** — `libraryOpen` (browse-history) and `diagnosticsOpen` state threaded into
  `ChatsStageBody`; `onSessionOpened` focuses a newly-opened history session.
- **Focus-return tokens** — `toggleChatsDiagnostics` captures a focus-return token on open and restores
  it on close (F9), and the library close/back path consumes the same token idiom (F16), so neither
  drops focus to `<body>`.
- **Palette commands** — `chats.browseHistory` (opens the in-stage library, controlled sessions) and
  `chats.terminalDiagnostics` (toggles the drawer) join the registry, plus `conversation.backToChat`
  (when-gated on library open).
- **Interrupt** — the `conversation.stop` registry chord/palette command replaces the stale L6
  `turn.stop` registration (F2), and the interrupt hook (`useConversationInterrupt`) is fed to
  `WorkingLine` as its `interrupt` prop, which renders the actionable, capability-gated stop.

This is an additive composition change; QueuePreview/InteractionBar/HeaderStrip authorities and the
`data-kbzone`/`data-region` focus model are unchanged. The reviewed L4 candidate is
uncommitted; verification stays pinned to the FEUI-MX-FIX-2 base until closeout stamps the L4 commit.

## 260718-CHATS-L5F R9 Delta (streaming turn-state honesty — audit V5)

The route now imports `useActiveConversation` (`data/conversation/store`) and computes
`focusedLiveTurnWorking` for the FOCUSED seat only (L296-L318): it reads that seat's conversation
projection and returns true only when `projection.stream === "live"`, the status exists and its
`freshness.state !== "stale"`, and `status.turn.state ∈ {working, settling, retrying, compacting}`.
`focused` is then the base session row merged with `{ liveTurnWorking: true }` when that holds,
otherwise the plain base row. That flag flows through `stateGrammar.seatVisualState` (which prefers
it over the sweep-lagging catalog `turnState` but only below the terminal/fault/blocked/wait guards)
into the stage authorities — HeaderStrip StateDot and working cues — so a live streaming
turn stops reading a settled-green `turn-ended`. This is the honest display-preference: a
stale/disconnected projection is never trusted, and a real terminal/fault/blocked catalog state
still wins. **Recorded remainder (durable):** only the focused stage seat is covered here; the rail
chip is a separate store-driven per-row derivation (`SessionRail`), and wiring the projection signal
into non-focused rail rows is left as a follow-on — the stage (the surface in the developer's
screenshots) is covered, the rail chip is not.

## Current L5I Maintenance

`SessionsView` composes the decluttered stage: a deliberate 0.75rem rail gutter, stage-header
focused-session actions and rail/inspector controls, and no StatusLine or end-notification stack.
Rail selection defers focus into the controlled composer or raw PTY host. The working slot chooses
the live SSE conversation cue for a live harness stream and otherwise the catalog cue; the controlled
stop remains beside Send, while raw-terminal stop remains on its line. It passes cockpit visibility
through to the stage so scroll geometry can restore after a view switch.

## Update History

- 2026-07-24T13:17:17Z — Curator: corrected stage composition, focus handoff, source-selected working
  feedback, stop placement, view visibility, and removed StatusLine/stop-notification chrome. This
  is the current replacement owner for the retired StatusLine composition knowledge.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R9 (audit V5) focused-seat
  live-turn merge. The view imports `useActiveConversation` and computes `focusedLiveTurnWorking`
  from the focused seat's projection (`stream === "live"`, non-stale freshness, `turn.state ∈
  {working,settling,retrying,compacting}`), merging `{ liveTurnWorking: true }` into `focused` so
  `seatVisualState` shows a working stage over the lagging catalog `turn-ended`. Documented the
  honest fallbacks and the recorded remainder (rail chip left to a follow-on). Source uncommitted;
  closeout re-stamps verification.
- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded V11 (collapsed rail aside `display:none`,
  removing the ~21px residual sliver; drag min stays 12%) and R6 (the focus-handoff banner remembers the
  focused seat's human label via `lastFocusRef.label`, falling back to `shortId(previous.id)` — never a
  raw UUID). Composition/keep-alive/focus-model unchanged. Verification pinned to the leaf base
  (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 (structured Chats renderer, reviewer FINAL PASS): recorded
  the composition change from the unconditional `PtySurface` body to `ChatsStageBody` (structured
  surface default; PTY demoted to the read-only diagnostics drawer + legacy-raw body — supersedes the
  FEUI-L8 unconditional-PTY claim), the browse-history/diagnostics stage-mode state and focus-return
  tokens (F9/F16), the new `chats.browseHistory`/`chats.terminalDiagnostics`/`conversation.backToChat`
  palette commands, and the `conversation.stop` chord + `WorkingLine` interrupt-hook feed replacing the
  stale `turn.stop` (F2). Verification metadata remains pinned to the leaf base until closeout.
- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: removed the view-level raw opener and delegated accepted
  server-id focus from ChatContextBar, eliminating focus on failed or contradictory opens.
  Verification metadata remains pinned until closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: documented the empty-narrow rail exception and collapsed
  accessibility semantics; verification metadata remains pinned pending candidate closeout.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 kept this packed route to a narrow composition seam:
  it selects projected pickups, supervisor heartbeat, and poll health; passes them into the
  stable-mounted inspector; and composes the contractual StatusLine with existing reopen actions.
  Domain logic remains in focused files. Verification metadata remains pinned to the leaf base
  until closeout.
- 2026-07-17T21:39+02:00 — FEUI-L5: replaced the composer stub with live submit/pop-back wiring,
  slash palette query, queue/recovery UI, and explicit answer-channel separation.

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R2/R4/R6–R8 wired the one controlled model/effort
  popover to header and palette, live effort cycling, promotion/drift and seat-state watchers,
  queued composer hint, shared attention rollup, persistent background toasts, and dual live
  regions. Verification metadata is pinned to the contract base until the uncommitted code lands.
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
