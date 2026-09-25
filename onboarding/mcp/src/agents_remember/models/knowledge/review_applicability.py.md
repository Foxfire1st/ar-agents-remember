# mcp/src/agents_remember/models/knowledge/review_applicability.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_applicability.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T02:30+02:00 |
| lastVerifiedCommitHash | `09329a7ee598920c519b06305b73ba8e48d72c88` |
| lastVerifiedCommitDate | 2026-09-26T00:58:43+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**Why one supplied record may be displayed beside one selected subject** (`ICR-R26@v1`), as the wire
shape the review panes carry. Complete evidence delivery (`ICR-R14@v1`) and correct attribution are
separately falsifiable; this module is the vocabulary of the attribution half, and it is written so
the F09 defect is **unrepresentable** rather than merely fixed.

**Six display states, each a different recorded fact.** `direct` is a record whose own recorded
subject/revision binding names the selected subject, on a revision the selection retains, in the
displayed generation. `historical` is the same subject in another generation (or outside the
selection's recorded population), kept inspectable, labelled with the input identity it really
examined, and never read as this generation's result — dependency *currentness* is a separate
measurement (`ICR-R15@v1`). `candidate` is a record bound to the compared candidate rather than to a
subject, including every record of a review that selected no subject at all. `unresolved` is a
required binding that could not be resolved, displayed with the exact references it carries and the
reason. `unrelated` is a record whose recorded subject is a subject this comparison records and the
selection's relationships do not reach: it is **not** displayed as a judgment on the selected subject
at all, and the pane states how many records that is rather than dropping them silently. `context` is
the sixth state and has its own value: a record of *another* identity the selection reaches through an
explicit recorded relationship.

**This module decides nothing.** The policy lives in
[`application/review_record_applicability.py`](../../application/review_record_applicability.py.md);
what this module owns is that a misreading cannot be *recorded*: there is deliberately no field for a
similarity, a confidence, a score or a nearest match, so "this record probably applies" cannot be
written here by a caller that wanted to.

## Code Commentary

### Logic

**`ReviewApplicabilityClass` is the five supplied collections, spelled as the record-class vocabulary
minus its one measurement channel.** `assessments`, `detection_signals`, `verification_observations`,
`authored_effects` and `evidence_claims`; `assessment_currentness` is deliberately absent because it
reports *whether a measurement was supplied* and is not a collection of records, so no record can be
classified into it. The `REVIEW_APPLICABILITY_CLASSES` tuple is derived with `get_args` and an
import-time `assert` proves the equality against `ReviewRecordClassName` — so the two spellings cannot
drift, and a new record class that is not a measurement channel cannot be added without this module
being updated in the same edit.

**`ReviewApplicabilityState` is the six treatments, and `ReviewDisplayedApplicabilityState` the four a
*displayed* record can carry.** `context` is absent from the displayed union because a context record
is displayed as its own labelled value rather than as the selected subject's record, and `unrelated` is
absent because an unrelated record is not displayed as a judgment at all. The broader union exists for
the pane's stated count and for the context value's own vocabulary.

**`ReviewDisplayedApplicability` is why one displayed record may appear beside the selected subject.**
`subject_kind`/`subject_id` are the record's **own recorded subject** — the identity its binding named —
and are absent only where the record records none; `subject_revision_ids` carries the revisions the
record itself names; `references` are the exact recorded references the treatment was decided from, so
a reader can re-read the decision instead of trusting the label, and they are **required for every
state** because a label that names no recorded reference would be the surface's own opinion rather than
a statement about the record. The validator
`_require_the_subject_bearing_states_to_name_their_subject` makes the one attribution claim structural:
`direct` and `historical` are claims *about a subject*, so either state without a subject identity is
refused at construction — that is the F09 shape made unrepresentable.

**`ReviewContextRecord` is the packet's "related family/closure context" clause as a value.** It
carries the record's **true subject** (`subject_kind`/`subject_id`, required), the `relationship`
spelling that reached it, the record's own attribution (`author_ref`/`role_ref`) and its `references` —
and deliberately **not** its judgment content. A sibling's finding, disposition or rationale belongs to
that sibling's own review: displaying it is the cross-subject contamination this requirement exists to
prevent, while hiding the record entirely would erase recorded context the packet requires to stay
visible. `label` names the record's **kind** — the collection it came from, the condition a detection
matched, the record kind a matrix row shows — and never the record's judgment, which is the F-V3 fix of
this leaf's first verification round recorded as the value's own contract.

**`ReviewApplicabilitySummary` is one collection counted by treatment, and its two validators are the
"filtering is arithmetic, not erasure" rule.** `supplied` is the population the pane's collection was
classified from — the same population the collection's own `ICR-R14@v1` channel counts for the three
owner-read collections, and the rows the review matrix **page** returned for the two matrix-owned ones,
where the page is the displayed population and the owner's complete count travels on the channel (which
the summary's own `detail` states).
`_require_the_counts_to_partition_the_supplied_population` refuses a summary whose six states do not
account for every supplied record exactly once — a count that silently loses a record is how filtering
becomes erasure — and `_require_an_exclusion_to_state_itself` refuses an `unrelated` count a reader
cannot act on. `unrelated` records are named **by count and not by identity**: they are another
subject's records, and this review is not the place that displays them; the detail says so and names the
action that reaches them.

### Conventions

`__all__` publishes the six names: `ReviewApplicabilityClass`, `ReviewApplicabilityState`,
`ReviewApplicabilitySummary`, `ReviewContextRecord`, `ReviewDisplayedApplicability` and
`ReviewDisplayedApplicabilityState`. Every value is a
[`KnowledgeModel`](base.py.md) subclass, so the redaction and length rules of the wire surface apply to
it unchanged: identifiers use `REFERENCE_MAX_LENGTH`, labels `LABEL_MAX_LENGTH` and prose
`PROSE_MAX_LENGTH`, and every state/kind union is a `Literal` rather than a free string. All three
models are additive on the payload, so a payload published before these labels existed still validates
— which is what lets the client render an older body. The module holds no state and writes nothing.

### Invariants And Boundaries

- **A treatment is one of six named recorded facts, and there is no field for a seventh.** No
  relevance, similarity, confidence, score or nearest-match field exists here.
- **A subject-bearing claim must name its subject.** `direct` and `historical` without a subject
  identity are refused at construction.
- **Every label carries the references it was decided from.** `references` is required for every state,
  so the label is re-readable rather than an assertion.
- **A context row carries no judgment.** The value has a label (the record's kind), a true subject, a
  relationship, attribution and references — and no disposition, finding or rationale field.
- **A summary must partition its population exactly, and an exclusion must state itself.** Both are
  validators, not conventions.
- **This module declares the vocabulary, not the policy.** Which treatment a record earns is decided in
  `application/review_record_applicability.py`; nothing here reads a store, a comparison or a
  relationship.
- **No identity is invented here.** A subject identity is the record's own recorded binding; an absent
  subject stays absent rather than being filled with the selection's or the candidate's identity.

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
| **The module's own statement of the six treatments, what `context` is, and that no similarity or score can be recorded here.** | "Five display treatments, each a different recorded fact" | mcp/src/agents_remember/models/knowledge/review_applicability.py:1-40 |
| **The published vocabulary.** | `__all__` | mcp/src/agents_remember/models/knowledge/review_applicability.py:56-63 |
| **The five supplied collections, spelled as the record-class vocabulary minus its measurement channel, with the import-time assertion that keeps the two from drifting.** | `ReviewApplicabilityClass`; `REVIEW_APPLICABILITY_CLASSES` | mcp/src/agents_remember/models/knowledge/review_applicability.py:69-81 |
| **The six treatments, and the four a displayed record can carry.** | `ReviewApplicabilityState`; `ReviewDisplayedApplicabilityState` | mcp/src/agents_remember/models/knowledge/review_applicability.py:86-88; mcp/src/agents_remember/models/knowledge/review_applicability.py:93-93 |
| **Why one displayed record may appear beside the selected subject, with its own recorded subject and the exact references the treatment was decided from.** | `ReviewDisplayedApplicability` | mcp/src/agents_remember/models/knowledge/review_applicability.py:96-137 |
| **The validator that makes the F09 shape unrepresentable: a `direct` or `historical` claim without a subject identity is refused at construction.** | `_require_the_subject_bearing_states_to_name_their_subject` | mcp/src/agents_remember/models/knowledge/review_applicability.py:119-137 |
| **The labelled context value: true subject, the recorded relationship that reached it, author/role and references, and no judgment content.** | `ReviewContextRecord` | mcp/src/agents_remember/models/knowledge/review_applicability.py:140-166 |
| **One collection counted by treatment, with `supplied` stated per class and the two validators that refuse a losing partition and an unactionable exclusion.** | `ReviewApplicabilitySummary`; `_require_the_counts_to_partition_the_supplied_population`; `_require_an_exclusion_to_state_itself` | mcp/src/agents_remember/models/knowledge/review_applicability.py:169-222; mcp/src/agents_remember/models/knowledge/review_applicability.py:199-211; mcp/src/agents_remember/models/knowledge/review_applicability.py:214-222 |
| **The wire limit constants this vocabulary reads, shared with every other knowledge model.** | `KnowledgeModel`; `REFERENCE_MAX_LENGTH` | mcp/src/agents_remember/models/knowledge/base.py:1-40 |
| **The owner that produces these values, and the one place the policy lives.** | `review_applicability`; `AppliedRecords` | mcp/src/agents_remember/application/review_record_applicability.py:183-214; mcp/src/agents_remember/application/review_record_applicability.py:134-180 |
| **The re-export that keeps the vocabulary reachable through the payload module, and the five display models that carry a label plus the two panes that carry the context rows and the counts.** | `ReviewAuthoredEffect`; `ReviewKnowledgePane`; `ReviewEvidencePane` | mcp/src/agents_remember/models/knowledge/review.py:483-505; mcp/src/agents_remember/models/knowledge/review.py:680-756; mcp/src/agents_remember/models/knowledge/review.py:918-958 |
| **The cases that measure the vocabulary's own refusals and its class-set equality with the record vocabulary.** | `test_a_label_and_a_summary_refuse_a_claim_their_recorded_facts_do_not_support`; `test_the_class_vocabulary_is_the_record_vocabulary_minus_its_measurement_channel` | mcp/tests/test_knowledge_review_subject_isolation.py:528-553; mcp/tests/test_knowledge_review_subject_isolation.py:520-525 |
| **The client mirror of this vocabulary, and the one client case that proves a pre-label payload still renders.** | `ReviewDisplayedApplicability`; `ReviewContextRecord`; `ReviewApplicabilitySummary`; "still renders a payload published before the labels existed" | dashboard/src/data/review.ts:155-164; dashboard/src/data/review.ts:166-178; dashboard/src/data/review.ts:180-190; dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:299-310 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It is a wire vocabulary and names no
boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-25T22:19:46+00:00: Generated citation repair: `ReviewDisplayedApplicability`; `ReviewContextRecord`; `ReviewApplicabilitySummary`; "still renders a payload published before the labels existed" repointed to dashboard/src/data/review.ts:155-164; dashboard/src/data/review.ts:166-178; dashboard/src/data/review.ts:180-190; dashboard/src/panels/review/ReviewSurface.applicability.test.tsx:299-310. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-23T02:30:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): created this one-to-one card for the display vocabulary this leaf introduced (`ICR-R26@v1`). The card records the six treatments as six different recorded facts, the class union that is the record-class vocabulary minus its measurement channel (with the import-time assertion that keeps the two spellings equal), the two model validators that make a losing partition and an unnamed subject unrepresentable, the context value that carries a record's true subject and kind but none of its judgment, and the deliberate absence of any similarity, confidence or score field. **Stamp accounting:** the verification pair names the production line at this leaf's base — the last real commit the reading was taken against — because every construct this card cites exists only in this leaf's uncommitted candidate; the governed closeout owns the real stamp once the code commit exists. No claim in this card is made from a reading of a commit that does not contain the module.
