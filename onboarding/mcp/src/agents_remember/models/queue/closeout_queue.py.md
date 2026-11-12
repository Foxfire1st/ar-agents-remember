# mcp/src/agents_remember/models/queue/closeout_queue.py

## Governing Overview

[models overview](overview.md)

## Purpose

Defines the strict public status/rebuild request and effective response for the disposable sprint
closeout projection.

## Code Commentary

### Logic

`CloseoutQueueRequest` permits only `status` or idempotent `rebuild` for one sprint and caller.
`CloseoutQueueResponse` reports revision, service condition, source classification/fingerprint,
bounded source problems, deterministic waiting-generation members, the first ready generation, and
next action. Projection members carry classification, priority, order, and reasons; no lifecycle or
commit state is modeled. Since 260913-LCA-L6 the response's `members` list is unbounded — the
candidate ceiling was removed with its enforcement sites — while `reasons`, `sourceProblems` and
the queue's own master/edge caps keep their bounds.

### Conventions

All nested models are extra-forbid and every public text field is bounded; `CloseoutQueueResponse.members`
is the one public collection without an item ceiling, because it reports however many leaves a sprint
declares. One effective
priority is projected from candidate override or master default; portfolio comparison remains an
orchestrator decision outside this model.

### Invariants And Boundaries

- Service condition is exactly invalid-empty or valid-built.
- Only waiting door generations may be members.
- No claim, grade mutation, blocker, receipt, commit, certification, integration, or lifecycle
  evidence is modeled.
- A response may be discarded without losing canonical work evidence.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

### Repo-Internal References

- The request permits only status and rebuild. [1]
- The response carries effective projection condition, source identity, problems, and members. [2]

### Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE Final Disposable Projection Model

The public request now supports only `status` and idempotent `rebuild`, addressed by sprint ref and
caller. The response reports service condition, revision, source classification/fingerprints,
bounded source problems, members, first ready generation, and next action. Candidate mutation,
grade declaration, claim, certification, blocker, receipt, commit, lifecycle, and integration
actions have been removed. A projection is only `invalid-empty` or `valid-built`; it is a current
scheduling view, never an operation ledger.
