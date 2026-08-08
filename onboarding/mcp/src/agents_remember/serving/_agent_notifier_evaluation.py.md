# mcp/src/agents_remember/serving/_agent_notifier_evaluation.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_agent_notifier_evaluation.py`                                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-08T21:20+02:00                                            |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`                                        |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_agent_notifier_evaluation.py` (renamed from `_supervisor_evaluation.py` in 260713-TES-L1); owns the behaviours named by its top-level symbols. The rename window adds the seat-liveness ask-identity seam: `SEAT_LIVENESS_ASK_PREFIXES` names both the current (`"Agent notifier observed seat-liveness:"`) and legacy (`"Supervisor observed seat-liveness:"`) prefixes, and `_seat_liveness_ask_identity` normalizes either prefix to one `seat-liveness:` identity so legacy pending rows still coalesce/renew and chain-progress suppression matches both formats.

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

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_agent_notifier_evaluation.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
## Update History

- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded `SEAT_LIVENESS_ASK_PREFIXES` + `_seat_liveness_ask_identity` (fix round 1, reviewer F1) and the legacy+current createdBy/prefix acceptance in the chain-progress predicate. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
