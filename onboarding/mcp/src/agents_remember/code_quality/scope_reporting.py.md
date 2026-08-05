# mcp/src/agents_remember/code_quality/scope_reporting.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/scope_reporting.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Render truthful scope, input, config, and unit provenance for quality rails.

## Code Commentary

### Logic

Module-level surface:

- `ScopeReportingError` (class, lines 35-36) — A provenance line could not truthfully describe its input.
- `PushUpdate` (class, lines 40-49)
- `scope_line` (function, lines 52-54) — The stable one-line output contract shared by wrapper, hooks, and CI.
- `parse_push_updates` (function, lines 57-68)
- `validate_invocation_environment` (function, lines 71-81)
- `invocation_description` (function, lines 84-105)
- `pyright_config_description` (function, lines 108-125)
- `wrapper_scope_line` (function, lines 128-143)
- `fixed_step_scope_line` (function, lines 146-186)
- `coverage_result_scope_line` (function, lines 189-196)
- `randomized_pytest_scope_line` (function, lines 199-213)
- `crap_scope_line` (function, lines 216-227)
- `diff_input_description` (function, lines 230-247)
- `diff_scope_line` (function, lines 250-264)
- `untracked_scope_lines` (function, lines 267-295)
- `generated_scope_line` (function, lines 298-324)
- `frontend_files` (function, lines 330-338)
- `read_json_object` (function, lines 341-348)
- `tsconfig_project_inputs` (function, lines 351-377)
- `tsconfig_inputs` (function, lines 380-401)
- `config_input_files` (function, lines 404-424)
- `dashboard_lint_scope_line` (function, lines 427-443)
- `dashboard_test_scope_line` (function, lines 446-465)
- `dashboard_typecheck_scope_line` (function, lines 468-474)
- `dashboard_build_scope_line` (function, lines 477-502)
- `dashboard_scope_line` (function, lines 505-523)
- `build_parser` (function, lines 526-546)
- `main` (function, lines 549-575)

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
| Defines the class `ScopeReportingError` (lines 35-36) — A provenance line could not truthfully describe its input.. | `ScopeReportingError` | mcp/src/agents_remember/code_quality/scope_reporting.py:35-36 |
| Defines the class `PushUpdate` (lines 40-49). | `PushUpdate` | mcp/src/agents_remember/code_quality/scope_reporting.py:39-49 |
| Defines the function `scope_line` (lines 52-54) — The stable one-line output contract shared by wrapper, hooks, and CI.. | `scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:52-54 |
| Defines the function `parse_push_updates` (lines 57-68). | `parse_push_updates` | mcp/src/agents_remember/code_quality/scope_reporting.py:57-68 |
| Defines the function `validate_invocation_environment` (lines 71-81). | `validate_invocation_environment` | mcp/src/agents_remember/code_quality/scope_reporting.py:71-81 |
| Defines the function `invocation_description` (lines 84-105). | `invocation_description` | mcp/src/agents_remember/code_quality/scope_reporting.py:84-105 |
| Defines the function `pyright_config_description` (lines 108-125). | `pyright_config_description` | mcp/src/agents_remember/code_quality/scope_reporting.py:108-125 |
| Defines the function `wrapper_scope_line` (lines 128-143). | `wrapper_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:128-143 |
| Defines the function `fixed_step_scope_line` (lines 146-186). | `fixed_step_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:146-186 |
| Defines the function `coverage_result_scope_line` (lines 189-196). | `coverage_result_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:189-196 |
| Defines the function `randomized_pytest_scope_line` (lines 199-213). | `randomized_pytest_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:199-213 |
| Defines the function `crap_scope_line` (lines 216-227). | `crap_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:216-227 |
| Defines the function `diff_input_description` (lines 230-247). | `diff_input_description` | mcp/src/agents_remember/code_quality/scope_reporting.py:230-247 |
| Defines the function `diff_scope_line` (lines 250-264). | `diff_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:250-264 |
| Defines the function `untracked_scope_lines` (lines 267-295). | `untracked_scope_lines` | mcp/src/agents_remember/code_quality/scope_reporting.py:267-295 |
| Defines the function `generated_scope_line` (lines 298-324). | `generated_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:298-324 |
| Defines the function `frontend_files` (lines 330-338). | `frontend_files` | mcp/src/agents_remember/code_quality/scope_reporting.py:330-338 |
| Defines the function `read_json_object` (lines 341-348). | `read_json_object` | mcp/src/agents_remember/code_quality/scope_reporting.py:341-348 |
| Defines the function `tsconfig_project_inputs` (lines 351-377). | `tsconfig_project_inputs` | mcp/src/agents_remember/code_quality/scope_reporting.py:351-377 |
| Defines the function `tsconfig_inputs` (lines 380-401). | `tsconfig_inputs` | mcp/src/agents_remember/code_quality/scope_reporting.py:380-401 |
| Defines the function `config_input_files` (lines 404-424). | `config_input_files` | mcp/src/agents_remember/code_quality/scope_reporting.py:404-424 |
| Defines the function `dashboard_lint_scope_line` (lines 427-443). | `dashboard_lint_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:427-443 |
| Defines the function `dashboard_test_scope_line` (lines 446-465). | `dashboard_test_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:446-465 |
| Defines the function `dashboard_typecheck_scope_line` (lines 468-474). | `dashboard_typecheck_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:468-474 |
| Defines the function `dashboard_build_scope_line` (lines 477-502). | `dashboard_build_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:477-502 |
| Defines the function `dashboard_scope_line` (lines 505-523). | `dashboard_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:505-523 |
| Defines the function `build_parser` (lines 526-546). | `build_parser` | mcp/src/agents_remember/code_quality/scope_reporting.py:526-546 |
| Defines the function `main` (lines 549-575). | `main` | mcp/src/agents_remember/code_quality/scope_reporting.py:549-575 |

## Update History

- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: normalized decorator-inclusive citation ranges via scoped --fix against the frozen snapshot.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
