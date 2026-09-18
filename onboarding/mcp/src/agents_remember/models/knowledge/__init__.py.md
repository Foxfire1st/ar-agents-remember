# mcp/src/agents_remember/models/knowledge/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash |  `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate |  2026-09-18T09:42:44+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../overview.md)

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
`.result` (the requests, results, `KnowledgeOperation`, `KnowledgeRefusal`, `KnowledgeRefusalCode`),
`.read` (the selective read's whole vocabulary, added by 260915-KS-L7 — see below) and
`.source` (`FileLocator`, `GitBlobIdentity`, `LineRangeLocator`, `SourceAnchor`, `SourceAnchorDraft`,
`SourceIdentity`, `SourceLocator`, `SymbolLocator`).

**`.snapshot` is the eighth source this leaf added**: the local candidate layout (`CANDIDATE_DATABASE_NAME`,
`CANDIDATE_RECEIPT_NAME` and the two path builders), the receipt and its sealing helpers
(`CANDIDATE_RECEIPT_VERSION`, `CandidateReceiptVersion`, `CandidateReceipt`, `build_candidate_receipt`,
`receipt_digest`), the lifecycle value objects (`AdmittedCandidateDestination`, `CandidateBaseline`,
`CandidateResult`), the publication vocabulary (`PreparedKnowledgeSnapshot`, `SnapshotDestinationRequest`,
`PublishSnapshotRequest`, `SnapshotPublicationResult`, `PublicationState`) and the closed disposal union
(`DiscardCandidate`, `PublishedCandidate`, `CandidateDisposition`, `CandidateDisposalResult`). Every one of
those names is now in `__all__`.

**`.read` is the ninth source, added by 260915-KS-L7**, and it is the one addition to this facade the
selective recorded-scope read makes: the five seed kinds (`PathSeed`, `InvariantIdentitySeed`,
`InvariantRevisionSeed`, `FamilyIdentitySeed`, `FamilyRevisionSeed`) and their union `KnowledgeReadSeed`, the
context and budget (`KnowledgeReadContext`, `KnowledgeReadBudget`), the request and its result
(`KnowledgeReadRequest`, `KnowledgeReadResult`), the page and its counting (`KnowledgeReadPage`,
`KnowledgeReadCounts`), the grouping and frontier models (`ReadItem`, `ReadRevisionGroup`,
`AdvertisedExpansion`, `AnchorResolution`, `KnowledgeReadSnapshot`), the policy constant
(`KNOWLEDGE_READ_POLICY_VERSION`) and the cursor helpers (`KnowledgeReadCursor`, `cursor_for`,
`continue_from_cursor`, `read_context_digest`, `seed_digest`, `snapshot_of_context`). Every one of those names
is in `__all__`.

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

### The Composition Vocabulary Joins The Served Surface (260915-KS-L17)

This leaf added **one more source module** to the facade and, with it, the whole authored-composition
vocabulary: `models/knowledge/composition.py`, re-exported name by name and listed in `__all__`. The
names are the closed command kinds and record tables the composition write path publishes
(`COMPOSITION_COMMAND_KINDS`, `COMPOSITION_WRITABLE_TABLES`), the one registered review scope a
traversal policy may widen (`REGISTERED_REVIEW_SCOPE`, `WidenedScope`) and the closed direction
vocabulary (`FOLLOW_DIRECTIONS`, `FollowDirection`), the policy draft and stored version
(`FamilyCompositionPolicyDraft`, `FamilyCompositionPolicyVersion`, `PolicyIdentity`), the edge and its
draft (`FamilyComposition`, `FamilyCompositionDraft`), the reported link (`FamilyCompositionLink`) and
the authored explanatory context with its draft (`FamilyExplanationContext`,
`FamilyExplanationContextDraft`, `FamilyExplanationContextRevision`).

**Two of the shared unions this facade re-exports grew in the same change**, and this card's own rows
record both: `KnowledgeOperation` gained `create_composition` and `set_family_revision_route` (the
operations a *relation write* reports when it is reached directly) and `follow_family_composition` (the
one act that is **not** a write — following declared composition edges under a versioned traversal
policy, which is a different operation from `read_knowledge_scope`'s retrieval selection rather than a
variant of it). The operation union therefore measures **forty-four** members on the merged line while
the refusal-code union is unchanged at **forty-five**: this leaf minted no new refusal code and reuses
the shipped ones through three new factories in `memory/knowledge/refusals.py`.

**The counts in this card are measurements, not constants.** `KnowledgeOperation` is counted from the
literal in `models/knowledge/result.py`; `ProposedCommand` is the discriminated union a batch's
commands travel under and then held **twenty-two** variants after this leaf's four composition kinds
joined the eighteen it held before. A later leaf that appends to either union re-counts from the
declaration rather than editing a number here.

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
| The facade's re-export list is the served knowledge vocabulary: authors, states, context, both payload versions and their sealing helpers, family shapes, relation shapes and read models, invariant shapes, repository identity, results, source locators, the whole snapshot vocabulary and — since this leaf — the composition vocabulary. | `__all__` | mcp/src/agents_remember/models/knowledge/__init__.py:160-288 |
| The eighth source module this leaf added to the facade, re-exported name by name. | `build_candidate_receipt`; `candidate_database_path`; `candidate_receipt_path`; `receipt_digest` | mcp/src/agents_remember/models/knowledge/__init__.py:144-144; mcp/src/agents_remember/models/knowledge/snapshot.py:58-62; mcp/src/agents_remember/models/knowledge/snapshot.py:64-67; mcp/src/agents_remember/models/knowledge/snapshot.py:144-148 |
| The internal rules deliberately kept off the served surface. | `require_stored_outcome`; `require_removal_outcome`; `require_consistent_acceptance` | mcp/src/agents_remember/models/knowledge/base.py:40-56; mcp/src/agents_remember/models/knowledge/result.py:230-247; mcp/src/agents_remember/models/knowledge/result.py:221-221; mcp/src/agents_remember/models/knowledge/result.py:220-220; mcp/src/agents_remember/models/knowledge/result.py:203-203 |
| The facade's re-export list is the served knowledge vocabulary: authors, states, context, both payload versions and their sealing helpers, family shapes, relation shapes and read models, invariant shapes, repository identity, results, source locators and — since this leaf — the whole snapshot vocabulary. | `__all__` | mcp/src/agents_remember/models/knowledge/__init__.py:146-262 |
| The eighth source module this leaf added to the facade, re-exported name by name. | `build_candidate_receipt`; `candidate_database_path`; `candidate_receipt_path`; `receipt_digest` | mcp/src/agents_remember/models/knowledge/__init__.py:112-136; mcp/src/agents_remember/models/knowledge/snapshot.py:58-62; mcp/src/agents_remember/models/knowledge/snapshot.py:64-67; mcp/src/agents_remember/models/knowledge/snapshot.py:144-151 |
| The internal rules deliberately kept off the served surface. | `require_stored_outcome`; `require_removal_outcome`; `require_consistent_acceptance` | mcp/src/agents_remember/models/knowledge/base.py:40-56; mcp/src/agents_remember/models/knowledge/result.py:188-202; mcp/src/agents_remember/models/knowledge/result.py:205-247 |
| The storage owner writes these values rather than defining its own copies — re-cited against the working tree, where the class docstring now names the sibling graph owners. | `OpenedKnowledgeStore` | mcp/src/agents_remember/memory/knowledge/store.py:92-110 |
| The composition seams that admit a destination and build every request from this vocabulary. | `admitted_knowledge_destination`; `admitted_revision_request`; `admitted_family_request`; `admitted_claim_request`; `admitted_candidate_destination` | mcp/src/agents_remember/application/knowledge.py:125-140; mcp/src/agents_remember/application/knowledge.py:144-159; mcp/src/agents_remember/application/knowledge.py:327-342; mcp/src/agents_remember/application/knowledge.py:374-389; mcp/src/agents_remember/application/knowledge_snapshot.py:67-82 |
| The shared branching fixture authors its identity and graph halves from these same models. | `build_branching_knowledge_fixture`; `BranchingKnowledgeFixture` | mcp/tests/knowledge_fixture_test_support.py:203-263; mcp/tests/knowledge_fixture_test_support.py:161-188 |
| The snapshot harness that consumes the newly re-exported names end to end. | `build_case`; `publish` | mcp/tests/snapshot_lifecycle_test_support.py:177-205; mcp/tests/snapshot_lifecycle_test_support.py:357-380 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T07:25:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read the `__all__` claim and retired the generated projection bullet that had rewritten its range mechanically.** The generated repair of 2026-09-17T06:49:47+00:00 had repointed `__all__` to `mcp/src/agents_remember/models/knowledge/__init__.py:146-262` — a mechanical anchor-range projection, not a reading: the list now spans `:160-288` (the assignment opening at `__all__ = [` and its closing bracket), because this leaf's composition vocabulary and the snapshot vocabulary the earlier leaves added both sit inside it. The row was re-cited at that extent and its wording completed with the composition source, so the claim now states what the range holds; the projection bullet is retired because a mechanically projected range is unverified evidence. Verification metadata advances to the merged base commit `15fe8678`.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand while resolving the memory sync** — `require_stored_outcome`, `require_removal_outcome`, `require_consistent_acceptance`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T07:10:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **added the composition-vocabulary section to this card's body and re-read the facade claims this leaf's change set moved.** The card's body now records the tenth source module the facade re-exports (`models/knowledge/composition.py`) and the two shared unions that grew with it — `KnowledgeOperation` gaining `create_composition`, `set_family_revision_route` and `follow_family_composition`, and `ProposedCommand` holding twenty-two variants after this leaf's four composition kinds joined the eighteen it held before — with both counts stated as measurements taken from the declarations rather than constants a later leaf edits. This is a body change, not a metadata refresh: the section is new prose about what the merged facade now serves. Verification metadata advances to the merged base commit `15fe8678`.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 3 generated projection bullet(s) by hand** — `require_stored_outcome`, `require_removal_outcome`, `require_consistent_acceptance`, `__all__`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/src/agents_remember/models/knowledge/result.py:161 to the row 112 of this card as the citation for `require_stored_outcome`: no cited file carried the construct, and the checker named line(s) [161, 359, 377] in this file as its live location

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `require_stored_outcome` in the row 112 of this card from mcp/src/agents_remember/models/knowledge/result.py:178-179 to mcp/src/agents_remember/models/knowledge/result.py:161-162, the extent of the construct the claim is about (the checker named line(s) [161, 359, 377] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `require_removal_outcome` in the row 112 of this card from mcp/src/agents_remember/models/knowledge/result.py:161-162 to mcp/src/agents_remember/models/knowledge/result.py:178-179, the extent of the construct the claim is about (the checker named line(s) [178, 477, 492] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/models/knowledge/result.py:178-179 in the row 112 of this card; the repetition added no pooled evidence

- 2026-09-16T21:50:00+00:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): recorded the facade's **ninth source, `.read`**, and it is the whole reason this file is in the change set: the selective recorded-scope read contributes no new submodule to the barrel beyond its own vocabulary module, and every name it serves is re-exported here and listed in `__all__` — the five seed kinds and their union, the context and budget, the request and result, the page and its counting model, the grouping/frontier models, the policy constant and the cursor helpers. The card states that these are **re-exported, not defined, here**, so the facade still holds no SQL, no authorization decision and no storage behaviour. Verification metadata remains empty until closeout stamps the code commit.

- 2026-09-16T09:30:00+00:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): recorded that the facade gained an **eighth source module** — `models/knowledge/snapshot.py` — and re-exports its whole surface: the local candidate layout, the sealed receipt and its two helpers, the lifecycle value objects, the publication vocabulary and the closed disposal union, all of them now in `__all__`. The card states what the exported vocabulary deliberately cannot carry (no field is a verdict; the receipt carries no dataset digest and no path) so a reader of the facade does not look for authority in it. The card's `governingOverview` link was repaired from `../../../overview.md` — which resolves to the repository-root overview — to `../overview.md`, the models route overview named by the memory census. Citation ranges were re-derived against the working tree, including rows that had drifted from their anchors. Verification metadata remains empty until closeout stamps the code commit.

- 2026-09-16T06:24:00+00:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): recorded the graph half's additions to the served surface (family shapes, relation shapes and their read models, the authored role vocabulary with `UNCLASSIFIED_ROLE`, the eight operations' requests and results, the anchor endpoint union, the family payload version and its sealing helpers) and the names the facade deliberately keeps off it (the two outcome rules, the acceptance rule, `SqliteFailureContext`, `RefusalFacts`, `KnowledgeStorageError`). This remains a re-export barrel: it defines nothing of its own and must not become an owner of validation. Verification metadata remains empty until closeout stamps the code commit.

- 2026-09-15T20:40:00+00:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new knowledge-vocabulary facade. It records the served surface as the explicit `__all__` re-export list and the ownership rule that literal vocabularies are defined in their owning submodule and imported by the decider. Verification metadata remains empty until closeout stamps the code commit.
