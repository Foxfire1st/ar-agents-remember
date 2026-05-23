# provider-setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `scripts/provider-setup.py`                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T04:29+02:00                     |
| lastVerifiedCommitHash |                                            `00aae9dad3d8740e10a41ab285f87ecab8608745`|
| lastVerifiedCommitDate |                                            2026-05-21T23:53:08+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`provider-setup.py` is a source-checkout helper for manual/debug provider setup
and benchmark CGC seed mechanics. It is no longer copied into coordinator
runtimes, and MCP runtime install does not call it.

## Code Commentary

### Logic

The script can still read legacy/generated provider settings for explicit
source-checkout runs, then dispatches provider-specific mechanics through the
neighboring source-level `provider-lifecycle.py`. Subprocess execution captures
UTF-8 text and forces `PYTHONUTF8=1` plus `PYTHONIOENCODING=utf-8` into
lifecycle children so Windows console defaults do not break JSON or provider
output rendering. MCP-owned installs use package-local provider lifecycle code
instead.

CGC seeding exports a `.cgc` bundle from a source coordination root, rewrites source repository path strings inside the bundle to the target repository root, then loads the rewritten bundle into the target CGC backend with `--clear`. It refuses to seed mismatched source and target HEAD commits unless the caller explicitly allows mismatch. If no source coordinator is configured, the source settings are missing, the source or target root cannot be resolved, or the commit check fails, the seed result is reported as skipped/failed and the caller can fall back to `cgc refresh-all`.

For worktree setup, callers can pass `--cgc-isolated-runtime-root` plus source and target repo roots. The script writes a temporary settings override containing only the target worktree CGC root, provider state under the isolated runtime root, and an isolated FalkorDB backend/data root under `providers/data`, while reusing the installed coordinator's CGC venv, requirements, and patches. Lifecycle commands then receive that override through `--from-settings`. The isolated runner path follows the main provider layout: `providers/runners/codegraphcontext`.

### Conventions

- Do not call this script from installed coordinator runtime paths.
- Use MCP `runtime_install` for normal runtime and provider dependency install.
- Use `provider-setup.py prepare` only for source-checkout benchmark/debug flows that explicitly need CGC bundle seeding.
- `provider-lifecycle.py` remains the lower-level provider command surface; setup flows should not duplicate its install/start/refresh details.
- Setup subprocesses should keep UTF-8 environment overrides because lifecycle output may include non-ASCII provider glyphs and JSON payloads.

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
| MCP runtime install uses package-local provider lifecycle modules instead of this source script. | n/a | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| The benchmark runner can still delegate explicit benchmark provider preparation to the source-level setup script. | n/a | [benchmark runner](agents-remember-md/scripts/run-benchmarks.py) |
| `subprocess_env` and `run_command` force UTF-8 environment variables for provider lifecycle child processes while still capturing stdout/stderr as UTF-8 text. | L197-L228 | [provider-setup.py](agents-remember-md/scripts/provider-setup.py) |
| Isolated CGC settings place worktree runner state under `providers/runners/codegraphcontext` and backend data under `providers/data/codegraphcontext/falkordb`. | L136-L152 | [provider-setup.py](agents-remember-md/scripts/provider-setup.py) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-23T04:29+02:00: Updated after isolated CGC worktree settings moved to `providers/runners` and `providers/data`.
- 2026-05-23T05:35+02:00: Moved onboarding from `runtime/scripts` to `scripts` after Python provider scripts stopped being installed coordinator runtime assets.
- 2026-05-21T23:18+02:00: Updated after setup subprocesses began forcing UTF-8 environment variables for lifecycle children.
- 2026-05-21T04:53+02:00: Created onboarding for the shared provider setup script and CGC bundle seed workflow.
