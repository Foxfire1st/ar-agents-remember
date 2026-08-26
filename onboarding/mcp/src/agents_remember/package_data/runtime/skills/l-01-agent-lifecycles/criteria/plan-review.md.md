# l-01-agent-lifecycles/criteria/plan-review.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-26T05:20+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `../../../../../../../overview.md` |

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
explicit graph or the reasoned graph-less source-pair-selected atomic-sequential default),
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

The standing list MUST run every time the catalog binds; amendments land only through the
promotion ratchet on the loop owner's (the orchestrator's) acceptance.

### Todos

PR-4 retains topological checks for explicit graphs. PR-7 is a candidate criterion, not an
immediate mechanization TODO.

### Docs References

No external domain documentation applies to this repository-local catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| This package-data catalog copy defines the complete current plan-review floor, including effective-priority resolution and explicit-graph or graph-less topology review. | `# Criteria Catalog — Plan Review (the strategist loop)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md:1-134 |
| Root `skills/` is the canonical source tree and `scripts/sync-skills.py` propagates it into the MCP package-data copy and all eight harness package copies. | "class SkillTarget" | scripts/sync-skills.py:27-27 |
| The reviewer role binds `plan-review` with `report-verification` for orchestration-task plan reviews, and keeps the promotion ratchet as the catalog amendment path. | `# Lifecycle — Adversarial Reviewer` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:1-232 |
| The orchestration-task template requires cited shown work, one effective priority per candidate, an explicit topology choice, and complete graph bootstrap when a graph is adopted. | `# Orchestration-Task Template` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md:1-198 |
| The strategist lifecycle produces the orchestration task and treats a persisted graph as optional while keeping topology reasoning mandatory. | `# Lifecycle — Strategist` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md:1-247 |

## Cross-Repo References

No sibling repository evidence is needed for this catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

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
valid: canonical commanded-master order is the stable equal-priority tie-break and source-pair
activation exposes one atomic master at a time. Selecting another may pause the former without full
integration, retirement, or an invented dependency. Graph absence does not waive classification,
priority, dependency, or coherence work. A sanctioned strategist skip changes the plan author to
the orchestrator, not the completeness standard. The repository-wide `add_edge`
example census already found `judgmentId` on every example, so L4 made no fabricated example edit.

## IAS Graph-Less Review Correction

Runtime activation serialization is not dependency evidence. PR-4 must reject a plan that turns
the selector's one-exposed-master property into a false full-integration edge or implies that a
paused master was terminalized.

## Update History

- 2026-08-26T05:20+02:00 — Corrected generated PR-4 onboarding: graph-less selection is a
  source-pair activation boundary, not a full-integration dependency. Final ranges remain
  post-Dagger-owned.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: reconciled one effective candidate priority,
  portfolio-comparison ownership, reasoned graph-less planning, optional explicit graphs, and the
  no-fabricated-example result. Canonical/generated sync is complete; Dagger acceptance remains
  closeout-owned and pending.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: PR-8 added — no plan self-review and requirement
  verdicts must match their evidence class (mounted-UI / operation-level / artifact-level proof).
  Verified at code commit de3a0fd9.

- 2026-08-20T05:10+02:00 — 260815-DAG-L14: PR-4 extended to typed-row/graph agreement.
  Verified at code commit 2f494982.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: aligned plan-loop authority and added auditable
  fact/judgment plus graph-edge traceability checks. Verification remains closeout-owned.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B19 curator: replaced the `n/a` table rows with
  exact anchors (headings/class) and fixer-generated ranges; exact non-fixing check returns zero
  findings.

- 2026-07-09T10:40+02:00 — 260707-HFX2-L8: refreshed after synced PR-6 scaling &
  reclamation at design time entered the plan-review candidate catalog, requiring plans to name
  caps, budgets, compactor/reclamation owners, and scaling proof before code exists. Verification
  metadata pinned until closeout stamps the HFX2-L8 commit.

- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `criteria/plan-review.md` catalog (leaf 260703-L12): PR-1 refute uncited edges, PR-2 missed-shared-surface hunt (incl. declared-new surfaces and parent-route CONFLICT risk), PR-3 blast-radius re-derivation via cgc, PR-4 order-respects-edges, PR-5 findings honesty — the fifth catalog, seeded by ruling for the strategist loop. Verification metadata pinned until closeout stamps the L12 commit.
