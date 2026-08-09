# mcp/src/agents_remember/serving/_agent_notifier_actions.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_agent_notifier_actions.py`                                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T01:21+02:00                                            |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484`                                        |
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_agent_notifier_actions.py` (renamed from `_supervisor_actions.py` in 260713-TES-L1); owns the behaviours named by its top-level symbols. Since the rename, the file also owns the two event-name constants (`AGENT_NOTIFIER_EVENT_PREFIX` / `LEGACY_SUPERVISOR_EVENT_PREFIX`) and `_log_event`'s dual append that emits every agent-notifier event under both the current and the legacy observer name for the compatibility window. Since 260713-TES-L2 the one-row-per-root-cause posting primitives (`OwnerSignal`, `OwnerSignalOptions`, `_find_coalescible`, `_post_owner_signal`) moved OUT to `serving/owner_signals.py`, and the relay actions `_emit_state_signal` / `_emit_non_reaction` / `_drain_boundary` moved IN.

## Code Commentary

- `AGENT_NOTIFIER_EVENT_PREFIX` / `LEGACY_SUPERVISOR_EVENT_PREFIX`
- `_log_event` (dual event emission during the rename window)
- `_redeliver`
- `_resolve_ladder_terminal`
- `_escalate_inbox_entry`
- `_auto_nudge`
- `_mark_expectation_missed`
- `_signal_emit`
- `_rung_entry`
- `_escalate_rung`
- `_respawn_suspect`
- `_signal_dead_upstream`
- `_emit_state_signal`
- `_emit_non_reaction`
- `_drain_boundary`
- `act_on_finding`

## 260713-TES-L2 Current Delta — Relay Actions

`_FINDING_ACTIONS` cit:([`_FINDING_ACTIONS`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:744-755) now maps `state-signal-due` → `_emit_state_signal`,
`non-reaction-due` → `_emit_non_reaction`, and `boundary-drain` → `_drain_boundary`, and no
longer maps the retired `turn-report-stale` kind (auto-nudge is inactive-only now). The two
emitters resolve the leaf's current manager via `derive_leaf_manager_owner`, post one
owner-addressed `state-signal` row with `DeliveryAdmission(boundary=True)`, record the
evidence/episode marker, and log `orchestration.agent-notifier.state-signal`. `_redeliver` cit:([`_redeliver`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:96-131) and `_escalate_rung` cit:([`_escalate_rung`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:401-462) pass `DeliveryAdmission(boundary=True)` for
state-signal rows as defense-in-depth behind the seam-level row-kind gate in
`inbox_delivery._delivery_refusal` (F1).

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_agent_notifier_actions.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
## Update History

- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the relay actions and the
  owner-signals extraction (posting primitives moved to `owner_signals.py`; retired
  `turn-report-stale` action; boundary admission on redeliver/escalate). Verification metadata
  pinned until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded the event dual-emission seam (`AGENT_NOTIFIER_EVENT_PREFIX` + `LEGACY_SUPERVISOR_EVENT_PREFIX` in `_log_event`) and the ask-prefix identity in `_find_coalescible`. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
