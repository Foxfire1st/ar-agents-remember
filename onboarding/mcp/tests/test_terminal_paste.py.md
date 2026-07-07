# mcp/tests/test_terminal_paste.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_terminal_paste.py`                |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-04T12:31+02:00                            |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`        |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                                  |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_terminal_paste.py` covers the server-side echo-confirmed paste helper (`serving.terminal_paste`,
L2). The paster mirrors the frontend `pasteAndConfirm` / `submitAndConfirm` over tmux primitives; every
tmux operation is injectable, so the confirmation loop runs against an in-memory fake pane — no real
tmux server and no real sleeping (an injected clock + a no-op sleep make the timeouts deterministic).

## Code Commentary

### Logic

`_FakePane` is an in-memory pane: `set_buffer` / `paste_buffer` (appends a `[Pasted text #1]` echo when
`echo` is on) / `send_key` (appends output on `Enter` when `submit_echo` is on) / `capture` (returns the
growing visible content). `_Clock` advances a fixed step per call so timeouts are hit deterministically,
and `_paster` wires all four tmux callables + the clock + a no-op sleep into a `TerminalPaster`.

- `SanitizeTests` pins `sanitize_for_injection`: it strips the `0x1a` suspend byte, the bracketed-paste
  markers, and CR while keeping NEWLINE and TAB (and ordinary text).
- `PasteTests` pin the loop: an echo-confirmed paste **without** submit delivers and leaves a draft (one
  bracketed paste of the sanitized text, no `Enter`); a paste **with** submit presses `Enter` and
  confirms; an **unechoed** paste re-pastes across the boot window and reports unconfirmed delivery,
  boot output without a pasted draft/chip does not count as delivered (never submitting either case),
  and a submit whose `Enter` produces no output reports `delivered=True,
  submitted=False`.

### Conventions

`unittest` + the `sys.path` insertion idiom. The fake pane models the composer echo (a paste advances
the visible content) and the submit echo (Enter advances it) so the `capture-pane` before/after
confirmation loop can be exercised deterministically; `echo`/`submit_echo` toggles drive the
unconfirmed paths. Timeouts are passed explicitly (`echo_timeout` / `boot_deadline` / `submit_timeout`)
so the boot-window retry and unconfirmed-submit cases terminate quickly against the stepped clock.

### Invariants And Boundaries

- No real tmux, no real sleep — the loop runs against the fake pane + injected clock/sleep.
- The loop must never submit an unconfirmed paste; the unechoed case asserts no `Enter` was sent.
- Sanitization keeps NEWLINE + TAB and drops control noise, mirroring the frontend.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation found; the behavior mirrors the frontend `data/terminal.ts`
paste loop, a local convention.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests pin the local server-side paste loop, not an external protocol. | L87-L122 | [test_terminal_paste.py](test_terminal_paste.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The paster + sanitizer under test (injectable tmux ops + confirmation loop). | L57-L229 | [../src/agents_remember/serving/terminal_paste.py](../src/agents_remember/serving/terminal_paste.py) |
| The frontend paste/submit loop this helper mirrors server-side. | — | [../../../dashboard/src/data/terminal.ts](../../../dashboard/src/data/terminal.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests cover local serving behavior only. | - | - |

## Update History

- 2026-07-04T12:31+02:00 - L3: added the harness-boot false-positive regression
  where pane output advances but no pasted draft/chip appears. Verification
  metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2: created coverage for the server-side echo-confirmed paste helper —
  sanitization, draft (no submit), paste+submit confirmation, unechoed boot-window retry reporting
  unconfirmed delivery, and unconfirmed submit — against an in-memory fake pane + injected clock/sleep.
  Verification metadata pinned until closeout stamps the L2 commit.
