# skills/l-01-agent-lifecycles/SKILL.md

## Governing Overview

[overview](overview.md)

## Purpose

This canonical router reference describes how a native role capsule is selected from an explicit supported role and one applicable operation. Besides the role and operation files, the capsule's first message carries the every-role digest and the handover facts; no other core file is loaded. Canonical task/workspace facts travel in the separate AR handover; the composition manifest owns routing metadata.

## Logic

The native launcher supports eight roles: Architect, Investigator, Orchestrator, Manager, Worker, Reviewer, Curator and Bootstrap. Missing, unsupported, inapplicable or conflicting role/operation/task bindings are reported rather than inferred. Projects is an execution location, not a repository identity. A manually selected taskless Architect asks only for missing outcome or registered repository details. An Investigator accepts a scoped concern of any kind from its actual parent's first message and asks that parent for missing concern/report scope; without a parent it uses the developer's request and own chat. Investigator may be selected at Projects, on a sprint, on a master that no sprint commands, or on a sprint and master, never on a leaf. No synthetic repository, sprint, master, task or parent is created.

Paseo hosts the role agents, keeps their sessions and shows their chats. AR tools come from the launching build’s bound `agents-remember-task` server; native role agents start/reach one another with `role_start` and `role_message`, retaining actual returned identities. A reply in the same turn reaches a sender only when that sender waits on its own call; otherwise the answer goes with `role_message`. With a parent named in `host.parent` a developer question goes to that parent, and only a parentless or unreachable-parent agent asks in its own chat; dashboard-started roles need no parent. An Architect first delegates coordination to one Manager for one master, or to one Orchestrator on the sprint when two or more masters are worked on at the same time; direct coordination is the developer’s exception, who may also ask for an Orchestrator above a single master.

After reconnect or compaction, restore the same role, operation, canonical task, agent IDs and report from the durable handover and recorded approvals. Reconcile an uncertain start with the same request ID. A finished turn, review, curation, semantic acceptance and paired-Git publication remain separate owning facts. Inside an assignment the seat organises its own work with its harness, including sub-agents; it answers for their work and alone performs boundary acts. A sub-agent holds no AR seat, starts no role and cannot supply independent review of its seat's own work; Curator authoring still uses one writer.

The following requirement/attempt constraints remain related standing preservation context, owned by the applicable approved packet, role/review and task records. Their retention here does not make them core blocks delivered by this router.

Requirement acceptance is upstream and revision-exact: approved requirements live in immutable,
version-addressed canonical packets carrying their durable corpus ruling. Managers, workers, and
reviewers refuse an absent, unapproved, or mismatched packet instead of reconstructing intent from
task prose or accepting an aggregate completion claim.

Requirement acceptance is keyed by stable ID and version. The owner puts the leaf's one owned
primary revision in the builder brief, with dependency and preservation context listed separately.
The worker supplies one acceptance block for that revision, while the reviewer independently
inspects the cited artifacts and adjudicates that exact manifestation. Aggregate prose cannot close a requirement, and any rejection prevents an overall pass.

Semantic requirement versions, delivery attempts, and internal protocol events are separate.
Semantic versions change only through explicit developer approval. The worker advances an attempt
only when handing an exact candidate to independent review, or after reviewer rejection when
handing off a successor. Internal implementation/test/evidence reruns remain separate events with
candidate, command, result, failure cause, repair, and expected next proof.

Each worker attempt is an immutable lightweight requirement-specific record bound to the exact
candidate and a content-addressed expanded-evidence anchor; it does not duplicate the complete
master acceptance corpus or protocol log. The reviewer appends an independent record without
modifying it. Rejection creates a linked successor at the next review handoff. Accepted attempts
stay closed; a requirement change needs a new version, durable developer approval and invalidation
of affected acceptance.

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
  brief schema. The composition manifest registers the shared template; the router names that manifest as the routing metadata authority.
- Native starts and peer messages use bound role tools and durable handovers; a developer question goes to the parent when one exists, and only a parentless or unreachable-parent agent asks in the own chat.
- Preserve actual returned agent IDs and canonical task/workspace bindings. Never invent a parent, recipient or delivery outcome.

## Invariants And Boundaries

- One explicit supported role and applicable operation selects the native capsule; missing or conflicting bindings are reported.
- Apart from the every-role digest, no core file is loaded into the capsule; canonical task/workspace facts are separate handover data.
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

Current role duty remains targeted/scoped evidence with failed or unrun results visible, followed by the existing authorized paired Git transaction under its real contract. Requested independent review preserves the sealed finding set and counts rounds against the settings limit (`orchestration.loops.defaults.maxRounds`); a round beyond it needs Architect or developer approval, recorded by the Manager. The normal Curator authoring pass remains the standing full memory-quality/coherence exception; an explicitly report-only admission claims none of that normal pass complete. No finished turn or green check supplies semantic acceptance or Git publication.

## Evidence

### Docs References

No external domain source governs this repository-owned lifecycle doctrine.

No configured domain documentation was available.

### Repo-Internal References

- One explicit supported role and applicable operation select the role and operation files; the first message adds the every-role digest and the handover facts, and no other core file is loaded. [11]

- The native launcher names eight role IDs, including Bootstrap. [12]

- Canonical task/workspace facts arrive separately in the handover; task-bound selection uses its supplied canonical reference and paired workspace. Projects is an execution location. [13]

- Restore the same role, operation, task, agent and report through reconnect; reconcile an uncertain start with its same request ID and retain separate acceptance/publication authorities. [14]
- Native role starts and messages use the launching build's task server and actual returned identities. Developer questions follow the actual parent channel when a parent exists. [15]
- First delegation to a coordinating agent, developer-chosen direct coordination and parentless dashboard admission have their stated scopes. [16]

The following requirement and attempt references retain their source-epoch evidence. Applicable approved packets and owning role records determine current authority; this router loads no core file other than the every-role digest.

- Requirement acceptance binds one requirement revision, needs a complete acceptance block and is judged independently for that exact manifestation; an aggregate claim never closes one. [7]

- Leaf journals are authority and the master summary is explicitly rebuildable and non-gating. [9]

## Current intake and developer-question evidence

- Investigator takes a scoped concern from the actual parent's first message, or the developer without a parent; its selected scope creates no fake task identity. Developer decisions go to the actual parent when one is named. [17]



## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.

- Canonical role-capsule doctrine and the packaged byte-equal carrier have one authored owner; the package is a generated distribution extent. [18]

- `curator-handoff-list.md` is the producers' contract for the Curator hand-off: Workers and Reviewers send their own lists directly, and Managers and Orchestrators relay none. [19]

- Semantic requirement versions and exact-candidate formal attempts keep separate immutable lineage; internal reruns mint no attempt. Reviewer records bind the exact attempt and candidate. Accepted attempts stay closed, and observations outside the sealed findings list go through the parent to the developer without adding or reopening findings or resetting review. [8]
