# mcp/src/agents_remember/serving/_agent_notifier_evaluation.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Evaluates mechanical agent-notifier findings from current catalog, topology, inbox, deadline, and
pane evidence without performing mutations.

## Code Commentary

### Logic

Rebind evaluation detects pending rows whose private occupant correlation is dead and derives the
current owner from task-document containment. Pending expiry, liveness, dead-upstream, inbox, and
pane predicates remain evidence-only. The combined evaluator passes one topology authority through
the structural finding families.
ARSPAWN-L2 makes structural failure containment explicit at every predicate seam that can resolve
an owner: rebind, stale-turn, dead-upstream, and redelivery filtering each suppress only the
unprovable row or finding. The evaluator therefore remains total for the rest of the sweep without
inventing a fallback recipient.

### Conventions

Evaluation returns typed findings; actions, persistence, and delivery are separate. Predicate
helpers accept the `TaskHierarchy` protocol, while the production composition constructs
`TaskDocumentTopology`; tests and other callers can supply an existing hierarchy authority without
requiring the concrete filesystem topology type.

### Invariants And Boundaries

- Owner rebinding never uses spawn ancestry or global role fallback.
- Ambiguous structural owners fail instead of first-match routing.
- Model output/artifact judgment is not a notifier predicate.
- Evaluation itself performs no durable write.
- A malformed or ambiguous structural route is non-actionable for that row, not an exception that
  aborts unrelated predicate families or the heartbeat.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Rebind evaluation contains a malformed or ambiguous replacement chain to the affected row. [1]
- Stale-turn and dead-upstream evaluation suppress only the structurally unprovable seat. [2]
- Redelivery budget excludes only a row whose route predicates cannot be proven. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
