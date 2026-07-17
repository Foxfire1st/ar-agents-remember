# dashboard/src/dev/lineLogFixture.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/lineLogFixture.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `../overview.md`                                 |

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

- **`RUNNER_LINE_LOG_BOOT`** (L9-L19): one boot's worth of runner output — protocol banner,
  `[control] ready` status transitions (idle→running→idle), user/assistant/result transcript
  lines with request ids.
- **`RUNNER_LINE_LOG_STREAM`** (L22-L30): steady-state lines the bench cycles to simulate a
  working controlled pane, including the queued-submission echo
  (`[control] submission req-77 queued: retained for the next turn`).
- **`MockLineLogSocket`** (L34-L82): a WebSocket lookalike — `queueMicrotask` fires `onopen`,
  emits the boot log, then `setInterval` drips stream lines as `ArrayBuffer` messages (binary,
  like the real terminal WS). **`send` models the controlled-stdin trap** (L55-L71): a stdin
  message containing `\r` echoes the runner's queued-submission acceptance line — exactly the
  behavior the InteractionBar honesty hint names (typing into a controlled pane queues for the
  NEXT turn; it never answers the pending interaction).
- **Factories** (L85-L90): `mockControlledLineLogSocketFactory` (one line / 2 s — the
  calm controlled pane) and `benchLineLogSocketFactory(linesPerSecond)` (the OQ-B firehose,
  floored at a 5 ms interval).

### Invariants And Boundaries

- The line shapes are a fidelity contract with `mcp/src/agents_remember/serving/`'s
  `harness_control_runner.py` — if the runner's `_render_updates`/`_read_terminal_input` formats
  change, this fixture (and design §8.1's archetype story) must follow.
- DEV-only: nothing here ships — `/dev/*` is dropped from the production bundle, and no product
  path imports the fixture.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Boot/stream line sets, the mock socket incl. the queued-submission stdin echo, both factories. | L9-L91 | [lineLogFixture.ts](lineLogFixture.ts) |
| The socket-factory context type this plugs into. | — | [../data/terminal.ts](../data/terminal.ts) |
| The bench consuming the firehose factory + stream lines (serialize probe fill). | L5, L83, L118 | [PtyRenderBench.tsx](PtyRenderBench.tsx) |
| The pre-existing generic dev echo socket this complements (Chats bench). | — | [mockTerminalSocket.ts](mockTerminalSocket.ts) |
| The honesty hint whose trap the `send` echo models. | L57-L58 | [../panels/session-cockpit/lifecycleCopy.ts](../panels/session-cockpit/lifecycleCopy.ts) |

## Update History

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R1/R9 (design §8.1): the controlled-pane
  line-log content (verbatim runner shapes incl. the queued-submission echo) + the mock socket
  with the controlled-stdin queue trap, in slow-drip and bench-firehose factory variants.
  Verification metadata pinned to the leaf base until closeout stamps the L6 code commit.
