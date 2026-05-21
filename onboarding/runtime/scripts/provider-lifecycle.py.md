# provider-lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/scripts/provider-lifecycle.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T03:05+02:00                     |
| lastVerifiedCommitHash | `0462de46a1da1bf1997e3979f4cc5bc53d1132f6` |
| lastVerifiedCommitDate | 2026-05-21T08:30:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

`provider-lifecycle.py` is the installed runtime entrypoint for managing optional discovery providers without teaching agents ad hoc shell sequences. It supports GrepAI memory-provider lifecycle commands and CodeGraphContext code-provider lifecycle commands backed by a lifecycle-owned FalkorDB Docker DBMS.

## Code Commentary

### Logic

The script imports shared provider helpers from the installed runtime skill tree, then exposes provider subcommands. CGC actions include `apply-settings`, `backend-start`, `backend-status`, `status`, `init-layout`, `patch`, `doctor`, `install`, `install-all`, `start`, `start-all`, `stop`, `stop-all`, `shutdown-all`, `refresh`, `refresh-all`, and `run`. GrepAI actions include `status`, `install`, `start`, `stop`, and `refresh`. The `watchers` command is the coordinator-level surface for normal watcher operations; `watchers start`, `watchers status`, and `watchers shutdown-all` read enabled providers from `system/settings.json` and fan out to GrepAI plus every configured CGC root. Managed process health is checked by PID; on Windows this uses `OpenProcess` / `GetExitCodeProcess` instead of shelling out to `tasklist`, because command access or localization failures must not make running watchers look dead.

CGC lifecycle commands use the coordinator `contextProviders.providers.codegraphcontext-code` settings to expand `roots[]` into one runtime instance per code repository. Each configured root must point at an existing code repository directory before lifecycle commands create runtime state, so placeholder settings cannot silently materialize example instances. `apply-settings` creates or updates each configured instance, writes provider state, records graph names, and reconciles stale generated runtime artifacts. It removes unconfigured generated CGC instance directories such as a leftover `my-app`, and removes legacy embedded-backend `db`, `global`, `kuzu`, and `kuzu.wal` artifacts from configured instances while preserving the shared FalkorDB backend data root.

The backend commands manage one shared browser-capable FalkorDB Docker container per coordination root. `backend-start` pulls/runs the pinned image when needed, writes backend state under the configured backend root, writes the image lock, maps Redis/FalkorDB plus browser ports on loopback, and health-checks with `redis-cli ping`. `backend-status` reports container health, ports, browser URL, image, and data root. Current settings place the durable backend root under `provider-data/codegraphcontext/falkordb/`, outside the disposable `providers/` tree.

CGC install commands create or reuse the shared provider venv, install the pinned requirements file, apply the required managed patches, run doctor checks, and update provider state. `patch` verifies both the `.cgcignore` runtime-root patch and the Windows repository-delete prefix patch. `doctor` checks runtime containment, source artifact cleanliness, command availability, patch verification, and CGC's own doctor command. `refresh` runs `cgc index <repo> --force` under the contained provider environment. `start` launches a supervised foreground `cgc watch <repo>` process in the background, records its PID, and redirects output to the provider runtime log. `start-all` and `shutdown-all` fan those operations across every configured root. `run` executes native CGC arguments through the selected repo's managed environment, so agents can issue relationship probes such as `find name` or `analyze callers` without reconstructing CGC env vars by hand.

GrepAI lifecycle commands run from the configured memory root. `install` installs the pinned platform-specific release binary into `providers/_bin/`; `status` calls `grepai status --no-ui` and `grepai watch --status`, then requires either a live managed PID or native watcher-running output before reporting `ok`; `start` launches a managed watcher and records state; `refresh` stops and restarts the watcher.

### Conventions

- Use `--coordination-root` to anchor all provider runtime paths.
- CGC operations derive roots, backend settings, graph names, and runtime reconciliation from `<coordination_root>/system/settings.json` by default; use `--from-settings` only for debug runs against an alternate settings file.
- Prefer `watchers start`, `watchers status`, and `watchers shutdown-all` for normal operator workflows across all enabled providers.
- Use one CGC provider instance per code repo, keyed by stable `--repo-id`; `start-all`, `shutdown-all`, `install-all`, and `refresh-all` operate across every configured root.
- Use `--json` for machine-readable lifecycle state in task/evaluation workflows.
- Use `--dry-run` to inspect command shapes without starting provider processes or rewriting provider state.
- Treat the recorded lifecycle PID as the authority for managed watcher status, using the platform PID probe rather than provider-native background-daemon status alone.

### Invariants And Boundaries

Provider lifecycle commands may create or mutate disposable provider runtime state under `ar-coordination/providers/`, but they should not mutate indexed code repositories except by reading them. CGC start/refresh should fail or be treated as unhealthy when source artifact probes find provider-created files in the code repo. Runtime reconciliation may delete stale provider-owned scaffolding and legacy embedded CGC artifacts under `providers/`, but must preserve durable backend data under `provider-data/` unless an explicit destructive database action is requested.

### Todos

- Add explicit lifecycle-state reporting for missing, installed, configured, indexed, watching, stale, refreshing, and faulted.
- Improve GrepAI status interpretation so managed foreground/background watcher differences are explicit in provider state.

## Docs References

No external documentation is cited here. The script is a repository-local operational wrapper over configured provider CLIs.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The script imports shared provider layout, artifact detection, patch, cleanup, and state helpers from the installed runtime skill tree. | L26-L61 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| Managed process health checks use `OpenProcess` / `GetExitCodeProcess` on Windows and `os.kill(pid, 0)` elsewhere, avoiding `tasklist` output as a lifecycle dependency. | L135-L158 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| Provider enabled checks read `contextProviders.providers.<id>` from the coordinator settings, and CGC settings expansion reads configured roots, backend settings, and graph names from `contextProviders.providers.codegraphcontext-code`; shared helpers reject unresolved or missing code repository root paths. | L303-L429 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| `apply-settings` creates configured instances, writes state, and reports stale runtime artifacts removed during reconciliation. | L514-L581 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| FalkorDB Docker backend commands inspect, start, lock, and health-check the shared browser-capable backend container and report the configured backend/data roots. | L641-L774 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| CGC install and patch flows install from pinned requirements, verify required patches, and record patch state. | L836-L1125 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| CGC start, stop, start-all, shutdown-all, refresh, and refresh-all supervise per-repo watchers and hard refresh configured repo scopes. | L1163-L1454 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| `cgc run` selects a configured repo layout, strips the optional `--` separator, and executes native CGC arguments through the managed provider environment. | L1468-L1488; L1861-L1890 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| GrepAI lifecycle commands install the pinned release binary, require a live watcher for healthy status, run start/stop/refresh probes, and write provider state under the GrepAI runtime root. | L1481-L1719 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| The aggregate `watchers` lifecycle command reads enabled GrepAI and CGC providers from settings, dispatches start/status/stop operations to each provider, and exposes the parser entrypoint for `watchers status`, `watchers start`, `watchers stop`, and `watchers shutdown-all`. | L1740-L1861; L1900-L1901 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |

## Cross-Repo References

No sibling repository evidence is needed for the lifecycle script.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T03:05+02:00: Updated after adding `cgc run` as the lifecycle-managed pass-through for native CodeGraphContext relationship queries.
- 2026-05-21T02:33+02:00: Updated after adding the aggregate `watchers` lifecycle command for all enabled provider watchers.
- 2026-05-21T02:25+02:00: Updated GrepAI status notes after lifecycle status began returning unhealthy when the index is present but no native or managed watcher is running.
- 2026-05-21T02:20+02:00: Updated after Windows managed watcher status switched from `tasklist` output to direct PID checks through the Windows process API.
- 2026-05-21T02:10+02:00: Updated lifecycle notes for the `provider-data/` backend root and disposable `providers/` scaffold model.
- 2026-05-21T01:47+02:00: Clarified that settings-expanded CGC roots must resolve to existing code repository directories before runtime state is created.
- 2026-05-21T01:32+02:00: Updated after CGC moved to FalkorDB Docker only, added settings-expanded multi-root lifecycle commands, start-all/shutdown-all, managed patch verification, GrepAI installation, and stale provider runtime cleanup. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
- 2026-05-20T19:11+02:00: Created onboarding for the provider lifecycle CLI covering CGC and GrepAI status/start/stop/refresh/doctor flows. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
