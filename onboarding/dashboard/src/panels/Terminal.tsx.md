# dashboard/src/panels/Terminal.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Terminal.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-19T14:05                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The imperative **xterm.js terminal** (slice 6e-1): a render-not-scrape view of the 6d PTY stream.
xterm is a DOM/canvas emulator that probes the canvas on import and cannot mount under jsdom, so —
like the topology constellation canvas — it stays an imperative engine wrapped in a thin React
component via refs, and is **code-split** (lazy-loaded by `Chats.tsx`) out of the initial bundle.

## Code Commentary

### Logic

A single `useEffect` keyed on `sessionId` (+ the context `socketFactory`): it constructs an
`@xterm/xterm` `Terminal`, loads `FitAddon`, `open`s it on the ref div, and `connectTerminal`s
(`data/terminal`) with a sink that `term.write`s incoming bytes and prints `— session ended —` on
exit. `term.onData` → `conn.sendInput`; a `refit()` helper runs `fit.fit()` then
`conn.sendResize(term.cols, term.rows)` — **the one known Mode B2 risk (xterm resize/reflow), kept in
lockstep with the PTY winsize**. Slice 6e-4 hardened it: `refit()` **skips while the host is hidden**
(`display:none` → 0×0, so a kept-mounted-but-hidden session never ships a degenerate winsize) and fires
on mount + the next `requestAnimationFrame` + `document.fonts.ready` (the mono font settles *after* the
effect), on top of the `ResizeObserver` that also re-fits when a hidden layer is shown again. Cleanup disconnects the observer, disposes the data sub + connection
+ terminal. An optional `onConnection(conn|null)` prop (slice 6e-3) hands the live `TerminalConnection`
up to `Chats` on mount and retracts it (`null`) on teardown/switch — the seam the context composer
injects through; held in a ref so a changing callback identity never re-runs the connect effect.
`cursorBlink` follows `html[data-effects]` (off under calm/`?effects=off`) for
deterministic screenshots.

### Conventions

`socketFactory` comes from `TerminalSocketContext` (dev bench supplies a mock; production = `null`
⇒ real same-origin socket). A concrete dark VT `THEME` (xterm needs literal colours, not Panda
tokens); the host div is Panda `css` (`data-testid="terminal-host"`).

### Invariants And Boundaries

xterm never renders in jsdom — there is no render test here; the protocol logic is tested in
`data/terminal.test.ts`. The component is the *only* importer of `@xterm/xterm` (so the lazy chunk
isolates it). Output is rendered, never scraped; the structured "who's doing what" view stays the
observer's job.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The WebSocket client this adapts a `Terminal` onto. | — | [data/terminal.ts](../data/terminal.ts) |
| The view that lazy-loads + mounts this per session. | — | [Chats.tsx](Chats.tsx) |

## Update History

- 2026-06-19T14:05 — Task 6 slice 6e-4: hardened resize — the fit logic became a `refit()` that **skips while the host is hidden** (`display:none`/0×0, so a kept-mounted-but-hidden session never ships a degenerate winsize) and runs on mount + `requestAnimationFrame` + `document.fonts.ready` (the mono font settles after the effect), on top of the `ResizeObserver` that re-fits when a hidden layer is shown. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T05:48 — Task 6 slice 6e-3: added an optional `onConnection(conn|null)` prop that hands the live `TerminalConnection` up to `Chats` (the context composer's stdin-injection seam); a ref keeps a changing callback from re-running the connect effect. Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-18T16:50 — Created for task 6 slice 6e-1: the imperative xterm.js terminal wrapper (FitAddon + ResizeObserver → `sendResize`; `onData` → `sendInput`; exit notice; effects-gated cursor blink). Code-split behind `Chats`. Verification metadata pinned to the task base until closeout stamps the 6e-1 code commit.
