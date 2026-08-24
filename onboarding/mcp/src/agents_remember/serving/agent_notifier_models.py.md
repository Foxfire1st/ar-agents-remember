# mcp/src/agents_remember/serving/agent_notifier_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/src/agents_remember/serving/agent_notifier_models.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-24T14:43+02:00|
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | mcp/src/agents_remember/serving/overview.md |

## Governing Overview

Governing overview: mcp/src/agents_remember/serving/overview.md

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

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

## Cross-Repo References

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

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented the notifier's typed task-registration seam. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Replaced generic lifecycle prose and the leaf-key finding field with the
  notifier model's actual task-document identity and evaluation/action boundary.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged agent-notifier model vocabulary and rename seam; the sidecar remains accurate. Verification metadata remains pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the fact-only vocabulary —
  expectation/ladder finding and action kinds removed, nudge-store/escalation-knob fields
  dropped from `AgentNotifierContext`, `SweepState.escalated_entry_ids` removed.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded `rebind-due`/`rebind-expired`/
  `inbox-ttl-expired` in `FindingKind` and `rebind`/`expire` in `ActionKind` (N14/N2/§9).
  Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: recorded `compound-idle-due` in
  `FindingKind` and `compound-idle` in `ActionKind`. Verification metadata pinned until
  closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the new state-signal
  finding/action kinds and the removal of `turn-report-stale` (the 260713-TES-L1 "literal values
  unchanged" claim is superseded). Verification metadata pinned until closeout stamps the
  260713-TES-L2 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path and recorded the `AgentNotifier*` model names. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: recorded the injected single-snapshot seam and
  post-compaction folded inbox state carried through the supervisor context/state models.
  Verification metadata remains pinned until closeout stamps the candidate commit.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
