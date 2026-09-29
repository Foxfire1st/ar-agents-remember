# mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R04's family route logic, written once so the validator's rules and, later, the route-maintenance worklist (MIK-R06) both read it.** A family record owns `routes`: repository directories where part of the family's code lives (D12, D20). The directory tree is the route hierarchy; there is no route registry and no parent edge. The module computes one family's route state against its members' realization entries, and the mechanical route suggestion of rule 3.

## Code Commentary

### Logic

- `realization_locations(sidecars)` maps each invariant ID to its `RealizationLocation`s (entry ID, invariant, source path, sidecar path), read from the `realizes` entries of the file sidecars of the same memory tree. `proves` entries are never read: tests live in their own directories and do not count.
- `route_covers(route, path)` is a pure path-prefix test (`path` lies under `route/`); the root route `.` (`ROOT_ROUTE_PATH`) covers every path.
- `FamilyRouteState(family, locations)` holds the family record and its members' locations (`family_route_state` gathers them). Its properties:
  - `retired`: the family's status is `retired`; neither rule applies.
  - `unrealized` (`unrealized_family`): no member has a realization entry; Non-empty is waived.
  - `unassigned` (`route_unassigned`): `routes: []` with `admission: legacy-unassessed`, which only the export (MIK-R24) produces; Coverage is waived.
  - `uncovered`: when Coverage applies, the locations under no route.
  - `emptied`: when Non-empty applies, the routes that contain no location.
  - `routeless`: Coverage applies and the family lists no route at all, a Coverage violation.
- **The mechanical suggestion.** `suggest_routes(family, realization_paths, code_files)` starts from the directories of the realization files and drops any directory that lies under another one. `_collapse_once` then replaces a group of two or more sibling directories with their parent, deepest parents first, only when every code file under that parent is a realization file of the family (`_only_family_code`); this repeats until nothing collapses. Collapsing never reaches the repository root. The root route `.` is added only when a realization file lies directly at the root, where nothing narrower covers it; those files are also listed in `at_repository_root`.
- `RouteSuggestion` carries `family`, `routes`, `at_repository_root` and `label`, a `Literal["mechanical"]` (`MECHANICAL`); `to_document` renders it for the `knowledge-routes` command. `suggest_family_routes` runs `suggest_routes` over a family record's state.

### Conventions

- Pure functions and frozen dataclasses over the parsed tree; the module imports only its own package and `models.knowledge_files`.
- "Family code" in the collapse step means a file that holds a realization entry of one of the family's members (worker gap 5, accepted).

### Invariants And Boundaries

- Coverage and Non-empty are evaluated over the realization entries of the same tree; a proof entry never satisfies Non-empty.
- A retired family is exempt from every route rule (ruling Q2), including route existence.
- An exported family with `routes: []` and no realization reports both `route_unassigned` and `unrealized_family`.
- The suggestion is offered, never written by itself: nothing here writes a route, and the curator places routes as deep as makes sense.
- The suggestion never proposes the root except for a realization file at the root (ruling Q3).

### Todos

MIK-R06 is expected to reuse `family_route_state` and `suggest_family_routes` for its route-maintenance item facts.

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

The route state, the coverage test and the mechanical suggestion.

| Finding | Anchor | Source |
| --- | --- | --- |
| Realization entries only, located by the source path of their sidecar. | `realization_locations` | mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py:50-63 |
| A route covers a path by prefix; the root route covers every path. | `route_covers` | mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py:66-69 |
| One family's route state: retired, unrealized, unassigned, uncovered, emptied, routeless. | `FamilyRouteState`; `family_route_state` | mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py:73-132; mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py:135-141 |
| The suggestion is labelled mechanical and lists root-level realization files. | `RouteSuggestion` | mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py:150-169 |
| Siblings collapse into a parent only when it holds nothing but family code. | `_only_family_code`; `_collapse_once` | mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py:180-184; mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py:187-198 |
| The mechanical suggestion, and its family-record form. | `suggest_routes`; `suggest_family_routes` | mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py:201-223; mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py:226-234 |
| The suggestion's five parametrised cases. | `test_the_mechanical_suggestion` | mcp/tests/test_knowledge_family_routes.py:363-404 |
| The root route is suggested only for a realization at the root. | `test_the_root_route_is_suggested_only_for_a_realization_at_the_repository_root` | mcp/tests/test_knowledge_family_routes.py:407-412 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads one parsed memory tree and a set of code paths the caller supplies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): created this card for the new file MIK-R04 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
