# mcp/tests/test_knowledge_family_routes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_family_routes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
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
- **The legacy count in the pins (leaf 260928-MIK-L27).** Since MIK-R27 registers its admission rules, every validation of the fixture tree carries one report-only `R27.4-legacy-unassessed` count (`LEGACY_COUNT`), because the Doc14 family is an export. The eight pins that expected no violation or an exact report-only set now include it and stay exact: the Doc14 example, the carried-route case, the standalone conversion, both root-route cases, and the two reported-state cases, whose `reports[0]` lookups now select the report by rule because the count sorts first. By ruling 22:11:24 Q4 (review F6), whichever of L06 and L27 lands second makes its own new pins over this tree include the count.
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
| The Doc14 family example validates, and a proof is not a location. | `test_the_doc14_family_example_validates_with_every_route_holding_realizations` | mcp/tests/test_knowledge_family_routes.py:99-124 |
| Coverage and Non-empty violations name the family, the route and the path. | `test_a_realization_outside_every_route_violates_coverage_naming_family_and_path`; `test_a_route_that_no_longer_contains_a_realization_violates_non_empty` | mcp/tests/test_knowledge_family_routes.py:132-140; mcp/tests/test_knowledge_family_routes.py:143-152 |
| One broad route passes; the suggestion offers local routes. | `test_one_broad_route_satisfies_the_rules_and_the_suggestion_offers_the_local_ones` | mcp/tests/test_knowledge_family_routes.py:170-183 |
| Route spellings: `.` or a repository path. | `test_a_family_route_is_a_repository_path_or_the_root_route` | mcp/tests/test_knowledge_family_routes.py:281-287 |
| The root route covers a root-level realization, and a family whose only route is `.` is non-empty; each validation's only finding is the report-only legacy count. | `test_the_root_route_covers_a_realization_at_the_repository_root`; `test_the_root_route_alone_is_non_empty_whenever_the_family_is_realized` | mcp/tests/test_knowledge_family_routes.py:290-299; mcp/tests/test_knowledge_family_routes.py:302-305 |
| The reported states and the retired exemption. | `test_an_unrealized_family_is_reported_and_non_empty_is_waived`; `test_an_exported_family_without_routes_is_route_unassigned_and_coverage_is_waived`; `test_a_retired_family_is_exempt_from_every_route_rule` | mcp/tests/test_knowledge_family_routes.py:313-321; mcp/tests/test_knowledge_family_routes.py:333-341; mcp/tests/test_knowledge_family_routes.py:355-362 |
| A family without routes that is not an unassessed export violates Coverage. | `test_a_family_without_routes_that_is_not_legacy_unassessed_violates_coverage`; `test_an_unrealized_family_still_needs_a_route_unless_it_is_an_unassessed_export` | mcp/tests/test_knowledge_family_routes.py:344-352; mcp/tests/test_knowledge_family_routes.py:324-330 |
| A standalone conversion checks no route directory: with no code tree it passes, reporting only the legacy count. | `test_a_standalone_conversion_checks_no_route_directory` | mcp/tests/test_knowledge_family_routes.py:262-265 |
| The lane registration. | "mcp/tests/test_knowledge_family_routes.py" | mcp/tests/test-evidence-lanes.toml:97-97 |

## Cross-Repo References

No meaningful cross-repo references found: the tests read the repository's own fixtures and a temporary directory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`test-evidence-lanes.toml`) moved with the leaf's inserted lines: 1 row(s) re-pointed by the installed fixer (its generated bullets kept). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:27:41+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_routes.py" repointed to mcp/tests/test-evidence-lanes.toml:97-97. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T00:17:15+02:00 — 260928-MIK-L27 curator (uncommitted change set on `ar/260928-mik-l27`, code base `46ca74302e76cf40fb6370ea9ece16d8fa719f00` plus the staged delta): **body update — the pins include MIK-R27's `LEGACY_COUNT` (ruling Q4).** A Logic bullet states it. **The two reopened claims** (`test_a_standalone_conversion_checks_no_route_directory` and `test_the_root_route_alone_is_non_empty_whenever_the_family_is_realized`) were re-read, reworded to say the only finding is the report-only count, and re-measured (`262-265`; `290-299`, `302-305`). The other rows were re-pointed by the exact line shifts. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): created this card for the new file MIK-R04 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
