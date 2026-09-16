# mcp/src/agents_remember/models/knowledge/result.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/result.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The typed operation requests, the refusal vocabulary and the mutation results: every knowledge failure is a
returned value with a code, an offending record and a concrete next action, rather than an exception a caller has
to parse.

## Code Commentary

### Logic

`KnowledgeOperation` is the closed literal union of mutating operations: the three L1 members
(`create_repository`, `create_invariant`, `create_invariant_revision`) plus the eight the graph half added
(`create_family`, `create_family_revision`, `create_source_anchor`, `remove_source_anchor`,
`create_family_member`, `remove_family_member`, `create_realization_claim`, `remove_realization_claim`).
`KnowledgeRefusalCode` declares sixteen codes:
`invalid_payload`, `unauthorized_scope`, `unsupported_schema`, `destination_occupied`, `candidate_busy`,
`lock_capability_unavailable`, `missing_expected_row`, `stale_precondition`, `duplicate_identity`,
`immutable_revision`, `invalid_reference`, `lineage_cycle`, `relationship_constraint`, `unknown_invariant`,
`unknown_family`, `no_change`.

`KnowledgeRefusal` carries `code`, `operation`, `detail`, optional `table`/`record_id`/`expected`/`observed` and a
required `next_action`.

`RevisionDraft` is the caller-supplied aggregate **before sealing** and therefore has no `payload_digest` field; it
refuses a self-declared predecessor. `RevisionRequest` pairs a draft with its `repository_id`, and
`InvariantRequest` carries an invariant identity insert.

**The graph's request vocabulary** follows the same shape: `FamilyRequest` / `FamilyRevisionRequest` for the
family half, `SourceAnchorRequest` and the three removal requests for the anchor and relation lifetimes,
`FamilyMemberRequest` and `RealizationClaimRequest` for the two relations, and `AnchorEndpoint` — the union of
`AnchorReference` (name an existing anchor) and `NewAnchor` (record one in the same transaction), which is the one
place where "which arm of the union" is decided by the request rather than by the models.

`require_stored_outcome` and `require_removal_outcome` are the shared consistency rules, and every result model
calls them: a `created` result carries a digest where applicable, `stored=True` and no refusal; a `no_change`
result stored nothing and carries no refusal; a `refused` result must carry its refusal and must not claim it
stored a row; a `removed` result carries no refusal. The eight graph result models reuse them rather than
repeating the three-way check, and each result carries a **defaulted** `operation` literal for its own operation so
a result cannot mislabel which operation produced it.

### Conventions

Codes are a declared vocabulary: a storage failure with no code here is a defect, not a new code invented at the
raise site. A caller branches on `code`, never on message text.

### Invariants And Boundaries

- The digest is absent from `RevisionDraft` by design — the store recomputes and stores it, so a caller cannot
  present a payload whose seal belongs to different content.
- The result models are the typed contract of the operation; they refuse an internally inconsistent outcome at
  construction, so an "everyone agrees" bug is caught at the returning call site and not by a caller's branch.
- **A result names its own operation.** The defaulted `operation` literal means a `CreateFamilyResult` cannot be
  returned for a family-revision operation, which matters once eight graph operations share two result helpers.
- `unsupported_schema` is declared vocabulary with **no producer** anywhere in `mcp/src` — a schema failure
  surfaces as `KnowledgeStorageError` from `connection.inspect_schema` instead; `no_change` is a *result state*
  rather than a refusal; and the previously unproduced `missing_expected_row` is now emitted by the three removal
  operations. The vocabulary is therefore recorded as declared interface with its producers named, not as a claim
  that every code is reachable.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The declared mutating-operation vocabulary, including the eight the graph half added. | `KnowledgeOperation` | mcp/src/agents_remember/models/knowledge/result.py:34-47 |
| The declared refusal vocabulary, with each member naming a distinct observable failure. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:52-69 |
| The refusal value carrying code, operation, offending record and next action. | `KnowledgeRefusal` | mcp/src/agents_remember/models/knowledge/result.py:72-83 |
| The two shared outcome-consistency rules every result model calls. | `require_stored_outcome`; `require_removal_outcome` | mcp/src/agents_remember/models/knowledge/result.py:85-100; mcp/src/agents_remember/models/knowledge/result.py:102-111 |
| The digest-free caller draft that refuses a self-declared predecessor. | `RevisionDraft` | mcp/src/agents_remember/models/knowledge/result.py:113-137 |
| The graph's request vocabulary and the anchor-endpoint union. | `FamilyRequest`; `FamilyRevisionRequest`; `FamilyMemberRequest`; `RealizationClaimRequest`; `AnchorReference`; `NewAnchor`; `AnchorEndpoint` | mcp/src/agents_remember/models/knowledge/result.py:155-163; mcp/src/agents_remember/models/knowledge/result.py:164-170; mcp/src/agents_remember/models/knowledge/result.py:183-189; mcp/src/agents_remember/models/knowledge/result.py:214-222; mcp/src/agents_remember/models/knowledge/result.py:190-196; mcp/src/agents_remember/models/knowledge/result.py:197-207; mcp/src/agents_remember/models/knowledge/result.py:208-213 |
| The eight graph result models that reuse the shared outcome rules. | `CreateFamilyResult`; `CreateFamilyRevisionResult`; `CreateSourceAnchorResult`; `CreateFamilyMemberResult`; `CreateRealizationClaimResult`; `RemoveSourceAnchorResult`; `RemoveFamilyMemberResult`; `RemoveRealizationClaimResult` | mcp/src/agents_remember/models/knowledge/result.py:282-297; mcp/src/agents_remember/models/knowledge/result.py:298-317; mcp/src/agents_remember/models/knowledge/result.py:318-333; mcp/src/agents_remember/models/knowledge/result.py:334-349; mcp/src/agents_remember/models/knowledge/result.py:350-366; mcp/src/agents_remember/models/knowledge/result.py:367-381; mcp/src/agents_remember/models/knowledge/result.py:382-396; mcp/src/agents_remember/models/knowledge/result.py:397-411 |
| The three L1 outcome models the shared rules were extracted from. | `CreateRevisionResult`; `CreateInvariantResult`; `RepositoryCreationResult` | mcp/src/agents_remember/models/knowledge/result.py:246-265; mcp/src/agents_remember/models/knowledge/result.py:266-281; mcp/src/agents_remember/models/knowledge/result.py:412-426 |
| The factories that build every refusal in this package, one per code and case. | `refusal`; `lineage_cycle_refusal`; `map_sqlite_error` | mcp/src/agents_remember/memory/knowledge/refusals.py:57-79; mcp/src/agents_remember/memory/knowledge/refusals.py:238-264; mcp/src/agents_remember/memory/knowledge/refusals.py:609-652 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded two claims of the L1 card and extended the vocabulary to the graph half.** `KnowledgeOperation` is no longer a three-member union (eight graph operations were added) and `KnowledgeRefusalCode` now declares sixteen codes, with `stale_precondition` and `unknown_family` introduced and `missing_expected_row` becoming reachable through the three removals. The card's statement that "`unsupported_schema` and `missing_expected_row` … this leaf's code does not raise" is corrected to name `unsupported_schema` as the one code with no producer and `no_change` as a result state rather than a refusal. The card also now records the extracted outcome-consistency helpers the eight graph results reuse and the anchor-endpoint union that keeps naming-an-anchor distinct from recording one. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new typed request/refusal/result vocabulary. It records that `RevisionDraft` has no digest field by design and that two declared codes are not raised by the current write path. Verification metadata remains empty until closeout stamps the code commit.
