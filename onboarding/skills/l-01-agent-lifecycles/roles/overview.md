# skills/l-01-agent-lifecycles/roles

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `skills/l-01-agent-lifecycles/roles` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash | `0dd1df9a950d59ac9622e5fb54250e528df08fa5`|
| lastVerifiedCommitDate | 2026-09-16T20:47:18+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |

## Purpose

This route owns the self-contained lifecycle for each role. Every file states what one seat is,
which task-document altitude it occupies, the loop and artifacts it owns, its communication path,
and the work it must refuse or escalate.

260915-CAPS-L1 rewrote all nine files here into one readable order — purpose and authority → required
inputs → normal workflow → permitted writes and actions → stop and escalation cases → completion and
handoff, then the machine-readable knob block — and each now declares the shared sources it composes
with in an `**Inherits:**` line instead of restating them, because the shared rules moved into a new
sibling `core/` and the procedures into `operations/`. A role file may name a sibling role file only to
wear that hat or dispatch that seat (architect → designer; orchestrator → strategist, designer;
strategist → manager; reviewer → manager); the shipped corpus check fails on any other reference. The
route's files are 2,792 → 2,322 lines in total, and the router that selects between them is no longer a
doctrine source.

## Hot Path Summary

Manager, orchestrator and curator handoffs name actual code/memory output refs and scoped onboarding evidence. They never require a ledger commit, cache freshness proof or cache-repair transaction; downstream consumers can rebuild the ledger from committed attribution.

## Detailed Route Context

Manager hosted dispatch consistently names the canonical leaf or master **task document**. That
vocabulary matches the public structural request and its task-reference authority; generated and
packaged role projections are synchronized from the canonical role file rather than edited apart.

### IAS Frozen Role Boundary

Architect, strategist, and orchestrator responsibilities operate on canonical task documents, not
on a queue-owned copy of the plan. They may change approved planning whenever their role authority
allows; downstream closeout projections are invalidated and rebuilt. For atomic work, implementation
admission is contract-scoped: each canonical series contract owns its own activation record, so
selecting a master publishes `reconciling` for that contract only — which suspends nothing and
excludes no other master — and it becomes `active` only when its own two protected source tips are
current. Nothing serializes a graph-less sprint: a sprint without an `executionGraph` declares no
dependencies, so the shipped `atomic-sequential` default describes sprint SHAPE (every commanded
master executes atomically) rather than a serialization mechanism, and no master is held because
another is selected. No role should discard or terminalize a valid master merely to free scheduling
state.

When source reconciliation retains a conflict, the assigned agent resolves and stages it in the
reported worktree, then continues the same contract-addressed operation or explicitly cancels it.
Private journal/ref identity stays in the plane; role briefs carry the public contract address and
recovery guidance.

Architect owns sprint-level direction, the initial plan loop, and the sprint plan-review reviewer.
Strategist authors the evidence-cited dependency graph when dispatched. Orchestrator adopts the
ruled artifact, maintains the runtime frontier, and records bounded reprioritization judgments;
substantial reshapes return through the architect-owned strategist loop. Manager owns readiness
inside one organizational or atomic master. Worker owns one leaf; reviewer owns independent route
or completion verdict evidence; and curator reconciles ruled intent with implementation.

Reviewer is one target-only role projected at the reviewed artifact's altitude: leaf, master, or
sprint. Managers own leaf and master-exit generations, the architect owns the plan generation, and
the orchestrator owns the super-exit generation. The control plane stamps that structural parent;
the shared role name and sprint address do not blur plan and super authority.

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

The curator's terminal structured authority is valid only after current-additions coverage and the
full leaf-scoped memory-quality worklist have been repaired and rerun. The lifecycle API publishes
that sole candidate-bound authority and renders Markdown from it. Expected dirty-source drift and
real-commit verification fields remain separately closeout-owned; they do not excuse a repairable
onboarding or citation finding.

Roles are immutable within dashboard-owned seats. For ordinary role-shaped work, free chat creates
the sprint architect through one identity-free `dispatch_agent` call built from the canonical
architect-brief template; an explicit developer-declared task-seat takeover instead targets the
named role at its canonical altitude. Once hosted, architect, orchestrator, and manager are plane
callers with only their documented direct-child scope. Strategist, designer, worker, reviewer,
curator, and system-specialist are target-only roles. The role-table dispatch/tool rows document
fixed structural authority and capability, not settings keys. Plane authorization
failures never retry as ambient launches. Native sub-agents, when allowed by a hands-on role,
remain read/search helpers and never become AR role seats.

## Conventions

- A role file is complete enough to start from its brief without transcript history.
- The source role files are canonical; packaged copies are exact synchronization outputs.
- Each role writes its artifact of record and communicates structurally one rung at a time.
- Shared dispatch/authority doctrine remains in the parent `SKILL.md`.
- Every role table names whether that role is an ambient target, a plane-hosted caller, or
  target-only; the request never carries a caller-mode selector.

## Invariants And Boundaries

- Manager owns a real master; worker/reviewer/curator own real leaves.
- Role replacement preserves the task-document/role address.
- `dispatch_agent` is the only public spawn verb. Ambient and plane authority are disjoint even
  though both use the same exact-brief transaction.
- Builder, reviewer, curator, and owner duties remain separate.
- Curator completion requires the required missing-onboarding and full-quality reruns to name no
  curator-actionable work.
- No role absorbs lifecycle machinery, memory duty, or gate authority assigned to another role.
- Terminal/finalizer truth and durable artifacts, not model completion posts, signal completion.
- No role may collapse per-requirement evidence into an aggregate completion claim.


## CCR-R12@v5 Lifecycle Boundary

Workers provide targeted checks and curators provide scoped onboarding checks with honest failed or not-run states. The prepared code and memory-content outputs move through the authorized Git transaction, whose commit legs suppress automatic quality and test hooks. The consumer ledger is refreshed without a commit while ordinary explicit Git hook policy outside the transaction remains unchanged; full quality, full tests, full memory quality, certification, and review require an explicit developer request. Requested reviews retain the sealed monotonic three-round rule.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Curator is a fresh conservative coherence seat with onboarding-only writes, a mandatory repair loop, and structured authority publication. | "# Lifecycle — Curator"; "### 4 — Repair Affected Onboarding, Then Publish" | skills/l-01-agent-lifecycles/roles/curator.md:1-6; skills/l-01-agent-lifecycles/roles/curator.md:153-195 |
| Manager is one master-scoped owner of the builder/reviewer/curator closeout chain. | "# Lifecycle — Manager" | skills/l-01-agent-lifecycles/roles/manager.md:1-47 |
| Worker is one leaf-scoped builder whose terminal artifact is the turn report. | "# Lifecycle — Worker" | skills/l-01-agent-lifecycles/roles/worker.md:1-33 |
| The shared registry enumerates every remaining role file. | "## The Role Registry" | skills/l-01-agent-lifecycles/SKILL.md:119-119 |
| Worker and reviewer roles define the two independent halves of per-ID acceptance. | `### 4 — Per-Requirement Acceptance Envelope And Delivery Attempt`; `## Per-Requirement Independent Attempt Adjudication` | skills/l-01-agent-lifecycles/roles/worker.md:77-145; skills/l-01-agent-lifecycles/roles/reviewer.md:101-160 |
| The graph-less atomic-sequential default describes sprint shape; nothing serializes the masters. | "nothing serializes the masters"; "nothing serializes its masters" | skills/l-01-agent-lifecycles/roles/architect.md:143-143; skills/l-01-agent-lifecycles/roles/orchestrator.md:265-265 |

Current working-candidate evidence for this route:

| Finding | Citations | Source Path |
| --- | --- | --- |
| Lifecycle publication and recovery carry the actual code/memory outputs. | L66-L72 | [mcp/src/agents_remember/models/lifecycles/operation.py](mcp/src/agents_remember/models/lifecycles/operation.py) |

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

## CCR-L42 Review-Phase And Altitude Update

The role files now distinguish a complete `reviewMode=baseline` from
`reviewMode=fix-verification`: the first review seals the agreed scope and issue IDs, while a
successor verifies only those outstanding IDs and cannot add routes, criteria, or new findings.
The role chain also records that standalone and organizational leaves carry independent route
review, atomic child leaves defer to the accumulated master integration review, and workers must
document applicable targeted checks before handoff. Task-document authority and the three-round
review limit remain in force.

## Ungoverned Mirror Status (known defect)

**260915-CAPS-L1 decision, recorded rather than implied.** This leaf rewrote all nine canonical role
files, so a contract-scoped quality pass reports this route's cards as unmodified bodies against changed
sources. The curator updated **this overview**, because route meaning genuinely changed. It deliberately
did **not** refresh the per-role cards under `onboarding/skills/l-01-agent-lifecycles/roles/**`: they sit
outside `pathRules.include`, they are already declared knowingly stale below, and a partial hand-refresh
would leave them mutually inconsistent while duplicating the governed cards on the tracked generated copy
under `onboarding/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/**`.
The govern-or-remove decision this section already asks for also determines whether those cards should be
refreshed or deleted. No fingerprint or verification stamp was advanced.

This route overview lives in the `onboarding/skills/**` tree, which mirrors the code repository's
`skills/**` route. `skills/**` is absent from `settings.json`'s `pathRules.include`, so this whole
onboarding tree sits outside normal onboarding census coverage: it is legacy and ungoverned. It is
retained here only because the contract-scoped memory-quality checker still validates these documents
whenever `skills/**` is part of a leaf's changed set, which is exactly why this overview was updated
by hand rather than by a governed maintenance pass. The remaining sibling sidecars under
`onboarding/skills/**` — the other role, criteria, and template cards — are knowingly stale and are
deliberately left untouched pending a follow-up decision on whether this mirror should be governed or
removed. That mismatch between the declared path rules and the enforced checking scope is itself the
recorded defect.

## Update History

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **route body updated** for the corpus consolidation. Purpose now names the route's actual shape (nine files in one readable order with `**Inherits:**` lines, a new sibling `core/`, procedures moved to `operations/`, sanctioned sibling references only, 2,792 → 2,322 lines), and the Ungoverned Mirror Status section records this pass's explicit decision to update the route overview while deliberately leaving the per-role cards under `onboarding/skills/l-01-agent-lifecycles/roles/**` unrefreshed (outside `pathRules.include`, already declared stale, and a partial refresh would duplicate the governed `mcp/**` cards without resolving the govern-or-remove question). No verification stamp or fingerprint was advanced.


- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Aligned role/template handoff doctrine with two outputs and non-authoritative cache status. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-13T15:01:46+02:00 — Gate-required ungoverned-mirror curation: rewrote the frozen role
  boundary to the shipped per-contract activation (selecting a master publishes `reconciling` for
  that contract only, which suspends nothing and excludes no other master; `active` requires its own
  two protected source tips) and added the explicit developer ruling that nothing serializes a
  graph-less sprint, with `atomic-sequential` describing sprint SHAPE rather than a serialization
  mechanism. Added the graph-less ruling citation row against
  roles/architect.md:143-143 and roles/orchestrator.md:265-265, both `grep -n`-verified. Re-checked
  the remaining role rows against the frozen role files and they still hold (curator.md:1-6/153-195,
  manager.md:1-47, worker.md:1-33, SKILL.md:119-119, worker.md:77-145, reviewer.md:101-160). Added the
  Ungoverned Mirror Status defect statement. Verification metadata remains closeout-owned.
- 2026-09-10T09:58+02:00 — CCR-R12@v5 transaction-only curation against code commit `4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0`: re-read the curator reference row against the rewritten `skills/l-01-agent-lifecycles/roles/curator.md` — section 4 is now `### 4 — Repair Affected Onboarding, Then Publish`, so the row carries the current heading and its 153-195 extent. Verification metadata remains closeout-owned.

- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-10T00:46+02:00 — CCR-L42 route reconciliation: recorded the current review-phase,
  review-altitude, and worker-check obligations from the canonical role files. Source inspection
  only; verification metadata remains closeout-owned.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: added the four reviewer
  contexts and plane-stamped parent ownership to the role map. Verification remains closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 recorded the complete role caller-context matrix,
  separated one-call architect bootstrap from explicit ambient takeover, corrected manager-only
  leaf-seat dispatch, and kept structural rows outside settings overrides. Verification remains
  closeout-owned.

- 2026-08-29T09:14+02:00 — MCAR-L02 made lifecycle-published structured coherence authority,
  rather than hand-authored Markdown, the curator's terminal artifact. Verification remains
  closeout-owned.

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
