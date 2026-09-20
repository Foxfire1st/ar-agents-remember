# mcp/tests/test_knowledge_review_surface.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_surface.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T18:05+02:00 |
| lastVerifiedCommitHash |  `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`|
| lastVerifiedCommitDate |  2026-09-20T02:00:33+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l22` uncommitted source; base `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
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

**The worked-review case walks the journey rather than sampling it.**
`test_the_worked_review_journey_renders_every_step_it_walks` drives the sequence the design's §8
describes in one case, and `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate`
closes it: changing only the source makes the assessment stale without making it unreadable or
reusable. The measured-binding case and the two-disagreeing-assessments case sit beside it so the
currentness axis is asserted from both directions.

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
| The module's own statement of the load-bearing properties, one case each, and the worked review of the design's §8 journey. | `FORBIDDEN_FIELD_NAMES` | mcp/tests/test_knowledge_review_surface.py:1-29; mcp/tests/test_knowledge_review_surface.py:94-119 |
| **The lane declaration, which is a precondition rather than metadata.** | `pytestmark` | mcp/tests/test_knowledge_review_surface.py:90-92 |
| The leaf id the resolution reports. | `REPOSITORY_LEAF` | mcp/tests/test_knowledge_review_surface.py:92-92 |
| The config that names no real root, so only the resolution's own refusals can answer. | `review_config` | mcp/tests/test_knowledge_review_surface.py:122-130 |
| The fresh two-snapshot fixture per case, and the resolution assembled without a contract so the composition can be driven without a coordination tree. | `fixture`; `resolution_for` | mcp/tests/test_knowledge_review_surface.py:133-152 |
| The one request shape and the one failing-loudly render helper every pane case goes through. | `review_request`; `render` | mcp/tests/test_knowledge_review_surface.py:155-183 |
| The three input builders that produce records through the seams that own them rather than by constructing stored rows. | `published_assessment`; `observation`; `signal` | mcp/tests/test_knowledge_review_surface.py:186-301 |
| The shipped two-snapshot support the whole module is built on. | `build_diff_fixture`; `DiffFixture` | mcp/tests/diff_scope_test_support.py:148-232 |
| The pane cases: the subject's own statements and the comparison's own facts, the unchanged sibling and the removed claim's before-side, and the counts the selection did not reach. | `test_the_knowledge_pane_renders_the_subjects_own_statements_and_the_comparisons_own_facts`; `test_the_source_pane_shows_the_unchanged_sibling_and_the_removed_claims_before_side`; `test_the_source_pane_counts_the_unmapped_path_and_the_records_outside_the_selection` | mcp/tests/test_knowledge_review_surface.py:302-356; mcp/tests/test_knowledge_review_surface.py:357-370; mcp/tests/test_knowledge_review_surface.py:371-386 |
| **The missing-role boundary asserted at the display: unclassified, never guessed from a name.** | `test_a_missing_role_stays_unclassified_and_is_never_guessed_from_a_name` | mcp/tests/test_knowledge_review_surface.py:387-404 |
| **The whole-schema walk for a field a generated conclusion could occupy, and the case that the vocabulary defines no record kind, table or status of its own.** | `walk_property_names`; `test_the_whole_payload_schema_has_no_field_a_generated_conclusion_could_occupy`; `test_the_surface_defines_no_record_kind_no_table_and_no_status_of_its_own` | mcp/tests/test_knowledge_review_surface.py:405-429; mcp/tests/test_knowledge_review_surface.py:430-439 |
| **The stores-nothing case, measured as the two datasets' row counts being identical across a full render.** | `test_the_surface_stores_nothing_so_deleting_every_rendering_loses_no_canonical_information` | mcp/tests/test_knowledge_review_surface.py:440-452 |
| **The selects-nothing case, comparing the payload's identity and counts against the shipped comparison value for value.** | `test_the_adapter_selects_nothing_because_the_shipped_comparison_is_the_comparison_rendered` | mcp/tests/test_knowledge_review_surface.py:453-504 |
| The state cases: unassessed is unassessed; no evidence records reads `none_recorded` with source inspection still available; a passing observation is never invariant-satisfied; a signal carries no severity. | `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible`; `test_a_passing_observation_is_displayed_as_an_observation_and_never_as_invariant_satisfied`; `test_a_detection_signal_carries_its_facts_and_scope_limitations_and_no_severity` | mcp/tests/test_knowledge_review_surface.py:505-529; mcp/tests/test_knowledge_review_surface.py:532-547; mcp/tests/test_knowledge_review_surface.py:550-566 |
| **The staleness pair, asserted from both directions, plus the absent-submission-path case.** | `test_the_stale_rule_holds_in_both_directions`; `test_the_surface_reports_the_absent_submission_path_instead_of_growing_a_private_one` | mcp/tests/test_knowledge_review_surface.py:569-590; mcp/tests/test_knowledge_review_surface.py:593-602 |
| The unresolved-author case and the missing-side case, both refusals rather than renderings. | `test_an_item_whose_author_is_not_published_is_shown_as_an_unresolved_reference`; `test_a_missing_side_is_its_own_state_and_never_an_empty_string` | mcp/tests/test_knowledge_review_surface.py:605-618; mcp/tests/test_knowledge_review_surface.py:621-632 |
| The two-disagreeing-assessments case and the measured matching-binding case: the currentness axis from both directions. | `test_two_disagreeing_assessments_are_both_displayed_with_their_authors_and_no_resolution`; `test_a_measured_matching_binding_reports_the_assessment_current` | mcp/tests/test_knowledge_review_surface.py:638-664; mcp/tests/test_knowledge_review_surface.py:667-674 |
| **The worked review of the design's §8 journey, and the case that closes it: a stale assessment is never reused.** | `test_the_worked_review_journey_renders_every_step_it_walks`; `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate` | mcp/tests/test_knowledge_review_surface.py:680-705; mcp/tests/test_knowledge_review_surface.py:708-723 |
| The two resolution cases: the candidate comes from task context rather than a browser-chosen path, and an absent dataset refuses by name. | `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`; `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` | mcp/tests/test_knowledge_review_surface.py:729-742; mcp/tests/test_knowledge_review_surface.py:745-764 |
| The two transport cases: exactly the two reviewable selector kinds are admitted, and the route refuses by name with no adapter. | `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds`; `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` | mcp/tests/test_knowledge_review_surface.py:767-783; mcp/tests/test_knowledge_review_surface.py:786-842 |
| The loader case and the pane-name case. | `test_the_published_assessment_loader_returns_nothing_for_an_unresolvable_candidate`; `test_the_rendered_pane_types_are_the_three_the_design_names` | mcp/tests/test_knowledge_review_surface.py:845-855; mcp/tests/test_knowledge_review_surface.py:858-872 |
| The lane row this module occupies. | "mcp/tests/test_knowledge_review_surface.py" | mcp/tests/test-evidence-lanes.toml:100-108 |
| The two consumer registrations this module's fixtures are recorded under. | "mcp/tests/test_knowledge_review_surface.py" | mcp/tests/evidence-lifecycle.toml:1385-1425 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds its datasets under
`tmp_path` and asserts one repository namespace's rendering.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T00:56+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 10 enforced citation rows this card carried (citation_anchor_absent_from_range, citation_range_out_of_bounds). Every row was re-read against the source rather than trusted from the item's cited text: the six first ranges the earlier mechanical projection had repointed were verified current and left untouched, while that projection's rewritten first range had opened a gap in each row and left the *second* range stale, so those six were repointed to the construct each claim names — `test_a_missing_side_is_its_own_state_and_never_an_empty_string` 621-632, `test_a_measured_matching_binding_reports_the_assessment_current` 667-674, `test_a_stale_assessment_is_never_reused_as_a_review_of_the_new_candidate` 708-723, `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` 745-764, `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` 786-842, `test_the_rendered_pane_types_are_the_three_the_design_names` 858-872 (the last also clearing the out-of-bounds 863-877). Two claims name cases that were merged upstream, so they were re-cited to the surviving case that carries the fact: `test_no_evidence_records_reads_none_recorded_with_source_inspection_still_available` is asserted inside `test_an_unassessed_subject_is_displayed_unassessed_and_never_defaulted_to_compatible` (505-529), and the staleness pair inside `test_the_stale_rule_holds_in_both_directions` (569-590). No claim wording was changed, every other range is untouched, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 6 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `test_an_item_whose_author_is_not_published_is_shown_as_an_unresolved_reference`; `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`; `test_the_published_assessment_loader_returns_nothing_for_an_unresolvable_candidate`; `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds`; `test_the_worked_review_journey_renders_every_step_it_walks`; `test_two_disagreeing_assessments_are_both_displayed_with_their_authors_and_no_resolution`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's case module. It records the module's four load-bearing properties — the surface **stores nothing**, **selects nothing**, has **no field a generated conclusion could occupy**, and renders every refusal state as a state — each pinned by one case, plus the worked review of `retrieval-review-design.md` §8's journey. It also records that the lane declaration is a **precondition** rather than metadata (an unregistered module makes the lane manifest refuse the repository), the two declared vocabularies (`REPOSITORY_LEAF`, `FORBIDDEN_FIELD_NAMES`), the helpers that build the fixture's three record collections through the shipped seams rather than by inserting stored rows, and the fact that no case re-implements the read, the comparison or the view it measures. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
