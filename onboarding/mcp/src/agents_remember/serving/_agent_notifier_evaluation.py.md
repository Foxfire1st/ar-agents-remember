# mcp/src/agents_remember/serving/_agent_notifier_evaluation.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_agent_notifier_evaluation.py`                                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T01:21+02:00                                            |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484`                                        |
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_agent_notifier_evaluation.py` (renamed from `_supervisor_evaluation.py` in 260713-TES-L1); owns the behaviours named by its top-level symbols. The rename window adds the seat-liveness ask-identity seam: `SEAT_LIVENESS_ASK_PREFIXES` names both the current (`"Agent notifier observed seat-liveness:"`) and legacy (`"Supervisor observed seat-liveness:"`) prefixes, and `_seat_liveness_ask_identity` normalizes either prefix to one `seat-liveness:` identity so legacy pending rows still coalesce/renew and chain-progress suppression matches both formats. Since 260713-TES-L2 the turn-report artifact/SLA predicates are retired and the state-signal families are composed from `serving/state_signals.py`.

## Code Commentary

- `evaluate_pane_findings`
- `evaluate_expectation_findings`
- `evaluate_inbox_findings`
- `_ladder_terminal_and_dead`
- `evaluate_ladder_terminal_findings`
- `_age_seconds`
- `_expectation_chain_progressed`
- `_inactivity_signal_chain_progressed` (matches both createdBy values and both ask prefixes)
- `SEAT_LIVENESS_ASK_PREFIXES`
- `_seat_liveness_ask_identity`
- `_stale_turn_state_due`
- `evaluate_seat_liveness_findings`
- `_delivery_failure_still_retrying`
- `EscalationSchedule`
- `evaluate_escalation_findings`
- `evaluate_dead_upstream_findings`
- `evaluate_predicates`

## 260713-TES-L2 Current Delta — Relay Predicates

`_INACTIVE_EXPECTATION_KINDS` cit:([`_INACTIVE_EXPECTATION_KINDS`], mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:35-35) is now `{verdict-by, ack-by}`: `briefed-by` rows are still
written and fulfilled as dashboard provenance but no longer drive any notifier finding.
`evaluate_turn_report_findings`/`turn_report_path_for_leaf_key` are deleted (the
artifact-presence/SLA interpretation on the worker→manager path, R6/N8). `evaluate_predicates` cit:([`evaluate_predicates`], mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:358-417) now composes the three relay families from `state_signals.py` —
`evaluate_state_signal_findings`, `evaluate_non_reaction_findings`, and
`evaluate_boundary_drain_findings` (the last bounded by `redeliver_budget`) — and excludes
`state_signal_landed`/`state_signal_held_on_boundary` rows from escalation findings and from the
sweep's redeliverable budget (F1).

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_agent_notifier_evaluation.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
## Update History

- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the relay predicate composition,
  `_INACTIVE_EXPECTATION_KINDS = {verdict-by, ack-by}`, the retired turn-report predicates, and
  the held/landed state-signal exclusions. Verification metadata pinned until closeout stamps
  the 260713-TES-L2 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded `SEAT_LIVENESS_ASK_PREFIXES` + `_seat_liveness_ask_identity` (fix round 1, reviewer F1) and the legacy+current createdBy/prefix acceptance in the chain-progress predicate. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
