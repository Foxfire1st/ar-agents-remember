# provider-setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/scripts/provider-setup.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T04:53+02:00                     |
| lastVerifiedCommitHash |                                            `0462de46a1da1bf1997e3979f4cc5bc53d1132f6`|
| lastVerifiedCommitDate |                                            2026-05-21T08:30:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

`provider-setup.py` is the shared provider setup orchestrator for installed coordinators. It keeps installer, benchmark preparation, and C-09 worktree preparation from duplicating provider install, refresh, watcher, backend, and CGC seed logic. Callers should only enter it when their relevant `settings.json` enables providers; when invoked against missing or disabled provider settings, it returns an empty successful no-op.

## Code Commentary

### Logic

The script reads `<coordination-root>/system/settings.json`, detects enabled context providers, and dispatches provider-specific mechanics through `provider-lifecycle.py`. The `install` action installs enabled GrepAI and CodeGraphContext dependencies. The `prepare` action installs enabled dependencies, refreshes GrepAI when enabled, attempts CGC seed import, and starts plus checks provider watchers.

CGC seeding exports a `.cgc` bundle from a source coordination root, rewrites source repository path strings inside the bundle to the target repository root, then loads the rewritten bundle into the target CGC backend with `--clear`. It refuses to seed mismatched source and target HEAD commits unless the caller explicitly allows mismatch. If no source coordinator is configured, the source settings are missing, the source or target root cannot be resolved, or the commit check fails, the seed result is reported as skipped/failed and the caller can fall back to `cgc refresh-all`.

For worktree setup, callers can pass `--cgc-isolated-runtime-root` plus source and target repo roots. The script writes a temporary settings override containing only the target worktree CGC root, provider state under the isolated runtime root, and an isolated FalkorDB backend/data root, while reusing the installed coordinator's CGC venv, requirements, and patches. Lifecycle commands then receive that override through `--from-settings`.

### Conventions

- Use `provider-setup.py install` from installer/reinstall flows that only need provider dependencies.
- Use `provider-setup.py prepare` from benchmark and worktree preparation after runtime assets and dependencies are installed.
- Benchmark and worktree callers should pass a CGC seed source coordinator whenever a source index exists.
- Worktree callers should pass an isolated runtime root so worktree CGC data does not mutate the main coordinator backend.
- `provider-lifecycle.py` remains the lower-level provider command surface; setup flows should not duplicate its install/start/refresh details.

### Invariants And Boundaries

Provider output remains discovery evidence only. Source files, verified onboarding, drift checks, branch validity, and approved memory promotion remain the proof layer.

The script does not delete source indexes or provider backend data. Destructive provider cleanup stays in explicit lifecycle commands.

### Todos

Refresh verification metadata after the provider setup script is committed.

### Docs References

No external documentation is needed for this standard-library orchestrator.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The installer delegates enabled provider dependency installation to `scripts/provider-setup.py install`. | n/a | [installer](agents-remember-md/installer/install-runtime.py) |
| The benchmark runner delegates memory-enabled provider preparation to `scripts/provider-setup.py prepare` and passes a source coordination root for CGC seed import when available. | n/a | [benchmark runner](agents-remember-md/runtime/scripts/run-benchmarks.py) |
| The C-09 worktree manager delegates default worktree provider preparation to `scripts/provider-setup.py prepare` with an isolated CGC runtime root. | n/a | [git worktree manager](agents-remember-md/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T04:53+02:00: Created onboarding for the shared provider setup script and CGC bundle seed workflow.
