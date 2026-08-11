# mcp/src/agents_remember/serving/terminal_paste.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/terminal_paste.py`     |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-10T13:03+02:00                                  |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this server-side tmux paste/submit loop. | — | — |

## Repo-Internal References

The current acceptance/retry contract is implemented and tested locally; the older capture-echo
rows below are retained only as historical provenance for the superseded L3 mechanism.

| Finding | Anchor | Source |
| --- | --- | --- |
| Submitted acceptance is callback-driven; recovery is one Enter re-press then one verified-absence clear/replace re-paste. | `TerminalPaster`, `_paste_verified`, `_retry_repastes` | mcp/src/agents_remember/serving/terminal_paste.py:206-511 |
| Tier 3 preserved: the historical row names a deleted `DeliveryIntegrityTests` grouping; the current focused tests retain the duplicate-chip, clear-before-replacement, unobservable-pane, settle-floor, and Escape evidence as standalone functions. | `test_duplicate_chip_blocks_repaste_when_clear_does_not_remove_it`, `test_visible_composer_chip_is_cleared_before_replacement`, `test_unobservable_pane_blocks_repaste`, `test_settle_guard_is_at_least_100ms`, `test_escape_is_refused` | mcp/tests/test_terminal_paste.py:255-276; mcp/tests/test_terminal_paste.py:279-299; mcp/tests/test_terminal_paste.py:302-315; mcp/tests/test_terminal_paste.py:318-335; mcp/tests/test_terminal_paste.py:347-349 |

| Finding | Anchor | Source |
| --- | --- | --- |
| Tier 3 preserved: the historical row says `spawn_agent_session` pastes a worker/draft context packet, but the current spawn contract returns `spawned-unbriefed` and refuses legacy context/submit inputs before durable brief delivery. | `spawn_agent_session_tool` | mcp/src/agents_remember/application/terminal_tools.py:769-842 |
| `POST /api/terminal/{session}/paste` is the serving endpoint mirror (404 on unknown/gone session, else delivered/submitted). | `api_terminal_paste`, "def _paste_response(" | mcp/src/agents_remember/serving/_app_terminal_routes.py:504-504; mcp/src/agents_remember/serving/_app_terminal_routes.py:717-729 |
| It mirrors the frontend `pasteAndConfirm` / `submitAndConfirm` bracketed-paste + echo-confirm loop. | `pasteAndConfirm`, `bracketedPaste`, `sanitizeForInjection` | dashboard/src/data/terminal.ts:87-89; dashboard/src/data/terminal.ts:99-107; dashboard/src/data/terminal.ts:174-188 |
| Tier 3 preserved: the historical unit-test row names deleted `DeliveryIntegrityTests` and its chip-vocabulary counter; the current focused tests retain the one-paste, duplicate-chip, failure-capture, Escape, and Enter evidence as standalone functions. | `test_initial_dispatch_uses_one_paste_and_one_enter`, `test_dispatch_retry_leaves_ambiguous_duplicate_chips_pending`, `test_exhausted_ladder_returns_the_final_failure_capture`, `test_escape_is_refused`, `test_early_enter_control_is_suppressed_but_dispatch_enter_submits` | mcp/tests/test_terminal_paste.py:239-252; mcp/tests/test_terminal_paste.py:347-349; mcp/tests/test_terminal_paste.py:356-368; mcp/tests/test_terminal_paste.py:406-423; mcp/tests/test_terminal_paste.py:461-499 |
| Tier 3 preserved: the historical row says inbox hosted push records a pane-capture tail, while the current protocol delivery records adapter correlation/detail and never invokes the pane paster. | `deliver_inbox_entry`, `_record_reconciliation` | mcp/src/agents_remember/serving/inbox_delivery.py:170-228; mcp/src/agents_remember/serving/inbox_delivery.py:293-325 |
| `capture_pane` is called from the liveness sweeper's alive-harness-row turn-state classification path. | `_observe_alive`; `pane_capturer` | mcp/src/agents_remember/serving/terminal_liveness.py:82-82; mcp/src/agents_remember/serving/terminal_liveness.py:327-393 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This helper drives only a local tmux session over the tmux CLI. | `TerminalPasterSeams`, `_tmux_load_buffer`, `_tmux_paste_buffer`, `_tmux_send_key`, `_tmux_capture_pane` | mcp/src/agents_remember/serving/terminal_paste.py:117-131; mcp/src/agents_remember/serving/terminal_paste.py:134-148; mcp/src/agents_remember/serving/terminal_paste.py:151-163; mcp/src/agents_remember/serving/terminal_paste.py:166-178; mcp/src/agents_remember/serving/terminal_paste.py:185-198 |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## 260731-EFA-L2 Current Delta

The recovery contract and the impure boundary became named values, and dispatch became its own
public method.

- **`AcceptanceWindow`** (`flush_window=30.0`, `poll_interval`; default
  `DEFAULT_ACCEPTANCE_WINDOW`) — how long one Enter is given to show up in the harness log, and how
  often that is checked. One calibration: the poll interval is meaningless without the window it
  divides, and shortening the window without tightening the interval changes how many probes a
  submission actually gets. Every rung of the ladder waits exactly one of these.
- **`PasteRecoveryLadder`** (`window`, `settle_delay=0.1`, `enter_represses=1`, `repastes=1`,
  `clear_key="C-u"`; default `DEFAULT_PASTE_LADDER`) — the **fixed, bounded** recovery contract for
  one verified paste. Three rungs in order, each ending the moment the harness log confirms
  acceptance: the initial paste+Enter, then `enter_represses` bare Enter re-presses for a composer
  that held the text unsubmitted, then `repastes` clear/replace re-pastes driven by `clear_key`.
  The bounds ARE the contract — "fixed and bounded recovery" is a single safety property, and
  raising one bound without the others silently changes how many duplicate submissions the ladder
  can produce.
- **`TerminalPasterSeams`** (`load_buffer`, `paste_buffer`, `send_key`, `capture_pane`, `sleep`,
  `monotonic`) — the impure surface a `TerminalPaster` drives: the tmux commands **and the clock**,
  because the recovery ladder is defined in seconds. One object for the same reason
  `TerminalHostSeams` is; `None` keeps the real implementation.

**`paste_dispatch(tmux_name, text, *, accepted, policy, window=DEFAULT_ACCEPTANCE_WINDOW)`** is now
a public method, separate from `paste`. It submits one durable brief **exact-once**: no Enter
re-presses, no duplicate re-pastes. The harness-log probe is **mandatory in its signature** — a
durable brief that cannot be proven accepted must fail rather than be retried into a duplicate.
Correspondingly, `paste()` no longer takes `dispatch_policy`, and its old runtime guard
(`ValueError("dispatch paste requires a harness-log acceptance probe")`) is gone: the requirement is
now carried by the type. `paste()` keeps its own contract — `accepted=None` is allowed only for
draft transport or a spawn command whose evidence is checked retroactively, and never produces
`submitted=True`.

The verified path is also decomposed into named rungs: `_paste_verified`, `_retry_enter_represses`,
`_retry_repastes`, `_clear_prior_payload`, `_press_enter_and_await`, `_compose_dispatch`,
`_await_acceptance`.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: curated 9 reference rows (5 Tier 2 and 4 Tier 3 preservation rows), normalized 1 no-domain placeholder, and resolved the substantive local-tmux Cross-Repo row; scoped citation fixing regenerated the Tier-2 source ranges.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `AcceptanceWindow`, `PasteRecoveryLadder`, `TerminalPasterSeams` and the public `paste_dispatch` split — the mandatory acceptance probe is now signature-enforced, replacing the removed `ValueError` guard.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

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
