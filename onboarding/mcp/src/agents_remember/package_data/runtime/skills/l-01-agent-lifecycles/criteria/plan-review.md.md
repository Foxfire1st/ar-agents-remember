# l-01-agent-lifecycles/criteria/plan-review.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The plan-review criteria catalog — the fifth catalog in the new `criteria/` folder (leaf
260703-L12): what the adversarial reviewer runs against an **orchestration task** (the
strategist's sprint plan) in the portfolio three-party loop, before the developer's drawing
board. Its criteria are seeded by ruling (the developer's method challenge, 2026-07-06) rather
than by prior catches — the strategist loop had not run yet when the catalog was seeded. It now
also carries the PR-7 design-time scaling and reclamation candidate seeded by the HFX2-L7/HFX2-L8
incident.

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/criteria/plan-review.md`. The standing catalog covers **PR-1 refute
uncited edges** (every dependency edge needs evidence — a tool query, file, decision-log, design
citation, or a declaration cross-reference for new surfaces; uncited = refutable by default),
**PR-2 missed-shared-surface hunt** (class-completeness applied to surface intersections:
re-intersect the per-leaf surface lists — existing AND declared-new, including CONFLICT-risk at a
shared parent route — and hunt omitted pairs), **PR-3 blast-radius re-derivation** (re-derive at
least the HIGH entries with `cgc_dependencies`/`cgc_callers`/`cgc_callees`; spot-check the rest;
resolve one effective priority per candidate), **PR-4 topology agreement** (validate either an
explicit graph or the reasoned graph-less per-contract-activated atomic-sequential default — a
sprint shape that serializes nothing, since a graph-less sprint declares no dependencies and
independent atomic masters proceed concurrently),
**PR-5 findings honesty**,
**PR-6 detection-versus-judgment ownership**, and **PR-8 review independence plus evidence-class
matching**. A **Candidate Criteria** tier carries **PR-7 scaling & reclamation at design time**:
plans that introduce or change a store, loop over a store, queue, or append-only log must name the
cap, budget, and compactor/reclamation owner before code exists, and must plan scaling proof
across at least two input sizes. Plus the exploratory mandate (default 2) and the promotion
ratchet. The reviewer holds the same read-only analysis tools the strategist used, so mechanical
claims are re-derivable.

### Conventions

Catalog files live beside the templates under `criteria/` and are bound per review type by
`roles/reviewer.md`: the plan review runs this catalog + report-verification.

### Invariants And Boundaries

When a plan review is explicitly requested, the standing list runs and reports each criterion; the
catalog does not create a routine closeout or integration gate. Amendments land only through the
promotion ratchet on the loop owner's (the orchestrator's) acceptance.

### Todos

PR-4 retains topological checks for explicit graphs. PR-7 is a candidate criterion, not an
immediate mechanization TODO.


## CCR-R12@v5 Review Scope

This criteria catalog supplies evidence only when the corresponding review is explicitly requested. It does not create a closeout or integration prerequisite; routine handoff uses the worker and curator targeted/scoped check records and preserves any failed or not-run state.

### Docs References

No external domain documentation applies to this repository-local catalog.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- This package-data catalog copy defines the complete current plan-review floor, including effective-priority resolution and explicit-graph or graph-less topology review. [1]
- Root `skills/` is the canonical source tree and `scripts/sync-skills.py` propagates it into the MCP package-data copy and all eight harness package copies. [2]
- The reviewer role binds `plan-review` with `report-verification` for orchestration-task plan reviews, and keeps the promotion ratchet as the catalog amendment path. [3]
- The orchestration-task template requires cited shown work, one effective priority per candidate, an explicit topology choice, and complete graph bootstrap when a graph is adopted. [4]
- The strategist lifecycle produces the orchestration task and treats a persisted graph as optional while keeping topology reasoning mandatory. [5]
- The shipped plan-review catalog now states the corrected graph-less rule instead of the removed source-pair exposure wording. [6]

### Cross-Repo References

No sibling repository evidence is needed for this catalog.

No meaningful cross-repo references found.

## 260815-DAG-L2 Plan Ownership And Traceability

Plan review is architect-owned. The strategist is builder when approved; the orchestrator is
builder only after a sanctioned strategist skip, and always adopts the architect-ruled artifact.
The criteria now re-derive nature, blast radius, priority, graph order, and blockers; PR-6 requires
mechanical facts to remain distinguishable from explicit judgment. Every graph-selected relation
must carry evidence and the owning Judgment Register id.

## 260815-DAG-L14 Doctrine Sync

PR-4 (topology agreement) is extended to typed-row/graph agreement: a sprint row carrying a typed
`masterRef` must agree with the execution graph and `orchestrates` membership.

## 260815-DAG-L15 Review-Doctrine

PR-8 stands as a new criterion: the reviewer of a plan is never its author (a distinct reviewer
seat runs the review; a self-signed requirement is a blocking finding), and every requirement
verdict must cite evidence of the requirement's class — mounted-UI proof for rendering,
operation-level proof for scheduling, artifact-level proof for the data model. Evidence of the
wrong class is verdict-laundering, never a pass. Catching class: 260815-DAG L7/L8/L9 orchestrator
self-reviews and the L8-R3 projection-only pass (review reports r2 F7, r4 F6, r6 F8/F9/F12).

## 260821-DAGQC-L4 Priority And Optional-Topology Closure

PR-3 resolves exactly one effective priority for each schedulable candidate: a candidate row
overrides its owning-master default; without an override, the master row is inherited. Grades are
never combined, duplicate current rows are invalid, and the orchestrator still compares the
resulting effective grades across the ready portfolio. Stable graph/task order is only an
equal-grade tie-break.

PR-4 reviews the topology actually chosen. An explicit graph needs exact membership, cited edges,
acyclic derived waves, and correct atomic-blocker placement. A reasoned graph-less sprint is also
valid: canonical commanded-master order is the stable equal-priority tie-break, and per-contract
activation means two sprint-commanded atomic masters sharing one protected source pair hold
independent records, so activating one never pauses, replaces, or blocks the other and never invents
a dependency. Graph absence does not waive classification,
priority, dependency, or coherence work. A sanctioned strategist skip changes the plan author to
the orchestrator, not the completeness standard. The repository-wide `add_edge`
example census already found `judgmentId` on every example, so L4 made no fabricated example edit.

## IAS Graph-Less Review Correction

Per-contract activation is admission state, not dependency evidence, and it serializes nothing
across masters. PR-4 must reject a plan that turns the per-contract activation boundary into a
false full-integration edge, treats a sibling master sharing the protected source pair as blocked
by the selected one, or implies that a nonterminal master was terminalized. The only activation
waiting reason is `atomic-series-reconciling` for a contract's own in-flight reconciliation, so a
plan may not cite a foreign master as a reason to wait; and because a graph-less sprint declares no
dependencies, PR-4 must not read its `atomic-sequential` shape as a serialization mechanism —
independent atomic masters proceed concurrently, and only explicit `executionGraph` waves gate on
`predecessor-incomplete:` (developer ruling).

**Shipped text corrected (260831-LOCR-L36 round 2).** The mirrored runtime catalog this card
describes — `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md` —
now states the corrected doctrine in its own text at `:64-68`: "canonical commanded-master order is
the stable tie-break and nothing serializes the masters. A graph-less sprint declares no
dependencies, so independent atomic masters proceed concurrently and no master is held because
another is selected; graph absence must not be misrepresented as a dependency requiring full
integration before another master can proceed." The earlier shipped-source debt note is therefore
removed — a repo-wide grep for `source-pair-scoped`, `source-pair-selected`, the "logically pauses
the former master" admission, one-selected-master-at-a-time and source-pair activation wording
returns 0 hits in the code worktree.

## CCR-L42 current candidate

The plan-review criteria now apply exploratory and promotion duties only to a baseline review. Fix-verification uses the sealed plan issue IDs and cannot recensus the plan, add a criterion, or broaden an issue.
