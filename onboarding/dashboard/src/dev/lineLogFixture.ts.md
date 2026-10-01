# dashboard/src/dev/lineLogFixture.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **controlled-pane PTY content fixture** (260715-FEUI-L6 R1/R9, design §8.1): what a
CONTROLLED session's terminal REALLY shows — the hosted runner's plain line-log, with shapes
verbatim-faithful to `harness_control_runner.py` `_render_updates`/`_read_terminal_input`
(`[control] {state} activity=… acceptance=…` status lines, `[{ts}] {role} request=…: text`
transcript lines, `[control] submission {id} {acceptance}: {detail}` echoes) — NEVER a vendor
TUI. Plus the mock WebSocket that drips it: consumed by the `/dev/pty-bench` renderer
measurement (configurable-rate firehose) and available as a slow-drip controlled-pane socket for
dev surfaces.

## Code Commentary

### Logic

- **`RUNNER_LINE_LOG_BOOT`** — cit:([`RUNNER_LINE_LOG_BOOT`], dashboard/src/dev/lineLogFixture.ts:9-19): one boot's worth of runner output — protocol banner,
  `[control] ready` status transitions (idle→running→idle), user/assistant/result transcript
  lines with request ids.
- **`RUNNER_LINE_LOG_STREAM`** — cit:([`RUNNER_LINE_LOG_STREAM`], dashboard/src/dev/lineLogFixture.ts:22-30): steady-state lines the bench cycles to simulate a
  working controlled pane, including the queued-submission echo
  (`[control] submission req-77 queued: retained for the next turn`).
- **`MockLineLogSocket`** — cit:([`MockLineLogSocket`], dashboard/src/dev/lineLogFixture.ts:34-82): a WebSocket lookalike — `queueMicrotask` fires `onopen`,
  emits the boot log, then `setInterval` drips stream lines as `ArrayBuffer` messages (binary,
  like the real terminal WS). **`send` models the controlled-stdin trap** — cit:([`send`], dashboard/src/dev/lineLogFixture.ts:55-71): a stdin
  message containing `\r` echoes the runner's queued-submission acceptance line — exactly the
  behavior the InteractionBar honesty hint names (typing into a controlled pane queues for the
  NEXT turn; it never answers the pending interaction).
- **Factories** — cit:([`mockControlledLineLogSocketFactory`, `benchLineLogSocketFactory`], dashboard/src/dev/lineLogFixture.ts:85-86; dashboard/src/dev/lineLogFixture.ts:89-90): `mockControlledLineLogSocketFactory` (one line / 2 s — the
  calm controlled pane) and `benchLineLogSocketFactory(linesPerSecond)` (the OQ-B firehose,
  floored at a 5 ms interval).

### Invariants And Boundaries

- The line shapes are a fidelity contract with `mcp/src/agents_remember/serving/`'s
  `harness_control_runner.py` — if the runner's `_render_updates`/`_read_terminal_input` formats
  change, this fixture (and design §8.1's archetype story) must follow.
- DEV-only: nothing here ships — `/dev/*` is dropped from the production bundle, and no product
  path imports the fixture.

## Evidence

### Repo-Internal References

- Boot/stream line sets, the mock socket incl. the queued-submission stdin echo, both factories. [1]
- The socket-factory context type this plugs into. [2]
- The bench consuming the firehose factory + stream lines (serialize probe fill). [3]
- The pre-existing generic dev echo socket this complements (Chats bench). [4]
- The honesty hint whose trap the `send` echo models. [5]
