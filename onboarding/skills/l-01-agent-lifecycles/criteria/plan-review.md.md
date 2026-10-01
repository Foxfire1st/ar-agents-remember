# skills/l-01-agent-lifecycles/criteria/plan-review.md

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


## CCR-R12@v5 Review Scope

This criteria catalog supplies evidence only when the corresponding review is explicitly requested. It does not create a closeout or integration prerequisite; routine handoff uses the worker and curator targeted/scoped check records and preserves any failed or not-run state.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- PR-4 defines both explicit-graph and graph-less activation review. [1]
- Strategist doctrine authors the topology choice under review. [2]
- The template renders the graph-less activation walk explicitly. [3]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned review criterion.
