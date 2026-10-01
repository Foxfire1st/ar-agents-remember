# mcp/src/agents_remember/application/review_record_rendering.py

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

- an assessment collection is projected per subject with its currentness **as measured** — the supplied measurement and availability remain the authority; an unmeasured binding is not promoted to current;
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

`ReviewRecordInputs.artifacts` carries immutable owner references for the producer. The renderer transports them with the typed bundle and does not derive, select or validate curator authority from their names. Record availability still travels separately from tuple length, including uncaptured and unavailable history.

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
  `none_recorded`; no measurement ⇒ the binding remains explicitly not measured. None of the three is a
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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and
functions, the review models it builds, the two compositions that call it, the record owner that
supplies the collections, and the adapter that re-exports two of its names. Three details a reader
should carry: the seven original renderers are a **verbatim move** (names de-privatised, bodies
unchanged) from `knowledge_review.py`; the `unmeasured-is-stale` rule and the two absence states came
with them rather than being re-decided here; and since `ICR-R14@v1` the module also carries the
**availability list** and renders each claim from the claim's own recorded fields — the
"one unresolved coverage reference per claim" the earlier table described is now true only of a claim
whose own record was not supplied, because the record owner supplies every claim the candidate holds.

- The module's own statement of what it renders, why it is separate, and the three rules its values obey. [1]
- The published surface: the record input set, the empty value, and the seven renderers. [2]
- **The collections the renderer is given, with the currentness measurement optional and its absence meaning "unmeasured".** [3]
- **The one refused-result builder the whole surface reaches, so a refusal is a state and never a degraded success.** [4]
- **Whether an assessment may be submitted: `disabled_stale` or `unavailable`, and never a private write path — the next action names the existing curator authority.** [5]
- **Pane 3: the evidence links with their unresolved coverage, the observations displayed exactly, and the two absence states computed from the collections themselves.** [6]
- **The per-subject projection that reports an unmeasured assessment `stale` rather than promoting it to current.** [7]
- The assessment display, its per-record projection, and the examined-inputs fallback to the record's own comparison reference. [8]
- **A verification observation displayed exactly, with no sufficiency field and no invented limitation.** [9]
- **A detection fact carried with its inputs, versions and scope limitations only — no voice, no severity, no disposition.** [10]
- **The adapter that re-exports the record input set and its empty value, so the existing importers keep resolving without a new home to learn.** [11]
- The two callers: the subject composition, which renders the matrix rows beside these records. [12]
- **The second caller, which is why this module exists: the task-context composition renders the same records with no matrix and no comparison.** [13]
- The published assessment collection the adapter reads from the curator authority's own publication, with an absent authority treated as empty rather than as an error. [14]
- The published surface: the record input set, the empty value, the claim renderer input and the seven renderers. [15]
- **The collections the renderer is given — including the supplied claims and the availability list — with the currentness measurement optional and its absence meaning "unmeasured".** [16]
- **One claim's own recorded fields as the evidence owner serves them, with the authored limitations verbatim and nothing derived.** [17]
- **Pane 3: the links rendered from each claim's own record, the observations displayed exactly, the two absence states computed from the collections, and the availability list carried onto the pane unchanged.** [18]
- **The one per-claim projection and its two shapes: a supplied claim's own author, lifecycle, limitations and coverage, or an identity whose missing content is named as unresolved.** [19]
- **The record owner that resolves the collections and builds each claim's renderer input, and which the adapter re-exports instead of owning.** [20]
- **The cases that measure the rendered values: unassessed is never defaulted to compatible, a passing observation is never invariant-satisfied, and a detection signal carries no severity.** [21]
- **The rendering a task-context review produces for the same records, measured through the real composition.** [22]
- **The cases that measure the two new claim-link shapes: an authored claim rendering its own limitations and coverage, and a damaged claim's identity kept with its content named unresolved.** [23]

The following declarations carry the changed boundary.

- Owner artifacts accompany the record collections without becoming a second store. [24]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It transforms record values supplied by other
owners into this surface's display values and touches no boundary.

No meaningful cross-repo references found.

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
