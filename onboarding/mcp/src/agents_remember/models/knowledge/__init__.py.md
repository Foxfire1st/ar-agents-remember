# mcp/src/agents_remember/models/knowledge/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash |  `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate |  2026-09-16T08:41:27+02:00|
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
(`FAMILY_REVISION_PAYLOAD_VERSION`, `REVISION_PAYLOAD_VERSION`, `canonical_family_revision_payload`,
`canonical_revision_payload`, `family_revision_payload_digest`, `revision_payload_digest`,
`sealed_family_revision`, `sealed_revision`), `.family` (`FamilyDraft`, `FamilyIdentity`, `FamilyRevision`,
`FamilyRevisionDraft`, `StoredFamilyRevision`), `.graph` (`AnchorRealizations`, `FamilyMember`,
`FamilyMemberDraft`, `FamilyMembers`, `InvariantFamilies`, `RealizationClaim`, `RealizationClaimDraft`,
`RealizationClaims`, `RealizationRole`, `UNCLASSIFIED_ROLE`), `.invariant` (`InvariantDraft`,
`InvariantIdentity`, `InvariantRevision`, `StoredInvariantRevision`), `.repository` (`RepositoryIdentity`),
`.result` (the requests, results, `KnowledgeOperation`, `KnowledgeRefusal`, `KnowledgeRefusalCode`) and
`.source` (`FileLocator`, `GitBlobIdentity`, `LineRangeLocator`, `SourceAnchor`, `SourceAnchorDraft`,
`SourceIdentity`, `SourceLocator`, `SymbolLocator`).

`__all__` is explicit and sorted, so the served surface is a declared list rather than "whatever the
submodules happen to export".

The graph half added its own names to that list — the family shapes, the two relation shapes and their read
models, the authored role vocabulary with `UNCLASSIFIED_ROLE`, the eight graph operations' requests and results,
and the anchor endpoint union. They are re-exported, not defined, here.

The facade deliberately does **not** export `require_stored_outcome`, `require_removal_outcome`,
`require_consistent_acceptance`, `SqliteFailureContext`, `RefusalFacts` or `KnowledgeStorageError`. Those are
internal rules and internal control flow; a consumer that branches on a refusal branches on the returned
`KnowledgeRefusal` value, not on the machinery that builds it.

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
| The facade's re-export list is the served knowledge vocabulary: authors, states, context, both payload versions and their sealing helpers, family shapes, relation shapes and read models, invariant shapes, repository identity, results and source locators. | `__all__` | mcp/src/agents_remember/models/knowledge/__init__.py:98-170 |
| The internal rules deliberately kept off the served surface. | `require_stored_outcome`; `require_removal_outcome`; `require_consistent_acceptance` | mcp/src/agents_remember/models/knowledge/result.py:85-100; mcp/src/agents_remember/models/knowledge/result.py:102-111; mcp/src/agents_remember/models/knowledge/base.py:40-56 |
| The storage owner writes these values rather than defining its own copies — re-cited against the working tree, where the class docstring now names the sibling graph owners. | `OpenedKnowledgeStore` | mcp/src/agents_remember/memory/knowledge/store.py:86-104 |
| The composition seam admits a destination and builds every graph request from this vocabulary. | `admitted_knowledge_destination`; `admitted_revision_request`; `admitted_family_request`; `admitted_claim_request` | mcp/src/agents_remember/application/knowledge.py:106-124; mcp/src/agents_remember/application/knowledge.py:125-140; mcp/src/agents_remember/application/knowledge.py:213-225; mcp/src/agents_remember/application/knowledge.py:260-274 |
| The shared branching fixture authors its identity and graph halves from these same models. | `build_branching_knowledge_fixture`; `BranchingKnowledgeFixture` | mcp/tests/knowledge_fixture_test_support.py:203-263; mcp/tests/knowledge_fixture_test_support.py:161-188 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): recorded the graph half's additions to the served surface (family shapes, relation shapes and their read models, the authored role vocabulary with `UNCLASSIFIED_ROLE`, the eight operations' requests and results, the anchor endpoint union, the family payload version and its sealing helpers) and the names the facade deliberately keeps off it (the two outcome rules, the acceptance rule, `SqliteFailureContext`, `RefusalFacts`, `KnowledgeStorageError`). This remains a re-export barrel: it defines nothing of its own and must not become an owner of validation. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new knowledge-vocabulary facade. It records the served surface as the explicit `__all__` re-export list and the ownership rule that literal vocabularies are defined in their owning submodule and imported by the decider. Verification metadata remains empty until closeout stamps the code commit.
