# mcp/src/agents_remember/application/review_record_rendering.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_record_rendering.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T02:40+02:00 |
| lastVerifiedCommitHash | `e605822eb3bf83bf63a45963c5f51d5fc28859ee` |
| lastVerifiedCommitDate | 2026-09-23T12:19:01+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The **record half** of one review: what the renderer is *given*, rendered as the surface's own pane
values. The review adapter composes operations; this module renders the collections a caller supplied,
and it is separate for the file-size rail's reason **and for one of its own**: the same rendering is
used by the subject review and by the task-context review, so a second copy of it would be the place
where the two surfaces come to disagree about what an unassessed subject looks like.

Nothing here selects a record, resolves a reference or decides an outcome. Every function takes the
typed value another owner published and returns the surface's own display value:

- an assessment collection is projected per subject with its currentness **as measured** — a caller
  that supplied no `current` mapping gets every assessment reported `stale`, because the shipped
  projection refuses to promote an unmeasured assessment and this module does not improve on it;
- an empty assessment collection is `unassessed` and an empty evidence collection is `none_recorded`,
  and neither has a favourable member to default to;
- a detection signal is carried with its condition, inputs, versions and scope limitations only, and
  there is no field in its display value for a voice, a severity or a disposition.

**Since `ICR-R14@v1` it also carries the availability fact that goes with the collections, and it
renders each evidence claim's own recorded fields.** `ReviewRecordInputs.channels` is the composition's
own supply of every record class it read, one entry per class, and it travels onto the pane
**whole** — a class that was not read, or could not be read, appears with that state instead of being
absent from the list. The channels are deliberately **not** derived from the collection lengths here:
an empty tuple is exactly what this module must be able to render without claiming which of the three
facts it is (`none_recorded`, `unavailable`, `not_selected`). The second addition is
`ReviewClaimRecord`: a claim's identity already reached the surface through the matrix row, but the row
deliberately does not restate the claim's content, so the authored fields travel as a renderer input
read from the claim's own owner.

**What moved here, and from where.** `ReviewRecordInputs`, `EMPTY_REVIEW_RECORDS`, `refused`,
`submission`, `evidence_pane`, `subject_states`, `assessment_displays`, `observation` and `signal`
were private helpers (`_refused`, `_submission`, `_evidence_pane`, `_subject_states`,
`_assessment_displays`, `_observation`, `_signal`) of `application/knowledge_review.py`. They were
moved **verbatim except for the names**, which were de-privatised because two compositions now call
them, and the adapter re-exports `ReviewRecordInputs` and `EMPTY_REVIEW_RECORDS` so the existing
importers (`cli/dashboard.py` and two test modules) keep resolving without a new home to learn.

## Code Commentary

### Logic

**`ReviewRecordInputs` is the frozen set of collections the renderer is handed, and it is a dataclass
rather than a pydantic model because it carries other owners' live record objects rather than a wire
shape.** `assessments`, an optional `current` mapping, `signals`, `observations`, `claims` and
`channels`. `current` is `None` by default and that default is the honest one: the surface has no
measurement of its own to supply, so every assessment it displays is reported as the shipped
projection reports an unmeasured one. `EMPTY_REVIEW_RECORDS` is the single module-level empty value —
a call in an argument default would rebuild it on every call, and the collections it holds are
immutable tuples.

**`ReviewClaimRecord` is one claim's own recorded fields as the evidence owner serves them**, and it
is a renderer input rather than a record: `claim_id`, the admission's `author_ref`, the record's
`lifecycle`, the declared `limitations` (**verbatim** — `""` is the author's own "no limitations
declared" and never "unknown") and the `claimed_coverage` endpoints the author asserted. Nothing in it
is derived, ranked or filtered; the record owner
([`application/review_evidence_records.py`](review_evidence_records.py.md)) builds it from the claim's
own owner read.

**`refused` is the one builder of a refused result in this surface.** It returns
`KnowledgeReviewResult(state="refused", repository_id=…, refusal=…)` with no payload, which is what
makes "a refusal is a state and never a degraded success" a property of a constructor rather than a
convention. Both compositions and both entry points reach it, so no code path raises out of a review
read.

**`submission` publishes the two states a display-only surface may have, and grows no private write
path.** It returns `disabled_stale` exactly when the caller says the comparison is stale — with the
reason "Candidate changed — open a new comparison" and the matching next action — and `unavailable`
otherwise, with the reason that this increment mounts no serving route that publishes an assessment
and a next action naming **the existing curator authority's publication action**. In both cases it
carries `PROPOSED_ASSESSMENT_DISPOSITIONS`, which is that authority's own vocabulary rather than a
control this surface invented.

**`evidence_pane` is pane 3, and its two absence states are computed from the collections themselves.**
`evidence_state` is `recorded` when there is at least one evidence link or observation and
`none_recorded` otherwise; `assessment_state` is `assessed` when at least one assessment display
exists and `unassessed` otherwise. It also carries `records.channels` onto the pane unchanged — this
is the one place the availability list reaches the served payload — and it renders each claim's link
through `_evidence_link`. `source_inspection_available=True` is carried here as it was before the move
(F10's recorded finding: the constant is the surface's own statement, and R03/R10 own any change to
it).

**`_evidence_link` is the one per-claim projection, and it has two shapes rather than one.**
`evidence_pane` indexes the supplied claims by identity and hands each matrix row its own record. A
claim this composition supplied gets the claim's own recorded fields **verbatim** — `author_ref`,
`lifecycle`, `claimed_coverage`, and `limitations=(claim.limitations,)` where an empty member is the
author's recorded "no limitations declared" and not missing data — plus the row's own assessment
references, and **no** unresolved reference. A claim whose record the evidence owner did not supply
keeps its identity and its assessment references and names the missing half as one
`ReviewUnresolvedReference` of field `claim_content`, with the detail naming both halves of the
evidence: the matrix publishes the claim's identity, lifecycle and assessment references, and the
evidence owner's own read of *this* claim supplied no content for it. That is why an unread claim is
never rendered as a claim that declared no limitations — before `ICR-R14@v1` every claim link carried
exactly that unresolved-coverage reference, which was true of the pane's knowledge and false of the
claim's.

**`subject_states` projects every stored assessment per subject and leaves currentness as measured.** A
caller that supplied no `current` measurement gets every assessment reported `stale`: the shipped
projection refuses to promote an unmeasured assessment to current, and this surface does not improve
on that by guessing which dependencies still match. `assessment_displays` then renders that projection
in order, de-duplicating by assessment id and reading each record's author provenance, examined inputs
and evidence references; `_assessment_display` is the one per-record projection, and its
`examined_inputs` falls back to the comparison reference when a record names no identities — the
record's own fact rather than an empty list.

**`observation` displays a verification observation exactly, and adds no sufficiency field.** The
command identity, the result artifact reference and digest, the execution result, the tested
candidate's logical digest and the environment identity are carried through; `limitations` is the
empty tuple and the docstring says why — a verification observation carries no authored limitation
field of its own, so the pane adds none rather than inventing one, and no sufficiency claim is made
from a result.

**`signal` carries one detection fact and nothing that could read as a verdict.** Condition, declared
input set, governing route, relationship paths, extractor version, policy version and the signal's own
scope limitations — and there is deliberately no field for a voice, a severity or a disposition.

### Conventions

`__all__` publishes the ten names the two compositions and the adapter consume: `EMPTY_REVIEW_RECORDS`,
`ReviewClaimRecord`, `ReviewRecordInputs`, `assessment_displays`, `evidence_pane`, `observation`,
`refused`, `signal`, `subject_states` and `submission`. Every value returned is a shipped type from
`models/knowledge/review.py`, `models/knowledge/detection.py`,
`models/knowledge/evidence.py` or `models/knowledge/view.py`; this module declares no model of its
own, and the one declaration it added (`ReviewClaimRecord`) is a frozen dataclass because it carries
another owner's record fields rather than a wire shape. Names are public where two callers use them and
private (`_assessment_display`, `_evidence_link`) where one does. The module holds no state and writes
nothing.

### Invariants And Boundaries

- **The renderer renders what it is given.** No function here resolves a reference, selects a record,
  ranks a subject or decides an outcome; the collections belong to other owners' read paths.
- **An absence is never a favourable default.** No assessments ⇒ `unassessed`; no evidence ⇒
  `none_recorded`; no `current` measurement ⇒ every assessment `stale`. None of the three is a
  clearance.
- **The availability list is carried, never recomputed.** `channels` reaches the pane exactly as the
  composition supplied it; this module never derives a state from a collection's length, because the
  whole point of the vocabulary is that an empty tuple has three possible meanings.
- **A claim is unresolved only when its own content was not supplied.** A claim this renderer holds is
  rendered with its own authored fields and no unresolved reference; the `claim_content` reference is
  reserved for the one case where the owner's read supplied nothing for that identity.
- **The authored field is rendered verbatim.** An empty `limitations` member is the author's recorded
  statement, and no rendering turns it into "unknown" or drops it.
- **`submission` never invents a write path.** Its `unavailable` state names the curator authority's
  own publication action, and its proposed dispositions are that authority's vocabulary.
- **One rendering, two compositions.** The subject review and the task-context review call these same
  functions, which is why an unassessed collection reads identically in both.
- **No path, no candidate and no store.** The module touches no filesystem, opens no database and
  carries no identity beyond the record values it is handed.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and
functions, the review models it builds, the two compositions that call it, the record owner that
supplies the collections, and the adapter that re-exports two of its names. Three details a reader
should carry: the seven original renderers are a **verbatim move** (names de-privatised, bodies
unchanged) from `knowledge_review.py`; the `unmeasured-is-stale` rule and the two absence states came
with them rather than being re-decided here; and since `ICR-R14@v1` the module also carries the
**availability list** and renders each claim from the claim's own recorded fields — the
"one unresolved coverage reference per claim" the earlier table described is now true only of a claim
whose own record was not supplied, because the record owner supplies every claim the candidate holds.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it renders, why it is separate, and the three rules its values obey. | `unassessed`; `none_recorded` | mcp/src/agents_remember/application/review_record_rendering.py:1-18 |
| The published surface: the record input set, the empty value, and the seven renderers. | `__all__` | mcp/src/agents_remember/application/review_record_rendering.py:46-56 |
| **The collections the renderer is given, with the currentness measurement optional and its absence meaning "unmeasured".** | `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/review_record_rendering.py:183-183; mcp/src/agents_remember/application/review_record_rendering.py:85-111 |
| **The one refused-result builder the whole surface reaches, so a refusal is a state and never a degraded success.** | `refused`; `KnowledgeReviewResult` | mcp/src/agents_remember/application/review_record_rendering.py:186-191; mcp/src/agents_remember/models/knowledge/review.py:1119-1134 |
| **Whether an assessment may be submitted: `disabled_stale` or `unavailable`, and never a private write path — the next action names the existing curator authority.** | `submission`; `PROPOSED_ASSESSMENT_DISPOSITIONS` | mcp/src/agents_remember/application/review_record_rendering.py:183-210; mcp/src/agents_remember/models/knowledge/review.py:137-141 |
| **Pane 3: the evidence links with their unresolved coverage, the observations displayed exactly, and the two absence states computed from the collections themselves.** | `evidence_pane`; `ReviewEvidenceLink`; `ReviewEvidencePane` | mcp/src/agents_remember/application/review_record_rendering.py:213-252; mcp/src/agents_remember/models/knowledge/review.py:569-580; mcp/src/agents_remember/models/knowledge/review.py:918-958 |
| **The per-subject projection that reports an unmeasured assessment `stale` rather than promoting it to current.** | `subject_states`; `assessment_state_for` | mcp/src/agents_remember/application/review_record_rendering.py:178-198; mcp/src/agents_remember/models/lifecycles/review_assessment.py:542-594 |
| The assessment display, its per-record projection, and the examined-inputs fallback to the record's own comparison reference. | `assessment_displays`; `_assessment_display`; `ReviewAssessmentDisplay` | mcp/src/agents_remember/application/review_record_rendering.py:277-302; mcp/src/agents_remember/application/review_record_rendering.py:305-322; mcp/src/agents_remember/models/knowledge/review.py:527-566 |
| **A verification observation displayed exactly, with no sufficiency field and no invented limitation.** | `observation`; `VerificationObservationPayload` | mcp/src/agents_remember/application/review_record_rendering.py:215-233; mcp/src/agents_remember/models/knowledge/evidence.py:1-40; mcp/src/agents_remember/application/review_record_rendering.py:276-294 |
| **A detection fact carried with its inputs, versions and scope limitations only — no voice, no severity, no disposition.** | `signal`; `DetectionSignalPayload` | mcp/src/agents_remember/application/review_record_rendering.py:297-311; mcp/src/agents_remember/models/knowledge/detection.py:1-40; mcp/src/agents_remember/models/knowledge/detection.py:635-753|
| **The adapter that re-exports the record input set and its empty value, so the existing importers keep resolving without a new home to learn.** | `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/knowledge_review.py:109-109; mcp/src/agents_remember/application/knowledge_review.py:111-111 |
| The two callers: the subject composition, which renders the matrix rows beside these records. | `compose_review`; `_knowledge_pane` | mcp/src/agents_remember/application/knowledge_review.py:327-500; mcp/src/agents_remember/application/knowledge_review.py:926-978 |
| **The second caller, which is why this module exists: the task-context composition renders the same records with no matrix and no comparison.** | `task_context_review`; `_task_context_pane` | mcp/src/agents_remember/application/review_task_context.py:84-158; mcp/src/agents_remember/application/review_task_context.py:170-193 |
| The published assessment collection the adapter reads from the curator authority's own publication, with an absent authority treated as empty rather than as an error. | `review_records_for`; `load_curator_coherence_authority` | mcp/src/agents_remember/application/review_evidence_records.py:174-192; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:255-280 |
| The published surface: the record input set, the empty value, the claim renderer input and the seven renderers. | `__all__` | mcp/src/agents_remember/application/review_record_rendering.py:47-58 |
| **The collections the renderer is given — including the supplied claims and the availability list — with the currentness measurement optional and its absence meaning "unmeasured".** | `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/review_record_rendering.py:85-111 |
| **One claim's own recorded fields as the evidence owner serves them, with the authored limitations verbatim and nothing derived.** | `ReviewClaimRecord` | mcp/src/agents_remember/application/review_record_rendering.py:61-82 |
| **Pane 3: the links rendered from each claim's own record, the observations displayed exactly, the two absence states computed from the collections, and the availability list carried onto the pane unchanged.** | `evidence_pane`; `ReviewEvidenceLink`; `ReviewEvidencePane` | mcp/src/agents_remember/application/review_record_rendering.py:213-252; mcp/src/agents_remember/models/knowledge/review.py:569-580; mcp/src/agents_remember/models/knowledge/review.py:918-958 |
| **The one per-claim projection and its two shapes: a supplied claim's own author, lifecycle, limitations and coverage, or an identity whose missing content is named as unresolved.** | `_evidence_link` | mcp/src/agents_remember/application/review_record_rendering.py:325-368 |
| **The record owner that resolves the collections and builds each claim's renderer input, and which the adapter re-exports instead of owning.** | `review_records_for`; `_claim_record` | mcp/src/agents_remember/application/review_evidence_records.py:575-598; mcp/src/agents_remember/application/review_evidence_records.py:548-572; mcp/src/agents_remember/application/review_evidence_records.py:171-196|
| **The cases that measure the rendered values: unassessed is never defaulted to compatible, a passing observation is never invariant-satisfied, and a detection signal carries no severity.** | `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`; `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`; `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity`; `test_the_surface_reports_the_absent_submission_path_instead_of_growing_a_private_one` | mcp/tests/test_knowledge_review_surface.py:606-622; mcp/tests/test_knowledge_review_surface.py:588-603; mcp/tests/test_knowledge_review_surface.py:650-659; mcp/tests/test_knowledge_review_surface.py:560-584 |
| **The rendering a task-context review produces for the same records, measured through the real composition.** | `test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all` | mcp/tests/test_knowledge_review_source_endpoints.py:733-810 |
| **The cases that measure the two new claim-link shapes: an authored claim rendering its own limitations and coverage, and a damaged claim's identity kept with its content named unresolved.** | `test_the_production_composition_supplies_every_owner_produced_record_class`; `test_a_damaged_evidence_claim_is_named_while_its_siblings_are_supplied` | mcp/tests/test_knowledge_review_evidence_channels.py:552-605; mcp/tests/test_knowledge_review_evidence_channels.py:847-870 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It transforms record values supplied by other
owners into this surface's display values and touches no boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-22T09:20:00+02:00 — 260921-ICR-L4 curator (gate repair pass on the merged line): **three enforced rows re-cited.** The pane-3 row, the second-caller row and the assessment-collection row cited pre-merge ranges; they now cite the merged declarations (`review_record_rendering.py:152-176`, `review_task_context.py:84-158`/`170-193`, `review_evidence_records.py:174-192`). Wording unchanged; no stamp advanced.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the one enforced citation row was re-read and its range written to the construct's real extent.** The row's first anchor, `review_records_for`, cited `mcp/src/agents_remember/application/knowledge_review.py:850-875` — a range that ends **44 lines past the end of the file**, which has 831 lines, so the citation could not name anything at all. The construct is at **806-831** (its `def` at 806, its last statement at 831), and the row now cites that extent; the anchor was verified to occur literally at 806 inside it. The row's second range (`curator_coherence.py:255-280` for `load_curator_coherence_authority`) was checked and is unchanged, as is every other row. The claim wording is unchanged and remains true. This is a citation-only repair; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately **not** advanced, because nothing in this leaf is committed and the governed closeout owns the real stamp.
- 2026-09-21T21:40:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **this card's claim that every evidence link carries one unresolved-coverage reference stopped being true, and the module gained the availability list.** `ICR-R14@v1`'s record owner now supplies every claim the candidate records, read from the claim's own owner, so the renderer gained `ReviewClaimRecord` (a frozen input carrying the claim's `author_ref`, `lifecycle`, verbatim `limitations` and asserted `claimed_coverage`) and the pane gained `records.channels` — the composition's own supply of every record class, carried **whole** onto `ReviewEvidencePane.channels` and deliberately not derived from collection lengths here, because an empty tuple has three possible meanings and this module must be able to render all three without claiming which one it is. `ReviewRecordInputs` therefore gained `claims` and `channels`; `evidence_pane` now renders each link through `_evidence_link`, whose two shapes the Logic section states — a supplied claim's own fields and **no** unresolved reference, or an identity whose missing content is named (`claim_content`) — and the Purpose paragraph records that the previous wording described the pane's knowledge, which was true before the owner supplied the claims and false after. `__all__` publishes ten names now (`ReviewClaimRecord` added); the Conventions and Invariants sections were corrected with the body rather than left describing the nine-name surface. **Citation accounting:** every range into the three files this leaf moved was re-derived from each construct's own declaration extent in the candidate rather than shifted — this module's docstring is unchanged at `1-18` but everything below the import block moved, so the rows were re-measured (`__all__` `46-56`→`47-58`, `ReviewRecordInputs` `59-77`→`85-111`, `refused` `80-85`→`114-120`, `submission` `88-115`→`122-149`, `evidence_pane` `118-154`→`152-176`, `subject_states` `157-176`→`178-198`, `assessment_displays` `179-212`→`200-234`, `observation` `215-233`→`276-294`, `signal` `236-250`→`297-311`), `models/knowledge/review.py` grew 836→851 so `PROPOSED_ASSESSMENT_DISPOSITIONS` is `100-121`, `ReviewAssessmentDisplay` `323-362`, `ReviewEvidenceLink` `364-375`, `ReviewEvidencePane` `643-666` and `KnowledgeReviewResult` `805-823`, and the external references moved with their files (`_knowledge_pane` `653-686`→`688-720`, `task_context_review`/`_task_context_pane` `59-104`/`107-129`→`64-105`/`131-152`, the R01 enclosure case `674-750`→`733-810`). The row that cited `review_records_for` at `knowledge_review.py:850-875` was **repointed, not reworded**: the resolver now lives in `application/review_evidence_records.py:174-192` and the adapter re-exports it, so the row cites the owner and the `_claim_record` that builds this module's own input. Two rows were added for the new claim renderer input and the two link shapes, and one for the two cases that measure them; nothing was dropped. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` now name the **production line this reading was against** — `d80a0513e928ef29a973527d09597c82c96fde87`, the master line's current tip and this leaf's base — replacing the previous pair rather than leaving a stamp no reading in this pass measured; the candidate is uncommitted, so no commit contains the content a stamp would claim to have verified, and the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates.
- 2026-09-21T16:10+02:00 — orchestrating session, pre-closeout metadata repair on `ar/260921-icr-l2`: the governed closeout refused the memory leg because this card for a module that exists only in this leaf's uncommitted candidate carried no verification stamp in its header metadata (`external-memory closeout requires onboarding verification metadata before memory commit`). The two fields were added naming the **production line this card was read against** — `c755cec6…`, the master line after this leaf's resolved syncs brought in the ICR-L5 and ICR-L19 landings, at that closeout's recorded time `2026-09-21T15:29:12+02:00` — and the candidate row was left as it was. This states what the reading was against, not that the module exists in that commit; the closeout's own metadata refresh re-stamps the card against the code commit this transaction creates. No range, claim or anchor was changed by this repair.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): created this one-to-one card for the module this leaf introduced by extracting the review adapter's **record-rendering** responsibility. The card records what the module is rather than only what moved: the collections it is *given* (`ReviewRecordInputs`, with `current` optional and its absence meaning "unmeasured"), the one refused-result builder, the two-state submission value that names the curator authority instead of growing a write path, pane 3's two absence states computed from the collections themselves, the per-subject projection that reports an unmeasured assessment `stale`, and the two display values (`observation`, `signal`) that carry no sufficiency, severity or disposition field. It also records the move's provenance: seven helpers came from `application/knowledge_review.py` verbatim, with the private names de-privatised because **two** compositions now call them — which is the module's second reason for existing, since one copy is what keeps an unassessed collection reading identically in the subject review and in the task-context review. **Stamp accounting:** this card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**, because every construct it cites exists only in this leaf's uncommitted candidate and no real commit contains the content a stamp would claim to have verified; what was actually read is this leaf's uncommitted working tree, and closeout owns the real stamp once the code commit exists.
## 260921-ICR-L26 The Renderer Carries The Label And The Port

`260921-ICR-L26` (`ICR-R26@v1`) makes this module the surface's **labelled** renderer without letting
it decide anything. It gained `ReviewApplicabilityProjection` — a `Protocol` stating exactly what a pane
needs from the applicability projection (`label_of`, `context_of`, `summaries_of`) — and the two
collection tuples `KNOWLEDGE_APPLICABILITY_CLASSES` and `EVIDENCE_APPLICABILITY_CLASSES`, declared once
so a pane's channels, its labelled values and its counts describe one population. **311 → 473 lines.**

**Every renderer now takes the projection and renders only what it kept.** `evidence_pane` and
`assessment_displays` filter through `label_of` (a record whose recorded subject is another identity is
either labelled context or not displayed as this subject's judgment at all, so it never reaches these
collections), `observation` and `signal` carry the label beside their facts, and both panes gained
`context` and `applicability`. The dependency stays one-way: this module renders the values it is
handed and the projection is the module that decided which values those are — the renderer still
reaches no comparison, no relationship and no store.

**Two renderers moved here, verbatim except for their names.** `authored_effects` and
`unresolved_authors` were `knowledge_review._authored_effect` and `knowledge_review._unresolved_author`;
they are the pane's authored rows and the "the matrix publishes no author for this record" reference,
and they moved because the adapter is over the repository's soft file-size rail. The unresolved
constant is stated once here rather than in the adapter.

**The one renderer input that gained a field.** `ReviewClaimRecord.subject_revision_id` carries the
claim's **own recorded subject revision**, read by the evidence owner from the claim's own subject edge;
it is absent exactly when the claim records a facet-revision subject or none at all, and an absent
subject is never filled with the candidate's or the selection's identity.

## Update History
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (candidate uncommitted; basis: leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta): **six enforced citation rows re-pointed to the declarations they name.** Citation accounting: `EMPTY_REVIEW_RECORDS` `:172-172`→`:183-183`; the refused-result row `:175-180`→`:186-191` for `refused` and `models/knowledge/review.py:1095-1110`→`:1119-1134` for `KnowledgeReviewResult` (the class is declared at 1119; `1095-1110` held a payload validator); the per-subject projection row `models/lifecycles/review_assessment.py:441-479`→`:542-594` for `assessment_state_for`; the record-owner row `review_evidence_records.py:178-196`→`:171-196` for `review_records_for`; and the damaged-claim case `mcp/tests/test_knowledge_review_evidence_channels.py:719-745`→`:847-870`. Wording, Findings and Anchors all unchanged. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header's stamp values are untouched, and the governed closeout owns the real stamp.
- 2026-09-23T02:40:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **the renderer gains the label, the port and two moved renderers (311 → 473 lines; `ICR-R26@v1`).** The card records `ReviewApplicabilityProjection` as the one-way port, the two class tuples, the filtering every display collection now applies, the `context`/`applicability` fields both panes gained, the two renderers that moved here from the adapter, and the one field `ReviewClaimRecord` gained. The "what moved here, and from where" paragraph now names ten names rather than eight, and the dependencies section records that the module still touches no comparison and no store. **Citation accounting:** the rows this leaf's insertions moved were re-derived from each construct's own extent in the 473-line candidate — the pane renderer `152`→`213-252`, `assessment_displays`/`_assessment_display` `200-234`→`277-302`/`305-322`, the `__all__` row, `_evidence_link` `236-274`→`325-368`, the two compositions' call sites (`knowledge_review.py` `321`/`905`→`327-500`/`926-978`), `ReviewClaimRecord` `61-82`→`74-100`, and `review_evidence_records._claim_record` `104`/`569`→`548-572`/`575-598`. Wording was retained where the claim still states what the code does. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header already names this leaf's base, and the governed closeout owns the real stamp.
