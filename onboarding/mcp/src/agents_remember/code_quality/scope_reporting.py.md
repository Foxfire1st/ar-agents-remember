# mcp/src/agents_remember/code_quality/scope_reporting.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/scope_reporting.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-08T02:00+02:00               |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## 260731-EFA-L8 Change

The scope report gained the dashboard rail steps and provenance lines (coverage,
diff-coverage, and e2e) forced by this leaf's S3 CI/hook wiring, plus the pinned

TypeScript input count update (349→425); the report remains read-only. The matching
hook-skip and provenance tests were reconciled in `mcp/tests/test_quality_scope_reporting.py`.

## 260731-EFA-L17 Change

The scope report gained the altitude-routed targeted tier:
`invocation_description` (lines 88-115) names `master-integration` and
`leaf-integration`; `wrapper_scope_line` (lines 136-163) and
`fixed_step_scope_line` (lines 164-234) render the targeted units (changed
files, reverse-import closure, derived test files, size-scoped changed files);
`targeted_scope_lines` (lines 235-263) prints the full derivation for review;
`diff_input_description` (lines 305-328) names the clean integration tree; and
`build_parser` (lines 627-653) accepts the `targeted` hook tier. The matching
provenance tests were extended in `mcp/tests/test_quality_scope_reporting.py`
(integration invocation labels, targeted pre-push tier).

## Purpose

Render truthful scope, input, config, and unit provenance for quality rails.

## Code Commentary

### Logic

Module-level surface:

- `ScopeReportingError` (class, lines 36-40) — A provenance line could not truthfully describe its input.
- `PushUpdate` (class, lines 41-52)
- `scope_line` (function, lines 53-57) — The stable one-line output contract shared by wrapper, hooks, and CI.
- `parse_push_updates` (function, lines 58-72)
- `validate_invocation_environment` (function, lines 73-87)
- `invocation_description` (function, lines 88-115)
- `pyright_config_description` (function, lines 116-135)
- `wrapper_scope_line` (function, lines 136-163)
- `fixed_step_scope_line` (function, lines 164-234)
- `targeted_scope_lines` (function, lines 235-263) — the printed derivation for targeted runs
- `coverage_result_scope_line` (function, lines 264-273)
- `randomized_pytest_scope_line` (function, lines 274-290)
- `crap_scope_line` (function, lines 291-304)
- `diff_input_description` (function, lines 305-328)
- `diff_scope_line` (function, lines 329-345)
- `untracked_scope_lines` (function, lines 346-376)
- `generated_scope_line` (function, lines 377-408)
- `frontend_files` (function, lines 409-419)
- `read_json_object` (function, lines 420-429)
- `tsconfig_project_inputs` (function, lines 430-458)
- `tsconfig_inputs` (function, lines 459-482)
- `config_input_files` (function, lines 483-505)
- `dashboard_lint_scope_line` (function, lines 506-524)
- `dashboard_test_scope_line` (function, lines 525-546)
- `dashboard_typecheck_scope_line` (function, lines 547-555)
- `dashboard_build_scope_line` (function, lines 556-583)
- `dashboard_scope_line` (function, lines 584-626)
- `build_parser` (function, lines 627-653)
- `main` (function, lines 690-704)

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
| Defines the class `ScopeReportingError` — a provenance line could not truthfully describe its input. | `ScopeReportingError` | mcp/src/agents_remember/code_quality/scope_reporting.py:36-40 |
| Defines the class `PushUpdate`. | `PushUpdate` | mcp/src/agents_remember/code_quality/scope_reporting.py:41-52 |
| Defines the function `scope_line` — the stable one-line output contract shared by wrapper, hooks, and CI. | `scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:53-57 |
| Defines the function `parse_push_updates`. | `parse_push_updates` | mcp/src/agents_remember/code_quality/scope_reporting.py:58-72 |
| Defines the function `validate_invocation_environment`. | `validate_invocation_environment` | mcp/src/agents_remember/code_quality/scope_reporting.py:73-87 |
| Defines the function `invocation_description`, including the L17 `master-integration` / `leaf-integration` labels. | `invocation_description` | mcp/src/agents_remember/code_quality/scope_reporting.py:88-115 |
| Defines the function `pyright_config_description`. | `pyright_config_description` | mcp/src/agents_remember/code_quality/scope_reporting.py:116-135 |
| Defines the function `wrapper_scope_line`, with the L17 targeted units branch. | `wrapper_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:136-163 |
| Defines the function `fixed_step_scope_line`, with the L17 targeted per-rail lines. | `fixed_step_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:164-234 |
| Defines the function `targeted_scope_lines` — the printed derivation for targeted runs. | `targeted_scope_lines` | mcp/src/agents_remember/code_quality/scope_reporting.py:235-263 |
| Defines the function `coverage_result_scope_line`. | `coverage_result_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:264-273 |
| Defines the function `randomized_pytest_scope_line`. | `randomized_pytest_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:274-290 |
| Defines the function `crap_scope_line`. | `crap_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:291-304 |
| Defines the function `diff_input_description`, including the integration-tree labels. | `diff_input_description` | mcp/src/agents_remember/code_quality/scope_reporting.py:305-328 |
| Defines the function `diff_scope_line`. | `diff_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:329-345 |
| Defines the function `untracked_scope_lines`. | `untracked_scope_lines` | mcp/src/agents_remember/code_quality/scope_reporting.py:346-376 |
| Defines the function `generated_scope_line`. | `generated_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:377-408 |
| Defines the function `frontend_files`. | `frontend_files` | mcp/src/agents_remember/code_quality/scope_reporting.py:409-419 |
| Defines the function `read_json_object`. | `read_json_object` | mcp/src/agents_remember/code_quality/scope_reporting.py:420-429 |
| Defines the function `tsconfig_project_inputs`. | `tsconfig_project_inputs` | mcp/src/agents_remember/code_quality/scope_reporting.py:430-458 |
| Defines the function `tsconfig_inputs`. | `tsconfig_inputs` | mcp/src/agents_remember/code_quality/scope_reporting.py:459-482 |
| Defines the function `config_input_files`. | `config_input_files` | mcp/src/agents_remember/code_quality/scope_reporting.py:483-505 |
| Defines the function `dashboard_lint_scope_line`. | `dashboard_lint_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:506-524 |
| Defines the function `dashboard_test_scope_line`. | `dashboard_test_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:525-546 |
| Defines the function `dashboard_typecheck_scope_line`. | `dashboard_typecheck_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:547-555 |
| Defines the function `dashboard_build_scope_line`. | `dashboard_build_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:556-583 |
| Defines the function `dashboard_scope_line`. | `dashboard_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:584-626 |
| Defines the function `build_parser`, including the `targeted` hook tier choice. | `build_parser` | mcp/src/agents_remember/code_quality/scope_reporting.py:627-653 |
| Defines the function `main`. | `main` | mcp/src/agents_remember/code_quality/scope_reporting.py:690-704 |

## 260731-EFA-L9 Change

The scope report gained the `layering` tier: the armed package-layering step reports violation
and cycle counts/edges alongside the other quality steps, and the wrapper's invocation labels
carry the layering result.

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: recorded the layering tier in the scope
  report; the L9 change section above documents it. Verification metadata pinned until closeout
  stamps the L9 code commit.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the targeted tier
  (invocation labels, targeted scope lines, integration-tree diff labels, the
  `targeted` hook tier), refreshed every function anchor to the post-L17
  ranges, and added the `targeted_scope_lines` row. Verification metadata stays
  pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: the file-size scope contract was added to scope reporting, and the TypeScript-input count now matches the live tsconfig project-input union (426). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the dashboard rail steps and pinned TS input count. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T13:06:07+02:00 — 260731-EFA-L6 residual curator: corrected the `main` citation from the stale range 549-575 (which holds no `main`) to the current definition extent 586-596 in the frozen code tree (HEAD 5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060).

- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: normalized decorator-inclusive citation ranges via scoped --fix against the frozen snapshot.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
