# mcp/src/agents_remember/models/knowledge/context.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/context.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash |  `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate |  2026-09-17T22:32:32+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The declared schema name and its separation from SQLite's integer user version. | `KNOWLEDGE_SCHEMA_NAME` | mcp/src/agents_remember/models/knowledge/context.py:19-21 |
| The schema identity a store is opened as, including its structural fingerprint. | `KnowledgeSchemaIdentity` | mcp/src/agents_remember/models/knowledge/context.py:24-29 |
| The authorized-destination handle the store receives instead of a bare path. | `AdmittedKnowledgeDestination` | mcp/src/agents_remember/models/knowledge/context.py:32-37 |
| The schema generation this name is validated against at open and on reopen. | `inspect_schema`; `create_or_validate_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:91-103; mcp/src/agents_remember/memory/knowledge/connection.py:88-108 |
| The application constructor that binds a resolved destination. | `admitted_knowledge_destination` | mcp/src/agents_remember/application/knowledge.py:69-85 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (correction of a generated entry, not a re-write of it): the 2026-09-17T06:49:47 entry below records a citation repair that "repointed" `inspect_schema`; `create_or_validate_schema` to `connection.py:106-121` and `connection.py:91-103`. Those ranges were already stale when they were written — neither holds the construct it names — and this leaf's change moved both again, so the entry's *stated targets are inaccurate even though its claim of no content impact is right*. The ranges in the citation rows themselves are now re-derived against the working tree (`connection.py:111-128` for `inspect_schema`, `connection.py:88-108` for `create_or_validate_schema`). The historical entry is left in place because history here is append-only; this line exists so a later reader does not treat its targets as verified. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `inspect_schema`; `create_or_validate_schema` repointed to mcp/src/agents_remember/memory/knowledge/connection.py:106-121; mcp/src/agents_remember/memory/knowledge/connection.py:91-103. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new schema-identity and admitted-destination vocabulary. It records that the destination is a typed handle conferring no authority. Verification metadata remains empty until closeout stamps the code commit.
