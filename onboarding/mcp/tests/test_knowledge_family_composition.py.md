# mcp/tests/test_knowledge_family_composition.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_family_composition.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:30+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a`|
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

The composition leaf's **unit-regression suite** for generation 5 and the authored record group:
eighteen cases covering the closed command union, the value-boundary policy validation, the appended
generation, a dataset that predates the composition tables, the authored edge and its immutability,
the declared unique tuple, the revision-altitude owning route, the explanatory context, and the one
shared cycle rule applied at both check levels.

Every case protects a clause of `KS-R17@v1` §1 through §6 and §9. The suite's load-bearing cases are
the ones that would catch a **silent widening** rather than a crash:

- an endpoint that could hold an invariant revision or an arbitrary record (**unrepresentable**, not
  merely rejected);
- a relationship inferred from a path, a label or a shared member;
- a silent second cycle rule beside the shared one;
- a policy that widens without a bound or a named scope;
- a context that rewrites the guarantee or is edited in place.

The module is registered as a **unit-regression** row in `mcp/tests/test-evidence-lanes.toml` and as
a **consumer** of three registered evidence contracts in `mcp/tests/evidence-lifecycle.toml`
(`knowledge-facet-cases`, `knowledge-generation-cases` and `knowledge-read-scope-cases`). It builds
its admitted candidate through the existing shared support modules — it adds **no** new fixture, no
new contract and no new artifact, so the catalogue's counts stay at **13 contracts / 54 artifacts**.

## Code Commentary

### Logic

- The **generation case** asserts `CURRENT_GENERATION is GENERATION_5`,
  `descends_from(GENERATION_5, GENERATION_4, GENERATION_4.tables)` and the six appended names **by
  name**, so a renumber is a rename in that case too rather than a rewrite.
- The **predating-dataset case** creates genuine generation-2 and generation-4 stores through their
  own recorded DDL and refuses a composition write against them; it uses
  `create_recorded_generation_store` with the registry's own constants, so the created-generation
  assertion follows the registry rather than a literal.
- The **union case** asserts the four command kinds and the six record tables from the leaf's own
  published constants, and that the six tables declare no content-address column.
- The **cycle cases** drive the shared rule at both check levels and assert that **no second walk and
  no `WITH RECURSIVE`** exists in any composition DDL.
- The **immutability case** drives three tables and five statements past the write path and proves the
  database refuses them.

### Conventions

- Hermetic: temporary directories and in-process APSW databases driven through the real admitted
  destination — no integration marker, no repository working tree, no subprocess — which is why the
  default unit lane is this module's behaviour-preserving classification.
- **Always run with `-o "filterwarnings=ignore"` on this host**: without it five modules fail to
  collect because `DeprecationWarning: The anyio.abc.BlockingPortal alias is deprecated` is raised as
  an error. That is a pre-existing, documented host condition, not this leaf's.
- Preservation comparisons are made **by value and by digest**, never by inspection.

### Invariants And Boundaries

- **No case deletes, skips, deselects or weakens a shipped assertion.** The two shipped assertions
  this leaf touched live in `test_knowledge_facets.py` and were re-scoped upward, not loosened.
- **The suite governs no durable artifact**: it creates no fixture, generator, recording or migration
  proof, and it carries no catalog row of its own.
- **Boundary.** The retrieval-read boundary and the projection cases are the sibling module's; this
  one owns the write shape and the generation.

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
| **The generation case: the six appended names, `descends_from` against generation 4, and the created generation.** | "test_the_registered_generation_appends_the_six_tables_to_the_generation_it_descends_from" | mcp/tests/test_knowledge_family_composition.py:376-376 |
| **The case that opens genuine generation-2 and generation-4 datasets and refuses a composition write against them — no migration path exists.** | "test_a_dataset_predating_the_composition_tables_refuses_a_composition_write" | mcp/tests/test_knowledge_family_composition.py:411-411 |
| **The case that proves a wrong endpoint kind is unrepresentable rather than merely rejected, and that the DDL carries exactly two family-revision keys and no target column.** | "test_every_non_family_endpoint_kind_is_unrepresentable_rather_than_merely_rejected" | mcp/tests/test_knowledge_family_composition.py:516-516 |
| The case that pins the union's membership from the leaf's published constants. | "test_the_composition_commands_are_the_closed_unions_own_members" | mcp/tests/test_knowledge_family_composition.py:245-245 |
| **The case that drives three authored tables past the write path and proves the database refuses an update and a delete.** | "test_an_authored_edge_a_policy_and_a_context_are_immutable_at_the_database" | mcp/tests/test_knowledge_family_composition.py:606-606 |
| **The case that proves the one shared rule judges the composition graph at both check levels, rolling back with its revision ids.** | "test_one_shared_rule_judges_the_composition_graph_at_both_check_levels" | mcp/tests/test_knowledge_family_composition.py:925-925 |
| **The case that asserts no second cycle walk and no recursive CTE exists beside the shared rule.** | "test_no_second_cycle_implementation_exists_beside_the_shared_rule" | mcp/tests/test_knowledge_family_composition.py:1005-1005 |
| The case that proves a context whose subject is not a family revision is refused. | "test_a_context_whose_subject_is_not_a_family_revision_is_refused" | mcp/tests/test_knowledge_family_composition.py:893-893 |
| The case that proves an edge with no declared policy is stored, readable and not traversable. | "test_an_edge_with_no_declared_policy_is_stored_readable_and_not_traversable" | mcp/tests/test_knowledge_family_composition.py:453-453 |
| The lane row this module is registered under, and the unit ceiling it is measured against. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |
| The one contract whose consumer list this module joined for its admitted candidate. | "contract:knowledge-facet-cases" | mcp/tests/evidence-lifecycle.toml:1339-1339 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: "contract:knowledge-facet-cases" repointed to mcp/tests/evidence-lifecycle.toml:1339-1339. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T03:57:45+00:00: Generated citation repair: "contract:knowledge-facet-cases" repointed to mcp/tests/evidence-lifecycle.toml:1341-1341. No content impact: mechanical anchor-range projection bound to citation source snapshot ef4a9932e0393a408ecd0f26b5bc2e0e1e335ad90b9e47a16092ffd6f3403af3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T00:16:01+00:00: Generated citation repair: "contract:knowledge-facet-cases" repointed to mcp/tests/evidence-lifecycle.toml:1339-1339. No content impact: mechanical anchor-range projection bound to citation source snapshot b8fe5b3589f1357e836aaad1587e69ed38bbda0d58221eaa2150e96eb0561e93; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "contract:knowledge-facet-cases" repointed to mcp/tests/evidence-lifecycle.toml:1337-1337. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T20:45:09+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **cleared the 1 enforced `citation_anchor_absent_from_range` row in this document.** The closeout's own code commit appended one `consumers` registration above every construct these cards cite, so each cited range ended exactly one line above the line that now carries the anchor row. Widened to the carrying line: `mcp/tests/evidence-lifecycle.toml:1333-1333` → `mcp/tests/evidence-lifecycle.toml:1333-1334` (row 106). Every line the author cited stays inside its range; no claim, Anchor cell or other range was dropped or re-worded, and each named anchor now resolves inside the widened range.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_the_registered_generation_appends_the_six_tables_to_the_generation_it_descends_from" repointed to mcp/tests/test_knowledge_family_composition.py:376-376. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_dataset_predating_the_composition_tables_refuses_a_composition_write" repointed to mcp/tests/test_knowledge_family_composition.py:411-411. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_every_non_family_endpoint_kind_is_unrepresentable_rather_than_merely_rejected" repointed to mcp/tests/test_knowledge_family_composition.py:516-516. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_the_composition_commands_are_the_closed_unions_own_members" repointed to mcp/tests/test_knowledge_family_composition.py:245-245. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_an_authored_edge_a_policy_and_a_context_are_immutable_at_the_database" repointed to mcp/tests/test_knowledge_family_composition.py:606-606. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_one_shared_rule_judges_the_composition_graph_at_both_check_levels" repointed to mcp/tests/test_knowledge_family_composition.py:925-925. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_no_second_cycle_implementation_exists_beside_the_shared_rule" repointed to mcp/tests/test_knowledge_family_composition.py:1005-1005. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_context_whose_subject_is_not_a_family_revision_is_refused" repointed to mcp/tests/test_knowledge_family_composition.py:893-893. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_an_edge_with_no_declared_policy_is_stored_readable_and_not_traversable" repointed to mcp/tests/test_knowledge_family_composition.py:453-453. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-facet-cases" repointed to mcp/tests/evidence-lifecycle.toml:1333-1333. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-facet-cases" repointed to mcp/tests/evidence-lifecycle.toml:1329-1329. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_one_shared_rule_judges_the_composition_graph_at_both_check_levels" repointed to mcp/tests/test_knowledge_family_composition.py:900-900. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_no_second_cycle_implementation_exists_beside_the_shared_rule" repointed to mcp/tests/test_knowledge_family_composition.py:980-980. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_a_context_whose_subject_is_not_a_family_revision_is_refused" repointed to mcp/tests/test_knowledge_family_composition.py:868-868. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-facet-cases" repointed to mcp/tests/evidence-lifecycle.toml:1325-1325. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-facet-cases" repointed to mcp/tests/evidence-lifecycle.toml:1223-1223. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_the_registered_generation_appends_the_six_tables_to_the_generation_it_descends_from" repointed to mcp/tests/test_knowledge_family_composition.py:351-351. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_a_dataset_predating_the_composition_tables_refuses_a_composition_write" repointed to mcp/tests/test_knowledge_family_composition.py:386-386. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_every_non_family_endpoint_kind_is_unrepresentable_rather_than_merely_rejected" repointed to mcp/tests/test_knowledge_family_composition.py:491-491. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_the_composition_commands_are_the_closed_unions_own_members" repointed to mcp/tests/test_knowledge_family_composition.py:244-244. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_an_authored_edge_a_policy_and_a_context_are_immutable_at_the_database" repointed to mcp/tests/test_knowledge_family_composition.py:581-581. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_one_shared_rule_judges_the_composition_graph_at_both_check_levels" repointed to mcp/tests/test_knowledge_family_composition.py:895-895. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_no_second_cycle_implementation_exists_beside_the_shared_rule" repointed to mcp/tests/test_knowledge_family_composition.py:973-973. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_a_context_whose_subject_is_not_a_family_revision_is_refused" repointed to mcp/tests/test_knowledge_family_composition.py:863-863. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_an_edge_with_no_declared_policy_is_stored_readable_and_not_traversable" repointed to mcp/tests/test_knowledge_family_composition.py:428-428. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:30:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 9 generated projection bullet(s) by hand** — `test_a_context_whose_subject_is_not_a_family_revision_is_refused`, `test_a_dataset_predating_the_composition_tables_refuses_a_composition_write`, `test_an_authored_edge_a_policy_and_a_context_are_immutable_at_the_database`, `test_an_edge_with_no_declared_policy_is_stored_readable_and_not_traversable`, `test_every_non_family_endpoint_kind_is_unrepresentable_rather_than_merely_rejected`, `test_no_second_cycle_implementation_exists_beside_the_shared_rule`, `test_one_shared_rule_judges_the_composition_graph_at_both_check_levels`, `test_the_composition_commands_are_the_closed_unions_own_members`, `test_the_registered_generation_appends_the_six_tables_to_the_generation_it_descends_from`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.

- 2026-09-18T06:06:32+00:00: Generated citation repair: "contract:knowledge-facet-cases" repointed to mcp/tests/evidence-lifecycle.toml:1220-1220. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T04:30:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): created this one-to-one card for the composition leaf's first case module. This seat re-read the module against the candidate and **corrected the record rather than repeating the builder's**: the suite collects **26** cases in total across the two modules, and this module's own top-level cases number **eighteen**; one consequence of the count being what it is, stated here because the distinction matters, is that the projection's own assertions are driven inside the sibling boundary module's application-seam case rather than by separate cases. The card records the two registered rails (the unit-regression lane row and the three evidence-contract consumer entries, with **no** new fixture, contract or artifact, so counts stay 13 / 54), the hermetic classification that makes the unit lane behaviour-preserving, and the host's required `-o "filterwarnings=ignore"` override. Verification metadata is the leaf's base commit `e963a01c`: the code commit does not exist yet and closeout owns that stamp.
