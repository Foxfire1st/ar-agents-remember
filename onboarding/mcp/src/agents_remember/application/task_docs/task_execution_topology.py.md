# mcp/src/agents_remember/application/task_docs/task_execution_topology.py

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Own the application policy for an explicit sprint execution topology. It validates edits against
the canonical task-document graph and provides `author_execution_graph` — since 260815-DAG-L11 the
incremental operation that applies one validated, judgment-provenanced batch of structural
mutations (add/remove node, add/remove edge, move leaf, set nature), and since 260815-DAG-L13 also
the bootstrap seam: the first `add_node` batch on a graph-less sprint creates the graph. The
one-time `migrate_execution_topology` operation is removed (L13): a graph-less sprint is not an
error — it runs the atomic-sequential default until a graph is authored.

## Code Commentary

### Logic

`author_execution_graph` plays the typed
`mutations` batch onto a `_GraphDraft` through the `_MUTATION_HANDLERS` dispatch: segments are
addressed by a sampling `leafId`, never named; `remove_node` refuses while an edge still touches
the node; `move_leaf` also places a leaf the master gained after authoring, and refuses to empty a
segment; `set_nature` targets only commanded masters. On a graph-less sprint the draft starts empty
and commanded membership comes from the canonical `orchestrates` aliases; the result reports
`bootstrapped: true`, and final validation requires exact membership plus an explicit nature for
every commanded master (a `set_nature` mutation in the same batch covers a master document that
lacks one). Judgment-bearing mutations (edges,
segmentation, nature reclassification) must carry a `judgmentId` that `_verify_authoring_judgments` (which since 260815-DAG-L14 delegates to the extracted shared
`verify_sprint_judgment_ids` — also used by the sprint linkage operations — so the graph-authoring
and attach paths verify judgment provenance through one function)
resolves against the sprint's canonical `Judgment Register (canonical judgment authority)` section —
a missing register is a typed refusal naming the section (sprint creation scaffolds the empty
canonical registers, and the write path validates their shape), an unknown row or a non
strategist/orchestrator author fails closed; the mechanism never invents a judgment. The prepared
candidate revalidates the whole graph, exact cross-document membership, and node-kind legality,
refuses unknown or unplaced leaf partitions (`_require_complete_partitions`), and reports
`leafPlacementFacts` plus `numberingHints` as facts. `dry_run` returns the rendered diff +
`wouldLose` preview without writing; apply publishes sprint plus nature-changed masters atomically
through the task-first publication transaction. Both preview and apply invoke the shared
`build_publication_batch_graph_titles` owner before their transaction boundary, so unsupported
multi-graph input refuses and the exact in-memory batch supplies the sole title context.

Since 260815-DAG-L15 every topology-schema write is preflighted against the serving runtime
(`require_serving_topology_schema` from `tasks/serving_preflight.py`): `author_execution_graph`
refuses with `ExecutionTopologyError` when the running build's `TaskDocument` model lacks the
topology fields or the installed non-editable `agents-remember-mcp` distribution is below the
`3.0.0rc8` serving floor (L15-R4, the rc7 `extra="forbid"` failure class). The authoring dialect
hardened on the playthrough findings: `judgmentId` is optional at parse on the edge/move/nature
mutations so a missing judgment surfaces the typed `task-execution-graph-judgment-required`
refusal instead of a raw pydantic error (F5); `_require_move_does_not_retarget_edge` refuses a
`move_leaf` whose leaf samples an edge endpoint with the named `task-execution-graph-move-retargets-edge`
before any acyclicity check (F3); `_require_draft_node_kinds` runs before `SprintExecutionGraph`
construction so the atomic segment-node-kind rule fires before the lump/segment mutual-exclusion
mask (F6), and records an explicit `None` for unresolvable segment refs so the later membership
validation names them instead of a raw `KeyError` (L15-FIX-1); the dry-run paths lock with
`create=False` so a preview never writes the controlplane lock file (F2).

`enforce_execution_topology_edit`
guards ordinary `create`, `replace`, and relevant `set_field` calls so partial graph/nature edits do
not create an invalid topology: a graph-less sprint has no topology contract to validate (the
series lane serializes masters), and dropping an authored `executionGraph` through an ordinary
write is refused — a graph is only ever retired through the graph-authoring seam. Since 260815-DAG-L15
the enforcement also runs the served-build preflight when `_edit_emits_topology_schema` detects the
edit writes topology schema bytes (`orchestrates`/`executionGraph`/`executionNature` present, or a
`set_field` touching them) — an edit that cannot change the schema's readability skips the gate (L15-R4).

### Invariants And Boundaries

- Legacy documents stay readable so graph authoring can inspect them; this module does not infer an
  execution nature or graph — a graph-less sprint runs the atomic-sequential default instead.
- Graph membership must exactly match the sprint's canonical `orchestrates` membership; atomic-nature
  masters admit lump nodes only, and the graph schema plus topology validation both refuse segment
  nodes on them (the node-kind rule lives once in `tasks/document_refs.py`).
- An authored `executionGraph` is never removed through ordinary document writes.
- Topology-schema writes are preflighted: a serving build that cannot parse the topology schema
  refuses before any publication, and a dry-run preview never writes the integration-authority
  lock file (L15-R4/F2).
- Preview is read-only. Apply prepares and publishes every affected document as one rollback-safe
  batch across task roots.
- Graph-title preparation has one application owner. This module neither selects a first graph nor
  retains its former private batch-title helper.
- Errors use the shared `AgentsRememberError` family and are translated to `TaskDocError` at the
  MCP application boundary.

## Evidence

### Repo-Internal References

- The incremental authoring operation applies one validated judgment-provenanced mutation batch and bootstraps graph-less sprints. [1]
- Claimed judgment ids resolve against the sprint's canonical Judgment Register (since 260815-DAG-L14 `_verify_authoring_judgments` delegates to the extracted shared `verify_sprint_judgment_ids`, also used by the sprint linkage operations). [2]
- Writes refuse unknown-leaf or incomplete segment partitions against the live leaf sets. [3]
- The read-only inventory previews every sprint and commanded master's proposed nature and blockers. [4]
- Ordinary execution-topology edits are validated against canonical cross-document topology; graph-less sprints skip graph validation and authored graphs cannot be dropped. [5]
- The served-build preflight refuses a topology write whose serving runtime cannot parse the schema (model self-probe + non-editable wheel floor). [6]
- A move whose leaf samples an edge endpoint refuses with the named retargets-edge cause before any acyclicity check (L15-R8 F3). [7]
- The draft node-kind scan runs before graph construction; unresolvable segment refs record an explicit `None` so membership validation names them (L15-R8 F6, L15-FIX-1). [8]
- The edit preflight fires only for edits that emit topology schema bytes (L15-R4). [9]

| The authoring suite proves mutation dispatch, judgment provenance, partition refusal, and previews. | `ExecutionGraphAuthoringTests` | mcp/tests/test_author_execution_graph.py:57-982; mcp/tests/test_author_execution_graph.py:53-53 |
| Preview and apply both route graph cardinality/title preparation through the central application owner. | `author_execution_graph` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:201-284 |
| The central owner provides the zero/one assertion and exact in-memory join. | `require_single_graph_document`; `build_publication_batch_graph_titles` | mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py:16-33; mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py:36-48 |

## 260815-DAG-L9 Inventory Boundary

`inventory_execution_topology` enumerates every persistent orchestration sprint and commanded
master before graph authoring, without writing. It proposes the explicit nature (atomic when an
`ar/<slug>` branch already backs the master, organizational otherwise) and reports the sprint
graph state plus declared completion blockers. Proposed edges are always parallel and left for
a strategist/orchestrator ruling; branch-backed detection runs through `run_git branch` and
refuses on enumeration failure.

## Current Sprint Publication Boundary

Execution-topology authoring publishes through `TaskDocPublicationTransaction` and the task-first
mutation owner. The complete changed scope is invalidated with task truth under one CAS, and
waiting projections rebuild afterward. `require_commanded_masters_completed` still validates the
exact canonical graph and refuses a sprint terminal status when any commanded master is not
`Completed` or still has completion blockers.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.


## 260815-DAG-L12 Title Threading

Graph authoring publication labels the sprint's Mermaid render from the exact in-memory authoring
batch. DAGQC L1 removes the private `_authoring_batch_titles` first-graph selector:
`build_publication_batch_graph_titles` now asserts zero/one graph-bearing document and produces the
single title context used by `_publish_authoring`; the dry-run invokes the same owner before
transaction validation. A batch without a graph produces no title context.


## 260815-DAG-L15 Authoring Dialect and Served-Build Preflight

L15 (hygiene sweep + playthrough dispositions) hardened the authoring seam: (1) served-build
preflight before any topology-schema write (L15-R4 — model self-probe + non-editable wheel floor
`3.0.0rc8`, wired into `author_execution_graph` and `enforce_execution_topology_edit` when
`_edit_emits_topology_schema`); (2) optional-at-parse `judgmentId` with the typed
`task-execution-graph-judgment-required` refusal (F5); (3) the named `move-retargets-edge` refusal
before acyclicity (F3); (4) the draft node-kind check before graph construction (F6) with the
`None`-recording unresolvable-ref branch (L15-FIX-1, closing the raw `KeyError`); (5) `create=False`
locking on the dry-run paths (F2). Refusals stay typed and fail-closed; nothing here weakens the
apply-path authority (apply re-locks).


## Current Contract After CLIVE

The current source seams include `ExecutionTopologyError`, `ExecutionTopologyAuthoringRequest`,
and `ExecutionTopologyEditRequest`. Accepted-source transactional publication no longer makes task
authoring subordinate to queue state: task truth publishes first, the affected queue projection is
invalidated, and current waiting-door facts rebuild it. DAGQC L1 adds the central graph-cardinality
and title-context precondition without changing that ownership.

### Reconciled Source Evidence

- The current module exposes `ExecutionTopologyError`, `ExecutionTopologyAuthoringRequest`, `ExecutionTopologyEditRequest` at this ownership boundary. [10]
