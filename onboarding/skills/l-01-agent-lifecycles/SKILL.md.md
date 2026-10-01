# skills/l-01-agent-lifecycles/SKILL.md

## Governing Overview

[l-01-agent-lifecycles overview](overview.md)

## Purpose

This is the canonical lifecycle router and shared doctrine for every agent role. It selects exactly
one session path, defines the minimal frame every session may rely on, registers role-owned
lifecycle files, and owns the common structural dispatch, authority, continuity, supervision, and
three-party-loop contracts.

## Logic

The router has three ordered conditions: a bound spawn role loads that role lifecycle; a fresh role
brief loads the named role lifecycle; otherwise the session is the free-chat launcher. For
ordinary role-shaped work, that launcher compiles `templates/architect-brief.md` and calls
`dispatch_agent` once on the canonical sprint document. An explicit developer-declared task-seat
takeover instead dispatches the named role on that role's canonical task document. Role seats bind to canonical task documents at the
appropriate altitude plus role. A plane-hosted dispatching role supplies the child document, role,
and complete brief through the same public request. Caller kind is derived only from the presence
or absence of plane identity; ambient target-document authority never substitutes for a failed
plane authorization. The control plane privately resolves/creates the occupant, establishes
readiness, and exact-pins only the initial brief. A stale/unavailable source-lineage refusal routes
through ordered contract-addressed sync; retained conflicts remain resumable through the advertised
continuation, with escalation reserved for semantic ambiguity. Repeating the same dispatch after
that recovery converges on the existing viable occupant or durable queued brief; a developer
takeover never means manually replacing a live incumbent.

Malformed hosted identity never falls into ambient/free-chat behavior: an unknown
`AR_SPAWN_ROLE`, or a role environment without its plane-injected hosted-session identity, fails
closed before any pasted brief is interpreted. Reviewer uses one role across leaf, master, and
sprint documents; the dispatching manager, architect, or orchestrator stamps the exact structural
parent on each generation so plan and super reviewers can share an address without sharing
authority.

Continuity lives in task documents and durable artifacts rather than transcripts or a particular
occupant. The agent-notifier relays mechanical facts; owners interpret them without seat-local
watchers or an escalation ladder. Role files own the detailed loops and authority limits.

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
  requirement-shaped items the builder, the reviewer, and the orchestrator hand to the curator, one
  entry per item with its statement, kind, place, evidence and disposition. Producers emit it as
  data; the curator fills the curator-side fields. It is a hand-off artifact rather than a
  brief-schema, which is why the router names it on its own.
- Roles communicate through structural parent/child operations and durable artifacts.
- Exact runtime ids, readiness correlations, inbox ids, lifecycle ids, and gate ids remain
  control-plane details.

## Invariants And Boundaries

- Exactly one routing condition wins for a session.
- `(canonical task document, role)` is the stable seat address; replacement changes the occupant.
- Agents never poll readiness, retain another seat's runtime address, or duplicate an initial brief.
- `dispatch_agent` is the sole public spawn choice. Ambient launcher and plane-hosted authority are
  disjoint modes of that one transaction, with no caller-mode field or fallback.
- Invalid role environment is a refusal, never a fourth routing entry or free-chat fallback.
- Reviewer parentage is task-altitude- and generation-specific; runtime occupant ids are not parent
  authority.
- Role-table `dispatch` and `tools` rows describe structural authority/capability, not settings
  keys; only the documented launch knobs participate in settings overrides.
- Durable artifacts, delegated authority, and human-only gates retain their owning altitudes.
- The three-party loop separates builder work, independent review, curator coherence, and owner
  decision; verdicts are evidence rather than gate decisions.
- The durable-evidence stable-contract-or-expiry hold point remains separate from the per-ID
  acceptance envelope; neither can substitute for the other.
- Worker/reviewer attempt records are append-only and bind one exact candidate; summaries never
  substitute for them or invalidate accepted work.


## CCR-R12@v5 Transaction Boundary

Current lifecycle contract: workers run relevant targeted checks after changes and fixes and before handoff; curators update affected onboarding and run scoped checks with honest failed or not-run status. Closeout and integration then perform the authorized Git transaction, whose commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside the transaction remains unchanged. Full code quality, full tests, full memory quality, certification, and independent review run only after an explicit developer request. When review is requested, its sealed three-round monotonic finding-set rule remains in force.

## Evidence

### Docs References

No external domain source governs this repository-owned lifecycle doctrine.

No configured domain documentation was available.

### Repo-Internal References

- The router is exactly three ordered conditions. [1]
- The registry assigns one canonical file to each role. [2]
- The minimal frame binds roles to canonical task-document altitude and relays silence mechanically. [3]
- Shared continuity and authority invariants are explicit. [4]
- Dispatch has two process-derived caller kinds and one shared transaction. [5]
- Ambient bootstrap compiles and pins one complete architect brief. [6]
- Requirement acceptance is exact, per-ID, independently adjudicated, and separate from evidence promotion. [7]
- Attempt lineage separates semantic versions from candidate-bound delivery history and gives regression invalidation to independent proof plus the owning seat. [8]
- Leaf journals are authority and the master summary is explicitly rebuildable and non-gating. [9]
- The companion files now include the producers' curator hand-off shape beside the brief schemas. [10]

## L23 Dispatch Admission

Canonical lifecycle dispatch now proves the task-derived ancestry applicable to
the target role before process creation. Stale or unavailable edges create no
child and carry ordered contract-addressed synchronization; agents do not retain
commit ids, branch ids, or occupant ids to make routing work.

## 260815-DAG-L2 Dependency-Aware Execution Plane

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
