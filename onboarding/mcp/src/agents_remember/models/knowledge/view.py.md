# mcp/src/agents_remember/models/knowledge/view.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/view.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T15:30+02:00 |
| lastVerifiedCommitHash | `5d64af264dc89b51d5c5e6454216573abde3c12e` |
| lastVerifiedCommitDate | 2026-09-20T02:50:22+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l32-ar`, uncommitted; base `7dcec036094768c5f50e571fb45e59a27ae78efc` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

The five query views of `KS-R20@v1`, declared so that the design's rule is "structural" rather than
documented: the module's docstring quotes `Doc13:233` — the product's views are "deterministic selections and
renderings of stored knowledge, observed changes, and existing assessments -- not new model-authored answers"
— and draws its two consequences here. The first is that a view returns "recorded facts and their provenance
classes, and nothing it computed", every ordered or qualified value carrying a
`models/knowledge/classification.py` `Provenance` "as a *sibling* field of that value". The second is that a
view "reads through a port and never through a database", `KnowledgeViewReader` being the only way this
vocabulary obtains a row. **What it deliberately does not have**, in the docstring's own words: "There is no
field anywhere below for a score, a rank, a weight, a severity, a percentage, a summary or a conclusion -- so a
view cannot acquire one by accident"; no sixth view or synonym, because "The five names are the contract" and
"the name a caller passes is one of these five"; and no connection, path or candidate tree, so that "A view
module that opened a connection, or that read the candidate tree to reconstruct what a record says, would not
typecheck against this interface at all". It also does not present a bounded response as a complete one: the
completeness field is spelled `complete_within_declared_scope` "so that no reader can take it for a statement
about the project's actual semantics", and a payload that "returned a first page without a continuation would
fail `ViewPayload`'s own validator".

## Code Commentary

### Logic

**The five names are a closed literal in the design's order, and each payload pins the one it is.**
`ViewName = Literal["source_context", "invariant", "family", "review_matrix", "curation_queue"]` with
`VIEW_NAMES = get_args(ViewName)` is `Doc13:235-239`'s list "spelled the same and in the same order";
the constant is now declared as `tuple[ViewName, ...]` rather than `tuple[str, ...]`, so a consumer that
iterates it is iterating **admitted view names** and does not have to re-narrow what `get_args` erased —
the runtime value is the same five strings, and a caller holding a plain `str` must still satisfy
`ViewRequest`'s own check. `VIEW_PURPOSES: Mapping[str, str]` supplies one published phrase per view for the interface `KS-R22@v1` mounts
and, as its comment says, describes "what the view selects; they are not a second content list and they carry no
ordering claim". Each of `SourceContextView`, `InvariantView`, `FamilyView`, `ReviewMatrixView` and
`CurationQueueView` narrows `view` to a single-member `Literal` and adds one `rows` tuple of its own row type,
`ViewPayloadUnion` discriminates the union on `view`, and `VIEW_PAYLOADS` lists the five classes in the same
declared order.

**Every required quantity is present on every view, and an absent measurement is stated rather than zero.**
`CountState = Literal["counted", "not_applicable"]` with the `COUNTED` and `NOT_APPLICABLE` members,
`COUNT_QUANTITIES` names the nine quantities "a bounded response" must expose, and `ViewCounts` declares exactly
those nine fields, so a view cannot satisfy "every quantity is present" by omitting one. `CountQuantity` carries
`state`, an optional non-negative `value` and an optional `reason`, and `_require_a_stated_state` refuses a
counted quantity with no value ("a count is not optional"), a counted quantity carrying a reason, a
`not_applicable` quantity carrying a value ("reporting a zero here would read as a measurement") and a
`not_applicable` quantity with no reason, so "omission is never silent". The helpers `_counted` and
`_not_applicable` build the two states, and `view_counts` turns each `None` argument into a per-quantity stated
absence — for example "this view is not scoped to a registered realization set" — so a caller "cannot leave a
quantity out: it either has a measurement or it has a reason named here".

**Completeness and continuation both carry the scope they were made about.** `ViewScope` names `Doc13:227`'s
four inputs individually — `snapshot_logical_digest` validated by `SHA256_PATTERN`, `recorded_graph`,
`traversal_policy` and an `extractors` tuple — so "a changed extractor set makes two otherwise identical
payloads distinguishable". `ViewCompleteness` then carries `complete_within_declared_scope: bool` beside that
scope, the field name being the guarantee. `ViewContinuation` carries an opaque `token`, the `view` that minted
it and the `snapshot_logical_digest` it is bound to, `continuation_for` mints one as
`f"{view}:{snapshot.logical_digest}:{position}"`, and `require_continuation_snapshot(continuation, snapshot)`
returns `None` on agreement or a `ViewRefusal` with code `continuation_binding_mismatch` naming both digests,
because a caller "that cannot see which two snapshots disagreed cannot fix the call".

**Ordering is closed at four admitted inputs and every position names the registered tiebreak that placed it.**
`ORDERING_PROVENANCE_RULE` is the single module value `("ordering.declared-tiebreak", 1)`, and the comment beside
it states that requirement 2.4's permitted alphabetical tiebreak is "permitted only as this declared ordering,
and only when everything declared has tied". `OrderedPosition` carries a `position` with `ge=1`, the
`ordering_input` that produced the order, the `provenance` of *the position*, and the tiebreak `rule_id` and
`rule_version`; `_require_the_declared_tiebreak` refuses a position that names no tiebreak ("so two runs at one
snapshot can be compared") and calls `mechanical_rule(self.tiebreak_rule_id, self.tiebreak_rule_version)` so an
unregistered rule "would be exactly the inline comparator requirement 2.2 forbids". `ordering_position` checks
its input through `require_admitted_ordering_input` and fills the tiebreak pair from `ORDERING_PROVENANCE_RULE`,
and `require_admitted_ordering_input` returns `None` for one of `ORDERING_INPUTS` or a `ViewRefusal` with code
`unadmitted_ordering_input` whose `expected` is the admitted set joined and whose detail records that "the view
does not fall back to a default order".

**The row shapes keep the distinctions the packet requires apart, by declaring closed literals instead of free
text.** `SourceContextRow.fact_kind` is a five-member `Literal` and its `assessment_state` is
`Literal["assessed", "missing", "not_applicable"]` defaulting to `not_applicable`, because "a fact whose
assessment is absent says so here, and the absence is never filled with a favourable default".
`InvariantRow.fact_kind` is a nine-member `Literal` and its `conditions_omitted` flag exists because a compact
view "may shorten prose it is licensed to shorten, but it may not drop the conditions under which the invariant
applies". `FamilyRow.change_locus` is `Literal["member_record", "attributed_source", "both", "neither"]`,
requirement 1.2's distinction made into a field. `ReviewMatrixRow` holds references rather than "re-rendered
content for the records other leaves own", with `assessment_status` reading `assessed`, `missing` or `stale` and
`source_change_state` reading `changed`, `unchanged` or `not_selected` because source is selected "by the
*registered links*, not by a path comparison"; it deliberately does not restate a requirement revision or an
effect claim, since that "would become a second renderer of it". The same separation governs the curation
queue, where machine work and curator judgment are two models and never one row's merged content:
`MachineWorkItem` carries a work item id, a condition code, the condition vocabulary version, matched facts and
a registered scope status — and "deliberately no field for a disposition, a rationale or an author", which is
requirement 1.6 as a shape obligation. `CuratorDisposition` symmetrically carries its own id, disposition, rationale, author
reference, origin state and provenance, "and no field here for a condition code, a matched fact or a detection
identity". `CurationQueueRow` composes them as an `item` plus an optional `disposition`, so a row carries at
most one separately attributed disposition, and `NoConsequenceStatement` adds
`_require_the_claim_only_when_authored`, which refuses a `claim_ref` exactly when the statement is not an
authored one ("a mechanical determination writes no authored record to name"). `require_distinct_row_subjects`
completes the row contract: it refuses a row set in which one `(record_kind, record_id, revision_id)` appears
twice, under code `ambiguous_row_identity`, "rather than choosing which row is authoritative".

**The payload's validator is the structural form of honest bounding.** `ViewPayload` carries the view name, the
`KnowledgeReadSnapshot`, the counts, the completeness statement, an optional continuation, a `limitations` tuple
of `UnresolvedLimitation`, an `ordering_rule_ids` tuple and a `renderer_version`. `_require_honest_bounding`
refuses a payload whose `rows_remaining` is not counted, ties `remaining.value > 0` to the presence of a
continuation in both directions ("a bounded response never presents its first page as the whole scope"), requires
the continuation's view and snapshot digest to agree with the payload's own, requires the completeness scope's
digest to be the payload's snapshot, and refuses any `ordering_rule_ids` entry that is not a rule id of
`MECHANICAL_RULES`, since "an inline comparator cannot acquire a rule id by being spelled like one".
`MAX_VIEW_ROWS = 64` is the declared page size — it "bounds one response; it never narrows a selection" — and
`ViewRequest.limit` both defaults to it and is bounded by it with `ge=1, le=MAX_VIEW_ROWS`.

**The reader port is a protocol of four methods, and the result carries exactly one outcome.** `ViewSourceRow`
is the recorded row as the port hands it over, its `payload` being the record revision's recorded payload
decoded from the store's `TEXT_JSON` column, and its docstring states that a view "reads these values; it does
not recompose them, and it never derives a field from a symbol name, a path prefix, a directory depth or a file
extension". `ViewSourceCounts` reports the two registered totals the port can give for one snapshot.
`KnowledgeViewReader` is a `@runtime_checkable` `Protocol` declaring exactly `snapshot()`,
`registered_counts()`, `rows(record_kind)` and `anchor_state(locator)` — the port is the view's whole
environment, so "a view that opens the database directly has left the contract" is "a property of the type
rather than of a reviewer's attention". `ViewRequest` names the view, the repository, the optional invariant and
family revisions, the optional `source_path` seed (a caller who knows only a file can ask what governs it
without first discovering a revision id, and the field's validator constructs the shipped `PathSeed` rather
than restating its rule, so "a path that no stored anchor could carry selects nothing by construction rather
than by a lookup that happens to miss"), the record kinds, the ordering input (defaulting to `stable_ordering`, "the only one that
needs nothing authored to exist"), the limit and an optional continuation. `ViewResult` carries
`state: Literal["view", "refused"]` and `operation: Literal["read_knowledge_view"]`, and `_require_one_outcome`
refuses a `view` state without a payload or with a refusal and a `refused` state without a refusal or with a
payload. `ViewReaderError` is a `RuntimeError` raised rather than absorbed, because "an empty result and an
unreadable input are different facts", and `ViewRefusal` carries one of the six `ViewRefusalCode` members, the
view, a detail, the optional offending input, expected and observed values, and a required `next_action` — a
refusal being "a state, never a degraded success". `UnresolvedLimitation` is where requirement 2.1 lands: an
unclassifiable value "is not emitted at all", and the record carries `code`, `detail` and an optional `subject`
and "no class, no severity and no ranking".

### Conventions

Every shape is a `KnowledgeModel` subclass, so `extra="forbid"` and `frozen=True` inherited from
`models/knowledge/base.py` are what refuse an undeclared field on a row, a payload or a refusal. Bounded text
reuses the base constants rather than literals: `LABEL_MAX_LENGTH` for view names, record kinds, fact and
disposition labels, lifecycles, condition codes and `renderer_version`, `PROSE_MAX_LENGTH` for refusal details,
`next_action`, statements, a continuation token and a rationale, `REFERENCE_MAX_LENGTH` for record and revision
identities, `offending_input`/`expected`/`observed`, claim references and repository ids, and `SHA256_PATTERN`
for the two digests a snapshot scope and a continuation are bound to. `PATH_MAX_LENGTH` is not imported, because
no shape here holds a filesystem path.

Declarations that must agree are one declaration. `VIEW_NAMES` is `get_args(ViewName)`, declared as
`tuple[ViewName, ...]` so its element type is the admitted vocabulary rather than `str` (a narrowing with no
runtime effect); `COUNT_QUANTITIES` is
the list `ViewCounts` declares field for field; `ORDERING_PROVENANCE_RULE` is the one place the declared
tiebreak pair is spelled and `ordering_position` reads it; `MAX_VIEW_ROWS` is simultaneously the declared page
size and `ViewRequest.limit`'s default and upper bound; and `VIEW_PAYLOADS` lists the same five classes
`ViewPayloadUnion` discriminates, with every payload subclass adding only its own narrowed `view` literal and its
`rows` tuple. Vocabularies belonging to other modules are imported rather than re-declared: `OrderingInput`,
`ORDERING_INPUTS`, `Provenance`, `AUTHORED_CLASS`, `MECHANICAL_RULES` and `mechanical_rule` from
`models/knowledge/classification.py`, `RealizationRole` from `models/knowledge/graph.py`, and
`AnchorResolutionState` together with `KnowledgeReadSnapshot` from `models/knowledge/read.py`. `__all__` names the
forty-five public names this module adds — eight constants, five payload classes, twenty-seven other classes and
type aliases, and five module functions — and it does not name the private helpers `_counted` and
`_not_applicable`.

### Invariants And Boundaries

- **Five views and no sixth.** `ViewName` is a five-member `Literal`, `VIEW_NAMES` is `get_args` of it — and
  is *typed* as the five names (`tuple[ViewName, ...]`), so a reader or a type checker sees the admitted
  vocabulary rather than five arbitrary strings, while the request's own field check is still what refuses a
  caller-assembled name — each
  payload narrows `view` to its own single member, and `ViewPayloadUnion` discriminates on that field, so a
  caller-assembled view name cannot be spelled into existence.
- **A truncated payload cannot be built without its continuation, and a complete one cannot carry one.**
  `_require_honest_bounding` ties `rows_remaining > 0` to the presence of a continuation in both directions,
  requires the continuation's view and snapshot digest to match the payload's, and requires the completeness
  scope digest to be the payload's own snapshot.
- **A zero is never an absent measurement.** `CountQuantity` refuses a value on a `not_applicable` quantity and
  a reason on a counted one, and `view_counts` names a per-quantity reason for every `None` it receives, so the
  nine required quantities are present on every view in one of the two stated forms.
- **Ordering is admitted or refused, never defaulted.** `OrderedPosition` requires a registered tiebreak pair
  and `require_admitted_ordering_input` returns a typed refusal for anything outside `ORDERING_INPUTS` with the
  admitted set as its `expected`; `ViewRequest.ordering_input` defaults to `stable_ordering` rather than replacing
  a fifth input a caller names.
- **A view reads through the port and holds nothing else.** `KnowledgeViewReader` declares four methods
  (`snapshot`, `registered_counts`, `rows`, `anchor_state`) and no path, connection or candidate tree, and every
  row a payload carries is built from `ViewSourceRow` values or `SubjectRef` references.
- **Machine work and curator judgment stay in separate models.** `MachineWorkItem` declares no disposition,
  rationale or author field and `CuratorDisposition` declares no condition code, matched fact or detection
  identity, so a `CurationQueueRow` cannot present a detector's row wearing a curator's name or the reverse.
- **An unclassifiable value is reported, not classified.** `UnresolvedLimitation` carries `code`, `detail` and
  an optional `subject` and no class, severity or ranking, and `Provenance` in
  `models/knowledge/classification.py` has no constructor for an empty class, so the value is not emitted with
  one.
- **An unreadable read is not an empty row set.** `ViewReaderError` is a `RuntimeError`, `ViewRefusal` is a
  state whose holder "has no rows", and `ViewResult._require_one_outcome` refuses a result that carries both a
  payload and a refusal or neither.
- **Bounding is declared, not implied.** `MAX_VIEW_ROWS` is `64`, `ViewRequest.limit` is bounded by it, and
  `ViewPayload.ordering_rule_ids` must name rules of `MECHANICAL_RULES`, so a page size and an ordering rule
  cannot arrive as a renderer's private choice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below ground the card's claims in the declarations themselves: the five names and their per-view
phrases, the counts and the two stated quantity states, the scope and continuation a bounded response carries,
the ordering closure with its registered tiebreak, the row shapes that keep the packet's distinctions apart, the
payload validator that enforces honest bounding, the page size, the reader port, and the request and result that
carry exactly one outcome.

| Finding | Anchor | Source |
| --- | --- | --- |
| The five view names in the design's own order, derived from the closed literal, and the module docstring stating that the five names are the contract. | `VIEW_NAMES`; `ViewName` | mcp/src/agents_remember/models/knowledge/view.py:1-73; mcp/src/agents_remember/models/knowledge/view.py:115-124; mcp/src/agents_remember/models/knowledge/view.py:119-124 |
| The published phrase per view that describes what the view selects and, as its comment states, carries no ordering claim. | `VIEW_PURPOSES` | mcp/src/agents_remember/models/knowledge/view.py:113-142 |
| The one declared tiebreak rule, the position record that must name it, and the builder that fills it against the admitted ordering input. | `ORDERING_PROVENANCE_RULE`; `OrderedPosition`; `ordering_position` | mcp/src/agents_remember/models/knowledge/view.py:154-162; mcp/src/agents_remember/models/knowledge/view.py:86-86; mcp/src/agents_remember/models/knowledge/view.py:650-665; mcp/src/agents_remember/application/knowledge_view_render.py:76-76; mcp/src/agents_remember/application/knowledge_view_render.py:360-360; mcp/src/agents_remember/application/knowledge_view_render.py:1048-1048; mcp/src/agents_remember/models/knowledge/view.py:162-162; mcp/src/agents_remember/models/knowledge/view.py:615-647; mcp/src/agents_remember/models/knowledge/view.py:633-649 |
| The read failure raised rather than absorbed, the six refusal codes, and the refusal shape whose holder has no rows and which always names a next action. | `ViewReaderError`; `ViewRefusalCode`; `ViewRefusal` | mcp/src/agents_remember/models/knowledge/view.py:159-165; mcp/src/agents_remember/models/knowledge/view.py:168-176; mcp/src/agents_remember/models/knowledge/view.py:179-193 |
| The nine quantities a bounded response must expose, one field per quantity on the counts record so none can be omitted, and the validator that keeps each one either counted or an explicitly stated absence. | `COUNT_QUANTITIES`; `ViewCounts`; `_require_a_stated_state` | mcp/src/agents_remember/models/knowledge/view.py:195-208; mcp/src/agents_remember/models/knowledge/view.py:211-242; mcp/src/agents_remember/models/knowledge/view.py:245-262 |
| The builder that turns each `None` into a stated absence with a per-quantity reason, and the two state helpers it uses. | `view_counts`; `_counted`; `_not_applicable` | mcp/src/agents_remember/models/knowledge/view.py:265-270; mcp/src/agents_remember/models/knowledge/view.py:273-331 |
| The four inputs a completeness statement is scoped to and the field spelled so it cannot claim project semantics. | `ViewScope`; `complete_within_declared_scope` | mcp/src/agents_remember/models/knowledge/view.py:347-359; mcp/src/agents_remember/models/knowledge/view.py:362-372 |
| The opaque continuation bound to one snapshot and one view, its minter, and the check that refuses a token presented against another snapshot while naming both digests. | `ViewContinuation`; `continuation_for`; `require_continuation_snapshot` | mcp/src/agents_remember/models/knowledge/view.py:366-377; mcp/src/agents_remember/models/knowledge/view.py:380-389; mcp/src/agents_remember/models/knowledge/view.py:392-414; mcp/src/agents_remember/application/knowledge_views.py:68-68; mcp/src/agents_remember/application/knowledge_views.py:145-145; mcp/src/agents_remember/models/knowledge/view.py:552-552; mcp/src/agents_remember/models/knowledge/view.py:552-574 |
| Where a value whose classification cannot be determined lands: reported instead of guessed, with no class, severity or ranking. | `UnresolvedLimitation` | mcp/src/agents_remember/models/knowledge/view.py:417-429; mcp/src/agents_remember/application/knowledge_view_render.py:19-19; mcp/src/agents_remember/application/knowledge_view_render.py:71-71; mcp/src/agents_remember/application/knowledge_view_render.py:204-204; mcp/src/agents_remember/application/knowledge_view_render.py:280-280; mcp/src/agents_remember/application/knowledge_view_render.py:285-285; mcp/src/agents_remember/models/knowledge/view.py:577-589 |
| The recorded subject a row is about, and the refusal of a row set in which one subject appears at two positions. | `SubjectRef`; `require_distinct_row_subjects` | mcp/src/agents_remember/models/knowledge/view.py:437-442; mcp/src/agents_remember/models/knowledge/view.py:552-576; mcp/src/agents_remember/application/knowledge_view_render.py:70-70; mcp/src/agents_remember/application/knowledge_view_render.py:180-180; mcp/src/agents_remember/application/knowledge_view_render.py:453-453; mcp/src/agents_remember/application/knowledge_view_render.py:472-472; mcp/src/agents_remember/models/knowledge/view.py:712-736; mcp/src/agents_remember/models/knowledge/view.py:597-602 |
| The closure of ordering to the four admitted inputs, refused with the admitted set as its expected value and with no fallback order. | `require_admitted_ordering_input` | mcp/src/agents_remember/models/knowledge/view.py:498-522; mcp/src/agents_remember/application/knowledge_view_render.py:74-74; mcp/src/agents_remember/application/knowledge_view_render.py:277-277; mcp/src/agents_remember/models/knowledge/view.py:658-658; mcp/tests/test_knowledge_views_and_projection.py:63-63; mcp/tests/test_knowledge_views_and_projection.py:195-195; mcp/src/agents_remember/models/knowledge/view.py:658-682 |
| The no-consequence statement whose stored claim reference is required exactly when the statement is authored. | `NoConsequenceStatement`; `_require_the_claim_only_when_authored` | mcp/src/agents_remember/models/knowledge/view.py:695-710; mcp/src/agents_remember/application/knowledge_view_render.py:66-66; mcp/src/agents_remember/application/knowledge_view_render.py:363-363; mcp/src/agents_remember/application/knowledge_view_render.py:367-367; mcp/src/agents_remember/application/knowledge_view_render.py:375-375; mcp/src/agents_remember/models/knowledge/view.py:695-695; mcp/src/agents_remember/models/knowledge/view.py:695-719; mcp/src/agents_remember/models/knowledge/view.py:713-719 |
| The four per-view row shapes with their closed fact-kind literals, the member-record-versus-attributed-source locus, the assessment and source-change states and the conditions-omitted flag. | `FamilyRow`; `change_locus`; `conditions_omitted`; `source_change_state` | mcp/src/agents_remember/models/knowledge/view.py:756-894; mcp/src/agents_remember/application/knowledge_view_render.py:62-62; mcp/src/agents_remember/application/knowledge_view_render.py:926-926; mcp/src/agents_remember/application/knowledge_view_render.py:935-935; mcp/src/agents_remember/application/knowledge_view_render.py:896-896; mcp/src/agents_remember/application/knowledge_view_render.py:917-917; mcp/src/agents_remember/application/knowledge_view_render.py:931-931; mcp/src/agents_remember/models/knowledge/view.py:894-894 |
| The machine-selected work item with no judgment field, the separately attributed curator disposition with no detector field, and the row composing them. | `MachineWorkItem`; `CuratorDisposition`; `CurationQueueRow` | mcp/src/agents_remember/models/knowledge/view.py:864-870; mcp/src/agents_remember/application/knowledge_view_render.py:63-63; mcp/src/agents_remember/application/knowledge_view_render.py:1018-1018; mcp/src/agents_remember/application/knowledge_view_render.py:1032-1032; mcp/src/agents_remember/application/knowledge_view_render.py:1049-1049; mcp/src/agents_remember/application/knowledge_view_render.py:1054-1054; mcp/src/agents_remember/models/knowledge/view.py:849-862; mcp/src/agents_remember/models/knowledge/view.py:834-847; mcp/src/agents_remember/models/knowledge/view.py:867-868 |
| The payload validator that ties rows-remaining to the continuation, the continuation to the view and snapshot, the completeness scope to the payload's snapshot, and every ordering rule to the registry. | `ViewPayload`; `_require_honest_bounding` | mcp/src/agents_remember/models/knowledge/view.py:728-772; mcp/src/agents_remember/models/knowledge/view.py:906-906; mcp/src/agents_remember/application/knowledge_projection.py:54-54; mcp/src/agents_remember/application/knowledge_projection.py:90-90; mcp/src/agents_remember/application/knowledge_projection.py:105-105; mcp/src/agents_remember/application/knowledge_projection.py:187-187; mcp/src/agents_remember/models/knowledge/view.py:907-932; mcp/src/agents_remember/models/knowledge/view.py:888-932 |
| The discriminated union that keeps each payload's concrete row type, the declared page size, and the tuple of the five payload classes. | `ViewPayloadUnion`; `MAX_VIEW_ROWS`; `VIEW_PAYLOADS` | mcp/src/agents_remember/models/knowledge/view.py:97-97; mcp/src/agents_remember/models/knowledge/view.py:990-993; mcp/src/agents_remember/models/knowledge/view.py:997-997; mcp/src/agents_remember/models/knowledge/view.py:999-1005 |
| The reader port as a runtime-checkable protocol of four methods, and the recorded row and registered totals it hands a view. | `KnowledgeViewReader`; `ViewSourceRow`; `ViewSourceCounts` | mcp/src/agents_remember/models/knowledge/view.py:845-869; mcp/src/agents_remember/models/knowledge/view.py:872-891; mcp/src/agents_remember/application/knowledge_view_render.py:64-64; mcp/src/agents_remember/application/knowledge_view_render.py:540-540; mcp/src/agents_remember/application/knowledge_view_render.py:573-573; mcp/src/agents_remember/application/knowledge_view_render.py:620-620; mcp/src/agents_remember/models/knowledge/view.py:1033-1051; mcp/src/agents_remember/models/knowledge/view.py:1025-1029; mcp/src/agents_remember/models/knowledge/view.py:1005-1022 |
| One view request with its bounded limit and admitted ordering input, and the result that must carry a payload or a refusal and never both. | `ViewRequest`; `_require_one_outcome` | mcp/src/agents_remember/models/knowledge/view.py:1078-1109; mcp/src/agents_remember/models/knowledge/view.py:1122-1127; mcp/src/agents_remember/application/knowledge_projection.py:54-54; mcp/src/agents_remember/application/knowledge_projection.py:208-208; mcp/src/agents_remember/application/knowledge_view_render.py:75-75; mcp/src/agents_remember/application/knowledge_view_render.py:580-580; mcp/src/agents_remember/models/knowledge/view.py:1078-1078; mcp/src/agents_remember/models/knowledge/change_set.py:280-287 |
| The optional source-path seed on the read request, and the shipped `PathSeed` rule the request's own validator uses instead of copying it: a path no stored anchor could carry selects nothing by construction rather than by a lookup that happens to miss. | `ViewRequest`; `source_path`; `PathSeed`; `_require_a_confined_path_seed` | mcp/src/agents_remember/models/knowledge/view.py:1078-1109; mcp/src/agents_remember/models/knowledge/view.py:1091-1091; mcp/src/agents_remember/models/knowledge/view.py:1097-1110 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A view is a selection over one repository's stored
knowledge at one named snapshot, every row it carries is a recorded row of that store or a reference into it,
and the port it reads through is declared here rather than bound to any external system.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T02:24+02:00 — 260915-KS-L32 curator, post-sync citation pass (uncommitted change set on `ar/260915-ks-l32-ar`, code base `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`, memory base `4ffb8d8d3ff372847784fe8f7d2a13e57d9509a5`): re-measured this card after the master-line sync and the settled resolution pass, and it carries **no enforced finding**: the report's repairable set holds no row of this card, and the rows the previous pass cleared stay cleared against the merged tree. The one change made here is bookkeeping: the `reviewedWorkingCandidate` row named the superseded `ar/260915-ks-l20` candidate at base `9f88a6de`, a base the merged candidate no longer stands on, and now names this leaf's candidate `ar/260915-ks-l32-ar` at base `7dcec036` — the same candidate every other row of this block was read against. The card's `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained unchanged (the closeout's memory leg requires it present), no claim was re-worded, no anchor, row or citation was added, removed or dropped, and no stamp was advanced or invented.
- 2026-09-20T02:12+02:00 — 260915-KS-L32 memory-side conflict resolution (uncommitted; this worktree, code base `7dcec036`, merged tree = L30's landed `7ca3ac48` plus this leaf's four modified paths): **resolved both reference rows and the Update History block.** Every cell cites this leaf's two modified paths (`models/knowledge/view.py`, `application/knowledge_view_render.py`), so this leaf's ranges were kept; upstream's side left `ViewName`, `ORDERING_PROVENANCE_RULE`, `_require_the_claim_only_when_authored`, `source_change_state`, `ViewPayloadUnion` and `ViewSourceRow` cited at ranges that no longer hold them. Where **both** sides were wrong for the merged tree the cell was cited fresh against the construct's own current declaration: `view.py:535-559` (and upstream's `525-549`) → `view.py:695-710` — `NoConsequenceStatement`'s declaration through the stored-claim-reference field its claim is about; and the renderer cells `489/493/501` (upstream `358/362/370`) → `363/367/375`, the `_consequence` builder and its two branch constructions; and `909/918/923/324/321` (upstream `778/787/792/193/190`) → `926/935/896/917/931`, the family renderer's own `FamilyRow`, `change_locus` and `conditions_omitted` uses. `view.py:756-894` and `894-894` are this leaf's already-correct repoints and were kept. No claim was re-worded, no anchor, row or citation dropped, and no verification stamp advanced.
- 2026-09-20T01:39:03+02:00 — 260915-KS-L32 curator (uncommitted change set on `ar/260915-ks-l32-ar`, code base `7dcec036`, memory base `66b2ae8a`): **cleared the five enforced `citation_anchor_absent_from_range` rows this card carried.** In every one of them the Finding text, the Anchor cell and the row itself are unchanged and no citation was dropped; the stale cell was replaced by the range that actually holds the construct the row names, each read in the code worktree before it was written. The cause is common to all four: this card's `models/knowledge/view.py` and `application/knowledge_view_render.py` cells had been advanced by a fixed arithmetic offset that the real layout never had, so the constructs had moved by different amounts. (a) The tiebreak row: `455-487` (a span that now holds the continuation helpers) reads `86-86`, the `OrderedPosition` export in `__all__`, because the class's own extent `615-647` is already cited in the same row; `490-505` reads `650-665`, the declaration extent of `ordering_position`; and the three `knowledge_view_render.py` cells read `76-76` (the module's `ordering_position` import), `360-360` (the one call to it) and `1048-1048` (where `_queue_row` consumes a position as `OrderedPosition`). (b) The queue-row row: `666-702` reads `864-870` (`CurationQueueRow` itself), `856-862` reads `849-862` (`CuratorDisposition`), `841-853` reads `834-847` (`MachineWorkItem`), `826-838` reads `867-868` (the two fields that compose the row), and the five `knowledge_view_render.py` cells read the module's own five holds of `CurationQueueRow` at `63`, `1018`, `1032`, `1049` and `1054`. (c) The union row: `984-989` reads `97-97` (the `ViewPayloadUnion` export), `991-993` reads `990-993` (the union itself), `995-1001` reads `997-997` (`MAX_VIEW_ROWS = 64`) and `997-997` reads `999-1005` (the `VIEW_PAYLOADS` tuple). (d) The request row: `894-910` reads `1078-1109` (the `ViewRequest` class), `913-928` reads `1122-1127` (`ViewResult._require_one_outcome`), `1054-1070` reads `1078-1078` (the class's own line), and the two `knowledge_view_render.py` cells read `75-75` (the import) and `580-580` (a `request: ViewRequest` parameter); the `knowledge_projection.py` and `change_set.py` cells are unchanged because they already hold `ViewRequest` and `_require_one_outcome`. (e) The source-path-seed row: `1088-1088` reads `1078-1109`, the `ViewRequest` class the row is about; `1091-1091` is left as written because it is the line that declares `source_path`, and `1097-1110` is left as written because it holds all three of the remaining anchors — `@field_validator("source_path")` at `1097`, `_require_a_confined_path_seed` at `1099` and the shipped `PathSeed` it constructs at `1102` and `1109`. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a row, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T01:23+02:00 — 260915-KS-L30 curator, final citation pass (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared the 5 enforced `citation_anchor_absent_from_range` rows this card carried by RANGE REPAIR.** Every flagged range was hand-read against this candidate and repointed to the declaration extent of the anchor it was written for: `source_change_state` `view.py:880-880` → `view.py:889-889` (the field sits below the assessment-status line); `CurationQueueRow` `view.py:846-852` → `view.py:859-865`, `CuratorDisposition` `view.py:831-843` → `view.py:844-856`, `MachineWorkItem` `view.py:816-828` → `view.py:829-841` (the three queue-row models, each range still the one written for that model); and `ViewPayloadUnion` `view.py:974-979` → `view.py:985-988` (the `Annotated[...]` union itself, with `MAX_VIEW_ROWS` `:992-992` and `VIEW_PAYLOADS` `:994-1000` already correct and left standing). The pairing of each range to its anchor was fixed by the construct the range held at the revision its numbers were true at (the queue-row models at 816/831/846, `source_change_state` at 876 before its earlier repair, the union range beside `MAX_VIEW_ROWS`), so no citation changed which anchor it belongs to and none was dropped. Each named claim's wording was re-read at the repointed construct and retained: the machine item still declares no judgment field, the disposition no detector field, the queue row composes them, the union still pins each payload's concrete row type, and the source-change state is still a literal of three recorded states. No claim, anchor or other citation was added, removed or re-worded. **Stamp position:** unchanged — this card advances no verification stamp in this pass and no commit hash was written; closeout owns the stamp once the code commit exists.
- 2026-09-20T00:46:52+02:00 — 260915-KS-L32 curator (uncommitted change set on `ar/260915-ks-l32-ar`, code base `7dcec036`, memory base `66b2ae8a`): **body update for the request's new path seed, and the stale ranges this card carried.** `ViewRequest` gained `source_path`, so the read request now names the optional seed a caller who knows only a file can present, validated by constructing the shipped `PathSeed` rather than restating its rule; the reader-port paragraph and a new row state it. Citation repair in the same pass, all of it this leaf's own `+10` shift (the import block and the new field/validator sit above every construct below them, so nothing semantic changed and no claim was re-read as false): `ViewName` `106-111; 113-118` → `115-124` (with `ViewName` itself at 119 and `VIEW_NAMES` at 124), `ORDERING_PROVENANCE_RULE` `144-149` → `154-162`, `OrderedPosition` `445-477` → `455-487`, `ordering_position` `480-495` → `490-505`, `_require_the_declared_tiebreak`/`640-655` → `650-667`, `NoConsequenceStatement` `525-549` → `535-559` and `_require_the_claim_only_when_authored` `685-709` → `695-719`, the four-row-shape row `746-884` → `756-894` (so `source_change_state` at 894 is inside it), `CurationQueueRow` `656-692` → `666-702`, `MAX_VIEW_ROWS` `981-983` → `991-993` (definition at 997 added), `VIEW_PAYLOADS` `985-991` → `995-1001`, `ViewPayloadUnion` `974-979` → `984-989`, `ViewSourceRow` `835-859` → `845-869`, `KnowledgeViewReader` `862-881` → `872-891`, and `ViewRequest`/`_require_one_outcome` `884-900; 903-918` → `894-910; 913-928`. The card's `knowledge_view_render.py` citations were repointed by the same `+131` shift the sibling card records (`67`→`198`, `352`→`483`, `909`→`1040`, `190`→`321`, `193`→`324`, `409`→`540`, `442`→`573`, `489`→`620`, `778`→`909`, `787`→`918`, `792`→`923`, `879`→`1010`, `893`→`1024`, `910`→`1041`, `915`→`1046`), each verified against the construct it names rather than shifted blindly. The pre-existing `Update History` entries were left in the order the incoming line carried them; only the earlier accidental duplication of the 19:38+02:00 entry was removed, so the block still reads newest-first by absolute time (19:38+02:00 is 17:38Z, later than 17:54:55Z). No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 2 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `MAX_VIEW_ROWS`; `VIEW_PAYLOADS`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-18T18:04:10+00:00: 260915-KS-L23 residue clearance (seat A, follow-up): the five-view-names row's third citation widened from `mcp/src/agents_remember/models/knowledge/view.py:113-113` to `:113-118`, so the range now holds both declarations the row names: `ViewName` at 113 and `VIEW_NAMES` at 118, the latter having moved five lines down -- which is why the reopen item named `VIEW_NAMES`. Nothing was removed: the row still cites the module docstring (`:1-31`) and the `__all__` region (`:106-111`) beside the widened range, and the claim's wording is retained. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:54:55+00:00: 260915-KS-L23 residue clearance (seat A): `ViewReaderError` repointed from `view.py:152-158` to `view.py:159-165` — the new range holds the `RuntimeError` subclass itself; `ViewRefusalCode` repointed from `:161-168` to `:168-176` — the new range holds the six-member refusal-code literal; `ViewRefusal` repointed from `:171-184` to `:179-193` — the new range holds the refusal shape and its seven fields; `complete_within_declared_scope` repointed from `:354-363` to `:362-372` — the new range holds `ViewCompleteness` with the measured field on it, and its sibling range now holds `ViewScope`'s four inputs (`:347-359`); `ViewPayloadUnion` repointed from `:810-815` and `:817-827` to `:974-979` — the new range holds the discriminated union itself; `MAX_VIEW_ROWS` repointed from `:981-981`, `:981-987`, `:979-979` and `:972-975` to `:981-983` — the new range holds the declared page size; `VIEW_PAYLOADS` repointed from `:972-972` to `:985-991` — the new range holds the five-class tuple; `source_change_state` repointed from `view.py:876-876` to `view.py:880-880` and its sibling `view.py:582-720`, `view.py:791-791` and `view.py:791-813` ranges to `view.py:746-884` — the new range spans the four per-view row shapes the finding names, so `FamilyRow`, `change_locus` and `conditions_omitted` are held by it as well as `source_change_state`, while the `knowledge_view_render.py` citations were each read against their own occurrence and left standing. Claim re-read against each construct, wording unchanged. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T19:38+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the element type this module's one changed declaration now carries, and corrected the card's account of it. `VIEW_NAMES` is declared `tuple[ViewName, ...]` instead of `tuple[str, ...]` (`view.py:113-118`), a **narrowing** whose runtime value is unchanged: the constant is the five admitted view names, and `get_args` had erased that, so a consumer holding a plain `str` had to satisfy the request model's own check at every call site (the pyright error this clears is at the root of both `ViewRequest(view=<str>)` reports). The Logic paragraph on the five names, the "declarations that must agree are one declaration" convention and the "Five views and no sixth" invariant now say the element type is the admitted vocabulary rather than `str`, and that the request's own field check is still what refuses a caller-assembled name. No other declaration in the module moved, no row, citation or range was rewritten, and no verification stamp advanced (the source is uncommitted and closeout owns the stamp).
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): created this one-to-one card for the five query views — their names, typed payloads, counts, scope and continuation. It records that the five names are a closed literal in the design's order with each payload pinning its own member, that the nine required quantities are present on every view as either a count or a stated `not_applicable` reason, that ordering is closed to the four admitted inputs with every position naming the registered declared tiebreak, and that `_require_honest_bounding` ties rows-remaining to the continuation and every named ordering rule to the registry. It also states the deliberate absences the module docstring names — no field anywhere for a score, rank, weight, severity, percentage, summary or conclusion, no sixth view, and no connection, path or candidate tree behind the reader port — together with the row shapes that keep machine work items and curator dispositions apart and route an unclassifiable value to `UnresolvedLimitation`. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
