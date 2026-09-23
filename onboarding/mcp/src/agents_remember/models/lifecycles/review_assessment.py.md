# mcp/src/agents_remember/models/lifecycles/review_assessment.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/review_assessment.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T04:20+02:00 |
| lastVerifiedCommitHash | `e605822eb3bf83bf63a45963c5f51d5fc28859ee` |
| lastVerifiedCommitDate | 2026-09-23T12:19:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

**One authored curator judgment about one subject, bound to the exact inputs it examined.** This
module owns the `ReviewAssessment` record, the narrower `ReviewAssessmentRevision` a caller may
author, and the read projection that reports a subject's assessment state.

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

`_disposition_and_subject_agree` is the validator that keeps the three dispositions from being
interchangeable: `no_concern_found` carries no finding text and `concern_found` carries one, so
neither can be written in the other's shape. Nothing in the module reads the finding to decide
whether it is *true* — validation is structural only, and a checker that adjudicated the conclusion
would defeat the separation the type exists to enforce.

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
- **Structural validation only.** No code path reads a finding, a disposition or a state to decide an
  outcome; the stored value is data.
- **Absence is absence.** There is no default verdict and no `compatible` disposition; a subject with
  no record is `none-recorded` with a count of zero.
- **The assessed record is not stored here.** The record persists through the curator-coherence
  authority; this module owns its shape, not its home.
- **A moved binding leaves the judgment readable.** Staleness is reported as a state beside the
  finding, never by deleting or rewriting it.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three kinds of record that must not be promoted into each other. | `ReviewAssessment`; `AssessmentEvidenceReference` | mcp/src/agents_remember/models/lifecycles/review_assessment.py:188-213; mcp/src/agents_remember/models/lifecycles/review_assessment.py:374-395 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| What a caller may author, and the stored record that adds provenance and the examined-input binding. | `ReviewAssessmentRevision`; `ReviewAssessment`; `_AuthoredAssessmentFields`; `ExaminedInputs` | mcp/src/agents_remember/models/lifecycles/review_assessment.py:233-259; mcp/src/agents_remember/models/lifecycles/review_assessment.py:261-324; mcp/src/agents_remember/models/lifecycles/review_assessment.py:326-341; mcp/src/agents_remember/models/lifecycles/review_assessment.py:343-365 |
| The closed disposition vocabulary and the validator that keeps the three values from being spelled with each other's shape. | `ReviewAssessmentDisposition`; `_disposition_and_subject_agree` | mcp/src/agents_remember/models/lifecycles/review_assessment.py:49-61; mcp/src/agents_remember/models/lifecycles/review_assessment.py:338-354 |
| The subject kinds, the identity any kind carries, and the shape rule that pairs revisions with the kinds that have them. | `AssessmentSubject`; `_subject_shape_matches_its_kind` | mcp/src/agents_remember/models/lifecycles/review_assessment.py:131-185; mcp/src/agents_remember/models/lifecycles/review_assessment.py:170-185 |
| The subject states a read reports and the one function that decides which one a subject is in. | `SubjectAssessmentStatus`; `assessment_state_for` | mcp/src/agents_remember/models/lifecycles/review_assessment.py:95-102; mcp/src/agents_remember/models/lifecycles/review_assessment.py:542-594 |
| The read projection a caller receives, which carries identity, disposition and currentness and never a signal's payload. | `AssessmentEntry`; `SubjectAssessmentState` | mcp/src/agents_remember/models/lifecycles/review_assessment.py:439-451; mcp/src/agents_remember/models/lifecycles/review_assessment.py:453-539 |

## KS-R15@v1 Review Assessment Record

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

## Update History
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 citation-repair curator (memory worktree only; no code changed, no commits; leaf base `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta): **nine enforced citation findings discharged by re-pointing ranges; no claim, anchor or finding wording changed.** `ICR-R15@v1` rewrote this module's status vocabulary (502 → 620 lines), which moved every construct below the declaration block. **Citation accounting (old → new; every new range was re-read against the declaration it names in this candidate and contains it):** `AssessmentEvidenceReference` `:157-183` → `:188-213` and `ReviewAssessment` `:343-365` → `:374-395`; `_disposition_and_subject_agree` `:307-323` → `:338-354`; `AssessmentSubject` `:100-121` → `:131-185` and `_subject_shape_matches_its_kind` `:139-154` → `:170-185`; `SubjectAssessmentStatus` `:67-78` → `:95-102` and `assessment_state_for` `:441-501` → `:542-594`; `AssessmentEntry` `:408-414` → `:439-451` and `SubjectAssessmentState` `:416-439` → `:453-539`. The last two ranges are the anchors this leaf's own claim-reopen rows name, so those rows are now current rather than merely moved. No row was dropped and none was added. **No verification stamp was advanced**, because the candidate is uncommitted: `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are untouched and remain closeout-owned. **Left for the pass that may advance the stamp:** the Logic section above still says `assessment_state_for` decides among four states (`none-recorded`, `unresolved`, `stale`, `current`) and that an assessment the caller supplied no measurement for is reported `stale`; the candidate reports `not-measured` for that shape and `SubjectAssessmentStatus` now has six members. Changing those sentences is a claim review, not a range repair, so it is recorded here rather than made silently.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `e963a01c`): created this card for the `ReviewAssessment` record the leaf added — the closed
  disposition vocabulary with `unresolved` first-class, the four subject kinds, the authored-versus-
  stored field split that keeps caller-supplied authority unrepresentable, the structural-only
  validation rule, and the four-state read projection in which absence stays absence. Verification
  metadata remains closeout-owned; no acceptance or certification claim is made.
