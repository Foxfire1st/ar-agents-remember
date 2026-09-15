# mcp/src/agents_remember/application/knowledge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash | `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate | 2026-09-15T22:46:24+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

The composition seam between admitted authority and the concrete knowledge store. This is where a destination
becomes an authorized handle and where the required provenance envelope is actually assigned.

## Code Commentary

### Logic

`write_authorship` builds the `Authorship` envelope for one admitted write and **assigns** `operation_id` (a fresh
`uuid4`) and `recorded_at` (UTC now, unless the caller passes one) rather than accepting them from the payload.

`admitted_knowledge_destination` is the constructor the admitted authority path calls after its own checks; it
binds a resolved `database_path`, the `RepositoryIdentity` and an `Authorship` into an
`AdmittedKnowledgeDestination`.

`admitted_revision_request` attaches one authored `RevisionDraft` to its destination: the caller supplies what was
authored, while the repository identity and the provenance envelope come from the destination.

`initialize_knowledge_namespace` refuses an **occupied** destination outright with `destination_occupied` (an
existing path is a resume attempt, never permission to initialize over it), otherwise opens the store, calls
`create_repository` and closes it in a `finally`.

`open_admitted_knowledge_store` opens for reads only, without creating or repairing, and documents that the caller
owns the returned store and must close it.

`create_knowledge_revision` opens the admitted destination and delegates to `OpenedKnowledgeStore.create_revision`,
closing in a `finally`. It refuses rather than repairs: a foreign namespace, an identity reuse, a lineage
violation and an unrecognized schema all return a typed refusal with the row count unchanged.

`__all__` declares the six served functions.

### Conventions

The direction matters and the module docstring states it: storage ranks below application, and the worktree and
memory-quality owners rank below storage, so a lower owner receives `models.knowledge` values — never an import of
this module or of the store. This module is the only place the admitted authority and the concrete store are
wired together. It holds no schema and no durable state: it admits, delegates and returns the typed result
unchanged.

### Invariants And Boundaries

- Provenance is **not a parameter**: `admitted_revision_request` overwrites the draft's provenance from the
  destination, so a request cannot claim an actor or an authorization the admission did not establish.
- No acceptance or promotion operation exists anywhere in this module: the store manufactures no acceptance, and
  `state_at_origin` plus `acceptance_ref` remain authored data.
- Every opened store is closed in a `finally`; the read path returns the caller-owned store deliberately so a
  multi-read flow does not pay a reopen per read.
- This module is the only permitted consumer of `memory.knowledge` (rank 12) from `application` (rank 21); the
  layer direction is verified by a focused test, so a later reverse import fails a check rather than passing
  review.

### Todos

None recorded. The admitted-authority path that calls `admitted_knowledge_destination` is the next leaf's
composition work; this leaf exposes the seam and proves it with a focused test.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The provenance envelope is assigned here, not accepted from the payload. | `write_authorship` | mcp/src/agents_remember/application/knowledge.py:46-66 |
| The admitted-destination constructor that confers no authority by itself. | `admitted_knowledge_destination` | mcp/src/agents_remember/application/knowledge.py:69-85 |
| Provenance and namespace come from the destination, so a request cannot assert them. | `admitted_revision_request` | mcp/src/agents_remember/application/knowledge.py:88-101 |
| Initialization refuses an occupied destination as a resume attempt. | `initialize_knowledge_namespace` | mcp/src/agents_remember/application/knowledge.py:104-134 |
| The read open and the delegating insert, both closing in a `finally`. | `open_admitted_knowledge_store`; `create_knowledge_revision` | mcp/src/agents_remember/application/knowledge.py:137-165 |
| The store operation this seam delegates to. | `create_revision` | mcp/src/agents_remember/memory/knowledge/store.py:212-241 |
| The layer charter that keeps this composition one-directional. | "[package.memory]" | layers.toml:206-222 |
| The focused case that proves the seam and the layer direction. | `test_application_seam_initializes_and_extends_one_namespace`; `test_lower_ranked_owners_do_not_import_the_memory_domain` | mcp/tests/test_knowledge_store.py:696-767 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new application composition seam. It records that provenance is assigned rather than parameterized, that initialization refuses an occupied destination, and that no acceptance/promotion operation exists. Verification metadata remains empty until closeout stamps the code commit.
