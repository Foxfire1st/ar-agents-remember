# dashboard/src/panels/session-cockpit/ — Sessions Cockpit Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/session-cockpit/`          |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
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
(`data/stateGrammar.ts` — 2.4 s ease-in-out pulse, never steps()). Remaining scaffolding: L4 the
controls, L5 the real composer (CM6) + queue, L6 the PtySurface + WorkingLine, L7 the tabbed
inspector/status line. All pure derivations live in `data/` (`railModel`, `stateGrammar`,
`catalogPoll`, `seatEvents`, `sessionCockpitStore`); this route holds DOM + wiring only.

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
  attention.jump, bulk-end mirrors with counts+names in the title, question triage).
- `SessionRail.tsx` (L2) — the rail renderer over `data/railModel`: ruled row anatomy (dot ·
  role(3) · title · attention-slot · status · End; only the status chip elides, truth in the row
  tooltip), flat spine, hairline-indented leaf clusters (active seat on top), per-master
  collapsed completed folders, master+sprint bulk end with honest NAMING previews, the
  zero-state-suppressed attention strip with live-derived highlight expiry, gate badges +
  two-state brief markers in the reserved attention-marker slot, the poll-stale banner, the
  anchored bus footer, and the spawn-edge provenance tree toggle.
- `SessionStage.tsx` + `HeaderStrip.tsx` (L2) — the stage container's RULED layer order
  (HeaderStrip → reserved `data-slot="working-line"` → surface → composer; explained empty
  identity, F17 handoff note) and the §1.2 header anatomy (identity → EMPTY
  `data-slot="model-effort-control"` for L4 → grammar state → leaf/seat → diagnostics-first
  elision; honest `ws —`/quiet freshness + requested-tier provenance badges).
- `StateDot.tsx` (L2) — the ONLY renderer of `data/stateGrammar` visuals (rail + header +
  inspector; StatusLine joins in L7); Panda-literal 2.4 s ease-in-out pulse pinned to
  `PULSE_ANIMATION`, steady under reduced motion, frozen by effects-off.
- `SeatInspector.tsx` (L2) — the read-only provenance card in the inspector pane (spawn
  role/level/requested pair at its honest tier, spawned-by, landed/retired reasons, liveness
  evidence); replaced by the L7 tabbed inspector.
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
  entry focus, F17 handoff, alt+↑/↓ cycling) — all 21 L1 cases pass against the real rail/stage.
- `SessionRail.test.tsx` + `HeaderStrip.test.tsx` (L2) — the jsdom rail-state matrix (every
  fixture row's dot ≡ grammar), the anatomy-order and model-leakage DOM negatives, hierarchy /
  attention / joins / completed-folder / bulk-end / footer-honesty coverage, the cross-surface
  dot consistency case, and the HeaderStrip/SessionStage anatomy + honesty cases — over the
  shared `test/fixtures/catalogRows.ts` FLEET.

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

## Hot Path Summary

The Sessions cockpit view: a keep-alive full-bleed rail/stage/inspector panel group under the
`[data-view="sessions"]` WebTUI scope root — the rail renders the ruled role hierarchy (flat
spine, active-first leaf clusters, completed folders + naming bulk end) with fleet attention and
one shared state grammar (2.4 s ease-in-out dot pulse, blocked-on-human steady), the stage renders
the HeaderStrip + reserved L4/L6 slots for the smart-default-focused seat with reason-bearing
focus handoff, the inspector a read-only provenance card; narrow widths auto-collapse on threshold
crossings (reopenable), an ~80-col floor chip re-measures on every layout change, ctrl+k/ctrl+;
open the cmdk palette (now incl. attention jump, bulk-end mirrors, question triage), alt+↑/↓
cycles the rail order, F6 cycles regions, and the PTY zone passes every key through except exactly
the bound reserved set.

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

## Update History

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
