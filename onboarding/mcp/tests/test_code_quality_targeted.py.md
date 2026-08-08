# mcp/tests/test_code_quality_targeted.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_code_quality_targeted.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-08T02:00+02:00 |
| lastVerifiedCommitHash | `1b7f6f07c5ccc64627299b5d22463ef9c267e187` |
| lastVerifiedCommitDate | 2026-08-08T02:42:36+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The L17 proof suite for the change-set-scoped leaf gate: derivation selectors,
the reverse-import closure, the refusal shape, and real targeted wrapper runs.

## Code Commentary

### Logic

`TargetedScopeDerivationTests` (lines 142-359) builds real miniature
repositories (`targeted_repository`, lines 54-105) and pins the derivation:

- changed files, pyright closure, and test subset are derived from a leaf diff
  (`test_changed_files_closure_and_test_subset_are_derived`);
- a changed internal module is reached through its public import home
  (`test_internal_module_is_covered_through_its_public_import_home`);
- a changed production module with no test is refused
  (`test_changed_production_module_without_tests_is_refused`);
- string-based wiring tests are selected by whole-word module-path reference
  (`test_string_referenced_module_is_covered_by_wiring_tests`);
- tests-only, no-Python, and scripts-only change sets produce the honest
  empty/not-applicable shapes;
- import edge cases and fail-loud `ScopeError` paths (unknown base, git
  transport failure, unreadable string-reference file) are pinned.

`TargetedWrapperRunTests` (lines 360-630) drives the real wrapper contract:
every rail receives the derived scope and the derivation is printed
(`test_targeted_run_prints_derivation_and_scopes_every_rail`), radon consumes
the changed module files in a real run
(`test_radon_analyzes_the_changed_module_in_a_real_run`), and the
no-Python-changed and tests-only runs short-circuit to PASS with zero vacuous
rails (`test_no_python_changes_short_circuits_to_pass` — the regression that
removed the never-executed `unexpected_runner` closure).

### Conventions

Fixtures are real git repositories with `pyproject.toml` quality config so the
scope derives from `git ls-files`/`pytest_testpaths` exactly as production does.

### Invariants And Boundaries

- Every changed production module must have a derived test subset or the run is
  refused.
- Diff is always measured against the passed base revision.
- The suite never mocks the wrapper's scope derivation for the real-run class.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for the targeted suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wrapper contract the real-run class drives. | `quality_steps`, `run_quality_check` | mcp/src/agents_remember/code_quality/check.py:225-259; mcp/src/agents_remember/code_quality/check.py:308-361 |
| The printed derivation lines the suite asserts. | `targeted_scope_lines` | mcp/src/agents_remember/code_quality/scope_reporting.py:235-263 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new targeted-derivation suite; content derived from
  the current worktree source. Verification metadata pinned until closeout
  stamps the 260731-EFA-L17 commit.
