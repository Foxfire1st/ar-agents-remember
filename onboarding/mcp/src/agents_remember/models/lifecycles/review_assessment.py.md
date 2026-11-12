# mcp/src/agents_remember/models/lifecycles/review_assessment.py

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

**One authored curator judgment about one subject, bound to the exact inputs it examined.** This
module owns the retained `ReviewAssessment` record, the narrower `ReviewAssessmentRevision` a caller may
author, and the read projection that reports a subject's assessment state. This model remains for the
coherence authority; the current tree-review answer instead carries judgment rows and proofs.
Removal of the reviewer channel is not deletion of this independently used record shape.

It exists because three kinds of record meet on this branch and must not be promotable into each
other: a **worker claim** (an agent-authored assertion), a **machine signal** (a detector's factual
output, `KS-R14@v1`), and a **reviewer conclusion** (this record). That separation is a property of
the *type* rather than of a convention — no constructor here accepts a detection-signal payload or a
facet payload, and the module offers no conversion operation in either direction. Where an
assessment cites a signal it does so through `AssessmentEvidenceReference`, a citation type that
keeps both records and both types.

## Code Commentary

### Logic

`ReviewAssessmentDisposition` is the one closed vocabulary — `concern_found`, `no_concern_found`,
`unresolved` — and `unresolved` is a first-class outcome rather than a failure, so a curator who
could not decide has a value to write instead of having to overstate. `AssessmentSubject` carries the
judged identity under four kinds (`knowledge-record`, `family`, `invariant-revision`, `comparison`);
`recordId` names the subject's own record identity under every kind, which is what keeps a family
assessment from being spelled as a manufactured `sourceFile`, and `_subject_shape_matches_its_kind`
requires a revision-bearing kind to name its revisions while refusing them for `comparison`.

`ReviewAssessmentRevision` and `ReviewAssessment` share `_AuthoredAssessmentFields`, and the
difference between them is the requirement made structural: the revision has no `provenance`, no
`authorRef`, no `authorRole` and no `examinedInputs`, so a caller cannot author an assessment under
another identity or claim inputs it did not examine. Those four fields exist only on the stored
record, where the publication path supplies them.

`_disposition_and_subject_agree` requires a comparison subject to name the record's comparison and
refuses nonempty finding text for `no_concern_found`. The converse is not enforced here:
`concern_found` is allowed to carry an empty finding. These are structural checks, not a semantic
judgment that the finding is true or that an authored concern is substantively sufficient.

`assessment_state_for` is the single place that decides which state a subject is in. As of
`260921-ICR-L15` (`ICR-R15@v1`) the **subject** vocabulary has six members — `none-recorded`,
`unresolved`, `stale`, `not-measured` and `unavailable`, plus `current` — while the per-record
`AssessmentEntry.currentness` carries the four-member measured status (`not-measured`, `current`,
`stale`, `unavailable`). `none-recorded` is a state of the **subject**, not a disposition, which is how
absence stays representable as absence; the validator refuses a count that contradicts the records
beside it, so a subject with no stored assessment answers zero rather than a favourable default. An
assessment the caller supplied **no measurement for is reported `not-measured`, never `current` and
never `stale`**: the absence of a measurement is not evidence of movement, which is the defect this
leaf closed.

`SubjectAssessmentState` now requires `unresolvedCount` to equal the actual number of entries whose
disposition is `unresolved`, independently of their currentness. Merely staying below the total is
not enough. The existing partition checks still compare each declared binding-state count with
the entries and keep their precedence: stale, unavailable, unresolved, not-measured, then current.
The factory derives the same unresolved population; this is not an inference that unmeasured records passed.

### Conventions

- Every model is strict, frozen and `extra="forbid"`, the same seam the other durable records use.
- Text fields are stripped and refused when blank; authored evidence references are required to be
  unique so one citation cannot be counted twice.
- `AssessmentEvidenceReference` is namespace-relative (`code`, `memory`, `task`) and typed at the
  model boundary, so a fourth namespace cannot appear without a decision.
- `AssessmentEvidenceByte` records the three facts of a published byte — task-root-relative path,
  digest and size — and refuses a path that is not task-relative.

### Invariants And Boundaries

- **No promotion and no conversion.** Nothing here turns a signal, a facet payload or a worker claim
  into an assessment, and nothing turns an assessment into one of them.
- **Structural validation only.** Validators inspect dispositions and binding states to check counts
  and derive the declared summary state; they do not adjudicate the truth of an authored finding.
- **Absence is absence.** There is no default verdict and no `compatible` disposition; a subject with
  no record is `none-recorded` with a count of zero.
- **The assessed record is not stored here.** The record persists through the curator-coherence
  authority; this module owns its shape, not its home.
- **A moved binding leaves the judgment readable.** Staleness is reported as a state beside the
  finding, never by deleting or rewriting it.

## Evidence

### Docs References

No Domain Documentation entries are configured. Current model bodies, their retained owner boundary
and the named stored assertion supply the repository evidence, not an external design-source read.

## Historical KS-R15@v1 creation account — retained, not current reviewer delivery

This section preserves the creation-era account, including its then-current channel and partial-delivery
wording. It is not a present promise of a reviewer assessment channel or later-work debt.

**The leaf that created this module.** `KS-R15@v1` §1 charters the typed record with the named field
set and a closed, stored disposition vocabulary in which `unresolved` is first-class; §2 requires the
author and role to come from the authenticated path rather than caller text; §3 requires the three
kinds to be three types with no conversion in either direction; and §4 requires absence to be
reported as absence with no default verdict.

The additions this card records beyond the module's own shape:

- The **currentness field** is `binding_state` on the projection (owned by
  `review_assessment_binding.py`), chosen to match the same-named, same-two-member literal L14
  shipped on `DetectionRunCurrentness.binding_state` rather than the coherence authority's own
  free-form `currentnessStatus`.
- The **typed collection** on the coherence authority is `CuratorCoherenceRecord.assessments`, a
  collection separate from `judgments` with its own uniqueness validator; exact source-candidate
  coverage is unchanged and still enforced by `_judgments_cover_candidates_exactly`.
- Delivery is reported as **partial in one place only**: `require_current_assessment_binding` and
  `require_current_assessments` are delivered and tested refusing primitives, but no publication
  action calls them, because the coherence `publish` action has no "submit against an existing
  assessment's comparison" input and adding one would invent a submission gate the packet does not
  charter. The consumption-side refusal belongs to the views and review-surface requirements.

## Evidence

The following current source and stored assertion bodies were inspected, not executed here. They do
not constitute a fresh runtime result, code verdict or whole-MEMORY acceptance.

- Retained assessment and evidence-reference values keep authored records distinct from their citations; this model supplies no conversion operation. [1]
- Caller revision and stored assessment share authored fields; provenance and examined-input binding belong to the stored record, not the caller revision. [2]
- The closed disposition vocabulary and actual validator refuse nonempty no_concern_found finding text; the converse concern_found finding requirement is not enforced. [3]
- Subject identity and revision-bearing-kind constraints are structural and keep comparison subjects tied to their own comparison. [4]
- The projection keeps explicit none-recorded and unmeasured states; the factory derives counted dispositions and uses binding-state precedence without manufacturing measurements. [5]
- Assessment entries retain identity/disposition/currentness and the subject summary validates the actual carried entries and binding-state partition. [6]
- Unresolved count is the number of unresolved dispositions, not merely an integer below the total; the stored regression rejects both a false zero and a false one within the total. [7]
