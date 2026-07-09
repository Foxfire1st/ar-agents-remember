# dashboard/src/panels/Terminal.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Terminal.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-02T16:35+02:00                           |
| lastVerifiedCommitHash | `c392985424896e9f392507295a23c4902d0c0696`       |
| lastVerifiedCommitDate | 2026-07-09T14:31:11+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The imperative **xterm.js terminal** (slice 6e-1): a render-not-scrape view of the 6d PTY stream.
xterm is a DOM/canvas emulator that probes the canvas on import and cannot mount under jsdom, so —
like the topology constellation canvas — it stays an imperative engine wrapped in a thin React
component via refs, and is **code-split** (lazy-loaded by `Chats.tsx`) out of the initial bundle. The
reopened L6 follow-up makes the terminal scrollback explicit and captures wheel input with a clear
precedence: an application that tracks the mouse owns the wheel (xterm reports it as mouse events —
the tmux-hosted-session path), normal-buffer scrollback scrolls the xterm viewport, and only an
alternate-buffer pane without mouse tracking receives synthesized PageUp/PageDown navigation.

## Code Commentary

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

### Conventions

`socketFactory` comes from `TerminalSocketContext` (dev bench supplies a mock; production = `null`
⇒ real same-origin socket). A concrete dark VT `THEME` (xterm needs literal colours, not Panda
tokens); the host div is Panda `css` (`data-testid="terminal-host"`), with xterm descendant selectors for
height and viewport scrollability.

### Invariants And Boundaries

xterm never renders in jsdom — there is no render test here; the protocol logic is tested in
`data/terminal.test.ts`, while `Terminal.test.tsx` mocks xterm to pin wrapper options and host wheel
behavior that affect scrollback. The component is the *only* importer of `@xterm/xterm` (so the lazy
chunk isolates it). Output is rendered, never scraped; the structured "who's doing what" view stays the
observer's job.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The WebSocket client this adapts a `Terminal` onto. | — | [data/terminal.ts](../data/terminal.ts) |
| The view that lazy-loads + mounts this per session. | — | [Chats.tsx](Chats.tsx) |
| The wrapper enables xterm viewport scrolling, creates the terminal with explicit scrollback, defers wheel to xterm when mouse tracking is active, scrolls the viewport for normal scrollback, and maps mouse-less alternate-buffer wheel input to PageUp/PageDown. | L13-L26; L44-L89; L110-L155 | [Terminal.tsx](Terminal.tsx) |
| The focused component test mocks xterm (including `modes.mouseTrackingMode`) and asserts scrollback, normal-buffer wheel scrolling, mouse-tracking non-interception, alternate-buffer PageUp routing, and partial-pixel swallowing. | L22-L64; L80-L200 | [Terminal.test.tsx](Terminal.test.tsx) |

## Update History

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
