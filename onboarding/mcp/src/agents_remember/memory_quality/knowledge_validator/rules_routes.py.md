# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R04's six family route rules in the validator's one registry (MIK-R22 rule 9).** Importing the module registers `ROUTE_RULES`; `validator.py` imports it next to MIK-R22's rule modules, so every place the validator runs (`validate_tree`, `require_valid_commit`, the managed sync, `knowledge-validate`) runs these rules too. Three refuse and three are report-only.

## Code Commentary

### Logic

- `_families` yields every parsed family record with its `FamilyRouteState` (from `family_routes`) over the tree's realization locations.
- `R04.1-route-directory` (refuses, `writer_reports`): a route the candidate **adds** must be a directory of the paired code tree (`CodeTree.has_directory`). A route is *carried* when the same family lists it in any comparison base (K_B, or either merge parent; `_base_family_routes` unions all bases that parse).
- `R04.1-carried-route-absent` (**report-only**): a carried route whose directory is absent is reported as `route_path_absent` for the route-maintenance pass (MIK-R06), not refused. This is the same split MIK-R22 rule 6 makes for anchors (ruling Q1).
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

The six rules, the carried-route computation and their registration.

| Finding | Anchor | Source |
| --- | --- | --- |
| Carried routes are the union of every base's family routes. | `_base_family_routes` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py:58-71 |
| Absent routes, skipped for a conversion, a missing code tree and a retired family. | `_absent_routes` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py:83-93 |
| An added route is refused, a carried one reported. | `check_route_directories`; `check_carried_route_absent` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py:96-104; mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py:107-116 |
| Coverage and Non-empty name the family, the route and the uncovered path. | `check_coverage`; `check_non_empty` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py:119-137; mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py:140-149 |
| The two reported states. | `check_unrealized_family`; `check_route_unassigned` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py:152-160; mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py:163-171 |
| The six registered rules, three report-only and three writer-reported. | `ROUTE_RULES` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_routes.py:174-217 |
| An added route must be a directory; a carried one is reported. | `test_an_added_route_must_be_a_directory_of_the_code_tree`; `test_a_carried_route_whose_directory_is_gone_is_reported_not_refused` | mcp/tests/test_knowledge_family_routes.py:190-201; mcp/tests/test_knowledge_family_routes.py:204-215 |
| At a merge, a route carried by either parent is carried. | `test_at_a_merge_a_route_carried_by_either_parent_is_carried` | mcp/tests/test_knowledge_family_routes.py:218-234 |
| A route holding only a proof entry violates Non-empty. | `test_a_route_holding_only_a_proof_entry_violates_non_empty` | mcp/tests/test_knowledge_family_routes.py:154-166 |

## Cross-Repo References

No meaningful cross-repo references found: the rules read one memory tree, its bases and one paired code tree, all addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): created this card for the new file MIK-R04 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
