# mcp/tests/test_knowledge_review_resolution_and_route.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose
Checks canonical task-context review resolution and typed entry-route results using the current converted fixture.

## Code Commentary
The route cannot accept a browser-chosen candidate path. Missing or unreadable before/candidate halves refuse by name without a substitute; the entry returns the typed refusal instead of raising. Only the two declared selectors are transported, previous binding identity reaches the port, and an absent adapter or unresolvable candidate is explicit. Removed local entry-master/config helpers are not fixture ownership. Test names retaining historical dataset wording do not restore canonical dataset writes, and no run is claimed.

### Logic
**`review_config` names no real root, so only the resolution's own refusals can answer.** It is imported
from the surface module. The task-context resolution case uses it to measure the resolver's
refusals rather than a host repository.

**The transport cases go through the real route.** They register `register_review_routes` on a bare
`FastAPI` app and drive it through `TestClient`, so the route's own status idiom is measured: `200`
for a typed result, `400` for a malformed request and `503` with no adapter. The selector case calls
`review_request_from_query` directly: an invariant or a family identity is admitted, and `path`,
`invariant_revision`, an empty kind and `latest` are refused. The surface card records that
`260921-ICR-L2` extended this case with the selector-less answer. The case as moved does not assert it,
and was the same at the base. The selector-less route is measured by
`test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all` in the
source-endpoints module.

**The previous-identity case measures one property per hop (`260921-ICR-L17`).**
`test_the_previous_binding_identity_reaches_the_port_and_is_compared_against_the_read` registers the
real routes over a bare `FastAPI` app and drives three requests through `TestClient`:

- a **refresh**: the transport admits `previousBindingDigest`, hands it to the port on the request (the
  case asserts `asked[-1].previous_binding_digest == previous` rather than trusting the route), and the
  composition answers `staleness.state == "stale"` with `previous_comparison_ref` equal to the carried
  value and `submission.state == "disabled_stale"` — while `comparison.binding_digest` is **not** the
  carried value, which is the assertion that the previous identity never becomes the current one;
- a **plain read**: nothing carried, `previous_binding_digest is None` at the port, `staleness.state ==
  "current"` — current by construction rather than by assumption;
- a **malformed spelling**: `400` with `offendingInput == "not-a-digest"`, which is the transport's own
  vocabulary refusal rather than an uncaught model validation error.

It depends on the surface module's `render`, which puts the previous identity on the request with
`model_copy` the way a refresh does.

### Conventions
Marked `pytest.mark.evidence_unit`. The module defines its own three-line `fixture` over
`build_diff_fixture` rather than importing the surface module's, because an imported fixture would
shadow a parameter and hide fixture discovery. It imports the resolver,
`list_knowledge_review_entries` and the transport (`register_review_routes`, `review_request_from_query`)
directly.

### Invariants And Boundaries
- **No resolution is faked where the resolver is the subject.** The resolution cases use a config that
  names no real root; the before-half composition cases assemble a resolution only to make one side
  deliberately unusable.
- **Catalog footprint.** The module reaches `diff_scope_test_support.py` and `read_scope_test_support.py`
  through its imports. It is declared on both artifacts' exact `consumers` rows beside its sibling, and
  registers no artifact of its own.

### Todos
None.

## Evidence

### Repo-Internal References



### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds its datasets under
`tmp_path`.

No meaningful cross-repo references found.

- `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path` owns the current boundary described above. [13]
- `test_the_entry_route_refuses_a_damaged_before_half_instead_of_raising` owns the current boundary described above. [14]
- `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds` owns the current boundary described above. [15]
- `test_the_previous_binding_identity_reaches_the_port_and_is_compared_against_the_read` owns the current boundary described above. [16]
> Retained earlier citation wording: - The module's own statement of the boundary it measures, and the import of the surface helpers it reuses. [17]
> Retained earlier citation wording: - The unit marker and the per-case fixture. [18]
> Retained earlier citation wording: - The surface module's config that names no real root, and the render helper that puts the previous identity on the request. [19]
- **The absent before half refuses by name and the refused review creates nothing: the sibling leaf `260921-ICR-L5`'s case beside the absent-candidate one above, differing in *which* half is missing — the two halves are different facts and have different next actions.** [21]
- **The corrupt before half is a typed refusal rather than an `apsw.NotADBError` raised from inside the read, and the refusal names the baseline rather than the candidate — only one of the two sides can be repaired by authoring knowledge again.** [22]
- **The previous identity driven through every hop: carried by a refresh to the port and compared, absent on a plain read, and refused by name when malformed.** [24]
> Retained earlier citation wording: - The unit-regression lane row, beside its sibling's.  Anchor: `test_knowledge_review_resolution_and_route` [26]

- Task-context resolution refuses path-shaped or unresolved candidates; the separate absent-candidate composition case refuses with candidate_dataset_absent. [20]
- The selector test admits the two reviewable kinds and refuses invalid spellings; the route test serves typed results and names an absent adapter. [23]

- The unit-regression lane row, beside its sibling's.  Anchor: `test_knowledge_review_resolution_and_route` [26]

- The module's own statement of the boundary it measures, and the import of the surface helpers it reuses. [17]


- The unit marker and the per-case fixture. [18]


- The surface module's config that names no real root, and the render helper that puts the previous identity on the request. [19]
