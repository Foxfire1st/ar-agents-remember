# mcp/tests/test_terminal_paste.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_terminal_paste.py`                |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-10T13:03+02:00                            |
| lastVerifiedCommitHash | `c881828542f0ca916ce8b1d4fd5ab8a914e24110`        |
| lastVerifiedCommitDate | 2026-07-10T13:18:50+02:00|
| governingOverview      | `../overview.md`                                  |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_terminal_paste.py` covers the server-side capture-verified paste helper
(`serving.terminal_paste`, L2, hardened by 260707-HFX-L3). The paster mirrors the frontend
`pasteAndConfirm` / `submitAndConfirm` over tmux primitives; every tmux operation is injectable, so
the confirmation loop runs against in-memory fake panes — no real tmux server and no real sleeping
(an injected clock + a no-op sleep make the timeouts deterministic). The `DeliveryIntegrityTests`
class encodes 260707-HFX-L3: the SF-1 blind seat (codex chip vocabulary unrecognized → false
verdicts) and the F-V duplicate stack (blind retry re-pasted a landed paste up to 7 times) — each
scenario failed against the pre-fix seam by construction.

## Code Commentary

### Logic

**260707-HFX2-L15 coverage.** The suite now drives an acceptance callback rather than pane echo.
It pins the full calibrated-window order, one Enter re-press, one re-paste only after verified
absence, final failure capture, payload-specific/generic chip duplicate blocking, clear-before-
replacement, unobservable fail-closed behavior, the >=100 ms settle floor, pre-bind command
non-acceptance, sanitization, and Escape refusal.

`_FakePane` is an in-memory pane: `load_buffer` (the renamed injectable seam) / `paste_buffer`
(appends a `[Pasted text #1]` echo when `echo` is on) / `send_key` (appends output on `Enter` when
`submit_echo` is on) / `capture` (returns the growing visible content). Two 260707-HFX-L3 fakes model
the forensic panes: `_CodexChipPane` renders a large paste ONLY as the codex
`[Pasted Content N chars]` chip (the SF-1 shape), and `_LaggyChipPane` renders that chip a
configurable number of captures BEHIND the paste — past the first attempt's echo window, so only the
retry path's re-capture guard can see it landed (the F-V race). `_Clock` advances a fixed step per
call so timeouts are hit deterministically, and `_paster` wires all four tmux callables + the clock +
a no-op sleep into a `TerminalPaster`.

- `SanitizeTests` pins `sanitize_for_injection`: it strips the `0x1a` suspend byte, the bracketed-paste
  markers, and CR while keeping NEWLINE and TAB (and ordinary text).
- `ChipCountTests` pins `count_paste_chips` across BOTH harness chip vocabularies — claude
  `[Pasted text #N]` (with and without the number) and codex `[Pasted Content N chars]`
  (case-tolerant) count; near-miss strings do not; a plain pane counts zero.
- `PasteTests` pin the loop: an echo-confirmed paste **without** submit delivers and leaves a draft (one
  bracketed paste of the sanitized text, no `Enter`); a paste **with** submit presses `Enter` and
  confirms; a **verifiably-unlanded** paste re-pastes across the boot window (the idempotence guard
  re-captured first and found no trace each time) and reports unconfirmed delivery, boot output
  without a pasted draft/chip does not count as delivered (never submitting either case), and a
  submit whose `Enter` produces no output reports `delivered=True, submitted=False`.
- `DeliveryIntegrityTests` pin the 260707-HFX-L3 contract: the codex chip confirms delivery with
  exactly ONE paste (`_CodexChipPane`, `len(pane.pasted) == 1`); a late-rendering chip is seen by
  the retry path's re-capture and NEVER re-pasted (`_LaggyChipPane` — one paste, one chip; duplicate
  stacking impossible); an unverifiable delivery returns `delivered=False` WITH the final pane
  capture attached (`result.capture == pane.content`); a successful delivery also carries its
  confirming capture; `_press("Escape")` raises `ValueError` with no key sent (run discipline —
  Escape interrupts a codex session); and a full paste+submit flow sends ONLY `Enter`.

### Conventions

`unittest` + the `sys.path` insertion idiom. The fake pane models the composer echo (a paste advances
the visible content) and the submit echo (Enter advances it) so the `capture-pane` before/after
confirmation loop can be exercised deterministically; `echo`/`submit_echo` toggles drive the
unconfirmed paths. Timeouts are passed explicitly (`echo_timeout` / `boot_deadline` / `submit_timeout`)
so the boot-window retry and unconfirmed-submit cases terminate quickly against the stepped clock.

### Invariants And Boundaries

- No real tmux, no real sleep — the loop runs against the fake panes + injected clock/sleep.
- The loop must never submit an unconfirmed paste; the unechoed case asserts no `Enter` was sent.
- Delivery truth is capture-based (260707-HFX-L3): a landed chip in either vocabulary confirms with
  one paste, a landed-late chip must not be re-pasted, and a failed verification must carry the
  final capture — the pre-fix seam fails each of these by construction.
- Only `Enter` may cross the seam; the Escape refusal is itself the contract under test.
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
| The frontend paste/submit loop remains a separately ruled follow-up surface. | — | [terminal.ts](agents-remember/dashboard/src/data/terminal.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests cover local serving behavior only. | - | - |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 removal round + case (f): replaced capture-echo tests
  with log-probe acceptance and bounded retry-order tests, including duplicate-chip blocking,
  clear-and-verify replacement, unobservable failure, settle floor, and no-Escape. Verification
  metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-07T23:20+02:00 — 260707-HFX-L3 round 2: `_ScrollingCodexPane` (bounded suffix window with
  tmux-faithful top-eviction) pins the scroll-out case — delivered with exactly ONE paste even when
  the final window shows no net generic chip growth (the payload-specific probe rescue); the test
  asserts the blindness premise itself, so dropping the specific probe fails it with duplicates.
  `CaptureWindowTests` pins the literal `capture-pane -p -S -200` argv.
- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): added `ChipCountTests` (both
  chip vocabularies) and `DeliveryIntegrityTests` — `_CodexChipPane` single-paste confirmation,
  `_LaggyChipPane` retry-after-partial with exactly one paste (the F-V race, re-capture sees the
  landed chip), verification-failure capture attachment, the Escape refusal, and only-Enter across
  paste+submit; the fake pane's injectable seam renamed `set_buffer` → `load_buffer` with the
  paster. Verification metadata pinned until closeout stamps the HFX-L3 commit.
- 2026-07-04T12:31+02:00 - L3: added the harness-boot false-positive regression
  where pane output advances but no pasted draft/chip appears. Verification
  metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2: created coverage for the server-side echo-confirmed paste helper —
  sanitization, draft (no submit), paste+submit confirmation, unechoed boot-window retry reporting
  unconfirmed delivery, and unconfirmed submit — against an in-memory fake pane + injected clock/sleep.
  Verification metadata pinned until closeout stamps the L2 commit.
