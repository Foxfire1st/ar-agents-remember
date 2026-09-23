# mcp/src/agents_remember/models/knowledge/review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T06:50:00+02:00 |
| lastVerifiedCommitHash | `fdf3e4b6cfe73040d35cbfd4d8b93fd55369e499` |
| lastVerifiedCommitDate | 2026-09-23T22:41:36+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and five
bullets, each model and its validator, the shared bounds it imports, and the cases that check the
prohibitions over the whole payload schema rather than over one model.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it owns and the five prohibitions the display's shape enforces. | `KnowledgeReviewPayload`; `ReviewSideContent` | mcp/src/agents_remember/models/knowledge/review.py:13-13; mcp/src/agents_remember/models/knowledge/review.py:991-1082; mcp/src/agents_remember/models/knowledge/review.py:148-174 |
| The published vocabulary: the constants, the dispositions tuple, the refusal-code union and the models, with the channel vocabulary re-exported from its own module. | `__all__` | mcp/src/agents_remember/models/knowledge/review.py:47-88 |
| **The recorded surface version, the three pane names, `RRD:366`'s three proposed dispositions verbatim, the closed refusal-code union (seven members since 260921-ICR-L3, which added `source_content_unresolved` to the six 260915-KS-L45 left), the two-member subject-kind union, the three-member subject-presence union (`before_only`/`after_only`/`both`, ICR-R09) and the four-member side-state union — re-read at the merged candidate.** | `KNOWLEDGE_REVIEW_SURFACE_VERSION`; `REVIEW_PANE_NAMES`; `PROPOSED_ASSESSMENT_DISPOSITIONS`; `ReviewRefusalCode`; `ReviewSubjectKind`; `ReviewSubjectPresence`; `ReviewSideState` | mcp/src/agents_remember/models/knowledge/review.py:136-204; mcp/src/agents_remember/models/knowledge/review.py:210-210; mcp/src/agents_remember/models/knowledge/review.py:212-212 |
| **The movement vocabulary this module re-exports in its own `__all__` (`ICR-R08@v1`): the movement, its sides and states, the authored lineage, the gaps with their codes and the labelled rename inference — declared next door beside the other payload vocabularies.** | `ReviewRelationshipMovement`; `ReviewRelationshipSide`; `ReviewRelationshipGap`; `ReviewRenameInference`; `ReviewAuthoredLineage`; `ReviewRelationshipTransition` | mcp/src/agents_remember/models/knowledge/review_relationships.py:258-372; mcp/src/agents_remember/models/knowledge/review_relationships.py:153-201; mcp/src/agents_remember/models/knowledge/review_relationships.py:138-150; mcp/src/agents_remember/models/knowledge/review_relationships.py:221-255; mcp/src/agents_remember/models/knowledge/review_relationships.py:204-218; mcp/src/agents_remember/models/knowledge/review_relationships.py:89-91 |
| The shared shape that makes an unresolved reference a displayed fact rather than a dropped or anonymous one. | `ReviewUnresolvedReference` |mcp/src/agents_remember/models/knowledge/review.py:207-217|
| **The missing-side rule as a constructor check: text exactly when `present`, in both directions.** | `ReviewSideContent` |mcp/src/agents_remember/models/knowledge/review.py:220-245|
| The one request shape: a task context plus one of the read operation's own declared seeds, with no display version, instant or "latest" flag representable. | `ReviewSurfaceRequest`; `KnowledgeReadSeed` |mcp/src/agents_remember/models/knowledge/review.py:248-301; mcp/src/agents_remember/models/knowledge/read.py:206-213|
| The candidate reference, which carries task identities and never a filesystem path, and the comparison identity carried verbatim rather than recomputed. | `ReviewCandidateRef`; `ComparisonIdentity` | mcp/src/agents_remember/models/knowledge/review.py:289-362; mcp/src/agents_remember/models/knowledge/review.py:247-285 |
| The two per-side and per-item mechanical facts: the retained-revision count kept per side, and the field transition that states no meaning. | `ReviewRevisionGroup`; `ReviewFieldChange` |mcp/src/agents_remember/models/knowledge/review.py:487-496; mcp/src/agents_remember/models/knowledge/review.py:490-501; mcp/src/agents_remember/models/knowledge/review.py:507-518|
| The authored record displayed as the author wrote it, with no field for a computed effect, and the detection fact with no severity, verdict or author. | `ReviewAuthoredEffect`; `ReviewSignal` | mcp/src/agents_remember/models/knowledge/review.py:507-529; mcp/src/agents_remember/models/knowledge/review.py:532-548 |
| **The validator that refuses an anonymous verdict or an assessment that examined nothing.** | `ReviewAssessmentDisplay` | mcp/src/agents_remember/models/knowledge/review.py:527-566 |
| The evidence claim reference with its own authored limitations, and the observation that has no field for a sufficiency verdict. | `ReviewEvidenceLink`; `ReviewObservation` | mcp/src/agents_remember/models/knowledge/review.py:593-604; mcp/src/agents_remember/models/knowledge/review.py:607-625 |
| **The six persistent counts declared once, with the confirmed negative and the undetermined beside each other.** | `ReviewRemainingCountName`; `ReviewRemainingCount` | mcp/src/agents_remember/models/knowledge/review.py:635-642; mcp/src/agents_remember/models/knowledge/review.py:645-665 |
| **The selected location whose missing role stays unclassified rather than guessed from a path, and which since `ICR-R08@v1` carries the preserved identity, its own recorded side, the transition, the counterpart address (only when the other side records exactly one) and the whole movement.** | `ReviewSourceLocation` |mcp/src/agents_remember/models/knowledge/review.py:659-692|
| **Pane 1's own self-agreement rule: the pane's single assessment must be one of the assessments it displays, and the authored and mechanical collections keep separate element types. Pane 1's recorded selection: the optional `revision_selection` with its one-direction validator.** | `ReviewKnowledgePane` | mcp/src/agents_remember/models/knowledge/review.py:680-756 |
| **The explicit revision selection the pane carries: the compared head pair, the one-sided head, or the ambiguous/unresolved non-pair — declared next door, carried here, refused beside anything but a compared subject.** | `revision_selection`; `_require_a_compared_subject_to_record_its_selection`; `ReviewRevisionSelection` | mcp/src/agents_remember/models/knowledge/revision_selection.py:54-150; mcp/src/agents_remember/models/knowledge/review.py:739-739; mcp/src/agents_remember/models/knowledge/review.py:712-788 |
| **The inventory's own model, with the count checked against the list and the rule that an unrepresentable path makes the inventory measured and partial.** | `ReviewSourceInventory`; `ReviewChangedFile`; `ReviewUnrepresentablePath` | mcp/src/agents_remember/models/knowledge/review.py:764-880; mcp/src/agents_remember/models/knowledge/review.py:70-70; mcp/src/agents_remember/models/knowledge/review.py:102-102 |
| **Pane 2: the selected locations, the traversed recorded relationships (the associations with no source address at all), the expansion, the carried partition and the three changed-path lists read from it.** | `ReviewSourcePane` |mcp/src/agents_remember/models/knowledge/review.py:898-930|
| **Pane 3's two independent absence states, tied to the collections they describe, plus the availability list carried rather than inferred.** | `ReviewEvidencePane`; `channels` | mcp/src/agents_remember/models/knowledge/review.py:918-958 |
| The stale state that retains its previous input as a labelled value, and the rule that a current comparison has none to label. | `ReviewStaleness` |mcp/src/agents_remember/models/knowledge/review_staleness.py:51-82|
| The submission state with no favourable member, and the boundary that none of the published dispositions is approval. | `ReviewSubmission` |mcp/src/agents_remember/models/knowledge/review_staleness.py:190-204|
| **The whole payload and its stale/submission coupling, which refuses either direction of disagreement.** | `KnowledgeReviewPayload` |mcp/src/agents_remember/models/knowledge/review.py:991-1082|
| The refusal that is a state and never a degraded success, and the result that carries exactly one outcome. | `ReviewRefusal`; `KnowledgeReviewResult` | mcp/src/agents_remember/models/knowledge/review.py:403-415; mcp/src/agents_remember/models/knowledge/review.py:1110-1125 |
| **The catalogue's entry: a recorded identity, its own label and the presence the two snapshots give it, with no field for a path, a file, a display version, a ranking or a comparison count — the deleted `selected_item_count` was the wire carrier of the per-subject compare-to-earn-a-row mechanism.** | `ReviewEntry` |mcp/src/agents_remember/models/knowledge/review.py:318-336|
| **The entry read's typed outcome, whose validators refuse a refused read that offers any entry, non-zero totals beside a refusal, and a total smaller than the page beside it — so a caller can never be handed a subject beside the statement that nothing admitted one, nor a whole catalogue that reads as a first row.** | `ReviewEntryListResult`; `total_subjects`; `invariant_total`; `family_total`; `_require_the_totals_to_describe_the_catalogue` | mcp/src/agents_remember/models/knowledge/review.py:1143-1164; mcp/src/agents_remember/models/knowledge/review.py:1126-1160; mcp/src/agents_remember/models/knowledge/review.py:1127-1161; mcp/src/agents_remember/models/knowledge/review.py:1128-1162; mcp/src/agents_remember/models/knowledge/review.py:1128-1189 |
| **The two subject kinds declared once here, so the transport's admission tuple, the entry list and the panes cannot disagree about which identities are reviewable.** | `ReviewSubjectKind`; `SELECTOR_KINDS` |mcp/src/agents_remember/models/knowledge/review.py:189-189; mcp/src/agents_remember/serving/review.py:98-98|
| **The availability list the pane carries: one entry per record class the composition read, whole and underived.** | `channels`; `ReviewRecordChannel`; `ReviewEvidencePane` | mcp/src/agents_remember/models/knowledge/review.py:918-958; mcp/src/agents_remember/models/knowledge/review_records.py:68-123 |
| **The re-export that keeps every existing importer resolving while the vocabulary lives in its own module.** | `ReviewRecordChannel`; `ReviewRecordChannelState`; `ReviewRecordClassName` | mcp/src/agents_remember/models/knowledge/review.py:40-44; mcp/src/agents_remember/models/knowledge/review.py:47-88 |
| The shared bounds and the `KnowledgeModel` base every model here uses rather than restating its own. | `KnowledgeModel`; `PROSE_MAX_LENGTH`; `SHA256_PATTERN` | mcp/src/agents_remember/models/knowledge/base.py:1-80 |
| **The case that walks the whole payload schema for a field a generated conclusion could occupy.** | `test_the_whole_payload_schema_has_no_field_a_generated_conclusion_could_occupy` | mcp/tests/test_knowledge_review_surface.py:475-485 |
| **The case that asserts this module declares no record kind, no table and no status of its own.** | `test_the_surface_defines_no_record_kind_no_table_and_no_status_of_its_own` | mcp/tests/test_knowledge_review_surface.py:486-495 |
| The case that an unassessed subject is displayed unassessed and never defaulted to compatible, and the case that a missing side is its own state. | `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`; `test_a_missing_side_is_its_own_state_and_never_an_empty_string` | mcp/tests/test_knowledge_review_surface.py:561-587; mcp/tests/test_knowledge_review_surface.py:678-694 |
| The case that a passing observation is displayed as an observation and never as invariant-satisfied, and the case that a signal carries facts and scope limitations with no severity. | `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`; `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity` | mcp/tests/test_knowledge_review_surface.py:588-605; mcp/tests/test_knowledge_review_surface.py:606-624 |
| **The two rules that were extracted out of this module and the movement that arrived beside them (`ICR-R22@v1`): `ReviewStaleness`, `ReviewSubmission` and the new `ReviewSyncMovement` are declared in the staleness module, and this module re-exports all three so its importers and tests keep resolving.** | `ReviewStaleness`; `ReviewSubmission`; `ReviewSyncMovement` | mcp/src/agents_remember/models/knowledge/review_staleness.py:51-82; mcp/src/agents_remember/models/knowledge/review_staleness.py:190-204; mcp/src/agents_remember/models/knowledge/review_staleness.py:85-188 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every model is a display shape over one
repository's records, and no field carries an identity that ranges beyond the repository namespace the
request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **the recorded relationship enters the vocabulary (936 → 972 lines).** `ReviewSourceLocation` gains the preserved `invariant_id`, the `recorded_side`, the movement's `transition`, the `counterpart_path` (named only when the other side records exactly one address) and the whole `movement`; `ReviewSourcePane` gains the `relationships` collection, which exists because a membership and a governing route have no source address and because a movement whose sides are one row at one address is still one association. Both additions are purely additive with defaults, so an existing dashboard fixture still validates — the TypeScript mirror in `dashboard/src/data/review.ts` does not carry them yet, and mounting the collection is `ICR-R24`'s. The module also **re-exports** the new movement vocabulary in its own `__all__`, which is why the names a reader looks for stay where they were; the vocabulary itself is declared in `models/knowledge/review_relationships.py`. **Reopened-claim disposition:** the document carried a mechanical projection bullet for `ReviewSourceLocation`; the claim was re-read against the construct's current extent (`:465-498`), its wording retained, and the mechanical bullet retired (rewritten to record the re-read) so the projection is no longer presented as evidence of a review. **Citation accounting:** the two rows this leaf's change touched were re-derived at their constructs' own extents (`ReviewSourceLocation` `:465-498`, `ReviewSourcePane` `:696-728`), and one row was added for the re-exported vocabulary. **Metadata removal:** this card's six candidate-reading metadata rows were removed under the developer's 2026-09-22 rule, and the two history sentences that pointed at such a row were corrected in the same pass so the document no longer claims the row exists. No verification stamp was advanced: the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-22T14:58:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **the catalogue's presence and totals enter the vocabulary, and the count field is deleted (893 → 936 lines; `ICR-R09@v1`).** `ReviewEntry.presence` (the new three-member `ReviewSubjectPresence` union `before_only`/`after_only`/`both`) **replaces** `selected_item_count` — the deleted field was the wire carrier of the per-subject compare-to-earn-a-row mechanism the packet removes, and an entry that carried a comparison count would oblige the catalogue read to compare every subject before answering, which `ICR-R09@v1` forbids. `ReviewEntryListResult` gains the labelled totals (`total_subjects`/`invariant_total`/`family_total`) with the new `_require_the_totals_to_describe_the_catalogue` validator (the total must sum its kind totals, a refusal carries zero totals, and the total is `>=` the page beside it — the `>=` rule R10's paging depends on). The Logic paragraphs for both models were rewritten rather than annotated because the old account of `ReviewEntry` (a subject "the shipped comparison reached on both of the candidate's own sides", a count "the operation's own") is false at this candidate; the Conventions sentence naming the `Literal` aliases now names four; the entry Invariants bullet is rewritten for the same reason. **Citation accounting:** every range into this file re-derived from its construct's own extent against the 936-line candidate — `__all__` `47-88`, the re-export import `40-44`, `KNOWLEDGE_REVIEW_SURFACE_VERSION` `97`, `REVIEW_PANE_NAMES` `99`, `PROPOSED_ASSESSMENT_DISPOSITIONS` `104-108`, `ReviewRefusalCode` `110-120`, `ReviewSubjectKind` `123`, `ReviewSubjectPresence` `125-130`, `ReviewSideState` `132`, `ReviewUnresolvedReference` `135-146`, `ReviewSideContent` `148-174`, `ReviewSurfaceRequest` `176-196`, `ReviewCandidateRef` `198-210`, `ReviewEntry` `212-231`, `ComparisonIdentity` `233-272`, `ReviewRevisionGroup` `274-284`, `ReviewFieldChange` `286-298`, `ReviewAuthoredEffect` `300-317`, `ReviewSignal` `319-335`, `ReviewAssessmentDisplay` `337-376`, `ReviewEvidenceLink` `378-389`, `ReviewObservation` `391-416`, `ReviewRemainingCountName` `418-426`, `ReviewRemainingCount` `428-449`, `ReviewSourceLocation` `451-470`, `ReviewKnowledgePane` `472-546`, `revision_selection` `494-499`, its validator `529-540`, `ReviewChangedFile` `548-579`, `ReviewUnrepresentablePath` `581-601`, `ReviewSourceInventory` `603-665`, `ReviewSourcePane` `667-693`, `ReviewEvidencePane` `695-731`, `channels` `715`, `ReviewStaleness` `733-759`, `ReviewSubmission` `761-776`, `KnowledgeReviewPayload` `778-840`, `ReviewRefusal` `842-855`, `KnowledgeReviewResult` `857-873`, `ReviewEntryListResult` `875-936`; the six surface-test rows shifted one line with the candidate's import change (`475-485`, `486-495`, `561-587`, `678-694`, `588-605`, `606-624`). Two rows were added for `ReviewSubjectPresence` and the totals validator. **Stamp accounting:** the verification pair names the leaf's base — the last real commit the reading was taken against — because the presence union and the totals exist only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T10:40:00+02:00 — 260921-ICR-L7 curator (uncommitted change set on `ar/260921-icr-l7`, base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **pane 1 carries the explicit revision selection (873 → 893 lines).** Logic gained the selection paragraph (the optional `revision_selection`, absent exactly when no subject was compared, with the one-direction validator and the reason the value lives next door); Conventions records the imported-not-re-exported selection name; Invariants gained the recorded-selection bullet. One row added for the field, the validator and the value module. **Citation accounting:** every range into this file re-derived from its construct's own extent — the constants (`KNOWLEDGE_REVIEW_SURFACE_VERSION` `96`, `REVIEW_PANE_NAMES` `98`, `PROPOSED_ASSESSMENT_DISPOSITIONS` `103-107`, `ReviewRefusalCode` `109-119`, `ReviewSubjectKind` `122`, `ReviewSideState` `124`), `ReviewKnowledgePane` `462-532`, `channels` `705`, `ReviewSubmission` `751-767`, `KnowledgeReviewPayload` `768-831`, `ReviewRefusal` `832-846`, `KnowledgeReviewResult` `847-864`, the module-statement row's payload range, and the six surface-test rows to their merged extents. Header names this leaf's candidate row. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the leaf's base — the last real commit the reading was taken against — because the new field and validator exist only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T09:20:00+02:00 — 260921-ICR-L4 curator (gate repair pass): **two mechanical projection records retired after hand re-read; the six-counts and pane rows re-cited from their declarations.** The generated bullets below repointed `ReviewRemainingCount` to `:350-376` and `ReviewSourcePane` to `:434-443` by anchor-range projection; those ranges are retired here because a projected range does not evidence the claim — the rows now cite the constructs' own declarations (`ReviewRemainingCountName` `:407-415`, `ReviewRemainingCount` `:417-438`, `ReviewSourcePane` `:637-663`), each re-read against the merged module with wording retained because each still states what the code does: the alias declares the six names once, the model reads it, and the pane carries the partition value beside its three lists. No verification stamp was advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-22T09:15:00+02:00 — 260921-ICR-L4 curator (sync-merge resolution of the parked candidate against the landed line, merged base code `d21bc8a6` / memory `75bb4d65`): **additive union with landed `260921-ICR-L14`/`260921-ICR-L3`.** Both sides' history kept newest-first; L14's channel-list rows and L3's seven-member refusal-code row stand beside this leaf's six-counts and carried-partition rows, with every range re-derived against the merged 873-line module. Header names the merged base on this leaf's candidate row. No verification stamp was advanced.
- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the pane's attribution half became one accounting (836 → 857 lines).** `ReviewSourcePane` gained `unknown_attribution_changed_paths` and `attribution` (the `SourceAttribution` partition value the three path lists are read from, so a path appears in exactly one of them), and the six persistent counts are declared once as `ReviewRemainingCountName`, which `ReviewRemainingCount.name` now reads: `unattributed_changed_paths` is the confirmed negative conclusion and `unknown_attribution_changed_paths` is the measured population that conclusion could not be drawn for. The wire change is purely additive (`unknown_attribution_changed_paths` defaults to `()`, `attribution` to `None`), so existing dashboard fixtures still validate. **Stamp accounting:** old verification rows name the last real commit; this leaf's claims were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the refusal vocabulary gained one additive code, and the claim that counts its members was corrected rather than left stale.** `ReviewRefusalCode` is now a **seven**-member union: `source_content_unresolved` was inserted between `comparison_refused` and `review_adapter_unavailable`, and it is the code the new entry-content route answers with when the listed generation no longer resolves to the two code objects the listing published. The Logic paragraph said "the closed six-member union" and the reference row said "six members since 260915-KS-L45"; both were **false at this candidate**, so both now say seven and name the increment that added the member, together with the reason the addition is additive in the strict sense (the union is a vocabulary a client reads, not control flow, and a code the transport does not recognise already answers `400` rather than being mapped onto an existing answer). **Citation accounting:** the enforced row that carries this claim was re-read against the candidate and every one of its five ranges re-derived from the construct's real extent — the ranges it carried (`98-109`, `112-112`, `81-85`, `87-94`, `101-101`) no longer held their anchors, `ReviewSideState` among them (it is at 113). It now cites `85-85`, `87-87`, `92-96`, `98-106`, `111-111` and `113-113`, and `ReviewSubjectKind` — which the claim's own words name but the anchor cell had omitted — was added as a sixth anchor. The `ReviewSubjectKind`/`SELECTOR_KINDS` row was re-derived in the same pass (`110-110` → `111-111`; `serving/review.py:60-63` → `79-79`, a different file this leaf's sibling moved). No other row, anchor or claim wording was touched, and the two verification rows still name the last real commit whose bytes this card was verified against — nothing in this leaf is committed, and the governed closeout owns the stamp. **Stamp accounting:** the two verification rows now name the **production line this card was read against** — `d80a0513…`, the master line at this leaf's base, committed `2026-09-21T19:51:20+02:00` — rather than the older commit they carried before, because this card's body was read against that line and this leaf's uncommitted change set on top of it; they do not claim that a commit contains this leaf's bytes, and the governed closeout owns the real stamp once the code commit exists.
- 2026-09-21T22:05:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **pane 3 gained the record-availability list, and this module lost the vocabulary's declaration to a module of its own.** `ReviewEvidencePane.channels` carries one `ReviewRecordChannel` per record class a review's composition read — whole, including the classes that were not read or could not be read — because an empty tuple has three possible meanings and a consumer needs the fact whichever pane renders the records; the Logic section now states the field, why it sits on this pane, and the explicit refusal to derive it from collection lengths, and an Invariants bullet records that the list is carried rather than inferred. `ReviewRecordChannel`, `ReviewRecordChannelState` and `ReviewRecordClassName` were **extracted** to `models/knowledge/review_records.py` because this file had crossed the 900-line soft rail at 940 (it is 851 now) and because the vocabulary is a contract of its own; they are re-exported here, so the Conventions section now says so and no importer had to learn a new home. **Citation accounting:** this leaf's insertions moved everything below `:63`, so every range into this file was re-derived at its construct's own extent — `ReviewAssessmentDisplay` `315-353`→`323-363`, `ReviewEvidenceLink` `356-366`→`364-376`, `ReviewEvidencePane` `635-663`→`643-680`, `ReviewStaleness` `666-691`→`681-708`, `KnowledgeReviewPayload` `711-772`→`726-789`, `KnowledgeReviewResult` `790-805`→`805-822`, `PROPOSED_ASSESSMENT_DISPOSITIONS` `92-96`→`100-121`, `ReviewSideContent` `128-153`→`136-163` and `ReviewKnowledgePane` `439-488`→`447-503` — with the rows this pass touched re-pointed by hand and the rest left to the mechanical projection, which is the same division of labour the card's own history records. Two rows were **added** for the channel list and the re-export. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` now name the **production line this reading was against** — `d80a0513e928ef29a973527d09597c82c96fde87`, the master line's current tip and this leaf's base — replacing the previous pair rather than leaving a stamp no reading in this pass measured; the candidate is uncommitted, so no commit contains the content a stamp would claim to have verified, and the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **R02's wire shape: an inventory that is always present, and a comparison identity that can be absent.** Added `ReviewChangedFile`, `ReviewUnrepresentablePath`, `ReviewSourceInventory` and `ReviewSourcePane.inventory`; made `ReviewSurfaceRequest.selector` optional (absence = task context); added `ComparisonIdentity.knowledge_compared` and its all-or-nothing digest rule; added `ReviewKnowledgePane.selection_state`/`selection_detail`; added `not_compared` to `ReviewStaleness`; and made `KnowledgeReviewPayload.comparison` optional behind the validator that ties the absence to the staleness state and to which question the knowledge pane answered. `KNOWLEDGE_REVIEW_SURFACE_VERSION` stays `knowledge-review-surface/1`, and the ruling is recorded beside the constant: `/1` admits both shapes, the change is additive for a client that already requests the subject payload, and no version validator exists in this package to enforce a bump. All rows in the reference table were re-derived against this candidate, several of them to constructs whose lines this leaf moved. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.

- 2026-09-20T11:53:49+00:00: mechanical citation repair, **retired on 2026-09-23 after a curator re-read (260921-ICR-L22)**: the mechanical pass had moved `ReviewCandidateRef`; `ComparisonIdentity` by anchor-range projection, and this leaf's curation re-derived every range from the construct's own declaration in the candidate instead; the claim's wording is unchanged, and no range is claimed current on the projection's authority.
- 2026-09-20T11:53:49+00:00: mechanical citation repair, **retired on 2026-09-23 after a curator re-read (260921-ICR-L22)**: the mechanical pass had moved `ReviewRevisionGroup`; `ReviewFieldChange` by anchor-range projection, and this leaf's curation re-derived every range from the construct's own declaration in the candidate instead; the claim's wording is unchanged, and no range is claimed current on the projection's authority.
- 2026-09-20T11:53:49+00:00: mechanical citation repair, **retired on 2026-09-23 after a curator re-read (260921-ICR-L26)**: the mechanical pass had moved `ReviewAuthoredEffect` and `ReviewSignal` to their then-lines without re-reading the claim. `260921-ICR-L26`'s change moved both constructs again (the five display models each gained their optional `applicability` field), so the row was re-read against each construct's own extent in the 1174-line candidate and now cites mcp/src/agents_remember/models/knowledge/review.py:483-505 and mcp/src/agents_remember/models/knowledge/review.py:508-524; the claim's wording was retained because it still states what the code does. The projection is recorded here as the moved coordinate it is, not as evidence that the claim was reviewed.
- 2026-09-20T11:53:49+00:00: mechanical citation repair, **retired on 2026-09-23 after a curator re-read (260921-ICR-L26)**: the mechanical pass had moved `ReviewEvidenceLink` and `ReviewObservation` to their then-lines without re-reading the claim. `260921-ICR-L26`'s change moved both constructs again, so the row was re-read against each construct's own extent in the 1174-line candidate and now cites mcp/src/agents_remember/models/knowledge/review.py:569-580 and mcp/src/agents_remember/models/knowledge/review.py:583-601; the claim's wording was retained because it still states what the code does. The projection is recorded here as the moved coordinate it is, not as evidence that the claim was reviewed.
- 2026-09-20T11:53:49+00:00: mechanical citation repair, retired on 2026-09-22 after a curator re-read (260921-ICR-L8): the mechanical pass had moved `ReviewSourceLocation`'s range to mcp/src/agents_remember/models/knowledge/review.py:379-397 without re-reading the claim. The range the row carries is now derived from the construct's own declaration extent (mcp/src/agents_remember/models/knowledge/review.py:465-498, which gained the `invariant_id`/`transition`/`recorded_side`/`counterpart_path`/`movement` fields in this leaf), the claim was re-read against that construct and its wording retained, and the mechanical projection is recorded here as the fact it is -- a moved coordinate, not evidence that the claim was reviewed.
- 2026-09-20T11:53:49+00:00: mechanical citation repair, **retired on 2026-09-23 after a curator re-read (260921-ICR-L22)**: the mechanical pass had moved `ReviewStaleness` by anchor-range projection, and this leaf's curation re-derived every range from the construct's own declaration in the candidate instead; the claim's wording is unchanged, and no range is claimed current on the projection's authority.
- 2026-09-20T11:53:49+00:00: mechanical citation repair, **retired on 2026-09-23 after a curator re-read (260921-ICR-L22)**: the mechanical pass had moved `ReviewSubmission` by anchor-range projection, and this leaf's curation re-derived every range from the construct's own declaration in the candidate instead; the claim's wording is unchanged, and no range is claimed current on the projection's authority.
- 2026-09-20T11:53:49+00:00: mechanical citation repair, **retired on 2026-09-23 after a curator re-read (260921-ICR-L22)**: the mechanical pass had moved `ReviewRefusal`; `KnowledgeReviewResult` by anchor-range projection, and this leaf's curation re-derived every range from the construct's own declaration in the candidate instead; the claim's wording is unchanged, and no range is claimed current on the projection's authority.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **re-read this claim against the construct its mechanically projected range now covers, and retired that projection record after the read.** The claim names the recorded surface version, the three pane names, `RRD:366`'s three proposed dispositions verbatim, the closed refusal-code union and the side-state union. Each anchor was resolved at its own current declaration: `KNOWLEDGE_REVIEW_SURFACE_VERSION` and `REVIEW_PANE_NAMES` are in `:74-76`, `PROPOSED_ASSESSMENT_DISPOSITIONS` in `:81-85`, `ReviewRefusalCode` in `:87-94` — now **six** members, the new one being `subject_unresolved` — and `ReviewSideState` at `:101`. The range covers all five; the claim's wording was **corrected, not merely retained**, because "the closed refusal-code union" is now a six-member union and the sentence did not say so. The generated repair bullet for this range was **retired** because that projection resolves exact NAMES rather than the claim's subject. No other bullet or row was deleted and no verification stamp was advanced.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): the vocabulary gained the **entry half** of the surface. This card now records `ReviewSubjectKind` (the two admitted subject kinds, declared **here once** so the transport's `SELECTOR_KINDS`, the entry list and the panes cannot disagree about which identities are reviewable), `ReviewEntry` (the reviewed subject as the shipped comparison selected it — a recorded identity, its own label and the operation's count, with **no field for a path, a file, a display version or a ranking**, which is what keeps "the browser never chooses the candidate" a property of the value), and `ReviewEntryListResult` (the entry read's typed outcome, whose validator refuses a **refused** read that offers any entry: "an entry beside a refusal is how a caller comes to review a subject nothing admitted"). `ReviewRefusalCode` gained its sixth member `subject_unresolved`, and the public vocabulary count moved from twenty-two to twenty-five models plus `ReviewSubjectKind`. No verification stamp was advanced, because no commit contains this body; this entry now names this leaf's candidate.
- 2026-09-20T01:29+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared this card's one enforced citation row — a stale range on the signal case.** The row's second range was `553-571` for `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity`, whose declaration begins at 550 (its docstring "A signal is the matched condition with its versions and limits -- never a finding" opens the body, and the case ends at 566). The range was repointed to that case's own declaration extent, `:550-566`; the Finding text, both anchors and the row's other range (`:532-547`, the passing-observation case) are unchanged, and no citation was dropped. No other row, anchor or claim wording was touched, and no verification stamp was advanced.
- 2026-09-20T01:02:52+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): verified the 2 enforced citation rows this card carried (citation_anchor_absent_from_range ×2) by hand-reading `mcp/tests/test_knowledge_review_surface.py`: each named node sits inside the range its row now cites (`test_a_missing_side_is_its_own_state_and_never_an_empty_string` declared at 621, inside `:621-632`, beside `:505-521`; `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied` declared at 532, inside `:532-547`, beside `:553-571`), so the earlier mechanical projection was correct and needed no further edit; the claim wording, the anchors and every range are unchanged, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 2 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `test_a_missing_side_is_its_own_state_and_never_an_empty_string`; `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 2 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `review.py.md:216` (`test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`, `test_a_missing_side_is_its_own_state_and_never_an_empty_string`); `review.py.md:217` (`test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`, `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity`).
- 2026-09-18T18:20+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **re-read this card's own reopened claim against the construct its range now covers, and RETAINED its wording** — `KnowledgeReviewPayload`; `ReviewSideContent`, cited at mcp/src/agents_remember/models/knowledge/review.py:1-22 and `:490-528`. The claim says the module's docstring states what the module owns and the five prohibitions the display's shape enforces, and the cited ranges hold the docstring's five bullets and `class KnowledgeReviewPayload`; it is true as written. It reopens because at the temporary provenance this scrutiny uses (the leaf's base commit `2dcacb27`) `ReviewSideContent` does not exist — the card is one of this leaf's own six and every construct it cites is new. That is the stamp-relative condition, and it clears at closeout. No range was substituted or deleted and the verification stamp is **not** advanced.
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's three-pane vocabulary. It records the module's central fact — **it defines no record kind**, and the only thing it owns is the shape of a display — together with the five prohibitions that shape enforces: no field a conclusion could be assembled in, unassessed as the absence of a value, a missing side as its own state rather than an empty string, the stale rule as a constructor check on the payload, and the authored-record/mechanical-signal separation kept by element type. It also records each validator that makes those prohibitions structural rather than advisory (`ReviewSideContent`, `ReviewAssessmentDisplay`, `ReviewRemainingCount`, `ReviewKnowledgePane`, `ReviewEvidencePane`, `ReviewStaleness`, `KnowledgeReviewPayload`, `KnowledgeReviewResult`). This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The candidate this reading was taken against is named in the entry itself, and closeout owns the stamp once the code commit exists. (That metadata row was removed on 2026-09-22 under the developer's rule that it is not a real field.)

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

## Update History
- 2026-09-23T00:30:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; production line at this leaf's base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **the published page vocabulary, and the constructor that refuses a remainder without a
cursor.** `ReviewCollectionPage`, `ReviewPagedCollection`, `MAXIMUM_REVIEW_PAGE_SIZE`,
`REVIEW_PAGE_RESET_NEXT_ACTION`, the two page refusal codes, the request's three paging fields and the
payload's `page`/`page_refusal` are new; the constructor check that makes `remaining>0` without a cursor
unrepresentable is the property to carry forward. Every row on this card that cited
`models/knowledge/review.py` by line was re-derived against this candidate, because this leaf moved
them. No verification stamp was advanced: nothing in this leaf is committed, so the commit/closeout stamp remains closeout's.
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

## Update History
- 2026-09-23T02:40:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **the five display models gain `applicability`, both panes gain `context` and `applicability`, and the vocabulary is re-exported (1137 → 1174 lines; `ICR-R26@v1`).** The card records the additive-compatibility rule (a missing label is not an unrelated record), that `context` is the only place another subject's record appears on a pane, and that the two validators live in the vocabulary module. **Citation accounting:** the rows this leaf's insertions moved were re-derived from each construct's own extent in the 1174-line candidate — `ReviewAuthoredEffect`/`ReviewSignal` `67`/`93`→`483-505`/`508-524`, `ReviewAssessmentDisplay` `337-376`→`527-566`, `ReviewEvidenceLink`/`ReviewObservation` `74`/`78`→`569-580`/`583-601`, `ReviewKnowledgePane` `472-546`→`680-756`, `ReviewEvidencePane` `75`/`893`→`918-958` (twice, on two rows). Wording was retained where the claim still states what the code does. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header already names this leaf's base, and the governed closeout owns the real stamp.
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

## Update History
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the request names which record it is addressed to (ICR-R12@v1).** `ReviewHistoryRef` is the one
historical form this surface admits and `ReviewSurfaceRequest.history` carries it; its absence is the
live review, and the field is additive for a closed client vocabulary. 1189 lines, under the rail, no
limit widened. **Citation accounting:** every row into this module was re-derived against the
candidate. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and
the governed closeout owns the real stamp.

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


## Update History
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **the request names the comparison the reader was already looking at (`ICR-R17@v1`).** `ReviewSurfaceRequest.previous_binding_digest` is a new optional sha256-shaped field: it is the *previous* identity the composition compares the rendered comparison against, it selects nothing, and an absent value means the read replaces nothing (which is `current`). The docstring records both facts. **Citation accounting:** the rows this leaf's nine-line insertion moved were re-derived from each construct's own declaration on the candidate — `KnowledgeReviewResult` `:1119`, `ReviewAuthoredEffect` `:507`, `ReviewObservation` `:607`, `ReviewRemainingCount` `:645`, `ReviewSignal` `:532`, `_require_the_totals_to_describe_the_catalogue` `:1178`, `revision_selection` `:731`. **Stamp accounting:** the verification pair names this leaf's base — the last real commit the reading was taken against — because the field exists only in this leaf's uncommitted working tree; closeout owns the stamp once the code commit exists.

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

## Update History
- 2026-09-23T13:10:00+02:00 — 260921-ICR-L15 curator (candidate `ar/260921-icr-l15`, uncommitted; leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58`, so the honest basis for every claim here is that commit plus the working-tree delta): **the displayed binding state is documented as a measured fact (docstring-only; 1198 lines in both trees).** Recorded in the body rather than as a history-only note because the memory-refresh check requires the sidecar body itself to reflect a changed source. No claim, anchor or citation range changed, and **no verification stamp was advanced**: the candidate is uncommitted, the header's stamp values are untouched, and the governed closeout owns the real stamp.

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

## Update History
- 2026-09-23T20:30:00+02:00 — 260921-ICR-L23 curator (memory worktree only; no code changed, no commits; leaf base `473ad8242bb4c22bdabed5d5253767350381eb3e` plus the working-tree delta): **the payload publishes the boundary measurement, and two reference rows were re-anchored.** `KnowledgeReviewPayload` gained `external_git_movement: ExternalGitMovement | None = None` (`:1029-1037`) with its own comment, and the vocabulary re-exports the name (`:78`); `None` is "no boundary was measured", a different fact from a boundary that compared and found nothing replaced. The repaired rows are `revision_selection` (the pane field at `:739`) and `_require_a_compared_subject_to_record_its_selection` (`:777-788`). **No verification stamp was advanced**: the candidate is uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee):` **two rules left this module for `models/knowledge/review_staleness.py` and the payload gained one measured movement (`ICR-R22@v1`).** Recorded as an **extraction, not a feature loss**: `ReviewStaleness` (`review_staleness.py:51-82`) and `ReviewSubmission` (`:190-204`) moved whole beside the new `ReviewSyncMovement` (`:85-188`), one implementation of each rule, so the stale/previous-input labelling and the display-only submission boundary are unchanged in substance. The reason is the file-size rail, not a vocabulary change: the module was at **1198 lines** against the 1200-line hard limit, and it is **1164 lines** after the extraction plus the payload's new field. The three names are **re-exported** (import block `:61-65`; `__all__` `:116`, `:119`, `:121`) so importers and tests keep resolving; `KnowledgeReviewPayload` (`:991-1082`) gained `sync_movement: ReviewSyncMovement | None = None` (`:1026`), and its constructor rules are untouched. **Citation accounting:** one row was **added** for the extracted declarations and the re-export (`review_staleness.py:51-82`, `:190-204` and `:85-188`); no existing row, anchor or range on this card was moved, re-pointed, re-worded or dropped — deliberately, because the curator's citation pass owns that work row by row, including the rows that still point at this module for names that now live next door. **Stamp accounting:** the header's verification pair is left exactly as recorded — `e605822eb3bf83bf63a45963c5f51d5fc28859ee`, this leaf's recorded base — and it is not advanced, because every construct this entry cites exists only in this leaf's uncommitted working tree; the governed closeout owns the real stamp.

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

## Update History
- 2026-09-23T22:20:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): ``ReviewPagedCollection``/``REVIEW_PAGED_COLLECTIONS`` name a third bounded collection (``family_members``) and ``KnowledgeReviewPayload`` carries the required ``family_context`` field (`ICR-R31@v1`), so a read that found no family says so with ``no_family_recorded`` instead of an absent field. Body updated with the real section above; no stamp advanced beyond the leaf's base plus the working-tree delta.
