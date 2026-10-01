# mcp/tests/test_knowledge_family_routes.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R04: the validator's family route rules, the reported states, the root route `.` and the mechanical suggestion, over the converted Doc14 fixture tree.** The fixture's family is Doc14 §4.2's "attribution-and-landing-pairing" with its three routes (`worktrees`, `models/knowledge`, `application`) and six realizations (`knowledge_validator_test_support`). A test changes one thing and checks that exactly the owning rule answers, naming the family, the route and the uncovered path. Registered in the `unit-regression` lane; 33 collected cases.

## Code Commentary

### Logic

- **Doc14 example.** `test_the_doc14_family_example_validates_with_every_route_holding_realizations` asserts the exact route-to-files table of Doc14 §4.2 and that the proof `PRF-T3ST0K` is not among the family's locations.
- **Coverage and Non-empty.** An added realization outside every route is refused under `R04.2-coverage`; a route whose only realization is removed, and a route (`mcp/tests`) holding only a proof entry, are refused under `routes.<i>: [R04.2-non-empty]`. One broad route (`mcp`) passes the rules while the suggestion offers the three local routes.
- **Route existence.** An added absent route is refused (`R04.1-route-directory`); a carried absent route is reported (`R04.1-carried-route-absent`); at a merge, a route carried by either parent is carried, and one carried by neither is refused. A standalone conversion checks no route directory. Both code trees answer `has_directory`, the root included.
- **Writer reporting.** `test_the_refusing_route_rules_are_reported_inside_the_writer` pins MIK-R04's writer-reported set exactly (through `ROUTE_RULES`) and shows a Non-empty break still refuses in `validate_tree` while all its refusals fall inside `writer_reported_rule_ids()`.
- **The root route.** Eight spellings are parametrised: `.` is accepted and `""`, `" ."`, `"./"`, `"./mcp"`, `".."`, `"/"`, `"mcp/./src"` and `"mcp/"` are refused by `FamilyRecord`. A realization in `setup.py` violates Coverage until `.` is added; a family whose only route is `.` passes both rules.
- **Reported states.** `unrealized_family` is reported with Non-empty waived, but still needs a route unless it is an unassessed export; `route_unassigned` is reported with Coverage waived; `routes: []` on any other family violates Coverage; a retired family raises nothing.
- **Suggestion.** Five parametrised collapse cases (siblings collapse into a parent of only family code; no collapse when the parent holds other code; a directory under another is covered; collapsing repeats; never the root) and the root-route case.
- **The legacy count in the pins (leaf 260928-MIK-L27).** Since MIK-R27 registers its admission rules, every validation of the fixture tree carries one report-only `R27.4-legacy-unassessed` count (`LEGACY_COUNT`), because the Doc14 family is an export. The eight pins that expected no violation or an exact report-only set now include it and stay exact: the Doc14 example, the carried-route case, the standalone conversion, both root-route cases, and the two reported-state cases, whose `reports[0]` lookups now select the report by rule because the count sorts first. By ruling 22:11:24 Q4 (review F6), whichever of L06 and L27 lands second makes its own new pins over this tree include the count.
- **Command.** `test_the_routes_command_offers_the_suggestion_and_writes_nothing` runs `knowledge-routes` in text and JSON mode, checks `unknown family: <ID>`, and asserts the memory bytes are unchanged.

### Conventions

- Helpers `_validate`, `_rules`, `_family`, `_with_family`, `_new_family` and `_add_realization` edit one file of the fixture tree and validate it with `code()`.

### Invariants And Boundaries

- Every rule is asserted to land in either the refusals or the reports, so report-only disposition is pinned behaviourally.

### Todos

None recorded.

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
- The root route covers a root-level realization, and a family whose only route is `.` is non-empty; each validation's only finding is the report-only legacy count. [5]
- The reported states and the retired exemption. [6]
- A family without routes that is not an unassessed export violates Coverage. [7]
- A standalone conversion checks no route directory: with no code tree it passes, reporting only the legacy count. [8]
- The lane registration. [9]

### Cross-Repo References

No meaningful cross-repo references found: the tests read the repository's own fixtures and a temporary directory.

No cross-repo boundary is crossed by this file.
