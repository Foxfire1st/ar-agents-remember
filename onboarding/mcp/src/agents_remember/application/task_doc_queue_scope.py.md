# mcp/src/agents_remember/application/task_doc_queue_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_doc_queue_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T11:25+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Resolves the one sprint closeout queue that serializes a task-document publication, while
explicitly leaving genuinely standalone/light task documents outside queue governance.

## Code Commentary

### Logic

The resolver distinguishes existing versus new task documents, master versus leaf identity, and
orchestration-sprint versus commanded-master scope. Existing leaves first resolve their structural
parent master, then require an exact parent edge only when that master is commanded by a sprint.
New and edited masters compute every affected execution sprint and refuse ambiguous multi-sprint
scope. The result is a small immutable pair of sprint reference plus optional owning master.

### Conventions

Queue scope is derived from canonical task-document topology and normalized references; callers do
not supply a sprint or master override.

### Invariants And Boundaries

- Light documents and masters not commanded by an execution sprint are explicitly ungoverned.
- A graph-commanded leaf must resolve to its exact owning master.
- One publication cannot affect multiple sprint queues.
- The module resolves scope only; the caller owns the locked publication transaction.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is repository-internal task authority.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Existing task scope distinguishes orchestration sprints, commanded masters, and exact leaf parents. | `_existing_scope` | mcp/src/agents_remember/application/task_doc_queue_scope.py:59-80 |
| New task scope derives its master identity before checking commanded sprint membership. | `_new_scope` | mcp/src/agents_remember/application/task_doc_queue_scope.py:83-102 |
| The public resolver leaves light tasks ungoverned and translates malformed or ambiguous topology into one typed scope error. | `governing_queue_scope` | mcp/src/agents_remember/application/task_doc_queue_scope.py:107-127 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-15T11:25+02:00 — Created for the L3 static-gate repair that extracted queue-scope
  resolution from the task-doc dispatcher without duplicating or changing its policy.
