# dashboard/src/data/terminal.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/terminal.ts`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T09:45+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Provides browser terminal transport and the terminal catalog HTTP adapters. Its assignment write now
sends a canonical task-document reference plus role; runtime session id is used only to identify the
hosted occupant being changed.

## Code Commentary

### Logic

PTY WebSocket connection, catalog fetch, termination, and opener re-exports remain transport concerns.
`attachSessionToTask` posts `taskDocumentRef` and `role` to the assignment route and classifies the
strict `ok | seat-taken | error` result. It does not retain the deleted leaf-assignment request.

### Conventions

Callers derive task references from projected documents before entering this adapter. The server is
authoritative for uniqueness and returns the accepted structural binding.

### Invariants And Boundaries

- No leaf-key compatibility body is emitted.
- A session id selects the occupant for this operator/API mutation, never the durable seat.
- Terminal transport closure and durable terminal outcome remain distinct.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The client exposes a structural task-assignment result family. | `AttachTaskResult` | dashboard/src/data/terminal.ts:484-484 |
| Assignment posts a task-document reference and role. | `attachSessionToTask` | dashboard/src/data/terminal.ts:490-511 |
| Terminal transport remains a separate connection concern. | `connectTerminal` | dashboard/src/data/terminal.ts:310-362 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current data-contract card for `terminal.ts` with task-document identity, qualified seat state, and terminal projections represented by this source.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the terminal refactor and the self-caught intermediate reattach-socket defect (F6 correction). Verification metadata stays pinned until closeout stamps the code commit.

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
