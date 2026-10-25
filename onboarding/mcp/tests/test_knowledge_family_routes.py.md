# mcp/tests/test_knowledge_family_routes.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R04: the validator's family route rules, the reported states, the root route `.` and the mechanical suggestion, over the converted Doc14 fixture tree.** The fixture's family is Doc14 §4.2's "attribution-and-landing-pairing" with its three routes (`worktrees`, `models/knowledge`, `application`) and six realizations (`knowledge_validator_test_support`). Cases pin the applicable refusing/reporting rule sets, naming family, route and uncovered path; deleted carried routes can also trigger carried-anchor refusals. Registered in the `unit-regression` lane; the earlier 33-case collection is historical, not freshly recertified. This card describes static source assertions.

## Code Commentary

### Logic

- **Doc14 example.** `test_the_doc14_family_example_validates_with_every_route_holding_realizations` asserts the exact route-to-files table of Doc14 §4.2 and that the proof `PRF-T3ST0K` is not among the family's locations.
- **Coverage and Non-empty.** An added realization outside every route is refused under `R04.2-coverage`; a route whose only realization is removed, and a route (`mcp/tests`) holding only a proof entry, are refused under `routes.<i>: [R04.2-non-empty]`. One broad route (`mcp`) passes the rules while the suggestion offers the three local routes.
- **Route existence.** An added absent route is refused (`R04.1-route-directory`); a carried absent route refuses off merge (`R04.1-carried-route-absent`, alongside `R22.6-carried-stale` when anchors are absent); at a sync merge it reports, and a route carried by neither parent is refused as added. A standalone conversion checks no route directory. Both code trees answer `has_directory`, the root included.
- **Writer reporting.** `test_the_refusing_route_rules_are_reported_inside_the_writer` pins the writer-reported `ROUTE_RULES` set including nested-routes alongside route-directory, coverage, non-empty, carried-route-absent and unrealized-family and shows a Non-empty break still refuses in `validate_tree` while all its refusals fall inside `writer_reported_rule_ids()`.
- **The root route.** Eight spellings are parametrised: `.` is accepted and `""`, `" ."`, `"./"`, `"./mcp"`, `".."`, `"/"`, `"mcp/./src"` and `"mcp/"` are refused by `FamilyRecord`. A realization in `setup.py` violates Coverage under the narrower routes; replacing the route set with `.` alone covers it and passes both rules. Root-plus-descendant route sets are nested and refuse rather than being an alternative passing control.
- **Route states.** `test_an_unrealized_family_refuses_off_merge_and_non_empty_is_waived`
  asserts unrealized-family refusal on one base and reporting at sync, while preserving the
  Non-empty waiver. A realized family with no routes still violates Coverage unless an unassessed
  export; a newly admitted routeless/unrealized family fires Coverage and unrealized-family.
  `test_a_carried_exported_family_without_routes_is_migration_debt` uses a base already holding
  `route_unassigned`, reports actual carried incomplete debt with Coverage waived, and is not a
  blanket no-base exemption. Retired families raise nothing.
- **Suggestion.** Five parametrised collapse cases (siblings collapse into a parent of only family code; no collapse when the parent holds other code; a directory under another is covered; collapsing repeats; never the root) and the root-route case.
- **Actual carried debt in the pins (MIK-R53 superseding the L27 report-only premise).**
  Positive coverage/non-empty/root-route fixtures now supply explicit bases so live legacy debt is
  genuinely carried, not newly introduced by a no-base run. That incomplete migration reports
  `LEGACY_COUNT`; standalone conversion also reports the debt it authors. New debt at other routes
  refuses, and migration-complete carried debt refuses. The historical L06/L27 landing-order re-pin
  requirement explains the old pins, not permanent report-only permission for every fixture.
- **Command.** `test_the_routes_command_offers_the_suggestion_and_writes_nothing` runs `knowledge-routes` in text and JSON mode, checks `unknown family: <ID>`, and asserts the memory bytes are unchanged.

### Conventions

- Helpers `_validate`, `_rules`, `_family`, `_with_family`, `_new_family` and `_add_realization` edit one file of the fixture tree and validate it with `code()`.

### Invariants And Boundaries

- Static assertions distinguish single-base refusal, sync reporting, standalone conversion and
  actual base-held incomplete debt. Report disposition is route/finding-specific, not permanently
  report-only; writer reporting grants repair access, not commit/landing permission.

### Todos

None recorded.

The added nested-route fixtures cover both an ordinary ancestor/descendant pair and root-plus-descendant; the finding names the nested route and remains writer-reported. A counted wrapper around `family_route_state` observes its fixture family exactly once during one validation, an operation-count assertion rather than elapsed-time evidence. The routes command checks `differs` in JSON and text as well as unchanged memory bytes.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The route design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`, §4.2) and the
requirement packet `MIK-R04@v2` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cases and their helpers.


- The Doc14 family example validates, and a proof is not a location. [1]


- Coverage and Non-empty violations name the family, the route and the path. [2]


- One broad route passes; the suggestion offers local routes. [3]

- Route spellings: `.` or a repository path. [4]

- A family without routes that is not an unassessed export violates Coverage. [7]

- A standalone conversion checks no route directory: with no code tree it passes, reporting only the legacy count. [8]
- The lane registration. [9]

### Cross-Repo References

No meaningful cross-repo references found: the tests read the repository's own fixtures and a temporary directory.

No cross-repo boundary is crossed by this file.


- Based root-route fixtures pin coverage/non-empty and only carried incomplete legacy-debt reporting; not a no-base pass. [5]


- Current unrealized-family off-merge refusal/sync reporting, actual carried route-unassigned debt and the retired exemption. [6]


- Current source delta inspected statically: Repair route/debt/writer reporting and based controls; retain root routes, waivers and retired exemption. [10]


- Nested-route refusal, one state computation per fixture family/validation and explicit routes-command difference output are source assertions. [11]
