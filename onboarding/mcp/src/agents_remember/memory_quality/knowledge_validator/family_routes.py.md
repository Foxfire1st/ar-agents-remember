# mcp/src/agents_remember/memory_quality/knowledge_validator/family_routes.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The route design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`, §4.2) and the
requirement packet `MIK-R04@v2` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The route state, the coverage test and the mechanical suggestion.

- Realization entries only, located by the source path of their sidecar. [1]
- A route covers a path by prefix; the root route covers every path. [2]
- One family's route state: retired, unrealized, unassigned, uncovered, emptied, routeless. [3]
- The suggestion is labelled mechanical and lists root-level realization files. [4]
- Siblings collapse into a parent only when it holds nothing but family code. [5]
- The mechanical suggestion, and its family-record form. [6]
- The suggestion's five parametrised cases. [7]
- The root route is suggested only for a realization at the root. [8]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one parsed memory tree and a set of code paths the caller supplies.

No cross-repo boundary is crossed by this file.
