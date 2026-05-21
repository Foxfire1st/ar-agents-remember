# tools.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/coordinator/tools.md`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T04:53+02:00                     |
| lastVerifiedCommitHash |                                            `0462de46a1da1bf1997e3979f4cc5bc53d1132f6`|
| lastVerifiedCommitDate |                                            2026-05-21T08:30:44+02:00|

## Purpose

This example documents the coordinator-level tools surface, including the shared provider setup entrypoint and expected lifecycle command shapes for configured context providers.

## Code Commentary

### Logic

The file says coordinator tools are commands useful across many repositories. Repo-specific checks, branch workflow, and coding tools belong in memory-layer `system/tools.md`. When `contextProviders` are enabled, it records `provider-setup.py install` and `provider-setup.py prepare` as the shared setup entrypoints, bounded GrepAI status/watch/search commands, aggregate `watchers` lifecycle command shapes, and CodeGraphContext-specific command shapes. GrepAI search is documented as `grepai search "<query>" --json --compact --limit 5`, not as a path filter. The `watchers` commands default to `<coordination_root>/system/settings.json` and are the normal operator path for starting, checking, and shutting down all enabled provider watchers. The CGC commands default to the same settings file, read `contextProviders.providers.codegraphcontext-code`, expand the configured `roots` array into per-repo runtime instances, ensure the shared FalkorDB Docker backend is healthy, start or stop one watcher per configured code repo, and run native relationship queries through `cgc ... run -- <native cgc args>`. `provider-setup.py prepare` is the benchmark/worktree setup entrypoint for CGC seed export/import with path rewrite before fallback refresh, but callers should skip provider setup when the relevant `settings.json` does not enable providers. `--from-settings` is documented only as a debug override for alternate settings files.

### Conventions

Global commands stay here; repository-specific command details stay in the selected memory layer. Setup flows should use `provider-setup.py`; direct `provider-lifecycle.py` calls are lower-level provider diagnostics and operations. CGC/FalkorDB runtime env keys are process env only; for CGC v0.4.10 they should not be written into `<instanceRoot>/.codegraphcontext/.env`. Use `start` or `start-all` to start every configured watcher and `stop`, `stop-all`, or `shutdown-all` to stop every configured watcher; single-repo operations add `--repo-id`.

### Invariants And Boundaries

Agents should resolve the target repository with C-08 before choosing task, worktree, memory, validation paths, or context provider roots. Provider output is discovery evidence only, and source/onboarding proof remains required. Managed mode should fail containment/health checks if CGC writes `.cgcignore`, `.codegraphcontext`, reports, databases, or logs inside indexed source repositories.

### Todos

None.

### Docs References

No external documentation is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The coordinator tools example separates global commands from repository-specific checks and branch workflow. | L1-L9; L52-L56 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |
| The provider command section records GrepAI status/watch/search probes, aggregate `watchers status/start/shutdown-all`, and CGC `apply-settings`, per-repo `status`, all-root `start`, per-repo `start`, all-root `shutdown-all`, per-repo `stop`, `doctor`, and `run -- analyze callers` command shapes without requiring `--from-settings` for normal coordinator use. | L13-L50 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |
| The provider notes say aggregate `watchers` commands start or stop every enabled provider watcher, while CGC lifecycle commands default to `<coordination_root>/system/settings.json`, reserve `--from-settings` for debug overrides, expand the configured `roots` array, ensure the shared FalkorDB Docker backend, apply process env, record backend browser state, use one watcher per configured code repo, and pass post-`--` arguments to native CGC for relationship queries. | L52-L70 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |
| The containment notes require managed mode to reject source-repo `.cgcignore`, `.codegraphcontext`, reports, databases, or logs. | L53-L56 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T04:53+02:00: Added shared `provider-setup.py` setup commands and documented CGC seed export/import with path rewrite for benchmark and worktree preparation.
- 2026-05-21T03:05+02:00: Corrected GrepAI search to query-first JSON compact output and documented lifecycle-managed `cgc run` relationship queries.
- 2026-05-21T02:33+02:00: Added aggregate `watchers` command documentation for starting, checking, and stopping every enabled provider watcher through one coordinator-level command.
- 2026-05-21T02:33+02:00: Updated CGC command examples so normal lifecycle commands derive `system/settings.json` from `--coordination-root`; `--from-settings` is now documented only as a debug override.
- 2026-05-21T01:47+02:00: Updated provider command documentation for FalkorDB Docker lifecycle management, all-root watcher start/stop commands, and source-containment checks.
- 2026-05-20T19:11+02:00: Documented provider command shapes for GrepAI and CodeGraphContext, including CGC process-env-only keys and containment checks.
- 2026-05-13T13:38: Created onboarding for the coordinator tools example.
