# mcp/src/agents_remember/models/task_document_ref.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/task_document_ref.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:36+02:00 |
| lastVerifiedCommitHash |  `17987fa66a642306eb8d20fa9a4bff2b881550d2`|
| lastVerifiedCommitDate |  2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Models overview](overview.md)

## Purpose

Defines the one canonical, repository-qualified task-document reference used at sprint, master, and
leaf altitude. Paired with a role, it is the stable structural seat identity.

## Code Commentary

### Logic

`TaskDocumentRef` validates a repository segment and a confined, JSON-primary task path. Explicit
post-normalization validators cap the canonical repository and path values without publishing a
`maxLength` keyword that the workspace-projection TypeScript generator cannot represent exactly.
The model is frozen and hashes by `(repository, path)`, so equal references behave as immutable
value keys. Its `key` property is comparison/debug text, not a replacement identity exposed to agents.

### Conventions

The path points at the real task document under `tasks/<repo>/...`; altitude is resolved from the
task-document topology rather than duplicated in this value model.

### Invariants And Boundaries

- A reference is canonical and repository-qualified.
- Equality and hashing use the two canonical identity components.
- It identifies work, not a runtime occupant.
- Seat identity is exactly `(TaskDocumentRef, role)`.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The frozen model validates, hashes, and serializes the canonical document reference. | `TaskDocumentRef` | mcp/src/agents_remember/models/task_document_ref.py:15-57 |
| Topology resolves the reference against real task documents. | `TaskDocumentTopology` | mcp/src/agents_remember/tasks/document_refs.py:26-252 |

## Cross-Repo References


## 260815-DAG-L3 Bounded Durable Identity

The canonical task-document reference bounds normalized repository identity to 128 characters and
its normalized repository-relative path to 4096 characters. Queue requests, state, graph nodes,
and durable WAL records can therefore reuse this identity without admitting unbounded persisted
input. These are runtime persistence bounds, not fictional TypeScript string-length types: the
shared JSON schema remains an ordinary string shape, while Pydantic refuses an oversized canonical
value before it can enter any queue or task-document record.

## Update History

- 2026-08-15T09:36+02:00 — L3 fast-hook repair: moved the two canonical length bounds from
  unrenderable JSON Schema `maxLength` keywords into explicit post-normalization validators. Runtime
  admission remains bounded and the generated TypeScript surface remains truthfully `string`.
- 2026-08-15T09:10+02:00 — L3 content update: recorded explicit repository/path bounds on the
  canonical task-document reference; verification remains closeout-owned.

- 2026-08-11T20:28+02:00 — 260731-EFA-L19 closeout-gate repair: corrected the body to remove a
  nonexistent level field and recorded the explicit immutable-value hash over repository and path;
  verification metadata remains pending the real code commit.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created as the sole level-neutral task-document identity model.
