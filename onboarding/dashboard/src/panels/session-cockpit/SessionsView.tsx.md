# dashboard/src/panels/session-cockpit/SessionsView.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionsView.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **sessions cockpit view** (260715-FEUI-L1 S2 shell, FILLED by 260715-FEUI-L2): rail / stage /
inspector as a react-resizable-panels group with the narrow-width rules (inspector auto-collapses
<~1100px, rail <~900px — both reopenable) and the ~80-col PTY floor hint chip. **L2 fills the
panels**: the rail hosts `SessionRail` (the ruled role hierarchy + fleet attention), the stage the
`SessionStage` container + `HeaderStrip` (empty ModelEffortControl slot for L4, reserved
WorkingLine slot for L6), and the inspector the read-only `SeatInspector` provenance card (the L7
tabbed inspector replaces it). The PTY/composer placeholders REMAIN — they are the keyboard-zone
anchors L6/L5 fill. The view owns the L2 derivation seam: rail model + attention rollup are
derived ONCE per render and shared between the rail and the palette commands. The root div
carries **`[data-view="sessions"]`** — the WebTUI scope root (S1) and the keyboard layer's home —
plus `sessions--view` and the marker classes and `sessions-*` testids.

## Code Commentary

### 260715-FEUI-L2 Data Layer, Rail, And Stage Wiring

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
  (`Answer pending question — <label>: “<preview>”`, newest first; selecting focuses the seat —
  answering itself is L6's InteractionBar). All disposed and re-registered per dependency change.
- **Live `switchSession`** (L404-L416): alt+↑/↓ now cycles `railCycleOrder(model)` around the
  focused seat (the former L1 stub replaced — command ids/chords unchanged).

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
- The remaining PTY/composer placeholders are the keyboard-zone anchors (`data-kbzone`); L6/L5
  fill them WITHOUT moving the markers/testids.
- All decisions (thresholds, floor, calibration percentages) live in `data/sessionLayout.ts`, and
  ALL rail/attention/focus derivations live in `data/railModel.ts` — this file only measures,
  derives once, and wires.
- Focus handoff must never fight a deliberate landed-row inspection (the F17 only-under-us rule).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Panel group, floor chip, calibration, narrow rules, palette + keyboard wiring. | L190-L506 | [SessionsView.tsx](SessionsView.tsx) |
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

## Update History

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
