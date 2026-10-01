# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R04's six family route rules in the validator's one registry (MIK-R22 rule 9).** Importing the module registers `ROUTE_RULES`; `validator.py` imports it next to MIK-R22's rule modules, so every place the validator runs (`validate_tree`, `require_valid_commit`, the managed sync, `knowledge-validate`) runs these rules too. Three refuse and three are report-only.

## Code Commentary

### Logic

- `_families` yields every parsed family record with its `FamilyRouteState` (from `family_routes`) over the tree's realization locations.
- `R04.1-route-directory` (refuses, `writer_reports`): a route the candidate **adds** must be a directory of the paired code tree (`CodeTree.has_directory`). A route is *carried* when the same family lists it in any comparison base (K_B, or either merge parent; `_base_family_routes` unions all bases that parse).
- `R04.1-carried-route-absent` (**report-only**): a carried route whose directory is absent is reported as `route_path_absent` for the route-maintenance pass (MIK-R06), not refused. This is the same split MIK-R22 rule 6 makes for anchors (ruling Q1). Since leaf 260928-MIK-L06 the route-maintenance pass exists (`application/knowledge_worklist/route_conditions.py`): a carried route that the leaf's own range killed (present at B, absent at C) becomes a mandatory `family_route_condition` worklist item, even for a family the worklist does not reach; a route already absent at B stays this report, for the migration (L06 ruling Q1, 2026-09-29T21:49:19+02:00).
- Both existence rules are skipped for a standalone conversion or when there is no code tree, and for a retired family.
- `R04.2-coverage` (refuses, `writer_reports`): each uncovered realization is named with its entry, invariant and path, and the family's routes; a `routeless` family that is not `legacy-unassessed` is refused with its realization paths.
- `R04.2-non-empty` (refuses, `writer_reports`): each emptied route, under the field `routes.<i>`.
- `R04.4-unrealized-family` and `R04.4-route-unassigned` (**report-only**): the two reported states of rule 4.

### Conventions

- Every message starts `family <ID>:` or `family <ID> ...`; the field is `routes.<i>` when one route is at fault, and `routes` or `members` otherwise.
- `_absent_routes` serves both existence rules, so the carried/added split is computed once per rule.

### Invariants And Boundaries

- Enforcement goes through the registry only: there is no forked validator and no skip flag.
- A carried absent route is reported, never silently kept and never refused; MIK-R06 turns it into a mandatory worklist item.
- The three refusing rules refuse at every commit route; inside the writer they are reported (`writer_reports`, MIK-R04 rule 6), which the writer (MIK-R12) applies.
- The validator cannot tell a broad route (`mcp/`) from a deep one: route depth is curator judgment, supported by the suggestion (ruling Q4).

### Todos

Each rule recomputes the family states, and `_absent_routes` reparses the bases' family files twice; negligible at fixture scale, a cache on the context is a later option (review R1 finding 5).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The route design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`, §4.2) and the
requirement packet `MIK-R04@v2` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The six rules, the carried-route computation and their registration.

- Carried routes are the union of every base's family routes. [1]
- Absent routes, skipped for a conversion, a missing code tree and a retired family. [2]
- An added route is refused, a carried one reported. [3]
- Coverage and Non-empty name the family, the route and the uncovered path. [4]
- The two reported states. [5]
- The six registered rules, three report-only and three writer-reported. [6]
- An added route must be a directory; a carried one is reported. [7]
- At a merge, a route carried by either parent is carried. [8]
- A route holding only a proof entry violates Non-empty. [9]

### Cross-Repo References

No meaningful cross-repo references found: the rules read one memory tree, its bases and one paired code tree, all addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.
