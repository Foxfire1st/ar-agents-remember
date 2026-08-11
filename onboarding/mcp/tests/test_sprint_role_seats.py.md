# mcp/tests/test_sprint_role_seats.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_sprint_role_seats.py`             |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-08-10T04:39+02:00                            |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`        |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                     |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

This suite is the end-to-end regression boundary for sprint-local named command seats. It composes
the real spawn application path, terminal catalog, binding policy, signal routing, and inbox owner
resolution to prove two concurrent sprints cannot share or steal architect/orchestrator/manager
identity.

## Code Commentary

### Logic

The fixture creates two repositories/sprints and a detected hosted harness. The matrix proves
successful architect and descendant orchestrator binding, required/conflicting-scope refusals,
invalid/partial input handling, write-once reopen behavior, exact-sprint architect custody, and
rebind of an old manager only to the live orchestrator in that row's sprint. Refusal cases assert
that no terminal host is ensured, keeping the test non-vacuous at the side-effect boundary.

### Conventions

All named seat ids encode their test sprint for readability, but assertions use persisted
`spawn_repo`/`spawn_sprint` and routed owner ids rather than labels. The suite reuses the production
spawn test harness instead of duplicating a second fake catalog/open path.

### Invariants And Boundaries

- Two simultaneous sprints retain distinct named command-seat provenance and custody.
- Named roles cannot be spawned globally or rebound across a sprint boundary.
- Existing valid provenance survives reopen and conflict attempts.
- Routing assertions exercise the existing `derive_architect_owner` and `derive_row_owner`
  functions; this suite does not define a parallel owner resolver.

### Todos

No known follow-up is required.

## Docs References

No external domain documentation is needed; the suite verifies repository-owned runtime behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found after checking the configured source registry, which contains no Domain Documentation entries. | n/a | n/a |

## Repo-Internal References

The test source provides executable proof across the binding and routing seams.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sprint roles share one sprint document while remaining distinct role seats; identical roles on different repository sprints never cross. | `test_sprint_roles_share_document_but_remain_distinct_role_seats`; `test_same_role_on_different_sprints_never_crosses_repository_scope` | mcp/tests/test_sprint_role_seats.py:140-167 |
| Structural authorization pins architect children to sprint roles, orchestrator children to sprint specialists and direct-master managers, and manager children to leaf roles inside its master. | `test_architect_children_are_only_its_sprint_coordination_roles`; `test_orchestrator_owns_sprint_specialist_and_one_manager_per_direct_master`; `test_manager_owns_only_leaf_roles_inside_its_master` | mcp/tests/test_sprint_role_seats.py:169-198 |
| Replacing a role changes only the current occupant; the document-and-role seat identity remains stable. | `test_replacement_changes_only_the_current_occupant` | mcp/tests/test_sprint_role_seats.py:200-208 |
| Duplicate current occupants and role-altitude mismatches fail closed before any arbitrary selection. | `test_duplicate_current_occupants_fail_closed`; `test_role_altitude_mismatch_fails_before_any_occupant_lookup` | mcp/tests/test_sprint_role_seats.py:210-219 |

## Cross-Repo References

No cross-repository boundary is owned by this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_sprint_role_seats.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: created the one-to-one onboarding card for concurrent-
  sprint binding, refusal, write-once, custody, and rebind regressions. Verification metadata will
  be stamped by closeout after the source commit exists.
