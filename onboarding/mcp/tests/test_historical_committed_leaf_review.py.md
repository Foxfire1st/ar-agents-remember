# mcp/tests/test_historical_committed_leaf_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_historical_committed_leaf_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T04:31:57+02:00 |
| lastVerifiedCommitHash | `c422dc00273d4ae7a5d8c9c8db97365b8c85d640` |
| lastVerifiedCommitDate | 2026-09-23T05:16:40+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The cases that measure `ICR-R12@v1`'s produced behaviour through the real production composition**
— a real enclosure, a real linked worktree, the real capture and resolution owners, the real comparison,
R11's real freeze and the real HTTP route — rather than through a preconstructed payload. The packet's
own verification requirement is what shapes the module: "Compare a live frozen leaf and its
closed/cleaned/restarted view byte-for-byte; advance the branch and prove no contamination", and "tests
that merely mirror implementation or assert returned prebuilt payloads are insufficient for production
composition claims". Every assertion here therefore reads **served bytes** or an owner's own value, never
a value this module assembled.

The module carries the intake defect as its subject: a cleaned leaf's Intent Review answered
`candidate_not_live` because the history route required `contract.code_worktree.exists()`. Eight cases
measure the eight properties that replace it, one each:

- a leaf frozen while it was live, its worktree group removed exactly as cleanup removes it, serves
  **byte for byte the same** recorded comparison — the served bytes are compared, not a summary of them;
- a **fresh interpreter** reconstructs the same comparison from the coordination root and the record
  alone, so "reopen after a process restart" is measured rather than simulated;
- a **later task** landing on the repository and on the leaf's protected branch changes neither the
  bytes nor the provenance of the recorded comparison, and its content never enters the inventory;
- a **pre-feature leaf** — source history, no intent generation ever recorded — exposes its recorded
  source range and states that absence explicitly, as a typed absence and not as missing content;
- a generation that recorded **no intent half at all** states that absence as its own fact on the pane
  and on both refusals, and never as a channel that does not resolve (this leaf's F1 fix);
- a **recorded range the repository cannot resolve** answers `candidate_unresolved` with the restore
  action rather than the intake defect's `candidate_not_live` (this leaf's F2 fix);
- expected content that no longer resolves is reported unavailable on the channel it affects, with the
  record's own deletion statement, and nothing falls back to the current tip or to today's knowledge;
- a closed leaf that recorded **neither** a comparison nor a landed commit is still refused by name,
  which is the one state in which `candidate_not_live` is the honest answer.

## Code Commentary

### Logic

**The fixture is the existing R01 enclosure fixture, extended rather than duplicated.**
`closed_fixture` calls `build_endpoint_fixture` (imported from
`test_knowledge_review_source_endpoints`), so the two real snapshots, the two real committed trees and
the real linked worktree every case drives are the ones the source-endpoint cases already own; a case
that needs a closed leaf removes the worktree group itself. `_freeze` publishes a real comparison
through `freeze_review_comparison` (R11's owner), `_composition` reads the owner's own payload through
`read_knowledge_review` with `review_records_for`, and `_serve` drives the production collaborators
through `register_review_routes` and `TestClient` — so the entry route, the subject route, the expansion
route and the refusals are measured over HTTP with the real status and the real body.

**The restart leg is a child interpreter, not a second client.** `_served_in_a_new_process` writes a
descriptor of the four configuration roots, the route and the params, then runs `_CHILD_SERVE` in a
child `sys.executable` with only `mcp/src` on `PYTHONPATH`; the child builds the app from the
coordination root alone, calls the production port and writes its status and bytes out for the parent to
compare. Nothing is shared with the parent beyond the coordination root, which is what makes "a fresh
process reconstructs the same comparison" a measurement rather than a claim about the same object graph.

**The later-task leg lands real history and then measures contamination rather than assuming it.**
`_land_a_later_task` writes a path the leaf never touched, commits it, and moves the leaf's
**protected source branch** to the new commit — the exact event that could contaminate a review reading
a branch tip. The case then compares the served bytes with the frozen read and asserts the later task's
path is absent from the inventory, the comparison binding is unchanged and the declared limitations are
stable. `_object_present` is the supporting measurement that a reclaimed object really is gone, so the
unavailable-channel case deletes objects through R11's own reclamation owner
(`release_comparison_code_object`) rather than by touching files behind it.

**The two fix-round cases assert the sentence, not only the token.** The typed-absence case freezes a
task with **no datasets at all** through R11's `freeze_review_comparison`, asserts the manifest records
`{before: not-selected, after: not-selected}`, and then asserts the wording on the task-context pane, on
the entry route and on the subject route — including that the "does not resolve now" sentence appears in
none of them. The unresolvable-range case records a real landed commit, deletes the work branch, expires
reflogs, removes the worktree group and runs `git gc --prune=now`, asserts the commit no longer resolves,
and then asserts the route answers 404 `candidate_unresolved` with the "cannot be read (unresolvable)"
detail and the restore action. A case that asserted only the machine-readable state would have passed
while the human-readable sentence still told the reader the wrong fact, which is exactly what the fix
round corrected.

### Conventions

`pytestmark = pytest.mark.evidence_unit` places the module in the ordinary unit lane, and
`mcp/tests/test-evidence-lanes.toml` registers it there (a bare TOML key, so it is named as a quoted
anchor rather than as an identifier). `mcp/tests/evidence-lifecycle.toml` derives its three
`consumer_scope = "exact"` consumer rows from the census's own finding — the two snapshot/tree fixtures
and the read-scope fixture the R01 enclosure is built over — and no artifact, no contract and no
artifact identity is added: the population stays at **sixteen contracts / sixty-six artifacts**, and
`mcp/tests/test_dependency_ownership_ast_helpers.py` re-pins the catalog to
`4ab067e360c7807c3051ad71058c09058225f1e9155e7111da6e95c73cac0258` (the Twenty-third deliberate
re-pin). Helper names are private and single-purpose, the child source is one module-level constant so
the child and the parent cannot drift, and no case constructs a record, a manifest or a resolution by
hand.

### Invariants And Boundaries

- **Only served bytes and owner-produced values are asserted.** No case builds the payload it then
  checks, and the byte comparisons read the response body.
- **The enclosure is one per case.** `closed_fixture` builds a fresh fixture under the case's own
  `tmp_path`, so no case observes another's worktree, record or removed worktree group.
- **History is landed, not simulated.** A later task is a real commit that really moves the protected
  source branch, and a reclaimed object is really gone before the unavailable-channel case asserts.
- **A fresh process is a fresh interpreter.** The restart leg shares no state with the parent, so the
  record-only resolution is measured rather than re-entered.
- **No case re-derives what an owner owns.** Freezing, retaining, reclaiming and reopening all go
  through R11's owners; the cases observe, they do not reimplement.
- **Browser acceptance is not claimed here.** The packet's real-browser boundary belongs to
  `ICR-R25@v1`, and the mounted-surface cases for this leaf live in the dashboard's own module.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and cases,
the R01 enclosure fixture it extends, the R11 owners it drives for freezing and reclaiming, and the two
registration files that admit it to a lane and derive its consumer rows. Three details a reader should
carry: the module is **evidence_unit** and its lane row is what the collection gate reads before the
module may run at all; the three consumer rows are `exact`-scoped, so a fourth fixture dependency would
have to be registered rather than inferred; and the later-task and reclaimed-object legs mutate real Git
state inside the case's own fixture repository, never the source checkout.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the defect it measures, the six load-bearing properties, and that every case reads the production composition rather than a prebuilt payload.** | "candidate_not_live" | mcp/tests/test_historical_committed_leaf_review.py:1-27 |
| The route every case drives, and the lane the module belongs to. | `REVIEW_ROUTE`; `pytestmark` | mcp/tests/test_historical_committed_leaf_review.py:77-79 |
| **The child that reopens the same comparison in an interpreter sharing no state with the parent.** | `_CHILD_SERVE` | mcp/tests/test_historical_committed_leaf_review.py:90-123 |
| **The R01 enclosure fixture this module extends, one fresh enclosure per case.** | `closed_fixture`; `build_endpoint_fixture`; `EndpointFixture` | mcp/tests/test_historical_committed_leaf_review.py:126-130; mcp/tests/test_knowledge_review_source_endpoints.py:215-247; mcp/tests/test_knowledge_review_source_endpoints.py:121-205 |
| **The production composition the cases read through: the real route, the real collaborators, the real record loader.** | `_serve`; `_subject_params`; `_entry_params`; `_body` | mcp/tests/test_historical_committed_leaf_review.py:133-172 |
| **The two owners the fixture drives: freezing a real comparison and reading the owner's own payload.** | `_freeze`; `_composition`; `freeze_review_comparison` | mcp/tests/test_historical_committed_leaf_review.py:175-188; mcp/src/agents_remember/application/review_comparison_freeze.py:232-276 |
| **The restart leg: a descriptor of the four roots alone, a child interpreter, and the served bytes written out for the parent to compare.** | `_served_in_a_new_process`; `serving_collaborators`; `register_review_routes` | mcp/tests/test_historical_committed_leaf_review.py:191-227; mcp/src/agents_remember/cli/dashboard.py:67-132; mcp/src/agents_remember/serving/review.py:542-624 |
| **The later-task leg: a real commit on the repository, and the leaf's protected source branch really moved to it.** | `_land_a_later_task`; `LATER_TASK_PATH`; `LATER_TASK_TEXT` | mcp/tests/test_historical_committed_leaf_review.py:230-251; mcp/tests/test_historical_committed_leaf_review.py:84-85 |
| **The byte-for-byte case: the live frozen read and the cleaned read served as bytes and compared.** | `test_a_closed_leaf_serves_its_recorded_comparison_byte_for_byte` | mcp/tests/test_historical_committed_leaf_review.py:257-324 |
| **The restart case: the same bytes from a fresh interpreter that knows only the coordination root.** | `test_a_fresh_process_reconstructs_the_same_recorded_comparison` | mcp/tests/test_historical_committed_leaf_review.py:327-352 |
| **The contamination case: bytes, binding and provenance unchanged after a later task lands, and the later path absent from the inventory.** | `test_a_later_task_does_not_contaminate_the_recorded_comparison` | mcp/tests/test_historical_committed_leaf_review.py:355-384 |
| **The pre-feature case: the recorded source range exposed with the absence of an intent generation stated as a typed absence.** | `test_a_pre_feature_leaf_exposes_its_recorded_source_range_and_its_absence` | mcp/tests/test_historical_committed_leaf_review.py:387-446 |
| **The F1 case: a generation that recorded no intent half states that absence as its own fact on the pane and on both refusals, and never as content that does not resolve.** | `test_a_generation_that_recorded_no_intent_half_states_that_absence_as_its_own_fact` | mcp/tests/test_historical_committed_leaf_review.py:449-499 |
| **The F2 case: a recorded range the repository cannot resolve is `candidate_unresolved`, not the intake defect's code.** | `test_a_recorded_range_the_repository_cannot_resolve_is_unresolved_not_not_live` | mcp/tests/test_historical_committed_leaf_review.py:502-529 |
| **The supporting measurement that a reclaimed object really is gone, so the unavailable-channel case deletes through R11's own reclamation owner rather than behind it.** | `_object_present`; `discard_comparison_snapshots`; `release_comparison_code_object` | mcp/tests/test_historical_committed_leaf_review.py:532-549; mcp/src/agents_remember/application/review_comparison_reclamation.py:174-210; mcp/src/agents_remember/application/review_comparison_reclamation.py:77-124 |
| **The per-channel failure case: the affected channel unavailable with the record's own deletion statement, and nothing substituted.** | `test_expected_content_that_no_longer_resolves_is_unavailable_not_substituted` | mcp/tests/test_historical_committed_leaf_review.py:552-616 |
| **The one state in which the intake defect's code is still the honest answer.** | `test_a_closed_leaf_with_nothing_recorded_is_refused_by_name` | mcp/tests/test_historical_committed_leaf_review.py:619-637 |
| **The declared history tokens the cases assert, read from the resolution module's own vocabulary.** | `HISTORY_RECORDED_COMPARISON`; `HISTORY_RECORDED_SOURCE_RANGE`; `HISTORY_COMPARISON_PREFIX`; `HISTORY_INTENT_PREFIX`; `HISTORY_SOURCE_PREFIX`; `ClosedLeafReview` | mcp/src/agents_remember/application/review_committed_leaf.py:101-111; mcp/src/agents_remember/application/review_committed_leaf.py:141-182 |
| **The lane row that registers this module, and the three exact-scope consumer rows its cases are derived for.** | "mcp/tests/test_historical_committed_leaf_review.py" | mcp/tests/test-evidence-lanes.toml:77-77; mcp/tests/evidence-lifecycle.toml:729-729; mcp/tests/evidence-lifecycle.toml:1412-1412; mcp/tests/evidence-lifecycle.toml:1445-1445 |
| **The re-pin that keeps the catalog identity of the lifecycle TOML deliberate rather than incidental.** | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |

## Cross-Repo References

No cross-repository behavior is exercised by this module. Its enclosure is one repository's own leaf
worktree with an external memory half, and every case reads that repository's own records.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T05:10:00+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): created this one-to-one card for the case module this leaf introduced (`ICR-R12@v1`). The card records the enclosure every case drives, that each property is measured through the real HTTP composition and the real R11 owners rather than through a constructed payload, the child-interpreter restart leg, the real-history contamination leg, and the two fix-round cases — F1's declared-absence sentence and F2's per-kind refusal — as current behaviour. The lane row and the three `exact`-scope consumer rows the census derived are named, so a reader can see what registers this module and on what evidence. **Stamp accounting:** the verification pair names the production line at this leaf's base — the last real commit the reading was taken against — because every construct this card cites exists only in this leaf's uncommitted candidate; the governed closeout owns the real stamp once the code commit exists.
