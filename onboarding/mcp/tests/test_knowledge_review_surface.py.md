# mcp/tests/test_knowledge_review_surface.py

## Governing Overview

[mcp/tests route overview](overview.md)

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

## Code Commentary

### Logic

**The lane declaration is a precondition, not metadata.** `pytestmark = pytest.mark.evidence_unit`
registers the whole module in the unit population, and the leaf also appended the module to the
`unit-regression` lane in `mcp/tests/test-evidence-lanes.toml:109` and to two `consumers` lists in
`mcp/tests/evidence-lifecycle.toml:1412` and `:1447`. An unregistered `test_*.py` module makes the lane
manifest refuse the repository, so the registration is what lets the module be collected at all.

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

**`published_assessment` builds one assessment through the shipped binding seam rather than by
constructing a stored row.** It builds a `ReviewAssessmentRevision` whose `subject` names the fixture's
invariant id with its before and after revision ids, whose `evidenceRefs` name a code namespace, and
whose `comparisonRef` and `scopeManifestRef` are the fixture's own recorded references, and then
returns `bind_assessment(authorized=revision, inputs=AssessmentInputs(...))`. `observation(...)` and
`signal(fixture)` do the same for the other two collections, so the evidence pane's three inputs are
all produced by the modules that own them.

**The pane cases assert the rendering against the comparison's own values — and since leaf
`260921-ICR-L7` the knowledge-pane case asserts the recorded selection, not the old both-sides
statements.** The fixture's retry identity is branchy on both snapshots (the baseline retains two
successor heads of the base revision, the candidate three), so `ICR-R07@v1` reports an explicit
ambiguous selection: the case asserts the selection names every head and every retained revision
with no pair, both statements are `unresolved` carrying the ambiguity statement as their detail,
conditions are empty, and the field changes are exactly the comparison's own. The two source-pane cases read the
unchanged sibling, the removed claim's before-side, the unmapped path counted through the expansion and
the records outside the selection. One case is dedicated to a missing role staying unclassified and
never being guessed from a name, which is the `ReviewSourceLocation.role` boundary asserted at the
display rather than only in the model.

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

**The selects-nothing case compares the payload's identity and counts value for value against the
shipped comparison.** `test_the_adapter_selects_nothing_because_the_shipped_comparison_is_the_comparison_rendered`
runs the shipped `diff_knowledge_scope` directly and asserts the payload's comparison identity, item
identities and counts are that result's own values, so a future re-derivation inside the adapter fails
the case.

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

**The pane-type case stays here, under its own section header.** The candidate-resolution and
transport cases moved to the resolution-and-route module (see Purpose).
`test_the_rendered_pane_types_are_the_three_the_design_names` remains, beside the two measured-inventory
cases, and proves the rendered pane types are the three the design names.

**The worked-review case walks the journey rather than sampling it.**
`test_the_worked_review_journey_renders_every_step_it_walks` drives the sequence the design's §8
describes in one case, and `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate`
closes it: changing only the source makes the assessment stale without making it unreadable or
reusable. The measured-binding case and the two-disagreeing-assessments case sit beside it so the
currentness axis is asserted from both directions.


**`260921-ICR-L2` added a narrowing helper, extended the transport case, and added the two cases the new states are measured by.** `reviewed_selector(fixture)` returns the request's selector while asserting it is not `None`, which is what keeps the pyright rail green now that `ReviewSurfaceRequest.selector` is optional rather than papering over it with an ignore. `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds` was extended to assert the third admitted answer — **omitting both parameters** — beside the existing two. (That case now lives in the resolution-and-route module, and as moved it no longer carries the omission assertion; the selector-less route is measured by the source-endpoints module's task-context case.) The two new cases are: `test_a_knowledge_only_change_leaves_an_openable_review_with_a_measured_empty_inventory` (the declared candidate tree equals the base tree while the two real datasets still differ, so the payload carries `inventory.state="measured"`, `entries=()`, `listed_total=0` and the "measured empty change set" sentence *and* an untouched knowledge comparison — both statements `present`, staleness `current`); and `test_an_inventory_that_could_not_carry_a_name_is_partial_by_construction`, which attempts all three refused shapes (`unrepresentable_paths` beside a complete inventory, beside an unavailable one, and on an otherwise-complete inventory) and asserts the one accepted shape is measured **and** partial.

### Conventions

The module imports the shipped support rather than building its own: `DiffFixture` and
`build_diff_fixture` come from `diff_scope_test_support`, `bind_assessment`/`AssessmentInputs` from
`models/lifecycles/review_assessment_store.py`, the assessment models from
`models/lifecycles/review_assessment.py`, and `compose_review`, `ReviewCandidateResolution` and
`ReviewRecordInputs` from the adapter. Since `260921-ICR-L57` the resolver (`resolve_review_candidate`),
`review_records_for` and the transport (`register_review_routes`, `review_request_from_query`, driven
through `fastapi.testclient.TestClient`) are imported by the resolution-and-route module, not here. `pytest.raises(ValidationError)` is the shape used for
every constructor-enforced prohibition. Fixtures are function-scoped and take `tmp_path`, so no case
shares a dataset with another.

### Invariants And Boundaries

- **No case re-implements what it measures.** The comparison comes from `diff_knowledge_scope`, the
  matrix from the shipped view operation, the assessments from `bind_assessment`, and the row counts
  from `read_row_counts`.
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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and its
named properties, the lane declaration and the two catalogue registrations that go with it, the two
declared vocabularies, the helpers that build the fixture's inputs through the shipped seams, and each
case with the property it pins.

- The module's own statement of the load-bearing properties, one case each, and the worked review of the design's §8 journey. [1]
- **The lane declaration, which is a precondition rather than metadata.** [2]
- The leaf id the resolution reports. [3]
- The config that names no real root, so only the resolution's own refusals can answer. [4]
- The fresh two-snapshot fixture per case, and the resolution assembled without a contract so the composition can be driven without a coordination tree. [5]
- The one request shape, the narrowing helper the optional selector obliged, and the one failing-loudly render helper every pane case goes through. [6]
- The three input builders that produce records through the seams that own them rather than by constructing stored rows. [7]
- The shipped two-snapshot support the whole module is built on, with the independent byte-safe Git observation this leaf's inventory cases compare against. [8]
- The pane cases: since `260921-ICR-L7` the knowledge-pane case asserts the recorded ambiguous selection (every head and retained revision named, no pair, both sides `unresolved` with the ambiguity as their detail) and the comparison's own field changes; the source-pane cases read the unchanged sibling and the removed claim's before-side, and the counts the selection did not reach. [9]
- **The missing-role boundary asserted at the display: unclassified, never guessed from a name.** [10]
- **The whole-schema walk for a field a generated conclusion could occupy, and the case that the vocabulary defines no record kind, table or status of its own.** [11]
- **The stores-nothing case, measured as the two datasets' row counts being identical across a full render.** [12]
- **The selects-nothing case, comparing the payload's identity and counts against the shipped comparison value for value.** [13]
- The state cases: unassessed is unassessed; no evidence records reads `none_recorded` with source inspection still available; a passing observation is never invariant-satisfied; a signal carries no severity. [14]
- **The staleness pair, asserted from both directions, plus the absent-submission-path case.** [15]
- The unresolved-author case and the missing-side case, both refusals rather than renderings. [16]
- The two-disagreeing-assessments case and the measured matching-binding case — the currentness axis from both directions, and the case `260921-ICR-L15` renamed so its name and its input agree. [17]
- **The worked review of the design's §8 journey, and the case that closes it: a stale assessment is never reused.** [18]
- **The pane-name case carries the surface's re-contracted entry catalogue (`260921-ICR-L9`): the catalogue the resolver offers is measured identity for identity against the two snapshots' own tables — every recorded invariant and family listed with its label and before/after presence, listing one never comparing it, a subject the comparison cannot answer for still listed (its reason carried by the review it opens), and an identity neither snapshot records absent.** [19]
- **The two cases this leaf (`260921-ICR-L2`) added: a knowledge-only change leaves an openable review whose inventory is a *measured* empty set while the comparison is untouched, and an inventory that could not carry a name is partial **by construction**, with all three refused shapes asserted — the first now also asserting the corrected attribution (measured empty partition, zero denominator, empty lists, locations still displayed). Since `260921-ICR-L7` the first case also asserts the same explicitly ambiguous selection as the rewritten pane case (the knowledge half is untouched by the empty source half — only the source measurement changed, and only the source pane answers for it).** [20]

| The lane row this module occupies. | "mcp/tests/test_knowledge_review_surface.py" | mcp/tests/test-evidence-lanes.toml:111-113 |
| The two consumer registrations this module's fixtures are recorded under. | "mcp/tests/test_knowledge_review_surface.py" | mcp/tests/evidence-lifecycle.toml:1427-1441; mcp/tests/evidence-lifecycle.toml:1471-1471 |

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
