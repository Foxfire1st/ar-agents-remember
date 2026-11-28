# mcp/test_support/agents_remember_test_support/code_quality/scope_reporting.py

## Governing Overview

[Quality support overview](overview.md)

## 260824-PDLS Current Contract

Targeted reports now print the complete `TestImpact` disposition from the canonical ownership
graph: selected paths, whether ownership is complete, whether a global input invalidated the
population, any explicit conservative-full decision, and every stable selection reason. The output may truthfully be
broad; it must explain why rather than optimizing the count. Coverage provenance separately names
product measurement units, so executed tests/support are not misreported as CRAP inputs.

## 260831-CCR-L19 Change

L19 updated the targeted-ownership wording to the exact-ownership contract: the incomplete line now
reads `targeted ownership: incomplete; Gate 2 blocked without population expansion` (it never
prints a safe-full population), and the printed ownership reasons are the flattened set of every
`test_impact.reasons` rather than only reasons nested per owned path. The report remains
read-only.

## Purpose

Render truthful scope, input, config, and unit provenance for quality rails.

## Code Commentary

### Logic

Scope lines explain actual inputs and units for full/targeted Python, hooks and dashboard rails.
`crap_scope_line` labels production scores and the diagnostic review threshold;
`diff_scope_line` labels diagnostic changed coverage without a floor. The reporting owner never
changes selection or grants acceptance.

`fixed_step_scope_line` computes the recursive `python_files_under` counts only for the steps that
report them: the Radon pair and a non-targeted pytest line. The hook's fixed steps therefore do not
walk every test and product root for a line they do not read. `_pytest_scope_line` holds the
targeted and full pytest descriptions. The `hook-batch` subcommand derives one scope and renders
every tier payload through `collect_hook_scope_batch`; `_hook_batch_report` writes each payload to
the caller's temporary directory.

- `tsconfig_project_inputs` (function, lines 496-524)
- `tsconfig_inputs` (function, lines 527-548)
- `config_input_files` (function, lines 551-571)
- `dashboard_lint_scope_line` (function, lines 574-590)
- `dashboard_test_scope_line` (function, lines 593-612)
- `dashboard_typecheck_scope_line` (function, lines 615-621)
- `dashboard_build_scope_line` (function, lines 624-649)
- `dashboard_scope_line` (function, lines 652-692)
- `build_parser` (function, lines 695-722)
- `main` (function, lines 788-798)

`tsconfig_project_inputs` accepts both direct JSON references and directory references containing
`tsconfig.json`. Each referenced project's `files` and `include` entries resolve from that config's
own directory, so nested TypeScript projects cannot be silently measured against the dashboard root.

`dashboard_lint_scope_line` requires `dashboard/.oxlintrc.json`, resolves finding files through
`oxlint_result_files` (converting `ScopeError` into `ScopeReportingError`), and reports the oxlint
config, `lint` script (`oxlint .`), and distinct count of files with findings.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- This owner is verification support under `mcp/test_support`, not shipped product source.
- Targeted reporting never claims a safe-full population; incomplete ownership is reported as a
  Gate-2 block (L19).

### Todos

None.

## Evidence

### Repo-Internal References


- The fixed-step lines defer their recursive count walks to the steps that read them. [6]

- The hook-batch subcommand renders every tier payload from one derived scope. [7]

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.


- Exact selection reasons and incomplete ownership [1]

- Production-only diagnostic review threshold label [2]
- Diagnostic diff inputs without a floor [3]
- Project-relative TypeScript file resolution [4]
- Read-only provenance reporting dispatch [5]


- Dashboard oxlint scope provenance and missing-config refusal. [8]


### Docs References

No configured Domain Documentation source applies to this read-only reporting module.

### Cross-Repo References

No meaningful cross-repository boundary is owned by this module.

## 260731-EFA-L9 Change

The scope report gained the `layering` tier: the armed package-layering step reports violation
and cycle counts/edges alongside the other quality steps, and the wrapper's invocation labels
carry the layering result.
