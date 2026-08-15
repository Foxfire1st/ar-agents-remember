# skills/l-01-agent-lifecycles/roles/orchestrator.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/orchestrator.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-15T04:32+02:00 |
| lastVerifiedCommitHash |  `20cfd54cb0a3d425424afdfbb6d8c97f669cdcc4`|
| lastVerifiedCommitDate |  2026-08-15T05:12:01+02:00|
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

## Governing Overview

Governing overview: skills/l-01-agent-lifecycles/roles/overview.md

## Purpose

This source participates in the L4 spawn → readiness → dispatch contract; onboarding preserves one-to-one source mapping and canonical ownership.

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

This source participates in the L4 spawn → readiness → dispatch contract; onboarding preserves one-to-one source mapping and canonical ownership.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization outputs. Dispatch proof remains exact-session and fail-closed.

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
super moves. Atomic masters are exclusive barriers whose intermediate leaf state never reaches
super. Integration refs are not feature/fix workbenches, and super-exit repairs return to an owning,
reopened, or newly scoped leaf.

## Update History

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: recorded ready-frontier recomputation, auditable queue
  judgment, organizational direct landing, atomic barriers, and no-workbench repair routing.
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
