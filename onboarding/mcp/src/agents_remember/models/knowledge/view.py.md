# mcp/src/agents_remember/models/knowledge/view.py

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

**A realization row reports the place its claim was recorded at, and what it reports is the recorded value rather than a derived one.** `InvariantRow` and `FamilyRow` now declare the same three optional fields — `role: RealizationRole | None`, `path: str | None` bounded by `REFERENCE_MAX_LENGTH`, and `locator: SourceLocator | None` — so a view that answers "where is this realized" carries a place and not only prose. The row used to carry the claim id, the invariant revision id and the authored rationale, which told a caller that a realization existed and nothing about where; the location was already recorded against the claim, so the projection was dropping an answer it had been handed rather than failing to find one. Nothing is derived: the fields travel exactly as the store recorded them, through the same locator decoder `SourceContextRow.locator` already used, so two views cannot disagree about one claim's place and no view reads a filename out of a statement. Both models are one shape behind more than one row kind, so the fields appear on every row of their view as explicit `null`s — the convention this module already had for `SourceContextRow.anchor_state`, because `knowledge_read_payload` serializes with `model_dump(mode="json")` and no `exclude_none`. **`ReviewMatrixRow` and `CurationQueueRow` deliberately do not gain them**: no candidate feeding either view sets a `path` or a `locator`, so there is no recorded location for them to drop and an added field would be a field nothing can populate.

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

**The reader port is a protocol of five methods, and the result carries exactly one outcome.** `ViewSourceRow`
is the recorded row as the port hands it over, its `payload` being the record revision's recorded payload
decoded from the store's `TEXT_JSON` column, and its docstring states that a view "reads these values; it does
not recompose them, and it never derives a field from a symbol name, a path prefix, a directory depth or a file
extension". `ViewSourceCounts` reports the two registered totals the port can give for one snapshot.
`KnowledgeViewReader` is a `@runtime_checkable` `Protocol` declaring exactly `snapshot()`,
`registered_counts()`, `rows(record_kind)`, `family_member_rows()` and `anchor_state(locator)` — the port is
the view's whole
environment, so "a view that opens the database directly has left the contract" is "a property of the type
rather than of a reviewer's attention". `family_member_rows()` is the one method that exists because a generic
read cannot answer its question: family membership is a recorded generation-1 entity with its own table and is
**not** duplicated into the `knowledge_record`/`record_revision` envelope `rows(record_kind)` reads, so asking
that method for the kind `family_member` returned no rows on a dataset that holds them — and a family view
then reported a joint guarantee, no members, no implementation locations and a complete answer. The method's
own docstring records the same distinction, and declaring it is what makes the read a typed call rather than a
string a caller can spell into an empty answer. `ViewRequest` names the view, the repository, the optional invariant and
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
- **A view reads through the port and holds nothing else.** `KnowledgeViewReader` declares five methods
  (`snapshot`, `registered_counts`, `rows`, `family_member_rows`, `anchor_state`) and no path, connection or
  candidate tree, and every row a payload carries is built from `ViewSourceRow` values or `SubjectRef`
  references.
- **A recorded entity that its generic read cannot reach gets its own port method.** `family_member_rows()`
  exists because membership lives in its own generation-1 table and is not copied into the envelope
  `rows(record_kind)` reads; the alternative — asking the envelope for the kind by name — answers "no rows" on
  a dataset that holds membership, which is an empty answer indistinguishable from a real absence at the call
  site. The port method is the typed spelling of the question, so a reader that cannot answer it fails to
  satisfy the protocol rather than returning empty.
- **Machine work and curator judgment stay in separate models.** `MachineWorkItem` declares no disposition,
  rationale or author field and `CuratorDisposition` declares no condition code, matched fact or detection
  identity, so a `CurationQueueRow` cannot present a detector's row wearing a curator's name or the reverse.
- **An unclassifiable value is reported, not classified.** `UnresolvedLimitation` carries `code`, `detail` and
  an optional `subject` and no class, severity or ranking, and `Provenance` in
  `models/knowledge/classification.py` has no constructor for an empty class, so the value is not emitted with
  one.
- **A recorded location is reported, never derived, and only where one exists.** `InvariantRow` and
  `FamilyRow` carry `role`, `path` and `locator` exactly as the store recorded them, on the rows that are a
  realization claim, and both views decode the one stored locator through the same adapter
  `SourceContextRow` uses, so two views cannot disagree about one claim's place and no view reads a path out
  of authored prose. The fields are optional because a row kind that has no location must be able to say so:
  every `statement` row of the invariant view carries `None` in all three. `ReviewMatrixRow` and
  `CurationQueueRow` declare none, because no candidate feeding either view sets a `path` or a `locator`.
- **An unreadable read is not an empty row set.** `ViewReaderError` is a `RuntimeError`, `ViewRefusal` is a
  state whose holder "has no rows", and `ViewResult._require_one_outcome` refuses a result that carries both a
  payload and a refusal or neither.
- **Bounding is declared, not implied.** `MAX_VIEW_ROWS` is `64`, `ViewRequest.limit` is bounded by it, and
  `ViewPayload.ordering_rule_ids` must name rules of `MECHANICAL_RULES`, so a page size and an ordering rule
  cannot arrive as a renderer's private choice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The rows below ground the card's claims in the declarations themselves: the five names and their per-view
phrases, the counts and the two stated quantity states, the scope and continuation a bounded response carries,
the ordering closure with its registered tiebreak, the row shapes that keep the packet's distinctions apart, the
payload validator that enforces honest bounding, the page size, the reader port, and the request and result that
carry exactly one outcome.

- The five view names in the design's own order, derived from the closed literal, and the module docstring stating that the five names are the contract. [1]
- The published phrase per view that describes what the view selects and, as its comment states, carries no ordering claim. [2]
- The one declared tiebreak rule, the position record that must name it, and the builder that fills it against the admitted ordering input. [3]
- The read failure raised rather than absorbed, the six refusal codes, and the refusal shape whose holder has no rows and which always names a next action. [4]
- The nine quantities a bounded response must expose, one field per quantity on the counts record so none can be omitted, and the validator that keeps each one either counted or an explicitly stated absence. [5]
- The builder that turns each `None` into a stated absence with a per-quantity reason, and the two state helpers it uses. [6]
- The four inputs a completeness statement is scoped to and the field spelled so it cannot claim project semantics. [7]
- The opaque continuation bound to one snapshot and one view, its minter, and the check that refuses a token presented against another snapshot while naming both digests. [8]
- Where a value whose classification cannot be determined lands: reported instead of guessed, with no class, severity or ranking. [9]
- The recorded subject a row is about, and the refusal of a row set in which one subject appears at two positions. [10]
- The closure of ordering to the four admitted inputs, refused with the admitted set as its expected value and with no fallback order. [11]
- The no-consequence statement whose stored claim reference is required exactly when the statement is authored. [12]
- The four per-view row shapes with their closed fact-kind literals, the member-record-versus-attributed-source locus, the assessment and source-change states and the conditions-omitted flag. [13]
- The machine-selected work item with no judgment field, the separately attributed curator disposition with no detector field, and the row composing them. [14]
- The payload validator that ties rows-remaining to the continuation, the continuation to the view and snapshot, the completeness scope to the payload's snapshot, and every ordering rule to the registry. [15]
- The discriminated union that keeps each payload's concrete row type, the declared page size, and the tuple of the five payload classes. [16]
- The reader port as a runtime-checkable protocol of five methods — including the membership read a generic kind lookup cannot answer — and the recorded row and registered totals it hands a view. [17]
- One view request with its bounded limit and admitted ordering input, and the result that must carry a payload or a refusal and never both. [18]
- The optional source-path seed on the read request, and the shipped `PathSeed` rule the request's own validator uses instead of copying it: a path no stored anchor could carry selects nothing by construction rather than by a lookup that happens to miss. [19]
- The three optional location fields a realization row carries — the recorded role, path and locator, reported by the invariant and the family view alike — and the one stored locator both decode through. [20]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A view is a selection over one repository's stored
knowledge at one named snapshot, every row it carries is a recorded row of that store or a reference into it,
and the port it reads through is declared here rather than bound to any external system.

No meaningful cross-repo references found.
