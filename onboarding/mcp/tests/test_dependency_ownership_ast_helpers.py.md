# mcp/tests/test_dependency_ownership_ast_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dependency_ownership_ast_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Proves pytest-plugin and shared-support dependency discovery.

## Code Commentary

### Logic

The cases force AST assignment forms, relative imports, recursive plugin declarations, literal
module consumers, and attributed consumer reasons. Nested static plugin edges expand to the full
test population; a dynamic nested declaration makes ownership incomplete instead of being guessed.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.

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
| Static imports, recursive plugin closure, dynamic-declaration refusal, path-loaded owners, and dotted literal consumers are all forced here. | `test_file_imports_includes_python_and_declared_pytest_plugins`; `test_nested_pytest_plugin_edges_reach_the_complete_test_population`; `test_dynamic_nested_plugin_declaration_refuses_complete_ownership`; `test_imported_support_reaches_a_test_that_loads_its_owner_by_literal_path`; `test_exact_dotted_module_literal_is_an_observable_test_consumer` | mcp/tests/test_dependency_ownership_ast_helpers.py:1-194 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `test_file_imports_includes_python_and_declared_pytest_plugins` | mcp/tests/test_dependency_ownership_ast_helpers.py:1-194 |

## Update History

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: expanded the memory contract to recursive static
  pytest-plugin closure, dynamic-plugin fail-closed behavior, literal module consumers, and
  path-loaded owner reachability.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
