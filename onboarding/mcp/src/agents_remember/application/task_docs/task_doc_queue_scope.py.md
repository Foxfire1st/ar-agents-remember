# mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Prepares the one governing sprint queue identity from the exact task-source generation accepted
for a publication attempt, while explicitly leaving genuinely standalone/light documents outside
queue governance. Current L2 still retains the queue-governed publication seam; L3 owns task-first
publication, affected-candidate invalidation, and waiting-only queue rebuild.

## Code Commentary

### Logic

Preparation builds topology from the captured `TaskDocSourceSnapshot` set, including accepted
absence, then distinguishes existing versus new task documents, master versus leaf identity, and
orchestration-sprint versus commanded-master scope. Existing leaves resolve their structural parent
master through that generation; new and edited masters compute every affected execution sprint and
refuse ambiguous multi-sprint scope. The result pairs the optional queue scope with the unchanged
source snapshots that publication must use.

### Conventions

Queue scope is derived from canonical task-document topology and normalized references; callers do
not supply a sprint or master override.

### Invariants And Boundaries

- Light documents and masters not commanded by an execution sprint are explicitly ungoverned.
- A graph-commanded leaf must resolve to its exact owning master.
- One publication cannot affect multiple sprint queues.
- Queue projection reads are not task-document CAS inputs; only the captured task-source generation
  returns with the prepared scope.
- The module prepares scope only; the current-L2 caller still owns the queue-governed publication
  transaction, whose task-first replacement is deliberately deferred to L3.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is repository-internal task authority.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Existing task scope distinguishes orchestration sprints, commanded masters, and exact leaf parents. | `_existing_scope` | mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py:68-86 |
| New task scope derives its master identity before checking commanded sprint membership. | `_new_scope` | mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py:89-104 |
| The public resolver leaves light tasks ungoverned and translates malformed or ambiguous topology into one typed scope error. | `governing_queue_scope` | mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py:107-127 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Accepted-Generation Queue Scope

Queue-scope preparation now consumes the exact `TaskDocSourceSnapshot` set captured for the task
publication attempt. Presence and absence are resolved through that accepted topology generation,
and the prepared result returns the same snapshots to the publication owner. This prevents queue
projection reads from becoming task-document CAS inputs. The current L2 queue-governed publication
seam remains transitional; task-first invalidation and waiting-only rebuild are L3 obligations.

| Finding | Source |
| --- | --- |
| Preparation binds queue identity to one accepted task-source generation. | mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py:25-45 |
| Existing-source resolution includes accepted absence rather than consulting the live filesystem again. | mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py:137-179 |

## Update History

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled accepted-source-generation queue-scope preparation and the current-L2 versus L3 boundary. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/application/task_docs/task_doc_queue_scope.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T11:25+02:00 — Created for the L3 static-gate repair that extracted queue-scope
  resolution from the task-doc dispatcher without duplicating or changing its policy.
