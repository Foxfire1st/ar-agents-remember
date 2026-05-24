# mcp/src/agents_remember/benchmarks/runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T10:06+02:00                     |
| lastVerifiedCommitHash | `f48a34619fbe37c405419acfa60580b95ed8812c` |
| lastVerifiedCommitDate | 2026-05-24T10:04:28+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`runner.py` is the package-local benchmark prepare/run/analyze implementation
used by the `codex_benchmark_prepare` and `codex_benchmark_run` MCP tools.

## Code Commentary

### Logic

The module preserves the old benchmark runner behavior: selecting benchmark
cases, preparing resettable workspaces, optionally exposing skills, running
Codex prompt variants, and summarizing run artifacts.

Benchmark provider preparation now calls package-local `provider_setup` behavior
through a typed `ProviderSetupRequest` instead of a source-checkout
`scripts/provider-setup.py` file or provider setup CLI `argv` reconstruction.
Provider authority is generated from a benchmark-local `McpRuntimeConfig` shape
and temporary provider settings file, not from a benchmark coordinator
`system/settings.json`. Benchmark manifests can declare provider requirements
per variant; preparing a whole case runs the union of requested providers, while
running a selected memory-only variant skips provider setup.
Benchmark skill exposure is copy-only: `copy` is the default mode and `none`
skips harness skill exposure. The old shell/symlink installer path and `auto`
fallback mode are not part of this module anymore.

Benchmark prepare writes a child-workspace Codex MCP registration under
`<with-memory>/.codex/config.toml` plus MCP authority settings under
`<with-memory>/.codex/mcp/`. The generated settings point at the
benchmark-local coordinator, use the benchmark source checkout's parent as
`workspaceRoot`, derive the repository path through the normal MCP config
rules, and expose only the selected benchmark providers.

`prepare_benchmarks()` and `run_codex_benchmark()` are service entry points for
MCP controllers. They capture benchmark progress as structured `messages` so
dry-run evidence stays available without returning raw stdout/stderr or
requiring controllers to call `main(argv)`.

Codex benchmark execution is explicitly classified as benchmark-only host
execution. The runner resolves `codex` only from the server process `PATH`,
accepts only the allowlisted `danger-full-access` and `default` sandbox modes,
and records `codexExecutionPolicy` in service payloads and per-run metadata so
the PATH source, sandbox mode, sandbox argument, and lack of generic executable
override are visible. The `default` sandbox mode omits `--sandbox` so child
Codex uses its configured default permissions.

### Invariants And Boundaries

- MCP facades choose a configured/default benchmark root and call this module
  through service functions, not package-local command capture.
- `benchmark_prepare` and `benchmark_run` default to dry-run in the MCP surface.
- This module still carries benchmark-specific subprocess behavior; it is not a
  generic command execution surface.
- Provider setup must stay package-local; benchmark workspaces should not depend
  on deleted source-level Python scripts.
- Benchmark provider setup must not read or mutate coordinator
  `system/settings.json`; provider scope belongs to generated MCP/provider
  settings and the selected benchmark variants.
- Benchmark skill exposure must not call coordinator-local scripts or require
  Bash/symlink support.
- Codex benchmark execution must stay Codex-specific and `PATH`-resolved; do
  not add a caller-supplied executable path or generic shell command surface.
- Benchmark MCP registration belongs under the resettable child workspace
  `.codex` folder, outside the benchmark-local coordinator root.
- `codex_sandbox` is an allowlist, not a free-form Codex CLI flag tunnel.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Benchmark MCP tools call this module through `prepare_benchmarks()` and `run_codex_benchmark()`. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Provider setup is now package-local MCP code. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |
| Benchmark portability tests assert workspace-local MCP registration, Codex `PATH` resolution, default-sandbox omission, and benchmark-only run metadata. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

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
