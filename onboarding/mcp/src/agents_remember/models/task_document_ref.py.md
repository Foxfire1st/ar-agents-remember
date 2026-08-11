# mcp/src/agents_remember/models/task_document_ref.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/task_document_ref.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T20:28+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Models overview](overview.md)

## Purpose

Defines the one canonical, repository-qualified task-document reference used at sprint, master, and
leaf altitude. Paired with a role, it is the stable structural seat identity.

## Code Commentary

### Logic

`TaskDocumentRef` validates a repository segment and a confined, JSON-primary task path. The model
is frozen and hashes by `(repository, path)`, so equal references behave as immutable value keys.
Its `key` property is comparison/debug text, not a replacement identity exposed to agents.

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


## Update History

- 2026-08-11T20:28+02:00 — 260731-EFA-L19 closeout-gate repair: corrected the body to remove a
  nonexistent level field and recorded the explicit immutable-value hash over repository and path;
  verification metadata remains pending the real code commit.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created as the sole level-neutral task-document identity model.
