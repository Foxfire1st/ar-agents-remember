# mcp/src/agents_remember/serving/agent_notifier_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/src/agents_remember/serving/agent_notifier_models.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-08T21:20+02:00 |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`|
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
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
`AgentNotifierContext`, and `SweepState`; `FindingKind`/`ActionKind` literal values are unchanged.

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

- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path and recorded the `AgentNotifier*` model names. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: recorded the injected single-snapshot seam and
  post-compaction folded inbox state carried through the supervisor context/state models.
  Verification metadata remains pinned until closeout stamps the candidate commit.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
