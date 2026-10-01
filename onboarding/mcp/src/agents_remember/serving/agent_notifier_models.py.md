# mcp/src/agents_remember/serving/agent_notifier_models.py

## Governing Overview

[overview.md](overview.md)
## Purpose

Defines the immutable notifier finding/action/result records and the injected sweep context shared
by notifier evaluation and action modules. Findings carry canonical task-document identity when
they refer to a qualified seat.

## Code Commentary

### 260712-TRH-L5 Evidence Injection

`AgentNotifierContext.tmux_name_snapshotter` is the single injectable seam for the confirmed-gone
reconciliation. Production defaults to `snapshot_tmux_session_names`; tests can provide one
bounded snapshot implementation and prove that catalog-present subjects never invoke tmux.
`SweepState.inbox_current` carries the post-compaction folded snapshot into the rest of the
sweep, preserving one-fold boundedness and same-sweep redelivery exclusion.

### 260713-TES-L1 Rename

Module renamed from `supervisor_models.py` (internal-only rename, no wire/persisted surface): the
frozen models are `AgentNotifierFinding`, `AgentNotifierActionResult`, `AgentNotifierSweepResult`,
`AgentNotifierContext`, and `SweepState`; `FindingKind`/`ActionKind` literal values are unchanged
until 260713-TES-L2 (below).

### 260713-TES-L2 Relay Findings And Actions

`FindingKind` gained `state-signal-due`, `non-reaction-due`, and `boundary-drain`, and retired
`turn-report-stale` (the artifact-presence/SLA predicate on the worker→manager path). `ActionKind`
correspondingly gained `state-signal`, `non-reaction`, and `boundary-drain`
cit:([`FindingKind`, `ActionKind`], mcp/src/agents_remember/serving/agent_notifier_models.py:26-50).

### 260713-TES-L3 Compound-Idle Kinds

`FindingKind` gained `compound-idle-due` cit:([`FindingKind`], mcp/src/agents_remember/serving/agent_notifier_models.py:26-38) (between `state-signal-due` and
`non-reaction-due` in the Literal) and `ActionKind` gained `compound-idle`
cit:([`ActionKind`], mcp/src/agents_remember/serving/agent_notifier_models.py:39-50), consumed by `_emit_compound_idle` and its
`AgentNotifierActionResult`.

### 260713-TES-L4 Rebind, Expire, And TTL-Expired Kinds

`FindingKind` gained `rebind-due`, `rebind-expired`, and `inbox-ttl-expired`
cit:([`FindingKind`], mcp/src/agents_remember/serving/agent_notifier_models.py:26-38) and `ActionKind` gained `rebind` and `expire`
cit:([`ActionKind`], mcp/src/agents_remember/serving/agent_notifier_models.py:39-50) — the N14 rebind family, the N2 grace-expiry terminal, and the §9
pending-TTL resolution boundary, consumed by `_rebind_due`/`_rebind_expired`/`_expire_pending`
in `_agent_notifier_actions.py`.

### Logic

`AgentNotifierFinding` carries kind, subject session, optional `TaskDocumentRef`, seat role, timing,
and detail without deciding the action. `AgentNotifierContext` owns injected stores, clocks, and
host/catalog seams; `SweepState` freezes one bounded sweep snapshot.

### Invariants And Boundaries

- A finding's task identity is a structured `TaskDocumentRef`; consumers must not infer a leaf key.
- These records describe evidence and planned actions. Evaluators choose findings and action
  modules perform effects.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

### Cross-Repo References

No meaningful cross-repo references.

## 260713-TES-L5 Current Delta — Fact-Only Vocabulary And Context

`FindingKind` removes `expectation-overdue`, `inbox-ladder-terminal`, and `escalation-due`;
`ActionKind` removes `ladder-resolve`, `auto-nudge`, and `escalate-rung`. `AgentNotifierContext`
no longer carries `nudge_store`, `nudge_rate_limit_seconds`, `escalation_sla_seconds`,
`escalation_rung_seconds`, or `respawn_after_rung`; `escalation_budget` (250) stays as the
per-sweep owner-signal load-shed cap. `SweepState` drops `escalated_entry_ids` (no rung tracking)
and keeps the expectation snapshot only for the compaction read. This entry supersedes any
earlier description in this sidecar that conflicts with the current source behavior above;
verification metadata stays pinned to the pre-commit source history until closeout.

## 260821-CLIVE Execution Registrar Seam

`AgentNotifierContext.register_execution_evidence` accepts the current inbox snapshot and returns
the exact ids whose first-execution evidence is now durable in task truth. `None` authorizes no
deletion of task-bound leaf reports; it is a fail-closed injection state, not a compatibility reader.
