# mcp/src/agents_remember/application/task_docs/task_execution_topology.py

## Governing Overview

[overview](overview.md)

## Purpose

Own the application policy for an explicit sprint execution topology. It validates edits against
the canonical task-document graph and provides `author_execution_graph` — the
incremental operation that applies one validated, judgment-provenanced batch of structural
mutations (add/remove node, add/remove edge, move leaf, set nature), and also
the bootstrap seam: the first `add_node` batch on a graph-less sprint creates the graph. A
graph-less sprint is not an
error — it runs the atomic-sequential default until a graph is authored.

## Code Commentary

### Logic

`author_execution_graph` plays the typed
`mutations` batch onto a `_GraphDraft` through the `_MUTATION_HANDLERS` dispatch. The mutation models, the
draft, the handlers (`_apply_add_node` through `_apply_set_nature`), `_require_move_does_not_retarget_edge`
and `ExecutionTopologyError` are defined in `task_execution_graph_mutations.py`, the one candidate
mutation engine that graph authoring and master retirement share; this module imports them. Segments are
addressed by a sampling `leafId`, never named; `remove_node` refuses while an edge still touches
the node; `move_leaf` also places a leaf the master gained after authoring, and refuses to empty a
segment; `set_nature` targets only commanded masters. On a graph-less sprint the draft starts empty
and commanded membership comes from the canonical `orchestrates` aliases; the result reports
`bootstrapped: true`, and final validation requires exact membership plus an explicit nature for
every commanded master (a `set_nature` mutation in the same batch covers a master document that
lacks one). Judgment-bearing mutations (edges,
segmentation, nature reclassification) must carry a `judgmentId` that `_verify_authoring_judgments` (which delegates to the shared
`verify_sprint_judgment_ids` — also used by the sprint linkage operations — so the graph-authoring
and attach paths verify judgment provenance through one function)
resolves against the sprint's canonical `Judgment Register (canonical judgment authority)` section —
a missing register is a typed refusal naming the section (sprint creation scaffolds the empty
canonical registers, and the write path validates their shape), an unknown row or a row not
authored by the architect or orchestrator fails closed; the mechanism never invents a judgment. The prepared
candidate revalidates the whole graph, exact cross-document membership, and node-kind legality,
refuses unknown or unplaced leaf partitions (`_require_complete_partitions`), and reports
`leafPlacementFacts` plus `numberingHints` as facts. `dry_run` returns the rendered diff +
`wouldLose` preview without writing; apply publishes sprint plus nature-changed masters atomically
through the task-first publication transaction. Both preview and apply invoke the shared
`build_publication_batch_graph_titles` owner before their transaction boundary, so unsupported
multi-graph input refuses and the exact in-memory batch supplies the sole title context.

Every topology-schema write is preflighted against the serving runtime
(`require_serving_topology_schema` from `tasks/serving_preflight.py`): `author_execution_graph`
refuses with `ExecutionTopologyError` when the running build's `TaskDocument` model lacks the
topology fields; the check is a model self-probe and consults no installed distribution version.
The authoring dialect keeps refusals typed: `judgmentId` is optional at parse on the edge/move/nature
mutations so a missing judgment surfaces the typed `task-execution-graph-judgment-required`
refusal instead of a raw pydantic error; `_require_move_does_not_retarget_edge` refuses a
`move_leaf` whose leaf samples an edge endpoint with the named `task-execution-graph-move-retargets-edge`
before any acyclicity check; `_require_draft_node_kinds` runs before `SprintExecutionGraph`
construction so the atomic segment-node-kind rule fires before the lump/segment mutual-exclusion
mask, and records an explicit `None` for unresolvable segment refs so the later membership
validation names them instead of a raw `KeyError`; the dry-run paths take no lock and publish
nothing.

`enforce_execution_topology_edit`
guards ordinary `create`, `replace`, and relevant `set_field` calls so partial graph/nature edits do
not create an invalid topology: a graph-less sprint has no topology contract to validate (the
series lane serializes masters), and dropping an authored `executionGraph` through an ordinary
write is refused — a graph is only ever retired through the graph-authoring seam. The
enforcement also runs the served-build preflight when `_edit_emits_topology_schema` detects the
edit writes topology schema bytes (`orchestrates`/`executionGraph`/`executionNature` present, or a
`set_field` touching them) — an edit that cannot change the schema's readability skips the gate.

### Invariants And Boundaries

- Legacy documents stay readable so graph authoring can inspect them; this module does not infer an
  execution nature or graph — a graph-less sprint runs the atomic-sequential default instead.
- Graph membership must exactly match the sprint's canonical `orchestrates` membership; atomic-nature
  masters admit lump nodes only, and the graph schema plus topology validation both refuse segment
  nodes on them (the node-kind rule lives once in `tasks/document_refs.py`).
- An authored `executionGraph` is never removed through ordinary document writes.
- Topology-schema writes are preflighted: a serving build that cannot parse the topology schema
  refuses before any publication, and a dry-run preview takes no lock and writes nothing.
- Preview is read-only. Apply prepares and publishes every affected document as one rollback-safe
  batch across task roots.
- Graph-title preparation has one application owner. This module does not select a first graph
  itself.
- Errors use the shared `AgentsRememberError` family and are translated to `TaskDocError` at the
  MCP application boundary.

## Evidence

### Repo-Internal References

- The incremental authoring operation applies one validated judgment-provenanced mutation batch and bootstraps graph-less sprints. [1]

- Claimed judgment ids resolve against the sprint's canonical Judgment Register through the shared `verify_sprint_judgment_ids`, also used by the sprint linkage operations; only a row authored by the architect or orchestrator backs graph authoring. [2]

- Writes refuse unknown-leaf or incomplete segment partitions against the live leaf sets. [3]

- The read-only inventory previews every sprint and individual master's proposed nature and blockers. [4]

- Ordinary execution-topology edits are validated against canonical cross-document topology; graph-less sprints skip graph validation and authored graphs cannot be dropped. [5]


- The served-build preflight refuses a topology write whose serving runtime's `TaskDocument` model lacks the topology fields; it is a model self-probe and checks no installed version. [6]

- A move whose leaf samples an edge endpoint refuses with the named retargets-edge cause before any acyclicity check (L15-R8 F3). [7]
- The draft node-kind scan runs before graph construction; unresolvable segment refs record an explicit `None` so membership validation names them (L15-R8 F6, L15-FIX-1). [8]
- The edit preflight fires only for edits that emit topology schema bytes (L15-R4). [9]

- Preview and apply both route graph cardinality and title preparation through the central application owner. [11]
- The central owner provides the zero-or-one assertion and the exact in-memory title join. [12]
- The draft that the authoring handlers edit lives in the shared mutation engine. [13]
- The move handler refuses a move whose leaf samples an edge endpoint. [14]

## Inventory Boundary

`inventory_execution_topology` enumerates every persistent orchestration sprint and commanded
master before graph authoring, without writing. It proposes the explicit nature (atomic when an
`ar/<slug>` branch already backs the master, organizational otherwise) and reports the sprint
graph state plus declared completion blockers. Proposed edges are always parallel and left for
an accepted Architect or Orchestrator ruling; branch-backed detection runs through `run_git branch` and
refuses on enumeration failure.

## Current Sprint Publication Boundary

Execution-topology authoring publishes through `TaskDocPublicationTransaction` and the task-first
mutation owner. The complete changed scope is invalidated with task truth under one CAS, and
waiting projections rebuild afterward. `require_commanded_masters_completed` still validates the
exact canonical graph and refuses a sprint terminal status when any commanded master is not
`Completed` or still has completion blockers.

## Current Contract

The current source seams are `ExecutionTopologyAuthoringRequest` and `ExecutionTopologyEditRequest`
(defined here) and `ExecutionTopologyError` (defined in `task_execution_graph_mutations.py` and imported here). Accepted-source transactional publication keeps task
authoring independent of queue state: task truth publishes first, the affected queue projection is
invalidated, and current waiting-door facts rebuild it. The central graph-cardinality
and title-context precondition does not change that ownership.

### Reconciled Source Evidence

- The current module exposes `ExecutionTopologyError`, `ExecutionTopologyAuthoringRequest`, `ExecutionTopologyEditRequest` at this ownership boundary. [10]
