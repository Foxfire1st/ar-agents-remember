# mcp/tests/test_knowledge_family_routes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_family_routes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `overview.md` |

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
- **Command.** `test_the_routes_command_offers_the_suggestion_and_writes_nothing` runs `knowledge-routes` in text and JSON mode, checks `unknown family: <ID>`, and asserts the memory bytes are unchanged.

### Conventions

- Helpers `_validate`, `_rules`, `_family`, `_with_family`, `_new_family` and `_add_realization` edit one file of the fixture tree and validate it with `code()`.

### Invariants And Boundaries

- Every rule is asserted to land in either the refusals or the reports, so report-only disposition is pinned behaviourally.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The route design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`, §4.2) and the
requirement packet `MIK-R04@v2` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The cases and their helpers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The Doc14 family example validates, and a proof is not a location. | `test_the_doc14_family_example_validates_with_every_route_holding_realizations` | mcp/tests/test_knowledge_family_routes.py:98-123 |
| Coverage and Non-empty violations name the family, the route and the path. | `test_a_realization_outside_every_route_violates_coverage_naming_family_and_path`; `test_a_route_that_no_longer_contains_a_realization_violates_non_empty` | mcp/tests/test_knowledge_family_routes.py:131-139; mcp/tests/test_knowledge_family_routes.py:142-151 |
| One broad route passes; the suggestion offers local routes. | `test_one_broad_route_satisfies_the_rules_and_the_suggestion_offers_the_local_ones` | mcp/tests/test_knowledge_family_routes.py:169-182 |
| Route spellings: `.` or a repository path. | `test_a_family_route_is_a_repository_path_or_the_root_route` | mcp/tests/test_knowledge_family_routes.py:276-282 |
| The root route covers a root-level realization, and alone is non-empty. | `test_the_root_route_covers_a_realization_at_the_repository_root`; `test_the_root_route_alone_is_non_empty_whenever_the_family_is_realized` | mcp/tests/test_knowledge_family_routes.py:285-294; mcp/tests/test_knowledge_family_routes.py:297-300 |
| The reported states and the retired exemption. | `test_an_unrealized_family_is_reported_and_non_empty_is_waived`; `test_an_exported_family_without_routes_is_route_unassigned_and_coverage_is_waived`; `test_a_retired_family_is_exempt_from_every_route_rule` | mcp/tests/test_knowledge_family_routes.py:308-315; mcp/tests/test_knowledge_family_routes.py:327-334; mcp/tests/test_knowledge_family_routes.py:348-355 |
| A family without routes that is not an unassessed export violates Coverage. | `test_a_family_without_routes_that_is_not_legacy_unassessed_violates_coverage`; `test_an_unrealized_family_still_needs_a_route_unless_it_is_an_unassessed_export` | mcp/tests/test_knowledge_family_routes.py:337-345; mcp/tests/test_knowledge_family_routes.py:318-324 |
| A standalone conversion checks no route directory. | `test_a_standalone_conversion_checks_no_route_directory` | mcp/tests/test_knowledge_family_routes.py:257-260 |
| The lane registration. | "mcp/tests/test_knowledge_family_routes.py" | mcp/tests/test-evidence-lanes.toml:96-96 |

## Cross-Repo References

No meaningful cross-repo references found: the tests read the repository's own fixtures and a temporary directory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): created this card for the new file MIK-R04 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
