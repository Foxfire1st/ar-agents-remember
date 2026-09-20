# mcp/src/agents_remember/models/knowledge/review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T13:43:00+02:00 |
| lastVerifiedCommitHash |  `4a0442d62eb842661a3dd04686c376d0f0dbc61f`|
| lastVerifiedCommitDate |  2026-09-20T14:22:54+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l45-ar` uncommitted source; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
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
publication approval. `ReviewRefusalCode` is the closed **six**-member union
`candidate_unresolved`, `candidate_not_live`, `candidate_dataset_absent`, `subject_unresolved`,
`comparison_refused`, `review_adapter_unavailable`, and `ReviewSideState` the four-member union
`present`, `absent`, `binary`, `unresolved`. `ReviewSubjectKind` is the closed two-member
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
empty. `ReviewStaleness._require_the_previous_input_to_be_labelled` refuses a `stale` state with no
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
`expansion_command`, the attributed and unattributed changed paths, and its own `unresolved` rows.
`ReviewSourceLocation` keeps `role` as `None` when the record carries none, so a missing role is
displayed as unclassified rather than guessed from a path, and carries the recorded and observed
source identities, the `resolution`, the three-member `change_state` and `before_only`.
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

**`ReviewEntry` is the reviewed subject as the comparison itself selected it, and it exists so the
task-view entry never has to invent one.** `selector_kind`, `selector_id`, `label` and
`selected_item_count` are the whole model: `selector_id` is the recorded identity of a subject the
shipped comparison reached on both of the candidate's own sides, and `label` is that identity's own
recorded display label. There is deliberately **no field for a path, a file, a display version or a
ranking**, so an entry cannot point at a dataset the resolution did not select and cannot be ordered
by a preference this list invented. `selected_item_count` is the operation's own count and not a
score — a subject with zero reached items is not offered at all, which is why the field carries `ge=0`
while the entry operation drops a zero.

**`ReviewEntryListResult` is the entry read's typed outcome, and its validator is what keeps "nothing
to review" distinct from "nothing could answer".** It carries `state` (`entries` | `refused`), the
literal `operation="list_knowledge_review_entries"`, the task context (`repository_id`, `master`,
`leaf_id`), an `entries` tuple and an optional `refusal`.
`_require_one_outcome` refuses a `refused` state with no refusal, an `entries` state that carries a
refusal, and — the load-bearing one — **a refused read that offers any entry at all**: "a refused
entry read offers no subject; an entry beside a refusal is how a caller comes to review a subject
nothing admitted." So an empty `entries` on an `entries` state is a pair that selected no reviewable
subject (a fact about the datasets, stated as one), while a refusal is the resolution saying why it
could not answer, and the two cannot be confused by a caller that only reads the list.

### Conventions

Every model here is a `KnowledgeModel`, and the shared bounds are imported rather than restated:
`LABEL_MAX_LENGTH`, `PATH_MAX_LENGTH`, `PROSE_MAX_LENGTH`, `REFERENCE_MAX_LENGTH` and
`SHA256_PATTERN` come from `models/knowledge/base.py`, so a display field is bounded by the same
constants every other knowledge model uses. Identity fields use `REFERENCE_MAX_LENGTH`, prose uses
`PROSE_MAX_LENGTH`, and the four digests on `ComparisonIdentity` are constrained by `SHA256_PATTERN`
rather than by a length. `__all__` names the whole public vocabulary: the two constants
`KNOWLEDGE_REVIEW_SURFACE_VERSION` and `REVIEW_PANE_NAMES`, the dispositions tuple, and all
twenty-five models plus `ReviewRefusalCode`, `ReviewSubjectKind` and `ReviewSurfaceRequest`.
`ReviewRefusalCode`, `ReviewSubjectKind` and `ReviewSideState` are `Literal` aliases rather than
`enum` classes, and the three closed `record_kind`, `side` and `change_state` vocabularies are inline
`Literal`s on their fields. Immutable collections are `tuple[...]` with `()` defaults, so no model
carries a mutable default — which is what lets `ReviewEntryListResult.entries` default to an empty
tuple and still mean "no subject was selected" rather than "the question was not answered".

### Invariants And Boundaries

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
- **An entry cannot name a dataset, a path or a rank.** `ReviewEntry` carries a recorded identity, its
  own label and the comparison's count, and nothing else — which is what keeps "the browser never
  chooses the candidate" a property of the value rather than a convention of its callers.
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
| The module's own statement of what it owns and the five prohibitions the display's shape enforces. | `KnowledgeReviewPayload`; `ReviewSideContent` | mcp/src/agents_remember/models/knowledge/review.py:1-22; mcp/src/agents_remember/models/knowledge/review.py:490-528 |
| The published vocabulary: the two constants, the dispositions tuple, the refusal-code union and the twenty-two models. | `__all__` | mcp/src/agents_remember/models/knowledge/review.py:40-67 |
| **The recorded surface version, the three pane names, `RRD:366`'s three proposed dispositions verbatim, the closed refusal-code union (six members since 260915-KS-L45), the two-member subject-kind union and the four-member side-state union — re-read at this leaf's candidate.** | `KNOWLEDGE_REVIEW_SURFACE_VERSION`; `REVIEW_PANE_NAMES`; `PROPOSED_ASSESSMENT_DISPOSITIONS`; `ReviewRefusalCode`; `ReviewSideState` | mcp/src/agents_remember/models/knowledge/review.py:74-74; mcp/src/agents_remember/models/knowledge/review.py:76-76; mcp/src/agents_remember/models/knowledge/review.py:81-85; mcp/src/agents_remember/models/knowledge/review.py:87-94; mcp/src/agents_remember/models/knowledge/review.py:101-101 |
| The shared shape that makes an unresolved reference a displayed fact rather than a dropped or anonymous one. | `ReviewUnresolvedReference` | mcp/src/agents_remember/models/knowledge/review.py:95-105 |
| **The missing-side rule as a constructor check: text exactly when `present`, in both directions.** | `ReviewSideContent` | mcp/src/agents_remember/models/knowledge/review.py:108-133 |
| The one request shape: a task context plus one of the read operation's own declared seeds, with no display version, instant or "latest" flag representable. | `ReviewSurfaceRequest`; `KnowledgeReadSeed` | mcp/src/agents_remember/models/knowledge/review.py:136-149; mcp/src/agents_remember/models/knowledge/read.py:1-60 |
| The candidate reference, which carries task identities and never a filesystem path, and the comparison identity carried verbatim rather than recomputed. | `ReviewCandidateRef`; `ComparisonIdentity` | mcp/src/agents_remember/models/knowledge/review.py:161-172; mcp/src/agents_remember/models/knowledge/review.py:194-210 |
| The two per-side and per-item mechanical facts: the retained-revision count kept per side, and the field transition that states no meaning. | `ReviewRevisionGroup`; `ReviewFieldChange` | mcp/src/agents_remember/models/knowledge/review.py:213-222; mcp/src/agents_remember/models/knowledge/review.py:225-236 |
| The authored record displayed as the author wrote it, with no field for a computed effect, and the detection fact with no severity, verdict or author. | `ReviewAuthoredEffect`; `ReviewSignal` | mcp/src/agents_remember/models/knowledge/review.py:239-255; mcp/src/agents_remember/models/knowledge/review.py:258-273 |
| **The validator that refuses an anonymous verdict or an assessment that examined nothing.** | `ReviewAssessmentDisplay` | mcp/src/agents_remember/models/knowledge/review.py:248-286 |
| The evidence claim reference with its own authored limitations, and the observation that has no field for a sufficiency verdict. | `ReviewEvidenceLink`; `ReviewObservation` | mcp/src/agents_remember/models/knowledge/review.py:317-327; mcp/src/agents_remember/models/knowledge/review.py:330-347 |
| **The two count rules: an unexplained absent count is refused, and a measured count carries no not-applicable reason.** | `ReviewRemainingCount` | mcp/src/agents_remember/models/knowledge/review.py:350-376 |
| The selected location whose missing role stays unclassified rather than guessed from a path. | `ReviewSourceLocation` | mcp/src/agents_remember/models/knowledge/review.py:379-397 |
| **Pane 1's own self-agreement rule: the pane's single assessment must be one of the assessments it displays, and the authored and mechanical collections keep separate element types.** | `ReviewKnowledgePane` | mcp/src/agents_remember/models/knowledge/review.py:372-403 |
| Pane 2: the selected locations, the expansion, and the changed paths the selection did and did not reach. | `ReviewSourcePane` | mcp/src/agents_remember/models/knowledge/review.py:434-443 |
| **Pane 3's two independent absence states, tied to the collections they describe.** | `ReviewEvidencePane` | mcp/src/agents_remember/models/knowledge/review.py:418-446 |
| The stale state that retains its previous input as a labelled value, and the rule that a current comparison has none to label. | `ReviewStaleness` | mcp/src/agents_remember/models/knowledge/review.py:477-498 |
| The submission state with no favourable member, and the boundary that none of the published dispositions is approval. | `ReviewSubmission` | mcp/src/agents_remember/models/knowledge/review.py:501-515 |
| **The whole payload and its stale/submission coupling, which refuses either direction of disagreement.** | `KnowledgeReviewPayload` | mcp/src/agents_remember/models/knowledge/review.py:490-528 |
| The refusal that is a state and never a degraded success, and the result that carries exactly one outcome. | `ReviewRefusal`; `KnowledgeReviewResult` | mcp/src/agents_remember/models/knowledge/review.py:559-571; mcp/src/agents_remember/models/knowledge/review.py:574-589 |
| **The reviewed subject as the comparison selected it: a recorded identity, its own label and the operation's count, with no field for a path, a file, a display version or a ranking.** | `ReviewEntry` | mcp/src/agents_remember/models/knowledge/review.py:175-191 |
| **The entry read's typed outcome, whose validator refuses a refused read that offers any entry — so a caller can never be handed a subject beside the statement that nothing admitted one.** | `ReviewEntryListResult` | mcp/src/agents_remember/models/knowledge/review.py:592-620 |
| **The two subject kinds declared once here, so the transport's admission tuple, the entry list and the panes cannot disagree about which identities are reviewable.** | `ReviewSubjectKind`; `SELECTOR_KINDS` | mcp/src/agents_remember/models/knowledge/review.py:96-99; mcp/src/agents_remember/serving/review.py:60-63 |
| The shared bounds and the `KnowledgeModel` base every model here uses rather than restating its own. | `KnowledgeModel`; `PROSE_MAX_LENGTH`; `SHA256_PATTERN` | mcp/src/agents_remember/models/knowledge/base.py:1-80 |
| **The case that walks the whole payload schema for a field a generated conclusion could occupy.** | `test_the_whole_payload_schema_has_no_field_a_generated_conclusion_could_occupy` | mcp/tests/test_knowledge_review_surface.py:419-429 |
| **The case that asserts this module declares no record kind, no table and no status of its own.** | `test_the_surface_defines_no_record_kind_no_table_and_no_status_of_its_own` | mcp/tests/test_knowledge_review_surface.py:430-439 |
| The case that an unassessed subject is displayed unassessed and never defaulted to compatible, and the case that a missing side is its own state. | `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`; `test_a_missing_side_is_its_own_state_and_never_an_empty_string` | mcp/tests/test_knowledge_review_surface.py:505-521; mcp/tests/test_knowledge_review_surface.py:621-632 |
| The case that a passing observation is displayed as an observation and never as invariant-satisfied, and the case that a signal carries facts and scope limitations with no severity. | `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`; `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity` | mcp/tests/test_knowledge_review_surface.py:532-547; mcp/tests/test_knowledge_review_surface.py:550-566 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every model is a display shape over one
repository's records, and no field carries an identity that ranges beyond the repository namespace the
request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewCandidateRef`; `ComparisonIdentity` repointed to mcp/src/agents_remember/models/knowledge/review.py:161-172; mcp/src/agents_remember/models/knowledge/review.py:194-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewRevisionGroup`; `ReviewFieldChange` repointed to mcp/src/agents_remember/models/knowledge/review.py:213-222; mcp/src/agents_remember/models/knowledge/review.py:225-236. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewAuthoredEffect`; `ReviewSignal` repointed to mcp/src/agents_remember/models/knowledge/review.py:239-255; mcp/src/agents_remember/models/knowledge/review.py:258-273. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewEvidenceLink`; `ReviewObservation` repointed to mcp/src/agents_remember/models/knowledge/review.py:317-327; mcp/src/agents_remember/models/knowledge/review.py:330-347. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewRemainingCount` repointed to mcp/src/agents_remember/models/knowledge/review.py:350-376. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewSourceLocation` repointed to mcp/src/agents_remember/models/knowledge/review.py:379-397. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewSourcePane` repointed to mcp/src/agents_remember/models/knowledge/review.py:434-443. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewStaleness` repointed to mcp/src/agents_remember/models/knowledge/review.py:477-498. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewSubmission` repointed to mcp/src/agents_remember/models/knowledge/review.py:501-515. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `ReviewRefusal`; `KnowledgeReviewResult` repointed to mcp/src/agents_remember/models/knowledge/review.py:559-571; mcp/src/agents_remember/models/knowledge/review.py:574-589. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **re-read this claim against the construct its mechanically projected range now covers, and retired that projection record after the read.** The claim names the recorded surface version, the three pane names, `RRD:366`'s three proposed dispositions verbatim, the closed refusal-code union and the side-state union. Each anchor was resolved at its own current declaration: `KNOWLEDGE_REVIEW_SURFACE_VERSION` and `REVIEW_PANE_NAMES` are in `:74-76`, `PROPOSED_ASSESSMENT_DISPOSITIONS` in `:81-85`, `ReviewRefusalCode` in `:87-94` — now **six** members, the new one being `subject_unresolved` — and `ReviewSideState` at `:101`. The range covers all five; the claim's wording was **corrected, not merely retained**, because "the closed refusal-code union" is now a six-member union and the sentence did not say so. The generated repair bullet for this range was **retired** because that projection resolves exact NAMES rather than the claim's subject. No other bullet or row was deleted and no verification stamp was advanced.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): the vocabulary gained the **entry half** of the surface. This card now records `ReviewSubjectKind` (the two admitted subject kinds, declared **here once** so the transport's `SELECTOR_KINDS`, the entry list and the panes cannot disagree about which identities are reviewable), `ReviewEntry` (the reviewed subject as the shipped comparison selected it — a recorded identity, its own label and the operation's count, with **no field for a path, a file, a display version or a ranking**, which is what keeps "the browser never chooses the candidate" a property of the value), and `ReviewEntryListResult` (the entry read's typed outcome, whose validator refuses a **refused** read that offers any entry: "an entry beside a refusal is how a caller comes to review a subject nothing admitted"). `ReviewRefusalCode` gained its sixth member `subject_unresolved`, and the public vocabulary count moved from twenty-two to twenty-five models plus `ReviewSubjectKind`. No verification stamp was advanced, because no commit contains this body; the `reviewedWorkingCandidate` row now names this leaf's candidate.
- 2026-09-20T01:29+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared this card's one enforced citation row — a stale range on the signal case.** The row's second range was `553-571` for `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity`, whose declaration begins at 550 (its docstring "A signal is the matched condition with its versions and limits -- never a finding" opens the body, and the case ends at 566). The range was repointed to that case's own declaration extent, `:550-566`; the Finding text, both anchors and the row's other range (`:532-547`, the passing-observation case) are unchanged, and no citation was dropped. No other row, anchor or claim wording was touched, and no verification stamp was advanced.
- 2026-09-20T01:02:52+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): verified the 2 enforced citation rows this card carried (citation_anchor_absent_from_range ×2) by hand-reading `mcp/tests/test_knowledge_review_surface.py`: each named node sits inside the range its row now cites (`test_a_missing_side_is_its_own_state_and_never_an_empty_string` declared at 621, inside `:621-632`, beside `:505-521`; `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied` declared at 532, inside `:532-547`, beside `:553-571`), so the earlier mechanical projection was correct and needed no further edit; the claim wording, the anchors and every range are unchanged, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 2 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `test_a_missing_side_is_its_own_state_and_never_an_empty_string`; `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 2 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `review.py.md:216` (`test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`, `test_a_missing_side_is_its_own_state_and_never_an_empty_string`); `review.py.md:217` (`test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`, `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity`).
- 2026-09-18T18:20+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **re-read this card's own reopened claim against the construct its range now covers, and RETAINED its wording** — `KnowledgeReviewPayload`; `ReviewSideContent`, cited at mcp/src/agents_remember/models/knowledge/review.py:1-22 and `:490-528`. The claim says the module's docstring states what the module owns and the five prohibitions the display's shape enforces, and the cited ranges hold the docstring's five bullets and `class KnowledgeReviewPayload`; it is true as written. It reopens because at the temporary provenance this scrutiny uses (the leaf's base commit `2dcacb27`) `ReviewSideContent` does not exist — the card is one of this leaf's own six and every construct it cites is new. That is the stamp-relative condition, and it clears at closeout. No range was substituted or deleted and the verification stamp is **not** advanced.
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's three-pane vocabulary. It records the module's central fact — **it defines no record kind**, and the only thing it owns is the shape of a display — together with the five prohibitions that shape enforces: no field a conclusion could be assembled in, unassessed as the absence of a value, a missing side as its own state rather than an empty string, the stale rule as a constructor check on the payload, and the authored-record/mechanical-signal separation kept by element type. It also records each validator that makes those prohibitions structural rather than advisory (`ReviewSideContent`, `ReviewAssessmentDisplay`, `ReviewRemainingCount`, `ReviewKnowledgePane`, `ReviewEvidencePane`, `ReviewStaleness`, `KnowledgeReviewPayload`, `KnowledgeReviewResult`). This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
