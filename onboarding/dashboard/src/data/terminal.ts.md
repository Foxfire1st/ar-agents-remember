# dashboard/src/data/terminal.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/terminal.ts`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009`       |
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|
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

### 260707-HFX2-L17 Role-Carrying Attach Transport

Catalog rows expose optional `seatRole`, and `attachSessionToLeaf` requires a role in the JSON body.
The result remains a compact `ok | leaf-taken | error`; `leaf-taken` now means a live owner of the
same leaf-role pair rather than any chat on the leaf.

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
`harness`/`lifecycleId`, optional `leafKey` (the durable qualified leaf id the chat claims, slice L5),
`cwd`, `tmuxName`, timestamps, `status`, optional `terminatedAt`, optional `landedAt`/
`landedReason`/`landedEdge`, and — 260703-L14 — optional
`spawnRole`, the AR_SPAWN_ROLE the backend recorded on the catalog row at spawn, absent on
hand-opened sessions; the documented role examples include architect/orchestrator/strategist/manager/
worker/curator/reviewer/designer) and
`TerminalSessionStatus` is `"running" | "exited" | "landed" | "terminated"`.
`fetchTerminalSessions(base)` GETs
`/api/terminal/sessions` and returns an array or `[]` on failure, letting `Chats` hydrate rows after a
page/dashboard refresh without treating the session list as projected lifecycle truth.
`fetchTerminalSessionsOrNull(base)` uses the same endpoint but returns `null` on non-ok/network failure;
`Chats` uses that variant for cross-tab refresh so a successful empty catalog can clear remote-ended rows
without a transient fetch failure wiping local state.
`openTerminalSession(id, kind, base, harness?, options?)` (slice 6e-2a/6e-2b) is a best-effort
`POST /api/terminal/{id}` asking the server to **spawn + own** the session (the command is
server-resolved from `kind` + the `harness` id, never sent — `kind="harness"` posts `{kind,harness}`);
the optional `options` object sends the friendly label, `lifecycleId`, and (slice L5) `leafKey` so the
backend catalog can persist the same identity the store will hydrate later — `leafKey` claims a leaf at
open (the opener returns `409` when a different running chat already owns it). The caller then opens the
socket — best-effort because the dev bench has no backend yet renders its mock.
`terminateTerminalSession(id, base)` POSTs
`/api/terminal/{id}/terminate` and returns success/failure for the destructive UI action.
`cleanupLandedTerminalSessions(sessionIds, base)` POSTs `/api/terminal/landed-cleanup` and returns
the backend's `{closed, skipped, closedSessions, skippedSessions}` result; the endpoint only closes
rows that are still `status:"landed"` when the backend rechecks them.
`attachSessionToLeaf(sessionId, leafKey, base)` (slice L5) POSTs `/api/terminal/{id}/attach-leaf {leafKey}`
to claim a leaf for an **existing** session (enclosure-free, no respawn): the server is the uniqueness
arbiter, so it maps `200 → "ok"` (bound), `409 → "leaf-taken"` (another running chat owns it), and any
other status / network failure → `"error"` (the `AttachLeafResult` union the Chats page surfaces).
`fetchHarnesses(base)` (slice 6e-2b) GETs `/api/harnesses` → the `HarnessInfo[]`
(id/name/detected) the Chats strip turns into a button per *detected* harness; `[]` on any failure.
`TerminalSocketContext` is the dev/test seam — a provider supplies a fake factory (the bench mock);
`null` in production ⇒ a real same-origin socket.
`bracketedPaste(text)` (slice 6e-3) is a pure helper wrapping text in `ESC[200~…ESC[201~` so a TUI
treats composer-injected context as one paste (used by `Chats`; typed keystrokes stay raw).
`pasteAndConfirm(conn, packageText)` (reopened L6) is the confirmed **draft** delivery loop for the
leaf-bind handoff: it never sends Enter, and it does not trust a single send — a booting harness
(Claude Code loading MCP servers) silently **discards** stdin until its composer mounts, and tmux masks
every readiness signal from the client (it enables bracketed paste and the alternate screen for all
clients unconditionally and exposes no pane-level composer state). Each attempt waits for an
output-quiet window (`whenReady`), snapshots `lastOutputAt()`, sends ONE sanitized bracketed paste, and
polls for the paste's own echo (the draft render or a `[Pasted text #N]` chip) past that baseline
within `PASTE_ECHO_MS` (4s); no echo means the paste was discarded, so it retries after
`PASTE_RETRY_DELAY_MS` until `PASTE_BOOT_DEADLINE_MS` (30s) and resolves `false` so the caller can
surface an unconfirmed-delivery note. The long echo window doubles as a late-echo catch so a paste the
harness queued (rather than discarded) is not re-sent as a duplicate.

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

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: carried binding role in catalog types and attach POST
  bodies, with pair-scoped refusal semantics.

- 2026-07-09T13:07+02:00 — 260707-HFX2-L11 (landed chat archive): `TerminalSessionStatus` now includes
  `landed`, catalog payloads carry landed provenance, and the client exposes
  `cleanupLandedTerminalSessions` for the landed-archive cleanup button. Verification metadata remains
  pinned until closeout stamps the HFX2-L11 commit.

- 2026-07-07T22:21+02:00 — 260707-HFX-L6R4 curator spawnability fix: updated the
  `spawnRole` catalog comment/documentation to include `curator` as a recorded AR_SPAWN_ROLE value.
  Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:32+02:00 — 260707-HFX-L6 L6R2 review remediation: updated the `spawnRole`
  catalog comment/documentation to include `architect` as a recorded AR_SPAWN_ROLE value alongside
  backend orchestrator and the other role seats. Verification metadata pinned until closeout stamps
  the HFX-L6 commit.

- 2026-07-06T23:57:00+02:00 — 260703-L14 (visual hierarchy + chat grouping): `TerminalSessionInfo`
  gained optional `spawnRole` (the AR_SPAWN_ROLE recorded server-side on the catalog row; the
  Chats command-tree grouping key), a read-only wire mirror — no fetch/open call changed.
  Verification metadata pinned until closeout stamps the L14 commit.

- 2026-07-02T16:35+02:00 — Reopened L6 paste-loss fix: added `pasteAndConfirm(conn, packageText)` — the
  confirmed draft-paste loop (quiet-gated attempt → echo confirmation past the pre-paste `lastOutputAt`
  baseline → bounded retry over a 30s boot deadline, never sending Enter). Root cause it covers:
  reproduced against a scratch tmux+claude session, a bracketed paste sent 1.5s after spawn is discarded
  by booting Claude Code while the same paste at ~10s lands as an unsubmitted draft; no readiness signal
  exists to wait on because tmux 3.4 enables `?2004h`/`?1049h` on every client unconditionally.
  Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added the leaf-registry client surface — `TerminalSessionInfo.leafKey`
  and an `OpenTerminalOptions.leafKey` the opener body now sends (claim-at-open), plus
  `attachSessionToLeaf(id, leafKey)` → `POST /api/terminal/{id}/attach-leaf` mapping `200/409/other` to
  the `AttachLeafResult` union `"ok" | "leaf-taken" | "error"` (the server is the uniqueness arbiter).
  Verification metadata pinned until closeout stamps the L5 commit.
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
