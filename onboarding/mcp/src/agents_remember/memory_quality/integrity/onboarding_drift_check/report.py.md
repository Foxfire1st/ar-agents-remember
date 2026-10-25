# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/report.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`report.py` derives branch-aware report filenames and resolves output paths. It performs path construction/containment only, not rendering, discovery, classification or memory mutation.

## Code Commentary

### Logic

`default_report_filename` sanitizes repository and current-branch tokens; `default_report_dir/path` place reports under temp `drift-reports`. `resolve_report_path` redirects absolute durable-memory targets and absolute targets outside coordination into the default directory, preserves allowed coordination paths, and accepts relative paths only when their resolved candidate stays under temp. Escaping relative paths fall back to the default directory and requested basename.

Only branch lookup remains here through `git_ops.current_branch_name`; the converted Markdown renderer is `_write_converted_report` in `summary.py`. This module no longer reads a HEAD stamp.

### Conventions

Report paths are redirected back to the coordination temp area when callers point
at durable memory, so temporary drift reports never land inside a memory repo.

### Invariants And Boundaries

- Output only: it must not discover, mutate, or make classification decisions.
- Durable memory repo paths are not valid locations for temporary drift reports.

## Evidence

### Repo-Internal References


- The converted summary resolves its operational report path through the retained path helper; legacy renderer/CLI facade APIs are absent. [1]


- Branch facts (`current_branch_name`, for the default report filename) come from `git_ops`. [2]
