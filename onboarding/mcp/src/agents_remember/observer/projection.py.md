# mcp/src/agents_remember/observer/projection.py

## Governing Overview

[observer overview](overview.md)

## Purpose

Defines the canonical workspace projection models. It now carries structural task-document references
on task-aware analytics while preserving runtime ids only as observation/correlation.

## Code Commentary

L23 adds optional `lifecycleOperation` state to `EnclosureNode`; the browser receives task-addressed operation progress without internal operation identity.

### Logic

Task, expectation, pickup, and attention projections can expose `TaskDocumentRef` so the dashboard
joins the same real sprint/master/leaf hierarchy used by routing. `TaskDocNode` remains the
JSON-primary task view; lifecycle attachment is optional. Since 260815-DAG-L11 the sprint graph
projection is leaf-segmented: `TaskExecutionNode` (kind `master` lump or `segment` + `leafIds`)
and `TaskExecutionEndpointNode` (ref + optional segment-sampling `leafId`) mirror the persisted
schema, with before-validators lifting legacy bare refs into the uniform served shape;
`TaskExecutionEdgeNode` carries the optional `judgmentId`, and `TaskDocNode.executionWaves` derives
over execution nodes. The observer does not choose current seat occupants or authorize relations. Since
260815-DAG-L14 the task projection also carries first-class sprint structure:
`TaskSubTaskRefNode.masterRef` (the typed commanded-master link — the dashboard opens that
document directly; `None` for ordinary leaf rows and legacy slug-only rows) and `TaskSeatNode`
(role/label/identity/state, `extra="forbid"`, mirroring `tasks.document.SprintSeat`), projected
from `TaskDocument.seats`; `TaskDocNode.seats` defaults to empty so non-sprint docs are untouched.

### Conventions

The Python schema is the source for generated TypeScript and JSON schema artifacts.

### Invariants And Boundaries

- Projected task references identify work, not runtime occupants.
- Projection remains read-only evidence and cannot become routing authority.
- Generated dashboard types must be synchronized with this schema.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Pickup and expectation analytics carry structural references. [1]
- Task documents remain the real projected hierarchy. [2]
- The leaf-segmented graph projection (lump/segment nodes and sampling endpoints). [3]
- Workspace projection is the schema authority consumed by generation. [4]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

## L23 Engine Process Lineage

`EngineProcessNode` now carries the optional strict source-lineage projection.
The observer exposes resolved admission facts to operations; it does not compare
branches or synthesize recovery locally.

## L23 Lifecycle Model Package Review

Observer projection now imports `LifecycleOperationProjection` from
`models.lifecycles.operation`. Engine-process composition and the task-derived source-lineage
projection remain unchanged; this is an ownership-only model move.


## 260815-DAG-L12 Render-Ready Graph View

`TaskDocNode` gains the optional `executionGraphView` field (L12-R4): the render-ready per-node sprint graph (`observer/projection_graph.TaskExecutionGraphView`) the dashboard renders directly — node kind, master ref + title, leaf ids + titles, derived wave index, mechanically derived frontier state, execution nature, and predecessors with reasons. The field is `None` for documents without a graph (backward compatible); the dashboard never joins raw refs or re-derives waves.


## 260821-CLIVE Disposable Queue And Discard History Projection

Closeout nodes now expose service condition, source classification/fingerprint/problems, and exact
waiting-generation members with classification, effective priority, order, and reasons. Candidate
lifecycle state, active blocker, grade mutation, and commit/certification fields are removed.
Task/master and series nodes also expose typed discarded-unstarted history and counts; `None`
distinguishes a non-master from a master with an empty audit. The shared discard node/proof models
come from the dedicated closeout projection module.

## 260913-LCA-L6 Unbounded Closeout Queue Member Population

`CloseoutQueueNode` serves one exact-current disposable scheduling projection to the dashboard:
service condition, optional source classification/fingerprint, bounded `sourceProblems`, and
`members` as `CloseoutCandidateNode` rows. Since 260913-LCA-L6 the `members` array carries no item
ceiling — the `max_length=256` was removed with the candidate cap, so the served node reports
however many candidates the sprint has waiting. `sourceProblems` keeps `max_length=256` and
`CloseoutCandidateNode.reasons` keeps its own `max_length=256`; nothing else on this node is bounded
by that number.

- The served closeout-queue node's member population is unbounded while its problem and reason lists keep their item ceilings. [5]
