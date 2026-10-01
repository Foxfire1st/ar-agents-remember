# skills/w-02-light-task-workflow/workflow.md

## Governing Overview

[repository onboarding overview](../../overview.md)

## Purpose

This workflow governs the planning, approval, implementation, evidence, and closeout lifecycle for
one light task or a master plus light-subtask series.

## Code Commentary

### Logic

Phase 0 compiles independently falsifiable obligations into stable, versioned canonical packets,
cold-reads them, and obtains developer approval before any task topology exists. Later phases
project those exact revisions into tasks, implement against a live checklist, maintain one
acceptance envelope per revision, and require independent adjudication before closure.

A changed obligation creates a new version-addressed packet, invalidates only affected acceptance,
updates affected projections, and rebriefs affected leaves. Task documents summarize topology and
never become alternate requirement authorities.

Delivery attempts form a separate append-only axis and advance only when an exact candidate is
handed to independent review, or after rejection when its successor is handed off. Internal
implementation/test/evidence reruns remain separate protocol events. Lightweight worker records
bind exact candidates, requirement-specific facts, predecessors, and content-addressed expanded
evidence; reviewer records independently adjudicate those attempts, and failure classes determine
recovery ownership. Leaf journals remain authority. A rebuildable master summary exposes formal
attempts/rejections/current state/dominant class, excludes protocol events, and cannot gate or lock
any task, lifecycle, closeout, integration, or queue operation.

### Conventions

- Use one planning wrapper with `requirements/README.md` and immutable revision packets.
- Tool-managed light tasks are JSON-primary and rendered through `task_doc`.
- Decision logs are append-only and timestamps use `YYYY-MM-DDTHH:MM`.
- Escalate to a master series when the implementation plan no longer fits one page.

### Invariants And Boundaries

- No sprint, master, task, or leaf is authored before corpus approval.
- Every leaf owns exactly one primary requirement revision.
- One revision may have multiple independently executable manifestation leaves.
- Requirement acceptance and durable-evidence lifecycle remain independent gates.
- Worktree commits still require their separate approval.
- Accepted attempts reopen only through independently proven regression plus owner-recorded bounded
  invalidation, or an approved semantic revision.

### Todos

None.


## CCR-R12@v5 Light-Task Boundary

A light-task handoff records relevant targeted checks and honest failed or not-run results before the authorized Git transaction. Its commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside closeout/integration remains unchanged. Full quality, full tests, full memory quality, certification, and review remain explicit operations and are not automatic closeout or integration prerequisites.

## Evidence

### Docs References

No external Domain Documentation source governs this workflow.

### Repo-Internal References

- Requirement compilation, cold read, and approval precede topology. [1]
- Tasks carry filtered projections rather than rewritten contracts. [2]
- Implementation maintains one acceptance block per exact revision. [3]
- Requirement changes version, invalidate, update, and rebrief affected work. [4]
- Phase 2 and closure append exact worker/reviewer records, while master-series summaries remain rebuildable and non-gating. [5]

### Cross-Repo References

The context resolver supplies target-repository paths, tools, and memory policy; this workflow does
not hard-code them.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.
