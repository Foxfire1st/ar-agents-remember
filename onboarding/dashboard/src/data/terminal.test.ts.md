# dashboard/src/data/terminal.test.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No relevant domain documentation was found for this file.

### Repo-Internal References

- The WebSocket client under test. [1]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
