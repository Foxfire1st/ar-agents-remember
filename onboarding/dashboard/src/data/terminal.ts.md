# dashboard/src/data/terminal.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/terminal.ts`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T15:22+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The browser half of Mode B2 (slice 6e): a thin, **xterm-agnostic** WebSocket client for the 6d
terminal bridge at `/api/terminal/{session}`. It writes raw PTY bytes into an injected
`TerminalSink` and never imports xterm, so the protocol logic unit-tests against a fake socket —
the mirror of the backend's pure `_apply_terminal_input`. `panels/Terminal.tsx` owns the actual
xterm rendering. It re-exports the sole terminal opener from `terminalOpen.ts`, and carries
durable-session hydration, explicit termination, and compatibility harness-fetch facades. Strict pre-session harness validation and
result classification now belong to `harnessCatalog.ts`; the chooser's request lifetime belongs to
`useHarnessCatalogRead.ts`.

## Code Commentary

### FEUI MX-FIX-2 Authoritative Open Split

The old boolean, best-effort opener and its dev-bench fail-open comment were removed. This module
now re-exports `openTerminalSession`, its discriminated result/failure types, and stable failure copy
from `terminalOpen.ts`; it does not retain a second POST implementation. Transport/WebSocket,
catalog reads, attach, terminate, and cleanup responsibilities remain here unchanged.

### FEUI-L9R Reviewed Candidate Delta

The current connection contract separates a dropped WebSocket transport from durable terminal
exit. A close reports `dropped` but does not call `sink.onExit`; only the server's `{type:"exit"}`
control frame ends the session. `TerminalConnection.reattach()` is an explicit, once-per-serving-
boot action that may supersede stale CONNECTING or OPEN sockets, reports `reconnecting`, replays the
latest resize before buffered input, and ignores callbacks from superseded sockets. There is no
timer-driven reconnect loop. Harness validation now belongs to `harnessCatalog.ts`; its narrow
pre-session row is only `id`/`name`/`detected`, with no invented adapter `control` state.

### 260707-HFX2-L17 Role-Carrying Attach Transport

Catalog rows expose optional `seatRole`, and `attachSessionToLeaf` requires a role in the JSON body.
The result remains a compact `ok | leaf-taken | error`; `leaf-taken` now means a live owner of the
same leaf-role pair rather than any chat on the leaf.

### Logic

`connectTerminal(sessionId, sink, options)` opens a `WebSocket` (via an injectable
`socketFactory`, default `new WebSocket`), sets `binaryType="arraybuffer"`, and pumps it: **binary**
frames → `sink.write(Uint8Array)` (raw VT bytes); only a `{type:"exit"}` text frame calls
`sink.onExit()` **exactly once**. A socket close is transport loss and reports `dropped` without
ending the durable session; `dispose()` intentionally reports neither. It returns a
`TerminalConnection` whose `sendInput`/`sendResize` emit the
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
**The catalog-row wire shape moved to `types/terminalCatalog.ts`** (260715-FEUI-L2 R4: the
cockpit consumes the FULL `TerminalCatalogEntry.to_json()` mirror). This module RE-EXPORTS the
types so existing consumers keep their import site — `TerminalSessionInfo` is now an alias of the
full `TerminalCatalogRow` (identity/transport, leaf/seat identity, spawn + level provenance, the
requested model/effort pair, control metadata, liveness evidence, retirement/landing provenance,
turn state), and `TerminalOpenKind`/`TerminalSessionStatus`/`HarnessControlState`/
`HarnessActivityState`/`HarnessAcceptanceState`/`SeatTurnState`/`TerminalLivenessEvidence` are
re-exported from there; `fetchTerminalSessions(OrNull)` now returns `TerminalCatalogRow[]`.
`TerminalSessionStatus` remains `"running" | "exited" | "landed" | "terminated"`.
`fetchTerminalSessions(base)` GETs
`/api/terminal/sessions` and returns an array or `[]` on failure, letting `Chats` hydrate rows after a
page/dashboard refresh without treating the session list as projected lifecycle truth.
`fetchTerminalSessionsOrNull(base)` uses the same endpoint but returns `null` on non-ok/network failure;
`Chats` uses that variant for cross-tab refresh so a successful empty catalog can clear remote-ended rows
without a transient fetch failure wiping local state.
`openTerminalSession(id, kind, base, harness?, options?)` is re-exported from `terminalOpen.ts`, the
sole `POST /api/terminal/{id}` authority. It returns a discriminated opened/failed result, validates
the exact id/kind/harness identity, and exposes the accepted server row; callers may not open a
socket or materialize local state from request truth alone. The dev bench answers that same HTTP
contract through its explicit injector rather than selecting a local-success fallback.
**(260715-FEUI-L3 R5)** `OpenTerminalOptions` also carries the launch pair — optional `model` +
`effort` threaded into the POST body: a COMPLETE pair or neither knob (a partial pair is refused
synchronously by the server as `400 launch-selection-invalid`; catalog validity is NOT checked at
open time — a bad-but-complete pair opens 200/'starting' and fails asynchronously on every native
harness). The launch flow's `openHostedSession` delegates to the same opener and maps its result into
the established launch outcome grammar.
`terminateTerminalSession(id, base)` POSTs
`/api/terminal/{id}/terminate` and returns success/failure for the destructive UI action.
`cleanupLandedTerminalSessions(sessionIds, base)` POSTs `/api/terminal/landed-cleanup` and returns
the backend's `{closed, skipped, closedSessions, skippedSessions}` result; the endpoint only closes
rows that are still `status:"landed"` when the backend rechecks them.
`attachSessionToLeaf(sessionId, leafKey, base)` (slice L5) POSTs `/api/terminal/{id}/attach-leaf {leafKey}`
to claim a leaf for an **existing** session (enclosure-free, no respawn): the server is the uniqueness
arbiter, so it maps `200 → "ok"` (bound), `409 → "leaf-taken"` (another running chat owns it), and any
other status / network failure → `"error"` (the `AttachLeafResult` union the Chats page surfaces).
Legacy `fetchHarnesses(base)` remains a compatibility wrapper, but current harness discovery lives
in `harnessCatalog.ts`: the validated pre-session row contains only id/name/detected and the reader
distinguishes network, HTTP, protocol, empty, and ready results. LaunchFlow consumes that reader via
its request-owning hook rather than projecting adapter process state before a session exists.
`TerminalSocketContext` is the dev/test seam — a provider supplies a fake factory (the bench mock);
`null` in production ⇒ a real same-origin socket.
**`ConnectTerminalOptions.onSocketState`** (260715-FEUI-L6, R15 freshness wiring, L36-L43) is an
additive hook reporting the socket's OWN truth: `"connected"` fires from `socket.onopen` (the
real handshake), `"dropped"` from the shared `end()` path (a non-deliberate close/exit). A
deliberate `dispose()` reports NOTHING — a removed pane is not a dropped one. `"reconnecting"`
fires only for an explicit boot-owned `reattach`; no timer or background retry exists. The cockpit routes it into
`sessionCockpitStore.setPtyWs` (per-pane `freshness.ptyWs`).
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

### Conventions

WebSocket constants remain numeric literals for jsdom tests, connection callbacks are identity
gated, and all retry/reattach initiation is caller-owned.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

### 2026-07-24 Curator Delta

Terminal-session catalog reads now share an in-flight boot/poll request and enforce a 10-second socket
bound. A timed-out beat resolves through the existing `null` failure path and releases the slot for the
next authoritative read.

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
| The backend WebSocket bridge this connects to (binary out, JSON in). | "async def stream_events" | mcp/src/agents_remember/serving/app.py:315-315 |
| The serving API that returns terminal catalog rows and accepts terminate requests. | "async def stream_events" | mcp/src/agents_remember/serving/app.py:315-315 |
| The xterm wrapper that adapts a `Terminal` to the `TerminalSink`. | "export function Terminal" | dashboard/src/panels/Terminal.tsx:117-117 |
| The dev mock socket the bench provides through `TerminalSocketContext`. | `TerminalSocketContext` | dashboard/src/data/terminal.ts:500-500 |
| The freshness consumers: Terminal forwards `onSocketState`, PtySurface routes it into the cockpit store. | `onSocketState` | dashboard/src/panels/Terminal.tsx:151-151 |
| The per-pane `freshness.ptyWs` field this hook feeds. | "export type EvidenceTier" | dashboard/src/data/sessionCockpitStore.ts:18-18 |
| The launch flow consumes the narrow catalog reader through an explicit request-owning hook. | "export function LaunchFlow" | dashboard/src/panels/session-cockpit/LaunchFlow.tsx:177-177 |
| The typed narrow harness reader distinguishes transport, protocol, empty, and ready results. | "export function readHarnessCatalog" | dashboard/src/data/harnessCatalog.ts:45-45 |
| The classifying open client the launch flow uses instead of this module's boolean opener. | "export function launchableEfforts" | dashboard/src/data/launchFlow.ts:34-34 |

### 260713-PHA-L5 Protocol Catalog Fields

Terminal session API types expose additive adapter state, identity, interaction, sequence, and raw
detail fields. The WebSocket and paste helpers remain ordinary-terminal mechanics; hosted delivery
uses correlated backend protocol receipts.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-24T13:17:50Z — Added terminal-catalog single-flight and timeout semantics. Verification
  hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: removed the boolean fail-open implementation and
  documented this module as the compatibility facade over `terminalOpen.ts`, with one POST,
  discriminated failure, exact response identity, and no dev/production local-success path.
  Verification metadata remains pinned until closeout stamps the code commit.

- 2026-07-18T12:43+02:00 — FEUI-L9R: corrected current transport truth: close is dropped-only,
  server exit is durable termination, explicit reattach consumes one serving-boot identity and
  rejects stale socket callbacks, and pre-session harness discovery moved to the narrow reader.
  Verification metadata remains pinned pending candidate closeout.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.
- 2026-07-17T06:10+02:00 — 260715-FEUI-L3 (R5): additive launch-selection surface —
  `OpenTerminalOptions` gained optional `model`/`effort` threaded into the POST body (complete
  pair or neither; partial pairs are the server's synchronous 400, catalog validity is not
  checked at open time), `HarnessInfo` gained the optional `control` adapter-status word, and
  `fetchHarnessesOrNull` distinguishes a failed harness read (`null`) from an empty list so the
  launch flow fails loudly (`fetchHarnesses` now delegates to it). WebSocket/paste/terminate/
  cleanup mechanics untouched; the launch flow's own opener is `data/launchFlow.ts`.
  Verification metadata pinned to the leaf base until closeout stamps the L3 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (R15 freshness wiring): added the additive
  `ConnectTerminalOptions.onSocketState` hook — `connected` on the WS handshake, `dropped` on a
  non-deliberate close/exit, NOTHING on a deliberate `dispose()` (a removed pane is not a dropped
  one), and `reconnecting` never fires because no auto-reconnect exists. All other mechanics
  untouched (6 lines). Verification metadata pinned to the leaf base until closeout stamps the L6
  code commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 (R4): the catalog wire shape moved out to
  `types/terminalCatalog.ts` (the full `TerminalCatalogEntry.to_json()` mirror); this module now
  re-exports the types (`TerminalSessionInfo` = `TerminalCatalogRow`) so import sites are
  unchanged, and the catalog fetches return the full row. WebSocket/paste/open/terminate/cleanup
  mechanics untouched. Verification metadata pinned to the leaf base until closeout stamps the L2
  code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented additive catalog projection and hosted-delivery split.

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
