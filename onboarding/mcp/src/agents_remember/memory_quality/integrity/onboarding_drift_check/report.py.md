# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/report.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`report.py` renders drift results and resolves the report output path. It is the
reporter/formatter for the package: output only, no discovery or policy.

## Code Commentary

### Logic

`counts` tallies classifications; `write_markdown_report` builds the Markdown
report (summary + actionable findings); `print_text`/`print_json`/`print_csv`
emit stdout formats; `resolve_report_path` decides the output path;
`sanitize_report_token` and `default_report_*` derive default filenames.

Two git facts reach the rendered output, and since 260731-EFA-L3 they arrive by different routes.
The report header's HEAD stamp is read here through the single kernel runner —
`head = run_git(repo_root, ["rev-parse", "--short", "HEAD"])`, with the literal `unknown`
substituted when that call fails, so a git failure degrades the header instead of aborting the
report. The branch name in the default filename still comes from `git_ops.current_branch_name`.
`run_git` is imported from `agents_remember.kernel.git_command`; it used to be imported from
`git_ops`, which no longer defines it.

### Conventions

Report paths are redirected back to the coordination temp area when callers point
at durable memory, so temporary drift reports never land inside a memory repo.

### Invariants And Boundaries

- Output only: it must not discover, mutate, or make classification decisions.
- Durable memory repo paths are not valid locations for temporary drift reports.

## Evidence

### Repo-Internal References

- The drift summary and CLI facade call these renderers and the path resolver. [1]
- Branch facts (`current_branch_name`, for the default report filename) come from `git_ops`. [2]
- The HEAD stamp in `write_markdown_report` runs on the single kernel git runner. [3]
