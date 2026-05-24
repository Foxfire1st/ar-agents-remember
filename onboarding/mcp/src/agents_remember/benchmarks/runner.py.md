# mcp/src/agents_remember/benchmarks/runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T00:35+02:00                     |
| lastVerifiedCommitHash | `ddf6fcd5981664813c915e94e1c5229b542a28a4` |
| lastVerifiedCommitDate | 2026-05-24T00:25:39+02:00|
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
through a typed `ProviderSetupRequest` instead of a source-checkout
`scripts/provider-setup.py` file or provider setup CLI `argv` reconstruction.
Benchmark skill exposure is copy-only: `copy` is the default mode and `none`
skips harness skill exposure. The old shell/symlink installer path and `auto`
fallback mode are not part of this module anymore.

`prepare_benchmarks()` and `run_codex_benchmark()` are service entry points for
MCP controllers. They capture benchmark progress as structured `messages` so
dry-run evidence stays available without returning raw stdout/stderr or
requiring controllers to call `main(argv)`.

### Invariants And Boundaries

- MCP facades choose a configured/default benchmark root and call this module
  through service functions, not package-local command capture.
- `benchmark_prepare` and `benchmark_run` default to dry-run in the MCP surface.
- This module still carries benchmark-specific subprocess behavior; it is not a
  generic command execution surface.
- Provider setup must stay package-local; benchmark workspaces should not depend
  on deleted source-level Python scripts.
- Benchmark provider setup still reads benchmark-local generated
  `system/settings.json` fixture data; that remaining authority-shape cleanup is
  tracked separately by Phase 05 F-08.
- Benchmark skill exposure must not call coordinator-local scripts or require
  Bash/symlink support.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Benchmark MCP tools call this module through `prepare_benchmarks()` and `run_codex_benchmark()`. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Provider setup is now package-local MCP code. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |

## Update History

- 2026-05-24T00:35+02:00: Updated after benchmark controllers switched to service payload functions and structured progress messages.
- 2026-05-23T23:46+02:00: Updated after benchmark provider setup stopped reconstructing provider setup CLI arguments and started using `ProviderSetupRequest`.
- 2026-05-23T14:20+02:00: Updated after benchmark skill exposure became copy-only and stopped using the deleted `install-skills.sh` route.
- 2026-05-23T13:46+02:00: Updated after benchmark provider setup stopped invoking the deleted source `scripts/` route.
- 2026-05-23T13:09+02:00: Copied into the MCP package for Phase 04 benchmark tools.
