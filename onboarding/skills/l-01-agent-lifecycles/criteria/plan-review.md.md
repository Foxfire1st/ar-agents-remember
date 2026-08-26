# skills/l-01-agent-lifecycles/criteria/plan-review.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/criteria/plan-review.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:45+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

## Governing Overview

[lifecycle skill overview](../overview.md)

## Purpose

Canonical adversarial-review criteria for an orchestration plan. The catalog re-derives evidence,
shared surfaces, blast radius, priority, topology, findings honesty, fact/judgment ownership, and
review independence before the architect adopts a portfolio plan.

## Code Commentary

### Logic

PR-4 distinguishes dependency topology from runtime source-pair selection. An explicit
`executionGraph` requires exact membership, cited acyclic edges, derived waves, and valid atomic
blocker placement. A graph-less choice remains fully planned: canonical commanded-master order is
only the stable equal-priority tie-break, and source-pair activation exposes one atomic master at a
time. Selecting another master may pause the former without full integration, retirement, or an
invented dependency.

The remaining standing criteria keep the plan evidence-complete: refute uncited edges, re-intersect
shared surfaces, re-derive high blast-radius and effective priority, reject dishonest findings,
separate detection from judgment, and require an independent reviewer using evidence of the right
class. Graph absence never waives classification, priority, dependency, or coherence reasoning.

### Invariants And Boundaries

- Runtime serialization cannot be presented as a dependency edge.
- A graph-less plan is valid only when its topology choice and planning judgments are explicit.
- Selecting another master does not imply the old master integrated or terminated.
- Review remains independent of plan authorship.

### Todos

Exact source claims are reconciled to the frozen criterion; real-commit verification remains
closeout-owned.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| PR-4 defines both explicit-graph and graph-less activation review. | `### PR-4 — Order-respects-edges` | skills/l-01-agent-lifecycles/criteria/plan-review.md:48-70 |
| Strategist doctrine authors the topology choice under review. | `# Lifecycle — Strategist` | skills/l-01-agent-lifecycles/roles/strategist.md:1-249 |
| The template renders the graph-less activation walk explicitly. | "## Derived Waves And Blocker Walk" | skills/l-01-agent-lifecycles/templates/orchestration-task.md:154-154 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned review criterion.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:45+02:00 — Reconciled the frozen criterion, removed the obsolete pending-freeze
  todo, and restored canonical Docs/Cross-Repo reference sections.

- 2026-08-26T05:20+02:00 — Created strict onboarding for PR-4's corrected graph-less semantics:
  activation serialization is not full-integration dependency, and pause preserves durable work.