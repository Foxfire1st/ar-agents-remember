# skills/l-01-agent-lifecycles/templates/orchestration-task.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/orchestration-task.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:45+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

## Governing Overview

[lifecycle skill overview](../overview.md)

## Purpose

Canonical durable shape for an architect-ruled orchestration plan. It records mechanical facts,
judgments, evidence-cited relations, blast radius, one effective priority per candidate, topology,
leaf moves, reevaluation triggers, and the adoption payload independently of any seat occupant.

## Code Commentary

### Logic

The `Derived Waves And Blocker Walk` now describes graph-less runtime honestly. Canonical
commanded-master order is the stable tie-break, one source-pair-selected atomic master exposes
implementation at a time, and a later selection may logically pause and resume durable work. The
template no longer implies that graph absence forces every master to integrate fully before another
can be selected.

An explicit graph still derives waves and blocker positions from evidence-backed edges. Graph-less
adoption still requires the complete planning artifact; it merely stops before persisting an
`executionGraph`. First graph adoption remains one complete nodes-plus-edges batch after all master
attachments.

### Invariants And Boundaries

- Planning is mandatory; persisted graph structure is optional.
- Runtime activation order does not fabricate dependency truth.
- Selection may pause a live master without retiring its branch, task, or journal.
- Each candidate has one effective priority, with canonical order only breaking equal grades.

### Todos

Exact source claims are reconciled to the frozen template; real-commit verification remains
closeout-owned.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The graph-less walk carries source-pair selection and pause/resume semantics. | "## Derived Waves And Blocker Walk" | skills/l-01-agent-lifecycles/templates/orchestration-task.md:154-154 |
| Plan review independently validates that choice. | `### PR-4 — Order-respects-edges` | skills/l-01-agent-lifecycles/criteria/plan-review.md:48-70 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned orchestration template.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:45+02:00 — Reconciled the frozen template, removed the obsolete pending-freeze
  todo, and restored canonical Docs/Cross-Repo reference sections.

- 2026-08-26T05:20+02:00 — Created strict onboarding for the graph-less activation walk and its
  separation from dependency/full-integration semantics.