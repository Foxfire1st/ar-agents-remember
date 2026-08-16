# mcp/src/agents_remember/application/task_execution_topology.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_execution_topology.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Own the application policy for an explicit sprint execution topology. It validates edits against
the canonical task-document graph and provides the finite, previewable migration that writes one
sprint graph plus every commanded master's declared execution nature as one atomic generation.

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

### Invariants And Boundaries

- Legacy documents stay readable only so the explicit migration can inspect them; this module does
  not infer an execution nature or graph.
- Migration membership must exactly match graph nodes and the sprint's canonical `orchestrates`
  membership.
- Preview is read-only. Apply prepares and publishes every affected document as one rollback-safe
  batch across task roots.
- Errors use the shared `AgentsRememberError` family and are translated to `TaskDocError` at the
  MCP application boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The migration validates, previews, and atomically publishes the sprint and commanded masters. | `migrate_execution_topology` | mcp/src/agents_remember/application/task_execution_topology.py:67-129 |
| Ordinary execution-topology edits are validated against canonical cross-document topology. | `enforce_execution_topology_edit` | mcp/src/agents_remember/application/task_execution_topology.py:193-222 |
| The forcing suite proves migration, rollback, render, projection, and refusal behavior. | `ExecutionTopologyTests` | mcp/tests/test_task_execution_topology.py:107-317 |

## 260815-DAG-L3 Sprint Publication Boundary

Execution-topology migration now publishes through the sprint queue's completion/reopen WAL rather
than writing the task batch independently. `require_commanded_masters_completed` validates the
exact canonical graph and refuses a sprint terminal status when any commanded master is not
`Completed` or still has completion blockers.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

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
