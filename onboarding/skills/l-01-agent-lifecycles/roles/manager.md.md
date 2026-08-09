# skills/l-01-agent-lifecycles/roles/manager.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/manager.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-12T14:20:00+02:00 |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32`|
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

## Governing Overview

Governing overview: skills/l-01-agent-lifecycles/roles/overview.md

## Purpose

This source participates in the L4 spawn → readiness → dispatch contract; onboarding preserves one-to-one source mapping and canonical ownership.

## Code Commentary

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

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the passive-contract rewrite —
## 260713-TES-L5 Current Delta — Passive Contract Without Inference

The manager's passive contract now states the agent-notifier sweep relays seat-state facts on
its mechanical tick and never infers expectations from artifacts, never climbs an escalation
ladder, and never respawns a seat; the manager is woken with pending signals and processes
them before ending the turn (no watcher).

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the passive-contract rewrite —
  the agent-notifier sweep relays seat-state facts only; it never infers expectations from
  artifacts, never climbs an escalation ladder, and never respawns a seat. The manager's job
  stays "be woken with your pending signals and process + ack every item" with no watcher.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
