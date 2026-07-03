# dashboard/src/panels/Terminal.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Terminal.test.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-02T16:35+02:00                           |
| lastVerifiedCommitHash |                                                  `ad30dd38c3dcfa13fb85f44b281488499e92519a`|
| lastVerifiedCommitDate |                                                  2026-07-03T08:10:19+02:00|
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
navigation in Chats and the right-rail chat/terminal panes.

## Code Commentary

### Logic

The suite hoists mock state for the fake `TerminalConnection`, `FitAddon.fit`, and the constructor
options passed to `@xterm/xterm`. `@xterm/addon-fit` is replaced with a tiny class exposing `fit`, and
`@xterm/xterm` is replaced with a class that records constructor options while stubbing `loadAddon`,
`open`, `write`, `onData`, `scrollLines`, and `dispose`, plus a configurable public `buffer.active`
shape (`type` + `baseY`) so the wrapper's normal-buffer and alternate-buffer branches can be tested.
The `../data/terminal` module is mocked to
provide a neutral `TerminalSocketContext` plus `connectTerminal` returning the fake connection, so
rendering the component does not open a WebSocket.

The scrollback regression case defines `document.fonts.ready`, renders `<Terminal sessionId="s1" />`, and
asserts that xterm was constructed with `scrollback: 5000`. This pins the wrapper-level setting without
depending on xterm's DOM implementation.

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
| The mocked test replaces xterm, exposes fake buffer state, and records constructor options / scroll calls instead of mounting the real renderer. | L22-L57; L59-L65 | [Terminal.test.tsx](Terminal.test.tsx) |
| The regression assertions pin `scrollback: 5000`, normal-buffer wheel-to-viewport behavior, alternate-buffer PageUp routing, and partial-pixel swallowing. | L73-L157 | [Terminal.test.tsx](Terminal.test.tsx) |
| The component under test enables the xterm viewport, passes the explicit scrollback option, and captures wheel input to either `term.scrollLines` or PageUp/PageDown input depending on buffer state. | L13-L26; L44-L82; L104-L135 | [Terminal.tsx](Terminal.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

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
