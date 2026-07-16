# dashboard/src/panels/session-cockpit/SessionsView.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionsView.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **sessions cockpit view shell** (260715-FEUI-L1 S2): rail / stage / inspector as a
react-resizable-panels group with the narrow-width rules (inspector auto-collapses <~1100px, rail
<~900px — both reopenable) and the ~80-col PTY floor hint chip. Panel CONTENT is deliberate
scaffolding — labeled placeholder panels carrying the marker classes, focus targets, and
keyboard-zone markers later leaves fill (L2 rail rows + HeaderStrip, L4 controls, L5 composer,
L6 PTY, L7 inspector/status line). The root div carries **`[data-view="sessions"]`** — the WebTUI
scope root (S1) and the keyboard layer's home — plus `sessions--view` and the
`sessions__rail/stage/inspector/statusline` marker classes and `sessions-*` testids. No animation
is introduced, so `html[data-effects="off"]` and reduced-motion are trivially respected.

## Code Commentary

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
- Panel content placeholders are labeled with the leaf that fills them; filling leaves keep the
  markers/testids in place.
- All decisions (thresholds, floor, calibration percentages) live in `data/sessionLayout.ts`;
  this file only measures and applies.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Panel group, floor chip, calibration, narrow rules, palette + keyboard wiring. | L190-L506 | [SessionsView.tsx](SessionsView.tsx) |
| The shell that mounts this view as a keep-alive hidden layer and gates `active`. | — | [../../cockpit/Cockpit.tsx](../../cockpit/Cockpit.tsx) |
| The pure decisions this shell feeds widths into. | L5-L85 | [../../data/sessionLayout.ts](../../data/sessionLayout.ts) |
| The registry + default commands the context actions serve. | L56-L179 | [../../data/commands.ts](../../data/commands.ts) |
| The F6 cycle + focus selectors used by `cycleRegion`/`focusStageHeader`/`focusTerminal`. | L8-L34 | [../../data/keymap/focus.ts](../../data/keymap/focus.ts) |
| The end-to-end suite: structure, chip re-measure paths, calibration, palette, zones, focus. | L14-L246 | [SessionsView.test.tsx](SessionsView.test.tsx) |
| The one WebTUI mapping file whose scope root this component carries. | L17-L42 | [../../styles/webtui.css](../../styles/webtui.css) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S2 (R3), including the review round-2
  fixes: the rail/stage/inspector shell with edge-transition auto-collapse + reopen affordances,
  the ~80-col floor chip re-measured from every width path (`onLayout` + stage ResizeObserver —
  finding 1), the one-shot ~280px rail percentage calibration that never overrides a persisted
  layout (finding 4), the command-context wiring, palette invoker focus-return, and the F6 cycle.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
