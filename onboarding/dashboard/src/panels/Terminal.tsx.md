# dashboard/src/panels/Terminal.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Terminal.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels overview](overview.md)

## 260731-EFA-L8 Change

The xterm session machinery moved to `panels/terminalSession.ts` (the component
keeps the wrapper), and the e2e repair fixed a genuine headless-focus bug: palette
focus on the terminal landed on the host while xterm's textarea stayed inactive.
Focus is now delegated via a rAF deferral with a `termRef.focus()` fallback. The
mounted-scrollback and one-reattach contracts are unchanged.

## Purpose

The imperative xterm.js wrapper over a same-origin PTY socket. It is lazy-loaded by the canonical
cockpit's PtySurface and contextual RailChat, reports resize/freshness/harvest hooks, and preserves
normal/mouse/alternate-buffer wheel precedence. Controlled panes expose a runner line-log; legacy raw
panes may host a vendor TUI. This component is not a structured conversation renderer.

FEUI-L8 defers final xterm object disposal by one task only after application listeners and socket
ownership are detached. That narrow workaround is necessary because xterm 5.5 leaves an uncancelled
Viewport timer during React StrictMode probe teardown; synchronous disposal otherwise reads an
already-disposed RenderService.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

The mounted xterm surface now observes `servingBuild.bootedAt` and asks its current connection to
reattach once for each changed boot identity. The first observed identity adopts an already-open
socket without replacement; later identities may supersede stale OPEN or CONNECTING sockets.
Reattach preserves the xterm instance and scrollback and has no timer or generic retry loop.
Conditional ref cleanup prevents stale teardown from erasing a replacement connection.

### Logic

A single `useEffect` keyed on `sessionId` (+ the context `socketFactory`): it constructs an
`@xterm/xterm` `Terminal`, loads `FitAddon`, `open`s it on the ref div, and `connectTerminal`s
(`data/terminal`) with a sink that `term.write`s incoming bytes and prints `— session ended —` on
exit. The terminal is created with `scrollback: 5000`, and the host CSS lets the internal
`.xterm-viewport` scroll vertically while the wrapper itself still clips to the pane. `wheelScrollLines`
normalizes pixel/line/page wheel deltas to xterm line counts and carries a pixel remainder so small
trackpad deltas are swallowed until they add up to a line. After `term.open(node)`, the host installs a
capture-phase `wheel` listener with a three-way precedence. First, when
`term.modes.mouseTrackingMode !== "none"` the handler returns WITHOUT intercepting: the application
requested mouse tracking, so xterm's native path reports the wheel as mouse events — every hosted
session runs behind a tmux client (which always presents the alternate screen), and with the backend's
per-session `mouse on` tmux scrolls its own pane history for normal-buffer TUIs (Codex) and passes the
events through to panes whose app tracks the mouse itself (Claude Code). Second, when
`term.buffer.active` is the normal buffer and `baseY > 0`, the handler calls `term.scrollLines(...)` so
xterm moves its viewport. Third (alternate buffer, no mouse tracking), the handler accumulates wheel
lines in three-line steps and sends PageUp/PageDown escape sequences (`ESC[5~` / `ESC[6~`) through the
live `TerminalConnection`; synthesized keys are a last resort because they only scroll TUIs that happen
to bind them. The listener prevents the browser default when the event is cancelable and stops
propagation in the two intercepting paths only. `term.onData` →
`conn.sendInput`; a `refit()` helper runs `fit.fit()` then
`conn.sendResize(term.cols, term.rows)` — **the one known Mode B2 risk (xterm resize/reflow), kept in
lockstep with the PTY winsize**. Slice 6e-4 hardened it: `refit()` **skips while the host is hidden**
(`display:none` → 0×0, so a kept-mounted-but-hidden session never ships a degenerate winsize) and fires
on mount + the next `requestAnimationFrame` + `document.fonts.ready` (the mono font settles *after* the
effect), on top of the `ResizeObserver` that also re-fits when a hidden layer is shown again. Cleanup
removes the host wheel listener, disconnects the observer, and disposes the data sub + connection +
terminal. An optional `onConnection(conn|null)` prop (slice 6e-3) hands the live `TerminalConnection`
up to `Chats` on mount and retracts it (`null`) on teardown/switch — the seam the context composer
injects through; held in a ref so a changing callback identity never re-runs the connect effect.
`cursorBlink` follows `html[data-effects]` (off under calm/`?effects=off`) for
deterministic screenshots. **HFX2-L11** adds an optional `readOnly` prop (default `false`): when
`true`, the host `wheel` handler's alternate-buffer PageUp/PageDown send is gated by `!readOnly`, and
`term.onData` is never subscribed (`dataSub` is `null` and skipped on cleanup) — so a landed/archived
seat's terminal renders output and remains scrollable/inspectable but cannot forward any keystroke or
wheel-driven input to the PTY. `readOnly` is listed in the effect's dependency array so a prop flip
tears down and reconnects the data subscription correctly.

### 260715-FEUI-L6 Cockpit Pane Engine (Additive Props)

- **PtySurface relationship:** cockpit panes render Terminal THROUGH
  `session-cockpit/PtySurface.tsx` — PtySurface owns the two-archetype switch, keep-alive layers,
  and pane chrome; this component stays the one xterm engine. Chats/RailChat call sites are
  unchanged in behavior (they gained only `ariaLabel`).
- **Accessible-name guarantee (F6)** cit:([`aria-label`, `tabIndex`], dashboard/src/panels/Terminal.tsx:183-183): the host div is now `role="group"` with
  `aria-label={ariaLabel ?? `terminal session ${sessionId}`}` — the landmark can NEVER be unnamed
  regardless of caller. The cockpit passes the full `paneAccessibleName` (label + harness +
  state); legacy views pass `terminal: <label>`. The host also carries `tabIndex={-1}` with focus
  delegation into xterm's own textarea (`onFocus` → `term.focus()` when the host itself was the
  target) — the focus-terminal command / region routing lands here.
- **`screenReaderMode` (R2), applied LIVE** (L149-L155, L168): a dedicated effect mutates
  `term.options.screenReaderMode` on the existing instance — never a teardown/reconnect; the
  creation option seeds from a ref so the connect effect needn't depend on it.
- **`renderer` (R1 / master OQ-B)** (L121, L134-L136, L274-L296): `"dom"` (default — the measured baseline) or
  `"webgl"`, which lazily imports `@xterm/addon-webgl` (its own code-split chunk) and demotes
  itself back to DOM on load failure, constructor throw, or `onContextLoss` — never a dead pane.
  `renderer` joins the effect deps; it is constant at every current call site, so no new teardown
  path exists in practice.
- **Stream-observation hooks (R7)** (L85-L96, L179-L189): `TerminalStreamHooks`
  (`onBell`/`onTitle`/`onOsc133`/`onOsc9`) registered unconditionally-cheap via `term.onBell`,
  `term.onTitleChange`, and `parser.registerOscHandler(133)`/`(9)` — the OSC handlers `return
  false` (observe only, never swallowing the sequence from other handlers). PtySurface wires them
  ONLY for legacy-raw panes; held in refs so changing identities never re-run the effect.
- **`keyEventFilter`** (L141-L143, L218-L226): when provided, `term.attachCustomKeyEventHandler` gives the
  caller a veto — PtySurface's `reservedChordFilter` returns false only for the BOUND reserved
  set, so a reserved chord is never consumed by (or leaked into) the pane even when the
  window-capture tinykeys layer is inactive.
- **Freshness/floor reporting**: `onOutput` fires on every PTY write chunk (the caller throttles
  → `lastOutputAt`); `onSocketState` relays the socket's own
  `connected`/`reconnecting`/`dropped` (from `data/terminal.ts`'s additive option; a deliberate
  `dispose()` reports nothing);
  `onResizeCols(term.cols)` fires after EVERY successful `refit()` cit:(["const onResizeColsRef = useRef(props.onResizeCols);", "const refit = (force = false) => {", "refit();"], dashboard/src/panels/Terminal.tsx:76-76; dashboard/src/panels/terminalSession.ts:341-341; dashboard/src/panels/terminalSession.ts:379-379) — the R8 ~80-col floor
  chip's real-pane truth.

### Conventions

`socketFactory` comes from `TerminalSocketContext` (dev bench supplies a mock; production = `null`
⇒ real same-origin socket). A concrete dark VT `THEME` (xterm needs literal colours, not Panda
tokens); the host div is Panda `css` (`data-testid="terminal-host"`), with xterm descendant selectors for
height and viewport scrollability. **V31 (260718-CHATS-L5P):** the host `background` migrated from the
hardcoded `#070b0f` literal to the `well` token (`panels/Terminal.tsx:19`) — the same token the FB7.1
conversation stage/composer now use, so the "pty well" is one source of truth. (The xterm `THEME` still
carries literal colours, which xterm requires.)

### Invariants And Boundaries

xterm never renders in jsdom — there is no render test here; the protocol logic is tested in
`data/terminal.test.ts`, while `Terminal.test.tsx` mocks xterm to pin wrapper options, host wheel
behavior, and the L6 surface (hooks, filter, live screenReaderMode, named landmark). The component
is the *only* product importer of `@xterm/xterm` (so the lazy chunk isolates it; the dev-only
bench probe imports it inside `/dev/*`, which never ships). Output is rendered, never scraped; the
structured "who's doing what" view stays the observer's job. The refit/keep-alive rules are a
PRESERVED contract: refit skips hidden hosts, runs mount + rAF + `fonts.ready` + ResizeObserver,
and keeps the PTY winsize in lockstep — L6 changed none of it (only the additive `onResizeCols`
call after `fit.fit()`).

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The WebSocket client this adapts a `Terminal` onto (incl. the L6 `onSocketState` option). | `onSocketState` | dashboard/src/data/terminal.ts:55-55 |
| The canonical keep-alive owner lazy-loads and mounts this per inspectable session. | `PtySurface` | dashboard/src/panels/session-cockpit/PtySurface.tsx:136-336 |
| The cockpit surface that mounts this per seat: archetypes, keep-alive layers, hooks/filter wiring, accessible names. | `PTY_RENDERER` | dashboard/src/panels/session-cockpit/PtySurface.tsx:39-39 |
| The wrapper handles wheel input with three-way precedence: app mouse tracking passes through, normal-buffer viewport scrolls, and mouse-less alternate-buffer wheel input maps to PageUp/PageDown. | `handleWheel` | dashboard/src/panels/terminalSession.ts:272-301 |
| The L6 additive surface includes the always-named group landmark (`role="group"` + `aria-label` fallback). | `tabIndex` | dashboard/src/panels/Terminal.tsx:183-183 |
| The focused component test mocks xterm (extended for options/parser/onBell/onTitleChange/attachCustomKeyEventHandler) and asserts the always-named landmark plus scrollback. | "the group landmark is ALWAYS named", `attachCustomKeyEventHandler`, `onBell` | dashboard/src/panels/Terminal.test.tsx:74-76; dashboard/src/panels/Terminal.test.tsx:95-97; dashboard/src/panels/Terminal.test.tsx:132-143 |
| The renderer measurement behind the DOM default (master OQ-B). | `PtyRenderBench` | dashboard/src/dev/PtyRenderBench.tsx:83-164 |

## FEUI-L8 Reviewed Candidate Delta

Defers only xterm object disposal by one task after detaching application listeners and the socket. This is necessary for xterm 5.5's uncancelled Viewport timer during React StrictMode probe teardown; it prevents a disposed RenderService read without masking transport cleanup.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Current L5I Maintenance

The terminal now preserves the interrupt chord when no real selection is being copied: copy uses
the platform-native modifier, snapshots selection bytes, and clears the range after a copy so the
next Ctrl+C/Cmd+C can reach the PTY. `plainTextSelection` promotes an ordinary drag to xterm's
selection path only for terminals whose application lacks useful mouse gestures. Refit is keyed to
the last fitted visible box, corrects only genuinely overflowing rows, and does not churn scroll or
PTY winsize on a keep-alive re-show; disposal is synchronous after all listeners are detached.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the headless-focus delegation fix and the terminalSession extraction. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the seven `n/a`-anchor
  table citations and the two superseded `(L…​)` prose citations with exact frozen-source anchors
  and fixer-generated ranges (`data/terminal.ts:55`, `PtySurface.tsx:39,136-336`,
  `Terminal.tsx:316-338,451`, `Terminal.test.tsx:74-76;95-97;132-143`,
  `dev/PtyRenderBench.tsx:83-164`); the exact non-fixing check returns zero findings.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 2 stale self-citations. `renderer`
  cited L190-L212, which is now the serving-boot reattach effect and the xterm constructor; the
  prop default is L121, its typed doc L134-L136, and the lazy `@xterm/addon-webgl` escalation with
  its load-failure / constructor-throw / `onContextLoss` demotion is L274-L296. `keyEventFilter`
  cited L173-L177, now unrelated refs (`termRef`, `screenReaderModeRef`); the prop contract is
  L141-L143 and the `attachCustomKeyEventHandler` veto that consults `keyEventFilterRef` is
  L218-L226.

- 2026-07-24T13:17:17Z — Curator: corrected xterm copy/interrupt, selection, refit, and cleanup
  invariants; verification fields remain pre-commit.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the V31 well-token migration — the host
  `background` `#070b0f` literal → the `well` token (shared with the FB7.1 conversation stage/composer).
  No behavior change; the xterm THEME keeps its literal colours. Verification pinned to the leaf base
  (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-18T12:43+02:00 — FEUI-L9R: documented xterm-preserving, once-per-serving-boot socket
  reattach and stale-ref-safe teardown; verification metadata remains pinned pending closeout.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (PTY stage surface): additive cockpit-pane surface —
  `renderer` prop (DOM default by OQ-B measurement; lazy webgl escalation demoting to DOM on
  failure/context loss), opt-in `screenReaderMode` applied LIVE via options mutation (never a
  reconnect), the always-named `role="group"` host (`ariaLabel` with the
  `terminal session <sessionId>` fallback — review finding F6) + focus delegation into xterm,
  `keyEventFilter` (reserved-chord veto seam), observe-only `TerminalStreamHooks`
  (onBell/onTitleChange/OSC 133/OSC 9, `return false`), and freshness/floor reporting
  (`onOutput`, `onSocketState`, `onResizeCols` after every fit). The refit/keep-alive block is
  unchanged; all new props default to prior behavior, Chats/RailChat call sites byte-compatible
  (plus `ariaLabel`). Cockpit panes mount this through `PtySurface`. Verification metadata pinned
  to the leaf base until closeout stamps the L6 code commit.
- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive): added the `readOnly` prop so a landed/
  archived seat's terminal stays fully inspectable (output rendered, scrollback intact) but cannot
  send input — `onData` is not subscribed and the wheel-driven PageUp/PageDown send is gated when
  `readOnly` is true. `Chats.tsx` passes `readOnly` for non-`running` sessions. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-02T16:35+02:00 — Reopened L6 wheel-precedence fix: the wheel handler now yields to xterm's
  native mouse-report path when `term.modes.mouseTrackingMode !== "none"` instead of synthesizing
  PageUp/PageDown for every alternate-buffer pane. Rationale: tmux hosts every dashboard session and
  always presents the alternate screen to the client, so synthesized keys only scrolled TUIs that bind
  PageUp/PageDown (Claude Code yes, Codex no); with the backend's tmux `mouse on`, mouse reports scroll
  tmux pane history (Codex) or pass through to the TUI (Claude Code). Verification metadata pinned until
  closeout stamps the follow-up commit.
- 2026-07-02T15:03+02:00 — Reopened L6 served-page follow-up: live 8770 inspection showed agent
  sessions in xterm's alternate buffer (`scrollHeight == clientHeight`), so wheel input now keeps normal
  viewport scrolling for real scrollback but maps alternate-buffer wheel steps to PageUp/PageDown instead
  of xterm's default Up/Down arrow history mapping. Verification metadata pinned until closeout stamps
  the follow-up commit.
- 2026-07-02T14:28+02:00 — Reopened L6 wheel follow-up: host wheel events now scroll the xterm
  viewport via `term.scrollLines(...)`, swallow partial pixel deltas, and stop before xterm can convert
  them into PTY up/down input. The `scrollback: 5000` setting remains in place. Verification metadata
  pinned until closeout stamps the follow-up commit.
- 2026-07-02T13:07+02:00 — Reopened L6 follow-up: restored chat/terminal scrollback by enabling the
  internal xterm viewport to scroll and setting `scrollback: 5000` on the xterm instance. Added focused
  component coverage in `Terminal.test.tsx`. Verification metadata pinned until closeout stamps the
  follow-up commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: hardened resize — the fit logic became a `refit()` that **skips while the host is hidden** (`display:none`/0×0, so a kept-mounted-but-hidden session never ships a degenerate winsize) and runs on mount + `requestAnimationFrame` + `document.fonts.ready` (the mono font settles after the effect), on top of the `ResizeObserver` that re-fits when a hidden layer is shown. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T05:48 — Task 6 slice 6e-3: added an optional `onConnection(conn|null)` prop that hands the live `TerminalConnection` up to `Chats` (the context composer's stdin-injection seam); a ref keeps a changing callback from re-running the connect effect. Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-18T16:50 — Created for task 6 slice 6e-1: the imperative xterm.js terminal wrapper (FitAddon + ResizeObserver → `sendResize`; `onData` → `sendInput`; exit notice; effects-gated cursor blink). Code-split behind `Chats`. Verification metadata pinned to the task base until closeout stamps the 6e-1 code commit.
