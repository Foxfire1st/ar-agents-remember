# mcp/tests/test_knowledge_routes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_routes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T18:47+02:00 |
| lastVerifiedCommitHash | `7dcec036094768c5f50e571fb45e59a27ae78efc`|
| lastVerifiedCommitDate | 2026-09-19T18:19:12+02:00|
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
| An ungoverned row reports ungoverned rather than a repository root. | `test_an_ungoverned_row_reports_ungoverned_rather_than_a_repository_root` | mcp/tests/test_knowledge_routes.py:178-185 |
| The two remaining refusals: a non-governed table and an unauthored route. | `test_governing_refuses_an_unknown_governed_table_and_an_unauthored_route` | mcp/tests/test_knowledge_routes.py:276-297 |
| The write layer under test: authoring, the read side, the association, and the governed-table mapping that makes the constraint a table key. | `author_route`; `find_governing_route`; `set_governing_route`; `_GOVERNED_TABLES` | mcp/src/agents_remember/memory/knowledge/routes.py:238-292; mcp/src/agents_remember/memory/knowledge/routes.py:295-341; mcp/src/agents_remember/memory/knowledge/routes.py:398-480; mcp/src/agents_remember/memory/knowledge/routes.py:199-203 |
| The confinement rule and the cycle walk the refused cases exercise. | `normalize_route_path`; `require_acyclic_routes` | mcp/src/agents_remember/memory/knowledge/routes.py:75-89; mcp/src/agents_remember/memory/knowledge/routes.py:92-144 |
| The drafts the cases construct. | `GoverningRouteDraft` | mcp/src/agents_remember/memory/knowledge/routes.py:193-199 |
| The application entry points the fixture uses to build an initialized candidate and its provenance. | `admitted_knowledge_destination`; `initialize_knowledge_namespace`; `open_admitted_knowledge_store`; `write_authorship` | mcp/src/agents_remember/application/knowledge.py:117-125; mcp/src/agents_remember/application/knowledge.py:160; mcp/src/agents_remember/application/knowledge.py:193; mcp/src/agents_remember/application/knowledge.py:102-140 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `GoverningRouteDraft` repointed to mcp/src/agents_remember/memory/knowledge/routes.py:193-199. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T18:47+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **re-read this card against its source at code `c5a74a85` and found the body already current; advanced the verification stamp to that revision, which closeout re-stamps.** The source delta since the old stamp is five added `assert isinstance(x, str)` lines — type-narrowing assertions inside four existing cases (`test_a_child_names_an_authored_parent_and_the_hierarchy_stays_acyclic`, `test_a_hierarchy_that_reaches_itself_is_refused`, `test_a_governed_row_names_at_most_one_governing_route`, and the governing-column case). They add **no case, no refusal and no behaviour**: each only narrows a helper's declared return before it is passed on, so every case description in the body above still says what the case does, and the conventions row that already states "each negative case asserts `isinstance`/code" is unaffected. **No content impact:** no claim byte was rewritten and nothing was added to fit the stamp.
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 1 claim(s) here (1 x citation_provenance_invalid). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand** — `test_an_ungoverned_row_reports_ungoverned_rather_than_a_repository_root`, `test_governing_refuses_an_unknown_governed_table_and_an_unauthored_route`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; their claims' ranges were **re-verified by hand against the current source in this pass** and repaired where this leaf's addition moved them, so a mechanically projected range is no longer the only evidence any of these claims carries. Nothing in the body above was deleted to clear a finding.

- 2026-09-17T20:00:00+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`; the module is untracked in the leaf's code worktree): created this one-to-one card for the route write-layer case module. It records the initialized-candidate fixture, the refused-spelling table that also asserts nothing was written, the cycle introduced outside the authoring path, and the three facts the governing-association case measures (association, idempotent restatement, conflict refused with the first route retained).
