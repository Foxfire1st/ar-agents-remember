# mcp/tests/test_dependency_ownership_ast_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dependency_ownership_ast_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
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

The ambient-runner regression now requires exactly sixteen observed pytest consumers, no unresolved inputs, no global invalidation and attributed declared-consumer reasons. This includes the shared profile fixture closure; a narrow singleton and an unjustified whole-suite expansion both fail.

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

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| Static imports and declared pytest plugins are source evidence. | `test_file_imports_includes_python_and_declared_pytest_plugins` | mcp/tests/test_dependency_ownership_ast_helpers.py:21-50 |
| Only supported static assignment forms are accepted. | `test_pytest_plugin_ast_helpers_accept_only_assignment_string_values` | mcp/tests/test_dependency_ownership_ast_helpers.py:53-78 |
| Nested plugin ownership reaches the declared population. | `test_nested_pytest_plugin_edges_reach_the_complete_test_population` | mcp/tests/test_dependency_ownership_ast_helpers.py:81-102 |
| Dynamic plugin declarations retain typed incomplete ownership. | `test_dynamic_nested_plugin_declaration_refuses_complete_ownership` | mcp/tests/test_dependency_ownership_ast_helpers.py:105-121 |
| Literal path loading composes with imported support. | `test_imported_support_reaches_a_test_that_loads_its_owner_by_literal_path` | mcp/tests/test_dependency_ownership_ast_helpers.py:124-152 |
| Dotted module literals contribute attributed ownership. | `test_exact_dotted_module_literal_is_an_observable_test_consumer` | mcp/tests/test_dependency_ownership_ast_helpers.py:155-179 |
| Starter configuration has exactly its observed readers. | `test_codex_starter_config_has_exact_observed_consumers` | mcp/tests/test_dependency_ownership_ast_helpers.py:182-199 |
| The ambient runner selects exactly sixteen tests with no global invalidation. | `test_ambient_role_runner_has_exact_pytest_consumers` | mcp/tests/test_dependency_ownership_ast_helpers.py:202-236 |
| The layer contract selects exactly five source-observed readers. | `test_layers_contract_has_exact_observed_consumers` | mcp/tests/test_dependency_ownership_ast_helpers.py:239-259 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Recorded the exact sixteen-consumer runner regression and explicit no-global-invalidation assertions; repaired shifted layer-contract citation and reference buckets.

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
