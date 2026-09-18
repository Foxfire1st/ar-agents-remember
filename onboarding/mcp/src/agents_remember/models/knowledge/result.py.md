# mcp/src/agents_remember/models/knowledge/result.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/result.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:15+02:00 |
| lastVerifiedCommitHash | `15fe8678fc0f87eaac4606952f179135ebe392c4`|
| lastVerifiedCommitDate | 2026-09-18T07:49:45+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l14` uncommitted source; base `4264dcc9decf50e64c863e9c6526ea09117be71b` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

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
addressed), the six L4 added (`create_candidate`, `clone_candidate`, `open_candidate`, `publish_snapshot`,
`read_published_snapshot`, `dispose_candidate`), the two L5 added (`resolve_merge_base`,
`merge_knowledge_datasets`), the two L6 added (`export_knowledge_dataset`,
`import_knowledge_dataset`), the one L7 added (`read_knowledge_scope` — one operation rather than two
because a seed and a continuation are two ways of asking the same question ("which recorded scope, and which
page of it") and a caller branches on the refusal code, not on which of the two it passed), and **the one
L8 added: `diff_knowledge_scope`** — again one operation rather than two, and for the same reason: a first
comparison and a continuation are two ways of asking one question ("what does the union of these two
snapshots' selections hold, and which page of it is this"), and a caller branches on the refusal code
rather than on which of the two it passed. **The measured union is thirty-nine operations**, counted from
the literal on this candidate rather than carried forward: the L10 route pair (`author_route`,
`set_governing_route`), L11's six facet acts (`add_facet`, `attach_facet`, `remove_facet_attachment`,
`author_explanation`, `add_explanation_revision`, `designate_explanation`), L11's own read
(`read_facet_scope`), L14's two detection operations (`record_detection_run`, `read_detection_run`) and
L19's two requirement-revision operations (`record_requirement_revision`, `read_requirement_revisions`)
are all members now, and the L8 entry's "twenty-six" was a count of the members *that leaf* could see
rather than a count of the union. **The refusal vocabulary is untouched by L19**: every refusal the
requirement record group issues is a shipped code, so `KnowledgeRefusalCode` is still **forty-five
codes** — an absence recorded as a fact rather than left to be inferred from a diff.
`KnowledgeRefusalCode` declares **forty-five codes** (re-counted from the literal on this candidate; the
thirty-seven this card recorded before the L7 pass was already one short of the thirty-eight the union held
at that leaf's own base):`invalid_payload`, `unauthorized_scope`, `unsupported_schema`, `destination_occupied`, `candidate_busy`,
`lock_capability_unavailable`, `missing_expected_row`, `stale_precondition`, `duplicate_identity`,
`immutable_revision`, `invalid_reference`, `lineage_cycle`, `relationship_constraint`, `unknown_invariant`,
`unknown_family`, `target_not_candidate`, `promotion_not_supported`, `no_change`, the seven L4 added —
**`selected_input_unavailable`, `candidate_binding_changed`, `candidate_snapshot_unpublished`,
`snapshot_incomplete`, `destination_stale`, `publication_failed`, `publication_durability_unconfirmed`** —
the twelve L5 added (`common_base_unavailable`, `common_base_ambiguous`, `common_base_mismatch`,
`schema_mismatch`, `missing_required_table`, `conflicting_values`, `duplicate_relationship`,
`delete_reference_conflict`, `immutable_revision_changed`, `session_unavailable`, `changeset_incomplete`,
`changeset_postcondition_failed`), the one L6 added (`invalid_export`), the six L7 added:
`selector_absent`, `registration_absent`, `page_budget_too_small`, `continuation_binding_mismatch`,
`snapshot_unavailable`, `selection_incomplete`, and the one L14 added: `detection_self_reference`. **L8 added
no code at all** — it is the first knowledge leaf
of this master whose boundary needed no new refusal vocabulary, and that is a fact worth recording rather
than a silence: the comparison's whole failure surface is R07's own codes plus `selected_input_unavailable`,
which the L4 publication path already produced. **L10 and L11 added none either** — the route operations and
the six facet acts reuse shipped codes, and `invalid_payload` covers every inadmissible facet payload.
**L14 added exactly one**, and the reason is the same rule the L3 codes follow: only a detection write can
reach the self-invalidating sequence it names.
A comparison's refusals reach the same codes through their own factories and their own `detail` text, and
`side_absences` carries one side's absence as a **value beside the page** rather than as a refusal.

**`detection_self_reference` is the one member only a detection write can reach.** A detection signal and
its run are *measurements of an already-existing dataset*, so a write whose target store **is** one of the
datasets the run assessed would move the logical digest of the dataset it just digested and invalidate its
own signal. Rather than folding that into a neighbouring storage code, the vocabulary names the fact a
caller branches on — and the two operations were added as a pair rather than as one member, for the reason
the read pair and the diff pair are one each: recording a run and reading one back are different acts, and
the read is the one that must answer with the run's **recorded order** rather than with whatever order rows
come back in. Neither new member mints a gate, and no result model in this module changed.

**The six L7 codes are the ones only a bounded, continuable selection can reach, and each is a distinct fact
a caller acts on differently**: a seed that names no recorded identity or revision (`selector_absent` — the
caller asked the wrong question); a path with no recorded claim (`registration_absent` — a right question
whose answer is that nothing is recorded there yet, and **not** a verdict of "no semantic impact"); a
one-item page budget that cannot hold even one indivisible item (`page_budget_too_small`, which reports the
exact minimum and leaves the position unchanged); a continuation presented against another snapshot,
context, selector, policy, schema, manifest or position (`continuation_binding_mismatch`, which returns
**no items**); a selected snapshot that cannot be obtained at all (`snapshot_unavailable`, which is also
what a schema generation this build cannot read surfaces as — **the read does not use `unsupported_schema`**,
and its `detail` names both generations); and a selection that reached its declared execution bound
(`selection_incomplete`, which emits **no total and no partial manifest**). `unsupported_schema`,
`selected_input_unavailable`, `stale_precondition` and `candidate_snapshot_unpublished` are **shared** with
the paths where the failure is the same fact.

**`invalid_export` is the one member only a portable artifact can reach, and that is the reason it exists.** The
artifact is the only input on any of these paths that can be **malformed as a document**: an unknown envelope
field, a missing manifest key, a repeated JSON key, a row whose fields are not the declared columns in declared
order, a value the declared column type cannot hold, or a text that is not the canonical rendering of the
document it holds — a defect of the artifact rather than of an authored payload. Two other facts about it belong
here rather than on the encoder's card: **one code covers the malformed document and the incomplete dataset** on
purpose, because the caller's decision is the same for both and `detail` names which of the two it is (splitting
it would invite a caller to read "parsed" as "trustworthy"); and the canonical-form refusal carries
`record_id == "<canonical document>"` from its own factory, so the caller can tell "this is not the format" from
"this is the format spelled some other way". `unsupported_schema`, `duplicate_identity`, `invalid_reference` and
`destination_occupied` are **shared** with the paths where the failure is the same fact; `invalid_export` is not
shared with anything.

**The seven L4 codes are one member per observable failure point of the candidate-lifecycle and publication
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
  boundary conditions need their own remedies; the seven L4 added exist because a caller publishing or opening a
  candidate must distinguish "the input was not there", "the binding is not this admission's", "the runtime
  candidate is ahead of the published file", "the private stage did not complete", "the destination moved", "the
  install failed" and "the install cannot be confirmed" — seven different next actions that one code would have
  collapsed into one. **The twelve L5 codes exist for the same reason on the merge path**: each names one
  observable failure point of base resolution, structural preflight, changeset coverage or application, so a
  caller that has to decide what to do next reads a code rather than prose. The task-lane failure deliberately
  reuses `unauthorized_scope` because it is the same class of failure. **The one L6 code is the sharpest case of
  the same rule, and also the narrowest**: `invalid_export` exists because the portable artifact is the only input
  on any of these paths that can be malformed *as a document*, and no other code could tell a caller "your
  document is wrong" as distinct from "your records are not this schema's knowledge" (that second fact stays
  `relationship_constraint`, emitted by the staged-database check).

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
| The declared mutating-operation vocabulary, including the six L4 operations, the two L5 merge operations, the two L6 portable operations, the one L7 read operation, the one L8 comparison operation, the two L10 route operations, the seven L11 facet operations, **the two L14 detection operations and the two L19 requirement-revision operations** — **thirty-nine members, re-counted from the literal**, which is `:36-105`. | `KnowledgeOperation` | mcp/src/agents_remember/models/knowledge/result.py:36-105 |
| **The two members this leaf added, beside the read/diff/detection idiom they follow: recording a requirement revision and reading the revisions back are different acts with different remedies, and neither can carry a task status, a seat owner or a lifecycle gate.** | `record_requirement_revision`; `read_requirement_revisions` | mcp/src/agents_remember/models/knowledge/result.py:97-104; mcp/src/agents_remember/models/knowledge/result.py:105-105 |
| The declared refusal vocabulary, with each member naming a distinct observable failure — the seven L4 codes, the twelve L5 merge codes, the one L6 portable code, the six L7 read codes (L8, L10 and L11 added none) and **the one L14 detection code**; forty-five members, re-counted from the literal. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:101-171 |
| **The six L7 codes' producers, one factory per observable failure point, each carrying the next action a caller needs.** | `selector_absent_refusal`; `registration_absent_refusal`; `page_budget_too_small_refusal`; `continuation_binding_mismatch_refusal`; `snapshot_unavailable_refusal`; `selection_incomplete_refusal` | mcp/src/agents_remember/memory/knowledge/read_refusals.py:35-57; mcp/src/agents_remember/memory/knowledge/read_refusals.py:60-79; mcp/src/agents_remember/memory/knowledge/read_refusals.py:82-108; mcp/src/agents_remember/memory/knowledge/read_refusals.py:111-135; mcp/src/agents_remember/memory/knowledge/read_refusals.py:138-156; mcp/src/agents_remember/memory/knowledge/read_refusals.py:159-177 |
| **The read's own result model, which is a page or a refusal and never both, and the read operation literal it carries.** | `KnowledgeReadResult` | mcp/src/agents_remember/models/knowledge/read.py:485-511 |
| The refusal value carrying code, operation, offending record and next action. | `KnowledgeRefusal` | mcp/src/agents_remember/models/knowledge/result.py:190-200 |
| The two shared outcome-consistency rules every result model calls. | `require_stored_outcome`; `require_removal_outcome` | mcp/src/agents_remember/models/knowledge/result.py:204-204; mcp/src/agents_remember/models/knowledge/result.py:221-221; mcp/src/agents_remember/models/knowledge/result.py:220-220; mcp/src/agents_remember/models/knowledge/result.py:203-203 |
| The digest-free caller draft that refuses a self-declared predecessor. | `RevisionDraft` | mcp/src/agents_remember/models/knowledge/result.py:216-239 |
| The two label-edit requests, each naming the row the caller read. | `SetInvariantLabelRequest` | mcp/src/agents_remember/models/knowledge/result.py:348-359 |
| The family-label request that names the row the caller read. | `SetFamilyLabelRequest` | mcp/src/agents_remember/models/knowledge/result.py:355-363 |
| The invariant-label result and its `labeled`/`refused` consistency validator. | `SetInvariantLabelResult` | mcp/src/agents_remember/models/knowledge/result.py:538-558 |
| The family-label result and its `labeled`/`refused` consistency validator. | `SetFamilyLabelResult` | mcp/src/agents_remember/models/knowledge/result.py:561-581 |
| The batch vocabulary that carries the change request and its factual receipt. | `KnowledgeContext`; `ChangeBatch`; `MutationResult`; `RecordIdentity`; `ExpectedRecord` | mcp/src/agents_remember/models/knowledge/candidate.py:137-178; mcp/src/agents_remember/models/knowledge/candidate.py:381-406; mcp/src/agents_remember/models/knowledge/candidate.py:409-452; mcp/src/agents_remember/models/knowledge/candidate.py:194-215; mcp/src/agents_remember/models/knowledge/candidate.py:218-240 |
| The graph's request vocabulary and the anchor-endpoint union. | `FamilyRequest`; `FamilyRevisionRequest`; `FamilyMemberRequest`; `AnchorReference` | mcp/src/agents_remember/models/knowledge/result.py:242-315; mcp/src/agents_remember/models/knowledge/result.py:283-283; mcp/src/agents_remember/models/knowledge/result.py:302-302; mcp/src/agents_remember/models/knowledge/result.py:309-309 |
| The realization-claim request the graph half added. | `RealizationClaimRequest` | mcp/src/agents_remember/models/knowledge/result.py:325-333 |
| The eight graph result models that reuse the shared outcome rules. | `CreateFamilyResult`; `CreateFamilyRevisionResult`; `CreateSourceAnchorResult`; `CreateFamilyMemberResult`; `CreateRealizationClaimResult`; `RemoveSourceAnchorResult`; `RemoveFamilyMemberResult`; `RemoveRealizationClaimResult` | mcp/src/agents_remember/models/knowledge/result.py:416-431; mcp/src/agents_remember/models/knowledge/result.py:432-451; mcp/src/agents_remember/models/knowledge/result.py:452-467; mcp/src/agents_remember/models/knowledge/result.py:468-483; mcp/src/agents_remember/models/knowledge/result.py:484-500; mcp/src/agents_remember/models/knowledge/result.py:501-515; mcp/src/agents_remember/models/knowledge/result.py:516-530; mcp/src/agents_remember/models/knowledge/result.py:531-545; mcp/src/agents_remember/models/knowledge/result.py:538-538 |
| The three L1 outcome models the shared rules were extracted from. | `CreateRevisionResult`; `CreateInvariantResult`; `RepositoryCreationResult` | mcp/src/agents_remember/models/knowledge/result.py:380-399; mcp/src/agents_remember/models/knowledge/result.py:400-415; mcp/src/agents_remember/models/knowledge/result.py:592-606 |
| **The seven factories that produce this leaf's codes, one per observable failure point.** | `selected_input_unavailable_refusal`; `candidate_binding_changed_refusal`; `candidate_snapshot_unpublished_refusal`; `snapshot_incomplete_refusal`; `destination_stale_refusal`; `publication_failed_refusal`; `publication_durability_unconfirmed_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:882-902; mcp/src/agents_remember/memory/knowledge/refusals.py:904-928; mcp/src/agents_remember/memory/knowledge/refusals.py:930-949; mcp/src/agents_remember/memory/knowledge/refusals.py:951-974; mcp/src/agents_remember/memory/knowledge/refusals.py:976-999; mcp/src/agents_remember/memory/knowledge/refusals.py:1001-1018; mcp/src/agents_remember/memory/knowledge/refusals.py:1020-1039 |
| The factories that build every other refusal in this package, one per code and case. | `refusal`; `lineage_cycle_refusal`; `map_sqlite_error`; `batch_target_not_candidate_refusal`; `batch_promotion_not_supported_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:57-77; mcp/src/agents_remember/memory/knowledge/refusals.py:238-264; mcp/src/agents_remember/memory/knowledge/refusals.py:828-871; mcp/src/agents_remember/memory/knowledge/refusals.py:605-618; mcp/src/agents_remember/memory/knowledge/refusals.py:651-664 |
| The two result states that carry `no_change` and the two operations that reach them. | `MutationResult`; `SnapshotPublicationResult` | mcp/src/agents_remember/models/knowledge/candidate.py:409-452; mcp/src/agents_remember/models/knowledge/snapshot.py:259-293 |
| **The ten factories that produce this leaf's twelve merge codes, one per observable failure point**, including the two structural refusals that run before a session exists. | `schema_mismatch_refusal`; `missing_required_table_refusal`; `conflicting_values_refusal`; `duplicate_identity_refusal`; `delete_reference_conflict_refusal`; `duplicate_relationship_refusal`; `immutable_revision_changed_refusal`; `session_unavailable_refusal`; `changeset_incomplete_refusal`; `changeset_postcondition_failed_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:21-45; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:48-67; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:70-94; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:97-121; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:124-151; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:154-173; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:176-196; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:199-218; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:221-245; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:248-270 |
| **The five factories that produce the portable boundary's codes in this leaf's own refusal module, one per observable failure point.** | `invalid_export_refusal`; `non_canonical_export_refusal`; `unsupported_schema_refusal`; `destination_occupied_refusal`; `destination_absent_refusal`; `import_validation_failed_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:26-50; mcp/src/agents_remember/memory/knowledge/export_refusals.py:53-75; mcp/src/agents_remember/memory/knowledge/export_refusals.py:78-102; mcp/src/agents_remember/memory/knowledge/export_refusals.py:105-126; mcp/src/agents_remember/memory/knowledge/export_refusals.py:129-148; mcp/src/agents_remember/memory/knowledge/export_refusals.py:151-172 |
| **The one L6 code's dedicated refusal identity: the canonical-form refusal, whose `record_id` distinguishes "not this format" from "this format, spelled differently".** | `non_canonical_export_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:53-75 |
| The node that asserts the portable boundary's refusal codes by code rather than by message. | "test_a_document_that_is_not_a_well_formed_artifact_is_refused" | mcp/tests/test_knowledge_portable_roundtrip.py:716-802 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |
| The declared mutating-operation vocabulary, including the six L4 operations, the two L5 merge operations, the two L6 portable operations, the one L7 read operation, the one L8 comparison operation, the two L10 route operations, the seven L11 facet operations, **the two L14 detection operations** and **the two L18 citation-binding operations** — thirty-nine members, re-counted from the literal. | `KnowledgeOperation` | mcp/src/agents_remember/models/knowledge/result.py:36-104 |
| The declared refusal vocabulary, with each member naming a distinct observable failure — the seven L4 codes, the twelve L5 merge codes, the one L6 portable code, the six L7 read codes (L8, L10, L11 and L18 added none) and **the one L14 detection code**; forty-five members, re-counted from the literal. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:101-171 |
| The eight graph result models that reuse the shared outcome rules, cited at their own declarations rather than at one of them. | `CreateFamilyResult`; `CreateFamilyRevisionResult`; `CreateSourceAnchorResult`; `CreateFamilyMemberResult`; `CreateRealizationClaimResult`; `RemoveSourceAnchorResult`; `RemoveFamilyMemberResult`; `RemoveRealizationClaimResult` | mcp/src/agents_remember/models/knowledge/result.py:415-429; mcp/src/agents_remember/models/knowledge/result.py:431-449; mcp/src/agents_remember/models/knowledge/result.py:451-465; mcp/src/agents_remember/models/knowledge/result.py:467-481; mcp/src/agents_remember/models/knowledge/result.py:483-498; mcp/src/agents_remember/models/knowledge/result.py:500-513; mcp/src/agents_remember/models/knowledge/result.py:515-528; mcp/src/agents_remember/models/knowledge/result.py:539-539; mcp/src/agents_remember/models/knowledge/result.py:538-538 |
| The three L1 outcome models the shared rules were extracted from, cited at their own declarations. | `CreateRevisionResult`; `CreateInvariantResult`; `RepositoryCreationResult` | mcp/src/agents_remember/models/knowledge/result.py:379-397; mcp/src/agents_remember/models/knowledge/result.py:399-413; mcp/src/agents_remember/models/knowledge/result.py:591-600 |

## Update History
- 2026-09-18T05:29:42+00:00: Generated citation repair: `KnowledgeRefusal` repointed to mcp/src/agents_remember/models/knowledge/result.py:190-200. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: `SetInvariantLabelRequest` repointed to mcp/src/agents_remember/models/knowledge/result.py:348-359. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:40+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **extended the operation vocabulary to the requirement-revision record group, re-counted the union from the literal, and retired this card's generated projection bullets by hand.** `KnowledgeOperation` gained **two** members — `record_requirement_revision` and `read_requirement_revisions`, at `:103-104`, inside a union that now runs `:36-105` — and `KnowledgeRefusalCode` gained **nothing**. That absence is recorded rather than left to be inferred: the requirement record group issues only shipped codes (`promotion_not_supported`, `duplicate_identity`, `lineage_cycle`, `invalid_reference`, `missing_expected_row`, `immutable_revision`, `unauthorized_scope`), so the refusal union stays at **forty-five** and the body now says so. **A measured correction to this card's own count:** the operation union is **thirty-nine**, not the thirty-seven the L14 entry recorded — that was correct for the members L14 could see and L19's pair are members now — and the body paragraph and the reference row were both re-counted against the literal rather than shifted. Four generated projection bullets were **retired by hand** and their claims re-cited from the declarations an agent then read: `SetFamilyLabelRequest` is `:355-363` (the projected range stopped at the class body and missed nothing, but the row now names the whole class), `RealizationClaimRequest` is `:325-333`, the eight graph result models are each cited at their own full span (`:416-431`, `:432-451`, `:452-467`, `:468-483`, `:484-500`, `:501-515`, `:516-530`, `:531-545`), and the three L1 outcome models are `:380-399`, `:400-415`, `:592-606`. A row for the two new members was added, whose comment states why they are two rather than one and why neither can carry a task status, a seat owner or a lifecycle gate. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T06:35+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 4 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: ``SetFamilyLabelRequest`` → `mcp/src/agents_remember/models/knowledge/result.py:355-361`; ``RealizationClaimRequest`` → `mcp/src/agents_remember/models/knowledge/result.py:325-331`; ``CreateFamilyResult`; `CreateFamilyRevisionResult`; `CreateSourceAnchorResult`; `CreateFamilyMemberResult`; `CreateRealizationClaimResult`; `RemoveSourceAnchorResult`; `RemoveFamilyMemberResult`; `RemoveRealizationClaimResult`` → `mcp/src/agents_remember/models/knowledge/result.py:416-429; mcp/src/agents_remember/models/knowledge/result.py:432-449; mcp/src/agents_remember/models/knowledge/result.py:452-465; mcp/src/agents_remember/models/knowledge/result.py:468-481; mcp/src/agents_remember/models/knowledge/result.py:484-498; mcp/src/agents_remember/models/knowledge/result.py:501-513; mcp/src/agents_remember/models/knowledge/result.py:516-528; mcp/src/agents_remember/models/knowledge/result.py:531-543`; ``CreateRevisionResult`; `CreateInvariantResult`; `RepositoryCreationResult`` → `mcp/src/agents_remember/models/knowledge/result.py:380-397; mcp/src/agents_remember/models/knowledge/result.py:400-413; mcp/src/agents_remember/models/knowledge/result.py:592-606`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): **re-read this card against the current source and moved the count it states as a fact.** `KS-R18@v1` registers two operation members, so the measured union is now **thirty-nine** rather than thirty-seven, and the body names them with the reason they are a pair rather than one: authoring a binding and reading a selected view's citation closure are different acts, the read is the one that must answer with a per-state enumeration rather than with whatever rows come back, and neither member can carry a verdict or mint a gate. The refusal vocabulary is unchanged at forty-five, and the body now says so explicitly for this leaf too (L8, L10, L11 and L18 added none) — a leaf that adds operations and no code is a fact worth stating rather than leaving to be re-derived. Two citation ranges were **re-cited by hand**: the operation literal widened to `:36-104` for the two inserted members, and a new row cites the two members' own lines. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): **extended the vocabulary to the mechanical-detection record group, re-counted both unions from the literal, and replaced the generated projection bullet on this card with this entry.** `KnowledgeOperation` gained **two** members (`record_detection_run`, `read_detection_run`) and `KnowledgeRefusalCode` **one** (`detection_self_reference`). Two operations rather than one for the reason the read pair and the diff pair are one each — recording a run and reading one back are different acts, and the read must answer with the run's *recorded order* rather than with whatever order rows come back in — and one code because only a detection write can reach the self-invalidating sequence it names: a signal is a measurement of an already-existing dataset, so a write whose target store **is** one of the datasets the run assessed would move the digest of the dataset it just digested. **Two measured corrections to this card's own counts, made because the claims were false against the source rather than merely stale:** the operation union is **thirty-seven**, not the twenty-six the L8 entry recorded (that was a count of the members that leaf could see; L10's route pair, L11's seven facet operations and L14's two are members now), and the code union is **forty-five**, not forty-four. The body now says so in place, and the two rows that carried the old numbers were re-cited against the current literal (`:36-96`, `:101-171`). Five further rows were **re-cited by hand** rather than machine-projected — `KnowledgeRefusal` (:163 → :175), the two outcome-consistency rules (:176-201 → :188-202 and :205-213), `RevisionDraft` (:189 → :216), the two label-edit request and result rows (which named two anchors across ranges that no longer held them and are now one anchor per row) and `RealizationClaimRequest` (:246-311 → :317-323) — and the projection bullet that had produced the `KnowledgeRefusal` range was removed, because a mechanically projected range is unverified evidence and an agent has now read each declaration it points at. Verification metadata advances to the leaf's base commit `4264dcc9` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): No content impact: this leaf changed the *cited* sources, not this file's own source, and the card's claim bytes were re-read against the current anchored construct and retained; only citation ranges were re-derived where a cited file grew. No row, citation or claim was deleted, and the verification metadata is not advanced because the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): **extended the operation union to the baseline-to-candidate comparison and re-derived every citation range against the new bytes.** `KnowledgeOperation` gained **one** member, `diff_knowledge_scope` — one rather than two for the same reason the read pair is one: a first comparison and a continuation are two ways of asking one question and a caller branches on the refusal code, not on which of the two it passed. **The measured union is now twenty-six operations, and the code union stays at forty-four: L8 added no refusal code at all.** That is recorded as a fact rather than a silence — the comparison's whole failure surface is R07's own six codes plus `selected_input_unavailable`, which the L4 publication path already produced, and a one-sided absence travels as a **value beside the page** (`side_absences`) rather than as a seventh refusal — and the card says so explicitly, because "this leaf needed no new vocabulary" and "this leaf's vocabulary was never reviewed" must not read alike. Every citation below the operation insertion moved by four lines and was re-measured rather than shifted. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): **extended the vocabulary to the selective recorded-scope read and re-measured both unions.** `KnowledgeOperation` gained **one** member (`read_knowledge_scope` — one rather than two because a seed and a continuation are two ways of asking the same question and a caller branches on the refusal code, not on which of the two it passed) and `KnowledgeRefusalCode` gained **six**: `selector_absent`, `registration_absent`, `page_budget_too_small`, `continuation_binding_mismatch`, `snapshot_unavailable` and `selection_incomplete`. The card records why each is a distinct next action — the two **absence** codes are separated by which question the caller got wrong and neither is a verdict of "no semantic impact"; the budget refusal reports the exact minimum and leaves the position unchanged; the binding refusal returns **no items**; `snapshot_unavailable` is also what an unreadable schema generation surfaces as, so the read does **not** use `unsupported_schema`; and the bound refusal emits no total and no partial manifest. **Two measured corrections to this card's own counts:** the union is **twenty-five operations and forty-four codes** on the frozen candidate, and the "thirty-seven codes" the previous entry recorded was already one short of the **thirty-eight** the union held at this leaf's own base — the numbers here are now counted from the literal rather than carried. Every citation range in this card was re-derived against the working tree, because both insertions moved every anchor below them. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): **extended the vocabulary to the portable export/import boundary and corrected this card's vocabulary account, which the L5 pass had left describing the L4 list.** `KnowledgeOperation` gained two members (`export_knowledge_dataset`, `import_knowledge_dataset` — two rather than one for the same reason the merge pair is split: an export answers "what is this dataset, logically" and an import answers "may this artifact become a dataset here", and a caller branches on which of the two it asked) and `KnowledgeRefusalCode` gained **one**: `invalid_export`. The card records why that one code is the narrowest member of the vocabulary: the portable artifact is the only input on any of these paths that can be **malformed as a document** (an unknown envelope field, a missing manifest key, a repeated JSON key, a row whose fields are not the declared columns in declared order, a value the declared type cannot hold, or a text that is not the canonical rendering of the document it holds), and no other code could tell a caller "your document is wrong" as distinct from "your records are not this schema's knowledge" — that second fact stays `relationship_constraint`, emitted by the staged-database check. It also records that one code deliberately covers both the malformed document and the incomplete dataset, and that the canonical-form refusal carries `record_id == "<canonical document>"` so the two facts remain distinguishable. **The prose lists are now the measured ones**: the operation union and the code union both state every generation's additions with the count (thirty-seven codes), because the L5 pass recorded its merge additions in this card's history while leaving the body lists at their L4 state. Every citation range in this card was re-derived against the working tree — both insertions moved every anchor below them, and the graph/L1 rows had additionally drifted — and the card's `governingOverview` link was repaired from `../../../overview.md` (the application route) to the models route overview. Verification metadata: lastUpdated advanced, commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): **extended the vocabulary to the guarded common-base merge, and re-derived every citation range in this card against the new bytes.** `KnowledgeOperation` gained two members (`resolve_merge_base`, `merge_knowledge_datasets`) and `KnowledgeRefusalCode` gained twelve (`common_base_unavailable`, `common_base_ambiguous`, `common_base_mismatch`, `schema_mismatch`, `missing_required_table`, `conflicting_values`, `duplicate_relationship`, `delete_reference_conflict`, `immutable_revision_changed`, `session_unavailable`, `changeset_incomplete`, `changeset_postcondition_failed`) — one per observable failure point of base resolution, structural preflight, changeset coverage and application, because the twelve have twelve different next actions and one code would have collapsed them. Two members are operations rather than one because base resolution is a separately refusable step. The card states the three distinctions on this path a later reader must not flatten: `duplicate_identity` is produced even when both sides' payloads are byte-identical (two independent insertions of one identity are two authored acts), `delete_reference_conflict` is orientation-independent and names no row because the engine hands the conflict callback no change at all, and `conflicting_values` is a whole-application rollback rather than a resolution policy. Their producers are the ten factories in the new `merge_refusals.py`, cited here so the vocabulary and its producers stay one record. Every pre-existing citation range in this card was re-derived against the working tree, because the two insertions moved every anchor below them. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): **extended the vocabulary to the candidate lifecycle and snapshot publication, and corrected this card's `unsupported_schema` producer claim.** `KnowledgeOperation` gained six members (`create_candidate`, `clone_candidate`, `open_candidate`, `publish_snapshot`, `read_published_snapshot`, `dispose_candidate`) and `KnowledgeRefusalCode` gained seven (`selected_input_unavailable`, `candidate_binding_changed`, `candidate_snapshot_unpublished`, `snapshot_incomplete`, `destination_stale`, `publication_failed`, `publication_durability_unconfirmed`) — one per observable failure point, because a caller publishing or opening a candidate has seven different next actions that one code would have collapsed. The card states the two distinctions a later reader must not flatten: `snapshot_incomplete` covers both a freeze that did not complete and a candidate private stage that could not be sealed (nothing outside the operation's own stage exists in either case), and `publication_durability_unconfirmed` is the honest answer for a replacement that completed but could not be re-read. It also corrects the earlier claim that `unsupported_schema` has **no producer**: the publication gate and the candidate lifecycle now emit it for a selected input that is not a database of this schema, while the store's own open path still reports its own schema mismatches as `KnowledgeStorageError` — the split is deliberate. The `no_change` distinction is restated with the publication result state added to it, so all three vocabularies (two result states and one reserved code) are named in one place. Citation ranges in this card were re-derived against the working tree and the pre-existing rows whose ranges no longer held their anchors were corrected. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): **extended the vocabulary to the candidate-write boundary and recorded the code-versus-state distinction as a carried limitation.** `KnowledgeOperation` gained the two label edits and `change_candidate` (a batch's refusals have to name the operation the caller addressed); `KnowledgeRefusalCode` gained `target_not_candidate` and `promotion_not_supported`, the two candidate-boundary conditions that are refused before any DML, while the `task-candidate` lane deliberately reuses `unauthorized_scope` because it is an authority the operation does not hold rather than a new class of failure. The card also records the two label-edit request/result pairs and why they have their own validators instead of reusing `require_stored_outcome` (`labeled` is a third state), points at `models/knowledge/candidate.py` for the batch vocabulary, and states as a carried limitation that the refusal *code* `no_change` still has no producer while the *result state* `MutationResult.state == "no_change"` is the reachable vocabulary. Verification metadata remains closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded two claims of the L1 card and extended the vocabulary to the graph half.** `KnowledgeOperation` is no longer a three-member union (eight graph operations were added) and `KnowledgeRefusalCode` now declares sixteen codes, with `stale_precondition` and `unknown_family` introduced and `missing_expected_row` becoming reachable through the three removals. The card's statement that "`unsupported_schema` and `missing_expected_row` … this leaf's code does not raise" is corrected to name `unsupported_schema` as the one code with no producer and `no_change` as a result state rather than a refusal. The card also now records the extracted outcome-consistency helpers the eight graph results reuse and the anchor-endpoint union that keeps naming-an-anchor distinct from recording one. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new typed request/refusal/result vocabulary. It records that `RevisionDraft` has no digest field by design and that two declared codes are not raised by the current write path. Verification metadata remains empty until closeout stamps the code commit.

