# skills/l-01-agent-lifecycles/SKILL.md

## Governing Overview

[l-01-agent-lifecycles overview](overview.md)

## Purpose

This canonical thin router selects a native role capsule from an explicit supported role and one applicable operation. It does not define a shared lifecycle or inject shared core instructions. Canonical task/workspace facts travel in the separate AR handover; the composition manifest owns routing metadata.

## Logic

The native launcher supports Architect, Investigator, Orchestrator, Manager, Worker, Reviewer and Curator. System Specialist is the earlier read spelling of the same Investigator role. Missing, unsupported, inapplicable or conflicting role/operation/task bindings are reported rather than inferred. Projects is an execution location, not a repository identity. A manually selected taskless Architect asks only for missing outcome or registered repository details. An Investigator accepts a scoped concern of any kind from its actual parent's first message and asks that parent for missing concern/report scope; without a parent it uses the developer's request and own chat. Investigator may be selected at Projects, on a sprint, or on a sprint and master, never on a leaf. No synthetic repository, sprint, master, task or parent is created.

Paseo runs agents and delivers messages. AR tools come from the launching build’s bound `agents-remember-task` server; native role agents start/reach one another with `role_start` and `role_message`, retaining actual returned identities. With a parent named in `host.parent` a developer question goes to that parent, and only a parentless or unreachable-parent agent asks in its own chat; dashboard-started roles need no parent. An Architect first delegates coordination to one Manager for one master, or to one Orchestrator on the sprint when two or more masters are worked on at the same time; direct coordination is the developer’s exception, who may also ask for an Orchestrator above a single master.

After reconnect or compaction, restore the same role, operation, canonical task, agent IDs and report from the durable handover and recorded approvals. Reconcile an uncertain start with the same request ID. A finished turn, review, curation, semantic acceptance and paired-Git publication remain separate owning facts.

The following requirement/attempt constraints remain related standing preservation context, owned by the applicable approved packet, role/review and task records. Their retention here does not make them shared core blocks injected by this thin router.

Requirement acceptance is upstream and revision-exact: approved requirements live in immutable,
version-addressed canonical packets carrying their durable corpus ruling. Managers, workers, and
reviewers refuse an absent, unapproved, or mismatched packet instead of reconstructing intent from
task prose or accepting an aggregate completion claim.

Requirement acceptance is an exact-set contract keyed by stable IDs. The owner gives the same
applicable set to worker and reviewer. The worker supplies one delivery/verification evidence
envelope per ID, while the reviewer independently inspects the cited artifacts and adjudicates
each ID. Aggregate prose cannot close a requirement, and any rejection prevents an overall pass.

Semantic requirement versions, delivery attempts, and internal protocol events are separate.
Semantic versions change only through explicit developer approval. The worker advances an attempt
only when handing an exact candidate to independent review, or after reviewer rejection when
handing off a successor. Internal implementation/test/evidence reruns remain separate events with
candidate, command, result, failure cause, repair, and expected next proof.

Each worker attempt is an immutable lightweight requirement-specific record bound to the exact
candidate and a content-addressed expanded-evidence anchor; it does not duplicate the complete
master acceptance corpus or protocol log. The reviewer appends an independent record without
modifying it. Rejection creates a linked successor at the next review handoff. Accepted attempts
reopen only after independent regression proof plus owner-recorded bounded invalidation, or after a
developer-approved semantic revision.

Detailed leaf records are authority. The master summary is rebuilt from them and exposes attempts,
rejections, current state, and dominant open failure class only for observation; it cannot gate or
lock task authoring, lifecycle, closeout, integration, or queue operations, and it never counts the
separate protocol events as delivery attempts.

## Conventions

- `skills/l-01-agent-lifecycles/` is canonical. Package and harness trees are synchronized outputs.
- One self-contained role file owns each role lifecycle; templates carry dispatch inputs and
  hand-off shapes, not alternate doctrine.
- `templates/curator-handoff-list.md` is the one **producer output shape** among them: the
  requirement-shaped items the builder and the reviewer hand directly to the curator, one
  entry per item with its statement, kind, place, evidence and disposition. Producers emit it as
  data; the curator fills the curator-side fields. It is a hand-off artifact rather than a
  brief-schema, which is why the router names it on its own.
- Native starts and peer messages use bound role tools and durable handovers; a developer question goes to the parent when one exists, and only a parentless or unreachable-parent agent asks in the own chat.
- Preserve actual returned agent IDs and canonical task/workspace bindings. Never invent a parent, recipient or delivery outcome.

## Invariants And Boundaries

- One explicit supported role and applicable operation selects the native capsule; missing or conflicting bindings are reported.
- Shared core blocks are not injected; canonical task/workspace facts are separate handover data.
- A first delegation to one coordinating agent is the default; direct coordination is the developer’s choice, and dashboard starts need no parent.
- Native role starts/messages use the launching build’s task server and actual resolved identities.
- Preserve the same task/role/request/report through uncertainty; no duplicate owner or alternate transport is created.

- Durable artifacts, delegated authority, and human-only gates retain their owning altitudes.
- The three-party loop separates builder work, independent review, curator coherence, and owner
  decision; verdicts are evidence rather than gate decisions.
- The durable-evidence stable-contract-or-expiry hold point remains separate from the per-ID
  acceptance envelope; neither can substitute for the other.
- Worker/reviewer attempt records are append-only and bind one exact candidate; summaries never
  substitute for them or invalidate accepted work.


## CCR-R12@v5 Transaction Boundary

Current role duty remains targeted/scoped evidence with failed or unrun results visible, followed by the existing authorized paired Git transaction under its real contract. Requested independent review preserves the sealed monotonic finding set and three-round rule. The normal Curator authoring pass remains the standing full memory-quality/coherence exception; an explicitly report-only admission claims none of that normal pass complete. No finished turn or green check supplies semantic acceptance or Git publication.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The router now states the all-role harness freedom and its bounds: every role organises its assigned work with whatever its harness offers, at any size, while the seat answers for it, boundary acts stay the seat's own, a harness sub-agent is no AR seat, and nobody checks itself through one. The old fixed read/search/one-level fan-out restriction is gone; the router keeps the message and identity rules it already stated.

## 260928-MIK-L93 — a question for the developer goes up the chain

The router now states the parent rule: with a parent named in `host.parent`, every question requiring the developer's decision goes to that parent with `role_message` on `agents-remember-task`, with what is held back and what is recommended; the agent keeps working, and when nothing independent remains it records its state and ends waiting for its parent's message. A refused delivery stays pending under **Pending developer questions** and is retried before the turn ends; only a parentless or unreachable-parent agent asks in its own chat. A relayed answer is the developer's only with the quoted words and the receiving agent's id. The retired universal own-chat sentence is registered so it cannot return unnoticed.

## Evidence

### Docs References

No external domain source governs this repository-owned lifecycle doctrine.

No configured domain documentation was available.

### Repo-Internal References

- Explicit supported role and applicable operation select the native capsule. [1]
- The native launcher exposes seven roles while the manifest retains its compiler registry. [2]
- Canonical task/workspace facts arrive in the handover rather than being inferred from Projects. [3]
- Same-task continuity restores durable role, operation, agent and report identities. [4]
- Native role starts and messages use the bound task server and actual returned identities. [5]

- Developer-chosen direct coordination and valid parentless dashboard admission are explicit. [6]

- Requirement acceptance is exact, per-ID, independently adjudicated, and separate from evidence promotion. [7]
- Attempt lineage separates semantic versions from candidate-bound delivery history and gives regression invalidation to independent proof plus the owning seat. [8]
- Leaf journals are authority and the master summary is explicitly rebuildable and non-gating. [9]
- The producers' Curator hand-off shape remains a separate template contract, rather than an injected router rule. [10]

## Historical L23 Dispatch Admission

Canonical lifecycle dispatch now proves the task-derived ancestry applicable to
the target role before process creation. Stale or unavailable edges create no
child and carry ordered contract-addressed synchronization; agents do not retain
commit ids, branch ids, or occupant ids to make routing work.

## Historical 260815-DAG-L2 Dependency-Aware Execution Plane

The shared lifecycle doctrine now separates tool-derived execution facts from role-owned
judgment. Portfolio planning is an architect-owned loop: an approved strategist drafts the plan,
or the orchestrator builds it only after a sanctioned strategist skip; the architect rules it and
the orchestrator adopts it. Organizational masters are logical ownership groups whose leaves use
the direct super edge, while atomic masters retain the isolated super → master → leaf edge.

The lifecycle records worker targeted checks and curator scoped onboarding checks before handoff.
Closeout and integration then publish the authorized code, memory-content, and ledger Git
transaction; full code quality, full tests, full memory quality, certification, and review are
explicit developer-requested operations rather than automatic altitude gates. Transaction-owned
commit legs suppress automatic quality and test hooks; ordinary explicit Git hook policy outside
the transaction remains unchanged.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.


## Current intake and developer-question evidence

- Investigator takes any scoped concern from the actual parent, uses the developer request only without a parent, and never synthesizes task identity; developer decisions follow the parent channel with the stated parentless and unreachable exceptions. \[11] [11]
