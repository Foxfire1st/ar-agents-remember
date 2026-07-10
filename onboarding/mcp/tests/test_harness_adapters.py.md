# test_harness_adapters.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_harness_adapters.py`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T13:03+02:00                     |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814` |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

Created for 260707-HFX2-L3 (paste injector hardening, R2 + R5): covers the per-harness delivery
adapter (`serving/harness_adapters.py`) against captured-pane-shaped fixtures for BOTH known
harnesses (claude-code, codex) across the pilot run's trigger states — boot, ready (empty composer),
mid-turn, chip-stacked, and a modal trap (codex quota #20 / a permission prompt).

## Code Commentary

### Logic

**260707-HFX2-L15 coverage.** The suite now pins only stable known/generic adapter selection and
failure-only blocked-reason labeling. Boot/composer/mid-turn/turn-start delivery tests were removed
with the screen-acceptance mechanism.

Three test classes:

- `ClaudeCodeAdapterTests` / `CodexAdapterTests` — one adapter each, exercising every method
  (`boot_ready`, `composer_state`, `mid_turn`, `mid_turn_behavior`, `blocked_reason`,
  `turn_started`) against literal pane-text fixtures (`CLAUDE_BOOT`/`CLAUDE_READY`/... and their
  codex counterparts). `test_quota_modal_is_blocked_with_a_structured_reason` pins the issue #20
  distinction (`"codex-quota-limit"`) from an ordinary `"permission-prompt"`; `test_mid_turn_never_
  misread_as_blocked` pins that a busy marker wins even when a blocked-shaped phrase also appears
  in the same text (the precedence `pane_signals.classify_pane_signal` already enforces).
- `test_turn_started_corroborated_by_spinner_when_not_advanced` pins the harness-aware addition
  this leaf makes: `turn_started(pane, advanced=False)` still returns `True` when the pane shows a
  busy/spinner marker.
- `AdapterRegistryTests` — known ids resolve to the named singleton instances; an unknown/missing id
  falls back to a working generic adapter (never a refusal).

### Conventions

Plain literal pane-text fixtures (module-level constants), no tmux, no model — matches
`test_pane_signals.py`/`test_turn_state.py`'s existing fixture style for this same kind of
marker-based classifier.

### Invariants And Boundaries

- Every fixture is a captured-pane-SHAPED string, not a real capture — calibration against live
  harness panes is the same deferred Todo `pane_signals.py`/`turn_state.py` already carry.
- Tests exercise the ADAPTER, not the underlying classifiers directly (those have their own test
  files) — this suite pins the composition, not the classification internals.

### Todos

No known follow-up in this file.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation; this is a
same-repository unit-test suite for internal control-plane plumbing with no external spec.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines a per-harness delivery adapter; the leaf task doc (R2, R5) is the source of truth this suite pins. | whole module | [test_harness_adapters.py](test_harness_adapters.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The adapter under test. | `HarnessAdapter`; `get_adapter` | [../src/agents_remember/serving/harness_adapters.py](../src/agents_remember/serving/harness_adapters.py) |
| The underlying classifiers the adapter composes (their own dedicated fixtures live in their own test files). | `classify_pane_signal`; `composer_state` | [../src/agents_remember/serving/pane_signals.py](../src/agents_remember/serving/pane_signals.py) |
| | `classify_turn_state`; `boot_ready` | [../src/agents_remember/serving/turn_state.py](../src/agents_remember/serving/turn_state.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Adapter-local behavior only. | — | — |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 removal round: deleted screen-acceptance fixtures and
  retained only adapter identity plus failure-diagnostic modal labeling. Verification metadata
  remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-08T22:30+02:00 — Created for 260707-HFX2-L3 (paste injector hardening, R2 + R5): fixtures
  for both harnesses across boot/ready/mid-turn/chip-stacked/quota-modal, the codex-quota-vs-
  permission-prompt distinction, the spinner-corroborated `turn_started` addition, and the adapter
  registry's known-id/fallback behavior. Verification metadata pinned until closeout stamps the
  260707-HFX2-L3 commit.
