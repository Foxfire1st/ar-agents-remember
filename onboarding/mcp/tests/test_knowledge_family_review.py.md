# mcp/tests/test_knowledge_family_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_family_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:31+02:00 |
| lastVerifiedCommitHash |  `9f88a6de572dc15bbed1802cf08b77c1193fb24c`|
| lastVerifiedCommitDate |  2026-09-18T14:21:49+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l16` uncommitted staged source; base `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The 17 `unit-regression` cases that pin the pipeline `KS-R16@v1` places between the record leaves —
§2's fact groups, §4's separated statuses and per-input currentness, §5's routing and the one recorded
decision.** What the module owns is that composition in use: which signals merge into one group and what
a merge must retain, which status each of the five owners may report and what each says it does not
establish, what one moved input does to a stored binding, which existing surface a finding routes into
and which counts it may move, and what the recorded gate-consequence decision does and does not create.
It owns neither neighbour. Its inputs are built by hand through `KS-R14@v1`'s and `KS-R15@v1`'s declared
shapes rather than by running the detector or the curator, and no case opens a store, writes a file, or
constructs a process, a publication or a Git object.

## Code Commentary

### Logic

The module is a handful of small helpers, three named builders, and then three groups of cases in clause
order, with a section comment above each group. The builders exist so that no case has to hand-write a
neighbouring leaf's record:
`signal(claims=…, condition=CONCERNING)` returns a valid facts-only `DetectionSignalPayload` over the
shared family revision, carrying `NO_SEMANTIC_ASSESSMENT_LIMITATION` and a complete-for-declared-policy
scope status; `assessment(…)` returns a stored `ReviewAssessment` through the authored/revision shapes,
with a six-entry evidence-dependency declaration that names this leaf's own task intent among its
inputs; and `current_measurement(record)` returns a measurement of the world in which exactly one named
input has moved. **That last builder's digest is deliberately a value no recorded edge carries**, which
is what makes the "one input moved" case a genuine move rather than a re-statement of the recorded
binding — a comparison fed the recorded values back would report `current` and prove nothing.

**§2's cases separate the merge from the assurance.** The grouping case asserts that two signals
recorded against the same subject and the same declared input set become one group, whose subject is the
shared family revision in the `family:…` spelling and which carries the grouping rule's own declared
version. The retention case goes further than a count: two contributing claims arrive as one group and
both conditions, both supporting paths and all six supporting edges remain, and `retains(…)` answers
true for the matches that contributed. Its twin asserts the same method answers **false** for a match the
group never had, so "grouping must retain every matched condition and its supporting paths and edges" is
measured rather than assured. A family-conditioned signal whose recorded path is shorter than the
declared three-edge shape is refused by the pipeline as the defect it is — the group is not filed under
a subject guessed from the wrong edge. And the sweep that opens the requirement's mechanical clause runs
`conclusion_bearing_fields` over twelve declared models, nine from the family-review vocabulary and
three from the registered-scope vocabulary, requiring the empty tuple for each and naming the model in
the failure message, so a verdict, severity, explanation or compatibility field is reported whether or
not any payload would populate it.

**Missing stays missing, and the five statuses stay five.** A group whose subject has no stored record
carries no review record ids, the curator's own status answers `no-record-recorded`, the subject's
projection answers `none-recorded` rather than a disposition nobody authored, and the word
`no_concern_found` appears nowhere in the group's serialization. The status case accepts a complete
five-owner report only when the owners are exactly `PIPELINE_STATUS_OWNERS` in order, every entry's
"what this does not establish" sentence is nonblank, every status is a member of its own owner's closed
vocabulary, and the report type itself carries no conclusion-bearing field. Two collapses are refused
beside it: a detector reporting the currentness owner's status is "not one of its declared", and a report
carrying four owners is refused as one that "reported nothing". The two owners whose facts this pipeline
reads are then derived from their records — the detector's status has a declared precedence in which an
incomplete scan and an unresolved declared input outrank a match, and the curator's `unresolved` is a
vocabulary member reported as `declared-unresolved` rather than a gap.

**Currentness is a comparison with two refusals at its edges.** A binding measured against its own
recorded identities is `current` with no moved identities; measure one input at a digest no recorded
edge carries and the same binding is `stale` with exactly one moved identity. The stale record stays
readable, is not reusable (`reuse_permitted is False`), is not reinterpreted for the new inputs
(`reinterpreted_for_new_inputs is False`), and its stored disposition is unchanged — nothing re-judged
the old judgment against inputs it never examined. Only the stale case produces the currentness string
the shipped field carries; an empty sequence answers `None`, because "nothing is stale" is not a status
anybody needed a new field for. A hand-written state is refused in both directions: stale with nothing
moved is a comparison nobody made, and stale with reuse permitted is the reuse the clause forbids.

**§5's cases protect the boundary between a report and a gate.** The report-only section renders a
stored record as a row under the existing heading with one subject and one assessment, and an empty
projection as the explicit `_None recorded._` with zero subjects — absence gets no favourable row. The
routing case asserts `review_row_count == 1` beside `actionable_count == curator_actionable_count(2, 1,
3) == 6`: the shipped function's own value, called rather than restated, so a family-review row cannot
be folded into the count that gates closeout. It also asserts that the report-only property holds and
that the report names the validator which actually decides closeout readiness, and the routing surface
constant is asserted as exactly the two existing names beside a hand-built row naming a third, which is
refused as "a third surface". A report whose actionable count is not the shipped three terms is refused
as one that "gains no fourth" — the case's own zero-row report keeps its row count equal to its rows, so
only the arithmetic check can fire. The last two cases
close the authority question the only way a leaf may: the recorded decision is asserted field by field —
owner role, identity reference and ruling basis, durable home, question, outcome, rationale, revisit
condition, effective-from, and an authority basis equal to its three recorded sources — and its negative
is measured over the code itself: `creates_gate is False`, no declared field name other than
`creates_gate` contains "gate", no status vocabulary holds a closeout-readiness value, and no member of
the shipped refusal-code vocabulary contains `family_review`.

### Conventions

- **One value per fact.** The shared condition is a module constant, the recorded digests are distinct
  from the measured one, and the builder that fabricates a "move" is documented as fabricating a value
  no recorded edge carries — the cases can therefore tell a real move from a tautology.
- **Refusals are matched on the sentence the record itself produces**, through `pytest.raises(…,
  match=…)`, and each refusal is placed beside the acceptance it would otherwise hide — the valid
  five-owner report immediately before the two refused ones, the current binding inside the same
  currentness case as the stale one.
- **The builders are named without a leading underscore** because they are the module's fixture
  vocabulary, and each is documented with the leaf whose declared shape it builds.
- **Hermetic and in-process.** No fixture, no temporary directory, no store and no file: every input is
  constructed from declared pydantic shapes, and the module declares
  `pytestmark = pytest.mark.evidence_unit`, with its docstring naming the `unit-regression` lane.
- **Assertions name the thing they are about.** The conclusion sweep passes the model into its failure
  message, and the retention, currentness and routing cases name the condition, path, binding state or
  count each assertion is about, so a failure inside a case that carries several probes still says which
  probe failed.

### Invariants And Boundaries

- **A group keeps every contributing fact.** Retention is asserted as two conditions, two paths, six
  edges and a true `retains`, and its negative as a false `retains`; the pipeline has no field that
  could hold a dropped match.
- **Nothing in this record group can hold a conclusion.** Twelve declared models are swept, the report
  type is swept again, and the group's serialization is asserted to contain no disposition word.
- **Missing stays missing.** No record means no record ids, `no-record-recorded` for the curator,
  `none-recorded` for the subject, and no row in the report-only section.
- **Currentness follows from the comparison and is never written.** Both hand-written states are refused,
  and a stale binding is fixed as readable, non-reusable and not reinterpreted.
- **Two counts, never one.** The actionable value is the shipped function's own, the family row count is
  reported beside it and folded into nothing, and no case derives either from the other.
- **The gate question is closed by a record that cannot gate.** The decision's fields are asserted
  present and nonblank, and its inability to represent a gate, a refusal code or a readiness value is
  measured over the declared vocabularies.
- **Inputs are built, not produced.** No case runs the detector, opens a store or writes a file, so a
  green run says nothing about either neighbouring leaf's behavior — only about what this pipeline does
  with the records those leaves declare.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring states the clause groups, the lane, and the seven failures every case names — beginning with the merge that silently dropped a contributing match. | "a merge that silently dropped a contributing match" | mcp/tests/test_knowledge_family_review.py:1-13 |
| The module constants pin the shared identifiers and the one condition the shared-family signals carry. | "CONCERNING = "source_changed_on_both_sides_joined_to_same_family"" | mcp/tests/test_knowledge_family_review.py:83-89 |
| The signal builder emits a facts-only payload whose limitations carry the neighbouring leaf's no-semantic-assessment marker. | "limitations = (NO_SEMANTIC_ASSESSMENT_LIMITATION,)" | mcp/tests/test_knowledge_family_review.py:129-171 |
| The assessment builder declares its examined inputs through six recorded dependencies, one of which names this leaf's own task intent. | "dependency("task-intent", "task/260915-KS-L16", digests[0])," | mcp/tests/test_knowledge_family_review.py:174-216 |
| **The measurement builder moves exactly one named input, to a digest no recorded edge carries, so the currentness cases measure a genuine move.** | "measured[first] = (recorded[first][0], digest)" | mcp/tests/test_knowledge_family_review.py:219-233 |
| Two signals over one subject and one declared input set merge into one group carrying the declared grouping version. | `test_signals_about_one_subject_and_one_input_set_merge_into_one_group` | mcp/tests/test_knowledge_family_review.py:240-254 |
| **The merge retains both contributing conditions and their supporting paths and edges — all six edge steps survive grouping.** | "assert len(group.supporting_edges()) == 6" | mcp/tests/test_knowledge_family_review.py:257-283 |
| **The mechanical review is run over twelve declared models, each required to declare no conclusion-bearing field.** | "assert conclusion_bearing_fields(model) == (), model.__name__" | mcp/tests/test_knowledge_family_review.py:300-323 |
| A subject with no stored record answers `no-record-recorded` and `none-recorded`, and its serialization carries no favourable disposition word. | "assert "no_concern_found" not in group.model_dump_json()" | mcp/tests/test_knowledge_family_review.py:326-339 |
| **The five owners are reported separately, in order, each with a non-blank statement of what it does not establish.** | "assert tuple(entry.owner for entry in report.entries) == PIPELINE_STATUS_OWNERS" | mcp/tests/test_knowledge_family_review.py:369-389 |
| **A stale binding stays readable, is not reused and is not reinterpreted for the inputs it never examined.** | "assert stale.reuse_permitted is False" | mcp/tests/test_knowledge_family_review.py:455-471 |
| A currentness whose state contradicts its own moved-identity list is refused, in either direction. | "with pytest.raises(ValidationError, match="follows from the comparison"):" | mcp/tests/test_knowledge_family_review.py:474-494 |
| A stored record renders as one row in the existing report-only section, and an empty projection renders the explicit none-recorded line with zero subjects. | "assert "_None recorded._" in "\n".join(knowledge_review_section(()).lines)" | mcp/tests/test_knowledge_family_review.py:497-515 |
| **The actionable count is the shipped function's own value, asserted beside the separate family-review row count.** | "assert routing.actionable_count == curator_actionable_count(2, 1, 3) == 6" | mcp/tests/test_knowledge_family_review.py:522-541 |
| **The recorded decision adds no gate: no refusal code, and no status vocabulary, mentions this record group.** | "assert not any("family_review" in code for code in get_args(KnowledgeRefusalCode))" | mcp/tests/test_knowledge_family_review.py:598-611 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Its inputs are in-process pydantic records built
from this repository's own declared shapes, and nothing it asserts reaches a second repository, a network,
a store or a Git object.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T14:31+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): created this one-to-one card for the family-review pipeline suite. It records the three in-process builders (a facts-only signal, a stored assessment with six recorded dependencies, and a measurement that moves one input to a digest no recorded edge carries), §2's separation of the merge from the assurance that measures it, the twelve-model sweep for conclusion-bearing fields, the missing-never-favourable facts, the five owners reported separately with their own vocabularies and limits, per-input currentness with both of its refusals, the report-only section and the two counts that must never become one, and the recorded gate-consequence decision whose inability to create a gate is measured over the shipped vocabularies. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
