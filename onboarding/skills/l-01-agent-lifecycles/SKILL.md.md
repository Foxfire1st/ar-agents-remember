# skills/l-01-agent-lifecycles/SKILL.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/SKILL.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T12:57+02:00 |
| lastVerifiedCommitHash | `f9f92ca793811b6cb738d7e302dfecdf8636e96e`|
| lastVerifiedCommitDate | 2026-08-30T14:26:46+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

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
- One self-contained role file owns each role lifecycle; templates carry dispatch inputs, not
  alternate doctrine.
- Roles communicate through structural parent/child operations and durable artifacts.
- Exact runtime ids, readiness correlations, inbox ids, lifecycle ids, and gate ids remain
  control-plane details.

## Invariants And Boundaries

- Exactly one routing condition wins for a session.
- `(canonical task document, role)` is the stable seat address; replacement changes the occupant.
- Agents never poll readiness, retain another seat's runtime address, or duplicate an initial brief.
- `dispatch_agent` is the sole public spawn choice. Ambient launcher and plane-hosted authority are
  disjoint modes of that one transaction, with no caller-mode field or fallback.
- Role-table `dispatch` and `tools` rows describe structural authority/capability, not settings
  keys; only the documented launch knobs participate in settings overrides.
- Durable artifacts, delegated authority, and human-only gates retain their owning altitudes.
- The three-party loop separates builder work, independent review, curator coherence, and owner
  decision; verdicts are evidence rather than gate decisions.
- The durable-evidence stable-contract-or-expiry hold point remains separate from the per-ID
  acceptance envelope; neither can substitute for the other.
- Worker/reviewer attempt records are append-only and bind one exact candidate; summaries never
  substitute for them or invalidate accepted work.

## Docs References

No external domain source governs this repository-owned lifecycle doctrine.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The router is exactly three ordered conditions. | "## Which Lifecycle Am I? (the router — exactly three conditions, in order)" | skills/l-01-agent-lifecycles/SKILL.md:13-51 |
| The registry assigns one canonical file to each role. | "## The Role Registry" | skills/l-01-agent-lifecycles/SKILL.md:116-116 |
| The minimal frame binds roles to canonical task-document altitude and relays silence mechanically. | "## The Minimal Frame (the only machinery every session shares)" | skills/l-01-agent-lifecycles/SKILL.md:140-175 |
| Shared continuity and authority invariants are explicit. | "## Shared Invariants (every role can count on these)" | skills/l-01-agent-lifecycles/SKILL.md:198-198 |
| Dispatch has two process-derived caller kinds and one shared transaction. | "Caller kind comes only from process context"; "Every launcher or role that dispatches a hosted role calls" | skills/l-01-agent-lifecycles/SKILL.md:437-437; skills/l-01-agent-lifecycles/SKILL.md:444-444 |
| Ambient bootstrap compiles and pins one complete architect brief. | "# Template — Architect Brief"; "Compiler notes for the launcher" | skills/l-01-agent-lifecycles/templates/architect-brief.md:1-84 |
| Requirement acceptance is exact, per-ID, independently adjudicated, and separate from evidence promotion. | "Requirement acceptance is per stable ID and version, never aggregate." | skills/l-01-agent-lifecycles/SKILL.md:243-264 |
| Attempt lineage separates semantic versions from candidate-bound delivery history and gives regression invalidation to independent proof plus the owning seat. | "Requirement revisions and delivery attempts are separate axes." | skills/l-01-agent-lifecycles/SKILL.md:266-307 |
| Leaf journals are authority and the master summary is explicitly rebuildable and non-gating. | "The detailed per-leaf worker and reviewer records are authority." | skills/l-01-agent-lifecycles/SKILL.md:332-332 |

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

The quality altitude follows those two natures without duplication: each leaf receives one
change-set-scoped acceptance at closeout, and each completed organizational or atomic master
receives one full check against the exact candidate before its super ref moves.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

## Update History

- 2026-08-30T12:57+02:00 — 260821-ARSPAWN-L3 review correction: clarified that an explicit
  task-seat takeover converges idempotently on the canonical seat and never authorizes manual
  incumbent replacement or duplicate brief publication. Verification remains closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 recorded the one-call ambient launcher,
  separated ordinary architect bootstrap from explicit named-role takeover, made lineage-conflict
  continuation explicit, and kept structural authority outside settings overrides. Verification
  remains closeout-owned.

- 2026-08-28T14:18+02:00 — Reconciled lifecycle-router citations against the committed PDLS
  candidate after the final role-routing wording settled; behavior is unchanged.

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T21:53+02:00 — M40@v2/M44@v2: delivery attempts now advance only at review handoff or
  after rejection; internal protocol events remain separate, and lightweight records link frozen
  expanded evidence instead of duplicating the master corpus.
- 2026-08-27T19:59+02:00 — M42 clarification: distinguished pre-adjudication candidate replacement
  from unrelated post-acceptance candidate movement, which cannot silently reopen accepted work.
- 2026-08-27T18:06+02:00 — M40-M45: documented immutable worker/reviewer attempt lineage, exact
  candidate binding, the closed failure taxonomy, owner-recorded bounded regression invalidation,
  and leaf-authoritative/rebuildable non-gating summary semantics.
- 2026-08-27T14:04+02:00 — Clarified M39's revision authority: approved packets are immutable,
  version-addressed, and carry the durable corpus ruling consumed by every downstream seat.
- 2026-08-27T13:32+02:00 — M39@v1: recorded the upstream requirement-compilation gate and exact
  ID + version propagation into acceptance. Canonical packets and developer corpus approval now
  precede task topology. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: documented the mandatory per-requirement worker envelope,
  independent reviewer adjudication, exact stable-ID set, and separate durable-evidence hold
  point. Verification metadata stays pinned until governed closeout stamps the PDLS commit.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: documented fact-versus-judgment ownership,
  architect-owned plan review, organizational/atomic lineage, and the pre-landing full-master gate.
  Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented canonical source-lineage dispatch admission; verification remains closeout-owned.

- 2026-08-11T14:10+02:00 — Reconciled the sidecar directly to current structural lifecycle
  doctrine and removed duplicated task-delta/history blocks. Verification remains pinned pending
  governed closeout.
- 2026-08-09T12:08+02:00 — Fact-relay supervision replaced timed escalation-ladder doctrine.
- 2026-08-08T02:00+02:00 — Quality checks were assigned to leaf and master altitudes.
- 2026-07-12T14:20+02:00 — Established canonical lifecycle route coverage and generated-copy
  ownership.
