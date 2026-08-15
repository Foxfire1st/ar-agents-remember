# skills/l-01-agent-lifecycles/SKILL.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/SKILL.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T04:32+02:00 |
| lastVerifiedCommitHash | `20cfd54cb0a3d425424afdfbb6d8c97f669cdcc4` |
| lastVerifiedCommitDate | 2026-08-15T05:12:01+02:00|
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
brief loads the named role lifecycle; otherwise the session is the free-chat launcher. Role seats
bind to canonical task documents at the appropriate altitude plus role. A dispatching role supplies
the child document, role, and complete brief once; the control plane privately resolves/creates the
occupant, establishes readiness, and exact-pins only the initial brief.

Continuity lives in task documents and durable artifacts rather than transcripts or a particular
occupant. The agent-notifier relays mechanical facts; owners interpret them without seat-local
watchers or an escalation ladder. Role files own the detailed loops and authority limits.

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
- Durable artifacts, delegated authority, and human-only gates retain their owning altitudes.
- The three-party loop separates builder work, independent review, curator coherence, and owner
  decision; verdicts are evidence rather than gate decisions.

## Docs References

No external domain source governs this repository-owned lifecycle doctrine.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The router is exactly three ordered conditions. | "## Which Lifecycle Am I? (the router — exactly three conditions, in order)" | skills/l-01-agent-lifecycles/SKILL.md:13-51 |
| The registry assigns one canonical file to each role. | "## The Role Registry" | skills/l-01-agent-lifecycles/SKILL.md:95-111 |
| The minimal frame binds roles to canonical task-document altitude and relays silence mechanically. | "## The Minimal Frame (the only machinery every session shares)" | skills/l-01-agent-lifecycles/SKILL.md:140-175 |
| Shared continuity and authority invariants are explicit. | "## Shared Invariants (every role can count on these)" | skills/l-01-agent-lifecycles/SKILL.md:177-190 |
| Hosted role dispatch is one structural transaction. | "### Hosted role dispatch is one structural transaction" | skills/l-01-agent-lifecycles/SKILL.md:308-308 |

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

## Update History
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
