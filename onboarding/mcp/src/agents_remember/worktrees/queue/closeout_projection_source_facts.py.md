# mcp/src/agents_remember/worktrees/queue/closeout_projection_source_facts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection_source_facts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout queue overview](overview.md)

## Purpose

Defines the two explicit task-source planes used by closeout projection currentness: task address
plus completion-readiness fields, and the independent `semantic-topology/v2` fingerprint.

## Code Commentary

### Logic

`task_source_fact` projects only fields classified as completion-readiness and adds the exact task
address. `semantic_topology_source_fact` obtains the task-domain v2 fingerprint from the shared
bound graph context. A schema-taxonomy gap becomes `TaskSourceProjectionError` rather than causing
whole-document hashing or an implicit fallback.

### Conventions

- Public source-fact keys use the existing camelCase task-document wire convention.
- Schema version and topology fingerprint remain separate from task address and readiness fields.

### Invariants And Boundaries

- Complete task-document JSON is never serialized into projection currentness.
- Completion readiness and structural topology are separate named source planes.
- An unclassified schema field refuses source capture.
- No v1 topology shape or private whole-document table is retained.

### Todos

None.

## Docs References

No external source is required.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Task facts contain only address, presence, and schema-owned completion-readiness fields. | `task_source_fact` | mcp/src/agents_remember/worktrees/queue/closeout_projection_source_facts.py:27-42 |
| Semantic topology is emitted as a separate explicit v2 source plane. | `semantic_topology_source_fact` | mcp/src/agents_remember/worktrees/queue/closeout_projection_source_facts.py:44-68 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the explicit projection source-plane
  card. Verification remains closeout-owned.
