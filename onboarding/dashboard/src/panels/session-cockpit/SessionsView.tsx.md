# dashboard/src/panels/session-cockpit/SessionsView.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionsView.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

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

- **Narrow data seam** (cit:([`projectedTaskDocuments`], dashboard/src/panels/session-cockpit/SessionsView.tsx:261-263)): the view selects existing projected task documents.
- The same seam selects fleet pickups and supervisor heartbeat facts (cit:([`pickups`; `supervisorHeartbeat`], dashboard/src/panels/session-cockpit/SessionsView.tsx:265-270)).
- **Inspector composition** (cit:(["export function SeatInspector({"], dashboard/src/panels/session-cockpit/SeatInspector.tsx:60-60)): the `SeatInspector` component is declared in its focused file.
- **Current action composition:** focused-session actions and rail/inspector reopen controls render
  on `SessionStage`'s title row. There is no StatusLine footer; detailed evidence remains in the
  inspector and the data stores that own it.
- No list virtualization, reverse-reply, capability, evidence, or clock logic lives in this
  route file; this is intentionally the bounded composition seam for the already large route.

### Set-Control Wiring

- **One control, two entry surfaces** (cit:(["one control, two surfaces"], dashboard/src/panels/session-cockpit/SessionsView.tsx:281-281)): the file records the one-control/two-surface design seam.
- **Promotion and announcements** (cit:(["The promotion/drift watcher"], dashboard/src/panels/session-cockpit/SessionsView.tsx:299-299)): the file names the promotion/drift watcher seam.
- **Attention and cycle wiring** (cit:(["hasUnackedSetAttention(perSession[session.id])"; "cycleEffortRequested(focusedSessionId, direction)"], dashboard/src/panels/session-cockpit/SessionsView.tsx:349-349; dashboard/src/panels/session-cockpit/SessionsView.tsx:907-907)): the view invokes `hasUnackedSetAttention` for the rail rollup and `cycleEffortRequested` for focused effort commands.
- **Composer hint and durable outcomes** (cit:(["queuedSetHint={queuedComposerHint(perSession[focused.id])}"; "<SetOutcomeToasts"; "<CockpitLiveRegions />"], dashboard/src/panels/session-cockpit/SessionsView.tsx:1240-1240; dashboard/src/panels/session-cockpit/SessionsView.tsx:1323-1323; dashboard/src/panels/session-cockpit/SessionsView.tsx:1328-1328)): the stage mounts the queued composer hint, `SetOutcomeToasts`, and `CockpitLiveRegions`.

### PTY Stage, Interactions, And Lifecycle Wiring

- **Stage body fill** (cit:(["<ChatsStageBody"; "<ConversationWorkingLine sessionId={focused.id} />"; "<InteractionBar session={focused} composerRef={composerRef} />"], dashboard/src/panels/session-cockpit/SessionsView.tsx:1195-1195; dashboard/src/panels/session-cockpit/SessionsView.tsx:1216-1216; dashboard/src/panels/session-cockpit/SessionsView.tsx:1231-1231)): the stage fill includes `ChatsStageBody`, `ConversationWorkingLine`, and `InteractionBar`.
- **R8 floor chip prefers pane truth** (cit:(["With a live pane the chip reflects the pane's REAL column count"], dashboard/src/panels/session-cockpit/SessionsView.tsx:1158-1158)): the file records the live-pane column-count rule.
- **F1 retire-residual sweep** (cit:(["useEffect(() => startRetireResidualSweep(), []);"], dashboard/src/panels/session-cockpit/SessionsView.tsx:298-298); cit:([`startRetireResidualSweep`], dashboard/src/data/sessionLifecycle.ts:136-154)): SessionsView mounts `startRetireResidualSweep`, whose subscription is refcounted.
- **conversation.stop palette command** (cit:(["id: \"conversation.stop\""; "title: \"Stop turn\""; "keywords: [\"stop\", \"interrupt\", \"cancel\", \"turn\", \"abort\"]"; "when: () => chatsInterruptRef.current.available"; "run: () => chatsInterruptRef.current.onStop?.()"], dashboard/src/panels/session-cockpit/SessionsView.tsx:582-584; dashboard/src/panels/session-cockpit/SessionsView.tsx:586-587)): the palette command registers its id, title, keywords, availability gate, and stop callback; the disabled WorkingLine reason is assigned by (cit:(["data-disabled-reason={interrupt.reason ?? STOP_TURN_DISABLED_REASON}"], dashboard/src/panels/session-cockpit/WorkingLine.tsx:170-170)).
- **Triage focuses the bar in place** (cit:(["for (const seat of waitingSeats(sessions))"; "const payload = sessionPendingInteractionPayload(seat)"; "const rawPreview = interactionPromptPreview(payload, 60)"; "const asker = pendingInteractionAgentLabel(payload)"; "focusSession(seat.id)"], dashboard/src/panels/session-cockpit/SessionsView.tsx:644-644; dashboard/src/panels/session-cockpit/SessionsView.tsx:647-649; dashboard/src/panels/session-cockpit/SessionsView.tsx:660-660); cit:(["window.requestAnimationFrame(() => rootRef.current ?.querySelector<HTMLElement>("], dashboard/src/panels/session-cockpit/SessionsView.tsx:661-663); cit:(["interaction-bar"; "?.focus(),"], dashboard/src/panels/session-cockpit/SessionsView.tsx:662-666)): each pending-seat command derives the payload/agent preview, focuses `seat.id`, then schedules the `interaction-bar` button focus.

- **The shared feed** (cit:(["useEffect(() => startCockpitMirror(), []);"], dashboard/src/panels/session-cockpit/SessionsView.tsx:295-295); cit:(["useEffect(() => startCatalogPollDriver(), []);"], dashboard/src/cockpit/Cockpit.tsx:388-388)): the view starts the cockpit mirror and the shell starts the catalog poll driver.
- **One derivation, two surfaces** (cit:(["buildRailModel(sessions, { masterLabel: (key) => labels.get(key) })"; "attentionRollup(sessions, {"], dashboard/src/panels/session-cockpit/SessionsView.tsx:343-343; dashboard/src/panels/session-cockpit/SessionsView.tsx:359-359)): the view derives the rail model and attention rollup.
- **R9 smart-default focus + F17 handoff** (cit:(["Smart-default focus (never an empty landing) + focus handoff."], dashboard/src/panels/session-cockpit/SessionsView.tsx:429-429)): the file records the smart-default focus/handoff design seam.
- **Store mirrors** (cit:([`setLayout`; `setPaletteOpen`], dashboard/src/panels/session-cockpit/SessionsView.tsx:505-505; dashboard/src/panels/session-cockpit/SessionsView.tsx:508-508)): the view calls `setLayout` and `setPaletteOpen`.
- **L2 palette commands** (cit:(["rail.treeToggle"; "attention.jump"], dashboard/src/panels/session-cockpit/SessionsView.tsx:600-600; dashboard/src/panels/session-cockpit/SessionsView.tsx:609-609)): the dynamic command registration includes `rail.treeToggle` and `attention.jump`.
- **Live `switchSession`** (cit:(["switchSession: (direction) => {"], dashboard/src/panels/session-cockpit/SessionsView.tsx:891-891)): the live command wiring exposes `switchSession`.

### Launch Surfaces (pure appends — no existing node reshaped or reordered)

- **The `launch` state** (cit:([`launch`], dashboard/src/panels/session-cockpit/SessionsView.tsx:274-279)): `{open, prefill?}` — the LaunchFlow dialog's open state,
  set by the palette command or the banner's corrected-launch prefill.
- **The `session.launch` palette command** (cit:(["session.launch"; "Launch session…"], dashboard/src/panels/session-cockpit/SessionsView.tsx:514-515)): the view registers the `session.launch` command with title `Launch session…`.
- **FailedLaunchBanner for a focused FAILED seat** (cit:(["focusedLive && focused.controlState === \"failed\" ? ("; "<FailedLaunchBanner"], dashboard/src/panels/session-cockpit/SessionsView.tsx:1183-1184)): a failed focused seat conditionally renders `FailedLaunchBanner`.
- **LaunchFlow** (cit:(["<LaunchFlow"], dashboard/src/panels/session-cockpit/SessionsView.tsx:1314-1314)): SessionsView mounts `LaunchFlow`.

### Logic

- **Panel group** (cit:(["autoSaveId={PANELS_AUTOSAVE_ID}"; "onLayout={handlePanelLayout}"], dashboard/src/panels/session-cockpit/SessionsView.tsx:1038-1039)): the `PanelGroup` carries the auto-save id and layout callback.
- **Command wiring**: one memoized `registerDefaultCommands(createCommandRegistry())`
  instance; `buildContext` supplies live actions (palette open/close, panel toggles via the
  imperative refs, focus moves, session switch, and the effort cycle) plus the honest composer
  stub — routed through a `contextRef` so
  `dispatch(commandId)` always runs against fresh state; `useKeyboardZones({ active, dispatch })`
  installs the chords.
- **Palette focus discipline** (cit:([`openPalette`; `closePalette`], dashboard/src/panels/session-cockpit/SessionsView.tsx:721-733; dashboard/src/panels/session-cockpit/SessionsView.tsx:735-741)): `openPalette` records the ORIGINAL invoker only on a
  closed→open transition (an in-palette page switch keeps it); `closePalette` returns focus to
  the invoker when still connected (R7).
- **F6 cycle** (cit:(["The F6 cycle: rail → stage → inspector → status line"], dashboard/src/panels/session-cockpit/SessionsView.tsx:700-700); cit:([`nextRegion`], dashboard/src/data/keymap/focus.ts:14-24)): the file documents the F6 cycle and `nextRegion` supplies the ordered transition.
- **The ~80-col floor chip** (cit:([`measureStage`], dashboard/src/panels/session-cockpit/SessionsView.tsx:946-948)): `measureStage()` computes `stageNarrow` from `stageBelowPtyFloor`.
- **~280px rail calibration** (cit:([`calibrateRail`], dashboard/src/panels/session-cockpit/SessionsView.tsx:955-962)): `calibrateRail` skips non-positive widths, bypasses persisted layouts, and resizes the rail by `railDefaultPercent`.
- **Narrow-width rules** (cit:(["Narrow-width rules: rail behavior is unchanged."], dashboard/src/panels/session-cockpit/SessionsView.tsx:971-971)): the file records unchanged narrow-width rail behavior.

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
  `active` is passed from Cockpit.tsx (cit:(["active={view === \"chats\" && !takeover}"], dashboard/src/cockpit/Cockpit.tsx:623-623)) into this view, which passes it to `useKeyboardZones` (cit:(["useKeyboardZones({ active, dispatch });"], dashboard/src/panels/session-cockpit/SessionsView.tsx:940-940)).
- The keyboard-zone contract (`data-kbzone="pty"/"composer"`) survives the stage fill: the real
  `PtySurface` carries the pty zone marker (tested), the placeholder keeps it for the empty
  stage, and the composer textarea (the earlier placeholder, now ref-exposed) keeps the composer zone.
- All decisions (thresholds, floor, calibration percentages) live in data/sessionLayout.ts
  (cit:([`ptyFloorPx`; `railDefaultPercent`; `hasPersistedPanelLayout`; `stageBelowPtyFloor`; `autoCollapseTransition`], dashboard/src/data/sessionLayout.ts:21-23; dashboard/src/data/sessionLayout.ts:36-43; dashboard/src/data/sessionLayout.ts:50-61; dashboard/src/data/sessionLayout.ts:64-66; dashboard/src/data/sessionLayout.ts:74-85)), and
  The named rail/attention/focus derivations are implemented in data/railModel.ts
  (cit:([`masterLabels`; `buildRailModel`; `attentionRollup`; `smartDefaultFocus`], dashboard/src/data/railModel.ts:120-129; dashboard/src/data/railModel.ts:131-205; dashboard/src/data/railModel.ts:283-298; dashboard/src/data/railModel.ts:357-373)).
- Focus handoff must never fight a deliberate landed-row inspection (the F17 only-under-us rule).
- Model/effort palette commands and the header trigger must share one popover; queued hints,
  toasts, rail attention, and live regions must derive from the same cockpit evidence.

### Todos

No task-independent technical debt was identified during review.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The view names the panel, floor-chip, calibration, narrow-rule, and keyboard-wiring seams. | "useKeyboardZones({ active, dispatch });"; "The ~80-col floor chip"; "~280px rail default"; "Narrow-width rules: rail behavior is unchanged." | dashboard/src/panels/session-cockpit/SessionsView.tsx:940-940; dashboard/src/panels/session-cockpit/SessionsView.tsx:942-942; dashboard/src/panels/session-cockpit/SessionsView.tsx:950-950; dashboard/src/panels/session-cockpit/SessionsView.tsx:971-971 |
| The stage fill mounts the sweep, live-turn selector, `conversation.stop` registration fields, `ChatsStageBody`, and `InteractionBar`. | "useEffect(() => startRetireResidualSweep(), []);"; "const focusedLiveTurnWorking = useActiveConversation((state) => {"; "id: \"conversation.stop\""; "title: \"Stop turn\""; "keywords: [\"stop\", \"interrupt\", \"cancel\", \"turn\", \"abort\"]"; "when: () => chatsInterruptRef.current.available"; "run: () => chatsInterruptRef.current.onStop?.()"; "<ChatsStageBody"; "<InteractionBar session={focused} composerRef={composerRef} />" | dashboard/src/panels/session-cockpit/SessionsView.tsx:298-298; dashboard/src/panels/session-cockpit/SessionsView.tsx:310-310; dashboard/src/panels/session-cockpit/SessionsView.tsx:582-584; dashboard/src/panels/session-cockpit/SessionsView.tsx:586-587; dashboard/src/panels/session-cockpit/SessionsView.tsx:1195-1195; dashboard/src/panels/session-cockpit/SessionsView.tsx:1231-1231 |
| The payload selector + agent label the question-triage preview resolves (N1). | `sessionPendingInteractionPayload` | dashboard/src/data/sessions.ts:467-471 |
| The pending interaction agent label used by the question-triage preview. | `pendingInteractionAgentLabel` | dashboard/src/data/interactionAnswer.ts:192-199 |
| The pane surface the stage mounts per focused seat (archetypes, keep-alive, cols reporting). | `ChatsStageBody`; "<PtySurface" | dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:147-489 |
| The stage renders one `InteractionBar` above the composer. | "<InteractionBar session={focused} composerRef={composerRef} />" | dashboard/src/panels/session-cockpit/SessionsView.tsx:1231-1231 |
| The stage renders `ConversationWorkingLine`/`WorkingLine` and the complete `conversation.stop` command registration. | "<ConversationWorkingLine sessionId={focused.id} />"; "<WorkingLine"; "id: \"conversation.stop\""; "title: \"Stop turn\""; "when: () => chatsInterruptRef.current.available"; "run: () => chatsInterruptRef.current.onStop?.()" | dashboard/src/panels/session-cockpit/SessionsView.tsx:582-583; dashboard/src/panels/session-cockpit/SessionsView.tsx:586-587; dashboard/src/panels/session-cockpit/SessionsView.tsx:1216-1216; dashboard/src/panels/session-cockpit/SessionsView.tsx:1218-1218 |
| The retire-residual sweep implementation. | `startRetireResidualSweep` | dashboard/src/data/sessionLifecycle.ts:136-154 |
| The view mounts the focus-independent retire-residual sweep. | "useEffect(() => startRetireResidualSweep(), []);" | dashboard/src/panels/session-cockpit/SessionsView.tsx:298-298 |
| The shell passes the active expression to this view. | "active={view === \"chats\" && !takeover}" | dashboard/src/cockpit/Cockpit.tsx:623-623 |
| The pure decisions this shell feeds widths into. | `ptyFloorPx`; `railDefaultPercent`; `hasPersistedPanelLayout`; `stageBelowPtyFloor`; `autoCollapseTransition` | dashboard/src/data/sessionLayout.ts:21-23; dashboard/src/data/sessionLayout.ts:36-43; dashboard/src/data/sessionLayout.ts:50-61; dashboard/src/data/sessionLayout.ts:64-66; dashboard/src/data/sessionLayout.ts:74-85 |
| The registry + default commands the context actions serve. | `createCommandRegistry`; `registerDefaultCommands` | dashboard/src/data/commands.ts:57-81; dashboard/src/data/commands.ts:88-191 |
| The snapshot/set/pair/cycle/promotion drivers are defined in `setClient.ts`. | `refreshSessionSnapshot`; `sendSet`; `startPairChangeFlow`; `cycleEffortRequested`; `startSetPromotionWatcher` | dashboard/src/data/setClient.ts:68-115; dashboard/src/data/setClient.ts:157-244; dashboard/src/data/setClient.ts:327-335; dashboard/src/data/setClient.ts:352-374; dashboard/src/data/setClient.ts:398-445 |
| The `ModelEffortControl` component is declared here. | "export function ModelEffortControl({" | dashboard/src/panels/session-cockpit/ModelEffortControl.tsx:149-149 |
| Persistent background outcomes and screen-reader regions. | `SetOutcomeToasts` | dashboard/src/panels/session-cockpit/SetOutcomeToasts.tsx:58-142 |
| Persistent screen-reader regions. | `CockpitLiveRegions` | dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx:19-45 |
| `nextRegion` supplies the ordered F6 region transition. | `nextRegion` | dashboard/src/data/keymap/focus.ts:14-24 |
| The rail renderer receiving the once-derived model/rollup as props. | `SessionRail`; `model`; `rollup` | dashboard/src/panels/session-cockpit/SessionRail.tsx:480-481; dashboard/src/panels/session-cockpit/SessionRail.tsx:487-1102 |
| `SessionStage` is the stage container component. | "export function SessionStage({" | dashboard/src/panels/session-cockpit/SessionStage.tsx:46-46 |
| The accessible stable-mounted Evidence / Capabilities / Bus tab host. | `SeatInspector` | dashboard/src/panels/session-cockpit/SeatInspector.tsx:60-161 |
| The pure rail/attention/focus derivations are defined in `railModel.ts`. | `masterLabels`; `buildRailModel`; `attentionRollup`; `smartDefaultFocus` | dashboard/src/data/railModel.ts:120-129; dashboard/src/data/railModel.ts:131-205; dashboard/src/data/railModel.ts:283-298; dashboard/src/data/railModel.ts:357-373 |
| The cockpit store and catalog mirror are defined in `sessionCockpitStore.ts`. | `sessionCockpitStore`; `startCockpitMirror` | dashboard/src/data/sessionCockpitStore.ts:279-511; dashboard/src/data/sessionCockpitStore.ts:522-542 |
| The shared poll driver subscription is owned by the shell. | "useEffect(() => startCatalogPollDriver(), []);" | dashboard/src/cockpit/Cockpit.tsx:388-388 |
| The `LaunchFlow` component implementation. | `LaunchFlow` | dashboard/src/panels/session-cockpit/LaunchFlow.tsx:177-619 |
| The `FailedLaunchBanner` component implementation. | `FailedLaunchBanner` | dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:70-182 |
| SessionsView reads `focusedLiveTurnWorking` from the active conversation projection. | "const focusedLiveTurnWorking = useActiveConversation((state) => {" | dashboard/src/panels/session-cockpit/SessionsView.tsx:310-310 |
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

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: replaced stale SessionsView line citations with
  exact anchors; completed the whole triage dataflow audit, bound the full conversation.stop registration,
  narrowed JSX/comment-only claims, preserved the generated interaction-bar focus body, and split pooled
  reference rows by source owner.
