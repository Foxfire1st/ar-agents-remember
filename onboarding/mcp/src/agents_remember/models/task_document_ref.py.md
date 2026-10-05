# mcp/src/agents_remember/models/task_document_ref.py

## Governing Overview

[Models overview](overview.md)

## Purpose

Defines the one canonical, repository-qualified task-document reference used at sprint, master, and
leaf altitude. Paired with a role, it is the stable structural seat identity.

Defines immutable repository-qualified task identity and per-call leaf reader context.

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

### Role Runtime and Scope

TaskScopedReaderContext is extra-forbid/frozen and carries task_document_ref plus contract_path. The path must be normalized absolute POSIX with no parent traversal; source roots are not fields. Preserve TaskDocumentRef equality/hash/length rules and its distinction from runtime occupant identity.

## Evidence

### Docs References


### Repo-Internal References

- The frozen model validates, hashes, and serializes the canonical document reference. [1]
- Topology resolves the reference against real task documents. [2]

### Cross-Repo References

### Runtime Source References

- Frozen implementation of TaskScopedReaderContext supporting the stated file behavior. [3]
- Frozen implementation of TaskDocumentRef supporting the stated file behavior. [4]

## 260815-DAG-L3 Bounded Durable Identity

The canonical task-document reference bounds normalized repository identity to 128 characters and
its normalized repository-relative path to 4096 characters. Queue requests, state, graph nodes,
and durable WAL records can therefore reuse this identity without admitting unbounded persisted
input. These are runtime persistence bounds, not fictional TypeScript string-length types: the
shared JSON schema remains an ordinary string shape, while Pydantic refuses an oversized canonical
value before it can enter any queue or task-document record.
