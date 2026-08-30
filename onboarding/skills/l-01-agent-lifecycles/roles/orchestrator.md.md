# skills/l-01-agent-lifecycles/roles/orchestrator.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/orchestrator.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-30T12:57+02:00 |
| lastVerifiedCommitHash |  `f9f92ca793811b6cb738d7e302dfecdf8636e96e`|
| lastVerifiedCommitDate |  2026-08-30T14:26:46+02:00|
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

## Governing Overview

[l-01 role overview](overview.md)

## Purpose

This source defines the sprint-bound orchestrator. It is a plane-hosted `dispatch_agent` caller for
direct manager and system-specialist children; it never selects ambient mode for those calls,
exposes readiness as a caller step, or retries a plane authorization failure through the launcher
path. The architect ordinarily creates this seat, while an identity-free developer launcher may
target it only for an explicit task-seat takeover.

## Code Commentary

### Completion Cleanup And Quality Retry Doctrine (260805-ARG-L1)

The master-to-super integration duty now keeps manager/orchestrator owners out of automatic
cleanup while retiring exact-leaf worker/reviewer/curator seats only after their durable report is
present; the opt-out restores landed behavior for those three subordinate roles. The quality
altitude paragraph also makes cheap-first ordering and content-addressed retry a pipeline contract:
exact reuse or selected-test-only delta is automatic, ambiguous deltas run fresh, conservative
delta coverage falls back to one full selection, and CI never reuses local proof.

The current altitude contract is stricter than that historical retry description: targeted Dagger
runs exactly once when each leaf closes, leaf integration reruns nothing, and full Dagger runs once
when the master integrates into super. GitHub PR validation is a separate non-test check.

### Logic

The orchestrator submits a canonical child task document, target role, and complete brief once.
The control plane privately owns session creation, readiness proof, exact initial-brief pinning,
and rollback. Its role table therefore advertises the seat as a plane-hosted caller and an ambient
takeover target, while the public request contains no caller-kind or runtime-identity field. Its
`dispatch` and `tools` rows are structural documentation rather than settings keys. When the
developer explicitly selects this seat, the launcher converges on the canonical sprint-bound
orchestrator seat; it does not manually create or replace a live occupant.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization
outputs. Dispatch proof remains exact-session and fail-closed; plane refusal never becomes an
ambient retry.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

## Cross-Repo References

No meaningful cross-repo references.

## 260713-TES-L5 Current Delta — Idle Safety Via The State-Signal Relay

The orchestrator's idle-safety line now says silence is supervised by the agent-notifier sweep
and the state-signal relay; the escalation ladder is no longer part of the supervision story.
Ending a turn with nothing pending remains correct.

## R39 Generic Orchestrator Doctrine

The canonical orchestrator role resolves quality mechanics from the active repository memory and
keeps acceptance at leaf closeout and master integration only. Repository-specific Dagger/retry
instructions no longer leak into generic orchestration.

## 260815-DAG-L2 Ready-Frontier And Landing Authority

The orchestrator mechanically recomputes the ready frontier after candidate, blocker, landing, or
accepted-priority changes, then applies explicit priority judgment with canonical graph node order
only as the deterministic equal-priority tie-break. Every queue judgment records rationale,
evidence, author, confidence, and supersession before it changes selection; ordinary bounded
reprioritization stays here, while a substantial graph/classification reshape is proposed through
the architect-owned strategist loop.

Organizational leaves land directly on super as released; the final leaf is combined with prior
contributions into the exact proposed final candidate and receives the one full master gate before
super moves. Atomic masters expose no intermediate leaf state to super, but source-pair selection
may pause one live master and select another without retiring either durable branch. The separate
landing authority serializes only conflicting protected-ref movement. Integration refs are not
feature/fix workbenches, and super-exit repairs return to an owning, reopened, or newly scoped leaf.

## IAS Activation, Queue, And Reconciliation Boundary

Before a manager or worker receives implementation exposure for an atomic master, the control
plane selects its exact code/memory source pair as `reconciling`, auto-pauses the former selection,
reconciles both recorded bases, and publishes `active`. Reviewer and curator inspection does not
switch selection. Chats, processes, worktrees, contracts, and claimed lifecycle journals remain
intact across a logical pause.

Task authoring is not subordinate to selection or queue state. Valid task mutations publish first,
then invalidate/rebuild affected disposable projections. Queue rows merely observe
active/reconciling/paused/vacant facts and own no lifecycle or commit evidence. A malformed selector
fails closed only for affected projection/admission and is replaced with archived evidence by an
exact selecting operation; there is no contract-presence fallback.

Retained sync or integration conflicts are agent-owned when current requirements, code, tests, and
decisions determine a resolution. Continue or cancel the contract-addressed operation through its
advertised API; escalate only genuine semantic ambiguity through the architect.

## Update History

- 2026-08-30T12:57+02:00 — 260821-ARSPAWN-L3 review correction: replaced create/replace
  takeover wording with idempotent canonical-seat convergence. Verification remains
  closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 recorded the orchestrator as a plane-hosted caller
  and explicit ambient-takeover target, removed caller-visible readiness sequencing, and kept its
  structural authority outside settings. Verification remains closeout-owned.

- 2026-08-26T08:35+02:00 — Restored the required navigable governing-overview link while
  reconciling orchestrator activation doctrine.

- 2026-08-26T05:20+02:00 — Replaced the global exclusive-blocker reading with exact source-pair
  selection plus separate landing authority; documented pause preservation, task-authoring
  primacy, disposable queue projection, and agent-owned resumable conflict resolution.
  Verification remains post-Dagger/closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: recorded ready-frontier recomputation, auditable queue
  judgment, organizational direct landing, atomic blockers, and no-workbench repair routing.
  Verification remains closeout-owned.

- 2026-08-14T11:29+02:00 — R39 curator: reconciled canonical orchestrator guidance with generic
  repository-resolved policy. Verification remains closeout-owned.

- 2026-08-14T09:37+02:00 — Reopened L23 cadence: recorded the exact leaf-closeout/master-integration
  acceptance owners and the pull-request-only non-test GitHub boundary.
- 2026-08-10T07:30+02:00 — 260805-ARG-L1: recorded exact-leaf subordinate completion cleanup and
  the cheap-first/content-addressed quality retry doctrine. Verification metadata remains blank
  until closeout stamps the code commit.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the idle-safety wording — silence
  is supervised by the agent-notifier sweep and the state-signal relay; the escalation ladder
  is no longer part of the supervision story. Verification metadata pinned until closeout
  stamps the 260713-TES-L5 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
