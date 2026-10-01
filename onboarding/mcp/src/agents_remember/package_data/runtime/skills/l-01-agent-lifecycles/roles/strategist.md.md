# l-01-agent-lifecycles/roles/strategist.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the optional sprint-bound strategist lifecycle. The canonical
`skills/l-01-agent-lifecycles/roles/strategist.md` owns doctrine; the sync process publishes this
exact runtime artifact.

The packaged role is now a **self-contained lifecycle in the corpus's readable order** — purpose and
authority → required inputs → normal workflow → permitted writes and actions → stop and escalation
cases → completion and handoff, then its machine-readable knob block. It declares its shared sources
with `**Inherits:**` rather than restating them (`core/authority.md`, `core/invariants.md`,
`core/loop.md`, `core/acceptance.md`, `operations/orientation.md`, `operations/planning.md`); the
planning method, the requirement-compilation precedence, and the loop's review-round rules now live
once in `operations/planning.md` and `core/loop.md`.

Its boundary is unchanged and re-stated structurally: **reader, not mutator** — the strategist reads
the whole in-flight portfolio, proves it coherent, resolves dependency chains, establishes blast
radius and priority, chooses the topology explicitly, and delivers the orchestration-task draft. It
never edits task docs, raises gates, mutates Git, or addresses an orchestrator occupant. This role
file names `roles/manager.md` only to name the seat it hands to, which is its one sanctioned sibling
reference.

## Code Commentary

### Logic

The synchronized caller matrix makes strategist target-only: the architect is its ordinary
plane-hosted caller, while an identity-free launcher may target it only for explicit
developer-declared takeover. Dispatch/tools rows remain structural documentation, not settings
keys.

After developer approval, the architect may dispatch `(sprint document, strategist)` when the
reasoned topology choice or portfolio classification is absent/stale—not merely because a valid
graph-less sprint has no persisted graph. The strategist is read-only: it analyzes portfolio
dependencies, derives one effective priority per candidate, chooses either an evidence-backed
explicit graph or the graph-less atomic-sequential default, and drafts the
orchestration task.
`message_parent` carries clarification or quo-vadis escalation to the architect, the architect rules
the plan, and the orchestrator adopts it. The role never edits task docs, raises gates, mutates Git,
or addresses an orchestrator occupant.

The developer ruling governs that default: nothing serializes a graph-less sprint, because a sprint
with no `executionGraph` declares no dependencies to honour — `atomic-sequential` describes the
sprint's shape (every commanded master executes atomically), not a serialization mechanism, so
independent atomic masters proceed concurrently, no master is held because another is selected, and
no work is retired. Per-contract activation records each canonical contract's own
`reconciling -> active` transition, so masters that share one protected source pair never share that
state and one master's selection never pauses or excludes another; the closeout queue only projects
each contract's own active/reconciling/vacant waiting candidates. Only an explicit graph's
`predecessor-incomplete:` waves gate anything.

### Conventions

Use cited evidence for dependency and coherence claims, preserve the draft/adoption boundary, and
edit only the canonical role before synchronization.

### Invariants And Boundaries

- The strategist remains a sprint-bound reader, not a mutator or orchestrator child.
- Durable artifacts, not runtime identity, carry the result across occupant replacement.
- Planning, classification, priority, dependency, and coherence judgments are mandatory; a
  persisted `executionGraph` is optional.
- This packaged artifact must remain byte-identical to the canonical role.

### Todos

None recorded.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; curation is the exception — the curator always runs the complete memory-quality operation, and closeout and integration carry its completed result as a prerequisite rather than rerunning it. Requested reviews retain the sealed finding list and monotonic three-round limit.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

When approved, the strategist is spawned by the architect and hands its plan back for ruling and
adoption.

- Canonical source this bundle copy is sync-propagated from. [1]
- The role declares the readable order — Inputs, Process, Outputs — with no inherited-sources line and no operator-knob block. [2]
- The reader-not-mutator boundary the role must preserve. [3]
- The strategist names `roles/manager.md` only to name the seat it hands to, which is its one sanctioned sibling reference. [4]
- The router's role registry still names the strategist row, and the loop doctrine now has its single home in `core/`. [5]
- The orchestrator that adopts the ruled topology or authors the same complete orchestration task after a sanctioned strategist skip. [6]
- The deliverable's template separates mandatory planning from optional persisted graph structure and defines complete graph bootstrap. [7]
- The plan-review criteria re-derive effective priority and validate either topology choice. [8]

### Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

No meaningful cross-repo references found.

## 260815-DAG-L14 Doctrine Sync

The strategist adoption payload is updated to the atomic `attach_master` flow and the first-class
sprint seats structure.

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.

## 260815-DAG-L2 Evidence-Cited Topology Planning

Initial facts are architect-compiled; runtime-reshape facts arrive from the orchestrator through
the architect. The strategist classifies organizational versus atomic execution, builds the exact
topology choice, and records dependency meaning, blast radius, priority, blockers,
reprioritization, and leaf moves in one canonical Judgment Register. When an explicit
activity-on-node graph is justified, every selected relation cites evidence and its owning judgment
id; otherwise the artifact records the reasoned graph-less atomic-sequential default. In that
default canonical commanded-master order is the stable equal-priority tie-break and nothing
serializes the masters — a graph-less sprint declares no dependencies, so independent masters
proceed concurrently, no master is held because another is selected, and no work is retired — and no
full-integration edge may be fabricated from the activation boundary. Large size alone
never makes a master atomic.

## IAS Graph-Less Activation Choice

The synchronized strategist role keeps dependency planning separate from runtime selection.
Per-contract activation records each canonical contract's own `reconciling -> active` transition and
serializes nothing across masters: masters that share one protected source pair hold independent
records, so one master's selection never pauses, replaces, or excludes another, and the only
activation waiting reason is `atomic-series-reconciling` for that contract's own in-flight
reconciliation. The corrected shipped text says the same at its own `:133-136` — "canonical
commanded-master order is the stable tie-break and nothing serializes the masters". Queue or
selector state cannot veto task authoring or substitute for an evidence-backed relation judgment.

## 260821-DAGQC-L4 Optional Graph And Adoption Sequence

Each schedulable candidate has one effective priority: use its candidate override when present,
otherwise inherit the owning-master default; never combine them or retain duplicate current rows.
The strategist records this judgment input, while the orchestrator compares effective grades
across the portfolio.

A graph-less plan remains fully planned. It classifies every master and records dependency,
priority, coherence, and topology reasoning, then adoption stops after all `attach_master` calls.
If an explicit graph is later chosen, complete every master attachment first and send one
`author_execution_graph` batch with the full node set plus evidence-backed edges. The existing
`add_edge` examples already carried `judgmentId`; no example repair was invented.

## CCR-L42 current candidate

A successor strategy review now carries the sealed issue list, fixed/unfixed dispositions, and subset rule; it cannot perform a new portfolio sweep, add a lens or route, or turn an outside-list observation into a finding. Three rounds remain the ordinary maximum and further work requires developer authorization.
