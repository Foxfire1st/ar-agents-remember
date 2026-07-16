# dashboard/src/panels/session-cockpit/ — Sessions Cockpit Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/session-cockpit/`          |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
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
home. This leaf ships the SHELL: a react-resizable-panels rail/stage/inspector group with the
narrow-width rules and the ~80-col floor chip (S2), the cmdk command palette over the extensible
registry (S3), and the tinykeys keyboard-zone/focus wiring (S4). Panel CONTENT is deliberate
labeled scaffolding — L2 fills the rail rows + HeaderStrip, L4 the controls, L5 the real composer
(CM6) + queue, L6 the PtySurface, L7 the inspector/status line.

## Route Model

- `SessionsView.tsx` — the view shell. Root = the scope/testid/marker carrier
  (`sessions--view`, `data-view="sessions"`). A `PanelGroup`
  (`autoSaveId="cockpit.sessions.panels"`) of rail (collapsible, ~280px target via a one-shot
  percentage calibration) / stage (min 35%) / inspector (24%, collapsible), a status-line footer
  with reopen buttons, the non-portal `CommandPalette`, and the `useKeyboardZones` binding. Owns
  the command registry instance + the `CommandContext` actions (panel toggles, focus moves, honest
  L2/L4/L5 stubs), the narrow-width auto-collapse (pure decisions in `data/sessionLayout.ts`), and
  the ~80-col floor chip re-measured from every width-changing path (`onLayout` + a stage-observing
  `ResizeObserver`).
- `CommandPalette.tsx` — the cmdk palette, deliberately **not a portal** (the overlay stays inside
  the scope root; focus return stays local). Two pages: `commands` renders the live registry (the
  one options source); `keys` renders the SAME chord tables tinykeys binds (`data/keymap`), so the
  `?` reference can never drift from the real bindings. Backspace-on-empty returns to commands.
- `useKeyboardZones.ts` — the thin React binding: tinykeys at the window, capture phase, default
  ignore disabled (the zone contract owns suppression), one composed handler per chord string, all
  routing decisions deferred to `data/keymap`.
- `SessionsView.test.tsx` — end-to-end jsdom coverage: zones resolved from real DOM markers,
  tinykeys at the window, palette pages, F6 cycle, PTY non-interception via preventDefault
  observation, floor-chip re-measure paths, and rail calibration.

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
  markers.
- **No animation added** — effects-off/reduced-motion are trivially respected (the resize-handle
  hover transition follows the existing DualPane idiom and is frozen by the global freeze).

## Hot Path Summary

The Sessions cockpit view shell: a keep-alive full-bleed rail/stage/inspector panel group under the
`[data-view="sessions"]` WebTUI scope root — narrow widths auto-collapse on threshold crossings
(reopenable), an ~80-col floor chip re-measures on every layout change, ctrl+k/ctrl+; open the cmdk
palette whose `?` page renders the real keymap tables, F6 cycles regions, and the PTY zone passes
every key through except exactly the bound reserved set.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The shell that registers the view + owns the keep-alive hidden layer and `active` gating. | [cockpit/Cockpit.tsx](agents-remember/dashboard/src/cockpit/Cockpit.tsx) |
| The pure command registry + default command set the palette and chords dispatch into. | [data/commands.ts](agents-remember/dashboard/src/data/commands.ts) |
| The pure narrow-width/floor/calibration decisions the shell feeds measured widths into. | [data/sessionLayout.ts](agents-remember/dashboard/src/data/sessionLayout.ts) |
| The pure keyboard contract (reserved set, zones, chords, focus cycle) this route binds. | [data/keymap/](agents-remember/dashboard/src/data/keymap/reserved.ts) |
| The one WebTUI mapping file scoped to this route's view root. | [styles/webtui.css](agents-remember/dashboard/src/styles/webtui.css) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 (view shell, WebTUI spike, keyboard/palette
  foundation): the new `panels/session-cockpit/` child route — SessionsView (rail/stage/inspector
  PanelGroup + narrow rules + ~80-col floor chip + one-shot ~280px rail calibration),
  CommandPalette (cmdk, non-portal, commands/keys pages), useKeyboardZones (tinykeys binding over
  `data/keymap`), and the end-to-end jsdom suite. Includes the review round-2 fixes (floor chip
  re-measured via `onLayout` + stage observation; rail percentage calibration). Verification
  metadata pinned to the task base until closeout stamps the L1 code commit.
