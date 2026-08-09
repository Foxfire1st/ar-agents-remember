# mcp/src/agents_remember/serving/_agent_notifier_evaluation.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_agent_notifier_evaluation.py`                                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T06:48+02:00|
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`                                        |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_agent_notifier_evaluation.py` (renamed from `_supervisor_evaluation.py` in 260713-TES-L1); owns the behaviours named by its top-level symbols. The rename window adds the seat-liveness ask-identity seam: `SEAT_LIVENESS_ASK_PREFIXES` names both the current (`"Agent notifier observed seat-liveness:"`) and legacy (`"Supervisor observed seat-liveness:"`) prefixes, and `_seat_liveness_ask_identity` normalizes either prefix to one `seat-liveness:` identity so legacy pending rows still coalesce/renew and chain-progress suppression matches both formats. Since 260713-TES-L2 the turn-report artifact/SLA predicates are retired and the state-signal families are composed from `serving/state_signals.py`.

Since 260713-TES-L3 the compound-idle predicate joins that composition.
Since 260713-TES-L4 the module owns the N14 rebind predicates (dead-target rows,
5-minute grace) and the N3/§9 pending-TTL expiry predicate, and no longer composes the timed
escalation ladder (dormant, N3).

## Code Commentary

- `evaluate_pane_findings`
- `evaluate_expectation_findings`
- `evaluate_inbox_findings`
- `_ladder_terminal_and_dead`
- `evaluate_ladder_terminal_findings`
- `_row_target_dead`
- `_row_dead_since`
- `evaluate_rebind_findings` (`REBIND_GRACE_SECONDS = 300.0`)
- `evaluate_pending_expiry_findings`
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

`_INACTIVE_EXPECTATION_KINDS` cit:([`_INACTIVE_EXPECTATION_KINDS`], mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:41-41) is now `{verdict-by}` — `ack-by`
retired with the 260713-TES-L4 N16 consume demotion (no post writes one anymore, and legacy
rows no longer nudge/escalate): `briefed-by` rows are still
written and fulfilled as dashboard provenance but no longer drive any notifier finding.
`evaluate_turn_report_findings`/`turn_report_path_for_leaf_key` are deleted (the
artifact-presence/SLA interpretation on the worker→manager path, R6/N8). `evaluate_predicates` cit:([`evaluate_predicates`], mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:474-523) now composes the relay families from `state_signals.py` —
`evaluate_state_signal_findings`, `evaluate_non_reaction_findings`,
`evaluate_boundary_drain_findings` (the last bounded by `redeliver_budget`), and since
260713-TES-L3 `evaluate_compound_idle_findings` (inserted after state-signal, before
non-reaction) — and excludes `state_signal_landed`/`state_signal_held_on_boundary` rows from
escalation findings and from the sweep's redeliverable budget (F1).

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260713-TES-L4 Current Delta — Rebind, Grace, And Pending-Expiry Predicates

`evaluate_rebind_findings` cit:([`evaluate_rebind_findings`], mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:176-219) is the N14 sweep-time rebind
predicate: a pending row whose addressed seat is dead (`_row_target_dead`) and whose
`derive_row_owner` resolves a different live owner emits `rebind-due`; with no replacement
after `REBIND_GRACE_SECONDS = 300.0` (anchored by the dead seat's terminal stamp, the row's
delivery timeline, or a bounded fallback — unparseable stamps keep the grace unmeasured,
fail-closed) it emits `rebind-expired`. `dispatch-brief` rows are never evaluated here
(exact-pinned). `evaluate_pending_expiry_findings` cit:([`evaluate_pending_expiry_findings`], mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:221-246)
emits `inbox-ttl-expired` for pending rows past `INBOX_PENDING_TTL_SECONDS` — the §9
resolution boundary that runs BEFORE compaction, so expiry is always surfaced first.

`evaluate_predicates` cit:([`evaluate_predicates`], mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:474-523) no longer composes
`evaluate_ladder_terminal_findings` or `evaluate_escalation_findings` (the timed ladder is
dormant, N3); the redeliverable-budget filter now also excludes `_row_target_dead` rows (the
rebind machinery owns dead-target rows), and the sweep composes expectation findings →
inbox findings (bounded) → dead-upstream → rebind/grace/expiry → state-signal →
compound-idle → non-reaction after the rebind/expiry families.

## 260713-TES-L3 Current Delta — Compound-Idle Predicate Composition

`evaluate_predicates` cit:([`evaluate_predicates`], mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:474-523) now composes FOUR relay families from
`state_signals.py`: `evaluate_state_signal_findings` → `evaluate_compound_idle_findings` →
`evaluate_non_reaction_findings` → `evaluate_boundary_drain_findings`. The compound predicate
stays a pure catalog read — no inbox or expectation input — and emits at most one finding per
manager seat per sweep (see `state_signals.py.md`).

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_agent_notifier_evaluation.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the N14 rebind predicates
  (`_row_target_dead`, `_row_dead_since`, `evaluate_rebind_findings`,
  `REBIND_GRACE_SECONDS=300.0`, dispatch-brief exclusion), the §9 pending-expiry predicate
  (`evaluate_pending_expiry_findings`, `inbox-ttl-expired`), the `ack-by` retirement in
  `_INACTIVE_EXPECTATION_KINDS`, and the removal of ladder/escalation predicate composition
  from `evaluate_predicates` (dormant ladder, N3) plus the dead-target redeliverable-budget
  exclusion. Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: recorded the compound-idle predicate
  composition in `evaluate_predicates` (state-signal → compound-idle → non-reaction →
  boundary-drain). Verification metadata pinned until closeout stamps the 260713-TES-L3
  commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the relay predicate composition,
  `_INACTIVE_EXPECTATION_KINDS = {verdict-by, ack-by}`, the retired turn-report predicates, and
  the held/landed state-signal exclusions. Verification metadata pinned until closeout stamps
  the 260713-TES-L2 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded `SEAT_LIVENESS_ASK_PREFIXES` + `_seat_liveness_ask_identity` (fix round 1, reviewer F1) and the legacy+current createdBy/prefix acceptance in the chain-progress predicate. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
