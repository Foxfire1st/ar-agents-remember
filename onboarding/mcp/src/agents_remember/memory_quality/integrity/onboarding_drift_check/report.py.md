# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/report.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/report.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T12:10+02:00                     |
| lastVerifiedCommitHash | `12737deaac2fd75563ca1e3037cdac911023cf93` |
| lastVerifiedCommitDate | 2026-05-29T12:28:42+02:00|
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

### Conventions

Report paths are redirected back to the coordination temp area when callers point
at durable memory, so temporary drift reports never land inside a memory repo.

### Invariants And Boundaries

- Output only: it must not discover, mutate, or make classification decisions.
- Durable memory repo paths are not valid locations for temporary drift reports.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The drift summary and CLI facade call these renderers and the path resolver. | [summary.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |
| Branch/HEAD facts come from `git_ops`. | [git_ops.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py) |

## Update History

- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
