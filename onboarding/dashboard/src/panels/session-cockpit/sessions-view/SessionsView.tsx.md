# dashboard/src/panels/session-cockpit/sessions-view/SessionsView.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/SessionsView.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-07T08:19Z |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## 260731-EFA-L8 Split Layout

The 1,336-line `SessionsView.tsx` was split by responsibility into
`dashboard/src/panels/session-cockpit/sessions-view/`. `SessionsView.tsx` is now the
canonical memoized entry; the state/controller logic lives in
`sessionsViewController.ts` and `useSessionsPaletteCommands.tsx`; the composed
rail/stage/inspector/overlay JSX lives in `sessionsViewBody.tsx`; styles live in
`styles.ts`. The former monolithic test suite split into `shell.test.tsx`,
`focus.test.tsx`, `lifecycle.test.tsx`, `stageSurface.test.tsx`,
`stopResiduals.test.tsx`, and `launchAndKeepAlive.test.tsx` (shared fixtures in
`test-utils.tsx`). Behavior is preserved; the split is the frontend-rail size
remediation (260731-EFA-L8 R4/R5).

## Purpose

The canonical full-page Chats composition seam (internal filename and data-view=sessions marker
retained for implementation/test stability). It renders the role/spawn rail, persistent stage,
reliable composer, interaction/lifecycle surfaces, source-selected working feedback, and optional
Evidence/Capabilities/Bus inspector. Operations is the shell default; this route replaces both the
legacy Chats page and the separate Sessions navigation concept.

The route makes inspector intent default closed and toggleable, separate from responsive geometry;
separates live action/reload routing from landed-row inspection focus; mounts ChatContextBar for
launch/task/leaf duties; keeps PtySurface unconditional across transient focus handoff; gates
controls/composer to live rows; and hosts landed-cleanup recovery outside the rail. The route derives
rail/attention once from the shared data plane and never owns a second catalog.

## Code Commentary

### Accepted-Only Focus Delegation

The route no longer owns a parallel raw-terminal create callback. `ChatContextBar` performs the
authority check and invokes `focusSession` through `onSessionOpened` only after acceptance. This
keeps SessionsView as the focus/composition owner without letting a caller-minted id bypass the
visible duty-bar failure state.

### Responsive Collapse Candidate Delta

Responsive collapse now preserves the sole chat-creation entrance: an empty narrow cockpit expands
the rail rather than applying ordinary auto-collapse, while populated cockpits keep the established
edge-based policy. A collapsed rail is both visually hidden and `aria-hidden`, so off-screen controls
do not remain in the accessibility tree. LaunchFlow remains outside the collapsible panel without
becoming a second entrance. **V11:** the collapsed rail aside is now
`display:none` (was `visibility:hidden`), which removes the aside's own ~21px padding/border box — the
0px panel is truly empty, not a dead sliver. The drag min stays `RAIL_MIN_PERCENT` (12%); below it the
panel snaps fully collapsed and the `☰ rail` title-row chip + the in-place resize handle are the
reopen affordances. (The audit's desired ~220px min was left as an open design decision — react-resizable-panels
is percentage-only and the 280px calibration contract is pinned; see the worker report V11 flag.)

### Inspector Composition (superseded status details corrected below)

- **Narrow data seam** (cit:([`projectedTaskDocuments`], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:258-260)): the view selects existing projected task documents.
- The same seam selects fleet pickups and agent-notifier heartbeat facts (cit:(["pickups={data.pickups}", "heartbeat={data.agentNotifierHeartbeat}"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:354-355)).
- **Inspector composition** (cit:(["export function SeatInspector({"], dashboard/src/panels/session-cockpit/SeatInspector.tsx:112-112)): the `SeatInspector` component is declared in its focused file.
- **Current action composition:** focused-session actions and rail/inspector reopen controls render
  on `SessionStage`'s title row. There is no StatusLine footer; detailed evidence remains in the
  inspector and the data stores that own it.
- No list virtualization, reverse-reply, capability, evidence, or clock logic lives in this
  route file; this is intentionally the bounded composition seam for the already large route.

### Set-Control Wiring

- **One control, two entry surfaces** (cit:(["one control"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:212-212)): the file records the one-control/two-surface design seam.
- **Promotion and announcements** (cit:(["The promotion/drift watcher"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:813-813)): the file names the promotion/drift watcher seam.
- **Attention and cycle wiring** (cit:(["hasUnackedSetAttention(perSession[session.id])", "cycleEffortRequested(data.focusedSessionId"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:331-331; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:1023-1023)): the view invokes `hasUnackedSetAttention` for the rail rollup and `cycleEffortRequested` for focused effort commands.
- **Composer hint and durable outcomes** (cit:(["queuedSetHint={queuedComposerHint(perSession[focused.id])}", "<SetOutcomeToasts", "<CockpitLiveRegions />"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:223-223; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:393-393; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:398-398)}`, `<SetOutcomeToasts`, `<CockpitLiveRegions />`, `; `, `; `, `SetOutcomeToasts`, `CockpitLiveRegions`], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:223-223; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:393-393; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:398-398)}", "<SetOutcomeToasts", "<CockpitLiveRegions />"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:223-223; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:393-393; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:398-398)}"; "<SetOutcomeToasts"; "<CockpitLiveRegions />"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:223-223; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:393-393; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:398-398)): the stage mounts the queued composer hint, `SetOutcomeToasts`, and `CockpitLiveRegions`.

### PTY Stage, Interactions, And Lifecycle Wiring

- **Stage body fill** (cit:(["onToggleDiagnostics={handlers.toggleChatsDiagnostics}", "<ConversationWorkingLine sessionId={focused.id} />", "<InteractionBar session={focused} composerRef={refs.composerRef} />"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:260-260; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:195-195; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:215-215)): the stage fill includes `ChatsStageBody`, `ConversationWorkingLine`, and `InteractionBar`.
- **R8 floor chip prefers pane truth** (cit:(["The VISIBLE pane's real column count"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:196-196)): the file records the live-pane column-count rule.
- **F1 retire-residual sweep** (cit:(["useEffect(() => startRetireResidualSweep()", "export function startRetireResidualSweep(): () => void {"], dashboard/src/data/sessionLifecycle.ts:136-136; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:812-812)): SessionsView mounts `startRetireResidualSweep`, whose subscription is refcounted.
- **conversation.stop palette command** (cit:(["id: \"conversation.stop\""; "title: \"Stop turn\""; "keywords: [\"stop\", \"interrupt\", \"cancel\", \"turn\", \"abort\"]"; "when: () => deps.chatsInterruptRef.current.available"; "run: () => deps.chatsInterruptRef.current.onStop?.()"], dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:125-131)): the palette command registers its id, title, keywords, availability gate, and stop callback; the disabled WorkingLine reason is assigned by (cit:(["data-disabled-reason"], dashboard/src/panels/session-cockpit/sessions-view/stageSurface.test.tsx:173-173)).
- **Triage focuses the bar in place** (cit:(["for (const seat of waitingSeats(sessions))"; "const payload = sessionPendingInteractionPayload(seat)"; "const rawPreview = interactionPromptPreview(payload"; "const asker = pendingInteractionAgentLabel(payload)"; "focusSession(seat.id)"], dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:146-162); cit:(["window.requestAnimationFrame(() =>"], dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:163-166); cit:(["interaction-bar"], dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:166-166)): each pending-seat command derives the payload/agent preview, focuses `seat.id`, then schedules the `interaction-bar` button focus.

- **The shared feed** (cit:(["useEffect(() => startCockpitMirror()", "useEffect(() => startCatalogPollDriver()"], dashboard/src/cockpit/Cockpit.tsx:861-861; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:809-809) => startCockpitMirror(), []);"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:814-814); cit:(["useEffect(() => startCatalogPollDriver()"], dashboard/src/cockpit/Cockpit.tsx:861-861)): the view starts the cockpit mirror and the shell starts the catalog poll driver.
- **One derivation, two surfaces** (cit:(["buildRailModel(sessions, taskDocuments)", "attentionRollup(sessions"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:325-345)): the view derives the task-document rail model and attention rollup once for its rendering surfaces.
- **R9 smart-default focus + F17 handoff** (cit:(["Smart-default focus (never an empty landing) + focus handoff."], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:890-890) + focus handoff."], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:895-895)): the file records the smart-default focus/handoff design seam.
- **Store mirrors** (cit:([`setLayout`; `setPaletteOpen`], dashboard/src/data/sessionCockpitStore.ts:225-226)): the view calls `setLayout` and `setPaletteOpen`.
- **L2 palette commands** (cit:(["rail.treeToggle"; "attention.jump"], dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:199-199; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:190-190)): the dynamic command registration includes `rail.treeToggle` and `attention.jump`.
- **Live `switchSession`** (cit:(["switchSession: (direction) =>", `switchSession`, `switchSession`], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:1012-1012) =>"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:1017-1017)): the live command wiring exposes `switchSession`.

### Launch Surfaces (pure appends — no existing node reshaped or reordered)

- **The `launch` state** (cit:(["open={state.launch.open}", "prefill={state.launch.prefill}"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:385-386)): `{open, prefill?}` — the LaunchFlow dialog's open state,
  set by the palette command or the banner's corrected-launch prefill.
- **The `session.launch` palette command** (cit:(["session.launch", "Launch session…"], dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:38-39)): the view registers the `session.launch` command with title `Launch session…`.
- **FailedLaunchBanner for a focused FAILED seat** (cit:(["onLaunchCorrected={(prefill) => state.setLaunch({ open: true", "focused.controlState !== \"failed\""], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:179-179; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:173-173)): a failed focused seat conditionally renders `FailedLaunchBanner`.
- **LaunchFlow** (cit:(["onClose={() => state.setLaunch({ open: false })}"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:389-389)): SessionsView mounts `LaunchFlow`.

### Logic

- **Panel group** (cit:(["autoSaveId={PANELS_AUTOSAVE_ID}", "import { Panel, PanelGroup, PanelResizeHandle } from \"react-resizable-panels\";"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:413-413; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:1-1)): the `PanelGroup` carries the auto-save id and layout callback.
- **Command wiring**: one memoized `registerDefaultCommands(createCommandRegistry())`
  instance; `buildContext` supplies live actions (palette open/close, panel toggles via the
  imperative refs, focus moves, session switch, and the effort cycle) plus the honest composer
  stub — routed through a `contextRef` so
  `dispatch(commandId)` always runs against fresh state; `useKeyboardZones({ active, dispatch })`
  installs the chords.
- **Palette focus discipline** (cit:([`openPalette`, `closePalette`, `openPalette`], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:379-379; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:224-224)): `openPalette` records the ORIGINAL invoker only on a
  closed→open transition (an in-palette page switch keeps it); `closePalette` returns focus to
  the invoker when still connected (R7).
- **F6 cycle** (cit:(["The F6 cycle: rail → stage → inspector → status line", "const next = nextRegion(current"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:452-452; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:467-467)): the file documents the F6 cycle and `nextRegion` supplies the ordered transition.
- **The ~80-col floor chip** (cit:(["const measureStage = useCallback(() => {", "state.setStageNarrow(stageBelowPtyFloor(refs.stageRef.current?.clientWidth ?? 0));"], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:759-760)): `measureStage()` computes `stageNarrow` from `stageBelowPtyFloor`.
- **~280px rail calibration** (cit:([`calibrateRail`], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:56-56)): `calibrateRail` skips non-positive widths, bypasses persisted layouts, and resizes the rail by `railDefaultPercent`.
- **Narrow-width rules** (cit:(["Narrow-width rules: rail behavior is unchanged."], dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:772-772)): the file records unchanged narrow-width rail behavior.

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
  `active` is passed from Cockpit.tsx (cit:(["active={view === \"chats\" && !takeover}", "useKeyboardZones({ active"], dashboard/src/cockpit/Cockpit.tsx:782-782; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:1052-1052)) into this view, which passes it to `useKeyboardZones`.
- The keyboard-zone contract (`data-kbzone="pty"/"composer"`) survives the stage fill: the real
  `PtySurface` carries the pty zone marker (tested), the placeholder keeps it for the empty
  stage, and the composer textarea (the earlier placeholder, now ref-exposed) keeps the composer zone.
- All decisions (thresholds, floor, calibration percentages) live in data/sessionLayout.ts
  (cit:([`ptyFloorPx`; `railDefaultPercent`; `hasPersistedPanelLayout`; `stageBelowPtyFloor`; `autoCollapseTransition`], dashboard/src/data/sessionLayout.ts:21-23; dashboard/src/data/sessionLayout.ts:36-43; dashboard/src/data/sessionLayout.ts:50-61; dashboard/src/data/sessionLayout.ts:64-66; dashboard/src/data/sessionLayout.ts:74-85)), and
  The named rail/attention/focus derivations are implemented in data/railModel.ts
  (cit:([`buildRailModel`; `attentionRollup`; `smartDefaultFocus`], dashboard/src/data/railModel.ts:361-387; dashboard/src/data/railModel.ts:470-485; dashboard/src/data/railModel.ts:544-560)).
- Focus handoff must never fight a deliberate landed-row inspection (the F17 only-under-us rule).
- Model/effort palette commands and the header trigger must share one popover; queued hints,
  toasts, rail attention, and live regions must derive from the same cockpit evidence.

### Todos

No task-independent technical debt was identified during review.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The view names the panel, floor-chip, calibration, narrow-rule, and keyboard-wiring seams. | "useKeyboardZones({ active"; "The ~80-col floor chip"; "~280px rail default"; "Narrow-width rules: rail behavior is unchanged." | dashboard/src/data/sessionLayout.test.ts:42-58; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:757-757; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:772-772; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:1052-1052 |
| The stage fill mounts the sweep, live-turn selector, `conversation.stop` registration fields, `ChatsStageBody`, and `InteractionBar`. | "useEffect(() => startRetireResidualSweep()"; "const focusedLiveTurnWorking = useActiveConversation((state) => {"; "id: \"conversation.stop\""; "title: \"Stop turn\""; "keywords: [\"stop\", \"interrupt\", \"cancel\", \"turn\", \"abort\"]"; "when: () => deps.chatsInterruptRef.current.available"; "run: () => deps.chatsInterruptRef.current.onStop?.()"; "<InteractionBar session={focused} composerRef={refs.composerRef} />"; "onToggleDiagnostics={handlers.toggleChatsDiagnostics}" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:215-215; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:260-260; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:296-296; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:812-812; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:125-127; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:129-130 |
| The payload selector + agent label the question-triage preview resolves (N1). | `sessionPendingInteractionPayload` | dashboard/src/data/sessions.ts:552-556 |
| The pending interaction agent label used by the question-triage preview. | `pendingInteractionAgentLabel` | dashboard/src/data/interactionAnswer.ts:191-198 |
| The pane surface the stage mounts per focused seat (archetypes, keep-alive, cols reporting). | "hidden={!terminalFocused}"; "onVisibleCols={terminalFocused ? onVisibleCols : undefined}"; "import { ChatsStageBody } from \"../ChatsStageBody\";" | dashboard/src/panels/session-cockpit/stageLayers.tsx:104-104; dashboard/src/panels/session-cockpit/stageLayers.tsx:103-103; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:22-22 |
| The stage renders one `InteractionBar` above the composer. | "<InteractionBar session={focused} composerRef={refs.composerRef} />" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:215-215 |
| The stage renders `ConversationWorkingLine`/`WorkingLine` and the complete `conversation.stop` command registration. | "<ConversationWorkingLine sessionId={focused.id} />"; "id: \"conversation.stop\""; "title: \"Stop turn\"" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:195-195; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:197-197; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:125-131 |
| The retire-residual sweep implementation. | `startRetireResidualSweep` | dashboard/src/data/sessionLifecycle.ts:136-154 |
| The view mounts the focus-independent retire-residual sweep. | "useEffect(() => startRetireResidualSweep()" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:812-812 |
| The shell passes the active expression to this view. | "active={view === \"chats\" && !takeover}" | dashboard/src/cockpit/Cockpit.tsx:782-782 |
| The pure decisions this shell feeds widths into. | `ptyFloorPx`; `railDefaultPercent`; `hasPersistedPanelLayout`; `stageBelowPtyFloor`; `autoCollapseTransition` | dashboard/src/data/sessionLayout.ts:21-23; dashboard/src/data/sessionLayout.ts:36-43; dashboard/src/data/sessionLayout.ts:50-61; dashboard/src/data/sessionLayout.ts:64-66; dashboard/src/data/sessionLayout.ts:74-85 |
| The registry + default commands the context actions serve. | `createCommandRegistry`; `registerDefaultCommands` | dashboard/src/data/commands.ts:57-81; dashboard/src/data/commands.ts:88-191 |
| The snapshot/set/pair/cycle/promotion drivers are defined in `setClient.ts`. | `refreshSessionSnapshot`; `sendSet`; `startPairChangeFlow`; `cycleEffortRequested`; `startSetPromotionWatcher` | dashboard/src/data/setClient.ts:72-119; dashboard/src/data/setClient.ts:228-274; dashboard/src/data/setClient.ts:375-383; dashboard/src/data/setClient.ts:405-426; dashboard/src/data/setClient.ts:450-497 |
| The `ModelEffortControl` component is declared here. | "export function ModelEffortControl({" | dashboard/src/panels/session-cockpit/ModelEffortControl.tsx:635-635 |
| Persistent background outcomes and screen-reader regions. | `SetOutcomeToasts` | dashboard/src/panels/session-cockpit/SetOutcomeToasts.tsx:58-142 |
| Persistent screen-reader regions. | `CockpitLiveRegions` | dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx:19-45 |
| `nextRegion` supplies the ordered F6 region transition. | `nextRegion` | dashboard/src/data/keymap/focus.ts:14-24 |
| The rail renderer receiving the once-derived model/rollup as props. | `SessionRail`; `model`; `rollup` | dashboard/src/panels/session-cockpit/SessionRail.tsx:49-50; dashboard/src/panels/session-cockpit/SessionRail.tsx:155-235 |
| `SessionStage` is the stage container component. | "export function SessionStage({" | dashboard/src/panels/session-cockpit/SessionStage.tsx:46-46 |
| The accessible stable-mounted Evidence / Capabilities / Bus tab host. | `SeatInspector` | dashboard/src/panels/session-cockpit/SeatInspector.tsx:60-161 |
| The pure task-document rail, attention, and focus derivations are defined in `railModel.ts`. | `buildRailModel`; `attentionRollup`; `smartDefaultFocus` | dashboard/src/data/railModel.ts:361-387; dashboard/src/data/railModel.ts:470-485; dashboard/src/data/railModel.ts:544-560 |
| The cockpit store and catalog mirror are defined in `sessionCockpitStore.ts`. | `sessionCockpitStore`; `startCockpitMirror` | dashboard/src/data/sessionCockpitStore.ts:588-601; dashboard/src/data/sessionCockpitStore.ts:612-632 |
| The shared poll driver subscription is owned by the shell. | "useEffect(() => startCatalogPollDriver()" | dashboard/src/cockpit/Cockpit.tsx:861-861 |
| The `LaunchFlow` component implementation. | `LaunchFlow` | dashboard/src/panels/session-cockpit/LaunchFlow.tsx:353-413 |
| The `FailedLaunchBanner` component implementation. | `FailedLaunchBanner` | dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:69-143 |
| SessionsView reads `focusedLiveTurnWorking` from the active conversation projection. | "const focusedLiveTurnWorking = useActiveConversation((state) => {" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:296-296 |
| The seat-state grammar declares `liveTurnWorking`. | `liveTurnWorking` | dashboard/src/data/stateGrammar.ts:92-92 |

## Reliable Submit Delta

The view now wires the real shared composer to the focused controlled session, injects
`composer.popBack` into the command registry, hands slash query text to the palette, and preserves
the axis ordering PTY → interaction → composer. Gate-only answer mode shares the editor but never
calls prompt submit; raw-session typing remains confined to the PTY surface.

## Canonical Chats Composition Candidate Delta

This is now the canonical Chats composition seam. It separates live action routing from landed inspection focus, mounts `ChatContextBar`, keeps `PtySurface` unconditional across handoff gaps, gates live-only controls, persists default-closed inspector intent separately from responsive collapse, and hosts root-level cleanup recovery.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Structured Chats Renderer Candidate Delta

The stage body composition changed: the previously **unconditional** `PtySurface` body is replaced by
ChatsStageBody for the focused seat (+77/−8). SUPERSEDES the earlier "keeps PtySurface
unconditional" claim above — a controlled seat now defaults to the structured `ConversationSurface`,
and `PtySurface` survives only inside the default-off read-only terminal-diagnostics drawer and as the
legacy-raw primary body (both composed by `ChatsStageBody`, not this file). The keep-alive/handoff
discipline still holds for whichever PTY does mount.

New view-owned wiring:
- **Stage-mode state** — `libraryOpen` (browse-history) and `diagnosticsOpen` state threaded into
  `ChatsStageBody`; `onSessionOpened` focuses a newly-opened history session.
- **Focus-return tokens** — `toggleChatsDiagnostics` captures a focus-return token on open and restores
  it on close (F9), and the library close/back path consumes the same token idiom (F16), so neither
  drops focus to the document body.
- **Palette commands** — `chats.browseHistory` (opens the in-stage library, controlled sessions) and
  `chats.terminalDiagnostics` (toggles the drawer) join the registry, plus `conversation.backToChat`
  (when-gated on library open).
- **Interrupt** — the `conversation.stop` registry chord/palette command replaces the stale
  `turn.stop` registration (F2), and the interrupt hook (`useConversationInterrupt`) is fed to
  `WorkingLine` as its `interrupt` prop, which renders the actionable, capability-gated stop.

This is an additive composition change; QueuePreview/InteractionBar/HeaderStrip authorities and the
`data-kbzone`/`data-region` focus model are unchanged. The reviewed candidate is
uncommitted; verification stays pinned to the prior base until closeout stamps the commit.

## Streaming Turn-State Honesty Delta (audit V5)

The focused seat's live conversation projection wins over lagging catalog turn state only while the
projection is live, present, and fresh, and while its turn is in one of the active working states.
The focused row then carries the live-working flag into the stage grammar, where it is preferred below
terminal, fault, blocked, and waiting guards. A stale or disconnected projection is never trusted,
and a real terminal or fault catalog state still wins. Only the focused stage seat is covered here;
the rail chip remains a separate store-driven per-row derivation.

## Decluttered Stage Maintenance

`SessionsView` composes the decluttered stage: a deliberate 0.75rem rail gutter, stage-header
focused-session actions and rail/inspector controls, and no StatusLine or end-notification stack.
Rail selection defers focus into the controlled composer or raw PTY host. The working slot chooses
the live SSE conversation cue for a live harness stream and otherwise the catalog cue; the controlled
stop remains beside Send, while raw-terminal stop remains on its line. It passes cockpit visibility
through to the stage so scroll geometry can restore after a view switch.

## Update History
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: re-mapped this sidecar from dashboard/src/panels/session-cockpit/SessionsView.tsx to the sessions-view/ canonical entry after the responsibility split; added the L8 Split Layout section. Verification pinned to the leaf base until closeout stamps the code commit.

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: replaced stale SessionsView line citations with
  exact anchors; completed the whole triage dataflow audit, bound the full conversation.stop registration,
  narrowed JSX/comment-only claims, preserved the generated interaction-bar focus body, and split pooled
  reference rows by source owner.
