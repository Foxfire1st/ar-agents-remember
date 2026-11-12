# mcp/test_support/agents_remember_test_support/code_quality/scope.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Derive and validate the source-quality wrapper's repository scope while keeping executable Python
scope separate from product measurement scope.

## Code Commentary

### Logic

`configured_package_authority` reads the root quality policy and requires every tracked top-level
Python package to be classified exactly once as operational product or verification
infrastructure. `derive_scope` lint/type/size-checks every tracked Python file, reads executable
tests from pytest's own `testpaths`, and gives Coverage.py/CRAP only the declared product packages.
Test and support code therefore remain checked and executed without becoming recursive
product-quality targets. Untracked exposure remains report-only and cannot silently enter the
certified index.

Module-level surface:

- `ScopeError` (class, lines 16-17) — The gate could not work out what it is supposed to certify.
- `GateScope` (class, lines 21-35) — The concrete paths each quality rail receives.
- `DashboardBuildInputs` (class, lines 39-41)
- `git_ls_files` (function, lines 44-54) — Tracked paths matching ``patterns``, relative to ``project_root``.
- `git_untracked_files` (function, lines 57-74) — Non-ignored untracked files below ``roots``, preserving all path characters.
- `top_level_packages` (function, lines 77-84) — Tracked importable packages whose parent is not itself a package.
- `toml_section` (function, lines 87-93)
- `read_pyproject` (function, lines 96-104)
- `pytest_testpaths` (function, lines 107-116) — Where the suite lives, read from pytest's own declaration.
- `validate_quality_config` (function, lines 119-169) — Refuse missing or inert configuration used by an ordinary wrapper run.
- `validate_pyright_venv` (function, lines 172-192) — Reject a declared virtual environment that cannot resolve in this checkout.
- `path_is_within` (function, lines 195-202)
- `derive_scope_roots` (function, lines 205-220) — Roots where an untracked sibling is relevant to an existing quality rail.
- `python_files_under` (function, lines 223-232) — Python files currently present below configured roots, including untracked ones.
- `eslint_result_files` (function, lines 235-278) — The exact result set resolved by the dashboard's installed ESLint.
- `config_string_array` (function, lines 281-292)
- `dashboard_build_inputs` (function, lines 295-311)
- `coverage_json_file_count` (function, lines 314-322)
- `derive_scope` (function, lines 325-345) — Derive index paths, configured roots, and report-only untracked exposure.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- Tests and shared support never enter `coverage_paths`; moving them there would recreate the
  self-certifying test-system loop removed by PDLS.
- Package authority is explicit, exhaustive, and non-overlapping; new, missing, stale, or
  dual-classified roots refuse before rail construction.
- `lint_paths`, `type_paths`, and `size_paths` still cover tracked Python source regardless of
  whether it is product or test code.
- Missing/inert configuration or empty package/test populations refuse instead of producing a
  vacuous scope.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Explicit product/verification package authority is exhaustive and non-overlapping. [1]
- Defines the class `ScopeError` (lines 16-17) — The gate could not work out what it is supposed to certify.. [2]
- Defines the class `GateScope` (lines 21-35) — The concrete paths each quality rail receives.. [3]
- Defines the class `DashboardBuildInputs` (lines 39-41). [4]
- Defines the function `git_ls_files` (lines 44-54) — Tracked paths matching ``patterns``, relative to ``project_root``.. [5]
- Defines the function `git_untracked_files` (lines 57-74) — Non-ignored untracked files below ``roots``, preserving all path characters.. [6]
- Defines the function `top_level_packages` (lines 77-84) — Tracked importable packages whose parent is not itself a package.. [7]
- Defines the function `toml_section` (lines 87-93). [8]
- Defines the function `read_pyproject` (lines 96-104). [9]
- Defines the function `pytest_testpaths` (lines 107-116) — Where the suite lives, read from pytest's own declaration.. [10]
- Defines the function `validate_quality_config` (lines 119-169) — Refuse missing or inert configuration used by an ordinary wrapper run.. [11]
- Defines the function `validate_pyright_venv` (lines 172-192) — Reject a declared virtual environment that cannot resolve in this checkout.. [12]
- Defines the function `path_is_within` (lines 195-202). [13]
- Defines the function `derive_scope_roots` (lines 205-220) — Roots where an untracked sibling is relevant to an existing quality rail.. [14]
- Defines the function `python_files_under` (lines 223-232) — Python files currently present below configured roots, including untracked ones.. [15]
- Defines the function `eslint_result_files` (lines 235-278) — The exact result set resolved by the dashboard's installed ESLint.. [16]
- Defines the function `config_string_array` (lines 281-292). [17]
- Defines the function `dashboard_build_inputs` (lines 295-311). [18]
- Defines the function `coverage_json_file_count` (lines 314-322). [19]
- Defines the function `derive_scope` (lines 325-345) — Derive index paths, configured roots, and report-only untracked exposure.. [20]
