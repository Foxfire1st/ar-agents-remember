# mcp/src/agents_remember/observer/projection.py

## Governing Overview

[observer overview](overview.md)

## Purpose

Defines the canonical workspace projection models and re-exports the extracted task DTOs. Retained task-document projections carry structural references; removed pickup and expectation analytics DTOs are not current carriers. Runtime ids remain observation/correlation, not routing authority.

Current ownership split: workspace/lifecycle/process/analytics composition remains here; task-reader, graph-shape, closeout and series DTO definitions now live in [projection_task_documents](projection_task_documents.py.md). This file imports that module and keeps public task DTO class names as aliases. The canonical `TaskDocumentRef` identity is defined in `models.task_document_ref`, not exported as an incidental import by this schema facade; readers import that defining module directly. Retained DTO contracts below describe those definitions, not an alias as independent schema authority. `TaskDependencyNode` and optional completion/dependency/fixed-prose fields are served display data, never task mutation or execution permission.

## Code Commentary

### Task-reader display projection

The served TaskDocNode adds model-derived sprint/master/task `form`, type, optional branch/status note,
header-note label/value rows and their total, and optional review state. A present current-server review
state always carries the whole-round `openFindings` and `totalFindings`; a reader must not recount flags
in the capped findings slice. The Python fields have construction defaults and the generated TypeScript
wire mirror requires counts; this is a producer obligation, not a claim that JSON Schema rejects every
omitted default. An older payload omits the entire review state.

Top-level step outcome/note and finding-description previews have explicit truncation flags. Nested
step notes are projected but have no corresponding truncation flag and are not drawn by the current
task-page nested-row renderer. Projection is observation only, never review or lifecycle authority.


L23 adds optional `lifecycleOperation` state to `EnclosureNode`; the browser receives task-addressed operation progress without internal operation identity.

### Logic

Retained task-document projections expose `TaskDocumentRef` so the dashboard
joins the same real sprint/master/leaf hierarchy used by routing. Removed pickup and expectation
analytics DTOs are not current structural-reference carriers. `TaskDocNode` remains the
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

## L126 Product-Record Marking Field

`TaskDecisionNode` carries `product_record: bool = False`: true when the entry
is a product-written record (finalize lifecycle, removed/skip step), marked from
the writers' own constants in `tasks.document`. The marking is provenance-based
(exact/prefix string match); no enforced authorship separation keeps authored
text from colliding (see INV-NBCGCF). The stored decision shape is unchanged.

The marking definition now lives in `projection_task_documents.TaskDecisionNode`. Exact Finalize text remains recognized for retained legacy records, but the current finalizer stamps `completedAt` on its own newly completed document and appends no Finalize decision to either own or parent logs. Removed/skip-step recognition and the collision caveat remain.

### Invariants And Boundaries

- Projected task references identify work, not runtime occupants.
- Projection remains read-only evidence and cannot become routing authority.
- Generated dashboard types must be synchronized with this schema.

### Todos

None.

## Display-only grant projection

Task nodes and series-child rows may carry strict directGrant evidence (grantedBy/grantedAt). None means no displayed readable grant. This observer schema neither reads nor writes the store and cannot authorize direct execution; TaskDocument remains unchanged. Generated projection schema/types mirror this display model.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References


- Retained task-document projection models carry canonical task references; pickup and expectation analytics DTOs are removed. [1]


- Lump/segment nodes and sampling endpoints retain strict served shapes and bare-ref lifting in the extracted DTO owner. [3]



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

> **Retained historical source account — superseded by the current contract:**
> `TaskDocNode` gains the optional `executionGraphView` field (L12-R4): the render-ready per-node sprint graph (`observer/projection_graph.TaskExecutionGraphView`) the dashboard renders directly — node kind, master ref + title, leaf ids + titles, derived wave index, mechanically derived frontier state, execution nature, and predecessors with reasons. The field is `None` for documents without a graph (backward compatible); the dashboard never joins raw refs or re-derives waves.

Current view: the field is defined by `projection_task_documents.TaskDocNode`. A sprint may receive its persisted-graph view; an ordinary master may instead receive a derived dependency Order graph without a persisted `executionGraph`. The server prefers a nonempty Order graph over the sprint-view fallback. The DTO remains optional, and the browser renders served nodes rather than joining refs or deriving waves.


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


- Extracted CloseoutQueueNode has unbounded members; sourceProblems and candidate reasons retain their 256-item ceilings. [5]





- Task documents remain the projected hierarchy; the actual TaskDocNode/dependency definitions live in projection_task_documents, while projection re-exports them. [2]



- Task nodes and series-child rows carry optional strict directGrant evidence defined by the extracted DTO owner; it is display, not authorization. [6]
