# mcp/tests/test_knowledge_routes.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

The focused case module for the route **write layer**: authoring a route, the confinement rule over its path, and the
governing association between a governed generation-1 row and the route that governs it. Its docstring states what each
case protects — one rule that makes `Route` an operable scope axis rather than a declaration — and it states the
boundary too: constructor validation is not re-tested here.

## Code Commentary

### Logic

An `admitted` fixture builds one initialized candidate through the application layer: `admitted_knowledge_destination`
with a repository identity and `write_authorship(actor_ref="agent:routes", authorization_ref="260915-KS developer
kickoff ruling", origin_refs=("requirement:KS-R10@v1",))`, then `initialize_knowledge_namespace`, then
`open_admitted_knowledge_store` held for the duration of the case. The docstring calls it one initialized generation-2
candidate, its store and its authored provenance, so every case runs against a real initialized store rather than a bare
connection. `_author` is the module's one helper: it wraps `routes.author_route` over a `RouteDraft`, defaulting the
route id to a fresh UUID.

- `test_a_confined_path_is_authored_and_its_identity_returned` is the admitted case: authoring a confined path returns
  the route id it was given.
- `test_one_scope_keeps_one_route_when_the_same_spelling_is_restated` measures the de-duplication: a second authoring
  call for an already-authored path returns the first route's id even though it names a different id, and a direct
  count over `route` filtered by that path shows exactly one row.
- `test_a_path_outside_the_one_admitted_form_is_refused` is parametrized over ten spellings (empty, absolute, backslash,
  drive form, UNC form, traversal, dot segment, doubled separator, trailing separator, embedded NUL). Each returns a
  non-`str` refusal with code `invalid_reference`, and the case then asserts the `route` table is still empty — the
  refusal wrote nothing.
- `test_a_child_names_an_authored_parent_and_the_hierarchy_stays_acyclic` authors a parent and a child naming it, then
  asserts `require_acyclic_routes` returns `None`.
- `test_a_child_naming_an_unauthored_parent_is_refused` measures the other direction: a random parent id yields
  `missing_expected_row`.
- `test_a_hierarchy_that_reaches_itself_is_refused` introduces the cycle by a direct `UPDATE` of `parent_route_id`
  rather than through authoring, and still gets a `lineage_cycle` refusal — the docstring's point that a cycle is
  refused however it arrives, not only through the authoring path.
- `test_a_governed_row_names_at_most_one_governing_route` authors an invariant through the store's own
  `create_invariant`, authors two routes, associates the invariant with the first, and then measures three facts: the
  association reads back as the first route, restating the same association is idempotent (`None`), and naming the
  second route returns a `relationship_constraint` refusal while `find_governing_route` still reports the first.
- `test_an_ungoverned_row_reports_ungoverned_rather_than_a_repository_root` asserts an unassociated governed id reads
  back as `None` — an explicit "ungoverned" fact rather than an implicit repository root.
- `test_governing_refuses_an_unknown_governed_table_and_an_unauthored_route` covers the two remaining refusals:
  governing a table outside the governed set is `invalid_reference`, and naming a route that was never authored is
  `missing_expected_row`.

### Conventions

- Every write goes through the route module's public entry points (`author_route`, `set_governing_route`) or the store's
  own operation (`create_invariant`); only the deliberate cycle case writes SQL directly, and it does so to prove the
  check is not an authoring-path artifact.
- Refusals are values, not exceptions, so each negative case asserts `isinstance`/code rather than catching.
- The fixture supplies the store, the repository id and the authorship envelope; cases never build their own candidate
  or invent provenance.
- Negative path cases assert both the refusal code and the absence of a written row, so "refused" means "nothing
  stored", not merely "returned something".

### Invariants And Boundaries

- **A path that is not in the one admitted form is refused, never rewritten**, so two spellings of one path cannot
  become two routes; and an already-authored scope returns its existing route rather than a second row.
- **A governed row names at most one governing route.** That is a constraint of the join table's key, and this module
  measures the operational consequences: restatement is idempotent, and a conflicting route is refused instead of
  silently overwriting the existing association.
- **An unauthored parent, an unauthored route, a missing governed row and a non-governed table are all refusals**, never
  implicitly created — scope is a recorded input.
- **Boundary.** The module tests the write layer's own behaviour; the generation-2 DDL shape, the confinement rule's
  error surface and the acyclicity walk are also exercised at the declaration level in
  `test_knowledge_merge_generations_and_envelope.py`, and constructor validation of the drafts is deliberately out of
  scope here.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module's scope: one rule per case, and constructor validation deliberately not re-tested. [1]
- The initialized generation-2 candidate, its store and its authored provenance used by every case. [2]
- The one authoring helper and the draft it wraps. [3]
- A confined path is authored and its identity returned. [4]
- One scope keeps one route when the same spelling is restated, measured by a row count. [5]
- Ten refused spellings, each `invalid_reference` with nothing written. [6]
- An authored parent yields an acyclic hierarchy; an unauthored parent is `missing_expected_row`. [7]
- A cycle introduced by a direct UPDATE is still refused as `lineage_cycle`. [8]
- At most one governing route per governed row: association, idempotent restatement, and the conflict refusal that keeps the first route. [9]
- An ungoverned row reports ungoverned rather than a repository root. [10]
- The two remaining refusals: a non-governed table and an unauthored route. [11]
- The write layer under test: authoring, the read side, the association, and the governed-table mapping that makes the constraint a table key. [12]
- The confinement rule and the cycle walk the refused cases exercise. [13]
- The drafts the cases construct. [14]
- The application entry points the fixture uses to build an initialized candidate and its provenance. [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
