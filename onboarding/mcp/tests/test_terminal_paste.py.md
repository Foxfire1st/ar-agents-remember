# mcp/tests/test_terminal_paste.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_terminal_paste.py`                |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-10T13:03+02:00                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                  |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_terminal_paste.py` covers the server-side capture-verified paste helper
(`serving.terminal_paste`). The paster mirrors the frontend `pasteAndConfirm` / `submitAndConfirm`
over tmux primitives; every tmux operation is injectable through cit:([`TerminalPasterSeams`], mcp/src/agents_remember/serving/terminal_paste.py:117-131),
so the confirmation ladder runs against an in-memory tmux double — no real tmux server and no real
sleeping (a stepped clock makes the timeouts deterministic). The suite is module-level pytest
functions (24 tests): the paste ladder's acceptance/retry/failure arms, the dispatch policy's
suppression-window discipline, and the sanitizer.

## Code Commentary

### Logic

The suite drives an acceptance callback and pane-verified absence rather than pane echo.
`_Clock` (cit:([`_Clock`], mcp/tests/test_terminal_paste.py:16-23)) advances a fixed step per call so timeouts are hit
deterministically, `_Tmux` (cit:([`_Tmux`], mcp/tests/test_terminal_paste.py:26-70)) is an in-memory tmux double whose
`load`/`paste`/`key`/`capture`/`sleep` seams can also REFUSE per command (`paste_results`,
`failing_keys`) — each failure maps to a different paster verdict — and cit:([`_paster`], mcp/tests/test_terminal_paste.py:73-83)
wires the double plus the clock into a `TerminalPaster` through `TerminalPasterSeams`.

- Sanitization: cit:([`test_sanitize_strips_control_noise_and_nested_paste_markers`], mcp/tests/test_terminal_paste.py:86-88)
  pins `sanitize_for_injection` against control noise and nested bracketed-paste markers.
- Success path: cit:([`test_success_uses_log_probe_and_never_captures_pane`], mcp/tests/test_terminal_paste.py:91-97) — a
  confirmed paste uses the log probe and never captures the pane.
- Ladder windows: cit:([`test_first_absence_waits_full_window_before_enter_repress`], mcp/tests/test_terminal_paste.py:201-217),
  cit:([`test_repaste_happens_only_after_enter_repress_window`], mcp/tests/test_terminal_paste.py:220-236), and
  cit:([`test_exhausted_ladder_returns_the_final_failure_capture`], mcp/tests/test_terminal_paste.py:239-252) pin the full
  calibrated-window order, one Enter re-press, one re-paste only after verified absence, and the
  final failure capture.
- Chip guards: cit:([`test_duplicate_chip_blocks_repaste_when_clear_does_not_remove_it`], mcp/tests/test_terminal_paste.py:255-276),
  cit:([`test_visible_composer_chip_is_cleared_before_replacement`], mcp/tests/test_terminal_paste.py:279-299), and
  cit:([`test_unobservable_pane_blocks_repaste`], mcp/tests/test_terminal_paste.py:302-315) pin duplicate-chip blocking,
  clear-before-replacement, and unobservable fail-closed behavior.
- Discipline: cit:([`test_settle_guard_is_at_least_100ms`], mcp/tests/test_terminal_paste.py:318-335),
  cit:([`test_unbound_command_never_claims_log_acceptance`], mcp/tests/test_terminal_paste.py:338-344), and
  cit:([`test_escape_is_refused`], mcp/tests/test_terminal_paste.py:347-349) pin the >=100 ms settle floor, pre-bind command
  non-acceptance, and the Escape refusal.
- Dispatch policy: cit:([`test_dispatch_settle_is_strictly_beyond_codex_suppression_window`], mcp/tests/test_terminal_paste.py:352-353)
  plus cit:([`test_initial_dispatch_uses_one_paste_and_one_enter`], mcp/tests/test_terminal_paste.py:356-368) through
  cit:([`test_early_enter_control_is_suppressed_but_dispatch_enter_submits`], mcp/tests/test_terminal_paste.py:461-499) pin the
  dispatch ladder — one paste + one Enter initially, retry submitting a visible same draft without
  re-paste, re-paste only after verified absence, ambiguous duplicates and unrelated/historical
  drafts left pending, and Enter suppression outside the dispatch window.

### Conventions

Module-level `pytest` functions over two local doubles. The `_Tmux` double records every command
and can refuse per command (`paste_results`, `failing_keys`), because the paster's contract differs
per failure — an unwritten buffer is not delivered, a refused Enter is delivered but unsubmitted.
The stepped `_Clock` monotonic plus the injected `sleep` seam make every window (settle floor,
Enter re-press, re-paste) deterministic without real sleeping.

### Invariants And Boundaries

- No real tmux, no real sleep — the ladder runs against the tmux double + injected clock/sleep.
- The ladder must never submit an unconfirmed paste; the unwritable-buffer and refused-Enter cases
  assert no blind `Enter` crosses.
- Delivery truth is acceptance-probe + verified-absence based: a re-paste requires pane-verified
  absence, a duplicate chip that clear cannot remove blocks the re-paste, and an exhausted ladder
  returns the final failure capture.
- Escape never crosses the seam; the refusal is itself the contract under test.
- Sanitization strips control noise and nested paste markers before any buffer write.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation found; the behavior mirrors the frontend `data/terminal.ts`
paste loop, a local convention.

| Finding | Anchor | Source |
| --- | --- | --- |
| The tests pin the local server-side paste loop, not an external protocol. | `_paster` | mcp/tests/test_terminal_paste.py:73-83 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The paster + sanitizer under test (injectable tmux ops + confirmation loop). | `TerminalPaster` | mcp/src/agents_remember/serving/terminal_paste.py:48-51; mcp/src/agents_remember/serving/terminal_paste.py:206-511 |
| The frontend paste/submit loop remains a separately ruled follow-up surface. | `pasteAndConfirm` | dashboard/src/data/terminal.ts:174-188 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The tests cover local serving behavior only. | - | - |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## 260731-EFA-L2 Delta — the escalation ladder's failure arms

Five tests covering what the paste ladder does when a step will not take:

- acceptance on the **first** Enter climbs no rung of the ladder;
- an unwritable buffer reports `undelivered` and **never presses Enter** — a blind Enter into a
  seat whose buffer never took the text is how a wrong command gets submitted;
- a refused Enter ends the ladder as **delivered but unsubmitted** (a distinct state, not a
  failure);
- a refused clear key **blocks the repaste rather than appending**, so a retry cannot concatenate
  onto what is already in the buffer;
- dispatch recovery reports failure when the verified repaste cannot be written.

## Update History

- 2026-08-04T18:50+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 3 citation rows with exact anchors (`_paster` wiring, `TerminalPaster` with the sanitizer/seams extents, `pasteAndConfirm` frontend loop) and ledger-verified ranges. The frozen source showed the Purpose/Logic/Conventions/Invariants sections still described the removed 260707-HFX-L3 chip-echo suite (`_FakePane`/`_CodexChipPane`/`_LaggyChipPane`/`SanitizeTests`/`ChipCountTests`/`PasteTests`/`DeliveryIntegrityTests`/`count_paste_chips` — none present in the file), so those sections were rewritten against the actual ladder-based module-level pytest suite (`_Clock`/`_Tmux` doubles, `_paster` wiring, the 24 test functions) with cit citations. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

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
