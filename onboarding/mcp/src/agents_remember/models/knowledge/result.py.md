# mcp/src/agents_remember/models/knowledge/result.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/result.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `3332a4ce7029777d49feca22b499350435a9f83c`|
| lastVerifiedCommitDate | 2026-09-16T11:50:16+02:00|
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
`create_family_member`, `remove_family_member`, `create_realization_claim`, `remove_realization_claim`), the
three L3 added (`set_invariant_label`, `set_family_label`, `change_candidate` — the last being the batch
operation, which appears here because a batch's refusals have to name the operation the caller actually
addressed), and **the six this leaf added**: `create_candidate`, `clone_candidate`, `open_candidate`,
`publish_snapshot`, `read_published_snapshot` and `dispose_candidate`.
`KnowledgeRefusalCode` declares twenty-five codes:
`invalid_payload`, `unauthorized_scope`, `unsupported_schema`, `destination_occupied`, `candidate_busy`,
`lock_capability_unavailable`, `missing_expected_row`, `stale_precondition`, `duplicate_identity`,
`immutable_revision`, `invalid_reference`, `lineage_cycle`, `relationship_constraint`, `unknown_invariant`,
`unknown_family`, `target_not_candidate`, `promotion_not_supported`, `no_change`, and the seven this leaf added —
**`selected_input_unavailable`, `candidate_binding_changed`, `candidate_snapshot_unpublished`,
`snapshot_incomplete`, `destination_stale`, `publication_failed`, `publication_durability_unconfirmed`**.

**The seven new codes are one member per observable failure point of the candidate-lifecycle and publication
contract**, so a caller branches on the code rather than on prose. Two of them carry a distinction a later
reader must not flatten: `snapshot_incomplete` covers both a closed snapshot that could not be frozen and a
candidate whose private stage could not be sealed, because in both cases nothing outside the operation's own
stage exists afterwards and the caller has one decision to make; and `publication_durability_unconfirmed` is the
**honest** answer for a replacement that completed but could not be re-read — neither a failure to claim nor a
success to claim.

**The two L3 codes name the two boundary conditions a candidate-only write operation has to report**: a lane
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
- `unsupported_schema` is declared vocabulary whose **producer is the caller side of a selected input**, not this
  package's own open path: since this leaf the publication gate and the candidate lifecycle emit it (through the
  generic `refusal(...)` factory) for a baseline, stage or published file that is not a database of this schema,
  while a schema mismatch discovered by `connection.inspect_schema` on the store's own open still surfaces as a
  `KnowledgeStorageError` defect. `no_change` remains a *result state* rather than a refusal; and the previously
  unproduced `missing_expected_row` is emitted by the three removal operations. The vocabulary is therefore
  recorded as declared interface with its producers named, not as a claim that every code is reachable from every
  operation.
- **A refusal code is not a result state, and the difference drives different caller branches.** Three separate
  vocabularies are now in play and none substitutes for another: the batch's `MutationResult.state == "no_change"`,
  the publication's `SnapshotPublicationResult.state == "no_change"`, and the refusal *code* `no_change`, which
  still has no producer and must not be branched on. This is a carried limitation from L1/L2, recorded here as
  such rather than as something a later leaf made reachable.
- **A new code is a vocabulary decision, not a raise-site convenience.** The L3 codes were added because two
  boundary conditions need their own remedies; the seven this leaf added exist because a caller publishing or
  opening a candidate must distinguish "the input was not there", "the binding is not this admission's", "the
  runtime candidate is ahead of the published file", "the private stage did not complete", "the destination moved",
  "the install failed" and "the install cannot be confirmed" — seven different next actions that one code would
  have collapsed into one. The task-lane failure deliberately reuses `unauthorized_scope` because it is the same
  class of failure.

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
| The declared mutating-operation vocabulary, including the six this leaf added. | `KnowledgeOperation` | mcp/src/agents_remember/models/knowledge/result.py:36-57 |
| The declared refusal vocabulary, with each member naming a distinct observable failure — now including the seven candidate-lifecycle and publication codes. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:61-89 |
| The refusal value carrying code, operation, offending record and next action. | `KnowledgeRefusal` | mcp/src/agents_remember/models/knowledge/result.py:92-104 |
| The two shared outcome-consistency rules every result model calls. | `require_stored_outcome`; `require_removal_outcome` | mcp/src/agents_remember/models/knowledge/result.py:105-121; mcp/src/agents_remember/models/knowledge/result.py:122-132 |
| The digest-free caller draft that refuses a self-declared predecessor. | `RevisionDraft` | mcp/src/agents_remember/models/knowledge/result.py:133-158 |
| The two label-edit requests, each naming the row the caller read. | `SetInvariantLabelRequest`; `SetFamilyLabelRequest` | mcp/src/agents_remember/models/knowledge/result.py:250-263; mcp/src/agents_remember/models/knowledge/result.py:264-272 |
| The two label-edit results and their `labeled`/`refused` consistency validators. | `SetInvariantLabelResult`; `SetFamilyLabelResult` | mcp/src/agents_remember/models/knowledge/result.py:455-477; mcp/src/agents_remember/models/knowledge/result.py:478-500 |
| The batch vocabulary that carries the change request and its factual receipt. | `KnowledgeContext`; `ChangeBatch`; `MutationResult`; `RecordIdentity`; `ExpectedRecord` | mcp/src/agents_remember/models/knowledge/candidate.py:137-178; mcp/src/agents_remember/models/knowledge/candidate.py:381-406; mcp/src/agents_remember/models/knowledge/candidate.py:409-452; mcp/src/agents_remember/models/knowledge/candidate.py:194-215; mcp/src/agents_remember/models/knowledge/candidate.py:218-240 |
| The graph's request vocabulary and the anchor-endpoint union. | `FamilyRequest`; `FamilyRevisionRequest`; `FamilyMemberRequest`; `RealizationClaimRequest`; `AnchorReference`; `NewAnchor`; `AnchorEndpoint` | mcp/src/agents_remember/models/knowledge/result.py:175-183; mcp/src/agents_remember/models/knowledge/result.py:184-190; mcp/src/agents_remember/models/knowledge/result.py:203-209; mcp/src/agents_remember/models/knowledge/result.py:234-242; mcp/src/agents_remember/models/knowledge/result.py:210-216; mcp/src/agents_remember/models/knowledge/result.py:217-227; mcp/src/agents_remember/models/knowledge/result.py:228-231 |
| The eight graph result models that reuse the shared outcome rules. | `CreateFamilyResult`; `CreateFamilyRevisionResult`; `CreateSourceAnchorResult`; `CreateFamilyMemberResult`; `CreateRealizationClaimResult`; `RemoveSourceAnchorResult`; `RemoveFamilyMemberResult`; `RemoveRealizationClaimResult` | mcp/src/agents_remember/models/knowledge/result.py:325-340; mcp/src/agents_remember/models/knowledge/result.py:341-360; mcp/src/agents_remember/models/knowledge/result.py:361-376; mcp/src/agents_remember/models/knowledge/result.py:377-392; mcp/src/agents_remember/models/knowledge/result.py:393-409; mcp/src/agents_remember/models/knowledge/result.py:410-424; mcp/src/agents_remember/models/knowledge/result.py:425-439; mcp/src/agents_remember/models/knowledge/result.py:440-454 |
| The three L1 outcome models the shared rules were extracted from. | `CreateRevisionResult`; `CreateInvariantResult`; `RepositoryCreationResult` | mcp/src/agents_remember/models/knowledge/result.py:289-308; mcp/src/agents_remember/models/knowledge/result.py:309-324; mcp/src/agents_remember/models/knowledge/result.py:501-516 |
| **The seven factories that produce this leaf's codes, one per observable failure point.** | `selected_input_unavailable_refusal`; `candidate_binding_changed_refusal`; `candidate_snapshot_unpublished_refusal`; `snapshot_incomplete_refusal`; `destination_stale_refusal`; `publication_failed_refusal`; `publication_durability_unconfirmed_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:882-902; mcp/src/agents_remember/memory/knowledge/refusals.py:904-928; mcp/src/agents_remember/memory/knowledge/refusals.py:930-949; mcp/src/agents_remember/memory/knowledge/refusals.py:951-974; mcp/src/agents_remember/memory/knowledge/refusals.py:976-999; mcp/src/agents_remember/memory/knowledge/refusals.py:1001-1018; mcp/src/agents_remember/memory/knowledge/refusals.py:1020-1039 |
| The factories that build every other refusal in this package, one per code and case. | `refusal`; `lineage_cycle_refusal`; `map_sqlite_error`; `batch_target_not_candidate_refusal`; `batch_promotion_not_supported_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:57-79; mcp/src/agents_remember/memory/knowledge/refusals.py:238-264; mcp/src/agents_remember/memory/knowledge/refusals.py:828-871; mcp/src/agents_remember/memory/knowledge/refusals.py:605-618; mcp/src/agents_remember/memory/knowledge/refusals.py:651-664 |
| The two result states that carry `no_change` and the two operations that reach them. | `MutationResult`; `SnapshotPublicationResult` | mcp/src/agents_remember/models/knowledge/candidate.py:409-452; mcp/src/agents_remember/models/knowledge/snapshot.py:259-293 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): **extended the vocabulary to the candidate lifecycle and snapshot publication, and corrected this card's `unsupported_schema` producer claim.** `KnowledgeOperation` gained six members (`create_candidate`, `clone_candidate`, `open_candidate`, `publish_snapshot`, `read_published_snapshot`, `dispose_candidate`) and `KnowledgeRefusalCode` gained seven (`selected_input_unavailable`, `candidate_binding_changed`, `candidate_snapshot_unpublished`, `snapshot_incomplete`, `destination_stale`, `publication_failed`, `publication_durability_unconfirmed`) — one per observable failure point, because a caller publishing or opening a candidate has seven different next actions that one code would have collapsed. The card states the two distinctions a later reader must not flatten: `snapshot_incomplete` covers both a freeze that did not complete and a candidate private stage that could not be sealed (nothing outside the operation's own stage exists in either case), and `publication_durability_unconfirmed` is the honest answer for a replacement that completed but could not be re-read. It also corrects the earlier claim that `unsupported_schema` has **no producer**: the publication gate and the candidate lifecycle now emit it for a selected input that is not a database of this schema, while the store's own open path still reports its own schema mismatches as `KnowledgeStorageError` — the split is deliberate. The `no_change` distinction is restated with the publication result state added to it, so all three vocabularies (two result states and one reserved code) are named in one place. Citation ranges in this card were re-derived against the working tree and the pre-existing rows whose ranges no longer held their anchors were corrected. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): **extended the vocabulary to the candidate-write boundary and recorded the code-versus-state distinction as a carried limitation.** `KnowledgeOperation` gained the two label edits and `change_candidate` (a batch's refusals have to name the operation the caller addressed); `KnowledgeRefusalCode` gained `target_not_candidate` and `promotion_not_supported`, the two candidate-boundary conditions that are refused before any DML, while the `task-candidate` lane deliberately reuses `unauthorized_scope` because it is an authority the operation does not hold rather than a new class of failure. The card also records the two label-edit request/result pairs and why they have their own validators instead of reusing `require_stored_outcome` (`labeled` is a third state), points at `models/knowledge/candidate.py` for the batch vocabulary, and states as a carried limitation that the refusal *code* `no_change` still has no producer while the *result state* `MutationResult.state == "no_change"` is the reachable vocabulary. Verification metadata remains closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded two claims of the L1 card and extended the vocabulary to the graph half.** `KnowledgeOperation` is no longer a three-member union (eight graph operations were added) and `KnowledgeRefusalCode` now declares sixteen codes, with `stale_precondition` and `unknown_family` introduced and `missing_expected_row` becoming reachable through the three removals. The card's statement that "`unsupported_schema` and `missing_expected_row` … this leaf's code does not raise" is corrected to name `unsupported_schema` as the one code with no producer and `no_change` as a result state rather than a refusal. The card also now records the extracted outcome-consistency helpers the eight graph results reuse and the anchor-endpoint union that keeps naming-an-anchor distinct from recording one. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new typed request/refusal/result vocabulary. It records that `RevisionDraft` has no digest field by design and that two declared codes are not raised by the current write path. Verification metadata remains empty until closeout stamps the code commit.
