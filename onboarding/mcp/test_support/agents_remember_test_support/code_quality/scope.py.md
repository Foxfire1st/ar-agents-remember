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
certified index. For dashboard lint provenance, `oxlint_result_files` runs
`dashboard/node_modules/.bin/oxlint --format json .` (admitting exit codes `0` and `1` only) and
delegates to `parse_oxlint_result_files`, which verifies positive integer `number_of_files` and a
valid `diagnostics` list before returning deduplicated finding paths.

Module-level surface:

- `ScopeError` (class, lines 16-17) — The gate could not work out what it is supposed to certify.
- `GateScope` (class, lines 20-36) — The concrete paths each quality rail receives.
- `DashboardBuildInputs` (class, lines 39-42)
- `PackageAuthority` (class, lines 45-50) — Exhaustive ownership of importable packages for behavioral quality rails.
- `git_ls_files` (function, lines 53-63) — Tracked paths matching ``patterns``, relative to ``project_root``.
- `git_untracked_files` (function, lines 66-83) — Non-ignored untracked files below ``roots``, preserving all path characters.
- `top_level_packages` (function, lines 86-93) — Tracked importable packages whose parent is not itself a package.
- `configured_package_authority` (function, lines 96-134) — Resolve every importable package through explicit operational ownership.
- `toml_section` (function, lines 160-166)
- `read_pyproject` (function, lines 169-177)
- `pytest_testpaths` (function, lines 180-189) — Where the suite lives, read from pytest's own declaration.
- `file_size_armed` (function, lines 192-208) — Whether the wrapper's file-size rail fails the run on a violation.
- `validate_quality_config` (function, lines 211-261) — Refuse missing or inert configuration used by an ordinary wrapper run.
- `validate_pyright_venv` (function, lines 264-284) — Reject a declared virtual environment that cannot resolve in this checkout.
- `path_is_within` (function, lines 287-294)
- `derive_scope_roots` (function, lines 297-312) — Roots where an untracked sibling is relevant to an existing quality rail.
- `python_files_under` (function, lines 315-324) — Python files currently present below configured roots, including untracked ones.
- `parse_oxlint_result_files` (function, lines 327-366) — Parse oxlint JSON output into distinct files with findings.
- `oxlint_result_files` (function, lines 369-390) — The distinct files with findings reported by the dashboard's installed oxlint.
- `config_string_array` (function, lines 393-404)
- `dashboard_build_inputs` (function, lines 407-423)
- `coverage_json_file_count` (function, lines 426-434)
- `derive_scope` (function, lines 437-460) — Derive authority-aware rail inputs and report-only untracked exposure.

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
- `oxlint_result_files` and `parse_oxlint_result_files` refuse missing `node_modules/.bin/oxlint`,
  exit codes outside `{0, 1}`, invalid JSON, non-object payloads, non-integer/boolean or `<= 0`
  `number_of_files`, non-list `diagnostics`, and diagnostic entries lacking a non-empty string
  `filename`.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Explicit product/verification package authority is exhaustive and non-overlapping. [1]
- Defines the class `ScopeError` (lines 16-17) — The gate could not work out what it is supposed to certify.. [2]

- Defines the class `GateScope` (lines 20-36) — The concrete paths each quality rail receives. [3]
- Defines the class `DashboardBuildInputs` (lines 39-42). [4]
- Defines the function `git_ls_files` (lines 53-63) — Tracked paths matching `patterns`, relative to `project_root`. [5]
- Defines the function `git_untracked_files` (lines 66-83) — Non-ignored untracked files below `roots`, preserving all path characters. [6]
- Defines the function `top_level_packages` (lines 86-93) — Tracked importable packages whose parent is not itself a package. [7]
- Defines the function `toml_section` (lines 160-166). [8]
- Defines the function `read_pyproject` (lines 169-177). [9]
- Defines the function `pytest_testpaths` (lines 180-189) — Where the suite lives, read from pytest's own declaration. [10]
- Defines the function `validate_quality_config` (lines 211-261) — Refuse missing or inert configuration used by an ordinary wrapper run. [11]
- Defines the function `validate_pyright_venv` (lines 264-284) — Reject a declared virtual environment that cannot resolve in this checkout. [12]
- Defines the function `path_is_within` (lines 287-294). [13]
- Defines the function `derive_scope_roots` (lines 297-312) — Roots where an untracked sibling is relevant to an existing quality rail. [14]
- Defines the function `python_files_under` (lines 315-324) — Python files currently present below configured roots, including untracked ones. [15]
- Defines the functions `parse_oxlint_result_files` (lines 327-366) and `oxlint_result_files` (lines 369-390) — parse oxlint JSON output and return distinct files with findings from the dashboard's installed oxlint. [16]
- Defines the function `config_string_array` (lines 393-404). [17]
- Defines the function `dashboard_build_inputs` (lines 407-423). [18]
- Defines the function `coverage_json_file_count` (lines 426-434). [19]
- Defines the function `derive_scope` (lines 437-460) — Derive authority-aware rail inputs and report-only untracked exposure. [20]
