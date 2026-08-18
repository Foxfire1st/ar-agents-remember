# docs/reference/execution-topology-migration.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `docs/reference/execution-topology-migration.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-18 |
| lastVerifiedCommitHash | `e41ea31d6df3e35a92f526edef8420ae9bd56c57` |
| lastVerifiedCommitDate | 2026-08-18T19:37:20+02:00|
| governingOverview | `docs/reference/overview.md` |

## Governing Overview

[docs/reference/overview.md](overview.md)

## Purpose

Operator-facing cutover procedure for the explicit execution topology (`executionNature` on
commanded masters, `executionGraph` on orchestration sprints). The migration is finite and
explicit: a pre-migration snapshot is the rollback mechanism, and no runtime compatibility path
remains after cutover.

## Code Commentary

### Logic

The guide documents four steps: (1) a read-only inventory that proposes the explicit nature
(atomic when an `ar/<slug>` branch already backs the master, organizational otherwise) with
parallel edges pending a ruling; (2) the atomic `task_doc.migrate_execution_topology` write that
validates master set == graph nodes and authors the sprint graph plus each master nature; (3) the
post-cutover fail-closed refusal (`task-execution-topology-migration-required`) with no implicit
default; and (4) snapshot-based rollback that restores the pre-migration tree rather than
re-enabling a compatibility path.

### Invariants And Boundaries

- The inventory never infers edges from file order, names, or status.
- A branch recorded atomic is only reclassified by an accepted strategist/orchestrator ruling.
- Rollback restores the snapshot; it does not retain a dual-reader or feature-switch fallback.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-only inventory the guide documents. | `inventory_execution_topology` | mcp/src/agents_remember/application/task_execution_topology.py:333-396 |
| The atomic migration write the guide documents. | `migrate_execution_topology` | mcp/src/agents_remember/application/task_execution_topology.py:67-129 |
| Fail-closed validation of a sprint's commanded membership and natures. | `validate_execution_topology` | mcp/src/agents_remember/tasks/document_refs.py:194-240 |

## Update History

- 2026-08-18T12:00:00+00:00 — 260815-DAG-L9: created as the operator migration/rollback reference for the
  explicit execution-topology cutover. Verification remains closeout-owned.
