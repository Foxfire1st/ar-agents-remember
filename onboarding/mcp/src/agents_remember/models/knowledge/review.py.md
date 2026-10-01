# mcp/src/agents_remember/models/knowledge/review.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The Intent Reviewer surface's own vocabulary: what the three panes carry, and nothing more. This
module **defines no record kind**. Every value here is a rendering of records another owner already
stores, or a stated absence where no record exists. The one thing it does own is the shape of a
display, and that shape is where the display's prohibitions are enforced — the source's own five
bullets:

- **There is no field a conclusion could be assembled in.** No summary, no narrative, no severity, no
  score, no conflict verdict, no causal explanation and no approval exists anywhere in this
  vocabulary, so the surface cannot grow one by filling a blank that happens to be there.
- **Unassessed is the absence of a value, never a value.** An assessment is `None` or it is a record
  with an author and examined inputs; there is no "compatible", no "no concern recorded" and no
  default disposition that could stand in for a judgement nobody made.
- **A missing side is a state, not an empty string.** `ReviewSideContent` refuses to carry text unless
  it is `present`, so a missing operand renders as its own named state rather than as a blank that
  reads like an empty file.
- **The stale rule is structural.** A payload whose comparison is stale must carry the submission
  state that disables submission against it, and one that is current must not.
- **A signal is not a finding, and the vocabulary keeps them apart.** A mechanical detection fact
  carries its matched condition, its inputs, its versions and its scope limitations and has no field
  for a voice, a severity or a disposition.

## Code Commentary

### Logic

**Two recorded constants and three closed unions are the module's vocabulary-level declarations.**
`KNOWLEDGE_REVIEW_SURFACE_VERSION` is `"knowledge-review-surface/1"` — a recorded value rather than a
package version read at display time, so two payloads produced by different renderings are
distinguishable from the payloads themselves — and it is the default of the payload's
`surface_version` field. `REVIEW_PANE_NAMES` is `("knowledge", "source", "evidence")`, the three panes
as a tuple rather than three separately spelled strings. `PROPOSED_ASSESSMENT_DISPOSITIONS` publishes
`RRD:366`'s three dispositions verbatim — `concern_found`, `no_concern_found`, `unresolved` — so a
reviewer can see which judgements are expressible; the source comment states that none of them is
publication approval. `ReviewRefusalCode` is the closed **seven**-member union
`candidate_unresolved`, `candidate_not_live`, `candidate_dataset_absent`, `subject_unresolved`,
`comparison_refused`, `source_content_unresolved`, `review_adapter_unavailable`, and `ReviewSideState`
the four-member union `present`, `absent`, `binary`, `unresolved`. The seventh member is this leaf's own
additive change and it names the one refusal the **entry-content** route answers with: the listed
generation no longer resolves to the two code objects the listing published, so there are no bytes to
serve. It is additive in the strict sense — the union is a closed vocabulary a client reads, not a
control flow, and every code the transport does not recognise already answers `400`, so a client
written against the six keeps working and an unknown code is refused rather than silently mapped onto
an existing answer. `ReviewSubjectKind` is the closed two-member
`invariant`/`family` union, **declared here once** so the transport's `SELECTOR_KINDS`, the entry list
and the panes cannot come to disagree about which identities are reviewable; the browser's
`ReviewSelectorKind` is the same two spellings on the wire.

**`ReviewSideContent` is where "a missing side is a state" becomes unconstructible otherwise.** Its
`_require_text_exactly_when_present` validator refuses a `present` side with `text is None` — "a
present side with no text is absent" — and refuses any non-`present` side that carries text, with the
reason spelled out: rendering an absent, binary or unresolved operand as text is how a missing side is
read as an empty one. That rule is what feeds the surface's diff renderer rather than asking it to
infer the case.

**`ReviewSurfaceRequest` is one spelling of "what was asked".** It carries `repository_id`, `master`,
`leaf_id` and a `selector` that is one of the read operation's own declared seeds — `KnowledgeReadSeed`
— and nothing else. No display version, no insertion instant and no "latest" flag is representable, so
none of them can select. The transport parses this value from its query string and the composition
consumes the same value, so there is no separate wire shape to keep in agreement with a domain shape.

**`ReviewCandidateRef` and `ComparisonIdentity` are the two identity values, and neither can address a
database.** `ReviewCandidateRef` carries only task identities — repository, master, leaf, an optional
`task_ref` — and the docstring states that no filesystem path appears in it, which is the point: the
browser chooses the task context and the resolution layer chooses the candidate. `ComparisonIdentity`
carries the shared operation's own values and nothing recomputed: `reference`, `policy_version`, the
`binding_digest`, the `selector_digest`, both declared snapshot digests, and both optional code tree
ids.

**The display records each carry one prohibition, and it is a validator rather than a note.**
`ReviewAssessmentDisplay._require_the_basis_to_travel` refuses an assessment whose `author_ref` is
blank or whose `examined_inputs` is empty: "a disposition with no author is an anonymous verdict, and
an assessment that examined nothing cannot have been made *about* the subject it is shown beside."
`ReviewRemainingCount._require_a_stated_state` refuses a count with no value and no stated reason —
"an unexplained absent count reads as a zero" — and refuses a measured count that also carries a
not-applicable reason. `ReviewKnowledgePane._require_the_assessment_state_to_be_one_fact` keeps the
pane's singular `assessment` inside the `assessments` collection it displays, so the pane cannot
describe two different states of the same subject. `ReviewEvidencePane._require_the_states_to_match_their_collections`
ties `evidence_state` to `bool(evidence_links or observations)` and `assessment_state` to
`bool(assessments)`, refusing an empty corpus reported as recorded and a populated one reported as
empty. The pane also carries the composition's own record-availability list:
`ReviewEvidencePane.channels` is a tuple of
[`ReviewRecordChannel`](review_records.py.md), one entry per record class the composition read,
carried **whole** — a class that was not read, or could not be read, appears with that state instead
of being absent from the list — and deliberately not derived from the collection lengths here, because
an empty tuple has three possible meanings and the pane must be able to render all three without
claiming which one it is. It sits on this pane rather than beside the payload because this is the pane
that displays *records* rather than recorded knowledge, and it is read by a consumer that needs the
availability fact whichever pane renders the records. `ReviewStaleness._require_the_previous_input_to_be_labelled` refuses a `stale` state with no
`previous_comparison_ref` and a `current` state that carries one. `KnowledgeReviewResult._require_one_outcome`
refuses a `review` carrying a refusal and a `refused` carrying a payload.

**`ReviewKnowledgePane` keeps the authored records and the mechanical signals as separate typed
collections.** `authored_effects` holds `ReviewAuthoredEffect` and `signals` holds `ReviewSignal` —
two element types, so a rendering cannot place a signal where a finding goes without the type system
objecting first. `ReviewAuthoredEffect`'s `record_kind` is the closed three-member union
`invariant_effect_claim`, `preservation_claim`, `unresolved_question`, and it carries the author's own
`label`, `rationale` and `examined_inputs` with no field for a computed effect. `ReviewSignal` carries
the matched `condition`, the `input_set`, the `detected_at` route, its `relationship_paths`, the
`extractor_version`, the `policy_version` and `scope_limitations` — and deliberately no severity, no
verdict, no causal explanation and no author.

**The three panes are three models whose fields are the panes' own statements.** `ReviewSourcePane`
carries the selected `locations`, the published `remaining` counts, the `expansion_reference` and
`expansion_command`, the attributed, confirmed-unregistered and undetermined changed paths, the
`attribution` partition value those three lists are read from (so a path appears in exactly one of
them), and its own `unresolved` rows. The six persistent counts are declared once as
`ReviewRemainingCountName` — `unattributed_changed_paths` is the confirmed negative conclusion and
`unknown_attribution_changed_paths` is the measured population that conclusion could not be drawn
for, so a bare zero is never shown without the undetermined count beside it.
`ReviewSourceLocation` keeps `role` as `None` when the record carries none, so a missing role is
displayed as unclassified rather than guessed from a path, and carries the recorded and observed
source identities, the `resolution`, the three-member `change_state` and `before_only`. Since
`ICR-R08@v1` it also carries the association the address belongs to: `invariant_id` is the preserved
canonical identity both sides of a movement sit under, `recorded_side` says which snapshot's address
this row is, `transition` is the movement's own transition, `counterpart_path` names the other side's
recorded address **only when that side records exactly one** (several are listed by the movement and
none is chosen to stand for them), and `movement` carries the whole relationship — so the two rows of a
moved realization are readable as one association instead of two unrelated locations. The identity is
absent exactly when the traversal could not establish it, and the movement beside it states that as a
gap rather than the location inventing one. `ReviewSourcePane` gained `relationships` for the same
reason the locations are not enough: a family membership and a governing-route association have no
source address at all, and a movement whose two sides are one row at one address is still one
relationship rather than two locations.
`ReviewEvidenceLink` carries the claim's identity, its `claimed_coverage` and `limitations`, its
`assessment_refs` and its own `unresolved` rows; `ReviewObservation` carries what the run recorded —
the tested candidate, the command identity, the result artifact and its digest, the execution result
and the environment — with no field for a sufficiency verdict, which is what keeps a passing run from
being rendered as an invariant being satisfied. `ReviewUnresolvedReference` is the shared shape that
makes "cannot be resolved" a *displayed* fact: a `field`, the optional `recorded_reference` and a
`detail`.

**`ReviewSubmission` states the increment's boundary as data.** Its `state` is the two-member union
`unavailable` and `disabled_stale` — no favourable member — and it carries the `reason`, the
`next_action`, the `proposed_dispositions` the existing authority accepts, and `none_is_approval`,
which defaults to `True`.

**Pane 1 carries the explicit before/after revision selection the two statements were rendered
from (`ICR-R07@v1`).** `ReviewKnowledgePane.revision_selection` is an optional
`ReviewRevisionSelection` — the compared head pair, the one-sided head, or the explicit ambiguous
or unresolved selection that rendered no winner — and it is absent exactly when no subject was
compared (the task-context pane below), because a review that compared no operand selected no
revision either. The value itself is declared next door in
[`models/knowledge/revision_selection.py`](revision_selection.py.md), not here, so this file stays
under the soft rail; what lives here is the field and the one-direction validator
`_require_a_compared_subject_to_record_its_selection`, which refuses a recorded selection beside
anything but a compared subject. The direction is deliberate: a recorded selection implies a
compared subject, but a compared subject need not carry one — a selector that names no identity (a
path seed through the direct composition call) addresses no identity item, and recording a selection
there would invent the identity it never named.

**`KnowledgeReviewPayload` is where the stale rule becomes a constructor check.** Its
`_require_the_submission_state_to_follow_staleness` validator refuses a payload where
`staleness.state == "stale"` and `submission.state != "disabled_stale"` disagree in either direction,
with the reason that a stale comparison offered for submission, or a current one refused for staleness,
"is a review that would be reused against inputs it never examined." The same validator refuses a
`proposed_dispositions` entry that is not in `PROPOSED_ASSESSMENT_DISPOSITIONS`, so the surface
publishes the authority's declared dispositions and invents none. The payload's own fields are the
`surface_version`, the `candidate`, the `comparison`, the three panes, the `staleness`, the
`submission` and a `limitations` tuple.

**`ReviewRefusal` is a state and never a degraded success.** It carries the closed `code`, a `detail`,
a `next_action`, and the optional `offending_input`, `expected` and `observed`, so a caller that
receives one has no panes and cannot read their absence as a review of an empty candidate.
`KnowledgeReviewResult` then carries `state`, the literal `operation="read_knowledge_review"`, the
`repository_id`, and exactly one of `payload` and `refusal`.

**`ReviewEntry` is one subject of the comparison's before/after population, as the catalogue lists
it (`ICR-R09@v1`), and it exists so the task-view entry never has to invent one.** `selector_kind`,
`selector_id`, `label` and `presence` are the whole model: `selector_id` is the recorded identity
the review is opened with, `label` is that identity's own recorded display label (read from the
after snapshot when it records the identity, from the before snapshot otherwise), and `presence` —
the new `ReviewSubjectPresence` union `before_only`/`after_only`/`both` — states which of the two
snapshots record the identity, so a retired (before-only) subject and a newly added (after-only)
one are listed beside the subjects both snapshots hold rather than dropped to imply a smaller
complete population. There is deliberately **no field for a path, a file, a display version, a
ranking or a comparison count**, so an entry cannot point at a dataset the resolution did not
select, cannot be ordered by a preference this list invented, and cannot oblige the catalogue read
to compare every subject before answering. The deleted `selected_item_count` field (the per-subject
compare-to-earn-a-row count) was the wire carrier of the F06 mechanism; its removal is deliberate
and same-repo clients read `presence`/totals instead.

**`ReviewEntryListResult` is the entry read's typed outcome, and its validators are what keep
"nothing to review" distinct from "nothing could answer" and a whole catalogue distinct from its
first row.** It carries `state` (`entries` | `refused`), the literal
`operation="list_knowledge_review_entries"`, the task context (`repository_id`, `master`,
`leaf_id`), an `entries` tuple, an optional `refusal`, and the **labelled totals** —
`total_subjects`, `invariant_total`, `family_total` (each `ge=0`, defaulting to `0`).
`_require_one_outcome` refuses a `refused` state with no refusal, an `entries` state that carries a
refusal, and — the load-bearing one — **a refused read that offers any entry at all**: "a refused
entry read offers no subject; an entry beside a refusal is how a caller comes to review a subject
nothing admitted." The second validator (`_require_the_totals_to_describe_the_catalogue`) refuses a
total that does not sum its two kind totals, non-zero totals beside a refusal (a refused read
measured no catalogue), and — the `>=` rule R10's paging depends on — an `entries` state whose
`total_subjects` is smaller than the page beside it: "a smaller total is how a whole catalogue
comes to read as a first row." So an empty `entries` on an `entries` state is a pair that records
no subject (a fact about the datasets, stated as one, with the task-context source review still
reachable beside it), while a refusal is the resolution saying why it could not answer, and the two
cannot be confused by a caller that only reads the list.


**The wire shape gained the inventory and the two states that let a review exist without a subject.** This leaf added `ReviewChangedFile` (path, `status`, `content`, `mode_change`, and a `detail` required exactly when `content` is `unknown`), `ReviewUnrepresentablePath` (`path_bytes` — the exact bytes in an ASCII-safe spelling, never re-encoded), `ReviewSourceInventory` (`state` `measured`/`unavailable`, the entries, a `listed_total` checked against the list it describes, a `detail`, the reproducing `command`, both tree ids, and `unrepresentable_paths`, whose presence forces `measured` **and** `partial`), and `ReviewSourcePane.inventory` as a required first field. `ReviewSurfaceRequest.selector` became optional — its absence is the task context, not an empty subject — `ComparisonIdentity` gained `knowledge_compared` with an all-or-nothing validator over the selector and both snapshot digests, `ReviewKnowledgePane` gained `selection_state`/`selection_detail` with their own agreement rule, `ReviewStaleness.state` gained `not_compared`, and `KnowledgeReviewPayload.comparison` became optional with a validator tying its absence to `not_compared` and to the pane's `subject_selected`/`task_context` answer so a payload cannot disagree with itself.

### Conventions

Every model here is a `KnowledgeModel`, and the shared bounds are imported rather than restated:
`LABEL_MAX_LENGTH`, `PATH_MAX_LENGTH`, `PROSE_MAX_LENGTH`, `REFERENCE_MAX_LENGTH` and
`SHA256_PATTERN` come from `models/knowledge/base.py`, so a display field is bounded by the same
constants every other knowledge model uses. Identity fields use `REFERENCE_MAX_LENGTH`, prose uses
`PROSE_MAX_LENGTH`, and the four digests on `ComparisonIdentity` are constrained by `SHA256_PATTERN`
rather than by a length. `__all__` names the whole public vocabulary: the two constants
`KNOWLEDGE_REVIEW_SURFACE_VERSION` and `REVIEW_PANE_NAMES`, the dispositions tuple, and all
twenty-five models plus `ReviewRefusalCode`, `ReviewSubjectKind` and `ReviewSurfaceRequest`. It also
**re-exports** the three record-availability names — `ReviewRecordChannel`,
`ReviewRecordChannelState` and `ReviewRecordClassName` — from
[`models/knowledge/review_records.py`](review_records.py.md), where the vocabulary now lives in its own
module; the re-export is deliberate, so every importer that reached them through this module keeps
resolving and no second spelling of the states can appear. The selection value's import is the same
convention without the re-export: `ReviewRevisionSelection` is imported from
[`models/knowledge/revision_selection.py`](revision_selection.py.md) for the pane field and is **not**
re-exported through `__all__`, because no importer reached it through this module before — there is
no importer to keep resolving.
`ReviewRefusalCode`, `ReviewSubjectKind`, `ReviewSubjectPresence` and `ReviewSideState` are
`Literal` aliases rather than
`enum` classes, and the three closed `record_kind`, `side` and `change_state` vocabularies are inline
`Literal`s on their fields. Immutable collections are `tuple[...]` with `()` defaults, so no model
carries a mutable default — which is what lets `ReviewEntryListResult.entries` default to an empty
tuple and still mean "no subject was selected" rather than "the question was not answered".

### Invariants And Boundaries

- **The availability list is carried, never inferred.** `ReviewEvidencePane.channels` is the
  composition's own supply, one entry per class it read; this module defines the shape of the fact and
  no rule that could derive one from a collection's length.
- **No record kind is defined here.** The module declares no table, no status, no stored entity and no
  writer; every field renders a record some other owner stores, or states its absence.
- **No field can hold a conclusion.** There is no summary, severity, score, verdict, causal
  explanation or approval anywhere in the vocabulary — verified over the whole payload schema by a
  case in the surface's test module rather than over one model.
- **Unassessed is `None` or a record with an author and examined inputs.** There is no default
  disposition a renderer could fall back to.
- **A missing operand is its own named state.** `ReviewSideContent` cannot carry text unless the state
  is `present`, in either direction.
- **A stale comparison and a disabled submission are the same fact.** The payload validator refuses
  the two states disagreeing, so the rule is a property of the value rather than a client convention.
- **One refusal is a terminal state.** `KnowledgeReviewResult` cannot carry a payload and a refusal
  together, and a refusal is never a degraded payload. `ReviewEntryListResult` carries the same rule in
  its own direction: a refused entry read can offer **no** entry, so a caller can never be handed a
  subject beside the statement that nothing admitted one.
- **A recorded selection implies a compared subject, and only in that direction.** The pane's
  validator refuses a `revision_selection` beside a task-context pane, while a compared subject
  without one stays constructible for the selector that named no identity. An ambiguous or
  unresolved selection records heads and retained revisions with no pair, so no winner can be read
  where the policy chose none.
- **An entry cannot name a dataset, a path or a rank.** `ReviewEntry` carries a recorded identity,
  its own label and the presence the two snapshots give it, and nothing else — which is what keeps
  "the browser never chooses the candidate" a property of the value rather than a convention of its
  callers, and what keeps the catalogue read bounded: a count of comparison items on the entry would
  oblige the read to compare every subject before answering, which is exactly what `ICR-R09@v1`
  forbids.
- **`ReviewSubmission` has no favourable member.** Both `unavailable` and `disabled_stale` are
  statements that no assessment may be submitted from this surface.

### Todos

None recorded. The module ships the review surface display-only; the assessment-publication path is
the existing curator authority's and is deliberately not modelled here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and five
bullets, each model and its validator, the shared bounds it imports, and the cases that check the
prohibitions over the whole payload schema rather than over one model.

- The module's own statement of what it owns and the five prohibitions the display's shape enforces. [1]
- The published vocabulary: the constants, the dispositions tuple, the refusal-code union and the models, with the channel vocabulary re-exported from its own module. [2]
- **The recorded surface version, the three pane names, `RRD:366`'s three proposed dispositions verbatim, the closed refusal-code union (seven members since 260921-ICR-L3, which added `source_content_unresolved` to the six 260915-KS-L45 left), the two-member subject-kind union, the three-member subject-presence union (`before_only`/`after_only`/`both`, ICR-R09) and the four-member side-state union — re-read at the merged candidate.** [3]
- **The movement vocabulary this module re-exports in its own `__all__` (`ICR-R08@v1`): the movement, its sides and states, the authored lineage, the gaps with their codes and the labelled rename inference — declared next door beside the other payload vocabularies.** [4]
- The shared shape that makes an unresolved reference a displayed fact rather than a dropped or anonymous one. [5]
- **The missing-side rule as a constructor check: text exactly when `present`, in both directions.** [6]
- The one request shape: a task context plus one of the read operation's own declared seeds, with no display version, instant or "latest" flag representable. [7]
- The candidate reference, which carries task identities and never a filesystem path, and the comparison identity carried verbatim rather than recomputed. [8]
- The two per-side and per-item mechanical facts: the retained-revision count kept per side, and the field transition that states no meaning. [9]
- The authored record displayed as the author wrote it, with no field for a computed effect, and the detection fact with no severity, verdict or author. [10]
- **The validator that refuses an anonymous verdict or an assessment that examined nothing.** [11]
- The evidence claim reference with its own authored limitations, and the observation that has no field for a sufficiency verdict. [12]
- **The six persistent counts declared once, with the confirmed negative and the undetermined beside each other.** [13]
- **The selected location whose missing role stays unclassified rather than guessed from a path, and which since `ICR-R08@v1` carries the preserved identity, its own recorded side, the transition, the counterpart address (only when the other side records exactly one) and the whole movement.** [14]
- **Pane 1's own self-agreement rule: the pane's single assessment must be one of the assessments it displays, and the authored and mechanical collections keep separate element types. Pane 1's recorded selection: the optional `revision_selection` with its one-direction validator.** [15]
- **The explicit revision selection the pane carries: the compared head pair, the one-sided head, or the ambiguous/unresolved non-pair — declared next door, carried here, refused beside anything but a compared subject.** [16]
- **The inventory's own model, with the count checked against the list and the rule that an unrepresentable path makes the inventory measured and partial.** [17]
- **Pane 2: the selected locations, the traversed recorded relationships (the associations with no source address at all), the expansion, the carried partition and the three changed-path lists read from it.** [18]
- **Pane 3's two independent absence states, tied to the collections they describe, plus the availability list carried rather than inferred.** [19]
- The stale state that retains its previous input as a labelled value, and the rule that a current comparison has none to label. [20]
- The submission state with no favourable member, and the boundary that none of the published dispositions is approval. [21]
- **The whole payload and its stale/submission coupling, which refuses either direction of disagreement.** [22]
- The refusal that is a state and never a degraded success, and the result that carries exactly one outcome. [23]
- **The catalogue's entry: a recorded identity, its own label and the presence the two snapshots give it, with no field for a path, a file, a display version, a ranking or a comparison count — the deleted `selected_item_count` was the wire carrier of the per-subject compare-to-earn-a-row mechanism.** [24]
- **The entry read's typed outcome, whose validators refuse a refused read that offers any entry, non-zero totals beside a refusal, and a total smaller than the page beside it — so a caller can never be handed a subject beside the statement that nothing admitted one, nor a whole catalogue that reads as a first row.** [25]
- **The two subject kinds declared once here, so the transport's admission tuple, the entry list and the panes cannot disagree about which identities are reviewable.** [26]
- **The availability list the pane carries: one entry per record class the composition read, whole and underived.** [27]
- **The re-export that keeps every existing importer resolving while the vocabulary lives in its own module.** [28]
- The shared bounds and the `KnowledgeModel` base every model here uses rather than restating its own. [29]
- **The case that walks the whole payload schema for a field a generated conclusion could occupy.** [30]
- **The case that asserts this module declares no record kind, no table and no status of its own.** [31]
- The case that an unassessed subject is displayed unassessed and never defaulted to compatible, and the case that a missing side is its own state. [32]
- The case that a passing observation is displayed as an observation and never as invariant-satisfied, and the case that a signal carries facts and scope limitations with no severity. [33]
- **The two rules that were extracted out of this module and the movement that arrived beside them (`ICR-R22@v1`): `ReviewStaleness`, `ReviewSubmission` and the new `ReviewSyncMovement` are declared in the staleness module, and this module re-exports all three so its importers and tests keep resolving.** [34]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every model is a display shape over one
repository's records, and no field carries an identity that ranges beyond the repository namespace the
request names.

No meaningful cross-repo references found.

## 260921-ICR-L10 The Published Page Vocabulary And Its Constructor Check

`260921-ICR-L10` (`ICR-R10@v1`) adds the review surface's page vocabulary here, where the
surface's other published shapes live. `ReviewCollectionPage` publishes `collection`, `state`, `total`,
`returned`, `remaining`, the owner's opaque `continuation`, the active `scope`, `continued_from`, the
reset refusal and `total_basis`; `ReviewPagedCollection` names the two bounded collections once;
`MAXIMUM_REVIEW_PAGE_SIZE` and `REVIEW_PAGE_RESET_NEXT_ACTION` carry the surface's bound and its
new-generation action; the closed refusal-code union gained `comparison_page_reset` and
`comparison_page_unreadable`; `ReviewSurfaceRequest` gained `page_of`/`continuation`/`page_size`; and
`KnowledgeReviewPayload` gained `page` and a separate `page_refusal`.

**Two properties a later reader must not relax.** A page with a remainder cannot be *constructed*
without its cursor — the page value's own validator refuses `(remaining > 0) != (continuation is not
None)`, so "remaining=100 with no way to inspect them" is unrepresentable rather than merely avoided.
And `total_basis` says what `total` counts (`selection` for the comparison, `walk` for the view) because
one rendered sentence carrying two meanings is how `total` came to mean two numbers.

## 260921-ICR-L26 The Display Models Carry Why A Record May Be Displayed

`260921-ICR-L26` (`ICR-R26@v1`) makes the attribution a **wire fact** rather than a rendering
convention: the five display models that carry a supplied record each gained an optional
`applicability` — `ReviewAuthoredEffect`, `ReviewSignal`, `ReviewAssessmentDisplay`,
`ReviewEvidenceLink` and `ReviewObservation` — and both panes gained `context` (the labelled context
rows) and `applicability` (the six-way counts), so the two panes that show the same assessments cannot
disagree about which of them may be displayed. The vocabulary itself is declared in
`models/knowledge/review_applicability.py` and re-exported through this module's `__all__`, which is
why the names a reader looks for stay where they were. **1137 → 1174 lines.**

**Every addition is optional and additive.** `applicability` defaults to `None` and both pane
collections default to `()` — a payload published before these labels existed still validates, which is
what lets the client render an older body — and the absence means "this body carries no label", never
"this record is unrelated". A related or unrelated record is a fact the **server** classifies: a record
of another subject is either a context row or not displayed at all, and never a record in these
collections with a missing label.

**The two collections that are new, and the field that is not.** `context` is the only place a record of
another subject appears on a pane, and it carries that record's true subject and none of its judgment;
`applicability` is the six-way partition of every supplied collection, stated beside the records so the
filtering is visible as arithmetic. Neither is derived on the client or on the wire — the values are
built by `application/review_record_applicability.py`, and their two validators (a subject-bearing
label must name its subject; a summary must partition its population) live in the vocabulary module.

## 260921-ICR-L12 The Request Names Which Record It Is Addressed To

`260921-ICR-L12` (`ICR-R12@v1`) adds one literal and one optional field to this vocabulary:

- `ReviewHistoryRef` is `Literal["recorded"]` — **one** value, because the surface addresses exactly
  one historical record (the leaf's own published comparison generation) and a second spelling would be
  a second way to ask for the same record. There is deliberately no way to ask for a generation that is
  not this leaf's: a caller names *which record*, never *which leaf's*.
- `ReviewSurfaceRequest.history` carries it. Its absence is the live review, which is what every caller
  that names none asks for, and `recorded` asks for the comparison the leaf's own durable generation
  bound — the same answer whether the leaf's worktree is still there or cleanup removed it, because the
  record and not the enclosure is what the review is read from.

The union is additive in the strict sense a closed client vocabulary requires: an absent field is the
live review the client already asks for, and an unknown spelling never reaches the model — the
transport refuses it in its own 400 vocabulary rather than letting the model's own bound raise. The
module is 1189 lines, still under its 1200-line rail, and no limit was widened to admit the field.

## 260921-ICR-L17 The Request Names The Comparison The Caller Was Already Looking At

`260921-ICR-L17` (`ICR-R17@v1`) adds **one optional field** to `ReviewSurfaceRequest` and changes
nothing else on this module: `previous_binding_digest`, the identity a reader was looking at when the
read replaces that display.

**Why it is on the request rather than beside it.** `read_knowledge_review` and `compose_review` used
to take a `previous_binding_digest` keyword; the field replaces both, so there is one spelling of what
was asked. The docstring says so, and says what an absent value means: the read replaces nothing, which
is `current`.

**What the field is and is not.** It is the *previous* identity — never a substitute for the current
one. It selects no dataset, resolves no candidate and is never rendered as the comparison; the
composition only ever compares it against the comparison it rendered, and answers a digest that does not
match as `stale` with the carried identity retained as `previous_comparison_ref`. Its `pattern` is
`SHA256_PATTERN` — the digest's own published shape — so a value that names no generation this surface
could have published cannot even be asserted as a previous input.

**What a later reader must not undo.** The field is validated here as well as at the route. The route
admits the spelling in its own vocabulary so a malformed value is a typed 400 rather than an uncaught
`ValidationError`; this model's `pattern` is the second half of the same rule, not a duplicate of it.


## 260921-ICR-L15 The Displayed Binding State Is A Measured Fact

`260921-ICR-L15` (`ICR-R15@v1`) documents `ReviewAssessmentDisplay.binding_state` as what a
**measurement** put the binding in, rather than as a status the authority recorded: `current` and
`stale` are a completed measurement's two answers, `not-measured` says nothing measured the record, and
`unavailable` says the measurement failed. The field, its type and every other member of this module are
unchanged — this leaf's edit here is documentation only and the file stays at **1198 lines**, so the
repository's ≥1200-line census is unmoved.

The change matters because the sentence it replaces ("the authority's own recorded status, carried
verbatim") described a projection that decided currentness from the **presence of a mapping**: an
absent measurement was displayed `stale` and an empty one `current`, neither of which the store ever
recorded. The measured vocabulary now displayed here is produced by
`application/review_assessment_currentness` and the shipped comparison, and the display still upgrades
nothing — a `not-measured` binding is neither promoted to `current` nor reported as a movement.

## 260921-ICR-L22 Two Rules Leave For The Staleness Module And The Payload Gains A Measured Movement

`260921-ICR-L22` (`ICR-R22@v1`) is an **extraction first and a feature second**, and a reader must not
mistake the first for a loss. `ReviewStaleness` and `ReviewSubmission` were extracted **out of this
module** into `models/knowledge/review_staleness.py`, which also declares `ICR-R22@v1`'s new
`ReviewSyncMovement` (`:85-188`) beside them: `ReviewStaleness` at `:51-82`, carrying the
`_require_the_previous_input_to_be_labelled` validator unchanged, and `ReviewSubmission` at `:190-204`.
There is **one implementation of each rule** and it lives in the new module — no rule was deleted,
weakened or duplicated, and nothing about the stale/submission coupling changed.

**Why the extraction, and why it is the file-size rule's own remedy.** This module stood at **1198
lines** against the repository's **1200-line hard rail** (the ICR-L15 entry above records that same
1198), so adding the movement vocabulary here would have made it a new offender. The extraction moves
one cohesive responsibility whole, and the module is **1198 → 1164 lines** with the payload's new field
included — under the rail, with no limit widened to admit anything.

**The three names are re-exported, so nothing had to learn a new home.** The import block at `:61-65`
brings `ReviewStaleness`, `ReviewSubmission` and `ReviewSyncMovement` back, and `__all__` publishes all
three (`:116`, `:119`, `:121`). That is this module's existing convention for a name whose owner moved
— the same shape as the re-exported `resolve_review_candidate` and `ReviewRecordInputs` — so an
importer or a test that reaches these names through this module keeps resolving. It is not an alias
kept beside a deleted implementation: the declarations' address stays where their readers already
point.

**The payload gained one measured field, and it changes no rule here.** `KnowledgeReviewPayload`
(`:991-1082`) carries `sync_movement: ReviewSyncMovement | None = None` (`:1026`) beside `staleness`
and `submission` (`:1020-1021`): what this leaf's own managed syncs measured against the generation it
published, or `None` when no measurement is recorded — "no sync has reported" is a different fact from
"a sync reported agreement", and the field states which. The composition folds a **stale** movement
into the `staleness` value it publishes, so
`_require_the_submission_state_to_follow_staleness` (`:1037-1053`) is untouched and still refuses
either direction of disagreement: submission is disabled exactly when the comparison is stale. The
field is additive, so a read that measured nothing is the payload it always was.

## 260921-ICR-L31 The Payload Gains A Required Family Context And A Third Bounded Collection

**Two changes, both additive to the published vocabulary (`ICR-R31@v1`).** First,
``ReviewPagedCollection`` and ``REVIEW_PAGED_COLLECTIONS`` now name **three** bounded collections —
``knowledge``, ``records`` and ``family_members`` — because a third owner publishes a cursor and the
request, the payload and the transport must not be able to disagree about which one a cursor addresses.
The family roster's cursor is the read operation's own position in one recorded family revision's
scope, which is why presenting it to another collection's owner is a caller's mistake the owners refuse
rather than a slice this surface may reinterpret.

Second, ``KnowledgeReviewPayload`` gained the **required** ``family_context`` field: the recorded
families the selected subject belongs to on each bound snapshot, each selected family revision's own
guarantee and its recorded member roster. It is required rather than optional on purpose — a selection
that read its scope and holds no family states ``no_family_recorded``, so an absent field can never be
read as a measured zero.

**Citation accounting:** six rows of this card were re-anchored to the declarations they name — the
refusal-code union, the paged-collection union, the payload class and the pane declarations — at their
own new extents after this leaf's insertions moved every row below them. No claim cell was re-worded;
the paragraph above records why the union has three members now instead of two.
