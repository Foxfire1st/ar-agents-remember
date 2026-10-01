# mcp/tests/test_family_route_conditions.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R06@v2 cases (10 collected): family route maintenance, raised as `family_route_condition`
worklist items.** Every case reuses MIK-R08's real Git code and converted memory repositories
(`test_knowledge_worklist.World`) with four families: `FAM-R00001` (routes `svc/application` and
`svc/worktrees`, realized in three files), `FAM-W00001` (an `unrealized_family` routed at `svc/legacy`),
`FAM-X00001` (an exported family with no routes) and `FAM-T00001` (a retired family routed at `svc/legacy`).
A case commits a code candidate C and a memory candidate K_C and computes the worklist exactly as the leaf
route does; the satisfying row is a family row in the leaf's own history file. The file runs in the
`unit-regression` lane (`test-evidence-lanes.toml`).

## Code Commentary

### Logic

- **Helpers.** `family` and `families` write the four family records with chosen routes; `family_row` and
  `history` write the leaf's family row; `moved` and `relocate` move realization entries to new files in
  K_C; `move_out_of_worktrees` commits the packet's conforming move (`ledger.py` and `integrate.py` into
  `svc/landing`); `route_items` picks the route items by subject; `assert_predicate_agrees` checks
  `family_route_item_open` over the stored item and K_C's history against the live `satisfiedBy`.
- **The conforming example** (`test_a_directory_move_…`): four worklists (before any entry moves, one moved,
  both moved, rerouted). `route_emptied` and `realization_uncovered` appear on the first (review N1), their
  IDs never change, and a `rerouted` row satisfies both. The R2-N1 stage writes the target routes and a
  `rerouted` row while K_C still records the old files: both items stay open with `recordSatisfiesRoutes`
  false (mutation-checked by the worker: judging only the locations at C fails this stage).
- **The non-conforming example** (`test_a_no_impact_row_…`): a `no_impact` row never satisfies, even with
  fixed routes; a `rerouted` row does not satisfy while `svc/worktrees` is kept after its last entry left.
- **`route_path_absent` and the carried L04 decision** (`test_a_carried_dead_route_…`): the validator passes
  and only reports `R04.1-carried-route-absent` for `FAM-W00001`, which the worklist does not reach; the item
  is still raised and open; a `changed` row alone does not satisfy it while the dead route stays; `rerouted`
  plus an existing route does. The retired family on the same dead route raises nothing.
- **Retired** (`test_a_reached_retired_family_raises_nothing`), **`route_unassigned`**
  (`test_a_reached_family_without_routes_…`: open at first, a `changed` row with `routes: []` stays open, an
  `assigned` row with a route is satisfied, the ID unchanged; ruling Q3), **the boundary example**
  (`test_an_entry_moving_to_another_file_inside_its_route_…`: no route item, `touched_invariant` still
  raised), **ambiguity** (`test_an_ambiguous_rename_target_…`: every candidate listed, no suggestion, and the
  checklist line), **the registry** (`test_the_kind_is_registered_…`: the kind, its facts, the row lookup that
  strips `#condition`, and an item without facts reads open).
- **Rulings round.** `test_an_unreached_familys_route_already_dead_at_b_…` (Q1: with B already lacking
  `svc/legacy` nothing is raised; with the deletion inside the range `route_path_absent` is raised) and
  `test_the_suggestion_follows_renames_…` (Q5: a rename gives `[svc/application, svc/landing]` with no
  `unmappedLocations`; a deletion gives no suggestion and lists the absent files).

- **MIK-R27 (L27 ruling Q4).** L06 landed after L27. The carried-route case asserts `validate_tree(...).ok`
  and filters the reports by rule, so the report-only `R27.4-legacy-unassessed` count every fixture
  validation now carries needs no pin here; the fixture families exist in K_B, so `R27.2-new-record` never
  applies to them.

### Conventions

- Real Git repositories under `tmp_path`, no mocks; the worklist is computed through the same run the leaf
  route uses.

### Invariants And Boundaries

- The file proves the candidate invariants recorded on `route_conditions.py.md`: the row and route
  requirement, the dead-at-B exemption, predicate agreement and the retired exemption.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R06@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `06_family-route-maintenance.json`; they live
outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The four families and the world. [1]
- The stored predicate checked against the live `satisfiedBy`. [2]
- The conforming directory move, with the R2-N1 stage. [3]
- `no_impact` refused; a kept dead route stays open. [4]
- The carried L04 decision end to end. [5]
- A reached retired family raises nothing. [6]
- `route_unassigned` until an `assigned` row with routes. [7]
- The boundary example. [8]
- An ambiguous rename target. [9]
- The registered kind and its row lookup. [10]
- Q1: a route dead at B is not charged. [11]
- Q5: the suggestion follows renames. [12]
- The lane registration. [13]

### Cross-Repo References

No cross-repo boundary is crossed: every repository is created under `tmp_path`.

No cross-repo boundary is crossed by this file.
