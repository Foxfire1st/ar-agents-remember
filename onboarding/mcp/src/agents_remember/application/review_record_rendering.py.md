# mcp/src/agents_remember/application/review_record_rendering.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_record_rendering.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T14:59:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l2`, uncommitted; base `702714fc05363cb28eacaf101ba8384475a6aa56` |
| lastVerifiedCommitHash | `945ddad6a9c90fbf5d7eef7546b9e69714c6c4fc` |
| lastVerifiedCommitDate | 2026-09-21T18:46:40+02:00|
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
shape.** `assessments`, an optional `current` mapping, `signals` and `observations`. `current` is
`None` by default and that default is the honest one: the surface has no measurement of its own to
supply, so every assessment it displays is reported as the shipped projection reports an unmeasured
one. `EMPTY_REVIEW_RECORDS` is the single module-level empty value — a call in an argument default
would rebuild it on every call, and the collections it holds are immutable tuples.

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
exists and `unassessed` otherwise. Each evidence-claim row becomes a `ReviewEvidenceLink` carrying the
row's own assessment references plus one unresolved-coverage reference, because the matrix publishes a
claim's identity, lifecycle and assessment references and publishes **no** coverage or limitations for
it. `source_inspection_available=True` is carried here as it was before the move (F10's recorded
finding: the constant is the surface's own statement, and R03/R10 own any change to it).

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

`__all__` publishes the nine names the two compositions and the adapter consume: `EMPTY_REVIEW_RECORDS`,
`ReviewRecordInputs`, `assessment_displays`, `evidence_pane`, `observation`, `refused`, `signal`,
`subject_states` and `submission`. Every value returned is a shipped type from
`models/knowledge/review.py`, `models/knowledge/detection.py`,
`models/knowledge/evidence.py` or `models/knowledge/view.py`; this module declares no model of its
own. Names are public where two callers use them and private (`_assessment_display`) where one does.
The module holds no state and writes nothing.

### Invariants And Boundaries

- **The renderer renders what it is given.** No function here resolves a reference, selects a record,
  ranks a subject or decides an outcome; the collections belong to other owners' read paths.
- **An absence is never a favourable default.** No assessments ⇒ `unassessed`; no evidence ⇒
  `none_recorded`; no `current` measurement ⇒ every assessment `stale`. None of the three is a
  clearance.
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
functions, the review models it builds, the two compositions that call it, and the adapter that
re-exports two of its names. Three details a reader should carry: this is a **verbatim move** (names
de-privatised, bodies unchanged) of seven helpers that used to live in `knowledge_review.py`; the
`unmeasured-is-stale` rule and the two absence states came with it rather than being re-decided here;
and the task-context composition is the second caller, which is the reason the module is separate at
all.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it renders, why it is separate, and the three rules its values obey. | `unassessed`; `none_recorded` | mcp/src/agents_remember/application/review_record_rendering.py:1-18 |
| The published surface: the record input set, the empty value, and the seven renderers. | `__all__` | mcp/src/agents_remember/application/review_record_rendering.py:46-56 |
| **The collections the renderer is given, with the currentness measurement optional and its absence meaning "unmeasured".** | `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/review_record_rendering.py:59-77 |
| **The one refused-result builder the whole surface reaches, so a refusal is a state and never a degraded success.** | `refused`; `KnowledgeReviewResult` | mcp/src/agents_remember/application/review_record_rendering.py:80-85; mcp/src/agents_remember/models/knowledge/review.py:790-805 |
| **Whether an assessment may be submitted: `disabled_stale` or `unavailable`, and never a private write path — the next action names the existing curator authority.** | `submission`; `PROPOSED_ASSESSMENT_DISPOSITIONS` | mcp/src/agents_remember/application/review_record_rendering.py:88-115; mcp/src/agents_remember/models/knowledge/review.py:92-96 |
| **Pane 3: the evidence links with their unresolved coverage, the observations displayed exactly, and the two absence states computed from the collections themselves.** | `evidence_pane`; `ReviewEvidenceLink`; `ReviewEvidencePane` | mcp/src/agents_remember/application/review_record_rendering.py:118-154; mcp/src/agents_remember/models/knowledge/review.py:356-366; mcp/src/agents_remember/models/knowledge/review.py:635-663 |
| **The per-subject projection that reports an unmeasured assessment `stale` rather than promoting it to current.** | `subject_states`; `assessment_state_for` | mcp/src/agents_remember/application/review_record_rendering.py:157-176; mcp/src/agents_remember/models/lifecycles/review_assessment.py:441-479 |
| The assessment display, its per-record projection, and the examined-inputs fallback to the record's own comparison reference. | `assessment_displays`; `_assessment_display`; `ReviewAssessmentDisplay` | mcp/src/agents_remember/application/review_record_rendering.py:179-212; mcp/src/agents_remember/models/knowledge/review.py:315-353 |
| **A verification observation displayed exactly, with no sufficiency field and no invented limitation.** | `observation`; `VerificationObservationPayload` | mcp/src/agents_remember/application/review_record_rendering.py:215-233; mcp/src/agents_remember/models/knowledge/evidence.py:1-40 |
| **A detection fact carried with its inputs, versions and scope limitations only — no voice, no severity, no disposition.** | `signal`; `DetectionSignalPayload` | mcp/src/agents_remember/application/review_record_rendering.py:236-250; mcp/src/agents_remember/models/knowledge/detection.py:1-40 |
| **The adapter that re-exports the record input set and its empty value, so the existing importers keep resolving without a new home to learn.** | `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/knowledge_review.py:43-105 |
| The two callers: the subject composition, which renders the matrix rows beside these records. | `compose_review`; `_knowledge_pane` | mcp/src/agents_remember/application/knowledge_review.py:362-437; mcp/src/agents_remember/application/knowledge_review.py:653-686 |
| **The second caller, which is why this module exists: the task-context composition renders the same records with no matrix and no comparison.** | `task_context_review`; `_task_context_pane` | mcp/src/agents_remember/application/review_task_context.py:59-104; mcp/src/agents_remember/application/review_task_context.py:107-129 |
| The published assessment collection the adapter reads from the curator authority's own publication, with an absent authority treated as empty rather than as an error. | `review_records_for`; `load_curator_coherence_authority` | mcp/src/agents_remember/application/knowledge_review.py:850-875; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:255-280 |
| **The cases that measure the rendered values: unassessed is never defaulted to compatible, a passing observation is never invariant-satisfied, and a detection signal carries no severity.** | `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`; `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`; `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity`; `test_the_surface_reports_the_absent_submission_path_instead_of_growing_a_private_one` | mcp/tests/test_knowledge_review_surface.py:525-549; mcp/tests/test_knowledge_review_surface.py:552-567; mcp/tests/test_knowledge_review_surface.py:570-586; mcp/tests/test_knowledge_review_surface.py:614-623 |
| The rendering a task-context review produces for the same records, measured through the real composition. | `test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all` | mcp/tests/test_knowledge_review_source_endpoints.py:674-750 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It transforms record values supplied by other
owners into this surface's display values and touches no boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T16:10+02:00 — orchestrating session, pre-closeout metadata repair on `ar/260921-icr-l2`: the governed closeout refused the memory leg because this card for a module that exists only in this leaf's uncommitted candidate carried no verification stamp in its header metadata (`external-memory closeout requires onboarding verification metadata before memory commit`). The two fields were added naming the **production line this card was read against** — `c755cec6…`, the master line after this leaf's resolved syncs brought in the ICR-L5 and ICR-L19 landings, at that closeout's recorded time `2026-09-21T15:29:12+02:00` — and the candidate row was left as it was. This states what the reading was against, not that the module exists in that commit; the closeout's own metadata refresh re-stamps the card against the code commit this transaction creates. No range, claim or anchor was changed by this repair.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): created this one-to-one card for the module this leaf introduced by extracting the review adapter's **record-rendering** responsibility. The card records what the module is rather than only what moved: the collections it is *given* (`ReviewRecordInputs`, with `current` optional and its absence meaning "unmeasured"), the one refused-result builder, the two-state submission value that names the curator authority instead of growing a write path, pane 3's two absence states computed from the collections themselves, the per-subject projection that reports an unmeasured assessment `stale`, and the two display values (`observation`, `signal`) that carry no sufficiency, severity or disposition field. It also records the move's provenance: seven helpers came from `application/knowledge_review.py` verbatim, with the private names de-privatised because **two** compositions now call them — which is the module's second reason for existing, since one copy is what keeps an unassessed collection reading identically in the subject review and in the task-context review. **Stamp accounting:** this card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**, because every construct it cites exists only in this leaf's uncommitted candidate and no real commit contains the content a stamp would claim to have verified; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the real stamp once the code commit exists.