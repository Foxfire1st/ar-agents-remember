# tools.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/coordinator/tools.md`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T17:16+02:00                     |
| lastVerifiedCommitHash |                                            `5ff4ed4ef94b5576a45059de8ac7c03e8c4c04a1`|
| lastVerifiedCommitDate |                                            2026-05-21T18:12:00+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

This example documents the coordinator-level tools surface, including the shared provider setup entrypoint and expected lifecycle command shapes for configured context providers.

## Code Commentary

### Logic

The file says coordinator tools are commands useful across many repositories. Repo-specific checks, branch workflow, and coding tools belong in memory-layer `system/tools.md`. When `contextProviders` are enabled, it records `provider-setup.py install` and `provider-setup.py prepare` as the shared setup entrypoints, bounded GrepAI backend/status/start/search commands, aggregate `watchers` lifecycle command shapes, and CodeGraphContext-specific command shapes. GrepAI search is documented through the runtime-owned `<coordination_root>/providers/_bin/grepai` binary with `--workspace agents-remember-memory --json --compact --limit 5`, not through a global command or path filter. The `watchers` and normal CGC commands infer the coordinator root from the installed lifecycle script path, default to `<coordination_root>/system/settings.json`, and are the normal operator path for starting, checking, and shutting down all enabled provider watchers. CGC commands read `contextProviders.providers.codegraphcontext-code`, expand the configured `roots` array into per-repo runtime instances, ensure the shared FalkorDB Docker backend is healthy, start or stop one watcher per configured code repo, run bounded native relationship queries through `cgc ... run -- <native cgc args>`, and launch the long-running visualizer through `cgc ... visualize --port <port>`. The provider notes distinguish long-running daemon/server actions from bounded query actions: watcher starts/stops, CGC start/stop/visualize, and GrepAI watcher start/stop/refresh must run from a durable host process namespace, while lifecycle status reports `processNamespace` diagnostics. `provider-setup.py prepare` is the benchmark/worktree setup entrypoint for CGC seed export/import with path rewrite before fallback refresh, but callers should skip provider setup when the relevant `settings.json` does not enable providers. `--coordination-root` and `--from-settings` are documented as explicit overrides for unusual coordinator roots or alternate settings files.

### Conventions

Global commands stay here; repository-specific command details stay in the selected memory layer. Setup flows should use `provider-setup.py`; direct `provider-lifecycle.py` calls are lower-level provider diagnostics and operations. GrepAI lifecycle commands read the `grepai-memory` settings, expand workspace roots into explicit projects, ensure the PostgreSQL/pgvector Docker backend is healthy, mirror memory roots under `providers/grepai/index-roots/` when enabled, and write GrepAI workspace config under `providers/grepai/home/.grepai/workspace.yaml`. CGC/FalkorDB runtime env keys are process env only; for CGC v0.4.10 they should not be written into `<instanceRoot>/.codegraphcontext/.env`. Use `start` or `start-all` to start every configured watcher and `stop`, `stop-all`, or `shutdown-all` to stop every configured watcher; single-repo CGC operations add `--repo-id`. Normal lifecycle examples do not repeat `--coordination-root` because the installed script already knows its coordinator root. Use `cgc visualize --port <port>` for the visualizer server instead of hiding it behind `cgc run`. Use `watchers status`/provider status to inspect `processNamespace` before starting daemons from automation or sandbox-like harnesses.

### Invariants And Boundaries

Agents should resolve the target repository with C-08 before choosing task, worktree, memory, validation paths, or context provider roots. Provider output is discovery evidence only, and source/onboarding proof remains required. Managed mode should fail containment/health checks if CGC writes `.cgcignore`, `.codegraphcontext`, reports, databases, or logs inside indexed source repositories, or if GrepAI writes `.grepai/` inside indexed source repositories or durable memory roots. Daemon/server lifecycle actions must be launched from a durable host process namespace; bounded retrieval commands like `cgc run` remain usable from sandboxed harnesses.

### Todos

None.

## Docs References

No external documentation is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The coordinator tools example separates global commands from repository-specific checks and branch workflow. | L1-L7; L121-L125 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |
| The provider command section records shared setup commands, GrepAI backend/status/start/search probes through the runtime-owned binary, aggregate `watchers status/start/shutdown-all`, and CGC `apply-settings`, per-repo `status`, all-root `start`, per-repo `start`, all-root `shutdown-all`, per-repo `stop`, `doctor`, bounded `run -- analyze callers`, and long-running `visualize --port 8000` command shapes without repeating `--coordination-root` for normal lifecycle operations. | L13-L68 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |
| The provider notes say aggregate `watchers` commands start or stop every enabled provider watcher; GrepAI lifecycle commands expand `grepai-memory` roots, ensure PostgreSQL/pgvector Docker health, mirror memory roots under `providers/grepai/index-roots/`, write provider-owned workspace config/state, and refuse global GrepAI fallback; CGC lifecycle commands infer the coordinator root from the installed script path, reserve `--coordination-root` and `--from-settings` for overrides, expand configured roots, ensure FalkorDB Docker, pass post-`--` arguments to native CGC for bounded relationship queries, and expose the visualizer as a separate long-running lifecycle command. | L70-L109 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |
| The process namespace note says long-running daemon actions such as watcher start/stop/shutdown, CGC start/stop/visualize, and GrepAI watcher start/stop/refresh must run from a durable host namespace, while lifecycle status reports `processNamespace` diagnostics and refuses `--die-with-parent` sandboxes. | L111-L117 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |
| The containment notes require managed mode to reject source-repo CGC artifacts and GrepAI `.grepai/` directories in source repositories or durable memory roots. | L119-L127 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T17:16+02:00: Updated examples after daemon/server lifecycle actions began requiring durable host process namespaces and status began reporting `processNamespace`.
- 2026-05-21T15:42+02:00: Updated examples after normal provider lifecycle commands began inferring the coordinator root from the installed script path.
- 2026-05-21T12:35+02:00: Updated GrepAI lifecycle command notes for provider-owned mirror roots under `providers/grepai/index-roots/`.
- 2026-05-21T12:40+02:00: Updated CGC command doctrine to show `cgc visualize --port <port>` as the explicit long-running visualizer command, separate from bounded `cgc run` queries.
- 2026-05-21T11:50+02:00: Updated GrepAI command doctrine for backend status/start, runtime-owned binary usage, workspace-mode PostgreSQL config, and `.grepai/` containment checks.
- 2026-05-21T04:53+02:00: Added shared `provider-setup.py` setup commands and documented CGC seed export/import with path rewrite for benchmark and worktree preparation.
- 2026-05-21T03:05+02:00: Corrected GrepAI search to query-first JSON compact output and documented lifecycle-managed `cgc run` relationship queries.
- 2026-05-21T02:33+02:00: Added aggregate `watchers` command documentation for starting, checking, and stopping every enabled provider watcher through one coordinator-level command.
- 2026-05-21T02:33+02:00: Updated CGC command examples so normal lifecycle commands derive `system/settings.json` from `--coordination-root`; `--from-settings` is now documented only as a debug override.
- 2026-05-21T01:47+02:00: Updated provider command documentation for FalkorDB Docker lifecycle management, all-root watcher start/stop commands, and source-containment checks.
- 2026-05-20T19:11+02:00: Documented provider command shapes for GrepAI and CodeGraphContext, including CGC process-env-only keys and containment checks.
- 2026-05-13T13:38: Created onboarding for the coordinator tools example.
