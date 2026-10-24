# skills/l-01-agent-lifecycles/SKILL.md

## Governing Overview

[l-01-agent-lifecycles overview](overview.md)

## Purpose

This canonical thin router selects a native role capsule from an explicit supported role and one applicable operation. It does not define a shared lifecycle or inject shared core instructions. Canonical task/workspace facts travel in the separate AR handover; the composition manifest owns routing metadata.

## Logic

The native launcher supports eight roles: Architect, Investigator, Orchestrator, Manager, Worker, Reviewer, Curator and Bootstrap. System Specialist is the earlier read spelling of the same Investigator role. Missing, unsupported, inapplicable or conflicting role/operation/task bindings are reported rather than inferred. Projects is an execution location, not a repository identity. A manually selected taskless Architect asks only for missing outcome or registered repository details. An Investigator accepts a scoped concern of any kind from its actual parent's first message and asks that parent for missing concern/report scope; without a parent it uses the developer's request and own chat. Investigator may be selected at Projects, on a sprint, or on a sprint and master, never on a leaf. No synthetic repository, sprint, master, task or parent is created.

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

- `skills/l-01-agent-lifecycles/` is canonical. The packaged runtime skill tree is its generated distribution output.
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

## 260928-MIK-L172 — a reply reaches the sender only when it waits

The router now separates a reply from a hand-over. A message another agent sent begins with a `From` line; the agent's reply in that turn reaches the sender only when the sender waits on its own call, and otherwise the answer is sent with `role_message` on `agents-remember-task`. An agent that ends its turn with its stage unfinished sends what it awaits, and from whom, to its parent the same way; a final chat line may repeat it but is not the transport. The retired own-chat answer sentence is registered against return, and the role and operation texts carry the same rule.

## Evidence

### Docs References

No external domain source governs this repository-owned lifecycle doctrine.

No configured domain documentation was available.

### Repo-Internal References

- One explicit supported role and applicable operation select the two instruction blocks; the router injects no shared core. [11]
- The native launcher names eight roles, including Bootstrap; System Specialist remains the earlier Investigator spelling, and other manifest registry entries are not launched here. [12]
- Canonical task/workspace facts arrive separately in the handover; task-bound selection uses its supplied canonical reference and paired workspace. Projects is an execution location. [13]
- Restore the same role, operation, task, agent and report through reconnect; reconcile an uncertain start with its same request ID and retain separate acceptance/publication authorities. [14]
- Native role starts and messages use the launching build's task server and actual returned identities. Developer questions follow the actual parent channel when a parent exists. [15]
- First delegation to a coordinating agent, developer-chosen direct coordination and parentless dashboard admission have their stated scopes. [16]

The following requirement and attempt references retain their source-epoch evidence. Applicable approved packets and owning role records determine current authority; this thin router does not inject the former shared sources.

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

- Investigator takes a scoped concern from the actual parent's first message, or the developer without a parent; its selected scope creates no fake task identity. Developer decisions go to the actual parent when one is named. [17]

## Inherited Source-Epoch Commentary

The following distribution-copy account preserves useful explanations and source-epoch history, not a second current contract. Its currentness, tool, seat, provider, execution and permission claims are inherited scope unless separately qualified above against the current canonical source. Earlier incompatible claims on the explicitly updated seams are historical, not restored authority. Historical labels in this quotation do not allocate this card's reference numbers.

> # l-01-agent-lifecycles/SKILL.md
>
> ## Governing Overview
>
> [MCP package overview](../../../../../../overview.md)
>
> ## Purpose
>
> The packaged thin router selects the native AR role capsule; canonical `skills/l-01-agent-lifecycles/SKILL.md` owns this contract and `scripts/sync-skills.py` produces the copies.
>
> ## Current Contract
>
> A capsule contains the explicitly selected `roles/<role>.md` followed by one applicable operation. Canonical task and workspace bindings travel separately in the handover. Shared `core/` blocks are not injected.
>
> The native launcher supports Architect, Investigator, Orchestrator, Manager, Worker, Reviewer and Curator. System Specialist is the earlier read spelling of the same Investigator role. Missing, unsupported, inapplicable or conflicting role/operation/task bindings are reported rather than inferred. Projects is an execution location, not a repository identity. A manually selected taskless Architect asks only for missing outcome or registered repository details. An Investigator accepts a scoped concern of any kind from its actual parent's first message and asks that parent for missing concern/report scope; without a parent it uses the developer's request and own chat. Investigator may be selected at Projects, on a sprint, or on a sprint and master, never on a leaf. No synthetic repository, sprint, master, task or parent is created.
>
> Paseo runs the agents. AR tools come from the launching build’s `agents-remember-task` server; agent starts and peer messages use `role_start` and `role_message` with actual returned identities. With a parent named in host.parent, every question requiring the developer's decision goes to that actual parent through bound role_message. Continue independent work; if none remains, record the state and await the parent's message. Busy or permission-prompt delivery stays pending and is retried before ending; it does not permit own-chat escalation. Only a parentless agent, or an agent whose parent cannot be reached at all with the exact refusal recorded, asks the developer in its own chat. Dashboard starts need no parent. An Architect first delegates coordination to one Manager for one master, or one Orchestrator for concurrently worked masters; direct coordination is the developer’s choice. Prior approvals survive reconnects and compaction.
>
> ## Conventions
>
> Canonical skills/l-01-agent-lifecycles/SKILL.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.
>
> ## Invariants And Boundaries
>
> Restore the same role, operation, task, agent IDs and report from the durable handover. Reconcile an uncertain start with the same request ID. A finished turn, review, curation, semantic acceptance and paired Git publication require their separate owning evidence.
>
> ## Code Commentary
>
> ### Invariants And Boundaries
>
> - This artifact must remain byte-identical to the canonical lifecycle SKILL.
>
> - No role is defined by reference to another role's lifecycle, and no role file sends its reader to a
>   sibling's prose to learn its own obligations. A sanctioned sibling reference exists only for wearing
>   that hat or dispatching that seat, and `mcp/tests/test_role_instruction_corpus.py` fails on any
>   other one.
>
> - Installed runtimes receive the same doctrine as the canonical tree, not a compatibility variant.
>
> ### Todos
>
> None recorded.
>
> ## Evidence
>
> ### Repo-Internal References
>
> | Finding | Anchor | References |
> | --- | --- | --- |
> | Explicit role/operation composition and taskless Projects scope. | lines 8-16 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:8-16 |
> | Bound server, actual role identities, one coordinating agent under the Architect and recovery/acceptance distinction. | lines 20-35 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:20-35 |
>
> ### Docs References
>
> No external domain documentation is configured for this repository-local lifecycle doctrine.
>
> No relevant external documentation found.
>
> ### Repo-Internal References
>
> - Investigator takes any scoped concern from the actual parent, uses the developer request only without a parent, and never synthesizes task identity; developer decisions follow the parent channel with the stated parentless and unreachable exceptions. \(historical reference 2) (historical reference 2)
>
> - Canonical skills are propagated into package data and harness mirrors by the sync script. (historical reference 3)
> - The enabled corpus stays self-contained: the shipped check fails on a role that leaks a sibling's duties, on a manifest that names a missing source, and on any relative path the corpus cites that does not resolve. (historical reference 4)
>
> ### Cross-Repo References
>
> No sibling repository evidence is needed for this doctrine file.
>
> No meaningful cross-repo references found.
>
> ## Current Investigator contract impact
>
> The native launcher’s seven roles use canonical Investigator in place of the earlier role name. Projects is execution location rather than repository identity, and manual parentless concern intake invents no task. The selected canonical role/operation owns duties; generated copies author no second role or routing authority.
>
> - This source owns the stated current Investigator scope or canonical vocabulary. (historical reference 1)
>
>
> ## Current intake and developer-question evidence
>
> - Investigator takes any scoped concern from the actual parent, uses the developer request only without a parent, and never synthesizes task identity; developer decisions follow the parent channel with the stated parentless and unreachable exceptions. (historical reference 2) (historical reference 2)

Inherited reference 1 commentary (not a revalidated target):

> This source owns the stated current Investigator scope or canonical vocabulary.

Inherited reference 2 commentary (not a revalidated target):

> Investigator takes any scoped concern from the actual parent, uses the developer request only without a parent, and never synthesizes task identity; developer decisions follow the parent channel with the stated parentless and unreachable exceptions. (historical reference 2)

Inherited reference 3 commentary (not a revalidated target):

> Canonical skills are propagated into package data and harness mirrors by the sync script.

Inherited reference 4 commentary (not a revalidated target):

> The enabled corpus stays self-contained: the shipped check fails on a role that leaks a sibling's duties, on a manifest that names a missing source, and on any relative path the corpus cites that does not resolve.

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.

- Canonical role-capsule doctrine and the packaged byte-equal carrier have one authored owner; the package is a generated distribution extent. [18]
