# mcp/src/agents_remember/models/knowledge/result.py

## Governing Overview

[models route overview](../overview.md)

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
rather than on which of the two it passed. **The measured union is fifty operations**, re-counted from
the literal on this candidate rather than carried forward: the L10 route pair (`author_route`,
`set_governing_route`), L11's six facet acts (`add_facet`, `attach_facet`, `remove_facet_attachment`,
`author_explanation`, `add_explanation_revision`, `designate_explanation`), L11's own read
(`read_facet_scope`), L14's two detection operations (`record_detection_run`, `read_detection_run`),
L19's two requirement-revision operations (`record_requirement_revision`, `read_requirement_revisions`),
L17's three composition operations, L18's two citation-binding operations and **L16's two:
`construct_registered_scope` and `compose_family_integrity_report`** are all members now, and the L8
entry's "twenty-six" was a count of the members *that leaf* could see rather than a count of the union.
**A count this card carried is corrected in place rather than shifted**: the "thirty-nine" the L19 entry
recorded was measured against a literal that already declared **forty-eight** members at this leaf's own
base — so the number was wrong rather than stale — and the literal is the authority.
**The refusal vocabulary is untouched by L16**: a scope-construction refusal reuses the shipped codes and
the family-integrity report adds no code of its own, so `KnowledgeRefusalCode` is still **forty-five
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

**Three operation members, two writes and one read.** `add_evidence_claim`, `add_verification_observation` and `read_evidence_scope` join `KnowledgeOperation`. The two writes are separate members rather than one because a caller branches on which authored act it performed and each carries its own remedy — recording a claim about what evidence covers is a different act from recording that a command ran — while the batch that carries either command restates its refusals as `change_candidate`. The read is its own member for the reason the facet read and the detection read are: it is a question rather than an act, and its refusals are about the snapshot rather than about a payload. `KnowledgeRefusalCode` is unchanged by this leaf: every refusal the supporting records produce reuses a shipped code.

- **`database_frozen` (L37, MIK-R37 rule 3)** joins `KnowledgeRefusalCode`: a database write or publication
  into a converted memory tree is refused by name, because that tree's knowledge is text written by the curator
  file writer and its database file is frozen in place until MIK-R26 removes it. The addition is additive; no
  other code changed.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The declared mutating-operation vocabulary, including the six L4 operations, the two L5 merge operations, the two L6 portable operations, the one L7 read operation, the one L8 comparison operation, the two L10 route operations, **the seven L11 facet operations, the two L14 detection operations, the two L19 requirement-revision operations and the two L16 family-integrity operations** — **fifty members, re-counted from the literal on this candidate**, whose declaration is `:36-157`. [1]
- **The two members this leaf added, each for the reason written beside it in the source: the scope construction is neither the retrieval selection nor the composition traversal, and the pipeline's composition act is neither the construction nor a record read — and no refusal code was added with either.** [2]
- The declared refusal vocabulary, with each member naming a distinct observable failure — the seven L4 codes, the twelve L5 merge codes, the one L6 portable code, the six L7 read codes (L8, L10, L11, L16 and L18 added none) **the one L14 detection code** and the cutover's `database_frozen` (260928-MIK-L37); forty-six members, re-counted from the literal, over `:161-236`. [3]
- **The six L7 codes' producers, one factory per observable failure point, each carrying the next action a caller needs.** [4]
- **The read's own result model, which is a page or a refusal and never both, and the read operation literal it carries.** [5]
- The refusal value carrying code, operation, offending record and next action. [6]
- The two shared outcome-consistency rules every result model calls. [7]
- The digest-free caller draft that refuses a self-declared predecessor. [8]
- The two label-edit requests, each naming the row the caller read. [9]
- The family-label request that names the row the caller read. [10]
- The invariant-label result and its `labeled`/`refused` consistency validator. [11]
- The family-label result and its `labeled`/`refused` consistency validator. [12]
- The batch vocabulary that carries the change request and its factual receipt. [13]
- The graph's request vocabulary and the anchor-endpoint union. [14]
- The realization-claim request the graph half added. [15]
- The eight graph result models that reuse the shared outcome rules. [16]
- The three L1 outcome models the shared rules were extracted from. [17]
- **The seven factories that produce this leaf's codes, one per observable failure point.** [18]
- The factories that build every other refusal in this package, one per code and case. [19]
- The two result states that carry `no_change` and the two operations that reach them. [20]
- The refusal value carrying code, operation, offending record and next action. [21]
- The two shared outcome-consistency rules every result model calls. [22]
- The digest-free caller draft that refuses a self-declared predecessor. [23]
- The two label-edit requests, each naming the row the caller read. [24]
- The family-label request that names the row the caller read. [25]
- The invariant-label result and its `labeled`/`refused` consistency validator. [26]
- The family-label result and its `labeled`/`refused` consistency validator. [27]
- The batch vocabulary that carries the change request and its factual receipt. [28]
- The graph's request vocabulary and the anchor-endpoint union. [29]
- The realization-claim request the graph half added. [30]
- The eight graph result models that reuse the shared outcome rules. [31]
- The three L1 outcome models the shared rules were extracted from. [32]
- **The seven factories that produce this leaf's codes, one per observable failure point.** [33]
- The factories that build every other refusal in this package, one per code and case. [34]
- The two result states that carry `no_change` and the two operations that reach them. [35]
- **The ten factories that produce this leaf's twelve merge codes, one per observable failure point**, including the two structural refusals that run before a session exists. [36]
- **The five factories that produce the portable boundary's codes in this leaf's own refusal module, one per observable failure point.** [37]
- **The one L6 code's dedicated refusal identity: the canonical-form refusal, whose `record_id` distinguishes "not this format" from "this format, spelled differently".** [38]
- The node that asserts the portable boundary's refusal codes by code rather than by message. [39]

- The refusal code of a database write into a converted tree. [44]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
- The declared mutating-operation vocabulary, including the six L4 operations, the two L5 merge operations, the two L6 portable operations, the one L7 read operation, the one L8 comparison operation, the two L10 route operations, the seven L11 facet operations, **the two L14 detection operations, the two L18 citation-binding operations and the two L16 family-integrity operations** — fifty members, re-counted from the literal on this candidate. [40]
- The declared refusal vocabulary, with each member naming a distinct observable failure — the seven L4 codes, the twelve L5 merge codes, the one L6 portable code, the six L7 read codes (L8, L10, L11, L16 and L18 added none) **the one L14 detection code** and the cutover's `database_frozen` (260928-MIK-L37); forty-six members, re-counted from the literal. [41]
- The eight graph result models that reuse the shared outcome rules, cited at their own declarations rather than at one of them. [42]
- The three L1 outcome models the shared rules were extracted from, cited at their own declarations. [43]
