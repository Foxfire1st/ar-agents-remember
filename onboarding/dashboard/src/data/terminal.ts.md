# dashboard/src/data/terminal.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/terminal.ts`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T01:25+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The browser half of Mode B2 (slice 6e): a thin, **xterm-agnostic** WebSocket client for the 6d
terminal bridge at `/api/terminal/{session}`. It writes raw PTY bytes into an injected
`TerminalSink` and never imports xterm, so the protocol logic unit-tests against a fake socket —
the mirror of the backend's pure `_apply_terminal_input`. `panels/Terminal.tsx` owns the actual
xterm rendering. It also carries the small Mode B2 control-plane fetches the Chats view needs — the
`openTerminalSession` opener, durable-session hydration (`fetchTerminalSessions`), explicit session
termination (`terminateTerminalSession`), and (slice 6e-2b) the `fetchHarnesses` detection helper.

## Code Commentary

### Logic

`connectTerminal(sessionId, sink, options)` opens a `WebSocket` (via an injectable
`socketFactory`, default `new WebSocket`), sets `binaryType="arraybuffer"`, and pumps it: **binary**
frames → `sink.write(Uint8Array)` (raw VT bytes), a `{type:"exit"}` text frame or a socket close →
`sink.onExit()` **exactly once** (an `ended` guard; `dispose()` pre-sets it so an intentional close
doesn't echo `onExit`). It returns a `TerminalConnection` whose `sendInput`/`sendResize` emit the
`{type:"stdin"|"resize"}` text frames the backend parses — gated on `readyState === 1` (`WS_OPEN`, a
literal so tests need no real `WebSocket`). `sendResize` also **buffers the latest winsize** and
`socket.onopen` replays it once OPEN, so the first `fit()` — which fires before the WS handshake
completes and would otherwise be dropped — still reaches the PTY (the cure for a terminal that
rendered small until a later resize). Likewise (slice 6f) `sendInput` **buffers** any stdin sent before
the socket opens and `socket.onopen` replays it, so a create-then-send — the highlight composer
injecting into a brand-new session — isn't dropped during the handshake; normal typed keystrokes arrive
after open and send directly. The connection also exposes **`whenReady()`** (slice 6f): it tracks PTY
output activity and resolves once output has been quiet for ~700ms (the harness settled at its prompt)
or an 8s timeout — the highlight composer awaits it so a package isn't dropped into a still-**booting**
harness. Pure helpers: `terminalSocketUrl` (same-origin
`ws(s)://<host>/api/terminal/{id}`, id-encoded) and `parseTerminalControl` (`"exit"` | `null`).
`TerminalSessionInfo` mirrors the server catalog payload (`id`, `label`, `kind`, optional
`harness`/`lifecycleId`, `cwd`, `tmuxName`, timestamps, `status`, optional `terminatedAt`) and
`TerminalSessionStatus` is `"running" | "exited" | "terminated"`. `fetchTerminalSessions(base)` GETs
`/api/terminal/sessions` and returns an array or `[]` on failure, letting `Chats` hydrate rows after a
page/dashboard refresh without treating the session list as projected lifecycle truth.
`fetchTerminalSessionsOrNull(base)` uses the same endpoint but returns `null` on non-ok/network failure;
`Chats` uses that variant for cross-tab refresh so a successful empty catalog can clear remote-ended rows
without a transient fetch failure wiping local state.
`openTerminalSession(id, kind, base, harness?, options?)` (slice 6e-2a/6e-2b) is a best-effort
`POST /api/terminal/{id}` asking the server to **spawn + own** the session (the command is
server-resolved from `kind` + the `harness` id, never sent — `kind="harness"` posts `{kind,harness}`);
the optional `options` object sends the friendly label and `lifecycleId` so the backend catalog can
persist the same identity the store will hydrate later. The caller then opens the socket — best-effort
because the dev bench has no backend yet renders its mock. `terminateTerminalSession(id, base)` POSTs
`/api/terminal/{id}/terminate` and returns success/failure for the destructive UI action.
`fetchHarnesses(base)` (slice 6e-2b) GETs `/api/harnesses` → the `HarnessInfo[]`
(id/name/detected) the Chats strip turns into a button per *detected* harness; `[]` on any failure.
`TerminalSocketContext` is the dev/test seam — a provider supplies a fake factory (the bench mock);
`null` in production ⇒ a real same-origin socket.
`bracketedPaste(text)` (slice 6e-3) is a pure helper wrapping text in `ESC[200~…ESC[201~` so a TUI
treats composer-injected context as one paste (used by `Chats`; typed keystrokes stay raw).

### Invariants And Boundaries

Binary-out / JSON-text-in, mirroring 6d-2. The client never decides command safety and never reconnects
by itself; it only reports catalog rows and POSTs explicit open/terminate intents. xterm is never
imported here (keeps it jsdom-safe + unit-testable); the heavy emulator is code-split behind
`panels/Terminal`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The backend WebSocket bridge this connects to (binary out, JSON in). | — | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The serving API that returns terminal catalog rows and accepts terminate requests. | L509-L515; L587-L604 | [serving/app.py](../../../mcp/src/agents_remember/serving/app.py) |
| The xterm wrapper that adapts a `Terminal` to the `TerminalSink`. | — | [panels/Terminal.tsx](../panels/Terminal.tsx) |
| The dev mock socket the bench provides through `TerminalSocketContext`. | — | [dev/mockTerminalSocket.ts](../dev/mockTerminalSocket.ts) |

## Update History

- 2026-06-27T01:25+02:00 — Task 22 follow-up: added `fetchTerminalSessionsOrNull` so cross-tab Chats
  sync can distinguish a successful empty catalog from a failed fetch while keeping
  `fetchTerminalSessions`'s existing `[]`-on-failure API stable. Verification metadata pinned until
  closeout stamps the task-22 follow-up code commit.
- 2026-06-26T23:05+02:00 — Task 22: added catalog-facing types plus `fetchTerminalSessions`, extended
  `openTerminalSession` to POST label/lifecycle metadata, and added `terminateTerminalSession` for the
  destructive session action. Verification metadata pinned until closeout stamps the task-22 code commit.
- 2026-06-19T15:59 — Task 6 slice 6f-1: `sendInput` buffers stdin sent before the socket opens (replayed on `onopen`); added `whenReady()` — an output-settle gate (~700ms quiet, or an 8s timeout) so the highlight composer doesn't drop a package into a still-booting harness. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: `sendResize` now buffers the latest winsize and `socket.onopen` replays it once OPEN, so the first `fit()` (which fires mid-handshake) is no longer dropped — fixes the terminal rendering small until a later resize. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T05:48 — Task 6 slice 6e-3: added the pure `bracketedPaste(text)` helper (`ESC[200~…ESC[201~`) for composer context injection — the `{type:stdin}` send path (`connectTerminal().sendInput`) already existed. Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-18T21:27 — Task 6 slice 6e-2b: added `fetchHarnesses(base)` (`GET /api/harnesses` → `HarnessInfo[]`, `[]` on failure) + a `harness?` arg on `openTerminalSession` (posts `{kind:"harness",harness}`); widened `TerminalOpenKind` to `"terminal"|"harness"`. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T17:40 — Task 6 slice 6e-2a: added `openTerminalSession(id, kind)` — a best-effort `POST /api/terminal/{id}` asking the server to spawn + own the session (command server-resolved from `kind`). Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:50 — Created for task 6 slice 6e-1: the xterm-agnostic terminal WebSocket client (`connectTerminal` + `terminalSocketUrl`/`parseTerminalControl` + `TerminalSocketContext`) — binary PTY bytes in, `{type:stdin|resize}` out, `{type:exit}`/close ends once. Verification metadata pinned to the task base until closeout stamps the 6e-1 code commit.
