# mcp/src/agents_remember/observer/projection.py

## Governing Overview

[observer overview](overview.md)

## Purpose

Defines the canonical workspace projection models and re-exports the extracted task DTOs. Retained task-document projections carry structural references; removed pickup and expectation analytics DTOs are not current carriers. Runtime ids remain observation/correlation, not routing authority.

Workspace/task/process/analytics composition remains here; task-summary, full-reader, graph and closeout DTOs live in [projection_task_documents](projection_task_documents.py.md) and are re-exported. `TaskDocumentRef` comes from its defining `models.task_document_ref` module. `TaskDependencyNode` carries qualified reference/gone display facts, not copied task status or execution permission.

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

`TaskState` carries authored `stage` and optional runtime `activity` and `eventAt`; it no longer declares a served `ageSeconds`. The browser computes task-event display age from `eventAt`. This is not removal of the separate task-document/file-age fields, which the ruling routes outside this leaf. `TaskEntry` adds qualified key/reference, summary, bound worktrees, one parent, ordered children and `TaskCounts`. `WorkspaceProjection.tasks` and `taskCounts` replace lifecycle and parallel series collections; top-level enclosures are the unbound remainder. `task_entries.build_task_entries` is the single stage/activity and membership producer, not this DTO module or the client.

Reader DTOs retain canonical references, lump/segment graph nodes and legacy bare-ref lifting, typed sprint seats and commanded-master links. `TaskSummary` holds reader content; `TaskDocNode` adds full identity, status and membership. Display fields do not choose occupants, authorize relationships or infer task completion from a host turn. Enclosure `lifecycleId` still binds operations, and `LifecycleOperationProjection` remains operation progress rather than session activity.

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

`TaskSummary`/`TaskDocNode` may carry strict directGrant evidence (`grantedBy`/`grantedAt`). None means no displayed readable grant. This schema does not read/write the grant store or authorize direct execution; the authored TaskDocument is unchanged.

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
Task summaries and full task nodes also expose typed discarded-unstarted history and counts; `None`
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



- Task summaries and full reader nodes carry optional strict directGrant display evidence, not authorization. [6]

- TaskState carries stage, activity and eventAt, without a served task-event age; the browser derives display age. [7]
