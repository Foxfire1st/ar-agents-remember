# mcp/src/agents_remember/serving/_agent_notifier_actions.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_agent_notifier_actions.py`                                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T03:51+02:00|
| lastVerifiedCommitHash | `7463b97a560e39367b9e31a687f09ea3f4f6b9f6`                                        |
| lastVerifiedCommitDate | 2026-08-09T04:22:51+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_agent_notifier_actions.py` (renamed from `_supervisor_actions.py` in 260713-TES-L1); owns the behaviours named by its top-level symbols. Since the rename, the file also owns the two event-name constants (`AGENT_NOTIFIER_EVENT_PREFIX` / `LEGACY_SUPERVISOR_EVENT_PREFIX`) and `_log_event`'s dual append that emits every agent-notifier event under both the current and the legacy observer name for the compatibility window. Since 260713-TES-L2 the one-row-per-root-cause posting primitives (`OwnerSignal`, `OwnerSignalOptions`, `_find_coalescible`, `_post_owner_signal`) moved OUT to `serving/owner_signals.py`, and the relay actions `_emit_state_signal` / `_emit_non_reaction` / `_drain_boundary` moved IN.
Since 260713-TES-L3 it also owns `_emit_compound_idle` (the orchestrator-facing compound-idle
emitter) and the manager-aware owner branch inside `_emit_non_reaction`.

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
- `_emit_compound_idle`
- `_emit_non_reaction`
- `_drain_boundary`
- `act_on_finding`

## 260713-TES-L2 Current Delta — Relay Actions

`_FINDING_ACTIONS` cit:([`_FINDING_ACTIONS`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:816-827) now maps `state-signal-due` → `_emit_state_signal`,
`non-reaction-due` → `_emit_non_reaction`, and `boundary-drain` → `_drain_boundary`, and no
longer maps the retired `turn-report-stale` kind (auto-nudge is inactive-only now). The two
emitters resolve the leaf's current manager via `derive_leaf_manager_owner`, post one
owner-addressed `state-signal` row with `DeliveryAdmission(boundary=True)`, record the
evidence/episode marker, and log `orchestration.agent-notifier.state-signal`. `_redeliver` cit:([`_redeliver`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:96-131) and `_escalate_rung` cit:([`_escalate_rung`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:401-462) pass `DeliveryAdmission(boundary=True)` for
state-signal rows as defense-in-depth behind the seam-level row-kind gate in
`inbox_delivery._delivery_refusal` (F1).

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260713-TES-L3 Current Delta — Compound-Idle Emitter And Manager Residue

`_FINDING_ACTIONS` cit:([`_FINDING_ACTIONS`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:816-831) now maps `compound-idle-due` →
`_emit_compound_idle` alongside the three L2 relay actions.

`_emit_compound_idle` cit:([`_emit_compound_idle`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:680-737) posts exactly one durable `state-signal` per
compound set to the owning orchestrator. The owner is `derive_signal_owner(sender=manager,
message_kind="state-signal")` — one hop up the spawn edge; a manager with no recorded
orchestrator edge is skipped ("no routable owner"), never routed by a global fallback (R4).
The episode signature is derived from the ACTION-time member read
(`compound_idle_signature(compound_idle_sets(...))`) and used for BOTH the ask and the
`compound_idle_emitted_for` marker write (fix round 1, F4); `finding.source_id` is trigger
only. Skip branches are fully covered (F5 — no `# pragma: no cover`): no seat row, no longer
idle at action time, already emitted on the fresh signature, and no routable owner. The post
rides `_post_owner_signal` with `DeliveryAdmission(boundary=True)` and
`OwnerSignal(message_kind="state-signal", ...)`; the marker write follows the durable append
so a lost-marker re-fire renews the one existing row (R7).

`_emit_non_reaction` cit:([`_emit_non_reaction`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:739-797) now branches on `entry.binding_role == "manager"`:
a manager's residue routes through `derive_signal_owner` to its orchestrator (one hop,
no-owner skip), while a worker's residue keeps the L2 `derive_leaf_manager_owner` rebinding
path. Compound-idle stays a pure seat-state signal; the non-reaction residue rides alongside
it and the orchestrator combines the two facts (N15/N16).

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_agent_notifier_actions.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
## Update History

- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: recorded `_emit_compound_idle` (action-time
  episode signature in ask + marker, master-scoped member read, one-hop orchestrator owner,
  no-owner skip, no coverage exemption, boundary-gated post) and the manager branch in
  `_emit_non_reaction` (manager residue → orchestrator; worker residue unchanged). Verification
  metadata pinned until closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the relay actions and the
  owner-signals extraction (posting primitives moved to `owner_signals.py`; retired
  `turn-report-stale` action; boundary admission on redeliver/escalate). Verification metadata
  pinned until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded the event dual-emission seam (`AGENT_NOTIFIER_EVENT_PREFIX` + `LEGACY_SUPERVISOR_EVENT_PREFIX` in `_log_event`) and the ask-prefix identity in `_find_coalescible`. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
