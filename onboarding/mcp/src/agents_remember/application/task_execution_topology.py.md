# mcp/src/agents_remember/application/task_execution_topology.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_execution_topology.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T08:55+02:00 |
| lastVerifiedCommitHash | `f2e2f4b9c18d89cc0f5c901f43831e014701aae0` |
| lastVerifiedCommitDate | 2026-08-19T11:32:36+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Own the application policy for an explicit sprint execution topology. It validates edits against
the canonical task-document graph, provides the finite, previewable migration that writes one
sprint graph plus every commanded master's declared execution nature as one atomic generation
(lump nodes only — the bootstrap), and — since 260815-DAG-L11 — the incremental
`author_execution_graph` operation that applies one validated, judgment-provenanced batch of
structural mutations (add/remove node, add/remove edge, move leaf, set nature) to an already
migrated sprint's graph.

## Code Commentary

### Logic

`migrate_execution_topology` validates the closed migration payload, resolves every canonical
master reference, constructs the sprint and master candidates, proves exact graph membership and
acyclicity through `TaskDocumentTopology`, and either returns per-document render diffs or publishes
all JSON/Markdown pairs through the cross-root batch writer. `enforce_execution_topology_edit`
guards ordinary `create`, `replace`, and relevant `set_field` calls so partial graph/nature edits do
not create an invalid topology. Migration validates the request envelope once and then constructs
only schema-preserving task-document updates; it does not retain an unreachable second validation
translation branch.

`author_execution_graph` (L11-R5) requires a migrated sprint, then plays the typed
`mutations` batch onto a `_GraphDraft` through the `_MUTATION_HANDLERS` dispatch: segments are
addressed by a sampling `leafId`, never named; `remove_node` refuses while an edge still touches
the node; `move_leaf` also places a leaf the master gained after authoring, and refuses to empty a
segment; `set_nature` targets only commanded masters. Judgment-bearing mutations (edges,
segmentation, nature reclassification) must carry a `judgmentId` that `_verify_authoring_judgments`
resolves against the sprint's canonical `Judgment Register (canonical judgment authority)` section —
a missing register is a typed refusal naming the section, an unknown row or a non
strategist/orchestrator author fails closed; the mechanism never invents a judgment. The prepared
candidate revalidates the whole graph, exact cross-document membership, and node-kind legality,
refuses unknown or unplaced leaf partitions (`_require_complete_partitions`), and reports
`leafPlacementFacts` plus `numberingHints` as facts. `dry_run` returns the rendered diff +
`wouldLose` preview without writing; apply publishes sprint plus nature-changed masters atomically
through the sprint queue's publication lane, exactly like migration.

### Invariants And Boundaries

- Legacy documents stay readable only so the explicit migration can inspect them; this module does
  not infer an execution nature or graph.
- Migration membership must exactly match graph nodes and the sprint's canonical `orchestrates`
  membership; migration authors lump nodes only.
- Atomic-nature masters admit lump nodes only; the graph schema and topology validation both
  refuse segment nodes on them.
- Preview is read-only. Apply prepares and publishes every affected document as one rollback-safe
  batch across task roots.
- Errors use the shared `AgentsRememberError` family and are translated to `TaskDocError` at the
  MCP application boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The migration validates, previews, and atomically publishes the sprint and commanded masters. | `migrate_execution_topology` | mcp/src/agents_remember/application/task_execution_topology.py:125-218 |
| The incremental authoring operation applies one validated judgment-provenanced mutation batch. | `author_execution_graph` | mcp/src/agents_remember/application/task_execution_topology.py:319-383 |
| Claimed judgment ids resolve against the sprint's canonical Judgment Register. | `_verify_authoring_judgments` | mcp/src/agents_remember/application/task_execution_topology.py:468-522 |
| Writes refuse unknown-leaf or incomplete segment partitions against the live leaf sets. | `_require_complete_partitions` | mcp/src/agents_remember/application/task_execution_topology.py:706-734 |
| The read-only inventory previews every sprint and commanded master's proposed nature and blockers. | `inventory_execution_topology` | mcp/src/agents_remember/application/task_execution_topology.py:899-963 |
| Ordinary execution-topology edits are validated against canonical cross-document topology. | `enforce_execution_topology_edit` | mcp/src/agents_remember/application/task_execution_topology.py:790-820 |
| The forcing suite proves migration, rollback, render, projection, and refusal behavior. | `ExecutionTopologyTests` | mcp/tests/test_task_execution_topology.py:198-317 |
| The authoring suite proves mutation dispatch, judgment provenance, partition refusal, and previews. | `ExecutionGraphAuthoringTests` | mcp/tests/test_author_execution_graph.py:56-391 |

## 260815-DAG-L9 Inventory Boundary

`inventory_execution_topology` enumerates every persistent orchestration sprint and commanded
master before migration, without writing. It proposes the explicit nature (atomic when an
`ar/<slug>` branch already backs the master, organizational otherwise) and reports the sprint
graph state plus declared completion blockers. Proposed edges are always parallel and left for
a strategist/orchestrator ruling; branch-backed detection runs through `run_git branch` and
refuses on enumeration failure.

## 260815-DAG-L3 Sprint Publication Boundary

Execution-topology migration now publishes through the sprint queue's completion/reopen WAL rather
than writing the task batch independently. `require_commanded_masters_completed` validates the
exact canonical graph and refuses a sprint terminal status when any commanded master is not
`Completed` or still has completion blockers.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

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
