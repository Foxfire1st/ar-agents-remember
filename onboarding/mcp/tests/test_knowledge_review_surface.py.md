# mcp/tests/test_knowledge_review_surface.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Fifteen current test definitions drive the real review composition over the fixture's two
text-backed snapshot sides and derived indexes. They cover selected knowledge/source rendering,
missing roles, the bounded forbidden-field scan, row-count and comparison parity, staleness,
submission, unresolved references, absent sides, pane types/catalogue properties, and measured-empty
or partial inventories. The distinct pane types are knowledge, source and judgment; signals and
authored-effects collections are expressly absent from the knowledge pane.

Seven assessment/observation/signal/worked-journey tests and their three record-input builders are
removed in L57. The unchanged module header still describes some of that old coverage; its prose is
not evidence that deleted tests run. This card describes assertions, not a new execution result.

The resolution/refusal/transport cases were historically moved to
[test_knowledge_review_resolution_and_route.py](test_knowledge_review_resolution_and_route.py.md).
That module now has eight test declarations: its published-assessment-loader test is also removed.
The shared config/request/resolution/render helpers stay here.

## Code Commentary

### Logic

**The lane declaration is collection input, not an execution receipt.** The module declares
`pytest.mark.evidence_unit`, is selected in unit-regression, and is named by seven exact-scope
lifecycle artifact records. Parsed source registrations, not old line offsets or module counts,
are the current authority. No lane membership proves a test ran.

**`REPOSITORY_LEAF` and `FORBIDDEN_FIELD_NAMES` are the module's two declared vocabularies.**
`REPOSITORY_LEAF = "260915-ks-l22"` names the leaf the resolution reports. `FORBIDDEN_FIELD_NAMES` is a
twenty-member frozenset of the names a generated conclusion would have to be carried in — `summary`,
`narrative`, `explanation`, `meaning`, `severity`, `score`, `confidence`, `ranking`, `rank`,
`recommendation`, `verdict`, `conclusion`, `conflict`, `impact`, `importance`, `approved`, `approval`,
`compatible`, `implied_finding`, `disposition_suggestion` — and the source comment states the scope the
check reads: the whole payload schema, so a field added anywhere under it is measured rather than only
a field added to the top.

**`review_config` names no real root, so only the resolution's own refusals can answer.**
`McpRuntimeConfig` is built with `/nonexistent-workspace`, `/nonexistent-coordination`,
`/nonexistent-config.json` and `/nonexistent-transcripts`. That is what makes the two
candidate-resolution cases (in the resolution-and-route module, which imports this helper) measure the
resolver's behaviour rather than the host's filesystem.

**The `fixture` fixture builds one fresh two-snapshot dataset per case.** `build_diff_fixture(tmp_path
/ "review")` returns a `DiffFixture` from the shipped `diff_scope_test_support`, so no case observes
another's candidate state, and the fixture's two databases and two Git roots are real files rather
than stubs. `resolution_for` then assembles the `ReviewCandidateResolution` **without a contract** —
the fixture's own before/after database paths, Git roots and tree ids — so the case can exercise
`compose_review` without standing up a coordination tree, while the resolution-and-route module's cases exercise
`resolve_review_candidate` against a config that names nothing.

**`render` is the module's one failing-loudly helper.** It calls `compose_review` with the fixture's
resolution and request, asserts `result.state == "review"` with the refusal as the assertion message,
asserts the payload is present, and returns it. Every pane case therefore reads a payload the shipped
composition actually produced, and a composition that starts refusing fails the case rather than
silently skipping it.

**The old record-input builders are removed.** `published_assessment`, `observation` and `signal`
no longer construct a review input bag. `render` calls `compose_review` with resolution and request,
including previous binding on the copied request, and returns only an admitted payload.

**The pane cases assert selected identity, presence, conditions and comparison-owned field changes.**
The knowledge case records the compared before/after revision IDs, requires both statement states
present, checks each side's condition tuple and compares the field-change identity set with the
shipped comparison. It does not assert literal statement-text equality; its title/docstring is not
stronger evidence than that body. The source cases retain the unchanged sibling, removed before-side
locations, unmapped/outside-selection counts, and a report whose roles are None or a permitted value;
the case does not identify an originally missing role or compare emitted roles with recorded roles.

**The schema guard is a bounded name check.** `walk_property_names` recursively collects JSON-schema
property names and the test requires no intersection with the twenty declared forbidden names.
The neighboring case checks the vocabulary's record-kind/table/status declarations. These assertions
do not inspect every free-text value or prove that no imaginable field could carry a conclusion.

**The stores-nothing case compares fixture row counts before and after rendering.** It reads
`read_row_counts` for both derived fixture indexes and requires equality. That is the measured
assertion; it is not instrumentation of every possible filesystem write.

**The selects-nothing case compares the payload's identity and counts value for value against the
shipped comparison.** `test_the_adapter_selects_nothing_because_the_shipped_comparison_is_the_comparison_rendered`
runs the shipped `diff_knowledge_scope` directly and asserts the payload's comparison identity, item
identities and counts are that result's own values, so a future re-derivation inside the adapter fails
the case.

**The retained state cases stay distinct.** Staleness is checked in both directions and the submission
path points to the existing owner rather than a private writer. The surviving state case renders, asserts
that the removed `authored_effects` field is absent and checks recorded-reference truthiness; it supplies
no unpublished-author input and accepts empty unresolved collections. The neighbouring missing-side case
mixes constructor refusals with rendering assertions, so the pair is not a refusal-only account. The
removed unassessed/observation/signal/disagreeing-assessment cases are historical, not current rendering
coverage.

**The pane-type case stays here, under its own section header.** The candidate-resolution and
transport cases moved to the resolution-and-route module (see Purpose).
`test_the_rendered_pane_types_are_the_three_the_design_names` remains, beside the two measured-inventory
cases, and proves the rendered pane types are the three the design names.

**The old worked-review and stale-assessment journey is removed.** Its old account is preserved
below as historical material. Current composition uses the recorded judgment pane instead of those
injected evidence collections; the retained fifteen tests do not measure the former journey.

**`260921-ICR-L2` added a narrowing helper, extended the transport case, and added the two cases the new states are measured by.** `reviewed_selector(fixture)` returns the request's selector while asserting it is not `None`, which is what keeps the pyright rail green now that `ReviewSurfaceRequest.selector` is optional rather than papering over it with an ignore. `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds` was extended to assert the third admitted answer — **omitting both parameters** — beside the existing two. (That case now lives in the resolution-and-route module, and as moved it no longer carries the omission assertion; the selector-less route is measured by the source-endpoints module's task-context case.) The two new cases are: `test_a_knowledge_only_change_leaves_an_openable_review_with_a_measured_empty_inventory` (the declared candidate tree equals the base tree while the two real datasets still differ, so the payload carries `inventory.state="measured"`, `entries=()`, `listed_total=0` and the "measured empty change set" sentence *and* an untouched knowledge comparison — both statements `present`, staleness `current`); and `test_an_inventory_that_could_not_carry_a_name_is_partial_by_construction`, which attempts all three refused shapes (`unrepresentable_paths` beside a complete inventory, beside an unavailable one, and on an otherwise-complete inventory) and asserts the one accepted shape is measured **and** partial.

### Conventions

The module imports `DiffFixture`/`build_diff_fixture`, the real comparison and row-count readers,
`ReviewCandidateResolution`, `compose_review` and the current knowledge/source/judgment types.
It no longer imports `ReviewRecordInputs` or assessment/observation/signal binders. The resolver and
HTTP transport live in the neighboring module. Constructor refusals use `pytest.raises(ValidationError)`;
function-scoped temporary fixtures isolate the cases.

### Invariants And Boundaries

- **No case re-implements what it measures.** The comparison comes from `diff_knowledge_scope`, the
  comparison data from the shipped view operation, and the row counts from `read_row_counts`.
- **No snapshot is faked.** The fixture's two datasets and two Git roots are real files under
  `tmp_path`; no case touches the checkout or the network.
- **A refusal fails the case that expected a payload.** `render` asserts `state == "review"` with the
  refusal as its message, so a composition that starts refusing is loud.
- **The lane registration is a precondition.** An unregistered module makes the lane manifest refuse
  the repository, which the collection hook turns into a collection error.
- **Boundary.** This is a test module. It declares one lane (`evidence_unit`), asserts behaviour and
  owns no production contract.

### Todos

None recorded.

## Historical Coverage Replaced By L57

The following earlier card text is retained verbatim as historical material, not current coverage.
Its citation markers and table rows are inert inside this fence. Canonical curator assessment
authoring is not claimed deleted merely because these reviewer tests/builders were removed.

```markdown
## Purpose

The Intent Reviewer surface's case module: **the three panes, every refusal state, and the worked
review.** It drives the real adapter over the real two-snapshot comparison built by
`diff_scope_test_support`, and reads the shipped L20 review matrix through `compose_review`. Nothing
here re-implements a read, a comparison or a view, fakes a snapshot, or asserts a rendering it did not
read back.

The module docstring names the load-bearing properties, **one case each**:

- the surface **stores nothing** — the two datasets' row counts are identical across a full render,
  and the vocabulary module declares no record kind, no table and no status;
- the surface **selects nothing** — the comparison identity, the item identities and the counts the
  payload publishes are the shipped operation's own, compared value for value;
- the surface has **no field a generated conclusion could occupy**, checked over the whole payload
  schema rather than over one model;
- every refusal state is a rendering: unassessed is unassessed, no evidence reads `none_recorded`
  while source inspection stays available, a passing observation is an observation and never an
  invariant-satisfied status, a signal carries facts and scope limitations and no severity, and a
  stale comparison keeps its previous input and disables submission.

The final group is the worked review of `retrieval-review-design.md` §8's journey: a comparison is
opened, the unchanged sibling and the removed claim are read on their own sides, the unmapped path is
inspected through the expansion, an authored assessment bound to the exact examined inputs is
displayed, and changing only the source is shown to make that assessment stale without making it
unreadable or reusable.

**The pair's resolution, its before-half refusals and the transport are measured next door.**
`260921-ICR-L57` moved those nine cases verbatim into
[`test_knowledge_review_resolution_and_route.py`](test_knowledge_review_resolution_and_route.py.md) when
this module crossed the 1200-line rail (1475 → 1056 lines, 31 → 22 cases). They cover the candidate
resolved from task context, the absent candidate, `260921-ICR-L5`'s three before-half refusals, the two
transport cases, `260921-ICR-L17`'s previous-identity case and the loader case. That module reuses this
module's `REPOSITORY_LEAF`, `review_config`, `resolution_for`, `review_request` and `render`, so those
helpers are shared surface, not private to this file.



**The lane declaration is a precondition, not metadata.** `pytestmark = pytest.mark.evidence_unit`
registers the whole module in the unit population, and the leaf also appended the module to the
`unit-regression` lane in `mcp/tests/test-evidence-lanes.toml:109` and to two `consumers` lists in
`mcp/tests/evidence-lifecycle.toml:1412` and `:1447`. An unregistered `test_*.py` module makes the lane
manifest refuse the repository, so the registration is what lets the module be collected at all.



**`published_assessment` builds one assessment through the shipped binding seam rather than by
constructing a stored row.** It builds a `ReviewAssessmentRevision` whose `subject` names the fixture's
invariant id with its before and after revision ids, whose `evidenceRefs` name a code namespace, and
whose `comparisonRef` and `scopeManifestRef` are the fixture's own recorded references, and then
returns `bind_assessment(authorized=revision, inputs=AssessmentInputs(...))`. `observation(...)` and
`signal(fixture)` do the same for the other two collections, so the evidence pane's three inputs are
all produced by the modules that own them.



**The whole-schema conclusion check walks the payload rather than listing the models.**
`walk_property_names` recurses a JSON schema and collects every property name, and
`test_the_whole_payload_schema_has_no_field_a_generated_conclusion_could_occupy` compares that set
against `FORBIDDEN_FIELD_NAMES`. Its sibling case,
`test_the_surface_defines_no_record_kind_no_table_and_no_status_of_its_own`, asserts the vocabulary
module declares nothing of its own. Together they are why "the surface cannot grow a conclusion by
filling a blank" is measured rather than asserted in prose.



**The stores-nothing case measures the two datasets' row counts across a full render.**
`test_the_surface_stores_nothing_so_deleting_every_rendering_loses_no_canonical_information` reads the
row counts before and after a complete render through the shipped `read_row_counts` and compares them,
so "deleting every rendering loses no canonical information" is a measured property of the datasets
rather than a claim about the code.



**The refusal and state cases are one property each.** An unassessed subject is displayed unassessed
and never defaulted to compatible; no evidence records reads `none_recorded` while source inspection
stays available; a passing observation is displayed as an observation and never as invariant-satisfied;
a detection signal carries its facts and scope limitations and no severity; a stale comparison keeps
its previous input and disables submission; a current comparison cannot be built with submission
disabled for staleness; the surface reports the absent submission path instead of growing a private
one; an item whose author is not published is shown as an unresolved reference; a missing side is its
own state and never an empty string; two disagreeing assessments are both displayed with their authors
and no resolution. The last three read `ValidationError` from the models layer where the prohibition is
a constructor check rather than a rendering choice.



**The worked-review case walks the journey rather than sampling it.**
`test_the_worked_review_journey_renders_every_step_it_walks` drives the sequence the design's §8
describes in one case, and `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate`
closes it: changing only the source makes the assessment stale without making it unreadable or
reusable. The measured-binding case and the two-disagreeing-assessments case sit beside it so the
currentness axis is asserted from both directions.




The module imports the shipped support rather than building its own: `DiffFixture` and
`build_diff_fixture` come from `diff_scope_test_support`, `bind_assessment`/`AssessmentInputs` from
`models/lifecycles/review_assessment_store.py`, the assessment models from
`models/lifecycles/review_assessment.py`, and `compose_review`, `ReviewCandidateResolution` and
`ReviewRecordInputs` from the adapter. Since `260921-ICR-L57` the resolver (`resolve_review_candidate`),
`review_records_for` and the transport (`register_review_routes`, `review_request_from_query`, driven
through `fastapi.testclient.TestClient`) are imported by the resolution-and-route module, not here. `pytest.raises(ValidationError)` is the shape used for
every constructor-enforced prohibition. Fixtures are function-scoped and take `tmp_path`, so no case
shares a dataset with another.



- The three input builders that produce records through the seams that own them rather than by constructing stored rows.

- The state cases: unassessed is unassessed; no evidence records reads `none_recorded` with source inspection still available; a passing observation is never invariant-satisfied; a signal carries no severity.

- The two-disagreeing-assessments case and the measured matching-binding case — the currentness axis from both directions, and the case `260921-ICR-L15` renamed so its name and its input agree.

- **The worked review of the design's §8 journey, and the case that closes it: a stale assessment is never reused.**

| The lane row this module occupies. | "mcp/tests/test_knowledge_review_surface.py" | mcp/tests/test-evidence-lanes.toml:111-113 |

| The two consumer registrations this module's fixtures are recorded under. | "mcp/tests/test_knowledge_review_surface.py" | mcp/tests/evidence-lifecycle.toml:1427-1441; mcp/tests/evidence-lifecycle.toml:1471-1471 |
```

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The operative account below follows current declarations and assertion bodies. The old module
header and historical card quotation do not establish removed case coverage. Registrations select
evidence; source inspection supplies no new execution or acceptance grade.

- **The lane declaration, which is a precondition rather than metadata.** [2]
- The leaf id the resolution reports. [3]
- The config that names no real root, so only the resolution's own refusals can answer. [4]
- The fresh two-snapshot fixture per case, and the resolution assembled without a contract so the composition can be driven without a coordination tree. [5]

- The one request shape, the narrowing helper the optional selector obliged, and the one failing-loudly render helper every pane case goes through. [6]


- The shipped two-snapshot support the whole module is built on, with the independent byte-safe Git observation this leaf's inventory cases compare against. [8]

- **The missing-role display case: reported roles are None or a permitted value.** [10]
- **The selects-nothing case, comparing the payload's identity and counts against the shipped comparison value for value.** [13]

- **The staleness pair, asserted from both directions, plus the absent-submission-path case.** [15]

- The surviving state case renders with its removed-field assertion, and the missing-side case mixes constructor refusals with rendering. [16]



- The module has fifteen current test declarations. Its old header still names removed coverage and is not a current case census; the bounded forbidden-name vocabulary remains declared. [1]
- The knowledge case asserts the compared revision pair, statement presence, side-specific condition tuples and comparison-owned field changes, not literal statement-text equality. The source cases retain sibling/before-side and unmapped/outside-selection counts. [9]
- The recursive schema-name scan excludes the declared forbidden names, and the neighboring vocabulary case checks no record kind/table/status of its own; this is bounded assertion coverage, not a universal free-text conclusion proof. [11]
- The rendering case compares both fixture indexes row-for-row by count before and after composition; it is not a general filesystem-write audit. [12]
- Distinct knowledge/source/judgment pane types, no authored_effects/signals, typed labelled catalogue entries, retry identity present on both sides, a direct retry comparison with a page and one absent identity excluded are asserted. The body does not compare every catalogue identity or open an unanswerable subject to assert its reason. [19]
- A knowledge-only change retains a compared selected pair while its inventory is measured empty; malformed inventory combinations are rejected and unrepresentable names require a partial measured inventory. [20]



> Retained earlier citation wording: - The module is selected once in the unit-regression lane and named by seven exact-scope lifecycle artifact records; registration is not execution.



### Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds its datasets under
`tmp_path` and asserts one repository namespace's rendering.

No meaningful cross-repo references found.

## 260921-ICR-L17 One Case Drives The Previous Identity Through Every Hop

`260921-ICR-L17` (`ICR-R17@v1`) adds **one collected case** — 30 become 31 — and changes the module's
`render` helper so the previous identity is asked for the way a refresh asks for it.

**The helper change records a contract, not a convenience.** `render` used to call `compose_review` with
a `previous_binding_digest` keyword beside the request. That keyword is gone from the adapter: the
identity travels **on** `ReviewSurfaceRequest`, which is where the transport admits it and where the
composition reads it. `render` now copies the request with
`model_copy(update={"previous_binding_digest": previous_binding_digest})` and calls the composition
without a parallel argument, and its docstring says why — "so this helper asks the way a refresh asks
rather than passing a parallel keyword beside the request".

**The new case lives in the resolution-and-route module.** `260921-ICR-L57` moved
`test_the_previous_binding_identity_reaches_the_port_and_is_compared_against_the_read` there verbatim;
its account of the three requests (refresh, plain read, malformed spelling) moved with it. `render`
stays here, and that module imports it.







- The module is selected once in the unit-regression lane and named by seven exact-scope lifecycle artifact records; registration is not execution.

Retired at the fifth freeze d59c3493: mcp/tests/evidence-lifecycle.toml:395-395 - the bytes it recorded now occur 6 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:830-830 - the bytes it recorded now occur 7 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:1215-1215 - the bytes it recorded now occur 9 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2072-2072 - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2753-2753 - the bytes it recorded now occur 93 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2813-2813 - the bytes it recorded now occur 61 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:3316-3316 - the bytes it recorded now occur 87 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:125-661 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit eb0b0e98596d07e4e206e7936c20f86d8123e401; mcp/tests/evidence-lifecycle.toml:663-747 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit b17c1ce5a93fd41d985352915ce1c30feb0fecb2; mcp/tests/evidence-lifecycle.toml:1552-2083 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 8b0254263c6998b1d4814b2e97c1bd231d39350f; mcp/tests/evidence-lifecycle.toml:2793-2830 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848; mcp/tests/evidence-lifecycle.toml:2393-2477 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a416985be1ec9cf8ec92f64882f50ca012518ac4; mcp/tests/evidence-lifecycle.toml:2847-2899 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit b52adc8bc0564f6328d3543e48998e9235f1e417; mcp/tests/evidence-lifecycle.toml:2422-2459 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit de5a7adbb21b2f6f22c3ced0eed9dd7189fe93c7. Retired means the anchor no longer stands, not that the cited subject was deleted [21]

## Retirements

- Retired at the fifth freeze d59c3493: mcp/tests/evidence-lifecycle.toml:395-395 - the bytes it recorded now occur 6 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:830-830 - the bytes it recorded now occur 7 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:1215-1215 - the bytes it recorded now occur 9 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2072-2072 - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2753-2753 - the bytes it recorded now occur 93 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2813-2813 - the bytes it recorded now occur 61 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:3316-3316 - the bytes it recorded now occur 87 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:125-661 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit eb0b0e98596d07e4e206e7936c20f86d8123e401; mcp/tests/evidence-lifecycle.toml:663-747 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit b17c1ce5a93fd41d985352915ce1c30feb0fecb2; mcp/tests/evidence-lifecycle.toml:1552-2083 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 8b0254263c6998b1d4814b2e97c1bd231d39350f; mcp/tests/evidence-lifecycle.toml:2793-2830 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848; mcp/tests/evidence-lifecycle.toml:2393-2477 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a416985be1ec9cf8ec92f64882f50ca012518ac4; mcp/tests/evidence-lifecycle.toml:2847-2899 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit b52adc8bc0564f6328d3543e48998e9235f1e417; mcp/tests/evidence-lifecycle.toml:2422-2459 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit de5a7adbb21b2f6f22c3ced0eed9dd7189fe93c7. Retired means the anchor no longer stands, not that the cited subject was deleted.