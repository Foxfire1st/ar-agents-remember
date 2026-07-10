# test_pane_signals.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_pane_signals.py`           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T13:03+02:00                     |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce` |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

`test_pane_signals.py` covers the supervisor sweep's pane-state classifier
(`serving/pane_signals.py::classify_pane_signal`, 260707-HFX2-L2 R2a/R6): every trigger family, the
no-trigger fallback, blank/`None` input, and the precedence rule between the mid-turn and blocked
marker families.

## Code Commentary

### Logic

**260707-HFX2-L15 coverage.** Empty-composer and paste-chip classifier cases were deleted with the
retired `never-briefed`/`delivery-stalled` signals. The remaining suite pins only mid-turn,
blocked/modal labeling, and normal fallback diagnostics.

One test class, `PaneSignalClassifierTests`, eight tests, each a plain scripted pane-text string (no
model, no tmux, no fixtures beyond a literal string):

- `test_empty_composer_post_boot_is_never_briefed` — a bare `>` prompt classifies `never-briefed`.
- `test_two_stacked_paste_chips_is_delivery_stalled` — two `[Pasted Content ...]` chip markers
  classify `delivery-stalled`.
- `test_one_paste_chip_alone_is_not_delivery_stalled` — a single chip alone (under
  `STACKED_CHIP_THRESHOLD`) falls through to `never-briefed` instead, since the pane still shows an
  empty composer — pins that one chip is not itself a trigger.
- `test_esc_to_interrupt_is_mid_turn` — the busy marker classifies `mid-turn`.
- `test_modal_confirmation_is_blocked` — "Do you want to..." + "(y/n)" classifies `blocked`.
- `test_ordinary_output_is_normal` — plain narrative text with no marker classifies `normal`.
- `test_blank_pane_is_normal_not_a_trigger` — both `""` and `None` classify `normal` (never raise).
- `test_mid_turn_takes_precedence_over_blocked_markers` — a pane containing BOTH a blocked-shaped
  phrase ("Do you want to keep going?") and a busy marker classifies `mid-turn`, pinning that the
  busy check runs first regardless of where in the text each marker appears.

### Conventions

Standard suite bootstrap (`MCP_SRC` path insert, `unittest`). No temp files, no fixtures package —
every case is a literal pane-text string, matching the classifier's pure-function contract.

### Invariants And Boundaries

- Every test passes an explicit `harness=` kwarg (`"codex"` or `"claude"`) even though the
  per-harness override tables are currently empty, so a future non-empty override table cannot
  silently change these fixtures' expected outcome without a visible test failure.
- No test exercises the per-harness override path itself (both harnesses currently fall through to
  the shared tables) — a future harness-specific marker addition should add a dedicated test rather
  than assume coverage here.

### Todos

No known follow-up in this file.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation; this is a
same-repository unit-test suite for internal control-plane plumbing with no external spec.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines pane-signal classification; the leaf task doc (R2a) is the source of truth this suite pins. | L1-L62 | [test_pane_signals.py](test_pane_signals.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The classifier under test, including the precedence order and per-harness override tables this suite pins. | whole module | [../src/agents_remember/serving/pane_signals.py](../src/agents_remember/serving/pane_signals.py) |
| The chip-counting helper the delivery-stalled fixtures exercise indirectly through the classifier. | `count_paste_chips` | [../src/agents_remember/serving/terminal_paste.py](../src/agents_remember/serving/terminal_paste.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Classifier-local behavior only. | — | — |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 removal round: removed screen-delivery predicate tests;
  retained supervisor intervention/failure diagnostics only. Verification metadata remains pinned
  until closeout stamps the eventual L15 code commit.

- 2026-07-08T18:45+02:00 — Created for 260707-HFX2-L2 (supervisor sweep + predicates, R2a/R6): eight
  tests over `classify_pane_signal` — every trigger family (mid-turn, blocked, delivery-stalled,
  never-briefed), the normal fallback, blank/`None` input, the single-chip-is-not-yet-stalled edge
  case, and the mid-turn-over-blocked precedence rule. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L2 commit.
