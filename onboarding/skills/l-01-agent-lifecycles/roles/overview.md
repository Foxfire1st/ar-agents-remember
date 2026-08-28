# skills/l-01-agent-lifecycles/roles

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `skills/l-01-agent-lifecycles/roles` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |

## Purpose

This route owns the self-contained lifecycle for each role. Every file states what one seat is,
which task-document altitude it occupies, the loop and artifacts it owns, its communication path,
and the work it must refuse or escalate.

## Hot Path Summary

### IAS Frozen Role Boundary

Architect, strategist, and orchestrator responsibilities operate on canonical task documents, not
on a queue-owned copy of the plan. They may change approved planning whenever their role authority
allows; downstream closeout projections are invalidated and rebuilt. For atomic work, selecting a
different live master pauses the old one and reconciles the new source pair before implementation
is exposed. No role should discard or terminalize a valid master merely to free scheduling state.

When source reconciliation retains a conflict, the assigned agent resolves and stages it in the
reported worktree, then continues the same contract-addressed operation or explicitly cancels it.
Private journal/ref identity stays in the plane; role briefs carry the public contract address and
recovery guidance.

Architect owns sprint-level direction, the initial plan loop, and strategist/reviewer lineage.
Strategist authors the evidence-cited dependency graph when dispatched. Orchestrator adopts the
ruled artifact, maintains the runtime frontier, and records bounded reprioritization judgments;
substantial reshapes return through the architect-owned strategist loop. Manager owns readiness
inside one organizational or atomic master. Worker owns one leaf, reviewer owns independent route
or completion verdict evidence, and curator reconciles ruled intent with implementation.

Organizational masters have no integration branch: their leaves are direct super descendants and
the final leaf is reviewed and full-gated as part of the exact proposed super candidate before it
lands. Atomic masters retain the branch-backed, no-partial-exposure block. A failed review routes
repair to an owning, reopened, or new scoped leaf—never to a master or super workbench.

Manager, orchestrator, and worker doctrine shares one quality altitude rule: the pinned Dagger
graph is the only Agents Remember acceptance environment. Leaf closeout selects targeted mode
exactly once; leaf integration and series closeout do not rerun it. The master gate selects full
mode once. Every run receives the explicit task-derived diff base. Host pytest/wrapper execution
is refused; a constrained lifecycle environment may explicitly configure a hard cap.

The manager also owns exact requirement-set compilation: each worker and reviewer receives the
same stable IDs applicable to the leaf. Workers give delivery and verification evidence per ID;
reviewers independently inspect that evidence and adjudicate every ID `accepted` or `rejected`.
Missing or wrong-class evidence, invalid citations, and missing developer approval reject the ID,
and one rejected ID prevents an overall pass. This requirement-acceptance plane is separate from
the durable-evidence stable-contract-or-expiry hold point.

The same role chain preserves append-only attempt identity. The worker writes a lightweight,
candidate-bound delivery record only at review handoff and keeps internal implementation/test/
evidence events separate; the reviewer writes an independent exact-attempt adjudication; the
manager records bounded invalidation and rebuilds an observational summary that excludes protocol
events. Unrelated later candidates do not reopen accepted attempts.

The curator's terminal artifact is valid only after current-additions coverage and the full
leaf-scoped memory-quality worklist have been repaired and rerun. Expected dirty-source drift and
real-commit verification fields remain separately closeout-owned; they do not excuse a repairable
onboarding or citation finding.

Roles are immutable within dashboard-owned seats. Horizontal role expansion uses structural
dispatch to another document+role seat; native sub-agents, when allowed by a hands-on role, remain
read/search helpers and never become AR role seats.

## Conventions

- A role file is complete enough to start from its brief without transcript history.
- The source role files are canonical; packaged copies are exact synchronization outputs.
- Each role writes its artifact of record and communicates structurally one rung at a time.
- Shared dispatch/authority doctrine remains in the parent `SKILL.md`.

## Invariants And Boundaries

- Manager owns a real master; worker/reviewer/curator own real leaves.
- Role replacement preserves the task-document/role address.
- Builder, reviewer, curator, and owner duties remain separate.
- Curator completion requires the required missing-onboarding and full-quality reruns to name no
  curator-actionable work.
- No role absorbs lifecycle machinery, memory duty, or gate authority assigned to another role.
- Terminal/finalizer truth and durable artifacts, not model completion posts, signal completion.
- No role may collapse per-requirement evidence into an aggregate completion claim.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Curator is a fresh conservative coherence seat with onboarding-only writes and a mandatory pre-closeout repair-and-rerun loop. | "# Lifecycle — Curator"; "### 4 — Iterate The Checklist, Then Report" | skills/l-01-agent-lifecycles/roles/curator.md:1-47; skills/l-01-agent-lifecycles/roles/curator.md:136-191 |
| Manager is one master-scoped owner of the builder/reviewer/curator closeout chain. | "# Lifecycle — Manager" | skills/l-01-agent-lifecycles/roles/manager.md:1-47 |
| Worker is one leaf-scoped builder whose terminal artifact is the turn report. | "# Lifecycle — Worker" | skills/l-01-agent-lifecycles/roles/worker.md:1-33 |
| The shared registry enumerates every remaining role file. | "## The Role Registry" | skills/l-01-agent-lifecycles/SKILL.md:95-111 |
| Worker and reviewer roles define the two independent halves of per-ID acceptance. | `### 4 — Per-Requirement Acceptance Envelope And Delivery Attempt`; `## Per-Requirement Independent Attempt Adjudication` | skills/l-01-agent-lifecycles/roles/worker.md:77-145; skills/l-01-agent-lifecycles/roles/reviewer.md:101-160 |

## L23 Role Recovery Semantics

Architect guidance treats a resumed thematic master behind super as a sync of
the same master, while manager guidance requires current master and leaf edges
before reading or delegating work. Both rely on plane-owned task identity and
never pass branch/commit/session ids between roles.

## L23 Pre-Curator Admission Boundary

The manager's last action before onboarding is a canonical-leaf `worktree_status` call whose full
code and external-memory `sourceLineage` projection must be `current`. That projection enters the
curator brief as evidence, and structural dispatch independently re-proves it before creating the
curator host. This boundary prevents stale onboarding; the later closeout/integration checks remain
separate because they guard ancestry movement during their own long quality phases.

## L23 Final Candidate Route Disposition

Manager, reviewer, curator, and orchestrator roles share one handoff: independent per-route review
is bound to the exact candidate, current lineage is proven before curator creation, and acceptance
uses targeted leaf or full master Dagger authority without model-carried operation ids.

## R39 Generic Role Boundary

Manager, orchestrator, and worker roles now obtain concrete acceptance from repository memory
instead of carrying Agents Remember-specific Dagger commands. They retain the one leaf-closeout,
no leaf-integration rerun, one master-integration cadence and must fail closed rather than invent a
runner or fallback.

## 260815-DAG-L14 Roles Route

`roles/orchestrator.md` replaces the seat-row prescription with the seats-structure +
`attach_master` adoption flow; `roles/strategist.md` and `roles/architect.md` adoption payloads
updated.

## 260815-DAG-L15 Roles Route

`roles/reviewer.md` gained the Review Independence and Evidence-Type Matching section (no self-review; requirement-evidence-type table: rendering → mounted-UI proof, scheduling → operation-level proof, data model → artifact-level proof, doctrine → code anchor); `roles/orchestrator.md` gained the review-independence paragraph. All 9 generated copy trees are byte-identical via `scripts/sync-skills.py`.

## 260821-DAGQC-L2 Curator Quality Invocation

No role authority changed. Curator doctrine now uses explicit sync/start/poll request objects and
treats capacity as poll/wait/retry guidance over the same API, never as permission for a fallback.

## Update History

- 2026-08-27T22:15+02:00 — Recorded worker, manager, and reviewer ownership of phase-sensitive
  malformed-attempt recovery without worker self-rejection.
- 2026-08-27T21:53+02:00 — M40@v2/M44@v2 role impact: separated internal protocol events from
  review-handoff attempts and made leaf records lightweight content-addressed views.
- 2026-08-27T19:59+02:00 — M40-M45 role impact: recorded worker/reviewer/manager attempt ownership
  and the accepted-attempt non-reopening boundary.
- 2026-08-27T12:43+02:00 — M38: recorded exact stable-ID dispatch, the worker acceptance envelope,
  independent per-ID reviewer adjudication, and separation from durable-evidence promotion.
  Verification metadata stays pinned until governed closeout stamps the PDLS commit.

- 2026-08-26T08:55+02:00 — Finalized the IAS role boundary label against the frozen pass-13
  candidate.

- 2026-08-24T14:19+02:00 — No route impact: aligned curator quality invocation and capacity guidance with the canonical controller. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: reviewer.md independence + evidence-type section; orchestrator.md independence paragraph. Verified at code commit de3a0fd9.


- 2026-08-20T05:06+02:00 — 260815-DAG-L14 route impact: orchestrator/strategist/architect role
  docs updated to the atomic attach flow and seats structure. Verified at code commit 8071a644.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: `architect.md` and `orchestrator.md` now
  name `task_doc.author_execution_graph` as the graph bootstrap/edit seam and teach the
  atomic-sequential default for graph-less sprints; the `migrate_execution_topology` reference is
  gone. Role lifecycles are unchanged. Verification remains closeout-owned.

- 2026-08-18T09:25+02:00 — No route impact: renamed the atomic 'barrier' concept to 'blocker' throughout; route purpose unchanged.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: reconciled initial-plan ownership, strategist and
  orchestrator judgment boundaries, organizational/atomic manager duties, pre-landing completion
  scope, and leaf-owned remediation. Verification remains closeout-owned.
- 2026-08-14T11:29+02:00 — R39 curator: reconciled the role route with repository-resolved
  acceptance doctrine. Verification remains closeout-owned.
- 2026-08-14T06:25+02:00 — L23 final candidate review: manager, reviewer, curator, and orchestrator
  roles preserve one candidate-bound route-review handoff, current-lineage admission, and Dagger-only
  acceptance without model-carried operation or commit ids. Verification remains closeout-owned.
- 2026-08-13T14:32+02:00 — L23 final roles-route review: synchronized Dagger-only acceptance,
  targeted/full altitude, mandatory explicit diff base, and diagnostic-only host execution.
  Verification remains closeout-owned.
- 2026-08-13T09:05+02:00 — L23 curator body review: clarified that the manager's immediately
  pre-curator `worktree_status.sourceLineage=current` proof is carried into the brief and repeated
  by dispatch before host creation, while closeout/integration independently close later races.
  Final provenance remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: recorded the manager-owned pre-curator current-lineage check and the structural dispatch recheck before curator host creation. Verification metadata remains closeout-owned.

- 2026-08-12T20:20+02:00 — L23 curator: documented architect/manager lineage recovery and dispatch boundaries; verification remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 route impact: manager,
  orchestrator, and worker quality-altitude doctrine now uses host-managed
  master memory by default and keeps leaf checks targeted. Verification
  metadata remains pinned until closeout stamps L24.

- 2026-08-11T14:40+02:00 — Made the curator's missing-onboarding and full-quality repair-and-rerun
  obligation part of the role route's current contract, with commit-derived stamps left to closeout.
- 2026-08-11T14:10+02:00 — Replaced task-delta sections with direct current role ownership,
  altitude, artifact, and separation contracts.
- 2026-08-10T07:30+02:00 — Durable reports became the cleanup precondition for short-lived seats.
- 2026-08-09T12:08+02:00 — Role-local watcher/ladder prose was superseded by fact relay.
- 2026-07-12T14:20+02:00 — Established the governing role-route overview.
