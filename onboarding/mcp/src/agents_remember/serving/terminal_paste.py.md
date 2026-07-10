# mcp/src/agents_remember/serving/terminal_paste.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/terminal_paste.py`     |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-10T13:03+02:00                                  |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`              |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `overview.md`                                           |

## Purpose

`terminal_paste.py` is the bounded tmux input transport for log-verified dispatch. It controls
sanitized bytes and Enter/C-u keypresses, but the caller-supplied harness-log probe is the only
submitted-acceptance authority. Pane text is captured only to prove absence before the one allowed
re-paste, clear visible prior content before replacement, or attach final failure evidence.

**Historical pre-L15 context (superseded by the contract above):** `terminal_paste.py` was the **server-side capture-verified stdin paste** into a durable tmux session
(slice L2 dispatch, hardened by 260707-HFX-L3). The browser delivers a context packet over the live
WebSocket (`data/terminal.ts` `pasteAndConfirm` / `submitAndConfirm`); the agent-facing
`spawn_agent_session` tool has **no live WebSocket** — it drives a freshly-spawned, PTY-clientless
durable tmux session — so this module mirrors the frontend paste/submit semantics server-side over
tmux primitives. Delivery reports success ONLY after a pane capture proves the paste landed; one
origin baseline per delivery — over a HISTORY-INCLUSIVE capture window (`capture-pane -p -S -200`,
review L3/N1: viewport-only capture let origin-visible chips scroll out, blinding growth math and
the idempotence guard alike) — plus a strongest-first probe ladder make duplicate stacking a
bounded-window impossibility, stated honestly rather than absolutely; failures are loud with the
capture attached (the F-V/SF-1 forensics: the codex chip form never matched the old regex, and
per-attempt re-baselining stacked up to 7 duplicate pastes). It backs the tool's context delivery, the
`POST /api/terminal/{session}/paste` serving endpoint, and the inbox hosted push.

## Governing Overview

[serving/ overview](overview.md)

## Code Commentary

### 260707-HFX2-L15 Current Logic

`TerminalPaster.paste` sanitizes the input, optionally short-circuits when the acceptance probe
already sees the id, captures one origin only for later retry safety, and transports through a
uniquely named tmux buffer. Submitted input waits at least 100 ms before Enter, then polls the
caller probe on a 100 ms cadence for its calibrated window. Recovery is fixed: one Enter re-press,
then at most one re-paste. Before that re-paste, `_payload_presence` compares the current pane to
the original baseline using the payload-specific Codex chip, generic chip-count growth, or payload
head. Unobservable state fails closed. Visible evidence triggers one `C-u`, a settle, and a second
absence check; if evidence remains, delivery fails rather than appending a duplicate. Escape is
refused. Drafts and pre-bind commands may transport with `accepted=None`, but can never report
`submitted=True`.

### Historical Logic Through HFX2-L3 (Superseded By L15)

`sanitize_for_injection(text)` mirrors the frontend `sanitizeForInjection`: it strips embedded
bracketed-paste markers (`_PASTE_MARKER`, so injected text can't break out of tmux's own bracketing)
and scrubs the C0 control range **except TAB and NEWLINE** (`_CONTROL_NOISE` — dropping CR, ESC, the
`0x1a` suspend byte, DEL). `PasteResult` is the frozen `(delivered, submitted, capture)` outcome:
`capture` is the LAST pane snapshot taken — on `delivered=False` it is the loud-failure evidence the
caller must surface (260707-HFX-L3: never a bare false-success boolean again).

`count_paste_chips(capture)` is the delivery-evidence probe, counting rendered paste chips across
BOTH harness chip vocabularies (`_PASTE_CHIP`): Claude Code's `[Pasted text #N]` AND codex's
`[Pasted Content N chars]` — the codex form was unrecognized pre-L3, so the seam misread landed
pastes as unconfirmed and blind-retried (the F-V forensic run stacked 7 duplicate chips in one
composer). `_paste_landed(origin, current, sanitized)` decides delivery against the origin snapshot with a
STRONGEST-FIRST probe ladder (L3 round 2): (1) payload-SPECIFIC codex chip instance growth —
`_expected_codex_chip(sanitized)` renders the literal `[Pasted Content {len} chars]` and requires
MORE instances than the origin held, so identical back-to-back briefs each demand a fresh chip;
(2) generic chip-count growth across both vocabularies; (3) growth of the payload's own head
(`_echo_fragment`, the first non-blank line ≤120 chars, for composers that echo the draft
verbatim). A merely-changed pane (boot repaint) is never enough. Origin and every verification
re-capture flow through the same `_capture_pane_argv` history window, so both sides of the growth
comparison see the same universe — content can only leave a suffix window from the top, never
enter, so counts only spuriously DECREASE (the direction the specific probe covers).

The four tmux operations are **injectable callables** (`TmuxBufferLoader`, `TmuxBufferPaster`,
`TmuxKeySender`, `TmuxPaneCapturer`) with real `subprocess`-backed defaults — `_tmux_load_buffer`
rides the payload over STDIN into `tmux load-buffer -b <name> -` (nothing on argv, so a large packet
can never hit ARG_MAX or shell-quoting seams; the injectable kwarg renamed `set_buffer` →
`load_buffer` with it), `_tmux_paste_buffer` with `-p` bracketed + `-d` delete, `_tmux_send_key`, and
`_tmux_capture_pane` (history-inclusive: `_CAPTURE_HISTORY_LINES = 200` via `_capture_pane_argv`) — each `stdin=DEVNULL` (except the payload feed) + timeout-guarded.
`TerminalPaster` takes all four plus `sleep`/`monotonic` seams so the confirmation loop is
deterministically unit-testable against fakes — no real tmux, no real sleep.

`TerminalPaster.paste(tmux_name, text, *, submit, echo_timeout, boot_deadline, submit_timeout,
poll_interval)` sanitizes the text and delegates to `_paste_until_verified` — the seam's heart. It
takes ONE pre-delivery `origin` capture and holds it as the single baseline for the whole delivery:
re-baselining per attempt was the F-V defect (a chip rendering between attempts landed inside the
fresh baseline, invisible, so the seam re-pasted). Each attempt loads a uniquely-named tmux buffer +
`paste-buffer -p`, then `_await_echo` runs bounded settle re-captures (`echo_timeout`, `poll_interval`)
until `_paste_landed` or timeout — returning the last capture either way, so a verdict always carries
fresh evidence. Before ANY re-paste the idempotence guard re-captures FIRST: the TUI renders a beat
behind keystrokes, so the previous paste may have landed after its echo window closed — a landed
paste is reported delivered and never re-sent; duplicate stacking is impossible by construction. The
retry loop runs across the boot window (`boot_deadline`, ~30s default) because a just-spawned harness
discards stdin until its composer mounts. Only once `delivered` and `submit` does it capture a
post-paste baseline, send `Enter` through `_press`, and `_await_advance` watches for output past that
baseline (`submitted`). `_press` refuses `"Escape"` by construction (`ValueError`): Escape interrupts
a codex session (260707-HFX-L3 run discipline, dispatch-pack PASTE DISCIPLINE) — Enter is the ONLY
key this seam ever sends. It never raises on a missing/gone session — an unverifiable delivery
reports `delivered=False` with the final pane capture attached.

**`capture_pane(tmux_name)` (260707-HFX-L8)** is a new PUBLIC wrapper around the existing PRIVATE
`_tmux_capture_pane` — added so live turn-state classification (`terminal_liveness.py`'s
`_observe_alive`) reads the IDENTICAL history-inclusive pane view (`-S -200`) that paste
verification already uses, rather than growing a second capture-command shape. It carries no new
behavior of its own; it exists purely to make the one existing capture primitive callable from
outside this module.

### Conventions

The `terminal.py` injectable-seam posture: every side-effecting tmux op is a constructor-injected
callable defaulting to a `subprocess.run` wrapper. Timeouts/cadence are module constants overridable
per call. `os.getpid()` + a `uuid4` hex name the throwaway tmux buffer so concurrent pastes never
collide.

### 260707-HFX2-L15 Current Invariants And Boundaries

- Only the harness-log callback may grant submitted acceptance.
- Pane reads can withhold/clear/rewrite transport or provide failure evidence; they never grant
  acceptance.
- Recovery is bounded to initial Enter, one Enter re-press, and one verified-absence re-paste.
- Re-paste requires verified absence; visible payload is cleared and verified absent before
  replacement, and unobservable/uncleared state fails closed.
- The settle floor is 100 ms and `Escape` is structurally forbidden.
- Payload bytes ride stdin into `tmux load-buffer`, never argv or a shell.

### Historical Invariants And Boundaries (Superseded By L15)

- **Never submit an unconfirmed paste.** `Enter` is sent only after a capture proves the paste landed.
- **One origin baseline per delivery.** Every landed/not-landed verdict compares against the same
  pre-delivery snapshot; per-attempt re-baselining is the forbidden F-V defect.
- **Re-capture before any re-paste.** A landed paste is never re-sent — duplicate stacking is
  impossible by construction, not by tuning.
- **Loud failure.** `delivered=False` always carries the final pane capture (`PasteResult.capture`);
  callers must surface it, never trust a bare boolean (the SF-1 blind seat).
- **Only Enter.** `_press` refuses `Escape` (it interrupts a codex session); no other key ever
  crosses this seam.
- `submit=False` leaves an editable draft in the composer (the human draft-only flow); a worker gets
  `submit=True` to auto-start.
- Boot chatter or harness startup output does not confirm delivery; the pane must show a NEW chip
  (either harness vocabulary) or more copies of the payload head than the origin had.
- The payload rides stdin into `tmux load-buffer -` — never argv — so packet size is unbounded by
  ARG_MAX and free of shell-quoting seams.
- No PTY client is attached; this operates on the durable tmux session by name over tmux CLI primitives.
- `capture_pane` is the only sanctioned external entry point for raw pane text; a future caller
  needing pane text (as `terminal_liveness.py` now does) uses this public wrapper, never the
  private `_tmux_capture_pane` directly.

### Todos

Reviewer note N5 remains outside this candidate: a later independent `deliver()` invocation can
still encounter an unlogged payload idling in a composer before its initial paste. The current
within-invocation retry ladder is guarded; the cross-invocation case is bounded by supervisor
redelivery pacing and awaits an owner disposition/follow-up.

## Docs References

No relevant external/domain documentation defines this local paste policy; the frontend
`data/terminal.ts` mirror, the serving route, the tool, and the tests are the source of truth.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines this server-side tmux paste/submit loop. | L133-L229 | [terminal_paste.py](terminal_paste.py) |

## Repo-Internal References

The current acceptance/retry contract is implemented and tested locally; the older capture-echo
rows below are retained only as historical provenance for the superseded L3 mechanism.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Submitted acceptance is callback-driven; recovery is one Enter re-press then one verified-absence clear/replace re-paste. | L130-L218 | [terminal_paste.py](terminal_paste.py) |
| Duplicate-chip, clear-before-replacement, unobservable-pane, settle-floor, and Escape regressions pin the current ladder. | L64-L210 | [../../../tests/test_terminal_paste.py](../../../tests/test_terminal_paste.py.md) |

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `spawn_agent_session` tool pastes the context packet into the spawned session (submit for a worker, draft otherwise). | L161-L169 | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| `POST /api/terminal/{session}/paste` is the serving endpoint mirror (404 on unknown/gone session, else delivered/submitted). | L653-L676 | [app.py](app.py) |
| It mirrors the frontend `pasteAndConfirm` / `submitAndConfirm` bracketed-paste + echo-confirm loop. | — | [../../../../dashboard/src/data/terminal.ts](../../../../dashboard/src/data/terminal.ts) |
| Unit tests drive the loop against in-memory fake panes + injected clock — incl. the `DeliveryIntegrityTests` (codex chip confirms with ONE paste, laggy chip seen by re-capture and never re-pasted, failure capture attached, Escape refused, only-Enter) and the chip-vocabulary counter. | whole module | [../../../tests/test_terminal_paste.py](../../../tests/test_terminal_paste.py) |
| The inbox hosted push records the capture tail in its durable delivery detail on an unverified push. | [inbox_delivery.py](inbox_delivery.py) | [inbox_delivery.py](inbox_delivery.py) |
| `capture_pane` is called from the liveness sweeper's alive-harness-row turn-state classification path. | `_observe_alive`'s default `pane_capturer` | [terminal_liveness.py](terminal_liveness.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This helper drives only a local tmux session over the tmux CLI. | — | — |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 removal round + case (f): replaced pane-echo/output
  acceptance with a caller-supplied harness-log probe; bounded recovery to one Enter re-press and
  one verified-absence re-paste; added clear-and-recheck duplicate prevention, unobservable
  fail-closed behavior, 100 ms settle/poll floors, and failure-only capture. Verification metadata
  remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: live turn-state): added a public
  `capture_pane(tmux_name)` wrapper around the existing private `_tmux_capture_pane`, so
  `terminal_liveness.py`'s turn-state classification reads the identical history-inclusive capture
  paste verification already uses — one capture-command shape, not two. No change to any existing
  behavior. Verification metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-07T23:20+02:00 — 260707-HFX-L3 round 2 (review N1/N3): verification captures are
  history-inclusive (`capture-pane -p -S -200`, shared by origin and every re-capture — viewport-only
  capture let origin chips scroll out and blinded both growth math and the idempotence guard);
  `_paste_landed` gained the strongest-first ladder headed by the payload-specific codex chip
  instance-growth probe (`_expected_codex_chip`); the module's delivery claim is stated honestly
  (bounded window + probe ladder). Truncating-pane test honesty: `_ScrollingCodexPane` pins the
  scroll-out case to ONE paste with no duplicate.
- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): `_paste_until_verified`
  replaces the echo loop — ONE origin baseline held for the whole delivery, re-capture before any
  re-paste (a landed paste is never re-sent; the F-V run stacked 7 duplicates via per-attempt
  re-baselining); `count_paste_chips` knows BOTH chip vocabularies (`[Pasted text #N]` claude,
  `[Pasted Content N chars]` codex — the unrecognized codex form was the SF-1 blind seat);
  `_tmux_load_buffer` feeds the payload via stdin to `tmux load-buffer` then `paste-buffer -p -d`
  (no argv/ARG_MAX seam; injectable kwarg renamed `set_buffer` → `load_buffer`);
  `PasteResult.capture` attaches the final pane snapshot (loud failure); `_await_echo` returns its
  last capture from bounded settle re-captures; `_press` refuses `Escape` — only Enter is ever
  sent. Verification metadata pinned until closeout stamps the HFX-L3 commit.
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
