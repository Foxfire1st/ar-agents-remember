# mcp/tests/test_family_route_conditions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_family_route_conditions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T01:22:26+02:00 |
| lastVerifiedCommitHash | `7127756cd132d1103cd0a24bc7dc6884ddb663ee`|
| lastVerifiedCommitDate | 2026-09-30T01:41:06+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R06@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `06_family-route-maintenance.json`; they live
outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The four families and the world. | "FAM-W00001"; `World` | mcp/tests/test_family_route_conditions.py:1-12; mcp/tests/test_family_route_conditions.py:133-149 |
| The stored predicate checked against the live `satisfiedBy`. | `assert_predicate_agrees` | mcp/tests/test_family_route_conditions.py:184-189 |
| The conforming directory move, with the R2-N1 stage. | `test_a_directory_move_raises_emptied_and_uncovered_and_a_rerouted_row_satisfies_them` | mcp/tests/test_family_route_conditions.py:206-271 |
| `no_impact` refused; a kept dead route stays open. | `test_a_no_impact_row_never_satisfies_and_a_kept_dead_route_keeps_the_item_open` | mcp/tests/test_family_route_conditions.py:274-307 |
| The carried L04 decision end to end. | `test_a_carried_dead_route_the_validator_only_reports_is_a_mandatory_item` | mcp/tests/test_family_route_conditions.py:315-358 |
| A reached retired family raises nothing. | `test_a_reached_retired_family_raises_nothing` | mcp/tests/test_family_route_conditions.py:361-376 |
| `route_unassigned` until an `assigned` row with routes. | `test_a_reached_family_without_routes_is_route_unassigned_until_an_assigned_row` | mcp/tests/test_family_route_conditions.py:384-409 |
| The boundary example. | `test_an_entry_moving_to_another_file_inside_its_route_raises_no_route_item` | mcp/tests/test_family_route_conditions.py:412-423 |
| An ambiguous rename target. | `test_an_ambiguous_rename_target_lists_every_candidate_and_suggests_nothing` | mcp/tests/test_family_route_conditions.py:426-450 |
| The registered kind and its row lookup. | `test_the_kind_is_registered_and_its_row_is_the_familys_row` | mcp/tests/test_family_route_conditions.py:453-471 |
| Q1: a route dead at B is not charged. | `test_an_unreached_familys_route_already_dead_at_b_is_not_charged_to_the_leaf` | mcp/tests/test_family_route_conditions.py:479-491 |
| Q5: the suggestion follows renames. | `test_the_suggestion_follows_renames_of_files_absent_at_c_and_is_withheld_without_one` | mcp/tests/test_family_route_conditions.py:494-514 |
| The lane registration. | "mcp/tests/test_family_route_conditions.py" | mcp/tests/test-evidence-lanes.toml:69-69 |

## Cross-Repo References

No cross-repo boundary is crossed: every repository is created under `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): created this card for the new test file MIK-R06 adds (10 cases). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
