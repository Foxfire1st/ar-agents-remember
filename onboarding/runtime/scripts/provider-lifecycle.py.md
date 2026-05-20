# provider-lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/scripts/provider-lifecycle.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-20T20:01+02:00                     |
| lastVerifiedCommitHash | `e4ae4955d888d3ce58b55b5ca99d20039cbcb214` |
| lastVerifiedCommitDate | 2026-05-20T20:01:26+02:00 |
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

`provider-lifecycle.py` is the installed runtime entrypoint for managing optional discovery providers without teaching agents ad hoc shell sequences. It currently supports GrepAI memory-provider lifecycle commands and CodeGraphContext code-provider lifecycle commands.

## Code Commentary

### Logic

The script imports shared provider helpers from the installed runtime skill tree, then exposes provider subcommands. CGC actions include `status`, `init-layout`, `patch`, `doctor`, `start`, `stop`, and `refresh`. GrepAI actions include `status`, `start`, `stop`, and `refresh`.

CGC lifecycle commands use `cgc_runtime_layout` to derive a contained runtime root, provider venv, requirements file, patch root, state file, `.codegraphcontext` root, and process environment. `init-layout` creates default runtime files and writes state. `patch` applies and records the required CGC `.cgcignore` runtime-root patch. `doctor` checks source artifact cleanliness, command availability, patch verification, and CGC's own doctor command. `refresh` runs `cgc index <repo> --force` under the contained provider environment. `start` launches a supervised foreground `cgc watch <repo>` process in the background, records its PID, and redirects output to the provider runtime log.

GrepAI lifecycle commands run from the configured memory root. `status` calls `grepai status --no-ui` and `grepai watch --status`; `start` launches `grepai watch --background --log-dir <runtimeRoot>/logs`; `refresh` stops and restarts the watcher.

### Conventions

- Use `--coordination-root` to anchor all provider runtime paths.
- Use one CGC provider instance per code repo, keyed by stable `--repo-id`.
- Use `--json` for machine-readable lifecycle state in task/evaluation workflows.
- Use `--dry-run` to inspect command shapes without starting provider processes or rewriting provider state.

### Invariants And Boundaries

Provider lifecycle commands may create or mutate provider runtime state under `ar-coordination/providers/`, but they should not mutate indexed code repositories except by reading them. CGC start/refresh should fail or be treated as unhealthy when source artifact probes find provider-created files in the code repo.

### Todos

- Add a bounded CGC relationship-probe action after the provider query budget is finalized.
- Improve GrepAI status interpretation so managed foreground/background watcher differences are explicit in provider state.

## Docs References

No external documentation is cited here. The script is a repository-local operational wrapper over configured provider CLIs.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The script imports shared provider layout, artifact detection, patch, and state helpers from the installed runtime skill tree. | L18-L41 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| CGC status reports command availability, runtime paths, source artifacts, patch state, and managed process liveness. | L121-L164 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| CGC init and patch actions create contained runtime files, write provider state, and record the required patch id. | L167-L241 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| CGC doctor checks containment, source cleanliness, executable presence, patch verification, and `cgc doctor` under the provider env. | L244-L277 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| CGC start, stop, and refresh supervise `cgc watch`, terminate only the managed PID, and run `cgc index <repo> --force` from the contained runtime root. | L280-L391 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| GrepAI lifecycle commands run `grepai status --no-ui`, `grepai watch --status`, `grepai watch --background`, `grepai watch --stop`, and write provider state under the GrepAI runtime root. | L394-L458 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| The CLI parser exposes `cgc` and `grepai` provider subcommands with shared `--coordination-root`, `--dry-run`, `--json`, and `--timeout` options. | L461-L523 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |

## Cross-Repo References

No sibling repository evidence is needed for the lifecycle script.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-20T19:11+02:00: Created onboarding for the provider lifecycle CLI covering CGC and GrepAI status/start/stop/refresh/doctor flows. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
