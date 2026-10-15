# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R04's family route rules in the validator's one registry (MIK-R22 rule 9).** `ROUTE_RULES` runs wherever the validator runs. The refusing route rules carry `writer_reports`; carried-route-absent and unrealized-family also defer at sync merge/standalone conversion (`merge_reports`). Route-unassigned is `migration_debt`, not a plain report-only rule.

## Code Commentary

### Logic

- `_families` yields every parsed family record with its `FamilyRouteState` (from `family_routes`) over the tree's realization locations.
- `R04.1-route-directory` (refuses, `writer_reports`): a route the candidate **adds** must be a directory of the paired code tree (`CodeTree.has_directory`). A route is *carried* when the same family lists it in any comparison base (K_B, or either merge parent; `_base_family_routes` unions all bases that parse).
- `R04.1-carried-route-absent` (refuses; `writer_reports`, `merge_reports`): a carried route whose
  directory is absent raises `route_path_absent` for MIK-R06. It reports at sync merge/standalone
  conversion and inside the writer, but refuses ordinary publication/landing. The route-maintenance
  pass still raises mandatory work for a route the leaf's own range killed (present at B, absent at C),
  even for an unreached family; an already-absent base route is no permanent publication exemption.
- Both existence rules are skipped for a standalone conversion or when there is no code tree, and for a retired family.
- `R04.2-coverage` (refuses, `writer_reports`): each uncovered realization is named with its entry, invariant and path, and the family's routes; a `routeless` family that is not `legacy-unassessed` is refused with its realization paths.
- `R04.2-non-empty` (refuses, `writer_reports`): each emptied route, under the field `routes.<i>`.
- `R04.4-unrealized-family` refuses publication/landing, with merge/conversion and writer deferrals.
  `R04.4-route-unassigned` is migration debt: new findings refuse immediately; actual base-carried
  live/routeless/legacy-unassessed findings report only while migration is incomplete. A base
  merely holding the same ID assessed, routed or retired does not carry that finding. Standalone
  conversion reports authored debt; completed migration refuses all debt.

### Conventions

- Every message starts `family <ID>:` or `family <ID> ...`; the field is `routes.<i>` when one route is at fault, and `routes` or `members` otherwise.
- `_absent_routes` serves both existence rules, so the carried/added split is computed once per rule.

### Invariants And Boundaries

- Enforcement goes through the registry only: there is no forked validator and no skip flag.
- Carried absent routes are findings, not silent preservation: sync/conversion and inside-writer
  reports name the deferral reason and refusing route; ordinary publication/landing refuses.
- The refusing route rules, including nested-routes, carry `writer_reports`; `route-unassigned` instead follows migration-debt
  currentness. Added-route, Coverage and Non-empty refusal mechanics remain unchanged.
- The validator cannot tell a broad route (`mcp/`) from a deep one: route depth is curator judgment, supported by the suggestion (ruling Q4).

### Todos

The former per-rule candidate-state recomputation is resolved by the context's cached `route_families`. `_absent_routes` still reparses comparison-base families for its separate existence checks; the candidate cache is not a claim of complete base-read deduplication or a timing result.

`R04.1-nested-routes` checks every live family for an ancestor among its own routes, including root `.` above a descendant, and names the descendant index and parent route. It is writer-reported but refuses ordinary validator publication. `_families` now iterates the context-cached candidate tuple; it does not recompute realization locations for each rule.

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
- At a merge, a route carried by either parent is carried. [8]
- A route holding only a proof entry violates Non-empty. [9]

### Cross-Repo References

No meaningful cross-repo references found: the rules read one memory tree, its bases and one paired code tree, all addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.

- Added route existence refuses; carried absent routes defer only in the named merge/conversion/writer contexts. [3]
- Coverage and Non-empty name the family, route and uncovered path. [4]
- Unrealized-family merge deferral and route-unassigned actual-base-finding migration debt. [5]
- Six registered rules: five writer-reported, two also merge-reported, one migration-debt rule. [6]
- Added-route existence and carried-route findings in the route fixture; a merge report is not publication permission. [7]
- Current source delta inspected statically: Replace the obsolete three-refuse/three-report split and base-ID-only debt carry with actual base-finding enforcement, keeping route mechanics, realization-only coverage and retired exemptions. [10]

- Nested routes refuse, while all route rules read the shared candidate-family states. [11]
