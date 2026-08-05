# dashboard/src/dev/lineLogFixture.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/lineLogFixture.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-02T01:42+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Boot/stream line sets, the mock socket incl. the queued-submission stdin echo, both factories. | `RUNNER_LINE_LOG_BOOT`; `RUNNER_LINE_LOG_STREAM`; `MockLineLogSocket`; `mockControlledLineLogSocketFactory`; `benchLineLogSocketFactory` | dashboard/src/dev/lineLogFixture.ts:9-19; dashboard/src/dev/lineLogFixture.ts:22-30; dashboard/src/dev/lineLogFixture.ts:34-82; dashboard/src/dev/lineLogFixture.ts:85-86; dashboard/src/dev/lineLogFixture.ts:89-90 |
| The socket-factory context type this plugs into. | `TerminalSocketFactory` | dashboard/src/data/terminal.ts:46-46 |
| The bench consuming the firehose factory + stream lines (serialize probe fill). | `PtyRenderBench` | dashboard/src/dev/PtyRenderBench.tsx:83-164 |
| The pre-existing generic dev echo socket this complements (Chats bench). | `MockTerminalSocket`; `createMockTerminalSocketFactory` | dashboard/src/dev/mockTerminalSocket.ts:11-56; dashboard/src/dev/mockTerminalSocket.ts:58-63 |
| The honesty hint whose trap the `send` echo models. | `INTERACTION_HONESTY_HINT` | dashboard/src/panels/session-cockpit/lifecycleCopy.ts:72-73 |

## Update History

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 15 citation finding(s); scoped recheck clean.

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R1/R9 (design §8.1): the controlled-pane
  line-log content (verbatim runner shapes incl. the queued-submission echo) + the mock socket
  with the controlled-stdin queue trap, in slow-drip and bench-firehose factory variants.
  Verification metadata pinned to the leaf base until closeout stamps the L6 code commit.
