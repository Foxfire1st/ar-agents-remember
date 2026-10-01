# mcp/src/agents_remember/memory/knowledge/lineages.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The one composition edge statement, scoped by `repository_id` alone and copied into the shape the shared rule reads.** [1]
- **The edge supplier: it reads the composition table alone and cannot synthesise an edge from a label, a path or prose.** [2]
- The one declared-cycle rule the composition graph is judged by, rather than a second rule grown beside it. [3]
- The walk both check levels call, including the branch where a candidate descends from a stored cycle. [4]
- The cycle-membership read the second branch reports through. [5]
- **The case that proves the composition graph is judged at both check levels and rolls back with its ids named.** [6]
- **The case that proves the shared rule's second branch applies uniformly to the cross-family graph.** [7]
- **The case that asserts no second cycle implementation and no recursive CTE exists.** [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
