# skills/l-01-agent-lifecycles/roles/architect.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/architect.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

## Governing Overview

[l-01 role overview](overview.md)

## Purpose

This source participates in the L4 spawn → readiness → dispatch contract and owns the
pre-topology requirement compiler gate. It creates one immutable, version-addressed canonical
packet per independently falsifiable revision, records corpus approval in the approved packet,
and only then projects filtered links into task topology.

## Code Commentary

### Logic

The architect compiles and cold-reads the complete requirement corpus before creating task
topology. A later semantic change retains the stable ID, creates a new version-addressed packet,
records the new durable ruling, invalidates only affected acceptance, and rebriefs affected leaves.

Delivery roles may diagnose a requirement contradiction but cannot change the packet. The
architect verifies the contradiction and presents a proposed semantic revision to the developer.
Implementation, evidence, and test/tool fixes leave the semantic version unchanged and remain
protocol events until an exact candidate is handed to review. Only that review handoff, or a
successor handoff after reviewer rejection, advances attempt lineage; only explicit developer
approval increments the requirement version.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization
outputs. Dispatch proof remains exact-session and fail-closed. An approved requirement packet is
never rewritten in place. A worker/reviewer classification cannot become semantic authority.

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

- 2026-08-27T21:53+02:00 — M40@v2: separated internal repair/test protocol events from formal
  review-handoff attempt lineage while preserving developer-only semantic revision authority.
- 2026-08-27T18:06+02:00 — M43: recorded architect/developer authority for requirement revisions
  and kept ordinary implementation, evidence, and test/tool repairs on attempt lineage rather than
  semantic versioning.
- 2026-08-27T14:04+02:00 — M39 clarification: recorded immutable version-addressed packets,
  packet-local durable corpus approval, and new-file revision handling rather than in-place edits.
- 2026-08-27T13:32+02:00 — M39@v1: the architect now compiles, splits, packets, cold-reads, and
  obtains developer approval for requirement revisions before creating topology; leaf projection
  and version-change invalidation/rebriefing are explicit. Verification remains closeout-owned.

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
