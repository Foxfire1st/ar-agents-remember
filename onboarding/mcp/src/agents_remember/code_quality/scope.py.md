# mcp/src/agents_remember/code_quality/scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Derive and validate the source-quality wrapper's repository scope.

## Code Commentary

### Logic

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

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `ScopeError` (lines 16-17) — The gate could not work out what it is supposed to certify.. | `ScopeError` | mcp/src/agents_remember/code_quality/scope.py:16-17 |
| Defines the class `GateScope` (lines 21-35) — The concrete paths each quality rail receives.. | `GateScope` | mcp/src/agents_remember/code_quality/scope.py:20-35 |
| Defines the class `DashboardBuildInputs` (lines 39-41). | `DashboardBuildInputs` | mcp/src/agents_remember/code_quality/scope.py:38-41 |
| Defines the function `git_ls_files` (lines 44-54) — Tracked paths matching ``patterns``, relative to ``project_root``.. | `git_ls_files` | mcp/src/agents_remember/code_quality/scope.py:44-54 |
| Defines the function `git_untracked_files` (lines 57-74) — Non-ignored untracked files below ``roots``, preserving all path characters.. | `git_untracked_files` | mcp/src/agents_remember/code_quality/scope.py:57-74 |
| Defines the function `top_level_packages` (lines 77-84) — Tracked importable packages whose parent is not itself a package.. | `top_level_packages` | mcp/src/agents_remember/code_quality/scope.py:77-84 |
| Defines the function `toml_section` (lines 87-93). | `toml_section` | mcp/src/agents_remember/code_quality/scope.py:87-93 |
| Defines the function `read_pyproject` (lines 96-104). | `read_pyproject` | mcp/src/agents_remember/code_quality/scope.py:96-104 |
| Defines the function `pytest_testpaths` (lines 107-116) — Where the suite lives, read from pytest's own declaration.. | `pytest_testpaths` | mcp/src/agents_remember/code_quality/scope.py:107-116 |
| Defines the function `validate_quality_config` (lines 119-169) — Refuse missing or inert configuration used by an ordinary wrapper run.. | `validate_quality_config` | mcp/src/agents_remember/code_quality/scope.py:119-169 |
| Defines the function `validate_pyright_venv` (lines 172-192) — Reject a declared virtual environment that cannot resolve in this checkout.. | `validate_pyright_venv` | mcp/src/agents_remember/code_quality/scope.py:172-192 |
| Defines the function `path_is_within` (lines 195-202). | `path_is_within` | mcp/src/agents_remember/code_quality/scope.py:215-222 |
| Defines the function `derive_scope_roots` (lines 205-220) — Roots where an untracked sibling is relevant to an existing quality rail.. | `derive_scope_roots` | mcp/src/agents_remember/code_quality/scope.py:225-240 |
| Defines the function `python_files_under` (lines 223-232) — Python files currently present below configured roots, including untracked ones.. | `python_files_under` | mcp/src/agents_remember/code_quality/scope.py:243-252 |
| Defines the function `eslint_result_files` (lines 235-278) — The exact result set resolved by the dashboard's installed ESLint.. | `eslint_result_files` | mcp/src/agents_remember/code_quality/scope.py:235-278 |
| Defines the function `config_string_array` (lines 281-292). | `config_string_array` | mcp/src/agents_remember/code_quality/scope.py:301-312 |
| Defines the function `dashboard_build_inputs` (lines 295-311). | `dashboard_build_inputs` | mcp/src/agents_remember/code_quality/scope.py:315-331 |
| Defines the function `coverage_json_file_count` (lines 314-322). | `coverage_json_file_count` | mcp/src/agents_remember/code_quality/scope.py:334-342 |
| Defines the function `derive_scope` (lines 325-345) — Derive index paths, configured roots, and report-only untracked exposure.. | `derive_scope` | mcp/src/agents_remember/code_quality/scope.py:325-345 |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: `GateScope.size_paths` = index-known Python plus `dashboard/src` TypeScript/TSX; `file_size_armed` reads the arming key (fail-closed on a non-boolean); `derive_scope` coverage roots now include the configured test roots so Coverage.py and CRAP measure the test tree. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: normalized decorator-inclusive citation ranges via scoped --fix against the frozen snapshot.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
