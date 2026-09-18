# mcp/tests/test_knowledge_family_composition.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_family_composition.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:30+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be`|
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
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
| **The generation case: the six appended names, `descends_from` against generation 4, and the created generation.** | "test_the_registered_generation_appends_the_six_tables_to_the_generation_it_descends_from" | mcp/tests/test_knowledge_family_composition.py:347-347 |
| **The case that opens genuine generation-2 and generation-4 datasets and refuses a composition write against them — no migration path exists.** | "test_a_dataset_predating_the_composition_tables_refuses_a_composition_write" | mcp/tests/test_knowledge_family_composition.py:379-379 |
| **The case that proves a wrong endpoint kind is unrepresentable rather than merely rejected, and that the DDL carries exactly two family-revision keys and no target column.** | "test_every_non_family_endpoint_kind_is_unrepresentable_rather_than_merely_rejected" | mcp/tests/test_knowledge_family_composition.py:480-480 |
| The case that pins the union's membership from the leaf's published constants. | "test_the_composition_commands_are_the_closed_unions_own_members" | mcp/tests/test_knowledge_family_composition.py:243-243 |
| **The case that drives three authored tables past the write path and proves the database refuses an update and a delete.** | "test_an_authored_edge_a_policy_and_a_context_are_immutable_at_the_database" | mcp/tests/test_knowledge_family_composition.py:570-570 |
| **The case that proves the one shared rule judges the composition graph at both check levels, rolling back with its revision ids.** | "test_one_shared_rule_judges_the_composition_graph_at_both_check_levels" | mcp/tests/test_knowledge_family_composition.py:884-884 |
| **The case that asserts no second cycle walk and no recursive CTE exists beside the shared rule.** | "test_no_second_cycle_implementation_exists_beside_the_shared_rule" | mcp/tests/test_knowledge_family_composition.py:962-962 |
| The case that proves a context whose subject is not a family revision is refused. | "test_a_context_whose_subject_is_not_a_family_revision_is_refused" | mcp/tests/test_knowledge_family_composition.py:852-852 |
| The case that proves an edge with no declared policy is stored, readable and not traversable. | "test_an_edge_with_no_declared_policy_is_stored_readable_and_not_traversable" | mcp/tests/test_knowledge_family_composition.py:417-417 |
| The lane row this module is registered under, and the unit ceiling it is measured against. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |
| The one contract whose consumer list this module joined for its admitted candidate. | "contract:knowledge-facet-cases" | mcp/tests/evidence-lifecycle.toml:1220-1220 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T08:30+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 9 generated projection bullet(s) by hand** — `test_a_context_whose_subject_is_not_a_family_revision_is_refused`, `test_a_dataset_predating_the_composition_tables_refuses_a_composition_write`, `test_an_authored_edge_a_policy_and_a_context_are_immutable_at_the_database`, `test_an_edge_with_no_declared_policy_is_stored_readable_and_not_traversable`, `test_every_non_family_endpoint_kind_is_unrepresentable_rather_than_merely_rejected`, `test_no_second_cycle_implementation_exists_beside_the_shared_rule`, `test_one_shared_rule_judges_the_composition_graph_at_both_check_levels`, `test_the_composition_commands_are_the_closed_unions_own_members`, `test_the_registered_generation_appends_the_six_tables_to_the_generation_it_descends_from`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.
- 2026-09-18T06:06:32+00:00: Generated citation repair: "contract:knowledge-facet-cases" repointed to mcp/tests/evidence-lifecycle.toml:1220-1220. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:30+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): created this one-to-one card for the composition leaf's first case module. This seat re-read the module against the candidate and **corrected the record rather than repeating the builder's**: the suite collects **26** cases in total across the two modules, and this module's own top-level cases number **eighteen**; one consequence of the count being what it is, stated here because the distinction matters, is that the projection's own assertions are driven inside the sibling boundary module's application-seam case rather than by separate cases. The card records the two registered rails (the unit-regression lane row and the three evidence-contract consumer entries, with **no** new fixture, contract or artifact, so counts stay 13 / 54), the hermetic classification that makes the unit lane behaviour-preserving, and the host's required `-o "filterwarnings=ignore"` override. Verification metadata is the leaf's base commit `e963a01c`: the code commit does not exist yet and closeout owns that stamp.
