# mcp/tests/test_dependency_ownership_ast_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dependency_ownership_ast_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `db57101a9001ede8c681ff9de4eb0147d8b636bc` |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Proves pytest-plugin and shared-support dependency discovery and the exact test-ownership
vocabulary: complete ownership is expressed through typed unresolved inputs, never through a
single freshness reason or an inferred safe-full population.

## Code Commentary

### Logic

The cases force AST assignment forms, relative imports, recursive plugin declarations, literal
module consumers, and attributed consumer reasons. Nested static plugin edges expand to the full
test population; a dynamic nested declaration makes ownership incomplete instead of being guessed.
The Codex starter-config case proves its narrow non-Python declaration against the repository's
observed literal readers and resolves exactly the public-surface and starter-renderer tests. The
root layer-contract case independently proves the composed path identity resolves exactly the five
architecture and structural-policy readers.

L19 changed the incomplete-ownership assertion vocabulary: `impact.fresh_rerun_reason` is gone and
the tests now assert `impact.unresolved_inputs` (including the `import-graph-invalid` detail) and an
empty test population when ownership is incomplete. The affected-test population therefore never
expands to a safe-full fallback; an incompletely owned change publishes an empty exact
population (or the selector's typed ownership failure) instead.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.
- Complete ownership is proven by an empty `unresolved_inputs` set; incomplete ownership is a
  typed list of unresolved input reasons, not a broad rerun reason.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned test contract. | `test_file_imports_includes_python_and_declared_pytest_plugins` | mcp/tests/test_dependency_ownership_ast_helpers.py:1-194 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Static imports, recursive plugin closure, dynamic-declaration refusal, path-loaded owners, and dotted literal consumers are all forced here. | `test_file_imports_includes_python_and_declared_pytest_plugins`; `test_nested_pytest_plugin_edges_reach_the_complete_test_population`; `test_dynamic_nested_plugin_declaration_refuses_complete_ownership`; `test_imported_support_reaches_a_test_that_loads_its_owner_by_literal_path`; `test_exact_dotted_module_literal_is_an_observable_test_consumer` | mcp/tests/test_dependency_ownership_ast_helpers.py:20-180 |
| The root layer contract resolves completely to the exact five source-observed consumers. | `test_layers_contract_has_exact_observed_consumers` | mcp/tests/test_dependency_ownership_ast_helpers.py:202-222 |
| Incomplete ownership is asserted as typed unresolved inputs with a non-expanded population. | `test_dynamic_nested_plugin_declaration_refuses_complete_ownership` | mcp/tests/test_dependency_ownership_ast_helpers.py:97-121 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `test_file_imports_includes_python_and_declared_pytest_plugins` | mcp/tests/test_dependency_ownership_ast_helpers.py:1-194 |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 ownership-vocabulary
  change — `fresh_rerun_reason` assertions became `unresolved_inputs` assertions and incomplete
  ownership now resolves to an empty test population rather than a safe-full expansion.
  Verification is pinned to the owning commit.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 added the exact `layers.toml` ownership forcing
  case and confirmed the composed declaration matches all five literal readers without safe-full
  selection. Verification remains closeout-owned.

- 2026-08-30T22:33:39+02:00 — 260821-ARSPAWN-L5 added the source-observed exact
  `.codex/config.toml` consumer proof; an unobserved declaration cannot claim complete ownership.

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: expanded the memory contract to recursive static
  pytest-plugin closure, dynamic-plugin fail-closed behavior, literal module consumers, and
  path-loaded owner reachability.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
