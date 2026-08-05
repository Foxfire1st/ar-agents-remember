# mcp/src/agents_remember/benchmarks/runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`runner.py` is now a compatibility facade for the benchmark prepare/run/analyze
surface. The benchmark implementation lives in `runner_modules/`, while this
module preserves the historical `agents_remember.benchmarks.runner` import path
used by MCP application entry points, CLI entrypoints, and tests.

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
  all MCP application entry point and test callers are migrated in the same change.
- The facade is allowed to contain compatibility glue for monkeypatch-sensitive
  public functions, but not benchmark business logic.
- `__main__` dispatch must continue to call the extracted CLI `main()`.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP benchmark tools import the facade as `benchmark_runner`. | "def skills_install_tool" | mcp/src/agents_remember/application/skill_tools.py:11-11 |
| Benchmark portability tests patch facade-level compatibility attributes. | `BenchmarkRunnerPortabilityTests` | mcp/tests/test_worktree_support.py:3094-3722 |

## Cross-Repo References

No configured sibling repository is required for this facade.

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors (deleting the unresolvable overview row); exact non-fixing check returns zero findings.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
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
