# dashboard/src/dev/mockTerminalSocket.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/mockTerminalSocket.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `../overview.md`                                |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The client contract this fakes (the socket surface + frame shapes). | — | [data/terminal.ts](../data/terminal.ts) |
| The bench that provides this via context. | — | [Bench.tsx](Bench.tsx) |

## FEUI-L8 Reviewed Candidate Delta

The mock socket can emit open, suppress its banner, or drop after opening. Close is idempotent and clears handlers, avoiding StrictMode/navigation races while preserving the legacy gallery mock by default.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-06-18T16:50 — Created for task 6 slice 6e-1: the dev mock terminal socket (banner + stdin echo + resize ack) so the Chats view renders without a backend. Verification metadata pinned to the task base until closeout stamps the 6e-1 code commit.
