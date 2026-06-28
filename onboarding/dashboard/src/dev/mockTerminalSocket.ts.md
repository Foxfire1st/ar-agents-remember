# dashboard/src/dev/mockTerminalSocket.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/mockTerminalSocket.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-18T16:50                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

A DEV-only fake of the 6d terminal WebSocket so the Chats view (slice 6e-1) renders a live-looking
terminal on the bench with **no backend**: it emits a banner, echoes typed stdin (Enter → newline +
prompt), and accepts resize frames.

## Code Commentary

### Logic

`MockTerminalSocket` implements the surface `connectTerminal` uses (`binaryType`, `onmessage`,
`onclose`, `send`, `close`, `readyState`). It `queueMicrotask`s the banner (so `onmessage` is wired
first), and on a `send` JSON `{type:"stdin",data}` echoes the data back as a **binary** frame
(`\r` → `\r\n$ `), encoding text via `TextEncoder` to match the real binary stream. Exported as
`mockTerminalSocketFactory` (a `TerminalSocketFactory` returning the mock cast to `WebSocket`),
which `dev/Bench.tsx` provides through `TerminalSocketContext`.

### Invariants And Boundaries

DEV-only — `/dev/*` is dropped from the production bundle, so this never ships; production has no
context provider and uses a real same-origin socket. It emulates only enough of the wire (binary
echo + a banner) to exercise xterm rendering + resize, not a real shell.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The client contract this fakes (the socket surface + frame shapes). | — | [data/terminal.ts](../data/terminal.ts) |
| The bench that provides this via context. | — | [Bench.tsx](Bench.tsx) |

## Update History

- 2026-06-18T16:50 — Created for task 6 slice 6e-1: the dev mock terminal socket (banner + stdin echo + resize ack) so the Chats view renders without a backend. Verification metadata pinned to the task base until closeout stamps the 6e-1 code commit.
