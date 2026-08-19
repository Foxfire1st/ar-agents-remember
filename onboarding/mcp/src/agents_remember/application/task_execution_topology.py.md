# mcp/src/agents_remember/application/task_execution_topology.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_execution_topology.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
| governingOverview | `overview.md` |

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
segmentation, nature reclassification) must carry a `judgmentId` that `_verify_authoring_judgments`
resolves against the sprint's canonical `Judgment Register (canonical judgment authority)` section —
a missing register is a typed refusal naming the section (sprint creation scaffolds the empty
canonical registers, and the write path validates their shape), an unknown row or a non
strategist/orchestrator author fails closed; the mechanism never invents a judgment. The prepared
candidate revalidates the whole graph, exact cross-document membership, and node-kind legality,
refuses unknown or unplaced leaf partitions (`_require_complete_partitions`), and reports
`leafPlacementFacts` plus `numberingHints` as facts. `dry_run` returns the rendered diff +
`wouldLose` preview without writing; apply publishes sprint plus nature-changed masters atomically
through the sprint queue's publication lane.

`enforce_execution_topology_edit`
guards ordinary `create`, `replace`, and relevant `set_field` calls so partial graph/nature edits do
not create an invalid topology: a graph-less sprint has no topology contract to validate (the
series lane serializes masters), and dropping an authored `executionGraph` through an ordinary
write is refused — a graph is only ever retired through the graph-authoring seam.

### Invariants And Boundaries

- Legacy documents stay readable so graph authoring can inspect them; this module does not infer an
  execution nature or graph — a graph-less sprint runs the atomic-sequential default instead.
- Graph membership must exactly match the sprint's canonical `orchestrates` membership; atomic-nature
  masters admit lump nodes only, and the graph schema plus topology validation both refuse segment
  nodes on them.
- An authored `executionGraph` is never removed through ordinary document writes.
- Preview is read-only. Apply prepares and publishes every affected document as one rollback-safe
  batch across task roots.
- Errors use the shared `AgentsRememberError` family and are translated to `TaskDocError` at the
  MCP application boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The incremental authoring operation applies one validated judgment-provenanced mutation batch and bootstraps graph-less sprints. | `author_execution_graph` | mcp/src/agents_remember/application/task_execution_topology.py:182-247 |
| Claimed judgment ids resolve against the sprint's canonical Judgment Register. | `_verify_authoring_judgments` | mcp/src/agents_remember/application/task_execution_topology.py:340-367 |
| Writes refuse unknown-leaf or incomplete segment partitions against the live leaf sets. | `_require_complete_partitions` | mcp/src/agents_remember/application/task_execution_topology.py:594-623 |
| The read-only inventory previews every sprint and commanded master's proposed nature and blockers. | `inventory_execution_topology` | mcp/src/agents_remember/application/task_execution_topology.py:804-867 |
| Ordinary execution-topology edits are validated against canonical cross-document topology; graph-less sprints skip graph validation and authored graphs cannot be dropped. | `enforce_execution_topology_edit` | mcp/src/agents_remember/application/task_execution_topology.py:678-725 |
| The forcing suite proves authoring, bootstrap, rollback, render, projection, and refusal behavior. | `ExecutionTopologyTests` | mcp/tests/test_task_execution_topology.py:213-938 |
| The authoring suite proves mutation dispatch, judgment provenance, partition refusal, and previews. | `ExecutionGraphAuthoringTests` | mcp/tests/test_author_execution_graph.py:56-983 |

## 260815-DAG-L9 Inventory Boundary

`inventory_execution_topology` enumerates every persistent orchestration sprint and commanded
master before graph authoring, without writing. It proposes the explicit nature (atomic when an
`ar/<slug>` branch already backs the master, organizational otherwise) and reports the sprint
graph state plus declared completion blockers. Proposed edges are always parallel and left for
a strategist/orchestrator ruling; branch-backed detection runs through `run_git branch` and
refuses on enumeration failure.

## 260815-DAG-L3 Sprint Publication Boundary

Execution-topology authoring publishes through the sprint queue's completion/reopen WAL rather
than writing the task batch independently. `require_commanded_masters_completed` validates the
exact canonical graph and refuses a sprint terminal status when any commanded master is not
`Completed` or still has completion blockers.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: removed `migrate_execution_topology` — a graph-less
  sprint runs the atomic-sequential default, and `author_execution_graph` is now the bootstrap
  seam (empty draft, `bootstrapped: true`, exact membership plus explicit natures at final
  validation). `enforce_execution_topology_edit` skips graph validation for graph-less sprints and
  refuses to drop an authored `executionGraph` through ordinary writes; the missing-register
  refusal names the scaffolded-register/`set_section` repair. Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: added `author_execution_graph` — the incremental,
  judgment-provenanced structural mutation batch (add/remove node, add/remove edge, move_leaf,
  set_nature) over a migrated sprint graph, with typed refusals (missing Judgment Register section,
  unknown/unauthorized judgment, segment-on-atomic, incomplete partitions), dry-run diff/wouldLose
  preview, queue-serialized atomic publish, and `leafPlacementFacts`/`numberingHints` reporting;
  `migrate_execution_topology` remains the lump-only bootstrap. Verification remains closeout-owned.

- 2026-08-18T12:00:00+00:00 — 260815-DAG-L9: added `inventory_execution_topology` (read-only pre-migration
  enumeration with branch-backed atomic classification); verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: documented queue-serialized topology migration and
  exact commanded-master completion proof; verification remains closeout-owned.

- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: retained strict explicit
  migration while extending forcing proof across malformed request shapes, missing and wrong-kind
  targets, unresolved masters, and out-of-repository task roots. Removed only an unreachable
  second task-document validation translation after the migration envelope and source documents
  are already validated.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: ordinary master
  `create`/`replace` and identity-bearing `set_field` edits now revalidate every sprint whose
  alias resolution could change, including same-path master-to-leaf kind replacement; migration
  canonical-reference failures are normalized at the task-doc boundary, and previews expose each
  master reference with its declared nature.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: created for the explicit execution-topology
  authoring and finite migration application policy. Verification remains closeout-owned.
