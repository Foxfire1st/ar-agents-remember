# mcp/src/agents_remember/benchmarks/runner_modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `mcp/src/agents_remember/benchmarks/runner_modules` |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Purpose

The `runner_modules` package contains the focused implementation modules behind
the public `benchmarks/runner.py` facade. It exists to keep benchmark manifest
handling, workspace setup, provider registration, Codex execution, JSONL
analysis, service payloads, and CLI wiring independently navigable and testable.

## Hot Path Summary

- `models.py`, `constants.py`, and `manifest.py` define benchmark case data,
  supported provider ids, manifest path validation, case loading, and
  prompt/variant selection.
- `filesystem.py`, `commands.py`, and `workspace.py` own benchmark workspace
  mutation: copying runtime assets, safe removal, Git checkout preparation,
  template rendering, memory repo preparation, and whole-case setup.
  `commands.py`'s `run_command` captures stdout/stderr and never inherits the
  parent's stdio (on MCP stdio transport those are the protocol pipes; 2.5.1,
  GitHub #49) — failures raise with a bounded output tail. Since 260731-EFA-L3 it
  never inherits a **git repository selector** either: both `run_command` and
  `repo_has_commit` pass `env=git_environment()` from
  `kernel/git_command.py`, which strips the eight `GIT_DIR`-family variables
  (`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
  `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`,
  `GIT_PREFIX`). The scrub covers **every** spawned command, not only the ones
  whose argv starts with `git`, because the git argv this runner spawns is
  `clone` / `checkout --detach` / `reset --hard` / `clean -fdx` against a scratch
  workspace — with `GIT_DIR` inherited, the most destructive commands in the
  package would run against whatever repository it names instead. The case manifest
  is NOT provider launch authority (containment R1, 260707-HFX-L1):
  `workspace.filter_benchmark_provider_ids` filters manifest provider ids
  against the caller's `allowed_provider_ids` — the live MCP authority set the
  benchmark application entry points always pass (`None` = no authority context, FAIL-CLOSED
  since review B4; the explicit `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1` env
  escape restores an unfiltered direct-script run) — before any workspace
  registration is written or a provider launches, and reports skipped ids
  loudly. `models.py`'s two service requests carry the field; `services.py`
  and `execution.py` thread it down to `prepare_case`.
- `mcp_registration.py` writes benchmark-local MCP/Codex configuration,
  generates provider settings with central `logs/mcp` and `logs/providers`
  paths, and invokes package-local provider setup. Benchmark provider setup is
  **hermetic-cold**: `prepare_configured_providers` wires no seed source, so a
  benchmark builds each index from its own fixture and never starts/clones the
  live workspace provider backends (task 260619). Its
  `disarm_stale_benchmark_registrations` (review B3) is the sweep both
  `services.py` entry points open with: persisted workspace registrations are
  the authority files for sessions booted in those workspaces — the one place
  the fleet kill-switch cannot reach — so every prepare/run pass narrows them
  to the live authority set (idempotent, loud per-file report, `None`
  untouched).
- `execution.py` owns Codex PATH resolution, sandbox policy, command
  construction, per-run metadata, and benchmark run orchestration; its
  `benchmark_mcp_config_overrides` points the benchmarked Codex at the
  benchmark's own MCP server.
- `analysis.py`, `services.py`, and `cli.py` own JSONL metrics, summary
  rendering, MCP service payloads, and the argparse command surface.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public facade re-exports this package for existing callers. | "def prepare_repo" | mcp/src/agents_remember/benchmarks/runner.py:28-28 |
| MCP application entry points call the benchmark service entry points through the facade. | `skills_install_tool` | mcp/src/agents_remember/application/skill_tools.py:11-28 |
| The shared seed resolvers refuse a benchmark-scoped target as defense-in-depth for the hermetic boundary. | `GrepaiSeedOptions` | mcp/src/agents_remember/providers/grepai/seed.py:30-35 |
| Focused benchmark tests exercise facade compatibility, provider setup, MCP registration, Codex execution policy, repository prep, and skill exposure behavior. | `BenchmarkRunnerPortabilityTests` | mcp/tests/test_worktree_support_benchmark.py:32-665 |

## Cross-Repo References

Benchmark cases may clone external repositories during runs, but this package's
source-level behavior is local to `agents-remember`.

## 260731-EFA-L2 Shared Runner Value Objects

`models.py` now owns five frozen value objects the runner modules are signed on:
`BenchmarkWorkspace` (a materialized case workspace), `BenchmarkTask`, `BenchmarkRun`,
`BenchmarkPreparation` and `BenchmarkRunOutcome`. The load-bearing one is `BenchmarkPreparation`:
**both** `BenchmarkPrepareRequest` and `BenchmarkRunRequest` project onto it through a `preparation`
property, so `prepare_case` takes one object and the prepare and run entry points cannot drift
apart on preparation semantics. `allowed_provider_ids` rides on it, so the containment R1
authority set still reaches `filter_benchmark_provider_ids` with its FAIL-CLOSED `None` handling
intact.

## 260731-EFA-L9 Route Impact — Caller Re-Points

The benchmark runner callers were rewritten by the L9 caller wave: `McpRuntimeConfig` imports now come from `kernel/primitives/runtime_config.py` (the former `mcp/config.py` home) and tool-report/command-capture helpers from `kernel/primitives/`. Runner behavior and benchmark case handling are unchanged.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 route impact: L9 caller/import re-points recorded and body updated.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No route impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T20:59+02:00 — 260731-EFA-L3 curator: extended the `commands.py` hot-path bullet, which
  previously recorded only the stdio-isolation half of the subprocess hygiene contract. Both
  `run_command` and `repo_has_commit` now also pass `env=git_environment()`
  (`kernel/git_command.py`), stripping the eight `GIT_DIR`-family repository selectors from every
  command this runner spawns — the workspace-prep argv (`clone`, `checkout --detach`,
  `reset --hard`, `clean -fdx`) is the reason the scrub is unconditional rather than git-only. No
  change to the module split, the containment R1 authority filter, or the L2 value objects.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: added the shared `BenchmarkWorkspace` / `BenchmarkTask`
  / `BenchmarkRun` / `BenchmarkPreparation` / `BenchmarkRunOutcome` value objects and re-signed
  `prepare_case`, `run_case`, `maybe_prepare_case`, `run_one`, `run_dry_batches`,
  `benchmark_run_payload` and the MCP-registration builders onto them. Generated files and run
  outputs are unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-07T20:45+02:00 — No route impact: 260707-HFX-L2's only change under this route is
  `mcp_registration.py`'s `prepare_configured_providers` opting INTO the synchronous cgc
  refresh fallback (hermetic-cold benchmarks need the timeout-bounded graph build now that
  the fallback default is off) — the prepare/registration model this overview narrates is
  unchanged; detail in the file sidecar.
- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fixes (B3/B4): `workspace.py`'s filter now treats
  `None` FAIL-CLOSED with the `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1` env escape (B4), and
  `mcp_registration.py` gained `disarm_stale_benchmark_registrations` — the stale-registration
  sweep both `services.py` entry points open with (B3). Verification metadata pinned until
  closeout stamps the HFX-L1 commit.
- 2026-07-07T16:50+02:00 — 260707-HFX-L1 route impact (provider containment R1): the manifest is
  no longer launch authority — `workspace.py` gained `filter_benchmark_provider_ids` (applied in
  `prepare_case` before registration/launch, skipped ids reported), `models.py`'s
  `BenchmarkPrepareRequest`/`BenchmarkRunRequest` gained `allowed_provider_ids` (None = direct
  script use, unfiltered), and `services.py`/`execution.py` thread it through. Verification
  metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): restored the **hermetic-cold** benchmark provider-isolation content (task 260619 / MCP 2.9.2) that the series carryover had reverted to pre-2.9.2 prose — `mcp_registration.py` wires no seed source, `execution.py`'s `benchmark_mcp_config_overrides` points at the benchmark's own MCP server, plus the grepai/seed.py defense-in-depth reference. The merged tree at 84e95ad keeps main's hermetic behavior (the series did not touch this route's source).
- 2026-06-19T13:42: Benchmark provider setup is now hermetic-cold — `workspace.py`/`mcp_registration.py` wire no seed source, so benchmark stacks index their own fixture and never start/clone the live workspace backends (task 260619). `execution.py` gained `benchmark_mcp_config_overrides` so the benchmarked Codex uses the benchmark's own MCP server.
- 2026-06-11T14:12+02:00: No route impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in files on this route; route structure and overview content are unchanged.
- 2026-06-10T05:30+02:00 — Route body caught up with 2.5.1: `run_command` captures output and never inherits parent stdio (GitHub #49). Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-05-30T21:51+02:00: Re-verified the route against `825a172`; the module split summary still matches. The only route change since `3f09b75` was `mcp_registration.py` renaming the generated `providerSeconds` cap to `providerSetupSeconds` (documented on its file card).
- 2026-05-28T12:32+02:00: Updated after benchmark provider settings and scaffolded runtime assets moved logs under the central `logs/` tree.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
