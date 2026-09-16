# mcp/src/agents_remember/models/knowledge/result.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/result.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `76c7697ca275a8d2764729145c950c166f3f9ec3`|
| lastVerifiedCommitDate | 2026-09-16T10:27:28+02:00|
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
(`create_repository`, `create_invariant`, `create_invariant_revision`), the eight the graph half added
(`create_family`, `create_family_revision`, `create_source_anchor`, `remove_source_anchor`,
`create_family_member`, `remove_family_member`, `create_realization_claim`, `remove_realization_claim`), and
the three this leaf added — `set_invariant_label`, `set_family_label` and `change_candidate`. The last one is
the batch operation: it appears here because a batch's refusals have to name the operation the caller
actually addressed, and a batch composes commands of the other kinds.
`KnowledgeRefusalCode` declares eighteen codes:
`invalid_payload`, `unauthorized_scope`, `unsupported_schema`, `destination_occupied`, `candidate_busy`,
`lock_capability_unavailable`, `missing_expected_row`, `stale_precondition`, `duplicate_identity`,
`immutable_revision`, `invalid_reference`, `lineage_cycle`, `relationship_constraint`, `unknown_invariant`,
`unknown_family`, **`target_not_candidate`**, **`promotion_not_supported`**, `no_change`.

**The two new codes name the two boundary conditions a candidate-only write operation has to report**: a lane
that is not a writable candidate is refused by name (`target_not_candidate`), and data asserting an accepted
origin — which would make the operation a promotion path — is refused (`promotion_not_supported`). Both are
produced by the batch's own factories in `refusals.py`, and both are refused **before any DML**. The lane
`task-candidate` deliberately reuses `unauthorized_scope` rather than inventing a code: the failure is an
authority the operation does not hold, and the refusal's `expected`/`observed` name the missing binding.

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

**The label-edit results this leaf added.** `SetInvariantLabelRequest`/`SetFamilyLabelRequest` each name the row
the caller read (`expected_row_digest`), and `SetInvariantLabelResult`/`SetFamilyLabelResult` carry the two-state
outcome `labeled | refused` with their own consistency validators: a `labeled` result must carry the label it
stored and no refusal, a `refused` result must carry its refusal. They are separate models rather than reuse of
`require_stored_outcome`, because "labeled" is a third state the shared rules do not describe — a label edit is
neither a creation nor a removal. The batch's own receipt and result vocabulary (`ChangeBatch`,
`MutationResult`, `RecordIdentity`, `ExpectedRecord`) lives in `models/knowledge/candidate.py`.

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
- **A refusal code is not a result state, and the difference drives different caller branches.** The batch's
  empty or net-zero case produces `MutationResult.state == "no_change"` with no refusal at all; the refusal
  *code* `no_change` still has no producer and a consumer must not branch on it. This is a carried limitation
  from L1/L2, recorded here as such rather than as something this leaf made reachable.
- **A new code is a vocabulary decision, not a raise-site convenience.** `target_not_candidate` and
  `promotion_not_supported` were added because the two boundary conditions need their own remedies; the
  task-lane failure deliberately reuses `unauthorized_scope` because it is the same class of failure.

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
| The declared mutating-operation vocabulary, including the three this leaf added. | `KnowledgeOperation` | mcp/src/agents_remember/models/knowledge/result.py:36-53 |
| The declared refusal vocabulary, with each member naming a distinct observable failure — now including the two candidate-boundary codes. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:55-75 |
| The two label-edit requests, each naming the row the caller read. | `SetInvariantLabelRequest`; `SetFamilyLabelRequest` | mcp/src/agents_remember/models/knowledge/result.py:235-247; mcp/src/agents_remember/models/knowledge/result.py:249-256 |
| The two label-edit results and their `labeled`/`refused` consistency validators. | `SetInvariantLabelResult`; `SetFamilyLabelResult` | mcp/src/agents_remember/models/knowledge/result.py:440-461; mcp/src/agents_remember/models/knowledge/result.py:463-484 |
| The batch vocabulary that carries the change request and its factual receipt. | `KnowledgeContext`; `ChangeBatch`; `MutationResult`; `RecordIdentity`; `ExpectedRecord` | mcp/src/agents_remember/models/knowledge/candidate.py:137-178; mcp/src/agents_remember/models/knowledge/candidate.py:381-406; mcp/src/agents_remember/models/knowledge/candidate.py:409-452; mcp/src/agents_remember/models/knowledge/candidate.py:194-215; mcp/src/agents_remember/models/knowledge/candidate.py:218-240 |
| The refusal value carrying code, operation, offending record and next action. | `KnowledgeRefusal` | mcp/src/agents_remember/models/knowledge/result.py:72-83 |
| The two shared outcome-consistency rules every result model calls. | `require_stored_outcome`; `require_removal_outcome` | mcp/src/agents_remember/models/knowledge/result.py:85-100; mcp/src/agents_remember/models/knowledge/result.py:102-111 |
| The digest-free caller draft that refuses a self-declared predecessor. | `RevisionDraft` | mcp/src/agents_remember/models/knowledge/result.py:113-137 |
| The graph's request vocabulary and the anchor-endpoint union. | `FamilyRequest`; `FamilyRevisionRequest`; `FamilyMemberRequest`; `RealizationClaimRequest`; `AnchorReference`; `NewAnchor`; `AnchorEndpoint` | mcp/src/agents_remember/models/knowledge/result.py:155-163; mcp/src/agents_remember/models/knowledge/result.py:164-170; mcp/src/agents_remember/models/knowledge/result.py:183-189; mcp/src/agents_remember/models/knowledge/result.py:214-222; mcp/src/agents_remember/models/knowledge/result.py:190-196; mcp/src/agents_remember/models/knowledge/result.py:197-207; mcp/src/agents_remember/models/knowledge/result.py:208-213 |
| The eight graph result models that reuse the shared outcome rules. | `CreateFamilyResult`; `CreateFamilyRevisionResult`; `CreateSourceAnchorResult`; `CreateFamilyMemberResult`; `CreateRealizationClaimResult`; `RemoveSourceAnchorResult`; `RemoveFamilyMemberResult`; `RemoveRealizationClaimResult` | mcp/src/agents_remember/models/knowledge/result.py:282-297; mcp/src/agents_remember/models/knowledge/result.py:298-317; mcp/src/agents_remember/models/knowledge/result.py:318-333; mcp/src/agents_remember/models/knowledge/result.py:334-349; mcp/src/agents_remember/models/knowledge/result.py:350-366; mcp/src/agents_remember/models/knowledge/result.py:367-381; mcp/src/agents_remember/models/knowledge/result.py:382-396; mcp/src/agents_remember/models/knowledge/result.py:397-411 |
| The three L1 outcome models the shared rules were extracted from. | `CreateRevisionResult`; `CreateInvariantResult`; `RepositoryCreationResult` | mcp/src/agents_remember/models/knowledge/result.py:246-265; mcp/src/agents_remember/models/knowledge/result.py:266-281; mcp/src/agents_remember/models/knowledge/result.py:412-426 |
| The factories that build every refusal in this package, one per code and case, including the two candidate-boundary codes. | `refusal`; `lineage_cycle_refusal`; `map_sqlite_error`; `batch_target_not_candidate_refusal`; `batch_promotion_not_supported_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:57-79; mcp/src/agents_remember/memory/knowledge/refusals.py:238-264; mcp/src/agents_remember/memory/knowledge/refusals.py:828-871; mcp/src/agents_remember/memory/knowledge/refusals.py:605-618; mcp/src/agents_remember/memory/knowledge/refusals.py:651-664 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): **extended the vocabulary to the candidate-write boundary and recorded the code-versus-state distinction as a carried limitation.** `KnowledgeOperation` gained the two label edits and `change_candidate` (a batch's refusals have to name the operation the caller addressed); `KnowledgeRefusalCode` gained `target_not_candidate` and `promotion_not_supported`, the two candidate-boundary conditions that are refused before any DML, while the `task-candidate` lane deliberately reuses `unauthorized_scope` because it is an authority the operation does not hold rather than a new class of failure. The card also records the two label-edit request/result pairs and why they have their own validators instead of reusing `require_stored_outcome` (`labeled` is a third state), points at `models/knowledge/candidate.py` for the batch vocabulary, and states as a carried limitation that the refusal *code* `no_change` still has no producer while the *result state* `MutationResult.state == "no_change"` is the reachable vocabulary. Verification metadata remains closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded two claims of the L1 card and extended the vocabulary to the graph half.** `KnowledgeOperation` is no longer a three-member union (eight graph operations were added) and `KnowledgeRefusalCode` now declares sixteen codes, with `stale_precondition` and `unknown_family` introduced and `missing_expected_row` becoming reachable through the three removals. The card's statement that "`unsupported_schema` and `missing_expected_row` … this leaf's code does not raise" is corrected to name `unsupported_schema` as the one code with no producer and `no_change` as a result state rather than a refusal. The card also now records the extracted outcome-consistency helpers the eight graph results reuse and the anchor-endpoint union that keeps naming-an-anchor distinct from recording one. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new typed request/refusal/result vocabulary. It records that `RevisionDraft` has no digest field by design and that two declared codes are not raised by the current write path. Verification metadata remains empty until closeout stamps the code commit.
