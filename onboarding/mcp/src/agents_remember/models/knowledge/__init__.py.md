# mcp/src/agents_remember/models/knowledge/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash |  `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate |  2026-09-15T22:46:24+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The package facade for the knowledge vocabulary. It re-exports every served knowledge shape — repository
namespace, invariant identity and revision aggregate, the sealed digest helpers, the source and locator
vocabulary, the typed operation requests/refusals/results and the schema identity — so a consumer imports
one module path and names one vocabulary.

## Code Commentary

### Logic

The file is a re-export barrel plus `__all__`. It imports from `agents_remember.models.knowledge.authorship`
(`ACCEPTED_STATE`, `PROPOSED_STATE`, `Authorship`, `KnowledgeState`), `.context`
(`KNOWLEDGE_SCHEMA_NAME`, `AdmittedKnowledgeDestination`, `KnowledgeSchemaIdentity`), `.digest`
(`REVISION_PAYLOAD_VERSION`, `canonical_revision_payload`, `revision_payload_digest`, `sealed_revision`),
`.invariant` (`InvariantDraft`, `InvariantIdentity`, `InvariantRevision`, `StoredInvariantRevision`),
`.repository` (`RepositoryIdentity`), `.result` (the requests, results, `KnowledgeOperation`,
`KnowledgeRefusal`, `KnowledgeRefusalCode`) and `.source` (`FileLocator`, `GitBlobIdentity`,
`LineRangeLocator`, `SourceAnchor`, `SourceIdentity`, `SourceLocator`, `SymbolLocator`).

`__all__` is explicit and sorted, so the served surface is a declared list rather than "whatever the
submodules happen to export".

### Conventions

Every name in `__all__` comes from a submodule; this file defines nothing of its own and holds no SQL, no
authorization decision and no storage behaviour. Literal vocabularies that decide something (`KnowledgeState`,
`KnowledgeOperation`, `KnowledgeRefusalCode`, `REVISION_PAYLOAD_VERSION`, `KNOWLEDGE_SCHEMA_NAME`) are defined
in their owning submodule and imported by the decider, never defined by the decider and imported back down.

### Invariants And Boundaries

- This package is the shared vocabulary of the knowledge substrate; `memory/knowledge` writes it and
  `application/knowledge.py` composes it. Owners ranked below `memory` receive these values rather than
  importing the storage package.
- Adding a name here is a served-surface change: a reader that imports the facade is entitled to assume the
  re-export list is the contract.
- Nothing here imports `memory.knowledge`; the direction is vocabulary first, storage second.

### Todos

None recorded. Later leaves extend the vocabulary in its owning submodules and re-export here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below cite the submodules this facade re-exports and the two consumers of the vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The facade's re-export list is the served knowledge vocabulary: authors, states, context, digest helpers, invariant shapes, repository identity, results and source locators. | `__all__` | mcp/src/agents_remember/models/knowledge/__init__.py:55-88 |
| The storage owner writes these values rather than defining its own copies. | `OpenedKnowledgeStore` | mcp/src/agents_remember/memory/knowledge/store.py:83-101 |
| The composition seam admits a destination and a revision request built from this vocabulary. | `admitted_knowledge_destination`; `admitted_revision_request` | mcp/src/agents_remember/application/knowledge.py:69-101 |
| The shared branching fixture authors its drafts from these same models. | `build_branching_knowledge_fixture` | mcp/tests/knowledge_fixture_test_support.py:90-133 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new knowledge-vocabulary facade. It records the served surface as the explicit `__all__` re-export list and the ownership rule that literal vocabularies are defined in their owning submodule and imported by the decider. Verification metadata remains empty until closeout stamps the code commit.
