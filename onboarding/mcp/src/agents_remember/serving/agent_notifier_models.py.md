# mcp/src/agents_remember/serving/agent_notifier_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/src/agents_remember/serving/agent_notifier_models.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-09T06:48+02:00|
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`|
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview | mcp/src/agents_remember/serving/overview.md |

## Governing Overview

Governing overview: mcp/src/agents_remember/serving/overview.md

## Purpose

This source participates in the L4 spawn → readiness → dispatch contract; onboarding preserves one-to-one source mapping and canonical ownership.

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
cit:([`FindingKind`, `ActionKind`], mcp/src/agents_remember/serving/agent_notifier_models.py:27-49).

### 260713-TES-L3 Compound-Idle Kinds

`FindingKind` gained `compound-idle-due` cit:([`FindingKind`], mcp/src/agents_remember/serving/agent_notifier_models.py:27-38) (between `state-signal-due` and
`non-reaction-due` in the Literal) and `ActionKind` gained `compound-idle`
cit:([`ActionKind`], mcp/src/agents_remember/serving/agent_notifier_models.py:40-53), consumed by `_emit_compound_idle` and its
`AgentNotifierActionResult`.

### 260713-TES-L4 Rebind, Expire, And TTL-Expired Kinds

`FindingKind` gained `rebind-due`, `rebind-expired`, and `inbox-ttl-expired`
cit:([`FindingKind`], mcp/src/agents_remember/serving/agent_notifier_models.py:27-41) and `ActionKind` gained `rebind` and `expire`
cit:([`ActionKind`], mcp/src/agents_remember/serving/agent_notifier_models.py:43-56) — the N14 rebind family, the N2 grace-expiry terminal, and the §9
pending-TTL resolution boundary, consumed by `_rebind_due`/`_rebind_expired`/`_expire_pending`
in `_agent_notifier_actions.py`.

### Logic

This source participates in the L4 spawn → readiness → dispatch contract; onboarding preserves one-to-one source mapping and canonical ownership.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization outputs. Dispatch proof remains exact-session and fail-closed.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

## Cross-Repo References

No meaningful cross-repo references.
## Update History

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
