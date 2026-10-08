# mcp/src/agents_remember/models/knowledge/context.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Declares the schema name and the structural identity of a knowledge SQLite shape:
`KNOWLEDGE_SCHEMA_NAME` plus `KnowledgeSchemaIdentity`.

## Code Commentary

### Logic

`KNOWLEDGE_SCHEMA_NAME = "ar-knowledge-sqlite/v1"` is the application-owned schema version string, kept
separate from SQLite's own integer `user_version` so a reader names the shape it expects instead of comparing
bare numbers. `KnowledgeSchemaIdentity` carries `schema_name` (bounded by `LABEL_MAX_LENGTH`), `user_version`
(`ge=1`) and `fingerprint`, the structural identity a reader records for the shape it opened.

### Conventions

The module holds declared data only: no path, authority, admission or write destination. A store's open-time
schema validation lives in `memory/knowledge/connection.py`, which compares the declared name and the structural
identity against the shape it actually opens.

### Invariants And Boundaries

- The schema name is a declared constant rather than a derived string, so a store that opens a different
  generation is detected instead of described.
- The identity is the open-time statement of the shape: name, integer user version and structural fingerprint.
- The module confers no authority by itself and holds no durable state; a later schema check is what refuses a
  mismatched generation.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The declared schema name and its separation from SQLite's integer user version. [1]
- The schema identity a store is opened as, including its structural fingerprint. [2]
- The schema generation this name is validated against at open and on reopen. [4]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
