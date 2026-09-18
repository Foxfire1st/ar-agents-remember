# mcp/src/agents_remember/memory/knowledge/lineages.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/lineages.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:26+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The third edge source.** `lineage.py` owns the one acyclic-lineage rule, and its own two edge
statements are per-object — one filtered by `invariant_id`, one by `family_id`. The composition graph
is not per-object: it relates *different* family revisions inside one repository namespace, so it
needs a third statement, scoped by `repository_id` alone, that feeds the same generic functions.

This module supplies **edges and nothing that decides**. It exists so a reader comparing the three
graphs sees all three edge sources in one place, all three feeding the shipped `find_cycle`,
`declared_cycle` and `cycle_vertices`.

**Why not a second cycle rule.** The substrate's acyclic guarantee states its reach cannot drift
between the graphs it judges, and `batch_preconditions.py` states the boundary that keeps that true.
A composition cycle check written here would make drift possible between **three** graphs instead of
two, which is exactly what reusing the shared rule prevents.

## Code Commentary

### Logic

- `_COMPOSITION_EDGES_SQL` — the one statement. It selects `from_family_revision_id` and
  `to_family_revision_id` from `family_composition` filtered by `repository_id`, and copies the pair
  into the `(child, parent)` shape the shared rule reads, so the walk descends the edge in the
  direction its author declared.
- `composition_edges` — returns the repository's recorded edges as `LineageEdge` tuples.
- The **direction a traversal policy later chooses is deliberately not part of this statement**: two
  datasets holding the same edges must agree about whether one of them is cyclic, whatever policies
  their edges carry. A policy decides what a *reader* may follow; it does not decide what the graph
  is.

### Conventions

- The edges are read from the composition table **alone**. No read path, projection or detector
  synthesises one, and this function cannot see a label, a path or prose to synthesise one from.
- The module imports only `lineage.LineageEdge` and `apsw`; it does not import the rule it feeds,
  which is what keeps it a supply of edges rather than a participant in the decision.

### Invariants And Boundaries

- **One cycle rule, three graphs.** `find_cycle`, `declared_cycle` and `cycle_vertices` are the only
  cycle implementation, and a case asserts that no second walk or `WITH RECURSIVE` exists beside
  them.
- **Scoped by `repository_id` alone.** The composition graph is a whole-namespace graph, so the
  statement takes no per-object filter; that is what makes `require_after_integrity`'s whole-graph
  level able to judge it.
- **Boundary.** This module decides nothing: it neither computes a cycle nor refuses a write. The
  batch's two check levels consume it through the shared rule.

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
| **The one composition edge statement, scoped by `repository_id` alone and copied into the shape the shared rule reads.** | `_COMPOSITION_EDGES_SQL` | mcp/src/agents_remember/memory/knowledge/lineages.py:31-31 |
| **The edge supplier: it reads the composition table alone and cannot synthesise an edge from a label, a path or prose.** | `composition_edges` | mcp/src/agents_remember/memory/knowledge/lineages.py:37-37 |
| The one declared-cycle rule the composition graph is judged by, rather than a second rule grown beside it. | `declared_cycle` | mcp/src/agents_remember/memory/knowledge/lineage.py:97-97 |
| The walk both check levels call, including the branch where a candidate descends from a stored cycle. | `find_cycle` | mcp/src/agents_remember/memory/knowledge/lineage.py:133-133 |
| The cycle-membership read the second branch reports through. | `cycle_vertices` | mcp/src/agents_remember/memory/knowledge/lineage.py:207-207 |
| **The case that proves the composition graph is judged at both check levels and rolls back with its ids named.** | "test_one_shared_rule_judges_the_composition_graph_at_both_check_levels" | mcp/tests/test_knowledge_family_composition.py:900-900 |
| **The case that proves the shared rule's second branch applies uniformly to the cross-family graph.** | "test_the_shared_rules_second_branch_applies_uniformly_to_the_cross_family_graph" | mcp/tests/test_knowledge_family_composition.py:944-944 |
| **The case that asserts no second cycle implementation and no recursive CTE exists.** | "test_no_second_cycle_implementation_exists_beside_the_shared_rule" | mcp/tests/test_knowledge_family_composition.py:980-980 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_one_shared_rule_judges_the_composition_graph_at_both_check_levels" repointed to mcp/tests/test_knowledge_family_composition.py:900-900. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_shared_rules_second_branch_applies_uniformly_to_the_cross_family_graph" repointed to mcp/tests/test_knowledge_family_composition.py:944-944. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_no_second_cycle_implementation_exists_beside_the_shared_rule" repointed to mcp/tests/test_knowledge_family_composition.py:980-980. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_one_shared_rule_judges_the_composition_graph_at_both_check_levels" repointed to mcp/tests/test_knowledge_family_composition.py:895-895. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_the_shared_rules_second_branch_applies_uniformly_to_the_cross_family_graph" repointed to mcp/tests/test_knowledge_family_composition.py:937-937. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_no_second_cycle_implementation_exists_beside_the_shared_rule" repointed to mcp/tests/test_knowledge_family_composition.py:973-973. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:30:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 3 generated projection bullet(s) by hand** — `test_no_second_cycle_implementation_exists_beside_the_shared_rule`, `test_one_shared_rule_judges_the_composition_graph_at_both_check_levels`, `test_the_shared_rules_second_branch_applies_uniformly_to_the_cross_family_graph`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.

- 2026-09-18T04:26:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): created this one-to-one card for the third edge source. It records the ruling this leaf had to make: **the composition graph is judged by the whole shipped shared rule, uniformly, including the branch where a candidate descends from a stored cycle** — a scoped alternative would need evidence that composition edges inherit nothing from the revisions they reach, which is exactly what a cyclic composition graph would falsify. It records that the module supplies edges and nothing that decides, that the statement is scoped by `repository_id` alone because the graph is a whole-namespace graph, and that the direction a traversal policy chooses deliberately does not reach the statement. Verification metadata is the leaf's base commit `e963a01c`: the code commit does not exist yet and closeout owns that stamp.
