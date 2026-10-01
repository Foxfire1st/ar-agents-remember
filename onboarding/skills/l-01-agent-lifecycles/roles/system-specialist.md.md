# skills/l-01-agent-lifecycles/roles/system-specialist.md

## Governing Overview

[overview.md](overview.md)
## Purpose

The optional sprint-bound, investigate-first provider-degradation seat.

## Code Commentary

### Logic

The system specialist binds to `(sprint document, system-specialist)` and investigates one provider
degradation event from durable event, state, metric, log, and runtime evidence. It writes the report
before any fix. Only an explicit orchestrator order authorizes the bounded provider remediation;
otherwise it recommends an action or provider stop. `message_parent` resolves the current sprint
orchestrator without exposing occupant identity.

The role table classifies system-specialist as target-only. Its orchestrator is the ordinary
plane-hosted dispatch caller; an identity-free developer launcher may target the sprint specialist
only for an explicit task-seat takeover. This seat has no `dispatch_agent` caller authority or
ambient recovery route, and its dispatch/tools rows are structural documentation rather than
settings keys.

### Invariants And Boundaries

- Provider-only scope: no task, memory, ledger, lifecycle, or product-code mutation.
- Report before remediation; investigation alone never implies fix authority.
- Completion is the report/fix artifact plus terminal/finalizer truth, not a parallel row.
- Canonical lifecycle doctrine owns this source; generated copies are synchronization outputs.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References

`skills/l-01-agent-lifecycles/roles/system-specialist.md` is the canonical role contract; provider
degradation state and the orchestrator brief supply the concrete event evidence.

### Cross-Repo References

No meaningful cross-repo references.
