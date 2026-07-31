# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/report.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/report.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T12:10+02:00                     |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7` |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `../../../../../overview.md`               |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The drift summary and CLI facade call these renderers and the path resolver. | [summary.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |
| Branch facts (`current_branch_name`, for the default report filename) come from `git_ops`. | [git_ops.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py) |
| The HEAD stamp in `write_markdown_report` runs on the single kernel git runner. | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |

## Update History

- 2026-07-31T20:56+02:00 — 260731-EFA-L3 curator: `run_git` is now imported from
  `kernel.git_command` instead of `git_ops`, which no longer defines it, so the reference row
  "Branch/HEAD facts come from `git_ops`" was half false. Split it, and documented the previously
  undocumented `rev-parse --short HEAD` stamp in `write_markdown_report` and its `unknown`
  fallback. Rendered output is unchanged.
- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
