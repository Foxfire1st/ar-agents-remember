# dashboard/src/panels/Terminal.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Terminal.test.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |                                                  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |                                                  2026-07-24T17:08:25+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Focused Vitest coverage for the imperative `Terminal` wrapper behavior that affects user-visible
scrollback. The real xterm renderer cannot run in jsdom, so this suite mocks xterm (buffer type/baseY
plus a `modes.mouseTrackingMode` getter) and verifies the wrapper still constructs it with the explicit
scrollback configuration and applies the wheel precedence: an app with active mouse tracking keeps the
wheel event un-intercepted (xterm's native mouse-report path — the tmux-hosted case), normal xterm
buffers get viewport scrolling, and mouse-less alternate-buffer agent TUIs get PageUp/PageDown
navigation in Chats and the right-rail chat/terminal panes. 260715-FEUI-L6 adds the group-landmark
naming case (F6) and extends the xterm class mock for the wrapper's new additive surface.

## Code Commentary

### Logic

The suite hoists mock state for the fake `TerminalConnection`, `FitAddon.fit`, and the constructor
options passed to `@xterm/xterm`. `@xterm/addon-fit` is replaced with a tiny class exposing `fit`, and
`@xterm/xterm` is replaced with a class that records constructor options while stubbing `loadAddon`,
`open`, `write`, `onData`, `scrollLines`, and `dispose`, plus a configurable public `buffer.active`
shape (`type` + `baseY`) so the wrapper's normal-buffer and alternate-buffer branches can be tested.
**260715-FEUI-L6 extended the fake xterm class for the new wrapper surface** (mock only — no
product behavior change asserted through it beyond registration safety): a public `options`
record (the live screenReaderMode effect writes it), a `parser.registerOscHandler` stub returning
a disposable (the OSC 133/9 hook registrations), `onBell`/`onTitleChange` disposables, `focus()`,
and `attachCustomKeyEventHandler()`.
The `../data/terminal` module is mocked to
provide a neutral `TerminalSocketContext` plus `connectTerminal` returning the fake connection, so
rendering the component does not open a WebSocket.

The scrollback regression case defines `document.fonts.ready`, renders `<Terminal sessionId="s1" />`, and
asserts that xterm was constructed with `scrollback: 5000`. This pins the wrapper-level setting without
depending on xterm's DOM implementation.

The L6 landmark case ("the group landmark is ALWAYS named", review finding F6) renders without an
`ariaLabel` and asserts `role="group"` + `aria-label="terminal session s1"` (the sessionId
fallback — never an unnamed group), then rerenders with an explicit
`ariaLabel="terminal: scout-claude"` and asserts the explicit label wins.

The wheel regression case renders the terminal under a parent `onWheel`, dispatches a cancelable vertical
wheel event on the terminal host, and asserts that the wrapper calls xterm `scrollLines(-3)`, prevents the
event default, stops parent bubbling, and does not call the connection's `sendInput` when normal
scrollback exists. The alternate-buffer case flips the fake buffer to `type: "alternate"` / `baseY: 0`
and asserts the wrapper sends the PageUp escape sequence (`ESC[5~`) instead of calling `scrollLines`;
this pins the live 8770 failure mode where xterm has no scrollable viewport and its default wheel
handling would send Up/Down arrows. A final wheel case covers small pixel deltas from trackpads: the
wrapper may not scroll a full line yet, but still prevents default/bubbling so partial wheel movement
never reaches terminal stdin.

### Conventions

Mock xterm at the module boundary rather than trying to run the real canvas/DOM emulator in jsdom. Cleanup
after each case and clear mock call history so future terminal option tests can be added independently.

### Invariants And Boundaries

This is component wrapper coverage only. It does not validate backend PTY output, WebSocket framing,
terminal resize behavior, or actual browser scroll physics. It does pin that the React wrapper prevents
wheel events from reaching raw arrow-history stdin while deliberately sending PageUp/PageDown in the
alternate-buffer TUI case. Backend and live xterm integration details remain owned by
`data/terminal.test.ts`, the live xterm integration, and manual/browser validation.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The mocked test replaces xterm (incl. the L6 extensions: `options`, `parser.registerOscHandler`, `onBell`/`onTitleChange`, `focus`, `attachCustomKeyEventHandler`), exposes fake buffer state, and records constructor options / scroll calls instead of mounting the real renderer. | L22-L80 | [Terminal.test.tsx](Terminal.test.tsx) |
| The always-named group-landmark case (fallback name + explicit label wins). | L96-L108 | [Terminal.test.tsx](Terminal.test.tsx) |
| The regression assertions pin `scrollback: 5000`, normal-buffer wheel-to-viewport behavior, alternate-buffer PageUp routing, mouse-tracking non-interception, and partial-pixel swallowing. | L109-L230 | [Terminal.test.tsx](Terminal.test.tsx) |
| The component under test enables the xterm viewport, passes the explicit scrollback option, captures wheel input to either `term.scrollLines` or PageUp/PageDown input depending on buffer state, and names the group host. | L13-L26; L44-L83; L229-L258; L302-L318 | [Terminal.tsx](Terminal.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

## Current L5I Maintenance

The terminal tests now exercise unchanged-box refit suppression, visible-box recovery, clipped-row
correction, and platform-correct selection copy. In particular they prove a copied selection is
released so a second interrupt chord is delivered to the running terminal.

## Update History

- 2026-07-24T13:17:17Z — Curator: recorded terminal geometry and copy-versus-interrupt regression
  coverage; verification fields remain pre-commit.

- 2026-07-17T04:20+02:00 — 260715-FEUI-L6: extended the fake xterm class for the wrapper's new
  surface (`options` record, `parser.registerOscHandler`, `onBell`/`onTitleChange` disposables,
  `focus`, `attachCustomKeyEventHandler`) and added the always-named group-landmark case (review
  finding F6: `role="group"`, sessionId-fallback `aria-label`, explicit label wins on rerender).
  Mock surface only — the wheel/scrollback cases are untouched. Verification metadata pinned to
  the leaf base until closeout stamps the L6 code commit.
- 2026-07-02T16:35+02:00 — Reopened L6 wheel-precedence fix: the fake xterm gained a `modes` getter
  (`mouseTrackingMode`, reset to `"none"` per test) and a case pinning that an active mouse-tracking
  mode leaves the wheel event un-intercepted (no `scrollLines`, no synthesized input, default not
  prevented, propagation intact) so xterm's native mouse-report path owns it. Verification metadata
  pinned until closeout stamps the follow-up commit.
- 2026-07-02T15:03+02:00 — Reopened L6 served-page follow-up: the fake xterm buffer now exposes
  normal vs alternate state, and coverage asserts alternate-buffer wheel input sends PageUp instead of
  calling xterm `scrollLines` or leaking arrow-history input. Verification metadata pinned until
  closeout stamps the source commit.
- 2026-07-02T14:28+02:00 — Reopened L6 wheel follow-up: extended the focused component test to assert
  that wheel input calls xterm `scrollLines`, partial pixel deltas are swallowed, default/bubbling is
  prevented, and wheel movement never reaches terminal stdin. Verification metadata pinned until closeout
  stamps the source commit.
- 2026-07-02T13:07+02:00 — Created for the reopened L6 follow-up: focused component coverage for the
  terminal scrollback regression. Verification metadata is pending until closeout stamps the source commit.
