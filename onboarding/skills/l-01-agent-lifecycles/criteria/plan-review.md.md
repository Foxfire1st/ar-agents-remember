# skills/l-01-agent-lifecycles/criteria/plan-review.md

## Governing Overview

[overview](../overview.md)

## Purpose

Canonical adversarial-review criteria for a sprint plan. The catalog re-derives evidence,
shared surfaces, blast radius, priority, topology, findings honesty, fact/judgment ownership, and
review independence before the plan reaches the developer's drawing board.

## Code Commentary

### Logic

PR-4 distinguishes dependency topology from runtime source-pair selection. An explicit
`executionGraph` requires exact membership, cited acyclic edges, derived waves, and valid atomic
blocker placement. A graph-less choice remains fully planned: canonical commanded-master order is
only the stable equal-priority tie-break, nothing serializes the masters, independent atomic masters
proceed concurrently, and selecting one does not hold another. PR-3 names implicated dependents
through `read_ar_files` and opens them natively, and requires one effective priority row per
schedulable candidate.

The remaining standing criteria keep the plan evidence-complete: refute uncited edges, re-intersect
shared surfaces, re-derive high blast-radius and effective priority, reject dishonest findings,
separate detection from judgment, and require an independent reviewer using evidence of the right
class. Graph absence never waives classification, priority, dependency, or coherence reasoning.

### Invariants And Boundaries

- Runtime serialization cannot be presented as a dependency edge.
- A graph-less plan is valid only when its topology choice and planning judgments are explicit.
- Selecting one master does not hold another; graph absence is never described as a dependency.
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

- PR-4 defines both explicit-graph and graph-less topology review. [1]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned review criterion.

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. The following whole-file reference locates that authored contract; it does not convert inherited statements into executed or whole-card acceptance.

- The authored source owns this contract; the distribution copy is not a separate authority. [4]
