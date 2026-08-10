# mcp/tests/test_sprint_role_seats.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_sprint_role_seats.py`             |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-08-10T04:39+02:00                            |
| lastVerifiedCommitHash | `a84add4c9422b18a26f1748dedaed16194994ded`        |
| lastVerifiedCommitDate | 2026-08-10T05:11:18+02:00|
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
| Two independent sprint topologies produce distinct bound architect and orchestrator rows and exact architect owners. | `test_two_live_sprints_keep_named_seats_and_custody_separate` | mcp/tests/test_sprint_role_seats.py:64-99 |
| Missing, invalid, partial, and conflicting scope is refused while valid descendants inherit and reopen remains write-once. | `test_named_roles_require_or_inherit_a_sprint_binding`; `test_policy_refuses_partial_unknown_and_conflicting_scope_inputs`; `test_spawn_scope_is_write_once_across_a_respawn` | mcp/tests/test_sprint_role_seats.py:101-220 |
| Leafless architect custody is resolved by stored sprint provenance without a global fallback. | `test_scope_binding_routes_a_leafless_architect_without_global_fallback` | mcp/tests/test_sprint_role_seats.py:222-269 |
| Rebinding a stale manager selects only the live orchestrator in the row's exact sprint. | `test_rebind_resolves_only_the_orchestrator_in_the_row_sprint` | mcp/tests/test_sprint_role_seats.py:271-331 |

## Cross-Repo References

No cross-repository boundary is owned by this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-10T04:39+02:00 — 260713-TES-L6: created the one-to-one onboarding card for concurrent-
  sprint binding, refusal, write-once, custody, and rebind regressions. Verification metadata will
  be stamped by closeout after the source commit exists.
