# mcp/tests/test_knowledge_routes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_routes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T22:00+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's scope: one rule per case, and constructor validation deliberately not re-tested. | "Constructor validation is not re-tested here" | mcp/tests/test_knowledge_routes.py:1-7 |
| The initialized generation-2 candidate, its store and its authored provenance used by every case. | `admitted` | mcp/tests/test_knowledge_routes.py:27-42 |
| The one authoring helper and the draft it wraps. | `_author`; `RouteDraft` | mcp/tests/test_knowledge_routes.py:45-51; mcp/src/agents_remember/memory/knowledge/routes.py:170-176 |
| A confined path is authored and its identity returned. | `test_a_confined_path_is_authored_and_its_identity_returned` | mcp/tests/test_knowledge_routes.py:54-57 |
| One scope keeps one route when the same spelling is restated, measured by a row count. | `test_one_scope_keeps_one_route_when_the_same_spelling_is_restated` | mcp/tests/test_knowledge_routes.py:60-68 |
| Ten refused spellings, each `invalid_reference` with nothing written. | `test_a_path_outside_the_one_admitted_form_is_refused` | mcp/tests/test_knowledge_routes.py:71-91 |
| An authored parent yields an acyclic hierarchy; an unauthored parent is `missing_expected_row`. | `test_a_child_names_an_authored_parent_and_the_hierarchy_stays_acyclic`; `test_a_child_naming_an_unauthored_parent_is_refused` | mcp/tests/test_knowledge_routes.py:94-99; mcp/tests/test_knowledge_routes.py:102-106 |
| A cycle introduced by a direct UPDATE is still refused as `lineage_cycle`. | `test_a_hierarchy_that_reaches_itself_is_refused` | mcp/tests/test_knowledge_routes.py:109-120 |
| At most one governing route per governed row: association, idempotent restatement, and the conflict refusal that keeps the first route. | `test_a_governed_row_names_at_most_one_governing_route` | mcp/tests/test_knowledge_routes.py:123-167 |
| An ungoverned row reports ungoverned rather than a repository root. | `test_an_ungoverned_row_reports_ungoverned_rather_than_a_repository_root` | mcp/tests/test_knowledge_routes.py:170-177 |
| The two remaining refusals: a non-governed table and an unauthored route. | `test_governing_refuses_an_unknown_governed_table_and_an_unauthored_route` | mcp/tests/test_knowledge_routes.py:180-199 |
| The write layer under test: authoring, the read side, the association, and the governed-table mapping that makes the constraint a table key. | `author_route`; `find_governing_route`; `set_governing_route`; `_GOVERNED_TABLES` | mcp/src/agents_remember/memory/knowledge/routes.py:225-279; mcp/src/agents_remember/memory/knowledge/routes.py:282-301; mcp/src/agents_remember/memory/knowledge/routes.py:304-392; mcp/src/agents_remember/memory/knowledge/routes.py:195-199 |
| The confinement rule and the cycle walk the refused cases exercise. | `normalize_route_path`; `require_acyclic_routes` | mcp/src/agents_remember/memory/knowledge/routes.py:75-89; mcp/src/agents_remember/memory/knowledge/routes.py:92-144 |
| The drafts the cases construct. | `GoverningRouteDraft` | mcp/src/agents_remember/memory/knowledge/routes.py:179-185 |
| The application entry points the fixture uses to build an initialized candidate and its provenance. | `admitted_knowledge_destination`; `initialize_knowledge_namespace`; `open_admitted_knowledge_store`; `write_authorship` | mcp/src/agents_remember/application/knowledge.py:125; mcp/src/agents_remember/application/knowledge.py:160; mcp/src/agents_remember/application/knowledge.py:193; mcp/src/agents_remember/application/knowledge.py:102 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-17T22:00+02:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`; the module is untracked in the leaf's code worktree): created this one-to-one card for the route write-layer case module. It records the initialized-candidate fixture, the refused-spelling table that also asserts nothing was written, the cycle introduced outside the authoring path, and the three facts the governing-association case measures (association, idempotent restatement, conflict refused with the first route retained).
