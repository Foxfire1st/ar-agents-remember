# mcp/src/agents_remember/serving/terminal_paste.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/terminal_paste.py`     |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-04T12:31+02:00                                  |
| lastVerifiedCommitHash | `6b940141fc319f1d2d18b2c94fd9e9a213d43141`              |
| lastVerifiedCommitDate | 2026-07-04T12:52:03+02:00|
| governingOverview      | `overview.md`                                           |

## Purpose

`terminal_paste.py` is the **server-side echo-confirmed stdin paste** into a durable tmux session
(slice L2 dispatch). The browser delivers a context packet over the live WebSocket (`data/terminal.ts`
`pasteAndConfirm` / `submitAndConfirm`); the agent-facing `spawn_agent_session` tool has **no live
WebSocket** — it drives a freshly-spawned, PTY-clientless durable tmux session — so this module mirrors
the frontend paste/submit semantics server-side over tmux primitives. It backs both the tool's context
delivery and the new `POST /api/terminal/{session}/paste` serving endpoint.

## Governing Overview

[serving/ overview](overview.md)

## Code Commentary

### Logic

`sanitize_for_injection(text)` mirrors the frontend `sanitizeForInjection`: it strips embedded
bracketed-paste markers (`_PASTE_MARKER`, so injected text can't break out of tmux's own bracketing)
and scrubs the C0 control range **except TAB and NEWLINE** (`_CONTROL_NOISE` — dropping CR, ESC, the
`0x1a` suspend byte, DEL). `PasteResult` is the frozen `(delivered, submitted)` outcome.

The four tmux operations are **injectable callables** (`TmuxBufferSetter`, `TmuxBufferPaster`,
`TmuxKeySender`, `TmuxPaneCapturer`) with real `subprocess`-backed defaults (`_tmux_set_buffer` /
`_tmux_paste_buffer` with `-p` bracketed + `-d` delete / `_tmux_send_key` / `_tmux_capture_pane`), each
`stdin=DEVNULL` + timeout-guarded. `TerminalPaster` takes all four plus `sleep`/`monotonic` seams so
the confirmation loop is deterministically unit-testable against fakes — no real tmux, no real sleep.

`TerminalPaster.paste(tmux_name, text, *, submit, echo_timeout, boot_deadline, submit_timeout,
poll_interval)` is the loop: it sanitizes the text, then `_paste_until_echo` loads a uniquely-named
tmux buffer + `paste-buffer -p` and watches for a **real echo**: either a visible sanitized draft
fragment or a new bracketed-paste chip such as `[Pasted text #N]`. It re-pastes across the boot
window (`boot_deadline`, about 30s by default) because a booting harness can advance the pane while
discarding stdin until its composer mounts; pane advancement alone is no longer treated as delivery.
Only once `delivered` and `submit` does it capture a baseline, `send-keys Enter`, and watch for output
past that baseline (`submitted`). It never raises on a missing/gone session — an unchanged pane simply
reports the unconfirmed outcome (the "surface a retry, never silently drop" contract).

### Conventions

The `terminal.py` injectable-seam posture: every side-effecting tmux op is a constructor-injected
callable defaulting to a `subprocess.run` wrapper. Timeouts/cadence are module constants overridable
per call. `os.getpid()` + a `uuid4` hex name the throwaway tmux buffer so concurrent pastes never
collide.

### Invariants And Boundaries

- **Never submit an unconfirmed paste.** `Enter` is sent only after the composer echoes the draft.
- `submit=False` leaves an editable draft in the composer (the human draft-only flow); a worker gets
  `submit=True` to auto-start.
- Delivery is best-effort and confirmation-based: a boot-discarded paste is retried, and a paste that
  never echoes past `boot_deadline` reports `delivered=False` rather than raising.
- Boot chatter or harness startup output does not confirm delivery; the composer must echo the pasted
  draft/chip.
- No PTY client is attached; this operates on the durable tmux session by name over tmux CLI primitives.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation defines this local paste policy; the frontend
`data/terminal.ts` mirror, the serving route, the tool, and the tests are the source of truth.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines this server-side tmux paste/submit loop. | L133-L229 | [terminal_paste.py](terminal_paste.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `spawn_agent_session` tool pastes the context packet into the spawned session (submit for a worker, draft otherwise). | L161-L169 | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| `POST /api/terminal/{session}/paste` is the serving endpoint mirror (404 on unknown/gone session, else delivered/submitted). | L653-L676 | [app.py](app.py) |
| It mirrors the frontend `pasteAndConfirm` / `submitAndConfirm` bracketed-paste + echo-confirm loop. | — | [../../../../dashboard/src/data/terminal.ts](../../../../dashboard/src/data/terminal.ts) |
| Unit tests drive the loop against an in-memory fake pane + injected clock (draft, submit, unechoed boot-window retry, unconfirmed submit) and the sanitizer. | L74-L123 | [../../../tests/test_terminal_paste.py](../../../tests/test_terminal_paste.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This helper drives only a local tmux session over the tmux CLI. | — | — |

## Update History

- 2026-07-04T12:31+02:00 - L3: tightened delivery confirmation to require a
  pasted draft fragment or new paste chip, preserving the L2 over-boot retry loop
  while fixing false-positive delivery during harness boot. Verification metadata
  pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2: created as the server-side echo-confirmed paste helper mirroring the
  frontend `pasteAndConfirm`/`submitAndConfirm` over tmux `set-buffer`/`paste-buffer -p`/`send-keys` +
  `capture-pane` confirmation, with re-paste across the harness boot window and every tmux op injectable
  for fake-driven tests. Backs the `spawn_agent_session` context delivery and the new
  `POST /api/terminal/{session}/paste` endpoint. Verification metadata pinned until closeout stamps the
  L2 commit.
