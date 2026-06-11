# mcp/src/agents_remember/benchmarks/runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T02:26+02:00                     |
| lastVerifiedCommitHash | `a7e160cd4381245327da7c5a52e2272b3080ebf7` |
| lastVerifiedCommitDate | 2026-05-26T02:40:22+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`runner.py` is now a compatibility facade for the benchmark prepare/run/analyze
surface. The benchmark implementation lives in `runner_modules/`, while this
module preserves the historical `agents_remember.benchmarks.runner` import path
used by MCP controllers, CLI entrypoints, and tests.

## Code Commentary

### Logic

The facade re-exports focused benchmark modules for existing callers and keeps a
small compatibility wrapper around `prepare_repo()` so tests and callers that
monkeypatch `benchmark_runner.run_command`, `benchmark_runner.remove_path`, or
`benchmark_runner.repo_has_commit` still affect repository preparation. It also
keeps `shutil`, `subprocess`, and `provider_setup` available as module
attributes because benchmark portability tests patch those old facade-level
objects.

The extracted implementation responsibilities are governed by
`runner_modules/overview.md`: manifest parsing, workspace preparation,
MCP/provider registration, Codex execution, JSONL analysis, service payloads,
and CLI wiring each live in a focused file.

### Invariants And Boundaries

- Keep this file thin; new benchmark behavior belongs in the owning
  `runner_modules` file.
- Preserve the public `agents_remember.benchmarks.runner` import surface unless
  all MCP controller and test callers are migrated in the same change.
- The facade is allowed to contain compatibility glue for monkeypatch-sensitive
  public functions, but not benchmark business logic.
- `__main__` dispatch must continue to call the extracted CLI `main()`.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The extracted implementation package owns benchmark runner behavior behind this facade. | [runner_modules overview](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/overview.md) |
| MCP benchmark tools import the facade as `benchmark_runner`. | [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |
| Benchmark portability tests patch facade-level compatibility attributes. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No configured sibling repository is required for this facade.

## Update History

- 2026-05-26T02:26+02:00: Updated after the benchmark runner implementation was split into focused `runner_modules` behind this facade.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` landed Codex `.codex` benchmark registration and default-sandbox support.
- 2026-05-24T09:23+02:00: Updated after Codex harness registration and benchmark skill exposure moved from `.agents` to `.codex`.
- 2026-05-24T08:56+02:00: Updated after benchmark prepare began writing child-workspace MCP registration and `codex_benchmark_run` gained the allowlisted `default` sandbox mode.
- 2026-05-24T06:57+02:00: Updated after F-09 made Codex benchmark host-execution policy explicit while keeping executable resolution tied to `PATH`.
- 2026-05-24T05:48+02:00: Updated after Phase 05 F-08 moved benchmark provider authority from coordinator `system/settings.json` to generated MCP/provider settings and variant-scoped provider declarations.
- 2026-05-24T00:35+02:00: Updated after benchmark controllers switched to service payload functions and structured progress messages.
- 2026-05-23T23:46+02:00: Updated after benchmark provider setup stopped reconstructing provider setup CLI arguments and started using `ProviderSetupRequest`.
- 2026-05-23T14:20+02:00: Updated after benchmark skill exposure became copy-only and stopped using the deleted `install-skills.sh` route.
- 2026-05-23T13:46+02:00: Updated after benchmark provider setup stopped invoking the deleted source `scripts/` route.
- 2026-05-23T13:09+02:00: Copied into the MCP package for Phase 04 benchmark tools.
