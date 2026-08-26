# skills/l-01-agent-lifecycles/roles/architect.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/architect.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-26T08:35+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

## Governing Overview

[l-01 role overview](overview.md)

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

## L23 Thematic Master Recovery

The architect treats a resumed master that trails super as a synchronization
condition on the existing thematic master, not a reason to fork a replacement
master. The plane derives ancestry from task structure and returns the contract
address needed for backend recovery.

## 260713-TES-L5 Current Delta — Mailbox Custody, Not Ladder Rungs

The terminal-custody section now says rows whose entire owner chain is dead surface to the
architect as a mailbox (the timed escalation ladder is retired), rows land at the architect's
turn boundary (the system acks), and `operator_inbox_consume` is an optional attribution
marker. The developer remains an authority, not an address.

## 260815-DAG-L2 Planning Authority

The architect inspects `executionGraph` plus every commanded master's `executionNature` before
spawning backend execution. A missing or materially stale topology produces a recommendation to
run a strategist, never an automatic dispatch. The initial strategist and its plan-review reviewer
are architect children and finish before the orchestrator exists; runtime reshapes still route
through that architect-owned loop. A strategist skip authorizes the orchestrator to author the
same explicit artifact, not an implicit default.

## IAS Source-Pair Activation Planning Boundary

The reviewed graph-less choice is now the source-pair-selected atomic-sequential mode. Canonical
commanded-master order is only the stable equal-priority tie-break; selecting another atomic master
may logically pause the former without forcing integration, contract retirement, or process and
worktree termination. The architect therefore judges dependency truth independently of runtime
selection and does not manufacture an edge merely to explain serialization.

Task-document authoring remains wholly upstream of activation and queue state. The architect may
approve otherwise-valid task changes; the affected disposable projection is then invalidated and
rebuilt. A selector or queue cannot veto planning, and no valid task/master is discarded merely to
free a runtime selection.

## Update History

- 2026-08-26T08:35+02:00 — Restored the required navigable governing-overview link while
  reconciling architect activation doctrine.

- 2026-08-26T05:20+02:00 — Reconciled architect doctrine with graph-less source-pair activation,
  pause-without-retirement, task-authoring primacy, and queue/projection invalidation. Final source
  ranges and verification remain post-Dagger/closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: recorded architect ownership of strategist planning,
  explicit topology admission, and the complete/still-valid condition for recommending a skip.
  Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented canonical thematic-master recovery semantics;
  verification remains closeout-owned.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the custody rewrite — rows whose
  entire owner chain is dead surface to the architect as a mailbox, not a ladder rung (the
  timed escalation ladder is retired); rows land at the architect's turn boundary and
  `operator_inbox_consume` is an optional attribution marker, never a mechanical ack.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
