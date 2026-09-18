# mcp/src/agents_remember/memory_quality/family_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/family_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:26+02:00 |
| lastVerifiedCommitHash |  `9f88a6de572dc15bbed1802cf08b77c1193fb24c`|
| lastVerifiedCommitDate |  2026-09-18T14:21:49+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l16` uncommitted staged source; base `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| governingOverview | `mcp/src/agents_remember/memory_quality/overview.md` |

## Governing Overview

[memory quality overview](overview.md)

## Purpose

The four acts that compose `KS-R16@v1`'s family-integrity pipeline: grouping a recorded detection run's
signals into fact groups, reporting the five status owners separately, comparing each stored authored
record's binding against the caller's measurement of the world, and routing the groups into the curator
worklist that already exists. **It supplies the seam and nothing else.** Every record it returns is
declared in `models/knowledge/family_review.py`, every comparison it makes belongs to `KS-R14@v1`'s
detector or `KS-R15@v1`'s authored record, and the one count it reports is produced by the shipped
formula in `curator_checklist.py`. It opens no store, reads no file, mutates nothing, and defines no
second detector, no second assessment collection, no second worklist and no second counter.

## Code Commentary

### Logic

**Grouping is a derivation from recorded facts, and every way of not having them is a refusal.**
`group_detection_facts(signals)` keys each signal by `_group_key` — the recorded subject and the declared
input signature — collects the signals under that key, and returns one `FamilyIntegrityFactGroup` per key
in sorted key order. `_subject_of` reads recorded facts only: for the two `FAMILY_CONDITIONS` it takes the
first edge of every recorded path through `_first_edges(required_edges=_FAMILY_PATH_EDGE_COUNT)`, whose
three-edge shape is checked because a shorter path would make the first edge something other than a family
revision, and spells the subject `family:{'+'.join(families)}`; every other signal is classified by
`_subject_kind` from its recorded change granularities — `family_statement_changed` is a family, the five
invariant-revision granularities are an invariant revision — and spelled `{kind}:{'+'.join(reached)}`,
which is `KS-R15@v1`'s own `assessment_subject_id` spelling, so a routing row addresses a subject the
existing collection can already hold a record for. A signal whose granularities place it under no kind
raises, naming the signal and its condition, rather than routing to a subject nobody recorded.
`_input_signature` renders the declared set and each side's context digest as `{declared}[{side=digest|…}]`
in sorted order. `_group_of` builds the record from `fact_group_identity` and
`FACT_GROUPING_POLICY_VERSION`, and `_match_of` projects each signal into a `FactMatch` that keeps every
supporting path, every supporting item id and one `FactSupportingEdge` per edge of every recorded path
(`edge_kind` = `{condition}/step-{index}`) — grouping merges, and nothing is dropped on the way.

**The five owners are composed from their own declarations, so a caller supplies a status member and never
a limit.** `compose_status_report(observed)` refuses an owner outside `PIPELINE_STATUS_OWNERS` ("a sixth
owner is a second reporting surface") and refuses an owner that reported nothing ("a missing owner is a
collapse, not an absent row"), then builds each `PipelineStatusEntry` with the `establishes` and
`does_not_establish` sentences taken from `STATUS_OWNER_DECLARATIONS` rather than from the caller.
`detector_status` declares its precedence in code order: a caller-reported `incomplete_scan` outranks a
caller-reported `unresolved_inputs`, which outranks a signal whose recorded `registered_scope_status` is
`incomplete_scan`, which outranks a signal recording an `unread_declared_input` or `unsupported_locator`
limitation; absent all of those, a non-empty signal set is `matched` and an empty one is
`no-match-under-declared-policy`. The status says nothing about whether a behavioral conflict exists, and
the owner's declaration repeats that limit. `curator_review_status` maps the stored dispositions to
`no-record-recorded` for none, `declared-unresolved` for an `unresolved` member and `record-recorded`
otherwise, so a curator who could not conclude is a vocabulary member rather than a gap.

**Currentness is measured by the shipped comparison and reported with the two facts the pipeline owes.**
`compose_currentness(assessments, current)` calls `KS-R15@v1`'s own `assessment_currentness` per record
with `current.get(assessmentId, {})` as the measurement — a recorded identity with no current value is a
mismatch rather than a pass — and builds a `FindingCurrentness` carrying `assessment_subject_id(assessment)`,
the record identity, the measured `binding_state` and the measured gaps' identities as `moved_identities`.
`curator_currentness_status(bindings)` is the only currentness string this leaf produces and it targets the
field the curator-coherence response already declares: `None` when nothing is stale, otherwise
`stale: N recorded review(s) no longer match their examined inputs (subjects)` over the sorted stale
subjects, with no second currentness surface.

**The routing report consumes the shipped formula instead of restating it, and the family rows move
nothing.** `route_family_review(groups, …)` builds one `FamilyReviewRoutingRow` per group, addressed by the
group's own `subject_id` — `_subject_id_of` returns the field rather than manufacturing an identity at the
routing boundary — carrying the group's match count and the stored record identities recorded for that
subject; the report names `report_only_section=KNOWLEDGE_REVIEW_HEADING`, counts the rows it carries, and
computes `actionable_count` by calling the imported `curator_actionable_count(repair, missing, stale)`, the
same three-term function the checklist's own writer calls. `family_review_summaries(assessments, current)`
groups the stored records by subject, asks `KS-R15@v1`'s `subject_state` for each subject's state, and
builds the `AssessmentSummaryInput`/`summarise_assessment_state` row: a subject with no stored record
produces **no row at all**, so it is never rendered as a disposition. `reported_subject_status` returns one
subject's `SubjectAssessmentStatus` through the same projection — `none-recorded`, `unresolved`, `stale` or
`current`, with no "compatible" member and no default — and it is defined and exercised by this leaf's tests
but is not named in the module's `__all__`.

### Conventions

Pure functions over caller-supplied inputs: the caller supplies the signals, the stored records and the
current measurement, and this module opens no store, reads no path's bytes and holds no state. Reuse is
preferred to restatement — the three-term actionability formula is imported from `curator_checklist`, the
assessment projections (`assessment_subject_id`, `assessment_currentness`, `subject_state`) from the
lifecycles modules, the section heading from `knowledge_review`, and the vocabulary constants and record
shapes from `models/knowledge/family_review.py` — so no copy of any of them is held here. Refusals are
`ValueError`s raised exactly where the recorded fact is missing or wrong, each naming the signal or the
owner and what would satisfy it, which is the pattern the shipped detector already uses. Every collection
that becomes output is ordered deterministically (sorted group keys, sorted subjects, sorted signature
parts, sorted stale subjects), so identical inputs produce identical output. The module docstring names the
four acts and the one failure each exists to prevent, so a reader meets the pipeline's order before its
functions.

### Invariants And Boundaries

- **The module never forms a conclusion.** Nothing here reads a rationale, a path's bytes, a label or a
  count to decide whether a change matters; a subject nobody reviewed answers `no-record-recorded` or
  `none-recorded`, and it is not rendered as a row or a clearance.
- **A subject comes only from recorded facts, and a fact that cannot place one is refused.** `_first_edges`
  refuses a path shorter than the declared shape and `_subject_kind` refuses a signal whose granularities
  classify nothing; both name the signal, and neither guesses a subject the collection cannot hold.
- **The five statuses are composed, never defaulted.** A sixth owner and a missing owner are both refusals,
  and both sentences of every entry come from the declaration table, so a caller cannot report a status
  without its limit.
- **The actionability formula has one definition.** `route_family_review` calls the imported
  `curator_actionable_count`; the family-review row count travels beside it and is folded into nothing, and
  `report_only_section` is the shipped `knowledgeReview` heading.
- **Currentness is the shipped comparison's result, reported verbatim.** `compose_currentness` supplies an
  empty mapping for a record the caller did not measure and reports the measured state and gaps;
  `curator_currentness_status` is the one currentness string, and an empty sequence answers `None`.
- **No second worklist, counter or reports directory.** The module routes to the two declared surfaces and
  renders into the existing checklist section; it introduces no new file, no parallel checklist and no
  currentness surface, and the one number it adds — the family-review row count — is reported beside the
  shipped three terms rather than folded into them.
- **The export surface omits one defined function.** `__all__` names nine public names, and
  `reported_subject_status` — defined, documented and exercised by the leaf's tests — is not one of them.
- **The report-only boundary is a property of the returns rather than a promise.**
  `FamilyReviewRouting` carries the family row count separately from the three shipped terms, and
  `curator_actionable_count` accepts only repair, missing and stale counts, so nothing this module returns
  can reach the gate's arithmetic.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The four acts this module owns, one per pipeline stage: grouping, separated statuses, currentness and routing. | `group_detection_facts`; `compose_status_report`; `compose_currentness`; `route_family_review` | mcp/src/agents_remember/memory_quality/family_review.py:92-106; mcp/src/agents_remember/memory_quality/family_review.py:229-262; mcp/src/agents_remember/memory_quality/family_review.py:309-332; mcp/src/agents_remember/memory_quality/family_review.py:353-388 |
| The two family conditions and the declared three-edge path shape their subject derivation requires. | `FAMILY_CONDITIONS`; `_FAMILY_PATH_EDGE_COUNT` | mcp/src/agents_remember/memory_quality/family_review.py:77-83; mcp/src/agents_remember/memory_quality/family_review.py:85-89 |
| The subject derivation from recorded facts only, in `KS-R15@v1`'s own subject spelling. | `_subject_of` | mcp/src/agents_remember/memory_quality/family_review.py:116-140 |
| The subject-kind classification over recorded change granularities, and the refusal of a signal that fits no kind. | `_subject_kind` | mcp/src/agents_remember/memory_quality/family_review.py:143-161 |
| The path-shape check that refuses to guess a subject from a shorter recorded path. | `_first_edges` | mcp/src/agents_remember/memory_quality/family_review.py:164-177 |
| The input signature rendered from the declared set and each side's context digest. | `_input_signature` | mcp/src/agents_remember/memory_quality/family_review.py:180-186 |
| One group per key, carrying the declared grouping policy version and the shared group identity. | `_group_of`; "group_id=fact_group_identity(subject_id, _input_signature(signals[0])),"; "grouping_policy_version=FACT_GROUPING_POLICY_VERSION," | mcp/src/agents_remember/memory_quality/family_review.py:189-201 |
| The match projection that keeps every supporting path, item id and edge of one signal. | `_match_of` | mcp/src/agents_remember/memory_quality/family_review.py:204-226 |
| The five-owner composition: a sixth owner and a missing owner are both refused, and both sentences come from the declaration table. | `compose_status_report`; "a sixth owner is a second reporting surface" | mcp/src/agents_remember/memory_quality/family_review.py:229-262 |
| The detector's declared precedence and the two recorded limitations that make an input unresolved. | `detector_status`; `registered_scope_status` | mcp/src/agents_remember/memory_quality/family_review.py:265-291 |
| The curator's status vocabulary, with `no-record-recorded` as the answer for an empty collection. | `curator_review_status`; "no-record-recorded" | mcp/src/agents_remember/memory_quality/family_review.py:294-306 |
| Currentness measured through `KS-R15@v1`'s own comparison rather than a locally restated one. | `compose_currentness`; "measured = assessment_currentness(assessment, current.get(assessment.assessmentId, {}))" | mcp/src/agents_remember/memory_quality/family_review.py:309-332; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:142-161 |
| The one currentness string, targeting the field the curator-coherence response already declares. | `curator_currentness_status` | mcp/src/agents_remember/memory_quality/family_review.py:335-350 |
| The routing report: one row per group addressed by the group's own subject id, the report-only heading, and the shipped formula consumed rather than restated. | `route_family_review`; `_subject_id_of`; `curator_actionable_count`; `KNOWLEDGE_REVIEW_HEADING` | mcp/src/agents_remember/memory_quality/family_review.py:353-388; mcp/src/agents_remember/memory_quality/family_review.py:391-399; mcp/src/agents_remember/memory_quality/curator_checklist.py:100-110; mcp/src/agents_remember/memory_quality/knowledge_review.py:31-31 |
| The report-only section's rows, built from the shipped state projection and summary builder, with no row for a subject nobody recorded. | `family_review_summaries`; "def summarise_assessment_state(measured: AssessmentSummaryInput) -> AssessmentSummary:" | mcp/src/agents_remember/memory_quality/family_review.py:402-434; mcp/src/agents_remember/memory_quality/knowledge_review.py:153-173 |
| The subject-state reader defined here, exercised by this leaf's tests and absent from the module's declared export list. | `reported_subject_status`; `__all__`; `subject_state` | mcp/src/agents_remember/memory_quality/family_review.py:437-452; mcp/src/agents_remember/memory_quality/family_review.py:65-75; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:190-211 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The pipeline's inputs are one namespace's
recorded detection run and stored assessments, and every identity it reports is a store-local reference.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T14:26+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): created this one-to-one card for the family-integrity pipeline's composing module. It records that every subject is derived from recorded facts and that a fact unable to place one is refused rather than guessed, that the five status owners are composed with both sentences taken from the declaration table so a caller supplies only a status member, that currentness is `KS-R15@v1`'s own comparison result and yields exactly one string for the shipped field, and that the routing report consumes the shipped three-term `curator_actionable_count` — the helper this leaf added to `curator_checklist.py` — and folds the family-review row count into nothing. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
