# dashboard/src/dev/mockTerminalSocket.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The client contract this fakes (the socket surface + frame shapes). [1]
- The bench that provides this via context. [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

The mock socket can emit open, suppress its banner, or drop after opening. Close is idempotent and clears handlers, avoiding StrictMode/navigation races while preserving the legacy gallery mock by default.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
