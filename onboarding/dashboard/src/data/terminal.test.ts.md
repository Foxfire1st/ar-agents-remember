# dashboard/src/data/terminal.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/terminal.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T15:22+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Unit tests for the terminal WebSocket client (`data/terminal.ts`, slice 6e-1) — the pure protocol
logic, driven against a `FakeSocket` so no real `WebSocket` (absent in jsdom) is touched. The
reopened-L6 suite pins `pasteAndConfirm`'s confirmed draft-paste contract under fake timers: one
bracketed-paste frame and `true` when the composer echoes, retries when a booting harness discards the
paste, confirmation of the echoing attempt without further sends, `false` past the 30s boot deadline,
and never a `\r` on any path.

## Code Commentary

### FEUI MX-FIX-2 Open-Authority Matrix

The opener suite now consumes real `Response` bodies and pins both directions of the authority
contract. Exact raw and harness responses open with the server-owned row. Network, non-OK HTTP,
harness refusal, empty success, malformed JSON, and mismatched id/kind/harness become explicit
failures. The same-reviewer Round 1 correction adds the raw-identity matrix: absent or null
`harness`/`controlState` is accepted, while harness text (including `""`) or a control state is a
protocol contradiction.

### FEUI-L9R Reviewed Candidate Delta

The fake-socket matrix now proves that transport close reports `dropped` without ending the durable
terminal, while an explicit server `exit` remains authoritative. It pins one replacement per
serving-boot identity, resize-before-input replay, superseding stale CONNECTING and OPEN sockets,
inert stale callbacks, first-observed-boot adoption, silence on dispose, and refusal after exit.

### Task Attachment Payload Regression

The request test proves `attachSessionToTask` posts the canonical `{repository, path}` task document
and selected role to `/attach-task`, while retaining `409`/network result classification.

### Logic

`terminalSocketUrl` resolves a same-origin `ws://`/`wss://` URL and percent-encodes the id;
`parseTerminalControl` recognizes only `{type:"exit"}`. The `connectTerminal` suite uses a
`FakeSocket` (records `send`, lets the test push binary/text frames + close): it sets
`binaryType="arraybuffer"`, writes binary frames verbatim into the sink, emits the
`{type:stdin|resize}` frames, suppresses sends when `readyState !== OPEN`, fires `onExit` exactly
once for an authoritative exit frame, reports an unexpected close as dropped-only, and after
`dispose()` closes the socket without echoing either signal. The reattach cases cover one socket per
boot identity and stale-callback rejection. The `openTerminalSession` suite stubs `fetch` with real
`Response` bodies to assert the exact POST shape and accepted server row, then separately pins
network/HTTP/harness/protocol/missing-response failures and raw-versus-harness identity. Task 22 adds
`fetchTerminalSessions` coverage for `GET /api/terminal/sessions` success and failure fallbacks, plus
`fetchTerminalSessionsOrNull` coverage proving empty success stays `[]` while non-ok/network failures
return `null`, and `terminateTerminalSession` coverage for the terminate POST. The `fetchHarnesses` suite
(6e-2b) asserts the harness list is returned and `[]` on non-ok / a missing `harnesses` key / error.
The `bracketedPaste` suite (6e-3) asserts the `ESC[200~…ESC[201~` wrap, with multi-line content verbatim.
The resize-handshake-race case (slice 6e-4) sets the `FakeSocket` to `CONNECTING`, fires two
`sendResize`s (both dropped while not OPEN), then `fireOpen()` and asserts only the **latest** size is
replayed once OPEN (the `FakeSocket` gains `onopen`/`fireOpen`). A `whenReady` case (slice 6f, fake
timers) pushes boot output, then asserts `whenReady()` resolves only after ~700ms of quiet.
**HFX2-L11** adds the `cleanupLandedTerminalSessions` suite: a success case stubs `fetch` and asserts a
`POST /api/terminal/landed-cleanup` with `{sessionIds}` in the body, resolving the normalized
`{closed, skipped, closedSessions, skippedSessions}` shape verbatim from the JSON body; a failure case
covers both a non-ok response and a rejected `fetch` promise, both resolving `null` (matching the
`fetchTerminalSessionsOrNull` fail-soft convention elsewhere in this file) rather than throwing.

### Conventions

vitest (`describe`/`it`/`expect`). The injected `socketFactory` returns the `FakeSocket` cast to
`WebSocket`, so the global `WebSocket` is never referenced — matching the production split where the
real socket is built lazily.

### Invariants And Boundaries

Tests keep durable session exit, socket transport state, and explicit boot-owned reattach as three
separate authorities; fakes must not collapse them into one close signal.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

### 2026-07-24 Curator Delta

The terminal tests now prove one shared catalog read for concurrent callers and a fresh successful
retry after an abort-aware hung catalog or harness request expires.

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
| The WebSocket client under test. | `connectTerminal` | dashboard/src/data/terminal.ts:197-313 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-11T19:58+02:00 — Replaced the retired leaf-key attachment description with the current
  canonical task-document attachment endpoint, payload, and regression boundary.
- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: bound the client-under-test row to
  `connectTerminal` (terminal.ts 197-313) with a plain source. Zero findings remain.

- 2026-07-24T13:17:50Z — Added terminal and harness catalog single-flight timeout coverage.
  Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: replaced boolean opener assertions with real-response
  success/failure classification, exact server identity, and Round 1 raw harness/control
  contradiction regressions; absent/null raw fields remain accepted. Verification metadata remains
  pinned until closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: captured transport-drop versus durable-exit and exact
  once-per-boot reattach regressions; verification metadata remains pinned pending closeout.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: pinned the role-bearing attach JSON contract.

- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive): `TerminalSessionStatus` gains `"landed"`
  (between `"exited"` and `"terminated"`); `TerminalSessionInfo` gains landing provenance
  (`landedAt`/`landedReason`/`landedEdge`/`spawnedBySession`/`spawnedByLifecycle`/`spawnedLabel`/
  `turnState`/`turnStateChangedAt`). New `cleanupLandedTerminalSessions()` calls
  `POST /api/terminal/landed-cleanup` and returns `{closed, skipped, closedSessions, skippedSessions}`.
  Test coverage added for the new type shape and the cleanup call. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-02T16:35+02:00 — Reopened L6 paste-loss fix: added the `pasteAndConfirm` suite under fake
  timers — a quiet-gated paste confirmed by its echo resolves `true` with exactly one bracketed-paste
  frame and never a `\r`; a discarded first attempt is retried and the echoing attempt confirms without
  further sends; and a never-echoing session resolves `false` after the 30s boot deadline with bounded
  retries. Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: added `fetchTerminalSessionsOrNull` coverage for the
  successful-empty vs failed-fetch distinction used by cross-tab catalog sync. Verification metadata
  pinned until closeout stamps the task-22 follow-up code commit.
- 2026-06-26T23:05+02:00 — Task 22: extended `openTerminalSession` expectations for label/lifecycle
  catalog metadata and added `fetchTerminalSessions` plus `terminateTerminalSession` success/failure
  coverage. Verification metadata pinned until closeout stamps the task-22 code commit.
- 2026-06-19T15:59 — Task 6 slice 6f-1: added a `whenReady` case (fake timers) — boot output then quiet, asserting `whenReady()` resolves after the idle window. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: added the resize-handshake-race case — both `sendResize`s while `CONNECTING` are dropped and only the latest is replayed on `onopen`; the `FakeSocket` gained `onopen`/`fireOpen`. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T05:48 — Task 6 slice 6e-3: added the `bracketedPaste` suite (`ESC[200~…ESC[201~` wrap + multi-line verbatim). Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-18T21:27 — Task 6 slice 6e-2b: extended the `openTerminalSession` suite (a `{kind:"harness",harness}` body case) + added the `fetchHarnesses` suite (list returned; `[]` on non-ok / missing-key / error). Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T17:40 — Task 6 slice 6e-2a: added the `openTerminalSession` suite (fetch-stubbed POST shape + ok/error mapping). Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:50 — Created for task 6 slice 6e-1: covers `data/terminal` (url + control parsing + the `connectTerminal` pump) against a fake socket. Verification metadata pinned to the task base until closeout stamps the 6e-1 code commit.
