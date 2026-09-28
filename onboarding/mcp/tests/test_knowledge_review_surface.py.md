# mcp/tests/test_knowledge_review_surface.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_surface.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T23:41:23+02:00 |
| lastVerifiedCommitHash | `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` |
| lastVerifiedCommitDate | 2026-09-29T00:17:28+02:00|
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
| The module's own statement of the load-bearing properties, one case each, and the worked review of the design's §8 journey. | `FORBIDDEN_FIELD_NAMES` | mcp/tests/test_knowledge_review_surface.py:1-35; mcp/tests/test_knowledge_review_surface.py:98-121 |
| **The lane declaration, which is a precondition rather than metadata.** | `pytestmark` | mcp/tests/test_knowledge_review_surface.py:92-93 |
| The leaf id the resolution reports. | `REPOSITORY_LEAF` | mcp/tests/test_knowledge_review_surface.py:94-97 |
| The config that names no real root, so only the resolution's own refusals can answer. | `review_config` | mcp/tests/test_knowledge_review_surface.py:124-135 |
| The fresh two-snapshot fixture per case, and the resolution assembled without a contract so the composition can be driven without a coordination tree. | `fixture`; `resolution_for` | mcp/tests/test_knowledge_review_surface.py:135-154 |
| The one request shape, the narrowing helper the optional selector obliged, and the one failing-loudly render helper every pane case goes through. | `review_request`; `reviewed_selector`; `render` | mcp/tests/test_knowledge_review_surface.py:157-163; mcp/tests/test_knowledge_review_surface.py:166-180; mcp/tests/test_knowledge_review_surface.py:183-199 |
| The three input builders that produce records through the seams that own them rather than by constructing stored rows. | `published_assessment`; `observation`; `signal` | mcp/tests/test_knowledge_review_surface.py:202-315 |
| The shipped two-snapshot support the whole module is built on, with the independent byte-safe Git observation this leaf's inventory cases compare against. | `build_diff_fixture`; `DiffFixture`; `independent_changed_records` | mcp/tests/diff_scope_test_support.py:148-232; mcp/tests/diff_scope_test_support.py:499-513 |
| The pane cases: since `260921-ICR-L7` the knowledge-pane case asserts the recorded ambiguous selection (every head and retained revision named, no pair, both sides `unresolved` with the ambiguity as their detail) and the comparison's own field changes; the source-pane cases read the unchanged sibling and the removed claim's before-side, and the counts the selection did not reach. | `test_the_knowledge_pane_renders_the_subjects_own_statements_and_the_comparisons_own_facts`; `test_the_source_pane_shows_the_unchanged_sibling_and_the_removed_claims_before_side`; `test_the_source_pane_counts_the_unmapped_path_and_the_records_outside_the_selection` | mcp/tests/test_knowledge_review_surface.py:318-409; mcp/tests/test_knowledge_review_surface.py:410-421; mcp/tests/test_knowledge_review_surface.py:424-437 |
| **The missing-role boundary asserted at the display: unclassified, never guessed from a name.** | `test_a_missing_role_stays_unclassified_and_is_never_guessed_from_a_name` | mcp/tests/test_knowledge_review_surface.py:440-455 |
| **The whole-schema walk for a field a generated conclusion could occupy, and the case that the vocabulary defines no record kind, table or status of its own.** | `walk_property_names`; `test_the_whole_payload_schema_has_no_field_a_generated_conclusion_could_occupy`; `test_the_surface_defines_no_record_kind_no_table_and_no_status_of_its_own` | mcp/tests/test_knowledge_review_surface.py:458-482; mcp/tests/test_knowledge_review_surface.py:483-492 |
| **The stores-nothing case, measured as the two datasets' row counts being identical across a full render.** | `test_the_surface_stores_nothing_so_deleting_every_rendering_loses_no_canonical_information` | mcp/tests/test_knowledge_review_surface.py:493-503 |
| **The selects-nothing case, comparing the payload's identity and counts against the shipped comparison value for value.** | `test_the_adapter_selects_nothing_because_the_shipped_comparison_is_the_comparison_rendered` | mcp/tests/test_knowledge_review_surface.py:506-555 |
| The state cases: unassessed is unassessed; no evidence records reads `none_recorded` with source inspection still available; a passing observation is never invariant-satisfied; a signal carries no severity. | `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`; `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`; `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity` | mcp/tests/test_knowledge_review_surface.py:558-582; mcp/tests/test_knowledge_review_surface.py:585-600; mcp/tests/test_knowledge_review_surface.py:603-619 |
| **The staleness pair, asserted from both directions, plus the absent-submission-path case.** | `test_the_stale_rule_holds_in_both_directions`; `test_the_surface_reports_the_absent_submission_path_instead_of_growing_a_private_one` | mcp/tests/test_knowledge_review_surface.py:622-644; mcp/tests/test_knowledge_review_surface.py:647-656 |
| The unresolved-author case and the missing-side case, both refusals rather than renderings. | `test_an_item_whose_author_is_not_published_is_shown_as_an_unresolved_reference`; `test_a_missing_side_is_its_own_state_and_never_an_empty_string` | mcp/tests/test_knowledge_review_surface.py:659-672; mcp/tests/test_knowledge_review_surface.py:675-689 |
| The two-disagreeing-assessments case and the measured matching-binding case — the currentness axis from both directions, and the case `260921-ICR-L15` renamed so its name and its input agree. | `test_two_disagreeing_assessments_are_both_displayed_with_their_authors_and_no_resolution`; `test_only_a_complete_matching_measurement_reports_the_assessment_current` | mcp/tests/test_knowledge_review_surface.py:692-718; mcp/tests/test_knowledge_review_surface.py:726-788 |
| **The worked review of the design's §8 journey, and the case that closes it: a stale assessment is never reused.** | `test_the_worked_review_journey_renders_every_step_it_walks`; `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate` | mcp/tests/test_knowledge_review_surface.py:790-837; mcp/tests/test_knowledge_review_surface.py:840-861 |
| **The pane-name case carries the surface's re-contracted entry catalogue (`260921-ICR-L9`): the catalogue the resolver offers is measured identity for identity against the two snapshots' own tables — every recorded invariant and family listed with its label and before/after presence, listing one never comparing it, a subject the comparison cannot answer for still listed (its reason carried by the review it opens), and an identity neither snapshot records absent.** | `test_the_rendered_pane_types_are_the_three_the_design_names`; `read_subject_catalogue` | mcp/tests/test_knowledge_review_surface.py:867-937; mcp/tests/test_knowledge_review_surface.py:895-895 |
| **The two cases this leaf (`260921-ICR-L2`) added: a knowledge-only change leaves an openable review whose inventory is a *measured* empty set while the comparison is untouched, and an inventory that could not carry a name is partial **by construction**, with all three refused shapes asserted — the first now also asserting the corrected attribution (measured empty partition, zero denominator, empty lists, locations still displayed). Since `260921-ICR-L7` the first case also asserts the same explicitly ambiguous selection as the rewritten pane case (the knowledge half is untouched by the empty source half — only the source measurement changed, and only the source pane answers for it).** | `test_a_knowledge_only_change_leaves_an_openable_review_with_a_measured_empty_inventory`; `test_an_inventory_that_could_not_carry_a_name_is_partial_by_construction` | mcp/tests/test_knowledge_review_surface.py:940-1015; mcp/tests/test_knowledge_review_surface.py:1018-1056 |

| The lane row this module occupies. | "mcp/tests/test_knowledge_review_surface.py" | mcp/tests/test-evidence-lanes.toml:111-113 |
| The two consumer registrations this module's fixtures are recorded under. | "mcp/tests/test_knowledge_review_surface.py" | mcp/tests/evidence-lifecycle.toml:1427-1441; mcp/tests/evidence-lifecycle.toml:1471-1471 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds its datasets under
`tmp_path` and asserts one repository namespace's rendering.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): **the resolution-and-transport section moved out, verbatim.** The worker moved nine cases, with `ENTRY_MASTER` and `_entry_route_config`, into `test_knowledge_review_resolution_and_route.py` (1475 → 1056 lines, 31 → 22 cases). The moved cases are the two resolution cases, the three `260921-ICR-L5` before-half cases, the two transport cases, the `260921-ICR-L17` previous-identity case and the loader case. The collected node names are identical apart from the module name. The pane-type and inventory cases stay here under a new section header. On this card, Purpose now points to the new module and names the helpers it imports from here. The before-half and previous-identity prose, five reference rows and the loader half of the loader/pane-name row moved to the new card; Conventions no longer lists the resolver and transport imports. The `260921-ICR-L2` paragraph now notes that the moved selector-kind case does not assert the selector omission; that was already true at the base. Every other range was re-pointed through the exact base-to-candidate line map. No stamp was advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-22T15:25:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **the KS-era mechanism block re-contracted to the catalogue (1314 → 1313 lines; `ICR-R09@v1`).** `test_the_rendered_pane_types_are_the_three_the_design_names` measured the old entry mechanism — `_reviewable_entries` compared each recorded identity through `diff_knowledge_scope` and `_selected_item_count` dropped a refused one — which the packet's Required Behavior ("catalogue loading must not fully compare") and VERIFICATION F06 order replaced. The case now drives `read_subject_catalogue` and asserts: union membership from **both** snapshots' tables, labels on every row, per-row `presence`, the fixture's retry identity present with `presence == "both"`, an unrecorded identity excluded (it is not part of the comparison's population), and an agreement check that the reviewed identity **opens through the shipped comparison** the review itself uses. All other assertions in the case are byte-identical. The import block dropped the two private helper imports for the catalogue's one public name (the -1 line every range below the block inherits). The Logic's mechanism paragraph and the pane-name row record the re-contract rather than the old drop rule. **Citation accounting:** all ranges into this file re-derived against the 1313-line candidate — the import-block shift is -1 below `:48`, so every row's range moved by one line, measured per construct and not by delta arithmetic (`pytestmark` `95`, `REPOSITORY_LEAF` `97-100`, `FORBIDDEN_FIELD_NAMES` `101-124`, `review_config` `127-138`, `fixture`/`resolution_for` `138-157`, the request/narrow/render helpers `160-166`/`169-183`/`186-202`, the builder block `205-318`, the pane cases `321-412`/`413-424`/`427-440`, the missing-role case `443-458`, the schema walk and its two cases `461-485`/`486-495`, stores-nothing `496-506`, selects-nothing `509-558`, the state cases `561-585`/`588-603`/`606-622`, staleness `625-647`/`650-659`, the refusals `662-675`/`678-692`, the disagreement pair `695-721`/`724-734`, the journey `737-763`/`766-784`, the resolution cases `787-800`/`803-822`, the before-half cases `825-861`/`864-904`, the entry-route case `974-1012` with `_entry_route_config` `908-973` and `ENTRY_MASTER` `905`, the transport cases `1015-1033`/`1036-1093`, the loader case `1096-1121`, the re-contracted pane-name case `1124-1194`, the L2 cases `1197-1274`/`1275-1313`); the lane rows moved with the manifests' own growth since they were recorded and are re-anchored at their current registrations (`test-evidence-lanes.toml:109`, `evidence-lifecycle.toml:1412` and `:1447`). **Stamp accounting:** the verification pair names the leaf's base — the last real commit the reading was taken against — because the re-contracted case exists only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T10:40:00+02:00 — 260921-ICR-L7 curator (uncommitted change set on `ar/260921-icr-l7`, base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **two cases rewritten from the old both-sides rule to ambiguity assertions (1261 → 1314 lines).** The knowledge-pane case and the knowledge-only case now assert the explicitly ambiguous selection — every head and retained revision named, no pair, both statements `unresolved` with the ambiguity as their detail — because the fixture's retry identity is branchy on both snapshots; the Logic pane paragraph and both reference rows record the rewrite rather than annotating the old wording. **Citation accounting:** all 33 ranges into this file re-derived from each construct's own extent against the 1314-line module (the two rewritten cases at `322-413` and `1198-1275`, everything between the two rewrite hunks shifted one hunk-width, everything below the second hunk two). Header names this leaf's candidate row. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the leaf's base — the last real commit the reading was taken against — because the rewritten assertions exist only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **one assertion block corrected (1251 → 1261 lines).** The knowledge-only case now asserts the corrected attribution: an empty change set yields a *measured* empty partition (`changed_total == 0`, `complete is True`) with all three lists empty and the recorded claims still displayed as locations — correcting the earlier behaviour that listed the fixture's unchanged mapped paths as attributed changes. The row above was re-derived against this candidate. **Stamp accounting:** old verification rows name the last real commit; this leaf's claims were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **the sync's memory-side conflict in this card resolved as a union, and every range in the reference table re-derived against the merged 1,251-line module.** Kept from the master line: L5's three before-half cases (`789-825`, `828-869`, `938-976` with `_entry_route_config` at `872-935` and `ENTRY_MASTER` at `869`), its `0fca5c69` / `14:06:50` verification rows, and its own history entries. Kept from this leaf: the two R02 cases and the `reviewed_selector` narrowing. **Corrected rather than merged:** the module statement row's second range moved to `102-125` (where `FORBIDDEN_FIELD_NAMES` now sits); `pytestmark` is `96` and `REPOSITORY_LEAF` `98-101`; the fixtures are `128-139`, `139-158` and the builder block `206-319`; the pane cases are `322-374`, `377-388`, `391-404`; the whole-schema walk is `425-447`; the stores-nothing and selects-nothing cases are `460-470` and `473-522`; the state cases are `525-549`, `552-567`, `570-586`; staleness is `589-611`/`614-623`; the refusals are `626-639`/`642-656`; the disagreement pair is `659-685`/`688-698`; the journey is `701-727`/`730-748`; the resolution cases are `751-764`/`767-786`; the transport cases are `979-997`/`1000-1057`; and the loader/pane-name cases are `1060-1085`/`1088-1158`. The master side's rows were **merged rather than duplicated** where both named the same case, and this leaf's two new cases were added at `1161-1210` and `1213-1251`. The `diff_scope_test_support` row now also names the independent byte-safe Git observation this leaf's inventory cases assert against. No claim was dropped and none was invented.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **two new cases, one added assertion and one narrowing helper.** The knowledge-only case is the R02 boundary "zero source changes, knowledge changed" measured on a real pair, and the structural case pins the rule that an inventory which could not carry a name is partial and measured by construction. The transport case now asserts the "omit both" answer beside the two admitted kinds, and `reviewed_selector` is the narrowing that kept the optional selector from turning the pyright rail red. Every row in the reference table was re-derived against this candidate — this module grew by 46 lines and the ranges below had all shifted. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T14:00+02:00 — 260921-ICR-L5 curator (uncommitted change set on `ar/260921-icr-l5`, code base `f745e16659c5602252bb185a2ffccc356c2bde26`): **three collected cases for the *before* half, and every citation range on this card re-measured.** Until this leaf the surface's pair refusals were measured only from the candidate's side; the new cases measure the other two states a before half can be in — absent, and present but unreadable — plus the entry route that used to raise `apsw.NotADBError` out of the call that exists to *offer* a subject. The Purpose gained the third refusal group, the Logic gained the composition-level paragraph and the entry-route paragraph (including `_entry_route_config`, whose contract is the task context the route resolves from), and four reference rows were added. The file grew 946 → 1,136 lines with the new block at `:770-957`, and the imports at `:42-46` added three lines, so the shift is **+3 for everything before the block and larger after it**: every range was re-derived rather than shifted by a delta — the pane cases `:302-386` → `:305-387`, `test_a_missing_side…` `:621-632` → `:624-635`, the two resolution cases `:729-764` → `:732-767`, the transport cases `:767-842` → `:960-1035`, and the loader/pane-name pair `:848-946` → `:1038-1136`. The lane and consumer rows (`test-evidence-lanes.toml:100-108`, `evidence-lifecycle.toml:1385-1425`) were re-read and left as they stand. This is a body change and not a metadata-only refresh. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded; no stamp was advanced or invented and no commit was made.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **the surface's entry half is asserted inside the two existing cases rather than in new ones.** The loader case now also asks the same unresolvable context for the entry list and asserts it refuses with `candidate_unresolved` and an empty `entries` — the read resolves through the identical operation the review does, so an empty list would be the wrong answer, and no new collected case was added (25 before, 25 after, so the unit lane's budget is untouched). The pane-name case now measures `_reviewable_entries` against the shipped `diff_knowledge_scope`'s own answer for the fixture's invariant: every offered entry is one the comparison answered for, its `selected_item_count` equals the comparison's own `items_total` rather than a trusted number, and an identity the candidate does not record is absent from the list with `_selected_item_count` returning `None` instead of a zero. This card's reference row was widened to name both facts. No verification stamp was advanced, because no commit contains this body.
- 2026-09-20T00:56+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 10 enforced citation rows this card carried (citation_anchor_absent_from_range, citation_range_out_of_bounds). Every row was re-read against the source rather than trusted from the item's cited text: the six first ranges the earlier mechanical projection had repointed were verified current and left untouched, while that projection's rewritten first range had opened a gap in each row and left the *second* range stale, so those six were repointed to the construct each claim names — `test_a_missing_side_is_its_own_state_and_never_an_empty_string` 621-632, `test_a_measured_matching_binding_reports_the_assessment_current` 667-674, `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate` 708-723, `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` 745-764, `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` 786-842, `test_the_rendered_pane_types_are_the_three_the_design_names` 858-872 (the last also clearing the out-of-bounds 863-877). Two claims name cases that were merged upstream, so they were re-cited to the surviving case that carries the fact: `test_no_evidence_records_reads_none_recorded_with_source_inspection_still_available` is asserted inside `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible` (505-529), and the staleness pair inside `test_the_stale_rule_holds_in_both_directions` (569-590). No claim wording was changed, every other range is untouched, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 6 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `test_an_item_whose_author_is_not_published_is_shown_as_an_unresolved_reference`; `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`; `test_the_published_assessment_loader_returns_nothing_for_an_unresolvable_candidate`; `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds`; `test_the_worked_review_journey_renders_every_step_it_walks`; `test_two_disagreeing_assessments_are_both_displayed_with_their_authors_and_no_resolution`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 2 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_knowledge_review_surface.py.md:206` (test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible) — re-read the claim against the current module: the named case was renamed or consolidated, and the successor's own docstring names the consolidation; `test_knowledge_review_surface.py.md:207` (test_the_stale_rule_holds_in_both_directions) — re-read the claim against the current module: the named case was renamed or consolidated, and the successor's own docstring names the consolidation.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 6 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `test_knowledge_review_surface.py.md:208` (`test_an_item_whose_author_is_not_published_is_shown_as_an_unresolved_reference`, `test_a_missing_side_is_its_own_state_and_never_an_empty_string`); `test_knowledge_review_surface.py.md:209` (`test_two_disagreeing_assessments_are_both_displayed_with_their_authors_and_no_resolution`, `test_a_measured_matching_binding_reports_the_assessment_current`); `test_knowledge_review_surface.py.md:210` (`test_the_worked_review_journey_renders_every_step_it_walks`, `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate`); `test_knowledge_review_surface.py.md:211` (`test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`, `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one`); `test_knowledge_review_surface.py.md:212` (`test_the_transport_admits_exactly_the_two_reviewable_selector_kinds`, `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter`); `test_knowledge_review_surface.py.md:213` (`test_the_published_assessment_loader_returns_nothing_for_an_unresolvable_candidate`, `test_the_rendered_pane_types_are_the_three_the_design_names`).
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's case module. It records the module's four load-bearing properties — the surface **stores nothing**, **selects nothing**, has **no field a generated conclusion could occupy**, and renders every refusal state as a state — each pinned by one case, plus the worked review of `retrieval-review-design.md` §8's journey. It also records that the lane declaration is a **precondition** rather than metadata (an unregistered module makes the lane manifest refuse the repository), the two declared vocabularies (`REPOSITORY_LEAF`, `FORBIDDEN_FIELD_NAMES`), the helpers that build the fixture's three record collections through the shipped seams rather than by inserting stored rows, and the fact that no case re-implements the read, the comparison or the view it measures. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. What was actually read is this leaf's uncommitted working tree, and closeout owns the stamp once the code commit exists.
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


## Update History
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (candidate `ar/260921-icr-l15`, uncommitted; leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58`, so the honest basis for every claim below is that commit plus the working-tree delta): **citation repair only, forced by this leaf's rewrite of this module (1395 → 1475 lines).** Twelve ranges across six rows were re-pointed to the construct each row names, every one read back at its new lines before it was written, and no row lost the anchor it still had: the journey/staleness row `:737-763` → `:793-840` and `:766-784` → `:843-864`; the resolution row `:787-800` → `:870-883` and `:803-822` → `:886-905`; the entry-route row `:905-905` → `:1057-1095`; the transport row `:1015-1033` → `:1098-1116` and `:1036-1093` → `:1119-1176`; the loader/pane-name/catalogue row `:1206-1206` → `:1258-1283`, `:1124-1194` → `:1286-1356` and `:1234-1234` → `:1314-1314` (the catalogue call, which moved with the module — the import at `:46` is the anchor's other holding); and the two R02 cases row `:1357-1357` → `:1359-1434` and `:1275-1313` → `:1437-1475`. The claim-reopen the journey and staleness anchors carried is cleared by those two ranges containing their declaration lines. One row could **not** be repaired and was left exactly as it stands: `test_a_measured_matching_binding_reports_the_assessment_current` (`:695-721`, `:724-734`) is the case this leaf renamed to `test_only_a_complete_matching_measurement_reports_the_assessment_current` (`:729`), whose input is now a real measurement rather than an empty mapping; the old name exists nowhere in the code tree, so the checker's remediation for that class is a claim-content re-read and not a range edit, and no anchor was renamed and no pointer invented. Its claim-reopen is left with it for the same reason. No Finding, anchor or claim wording changed, no range was deleted and none was appended, and **no verification stamp was advanced**: the candidate is uncommitted, so `lastVerifiedCommitHash`/`lastVerifiedCommitDate` keep the values they hold and the governed closeout owns the real stamp.
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **one case drives the previous identity through every hop (`ICR-R17@v1`; 30 → 31 collected).** `render` now asks the way a refresh asks — the identity travels on the request rather than as a parallel keyword, because the adapter's keyword is gone — and the new case drives the real route over `TestClient` three times: a refresh that reaches the port and answers `stale` with the carried identity labelled and submission disabled while the rendered comparison keeps its own digest, a plain read that carries nothing and is `current`, and a malformed spelling refused `400` with the offending input named. **Citation accounting:** the `read_subject_catalogue` and pane-name rows were re-derived — `read_subject_catalogue` is imported at `:46` and called at `:1234`, `test_the_rendered_pane_types_are_the_three_the_design_names` is at `:1206`, and `test_an_inventory_that_could_not_carry_a_name_is_partial_by_construction` at `:1357`. **Stamp accounting:** the verification pair names this leaf's base — the last real commit the reading was taken against — because the new case exists only in this leaf's uncommitted working tree; closeout owns the stamp once the code commit exists.
