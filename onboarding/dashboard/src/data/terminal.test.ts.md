# dashboard/src/data/terminal.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/terminal.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T01:25+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Unit tests for the terminal WebSocket client (`data/terminal.ts`, slice 6e-1) — the pure protocol
logic, driven against a `FakeSocket` so no real `WebSocket` (absent in jsdom) is touched.

## Code Commentary

### Logic

`terminalSocketUrl` resolves a same-origin `ws://`/`wss://` URL and percent-encodes the id;
`parseTerminalControl` recognizes only `{type:"exit"}`. The `connectTerminal` suite uses a
`FakeSocket` (records `send`, lets the test push binary/text frames + close): it sets
`binaryType="arraybuffer"`, writes binary frames verbatim into the sink, emits the
`{type:stdin|resize}` frames, suppresses sends when `readyState !== OPEN`, fires `onExit` exactly
once across an exit-frame-then-close, fires it on an unexpected close, and after `dispose()` closes
the socket without echoing `onExit`. The `openTerminalSession` suite (slice 6e-2a) stubs `fetch` to
assert the POST shape (`/api/terminal/{id}`, `{kind}` body), label/lifecycle metadata, and `true`/`false` on ok / non-ok / error,
plus (6e-2b) a `{kind:"harness",harness}` body when a harness id is passed. Task 22 adds
`fetchTerminalSessions` coverage for `GET /api/terminal/sessions` success and failure fallbacks, plus
`fetchTerminalSessionsOrNull` coverage proving empty success stays `[]` while non-ok/network failures
return `null`, and `terminateTerminalSession` coverage for the terminate POST. The `fetchHarnesses` suite
(6e-2b) asserts the harness list is returned and `[]` on non-ok / a missing `harnesses` key / error.
The `bracketedPaste` suite (6e-3) asserts the `ESC[200~…ESC[201~` wrap, with multi-line content verbatim.
The resize-handshake-race case (slice 6e-4) sets the `FakeSocket` to `CONNECTING`, fires two
`sendResize`s (both dropped while not OPEN), then `fireOpen()` and asserts only the **latest** size is
replayed once OPEN (the `FakeSocket` gains `onopen`/`fireOpen`). A `whenReady` case (slice 6f, fake
timers) pushes boot output, then asserts `whenReady()` resolves only after ~700ms of quiet.

### Conventions

vitest (`describe`/`it`/`expect`). The injected `socketFactory` returns the `FakeSocket` cast to
`WebSocket`, so the global `WebSocket` is never referenced — matching the production split where the
real socket is built lazily.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The WebSocket client under test. | — | [terminal.ts](terminal.ts) |

## Update History

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
