# mcp/src/agents_remember/models/knowledge/review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T18:05+02:00 |
| lastVerifiedCommitHash |  `c5a74a85af20a8fb48cc44f59de7e926d589d3fc`|
| lastVerifiedCommitDate |  2026-09-18T18:30:35+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l22` uncommitted source; base `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
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

**Two recorded constants and one closed union are the module's vocabulary-level declarations.**
`KNOWLEDGE_REVIEW_SURFACE_VERSION` is `"knowledge-review-surface/1"` — a recorded value rather than a
package version read at display time, so two payloads produced by different renderings are
distinguishable from the payloads themselves — and it is the default of the payload's
`surface_version` field. `REVIEW_PANE_NAMES` is `("knowledge", "source", "evidence")`, the three panes
as a tuple rather than three separately spelled strings. `PROPOSED_ASSESSMENT_DISPOSITIONS` publishes
`RRD:366`'s three dispositions verbatim — `concern_found`, `no_concern_found`, `unresolved` — so a
reviewer can see which judgements are expressible; the source comment states that none of them is
publication approval. `ReviewRefusalCode` is the closed five-member union
`candidate_unresolved`, `candidate_not_live`, `candidate_dataset_absent`, `comparison_refused`,
`review_adapter_unavailable`, and `ReviewSideState` the four-member union `present`, `absent`,
`binary`, `unresolved`.

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

### Conventions

Every model here is a `KnowledgeModel`, and the shared bounds are imported rather than restated:
`LABEL_MAX_LENGTH`, `PATH_MAX_LENGTH`, `PROSE_MAX_LENGTH`, `REFERENCE_MAX_LENGTH` and
`SHA256_PATTERN` come from `models/knowledge/base.py`, so a display field is bounded by the same
constants every other knowledge model uses. Identity fields use `REFERENCE_MAX_LENGTH`, prose uses
`PROSE_MAX_LENGTH`, and the four digests on `ComparisonIdentity` are constrained by `SHA256_PATTERN`
rather than by a length. `__all__` names the whole public vocabulary: the two constants
`KNOWLEDGE_REVIEW_SURFACE_VERSION` and `REVIEW_PANE_NAMES`, the dispositions tuple, and all
twenty-two models plus `ReviewRefusalCode` and `ReviewSurfaceRequest`. `ReviewRefusalCode` and
`ReviewSideState` are `Literal` aliases rather than `enum` classes, and the three closed `record_kind`,
`side` and `change_state` vocabularies are inline `Literal`s on their fields. Immutable collections
are `tuple[...]` with `()` defaults, so no model carries a mutable default.

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
  together, and a refusal is never a degraded payload.
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
| The recorded surface version, the three pane names, `RRD:366`'s three proposed dispositions verbatim, the closed refusal-code union and the four-member side-state union. | `KNOWLEDGE_REVIEW_SURFACE_VERSION`; `REVIEW_PANE_NAMES`; `PROPOSED_ASSESSMENT_DISPOSITIONS`; `ReviewRefusalCode`; `ReviewSideState` | mcp/src/agents_remember/models/knowledge/review.py:69-92 |
| The shared shape that makes an unresolved reference a displayed fact rather than a dropped or anonymous one. | `ReviewUnresolvedReference` | mcp/src/agents_remember/models/knowledge/review.py:95-105 |
| **The missing-side rule as a constructor check: text exactly when `present`, in both directions.** | `ReviewSideContent` | mcp/src/agents_remember/models/knowledge/review.py:108-133 |
| The one request shape: a task context plus one of the read operation's own declared seeds, with no display version, instant or "latest" flag representable. | `ReviewSurfaceRequest`; `KnowledgeReadSeed` | mcp/src/agents_remember/models/knowledge/review.py:136-149; mcp/src/agents_remember/models/knowledge/read.py:1-60 |
| The candidate reference, which carries task identities and never a filesystem path, and the comparison identity carried verbatim rather than recomputed. | `ReviewCandidateRef`; `ComparisonIdentity` | mcp/src/agents_remember/models/knowledge/review.py:152-182 |
| The two per-side and per-item mechanical facts: the retained-revision count kept per side, and the field transition that states no meaning. | `ReviewRevisionGroup`; `ReviewFieldChange` | mcp/src/agents_remember/models/knowledge/review.py:185-208 |
| The authored record displayed as the author wrote it, with no field for a computed effect, and the detection fact with no severity, verdict or author. | `ReviewAuthoredEffect`; `ReviewSignal` | mcp/src/agents_remember/models/knowledge/review.py:211-245 |
| **The validator that refuses an anonymous verdict or an assessment that examined nothing.** | `ReviewAssessmentDisplay` | mcp/src/agents_remember/models/knowledge/review.py:248-286 |
| The evidence claim reference with its own authored limitations, and the observation that has no field for a sufficiency verdict. | `ReviewEvidenceLink`; `ReviewObservation` | mcp/src/agents_remember/models/knowledge/review.py:289-319 |
| **The two count rules: an unexplained absent count is refused, and a measured count carries no not-applicable reason.** | `ReviewRemainingCount` | mcp/src/agents_remember/models/knowledge/review.py:322-348 |
| The selected location whose missing role stays unclassified rather than guessed from a path. | `ReviewSourceLocation` | mcp/src/agents_remember/models/knowledge/review.py:351-369 |
| **Pane 1's own self-agreement rule: the pane's single assessment must be one of the assessments it displays, and the authored and mechanical collections keep separate element types.** | `ReviewKnowledgePane` | mcp/src/agents_remember/models/knowledge/review.py:372-403 |
| Pane 2: the selected locations, the expansion, and the changed paths the selection did and did not reach. | `ReviewSourcePane` | mcp/src/agents_remember/models/knowledge/review.py:406-415 |
| **Pane 3's two independent absence states, tied to the collections they describe.** | `ReviewEvidencePane` | mcp/src/agents_remember/models/knowledge/review.py:418-446 |
| The stale state that retains its previous input as a labelled value, and the rule that a current comparison has none to label. | `ReviewStaleness` | mcp/src/agents_remember/models/knowledge/review.py:449-470 |
| The submission state with no favourable member, and the boundary that none of the published dispositions is approval. | `ReviewSubmission` | mcp/src/agents_remember/models/knowledge/review.py:473-487 |
| **The whole payload and its stale/submission coupling, which refuses either direction of disagreement.** | `KnowledgeReviewPayload` | mcp/src/agents_remember/models/knowledge/review.py:490-528 |
| The refusal that is a state and never a degraded success, and the result that carries exactly one outcome. | `ReviewRefusal`; `KnowledgeReviewResult` | mcp/src/agents_remember/models/knowledge/review.py:531-561 |
| The shared bounds and the `KnowledgeModel` base every model here uses rather than restating its own. | `KnowledgeModel`; `PROSE_MAX_LENGTH`; `SHA256_PATTERN` | mcp/src/agents_remember/models/knowledge/base.py:1-80 |
| **The case that walks the whole payload schema for a field a generated conclusion could occupy.** | `test_the_whole_payload_schema_has_no_field_a_generated_conclusion_could_occupy` | mcp/tests/test_knowledge_review_surface.py:419-429 |
| **The case that asserts this module declares no record kind, no table and no status of its own.** | `test_the_surface_defines_no_record_kind_no_table_and_no_status_of_its_own` | mcp/tests/test_knowledge_review_surface.py:430-439 |
| The case that an unassessed subject is displayed unassessed and never defaulted to compatible, and the case that a missing side is its own state. | `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`; `test_a_missing_side_is_its_own_state_and_never_an_empty_string` | mcp/tests/test_knowledge_review_surface.py:505-521; mcp/tests/test_knowledge_review_surface.py:626-642 |
| The case that a passing observation is displayed as an observation and never as invariant-satisfied, and the case that a signal carries facts and scope limitations with no severity. | `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`; `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity` | mcp/tests/test_knowledge_review_surface.py:535-552; mcp/tests/test_knowledge_review_surface.py:553-571 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every model is a display shape over one
repository's records, and no field carries an identity that ranges beyond the repository namespace the
request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T18:20+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **re-read this card's own reopened claim against the construct its range now covers, and RETAINED its wording** — `KnowledgeReviewPayload`; `ReviewSideContent`, cited at mcp/src/agents_remember/models/knowledge/review.py:1-22 and `:490-528`. The claim says the module's docstring states what the module owns and the five prohibitions the display's shape enforces, and the cited ranges hold the docstring's five bullets and `class KnowledgeReviewPayload`; it is true as written. It reopens because at the temporary provenance this scrutiny uses (the leaf's base commit `2dcacb27`) `ReviewSideContent` does not exist — the card is one of this leaf's own six and every construct it cites is new. That is the stamp-relative condition, and it clears at closeout. No range was substituted or deleted and the verification stamp is **not** advanced.
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's three-pane vocabulary. It records the module's central fact — **it defines no record kind**, and the only thing it owns is the shape of a display — together with the five prohibitions that shape enforces: no field a conclusion could be assembled in, unassessed as the absence of a value, a missing side as its own state rather than an empty string, the stale rule as a constructor check on the payload, and the authored-record/mechanical-signal separation kept by element type. It also records each validator that makes those prohibitions structural rather than advisory (`ReviewSideContent`, `ReviewAssessmentDisplay`, `ReviewRemainingCount`, `ReviewKnowledgePane`, `ReviewEvidencePane`, `ReviewStaleness`, `KnowledgeReviewPayload`, `KnowledgeReviewResult`). This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
