# mcp/tests/test_code_quality_dashboard_lint_scope.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Unit-regression tests for the dashboard oxlint JSON scope parser (`parse_oxlint_result_files`), the installed-binary runner (`oxlint_result_files`), and the `dashboard-lint` scope provenance line (`dashboard_lint_scope_line` / `dashboard_scope_line`).

## Code Commentary

`_write_fake_oxlint` builds a temporary executable shell shim at `dashboard/node_modules/.bin/oxlint` that prints a canned stdout file and exits with a chosen code, so the suite exercises the real subprocess boundary without requiring an installed Node toolchain.

The parser tests check that `parse_oxlint_result_files` deduplicates multiple diagnostics on the same file into distinct `Path` entries, accepts a clean run (`diagnostics: []`) when `number_of_files > 0`, and raises `ScopeError` on six invalid inputs: invalid JSON, non-object JSON (`[]`), `number_of_files: 0`, boolean `number_of_files: True`, non-list `diagnostics`, and diagnostic rows with an empty string `filename`.

The runner and reporting tests verify that `oxlint_result_files` and `dashboard_scope_line(tmp_path, "lint")` accept exit code `1` with findings (reporting `dashboard-lint`, `dashboard/.oxlintrc.json`, and the deduplicated finding-file count), accept exit code `0` with `0 oxlint files with findings`, and raise `ScopeReportingError` when `dashboard/.oxlintrc.json` is absent, `node_modules/.bin/oxlint` is absent, or `oxlint` exits with code `2`.

These are source-declared unit assertions; reading this card does not establish that pytest ran or passed.

## Relationships

Imports `ScopeError`, `oxlint_result_files`, and `parse_oxlint_result_files` from `agents_remember_test_support.code_quality.scope`, and `ScopeReportingError`, `dashboard_lint_scope_line`, and `dashboard_scope_line` from `agents_remember_test_support.code_quality.scope_reporting`. Registered in `unit-regression` in `mcp/tests/test-evidence-lanes.toml` and listed as an exact consumer of `mcp/tests/_user_settings_guard.py` and `mcp/tests/fixtures/repository_profiles/node/package-lock.json` in `mcp/tests/evidence-lifecycle.toml`. Distinct from `test_code_quality_check_scope.py`, which covers Python and general wrapper scope rather than the dashboard oxlint JSON scope contract.

## Evidence

- Temporary executable fake `oxlint` shim writes canned stdout and exit code under `node_modules/.bin/oxlint`. [1]
- Deduplicates multiple diagnostics per file into distinct finding `Path` entries. [2]
- Admits an empty `diagnostics` list when `number_of_files` is positive. [3]
- Rejects malformed JSON, non-object payloads, zero or boolean `number_of_files`, non-list `diagnostics`, and empty diagnostic `filename` with `ScopeError`. [4]
- Verifies `oxlint_result_files` and `dashboard_scope_line(..., "lint")` on exit code `1` with findings. [5]
- Verifies `dashboard_lint_scope_line` clean run (`0 oxlint files with findings`) and `ScopeReportingError` on missing `.oxlintrc.json`, missing `oxlint` binary, and exit code `2`. [6]
