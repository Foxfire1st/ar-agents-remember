# mcp/src/agents_remember/benchmarks/runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T14:20+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`runner.py` is the package-local benchmark prepare/run/analyze implementation
used by the Phase 04 `benchmark_prepare` and `benchmark_run` MCP tools.

## Code Commentary

### Logic

The module preserves the old benchmark runner behavior: selecting benchmark
cases, preparing resettable workspaces, optionally exposing skills, running
Codex prompt variants, and summarizing run artifacts.

Benchmark provider preparation now calls package-local `provider_setup` behavior
instead of a source-checkout `scripts/provider-setup.py` file.
Benchmark skill exposure is copy-only: `copy` is the default mode and `none`
skips harness skill exposure. The old shell/symlink installer path and `auto`
fallback mode are not part of this module anymore.

### Invariants And Boundaries

- MCP facades choose a configured/default benchmark root and call this module
  through package-local command capture.
- `benchmark_prepare` and `benchmark_run` default to dry-run in the MCP surface.
- This module still carries benchmark-specific subprocess behavior; it is not a
  generic command execution surface.
- Provider setup must stay package-local; benchmark workspaces should not depend
  on deleted source-level Python scripts.
- Benchmark skill exposure must not call coordinator-local scripts or require
  Bash/symlink support.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Benchmark MCP tools call this module through `run_package_main()`. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Provider setup is now package-local MCP code. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |

## Update History

- 2026-05-23T14:20+02:00: Updated after benchmark skill exposure became copy-only and stopped using the deleted `install-skills.sh` route.
- 2026-05-23T13:09+02:00: Copied into the MCP package for Phase 04 benchmark tools.
- 2026-05-23T13:46+02:00: Updated after benchmark provider setup stopped invoking the deleted source `scripts/` route.
