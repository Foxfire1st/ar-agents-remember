# mcp/src/agents_remember/application/knowledge_worklist/route_conditions.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**MIK-R06's family route maintenance, inside the worklist run.** A family's routes are its index into the
codebase (MIK-R04, D12, D20); a route that drifts from the code is stale memory. This module registers the
`family_route_condition` item kind in MIK-R08's registry and evaluates the four route conditions of a family
over K_C's realization entries and the code tree C: `route_path_absent`, `route_emptied`,
`realization_uncovered` and `route_unassigned`. `compute._Run._route_items` calls it as step 6 of every
worklist run, so the conditions are recomputed with the worklist, persisted in its one list, sorted by
`(kind, subject)` and covered by its digest. It also exports `family_route_item_open`, the stored-item
predicate the generic closeout gate (MIK-R09, L09) applies.

## Code Commentary

### Logic

- **Registration (rule 2).** `FAMILY_ROUTE_CONDITION_KIND` is `register_item_kind(ItemKind(...))` at import:
  name `family_route_condition`, subject `<FAM-ID>#<condition>` (pattern over the four `CONDITIONS`, so two
  conditions of one family have different item IDs), the nine facts (`family`, `condition`, `routes`,
  `affected`, `locations`, `renameCandidates`, `unmappedLocations`, `suggestion`, `recordSatisfiesRoutes`),
  the satisfying-row text and owner `MIK-R06`. Its `row_lookup` strips `#<condition>` (`family_of`) and looks
  up the family row, so every condition of a family is answered by the family's one row in the leaf's history
  file (MIK-R07 rule 5).
- **Which families are evaluated (`_Evaluation.conditions`, ruling Q1).**
  - Every family with a `reached_family` item is evaluated on all four conditions.
  - Any other family, on either side, is evaluated only for `route_path_absent`, and only on a route **this
    leaf's range killed**: its directory exists at B and is absent at C (`_killed`, `_with_killed_routes`).
    This is the decision carried from L04 (ruling 1): a carried dead route the validator only reports
    (`R04.1-carried-route-absent`) becomes a mandatory item for the leaf that killed it.
  - A route already absent at B is not charged to an unrelated leaf: it stays the validator's report for the
    migration (R19).
  - A family whose record in K_C (or K_B when K_C lacks it) is `retired` raises nothing (rule 1).
- **Two views (`_Family.view`, `_views`, ruling Q2).** Each condition is judged on K_B's route set (with the
  current record's members) and on K_C's route set, and holds when it holds in either view. The base view
  keeps the item raised after the curator fixes the routes, so the row requirement still binds; the
  candidate view catches a route set the leaf itself broke. The item's identity is the base view's affected
  set when the base view shows the condition, and the candidate view's otherwise, so fixing the routes does
  not change the ID.
- **Locations at C (`_effective`, review N1, ruling 2026-09-29T22:40:22+02:00).** Every condition and the
  suggestion are judged over the entries' **effective** locations: a K_C entry whose file is absent at C
  counts at its rename target from the run's rename map (L08's inventory, ICR-R08); an absent file without a
  rename keeps its recorded path. So the route items appear on the first worklist, before the curator moves
  the entries, and their IDs do not follow the curator's intermediate states.
- **Conditions per view (`_affected`).** `route_path_absent`: routes whose directory C lacks
  (`CodePathSet.has_directory`); `route_emptied`: L04's `FamilyRouteState.emptied`, waived for an
  `unrealized_family` (MIK-R04 rule 4); `realization_uncovered`: `FamilyRouteState.uncovered`;
  `route_unassigned`: no routes, including an exported family's `route_unassigned` state.
- **Rename candidates and ambiguity (`_rename_candidates`, `_renamed_under`, `_base_realization_paths`,
  ruling Q4).** For `route_path_absent` and `route_emptied`: the outermost directories that the family's
  renamed realization files under an affected route went to. More than one is an ambiguous rename target.
- **Suggestion (`_suggestion`, ruling Q5).** The MIK-R04 mechanical suggestion (`suggest_routes`) over the
  effective locations. No suggestion (`null`) when a file is absent at C without a rename, or when the rename
  target is ambiguous; the item then lists every candidate directory (`renameCandidates`) and every absent
  unrenamed location (`unmappedLocations`, the worker's refinement, accepted as review N5).
- **Satisfying rule (rule 3, `family_route_item_open`, `record_satisfies_routes`).** The item is open unless
  the leaf's family row about the family has disposition `rerouted`, `assigned`, `changed` or `retired`
  (`SATISFYING_DISPOSITIONS`, never `no_impact`) **and** `facts.recordSatisfiesRoutes` is true.
  `_record_satisfies` sets that fact: the K_C record satisfies MIK-R04, rule 4 waivers included, or is
  retired, **both** over the entries as K_C records them (the validator's reading) and at their effective
  locations at C (ruling 2026-09-29T23:14:41+02:00), and every route directory exists at C. For
  `route_unassigned` the route set must also be non-empty (`require_routes`, ruling Q3): the
  `legacy-unassessed` waiver alone does not answer it, because MIK-R04 rule 4 says the leaf assigns routes.
- **`satisfiedBy`.** `_condition` applies `family_route_item_open` to the live facts and the leaf's history
  file in K_C, and records the row ID when the item is answered; `compute` carries it in `Item.extra`. The
  stored predicate and the live `satisfiedBy` therefore agree by construction.

### Conventions

- The module never writes and never reroutes (MIK-R06 Exclusions): the suggestion is a fact only.
- L04's `family_route_state`, `route_covers` and `suggest_routes` are reused unchanged (Preservation
  Boundaries: the MIK-R04 rules).
- Complexity: after review N6 every block scores B or better under radon (at most 10); the shared per-family
  facts live in `_Judged`, the per-condition work in `_condition`.

### Invariants And Boundaries

- **A family route problem the leaf causes cannot survive its closeout without a non-`no_impact` family row
  and routes that satisfy MIK-R04.** Candidate invariant; realized by `family_route_item_open`,
  `SATISFYING_DISPOSITIONS` and `_record_satisfies`; proved by
  `test_a_no_impact_row_never_satisfies_and_a_kept_dead_route_keeps_the_item_open`,
  `test_a_directory_move_raises_emptied_and_uncovered_and_a_rerouted_row_satisfies_them` (including the R2-N1
  stage: a `rerouted` row with the target routes while K_C still records the old files stays open) and the
  worker's real-data run (w2 `no_impact` open, w3 `rerouted` satisfied). Enforcement is MIK-R09's (L09).
- **A route already dead at B is not charged to an unrelated leaf.** Candidate invariant; realized by
  `_killed` and the unreached branch of `_views`; proved by
  `test_an_unreached_familys_route_already_dead_at_b_is_not_charged_to_the_leaf`, with the killed-in-range
  case in `test_a_carried_dead_route_the_validator_only_reports_is_a_mandatory_item`.
- **The stored predicate and the live `satisfiedBy` agree.** Candidate invariant; realized by `_condition`
  calling `family_route_item_open`; proved by `assert_predicate_agrees` in every route-condition case.
- **Retired families raise nothing.** Candidate invariant; realized by the `retired` skip in `conditions`
  and `_affected`; proved by `test_a_reached_retired_family_raises_nothing` and the retired family on the
  dead route in the carried-route case.
- **Item IDs are stable across the curator's repair** (review N1, N2 for this kind): proved by the four
  worklists of the conforming case and the real-data IDs, identical over every round.
- **Inert before MIK-R37.** An unconverted leaf gets no worklist (MIK-R08 applicability), so no route item
  exists on today's production leaves.

### Todos

- **L09:** the gate applies `family_route_item_open(item, history)`, which takes the parsed history file
  (not L30's subject-to-row map). Review N2 (IDs of conditions that switch views) is carried to L09 by
  ruling 2026-09-29T22:40:22+02:00; ruling Q7 is recorded on L09.
- **Review N4 (intended):** once one of an unreached family's routes is killed, `recordSatisfiesRoutes`
  requires the whole K_C record to satisfy MIK-R04, so the leaf repairs older drift of that family too.
- **Review N8:** a family that exists only in K_C cannot be answered by a family row (`FamilyRow` judges a
  K_B family); it needs a new family routed at a directory the same range deletes, so nothing is done now.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R06@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`06_family-route-maintenance.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: conditions, evaluated families, views, registration, satisfying row, locations at C and the suggestion. [1]
- The kind name, the four conditions and the satisfying dispositions. [2]
- The family row of an item, found through its family ID. [3]
- The kind registered on import, with its facts, row rule and owner. [4]
- The stored-item predicate for the gate: never `no_impact`, and the record must satisfy the routes. [5]
- MIK-R04 satisfied, or retired; `route_unassigned` needs a non-empty route set. [6]
- What each condition names in one view. [7]
- The base view: K_B's routes over the current members. [8]
- The facts shared by a family's conditions, recorded and effective locations. [9]
- Reached families on all four conditions, others only on a killed route; retired skipped. [10]
- Entries judged where their files lie at C. [11]
- A killed route, and the families that have one. [12]
- The two views; an unreached family answers only for killed routes. [13]
- One condition: its facts, identity and `satisfiedBy`. [14]
- The record judged as recorded and at C. [15]
- The suggestion, withheld without a rename or when ambiguous. [16]
- The rename candidates: outermost target directories. [17]
- The inputs and the entry point, sorted by subject. [18]
- Step 6 of the run. [19]
- The conforming directory move, four worklists, stable IDs. [20]
- `no_impact` never satisfies; a kept dead route keeps the item open. [21]
- The carried L04 decision: a killed route is a mandatory item. [22]
- A route dead at B is not charged to the leaf. [23]

### Cross-Repo References

No meaningful cross-repo references found: the module reads the parsed memory sides and the file lists of
one code repository, handed to it by the worklist run.

No cross-repo boundary is crossed by this file.
