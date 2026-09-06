# mcp/tests/test_terminal_paste.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_terminal_paste.py`                |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Uses injected tmux operations, log evidence and a stepped clock to test safe paste/submission. Log-confirmed success avoids pane capture, an unwritable buffer never presses Enter, and an unobservable pane blocks repaste. Retry submits a visible matching draft once but leaves unrelated or historical-marker drafts pending. These six cases are not a live tmux acceptance suite.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Success uses log probe and never captures pane | `test_success_uses_log_probe_and_never_captures_pane` | mcp/tests/test_terminal_paste.py:82-88 |
| An unwritable buffer reports undelivered and never presses enter | `test_an_unwritable_buffer_reports_undelivered_and_never_presses_enter` | mcp/tests/test_terminal_paste.py:91-106 |
| Unobservable pane blocks repaste | `test_unobservable_pane_blocks_repaste` | mcp/tests/test_terminal_paste.py:109-122 |
| Dispatch retry submits visible same draft without repaste | `test_dispatch_retry_submits_visible_same_draft_without_repaste` | mcp/tests/test_terminal_paste.py:125-141 |
| Dispatch retry leaves unrelated codex draft pending | `test_dispatch_retry_leaves_unrelated_codex_draft_pending` | mcp/tests/test_terminal_paste.py:144-158 |
| Dispatch retry does not submit historical matching marker | `test_dispatch_retry_does_not_submit_historical_matching_marker` | mcp/tests/test_terminal_paste.py:161-176 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


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
