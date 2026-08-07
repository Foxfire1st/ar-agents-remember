# mcp/src/agents_remember/serving/_supervisor_evaluation.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_supervisor_evaluation.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_supervisor_evaluation.py`; owns the behaviours named by its top-level symbols.

## Code Commentary

- `evaluate_pane_findings`
- `evaluate_expectation_findings`
- `turn_report_path_for_leaf_key`
- `evaluate_turn_report_findings`
- `evaluate_inbox_findings`
- `_ladder_terminal_and_dead`
- `evaluate_ladder_terminal_findings`
- `_age_seconds`
- `_expectation_chain_progressed`
- `_inactivity_signal_chain_progressed`
- `_stale_turn_state_due`
- `evaluate_seat_liveness_findings`
- `_delivery_failure_still_retrying`
- `EscalationSchedule`
- `evaluate_escalation_findings`
- `evaluate_dead_upstream_findings`
- `evaluate_predicates`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_supervisor_evaluation.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
