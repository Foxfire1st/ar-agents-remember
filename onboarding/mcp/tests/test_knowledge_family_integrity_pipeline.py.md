# mcp/tests/test_knowledge_family_integrity_pipeline.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_family_integrity_pipeline.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:05+02:00 |
| lastVerifiedCommitHash |  `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`|
| lastVerifiedCommitDate |  2026-09-20T02:00:33+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l16` uncommitted staged source; base `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**`KS-R16@v1` §6 and §7 end to end: the worked example, its harmless control, and cleanup survival, as
seven cases that protect the pipeline's whole behaviour rather than one record's shape.** The module is
registered in the `integration` lane (`mcp/tests/test-evidence-lanes.toml:265`, inside the section that
opens at `:192`) and carries `pytestmark = pytest.mark.integration`, because the cases drive a real
two-snapshot comparison over two real databases and two real Git trees, walk it with `KS-R14@v1`'s
detector, and publish real bytes to a real destination.

Every case names the failure it catches, and those four failures are the contract the module states before
its first case: **a detector that emitted a verdict on the harmless control**, **a pipeline whose
end-to-end output does not distinguish the two scenarios once the curator has judged them**, **a retention
claim resting on a path nobody read back**, and **a worklist row discarded while it was the only pointer
to the evidence that interprets it**. The module builds its own inputs rather than reaching for private
helpers of the modules under test: the production walk, the production comparison, the production
detection-run store and the production publication functions all run, and only the fixture's two datasets
and two trees are prepared.

## Code Commentary

### Logic

The seven cases fall into four clause groups, and two of the four contain both an acceptance case and a
refusal case — which is the point of the split, since the same seam has to answer correctly on both sides.

**Group 1, §7.5/§7.6 — the machine side carries no verdict.** `test_the_detector_emits_the_same_signal_kind_for_a_budget_change_and_a_comments_only_change` is an
**acceptance-over-absence** case: it walks the real comparison, requires at least one recorded condition,
and then asserts, field by field on every produced signal, that
`conclusion_bearing_fields(DetectionSignalPayload) == ()` and that the words `severity`,
`semantic_conflict`, `explanation` and `compatible` appear nowhere in the dump, with
`registered_scope_status == "complete_for_declared_policy"`. **It catches the first control failure — a
detector emitting the concerning verdict or a severity on the harmless scenario.** Its companion,
`test_the_pipeline_distinguishes_the_two_curator_conclusions_without_moving_a_count`, is the pair's other
half and the module's sharpest claim: the machine side is asserted *identical* between the two authored
records (`[group.matched_conditions() …] == [… ]`), the curator status is `"record-recorded"` for both a
`concern_found` and a `no_concern_found` disposition, and the two scenarios separate **only** in the
report-only rows, where the rendered section must contain the disposition it was given. Beside those,
`actionable_count` is `0` in both and `report_only_rows()` equals the group count, so no count and no
status owner moved. **It catches the second control failure — a pipeline identical for both scenarios.**

**Group 2, §3.4 — the inconclusive review is a reported state.** `test_an_inconclusive_review_is_a_reported_state_that_moves_nothing` is the
**acceptance case for `unresolved`**, and it is written to catch four forbidden variants at once: nothing
is retried, the signal is not dropped, the absent verdict is not defaulted to a clearance, and the
unresolved state is not presented as an approval. It asserts `curator_review_status((…)) ==
"declared-unresolved"`, `unresolvedCount == 1`, `actionable_count == 0`,
`review_row_count == len(groups) > 0`, `binding_state == "current"`, and that a subject nobody recorded
answers `reported_subject_status(…, {}, …) == "none-recorded"` rather than a favourable default.

**Group 3, §6 — retention is measured, and a row that is the only pointer survives.** This group carries
one acceptance and two refusal cases.
`test_a_finding_and_its_manifest_are_read_back_after_the_enclosure_directory_is_gone` is the **acceptance
case**: it publishes a finding and a manifest, asserts `retention.destination == task_root / "notes" /
"reports"` and that this is *not* the enclosure-local reports directory, then removes the enclosure-shaped
directory and its parent and reads both artifacts back — `readable_together()`, each
`observed_sha256 == publication.sha256`, `matched()`, and `blocked_reason() == ""`.
`test_a_destination_that_did_not_keep_the_bytes_is_reported_and_never_claimed` is its **refusal case**: the
published file is unlinked, the read-back state is `"missing"`, `matched()` is `False`, and the reason
carries the destination — never "published".
`test_a_worklist_row_that_is_the_only_pointer_to_the_evidence_is_not_discarded` is a **pure refusal/acceptance
pair on one predicate**: `worklist_row_disposable(durable_reference_count=0) is False` and
`…=1) is True`, and the case's docstring states the reading it protects — a row that is the sole reference
to a finding or its manifest is not regenerable, so the predicate answers `False` exactly when no durable
reference was counted.

**Group 4, §1 + §2 + §4 + §5 in one operation — the composed seam.** `test_the_one_operation_composes_the_scope_the_run_the_statuses_and_the_routing` is the
module's only case that drives `family_integrity_report`, and it is both acceptance and refusal in one
body. On the acceptance side it opens a real run store, records a real detection run built from a
hand-constructed comparison, declares a two-snapshot scope with real `snapshot_source` handles, and
asserts the composed report: `state == "composed"`, `scope.constructed()`, the run read back with the
same `run_id`, groups present, `tuple(entry.owner for entry in report.statuses.entries) ==
PIPELINE_STATUS_OWNERS` (**the five separation asserted against the owner's own declared tuple rather than
against a restated list**), `binding_state == "current"`, `actionable_count == 0`,
`report_only_rows() == len(report.groups)`, and `"knowledgeReview"` present in the rendered section. On the
refusal side the same request is re-submitted with `owner_reported_statuses` carrying only
`structural-validator`: the second report is `state == "refused"` and the refusal's detail names
`verification-runner`. **The refusal is what makes the composition a pipeline rather than an assembly —
it is the seam proving it will not report another owner's fact for it.**

**Supporting builders, which are load-bearing to the contract rather than incidental.** A module-scoped
`fixture` calls `build_diff_fixture` once, because building two real snapshots and two real Git trees is
the expensive part; `walked_signals`/`walk_comparison` run the shipped comparison and walk it with
`detect_review_conditions`, recording both declared input sides; `authored` builds a real
`ReviewAssessment` with its evidence-dependency declaration and provenance; `composed` is the in-process
assembly the §7 cases use so that *only* the curator conclusion differs between the two scenarios — it
passes `scope=None` deliberately, because those cases are about the report's counts and rows rather than
about scope construction; and `minimal_comparison` hand-builds one union carrying exactly one
family-conditioned condition, with a docstring that states both why (the run's declared order is over
signal identity, so one signal is the smallest input that exercises the record path) and what it is not
(**not a substitute for the real comparison — the §7 case above walks that one**).

### Conventions

Assertions are written so a failure names the thing that broke: the module asserts on the *specific* owner
tuple, disposition, digest, row count and rendered token rather than on a total, and it renders the
report-only section with the shipped `knowledge_review_section` rather than re-implementing the text.
Real boundaries are used wherever a real boundary exists — two databases, two Git trees, a real recorded
run, real bytes on disk — and the one hand-built comparison is labelled as such in its own docstring. The
cases carry no `skipif` and no xfail, and the fixture is module-scoped with a stated reason rather than
for speed.

### Invariants And Boundaries

- **Seven cases, and no case is a shape check.** Every one asserts behaviour a user operation would
  notice: the control cannot differ from the case, the two scenarios must separate after judgment, a
  published artifact must be readable from the destination after the enclosure is gone, a lost artifact
  must be reported as lost, a sole-pointer row must not be discarded, and the composed seam must refuse a
  request that would make it report another owner's fact.
- **The detector's output is asserted closed, not just plausible.** The machine-side case asserts
  `conclusion_bearing_fields(DetectionSignalPayload) == ()` and the absence of four named fields on every
  produced signal, so a future field added to the payload makes this case fail rather than quietly joining
  the vocabulary.
- **Both halves of the §7 comparison are asserted in one case**, and that is deliberate: asserting only
  that the report differs would pass for a pipeline that also moved a count, so the case asserts the
  identical machine side, the identical curator status and the identical actionable count beside the
  differing rendered disposition.
- **The refusal is asserted at the composed seam, not at a helper.** The incomplete-owner request goes
  through `family_integrity_report` itself, so the case protects the public operation's ordering rather
  than a private function's return value.
- **The destination is asserted to be the durable one, and separately asserted not to be the
  enclosure-local one.** The acceptance case names both comparisons, which is what makes "publish
  somewhere that survives cleanup" checkable rather than assumed.
- **Deliberate absence: no case asserts a gate.** The module asserts counts, rows, states and digests, and
  never asserts that a closeout, a merge or a readiness verdict follows from the report — the pipeline has
  no such output to assert.
- **The module states the lane it occupies rather than leaving it to the manifest.** `pytestmark =
  pytest.mark.integration` is on line 94 and the module docstring names the lane in its first paragraph,
  so a reader does not have to reconcile the two registries to know which population runs these cases.
- **The module owns no fixture file.** Its shared support is `diff_scope_test_support.py`, a registered
  governed artifact, so the two-snapshot fixture's definition stays with its owner and this module is a
  declared consumer rather than a second copy.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module docstring: the lane the cases occupy, the real boundaries they drive, and the four failures each case is written to catch.** | "``KS-R16@v1`` §6 and §7 end to end"; "a retention claim resting on a path nobody read back"; "a worklist row discarded while it was" | mcp/tests/test_knowledge_family_integrity_pipeline.py:1-11 |
| The lane marker the module declares on itself, and the production entry points it imports from the module under test. | "pytestmark = pytest.mark.integration"; `worklist_row_disposable` | mcp/tests/test_knowledge_family_integrity_pipeline.py:94-94; mcp/tests/test_knowledge_family_integrity_pipeline.py:18-26 |
| The module-scoped fixture and the three declared constants the cases build their inputs from. | `SELECTOR_POLICY`; "def fixture(" | mcp/tests/test_knowledge_family_integrity_pipeline.py:96-121 |
| **The walk over the real comparison, recording both declared input sides, and the real comparison itself.** | `walked_signals`; "def real_comparison(fixture: DiffFixture) -> Any:"; "def walk_comparison(" | mcp/tests/test_knowledge_family_integrity_pipeline.py:125-181 |
| The two authored-record builders and the in-process assembly the §7 cases compare. | `authored`; `build_evidence_dependencies(`; "examinedInputs=ExaminedInputs(declaration=declaration)"; `composed` | mcp/tests/test_knowledge_family_integrity_pipeline.py:185-251 |
| **The first control case: every produced signal asserted field by field to carry no conclusion-bearing field, with the scope status complete for its declared policy.** | `test_the_detector_emits_the_same_signal_kind_for_a_budget_change_and_a_comments_only_change`; "conclusion_bearing_fields(DetectionSignalPayload) == ()"; "assert produced.registered_scope_status == \"complete_for_declared_policy\"" | mcp/tests/test_knowledge_family_integrity_pipeline.py:258-277 |
| **The second control case: the two scenarios separated only in the curator's own rows, with the identical machine side and no count moved.** | `test_the_pipeline_distinguishes_the_two_curator_conclusions_without_moving_a_count`; "curator_review_status((concerning.disposition,)) == \"record-recorded\"" | mcp/tests/test_knowledge_family_integrity_pipeline.py:280-317 |
| **The inconclusive-review case: `unresolved` reported with its owner, and the four forbidden variants refused together.** | `test_an_inconclusive_review_is_a_reported_state_that_moves_nothing`; "assert curator_review_status((unresolved.disposition,)) == \"declared-unresolved\""; "reported_subject_status((unresolved,), {}, f\"family:{uuid4()}\") == \"none-recorded\"" | mcp/tests/test_knowledge_family_integrity_pipeline.py:320-344 |
| **The retention acceptance case: the durable destination named and distinguished from the enclosure-local one, then both artifacts read back after the enclosure directory is removed.** | `test_a_finding_and_its_manifest_are_read_back_after_the_enclosure_directory_is_gone`; "assert retention.readable_together()"; "assert retention.finding_read_back.observed_sha256 == retention.finding.sha256" | mcp/tests/test_knowledge_family_integrity_pipeline.py:351-390 |
| **The retention refusal case: a destination that lost the bytes reports them lost instead of claiming publication.** | `test_a_destination_that_did_not_keep_the_bytes_is_reported_and_never_claimed`; "observed.state == \"missing\""; "assert str(retention.destination) in observed.blocked_reason()" | mcp/tests/test_knowledge_family_integrity_pipeline.py:393-415 |
| The one-predicate case: a row that is the sole durable pointer is not disposable, and a counted reference is. | `test_a_worklist_row_that_is_the_only_pointer_to_the_evidence_is_not_discarded`; "worklist_row_disposable(durable_reference_count=1) is True" | mcp/tests/test_knowledge_family_integrity_pipeline.py:418-427 |
| The hand-built one-signal comparison, and its own statement that it does not substitute for the real one. | `minimal_comparison`; "It is *not* a substitute for the real" | mcp/tests/test_knowledge_family_integrity_pipeline.py:430-496 |
| **The composed seam, acceptance and refusal in one case: the five separated owners asserted against the declared tuple, and the request that omits one refused by name.** | `test_the_one_operation_composes_the_scope_the_run_the_statuses_and_the_routing`; "assert tuple(entry.owner for entry in report.statuses.entries) == PIPELINE_STATUS_OWNERS"; "assert incomplete.state == \"refused\""; "assert \"verification-runner\" in incomplete.refusal.detail" | mcp/tests/test_knowledge_family_integrity_pipeline.py:547-678 |
| The declared owner tuple the composed case compares against, defined by the model owner rather than restated here. | `PIPELINE_STATUS_OWNERS` | mcp/src/agents_remember/models/knowledge/family_review.py:95-106 |
| The shared fixture this module consumes instead of owning, and the artifact row that declares the module a consumer of it. | "def build_diff_fixture"; "kind = \"shared-support\""; "\"mcp/tests/test_knowledge_family_integrity_pipeline.py\"," | mcp/tests/diff_scope_test_support.py:189-196; mcp/tests/evidence-lifecycle.toml:1382-1402; mcp/tests/evidence-lifecycle.toml:1400-1400; mcp/tests/diff_scope_test_support.py:111-111; mcp/tests/evidence-lifecycle.toml:1392-1397; mcp/tests/evidence-lifecycle.toml:1376-1376 |
| The lane row that selects this module into the integration population. | "\"mcp/tests/test_knowledge_family_integrity_pipeline.py\"" | mcp/tests/test-evidence-lanes.toml:282-282 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every boundary the cases drive — two knowledge
databases, two Git trees, a recorded detection run and a durable evidence destination — is created inside
one temporary directory for the case that needs it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T02:05:20+00:00: Generated citation repair: "\"mcp/tests/test_knowledge_family_integrity_pipeline.py\"" repointed to mcp/tests/test-evidence-lanes.toml:282-282. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T01:02:37+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 1 enforced citation row this card carried (citation_anchor_absent_from_range). Hand-read the claim and `mcp/tests/evidence-lifecycle.toml`: the artifact row it is about is the `mcp/tests/diff_scope_test_support.py` block, the one whose consumer list names this module, so the ambiguous `"kind = \"shared-support\""` anchor was given that block's own extent `:1382-1402` (its `kind` line is 1384) and the module's own consumer entry the exact line `:1400-1400`, replacing the two stale cells `:1370-1372` and `:1381-1389` — the first of which sat in the unrelated serving-handoff block. `mcp/tests/diff_scope_test_support.py:189-196`, `:111-111`, `mcp/tests/evidence-lifecycle.toml:1376-1376` and `:1392-1397` are unchanged, as are the claim's wording, its three anchors and the lane-row citation below it. The card's `citation_provenance_invalid` row is not cleared: it is gated on the verification stamp, which this residue pass may not advance. No verification stamp was advanced.
- 2026-09-18T19:54:18+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (one table row, two anchors). The artifact row cited `evidence-lifecycle.toml:1383-1389` for `"kind = \"shared-support\""` — the diff-scope artifact's `owner = …` and later fields, starting two lines below that artifact's own `kind` line at `1381` — and `1392-1392` for the module's own consumer entry, which is at `1397`. Both ranges were widened (`1381-1389`, `1392-1397`) so each anchor sits inside the range that names its construct; the claim, the anchors and the other four ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "\"mcp/tests/test_knowledge_family_integrity_pipeline.py\"" repointed to mcp/tests/test-evidence-lanes.toml:274-274. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "\"mcp/tests/test_knowledge_family_integrity_pipeline.py\"" repointed to mcp/tests/test-evidence-lanes.toml:269-269. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "\"mcp/tests/test_knowledge_family_integrity_pipeline.py\"" repointed to mcp/tests/test-evidence-lanes.toml:268-268. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "\"mcp/tests/test_knowledge_family_integrity_pipeline.py\"" repointed to mcp/tests/test-evidence-lanes.toml:267-267. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:05+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): created this one-to-one card for the family-integrity pipeline contract suite. It records the module's seven cases grouped by the clause they protect (the machine side that carries no verdict, the two scenarios that separate only after judgment, the inconclusive review as a reported state, retention measured by read-back, and the composed seam), which of them are acceptance cases and which are refusal cases, the four failures the module names before its first case, that its lane row sits in the integration section and agrees with its own `pytestmark`, and that its shared two-snapshot fixture is a registered governed artifact it consumes rather than owns. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
