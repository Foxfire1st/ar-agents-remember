# mcp/tests/test_knowledge_review_surface.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_surface.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T15:17:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l2`, uncommitted; production line `0fca5c69766aa95eebe950c19fbcdc83864ec35a` (leaf `260921-ICR-L5`'s landed cold-start work) with leaf `260921-ICR-L2`'s uncommitted review-surface work applied |
| lastVerifiedCommitHash | `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9` |
| lastVerifiedCommitDate | 2026-09-21T16:05:56+02:00|
| governingOverview | `mcp/tests/overview.md` |

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

**This leaf (`260921-ICR-L5`) adds a third refusal group: the *before* half.** Until this leaf the
surface's pair refusals were measured only from the candidate's side — a missing candidate dataset, an
unresolvable context — and the missing side was the candidate's. Three cases now measure the other two
states a before half can be in and what the surface does with them, because a comparison is *between*
two dataset files and a file that is not one used to make SQLite raise from inside the read:

- **an absent before half refuses by name rather than being substituted with an empty one** — the state
  a cold-start repository reached until the first knowledge write established that side, and the state
  a leaf reaches when the fork point it named is missing;
- **a before half that is present but unreadable refuses by name** — the operator gets a state naming
  the side and the action instead of an `apsw.NotADBError` traceback, and the refusal names the
  *before* side specifically, since only one of the two sides can be repaired by authoring knowledge
  again;
- **the entry route refuses a damaged before half instead of raising** — the subject list is the first
  call a reader's surface makes and it compares every recorded identity against the pair, so the same
  corruption raised out of the route that exists to *offer* a subject.

The last one also proves the refusal is caused by the corruption rather than by a fixture that could
never answer: replacing the damaged side with the dataset that belongs there turns the same route into
an entry list.

## Code Commentary

### Logic

**The lane declaration is a precondition, not metadata.** `pytestmark = pytest.mark.evidence_unit`
registers the whole module in the unit population, and the leaf also appended the module to the
`unit-regression` lane in `mcp/tests/test-evidence-lanes.toml:103` and to two `consumers` lists in
`mcp/tests/evidence-lifecycle.toml:1393` and `:1421`. An unregistered `test_*.py` module makes the lane
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
candidate-resolution cases measure the resolver's behaviour rather than the host's filesystem.

**The `fixture` fixture builds one fresh two-snapshot dataset per case.** `build_diff_fixture(tmp_path
/ "review")` returns a `DiffFixture` from the shipped `diff_scope_test_support`, so no case observes
another's candidate state, and the fixture's two databases and two Git roots are real files rather
than stubs. `resolution_for` then assembles the `ReviewCandidateResolution` **without a contract** —
the fixture's own before/after database paths, Git roots and tree ids — so the case can exercise
`compose_review` without standing up a coordination tree, while the resolution cases exercise
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

**The pane cases assert the rendering against the comparison's own values.** The knowledge-pane case
reads the subject's own statements and the comparison's own facts; the two source-pane cases read the
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

**The candidate-resolution and transport cases drive the two boundaries outside the composition.** One
case proves the candidate is resolved from task context and never from a browser-chosen path; one
proves an absent candidate dataset refuses by name rather than substituting one; one proves the
transport admits exactly the two reviewable selector kinds; one proves the route serves the typed
result and refuses by name with no adapter, through `TestClient` over a bare `FastAPI` app registered
by `register_review_routes`; one proves the published assessment loader returns nothing for an
unresolvable candidate; and one proves the rendered pane types are the three the design names.

**The three before-half cases build their own resolution, and the entry-route case builds its own task
context.** The two composition cases reuse the fixture's `DiffFixture` but hand `compose_review` a
`ReviewCandidateResolution` whose `baseline_database` is a path the case owns — an absent one, then a
file holding `b"this is not a database\n"` — so the pair is real on the candidate side and deliberately
unusable on the before side, and each asserts the typed refusal plus the fact that the refused review
did not create or rewrite the side it was asked about. The entry-route case cannot do that: the route
resolves its pair from canonical task context and the browser never names a dataset, so
`_entry_route_config` **is** that context — a coordination root, one enclosure contract under
`<coordination>/tasks/<repository>/<ENTRY_MASTER>/enclosures/leaf`, and the leaf root the contract's own
recorded worktree group derives, with the code side pointing at the fixture's own repository because a
resolution requires a live code worktree and the case is about the knowledge halves. The contract's
`repo_name` is the fixture's own namespace because the halves are copied from datasets bound to it and
carry no receipt beside them — a candidate with no receipt is read under the requested name, which is
the shipped fallback for a pair a caller assembled itself. The case then writes the fixture's candidate
bytes to the resolved candidate path and corrupt bytes to the resolved baseline path, asserts the
refusal names the baseline, and finally writes the fixture's **real** before dataset to that same path
and re-runs the route to require an entry list — which is what keeps the corruption, rather than the
fixture, as the proven cause.

**The worked-review case walks the journey rather than sampling it.**
`test_the_worked_review_journey_renders_every_step_it_walks` drives the sequence the design's §8
describes in one case, and `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate`
closes it: changing only the source makes the assessment stale without making it unreadable or
reusable. The measured-binding case and the two-disagreeing-assessments case sit beside it so the
currentness axis is asserted from both directions.


**This leaf added a narrowing helper, extended the transport case, and added the two cases the new states are measured by.** `reviewed_selector(fixture)` returns the request's selector while asserting it is not `None`, which is what keeps the pyright rail green now that `ReviewSurfaceRequest.selector` is optional rather than papering over it with an ignore. `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds` was extended to assert the third admitted answer — **omitting both parameters** — beside the existing two. The two new cases are: `test_a_knowledge_only_change_leaves_an_openable_review_with_a_measured_empty_inventory` (the declared candidate tree equals the base tree while the two real datasets still differ, so the payload carries `inventory.state="measured"`, `entries=()`, `listed_total=0` and the "measured empty change set" sentence *and* an untouched knowledge comparison — both statements `present`, staleness `current`); and `test_an_inventory_that_could_not_carry_a_name_is_partial_by_construction`, which attempts all three refused shapes (`unrepresentable_paths` beside a complete inventory, beside an unavailable one, and on an otherwise-complete inventory) and asserts the one accepted shape is measured **and** partial.

### Conventions

The module imports the shipped support rather than building its own: `DiffFixture` and
`build_diff_fixture` come from `diff_scope_test_support`, `bind_assessment`/`AssessmentInputs` from
`models/lifecycles/review_assessment_store.py`, the assessment models from
`models/lifecycles/review_assessment.py`, and `compose_review`, `resolve_review_candidate`,
`review_records_for`, `ReviewCandidateResolution` and `ReviewRecordInputs` from the adapter. The
transport is imported as itself — `register_review_routes` and `review_request_from_query` from
`serving/review.py` — and driven through `fastapi.testclient.TestClient` rather than called directly,
so the route's own status idiom is measured. `pytest.raises(ValidationError)` is the shape used for
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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and its
named properties, the lane declaration and the two catalogue registrations that go with it, the two
declared vocabularies, the helpers that build the fixture's inputs through the shipped seams, and each
case with the property it pins.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the load-bearing properties, one case each, and the worked review of the design's §8 journey. | `FORBIDDEN_FIELD_NAMES` | mcp/tests/test_knowledge_review_surface.py:1-32; mcp/tests/test_knowledge_review_surface.py:102-125 |
| **The lane declaration, which is a precondition rather than metadata.** | `pytestmark` | mcp/tests/test_knowledge_review_surface.py:96-96 |
| The leaf id the resolution reports. | `REPOSITORY_LEAF` | mcp/tests/test_knowledge_review_surface.py:98-101 |
| The config that names no real root, so only the resolution's own refusals can answer. | `review_config` | mcp/tests/test_knowledge_review_surface.py:128-139 |
| The fresh two-snapshot fixture per case, and the resolution assembled without a contract so the composition can be driven without a coordination tree. | `fixture`; `resolution_for` | mcp/tests/test_knowledge_review_surface.py:139-158 |
| The one request shape, the narrowing helper the optional selector obliged, and the one failing-loudly render helper every pane case goes through. | `review_request`; `reviewed_selector`; `render` | mcp/tests/test_knowledge_review_surface.py:161-167; mcp/tests/test_knowledge_review_surface.py:170-184; mcp/tests/test_knowledge_review_surface.py:187-203 |
| The three input builders that produce records through the seams that own them rather than by constructing stored rows. | `published_assessment`; `observation`; `signal` | mcp/tests/test_knowledge_review_surface.py:206-319 |
| The shipped two-snapshot support the whole module is built on, with the independent byte-safe Git observation this leaf's inventory cases compare against. | `build_diff_fixture`; `DiffFixture`; `independent_changed_records` | mcp/tests/diff_scope_test_support.py:148-232; mcp/tests/diff_scope_test_support.py:499-513 |
| The pane cases: the subject's own statements and the comparison's own facts, the unchanged sibling and the removed claim's before-side, and the counts the selection did not reach. | `test_the_knowledge_pane_renders_the_subjects_own_statements_and_the_comparisons_own_facts`; `test_the_source_pane_shows_the_unchanged_sibling_and_the_removed_claims_before_side`; `test_the_source_pane_counts_the_unmapped_path_and_the_records_outside_the_selection` | mcp/tests/test_knowledge_review_surface.py:322-374; mcp/tests/test_knowledge_review_surface.py:377-388; mcp/tests/test_knowledge_review_surface.py:391-404 |
| **The missing-role boundary asserted at the display: unclassified, never guessed from a name.** | `test_a_missing_role_stays_unclassified_and_is_never_guessed_from_a_name` | mcp/tests/test_knowledge_review_surface.py:407-422 |
| **The whole-schema walk for a field a generated conclusion could occupy, and the case that the vocabulary defines no record kind, table or status of its own.** | `walk_property_names`; `test_the_whole_payload_schema_has_no_field_a_generated_conclusion_could_occupy`; `test_the_surface_defines_no_record_kind_no_table_and_no_status_of_its_own` | mcp/tests/test_knowledge_review_surface.py:425-447; mcp/tests/test_knowledge_review_surface.py:450-457 |
| **The stores-nothing case, measured as the two datasets' row counts being identical across a full render.** | `test_the_surface_stores_nothing_so_deleting_every_rendering_loses_no_canonical_information` | mcp/tests/test_knowledge_review_surface.py:460-470 |
| **The selects-nothing case, comparing the payload's identity and counts against the shipped comparison value for value.** | `test_the_adapter_selects_nothing_because_the_shipped_comparison_is_the_comparison_rendered` | mcp/tests/test_knowledge_review_surface.py:473-522 |
| The state cases: unassessed is unassessed; no evidence records reads `none_recorded` with source inspection still available; a passing observation is never invariant-satisfied; a signal carries no severity. | `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`; `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`; `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity` | mcp/tests/test_knowledge_review_surface.py:525-549; mcp/tests/test_knowledge_review_surface.py:552-567; mcp/tests/test_knowledge_review_surface.py:570-586 |
| **The staleness pair, asserted from both directions, plus the absent-submission-path case.** | `test_the_stale_rule_holds_in_both_directions`; `test_the_surface_reports_the_absent_submission_path_instead_of_growing_a_private_one` | mcp/tests/test_knowledge_review_surface.py:589-611; mcp/tests/test_knowledge_review_surface.py:614-623 |
| The unresolved-author case and the missing-side case, both refusals rather than renderings. | `test_an_item_whose_author_is_not_published_is_shown_as_an_unresolved_reference`; `test_a_missing_side_is_its_own_state_and_never_an_empty_string` | mcp/tests/test_knowledge_review_surface.py:626-639; mcp/tests/test_knowledge_review_surface.py:642-656 |
| The two-disagreeing-assessments case and the measured matching-binding case: the currentness axis from both directions. | `test_two_disagreeing_assessments_are_both_displayed_with_their_authors_and_no_resolution`; `test_a_measured_matching_binding_reports_the_assessment_current` | mcp/tests/test_knowledge_review_surface.py:659-685; mcp/tests/test_knowledge_review_surface.py:688-698 |
| **The worked review of the design's §8 journey, and the case that closes it: a stale assessment is never reused.** | `test_the_worked_review_journey_renders_every_step_it_walks`; `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate` | mcp/tests/test_knowledge_review_surface.py:701-727; mcp/tests/test_knowledge_review_surface.py:730-748 |
| The two resolution cases: the candidate comes from task context rather than a browser-chosen path, and an absent dataset refuses by name. | `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`; `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` | mcp/tests/test_knowledge_review_surface.py:751-764; mcp/tests/test_knowledge_review_surface.py:767-786 |
| **The absent before half refuses by name and the refused review creates nothing: the sibling leaf `260921-ICR-L5`'s case beside the absent-candidate one above, differing in *which* half is missing — the two halves are different facts and have different next actions.** | `test_an_absent_baseline_half_refuses_by_name_rather_than_substituting_an_empty_one` | mcp/tests/test_knowledge_review_surface.py:789-825 |
| **The corrupt before half is a typed refusal rather than an `apsw.NotADBError` raised from inside the read, and the refusal names the baseline rather than the candidate — only one of the two sides can be repaired by authoring knowledge again.** | `test_a_before_side_that_is_present_but_unreadable_refuses_by_name` | mcp/tests/test_knowledge_review_surface.py:828-869 |
| **The entry route states the pair refusals before any subject is compared, proved against the damage rather than against the fixture: the same route that refuses the corrupted side returns an entry list once the dataset that belongs there is written back.** This is the route `_entry_route_config` builds a real task context for, because the route resolves its pair from canonical task context and the browser never names a dataset. | `test_the_entry_route_refuses_a_damaged_before_half_instead_of_raising`; `_entry_route_config`; `ENTRY_MASTER` | mcp/tests/test_knowledge_review_surface.py:938-976; mcp/tests/test_knowledge_review_surface.py:872-935; mcp/tests/test_knowledge_review_surface.py:869-869 |
| The two transport cases: exactly the two reviewable selector kinds are admitted — or no selector at all, the task context — and the route refuses by name with no adapter. | `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds`; `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` | mcp/tests/test_knowledge_review_surface.py:979-997; mcp/tests/test_knowledge_review_surface.py:1000-1057 |
| **The loader case and the pane-name case — now also the surface's whole entry half: the unresolvable context refuses the entry read with the same code as the review (an empty list would read as "this candidate records nothing to review", a different fact), and the entry the resolver offers is measured item for item against the shipped comparison's own answer for that identity, with a subject the comparison cannot answer for dropped rather than listed with a zero.** | `test_the_published_assessment_loader_returns_nothing_for_an_unresolvable_candidate`; `test_the_rendered_pane_types_are_the_three_the_design_names` | mcp/tests/test_knowledge_review_surface.py:1060-1085; mcp/tests/test_knowledge_review_surface.py:1088-1158 |
| **The two cases this leaf (`260921-ICR-L2`) added: a knowledge-only change leaves an openable review whose inventory is a *measured* empty set while the comparison is untouched, and an inventory that could not carry a name is partial **by construction**, with all three refused shapes asserted.** | `test_a_knowledge_only_change_leaves_an_openable_review_with_a_measured_empty_inventory`; `test_an_inventory_that_could_not_carry_a_name_is_partial_by_construction` | mcp/tests/test_knowledge_review_surface.py:1161-1210; mcp/tests/test_knowledge_review_surface.py:1213-1251 |

| The lane row this module occupies. | "mcp/tests/test_knowledge_review_surface.py" | mcp/tests/test-evidence-lanes.toml:100-108 |
| The two consumer registrations this module's fixtures are recorded under. | "mcp/tests/test_knowledge_review_surface.py" | mcp/tests/evidence-lifecycle.toml:1385-1425 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds its datasets under
`tmp_path` and asserts one repository namespace's rendering.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **the sync's memory-side conflict in this card resolved as a union, and every range in the reference table re-derived against the merged 1,251-line module.** Kept from the master line: L5's three before-half cases (`789-825`, `828-869`, `938-976` with `_entry_route_config` at `872-935` and `ENTRY_MASTER` at `869`), its `0fca5c69` / `14:06:50` verification rows, and its own history entries. Kept from this leaf: the two R02 cases and the `reviewed_selector` narrowing. **Corrected rather than merged:** the module statement row's second range moved to `102-125` (where `FORBIDDEN_FIELD_NAMES` now sits); `pytestmark` is `96` and `REPOSITORY_LEAF` `98-101`; the fixtures are `128-139`, `139-158` and the builder block `206-319`; the pane cases are `322-374`, `377-388`, `391-404`; the whole-schema walk is `425-447`; the stores-nothing and selects-nothing cases are `460-470` and `473-522`; the state cases are `525-549`, `552-567`, `570-586`; staleness is `589-611`/`614-623`; the refusals are `626-639`/`642-656`; the disagreement pair is `659-685`/`688-698`; the journey is `701-727`/`730-748`; the resolution cases are `751-764`/`767-786`; the transport cases are `979-997`/`1000-1057`; and the loader/pane-name cases are `1060-1085`/`1088-1158`. The master side's rows were **merged rather than duplicated** where both named the same case, and this leaf's two new cases were added at `1161-1210` and `1213-1251`. The `diff_scope_test_support` row now also names the independent byte-safe Git observation this leaf's inventory cases assert against. No claim was dropped and none was invented.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **two new cases, one added assertion and one narrowing helper.** The knowledge-only case is the R02 boundary "zero source changes, knowledge changed" measured on a real pair, and the structural case pins the rule that an inventory which could not carry a name is partial and measured by construction. The transport case now asserts the "omit both" answer beside the two admitted kinds, and `reviewed_selector` is the narrowing that kept the optional selector from turning the pyright rail red. Every row in the reference table was re-derived against this candidate — this module grew by 46 lines and the ranges below had all shifted. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T14:00+02:00 — 260921-ICR-L5 curator (uncommitted change set on `ar/260921-icr-l5`, code base `f745e16659c5602252bb185a2ffccc356c2bde26`): **three collected cases for the *before* half, and every citation range on this card re-measured.** Until this leaf the surface's pair refusals were measured only from the candidate's side; the new cases measure the other two states a before half can be in — absent, and present but unreadable — plus the entry route that used to raise `apsw.NotADBError` out of the call that exists to *offer* a subject. The Purpose gained the third refusal group, the Logic gained the composition-level paragraph and the entry-route paragraph (including `_entry_route_config`, whose contract is the task context the route resolves from), and four reference rows were added. The file grew 946 → 1,136 lines with the new block at `:770-957`, and the imports at `:42-46` added three lines, so the shift is **+3 for everything before the block and larger after it**: every range was re-derived rather than shifted by a delta — the pane cases `:302-386` → `:305-387`, `test_a_missing_side…` `:621-632` → `:624-635`, the two resolution cases `:729-764` → `:732-767`, the transport cases `:767-842` → `:960-1035`, and the loader/pane-name pair `:848-946` → `:1038-1136`. The lane and consumer rows (`test-evidence-lanes.toml:100-108`, `evidence-lifecycle.toml:1385-1425`) were re-read and left as they stand. This is a body change and not a metadata-only refresh. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded; no stamp was advanced or invented and no commit was made.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **the surface's entry half is asserted inside the two existing cases rather than in new ones.** The loader case now also asks the same unresolvable context for the entry list and asserts it refuses with `candidate_unresolved` and an empty `entries` — the read resolves through the identical operation the review does, so an empty list would be the wrong answer, and no new collected case was added (25 before, 25 after, so the unit lane's budget is untouched). The pane-name case now measures `_reviewable_entries` against the shipped `diff_knowledge_scope`'s own answer for the fixture's invariant: every offered entry is one the comparison answered for, its `selected_item_count` equals the comparison's own `items_total` rather than a trusted number, and an identity the candidate does not record is absent from the list with `_selected_item_count` returning `None` instead of a zero. This card's reference row was widened to name both facts. No verification stamp was advanced, because no commit contains this body.
- 2026-09-20T00:56+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 10 enforced citation rows this card carried (citation_anchor_absent_from_range, citation_range_out_of_bounds). Every row was re-read against the source rather than trusted from the item's cited text: the six first ranges the earlier mechanical projection had repointed were verified current and left untouched, while that projection's rewritten first range had opened a gap in each row and left the *second* range stale, so those six were repointed to the construct each claim names — `test_a_missing_side_is_its_own_state_and_never_an_empty_string` 621-632, `test_a_measured_matching_binding_reports_the_assessment_current` 667-674, `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate` 708-723, `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` 745-764, `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` 786-842, `test_the_rendered_pane_types_are_the_three_the_design_names` 858-872 (the last also clearing the out-of-bounds 863-877). Two claims name cases that were merged upstream, so they were re-cited to the surviving case that carries the fact: `test_no_evidence_records_reads_none_recorded_with_source_inspection_still_available` is asserted inside `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible` (505-529), and the staleness pair inside `test_the_stale_rule_holds_in_both_directions` (569-590). No claim wording was changed, every other range is untouched, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 6 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `test_an_item_whose_author_is_not_published_is_shown_as_an_unresolved_reference`; `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`; `test_the_published_assessment_loader_returns_nothing_for_an_unresolvable_candidate`; `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds`; `test_the_worked_review_journey_renders_every_step_it_walks`; `test_two_disagreeing_assessments_are_both_displayed_with_their_authors_and_no_resolution`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 2 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_knowledge_review_surface.py.md:206` (test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible) — re-read the claim against the current module: the named case was renamed or consolidated, and the successor's own docstring names the consolidation; `test_knowledge_review_surface.py.md:207` (test_the_stale_rule_holds_in_both_directions) — re-read the claim against the current module: the named case was renamed or consolidated, and the successor's own docstring names the consolidation.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 6 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `test_knowledge_review_surface.py.md:208` (`test_an_item_whose_author_is_not_published_is_shown_as_an_unresolved_reference`, `test_a_missing_side_is_its_own_state_and_never_an_empty_string`); `test_knowledge_review_surface.py.md:209` (`test_two_disagreeing_assessments_are_both_displayed_with_their_authors_and_no_resolution`, `test_a_measured_matching_binding_reports_the_assessment_current`); `test_knowledge_review_surface.py.md:210` (`test_the_worked_review_journey_renders_every_step_it_walks`, `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate`); `test_knowledge_review_surface.py.md:211` (`test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`, `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one`); `test_knowledge_review_surface.py.md:212` (`test_the_transport_admits_exactly_the_two_reviewable_selector_kinds`, `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter`); `test_knowledge_review_surface.py.md:213` (`test_the_published_assessment_loader_returns_nothing_for_an_unresolvable_candidate`, `test_the_rendered_pane_types_are_the_three_the_design_names`).
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's case module. It records the module's four load-bearing properties — the surface **stores nothing**, **selects nothing**, has **no field a generated conclusion could occupy**, and renders every refusal state as a state — each pinned by one case, plus the worked review of `retrieval-review-design.md` §8's journey. It also records that the lane declaration is a **precondition** rather than metadata (an unregistered module makes the lane manifest refuse the repository), the two declared vocabularies (`REPOSITORY_LEAF`, `FORBIDDEN_FIELD_NAMES`), the helpers that build the fixture's three record collections through the shipped seams rather than by inserting stored rows, and the fact that no case re-implements the read, the comparison or the view it measures. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.