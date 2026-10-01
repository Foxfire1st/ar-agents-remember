# mcp/src/agents_remember/models/knowledge/context.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Declares the two runtime handles the storage operation receives: the schema generation a store was opened as
(`KNOWLEDGE_SCHEMA_NAME` plus `KnowledgeSchemaIdentity`) and the already-authorized
`AdmittedKnowledgeDestination`.

## Code Commentary

### Logic

`KNOWLEDGE_SCHEMA_NAME = "ar-knowledge-sqlite/v1"` is the application-owned schema version string, kept
separate from SQLite's own integer `user_version` so a reader names the shape it expects instead of comparing
bare numbers. `knowledge/store.py` writes `schema_name` into `KnowledgeSchemaIdentity` at every open, and
`memory/knowledge/schema.py` reports the matching fingerprint.

`KnowledgeSchemaIdentity` carries `schema_name` (bounded by `LABEL_MAX_LENGTH`), `user_version` (`ge=1`) and
`fingerprint`. `AdmittedKnowledgeDestination` carries `database_path`, the `RepositoryIdentity` namespace and the
`Authorship` envelope to be used for writes.

### Conventions

A destination is constructed through `application.knowledge.admitted_knowledge_destination` after the
application's own authority checks. The model deliberately carries no `authorized: bool` and no self-asserted
authority: a deserialized request cannot mint one by claiming to be authorized.

### Invariants And Boundaries

- The schema name is a declared constant rather than a derived string, so a store that opens a different
  generation is detected instead of described.
- `AdmittedKnowledgeDestination` is a typed runtime handle; it confers no authority by itself and holds no
  durable state.
- The destination's `repository` is the single source of the namespace used by every read and write through the
  opened store, so a request addressed elsewhere is refusable by comparison rather than by trust.

### Todos

None recorded. `AdmittedKnowledgeDestination` is the seam later leaves extend for read/diff surfaces.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The declared schema name and its separation from SQLite's integer user version. [1]
- The schema identity a store is opened as, including its structural fingerprint. [2]
- The authorized-destination handle the store receives instead of a bare path. [3]
- The schema generation this name is validated against at open and on reopen. [4]
- The application constructor that binds a resolved destination. [5]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
