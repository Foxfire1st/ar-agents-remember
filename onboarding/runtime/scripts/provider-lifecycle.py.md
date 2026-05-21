# provider-lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/scripts/provider-lifecycle.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T23:18+02:00                     |
| lastVerifiedCommitHash | `00aae9dad3d8740e10a41ab285f87ecab8608745` |
| lastVerifiedCommitDate | 2026-05-21T23:53:08+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

`provider-lifecycle.py` is the installed runtime entrypoint for managing optional discovery providers without teaching agents ad hoc shell sequences. It supports GrepAI memory-provider lifecycle commands backed by a lifecycle-owned PostgreSQL/pgvector Docker DBMS and CodeGraphContext code-provider lifecycle commands backed by a lifecycle-owned FalkorDB Docker DBMS. It also reports whether the current process namespace is durable enough for provider daemons, so sandboxed harnesses fail loudly instead of pretending background watcher PIDs are trustworthy.

## Code Commentary

### Logic

The script imports shared provider helpers from the installed runtime skill tree, infers the default coordinator root from its installed script path, then exposes provider subcommands. Before daemon/server management, it checks the current PID namespace by reading `/proc/1/cmdline` on non-Windows systems; namespaces supervised with `--die-with-parent` are reported as non-durable because child daemons may be killed when the harness exits and host-side PIDs may be invisible. `status` surfaces this as `processNamespace`, while daemon actions raise a clear lifecycle error. CGC actions include `apply-settings`, `backend-start`, `backend-status`, `status`, `init-layout`, `patch`, `doctor`, `install`, `install-all`, `start`, `start-all`, `stop`, `stop-all`, `shutdown-all`, `refresh`, `refresh-all`, `run`, and `visualize`. GrepAI actions include `install`, `backend-start`, `backend-status`, `status`, `start`, `stop`, and `refresh`. The `watchers` command is the coordinator-level surface for normal watcher operations; `watchers start`, `watchers status`, and `watchers shutdown-all` read enabled providers from `system/settings.json` and fan out to GrepAI plus every configured CGC root. Managed process health is checked by PID; on Windows this uses `OpenProcess` / `GetExitCodeProcess` instead of shelling out to `tasklist`, because command access or localization failures must not make running watchers look dead.

CGC lifecycle commands use the coordinator `contextProviders.providers.codegraphcontext-code` settings to expand `roots[]` into one runtime instance per code repository. Each configured root must point at an existing code repository directory before lifecycle commands create runtime state, so placeholder settings cannot silently materialize example instances. Settings-backed commands tolerate an omitted `--from-settings` override and default to `<coordination_root>/system/settings.json`. `apply-settings` creates or updates each configured instance, writes provider state, records graph names, and reconciles stale generated runtime artifacts. It removes unconfigured generated CGC instance directories such as a leftover `my-app`, and removes legacy embedded-backend `db`, `global`, `kuzu`, and `kuzu.wal` artifacts from configured instances while preserving the shared FalkorDB backend data root.

The backend commands manage one shared browser-capable FalkorDB Docker container per coordination root. `backend-start` pulls/runs the pinned image when needed, writes backend state under the configured backend root, writes the image lock, maps Redis/FalkorDB plus browser ports on loopback, and health-checks with `redis-cli ping`. `backend-status` reports container health, ports, browser URL, image, and data root. Current settings place the durable backend root under `provider-data/codegraphcontext/falkordb/`, outside the disposable `providers/` tree.

CGC install commands create or reuse the shared provider venv, install the pinned requirements file, apply the required managed patches, run doctor checks, and update provider state. `patch` verifies the `.cgcignore` runtime-root patch, Windows repository-delete prefix patch, C++/TableGen discovery patches, visualizer repo-query patch, visualizer server route patch, and visualizer CLI route patch. `doctor` checks runtime containment, source artifact cleanliness, command availability, patch verification, and CGC's own doctor command. `refresh` runs `cgc index <repo> --force` under the contained provider environment. `start` launches a supervised foreground `cgc watch <repo>` process in the background, records its PID, and redirects output to the provider runtime log; `start`, `start-all`, `stop`, `stop-all`, `shutdown-all`, and the long-running `visualize` server require a durable host process namespace unless they are dry-runs. `start-all` and `shutdown-all` fan those operations across every configured root. `run` executes bounded native CGC query arguments through the selected repo's managed environment, so agents can issue relationship probes such as `find name` or `analyze callers` without reconstructing CGC env vars by hand. By default, `run` prints the native command stdout and stderr directly even when `--json` is present, because the provider answer is the useful retrieval payload; callers must pass `run --lifecycle-json -- ...` to render compact API JSON with `outputLines`, return code, duration, repo id, and status. Generic JSON rendering uses UTF-8 characters rather than ASCII escaping. `visualize` launches the long-running CGC visualizer server as its own lifecycle action with explicit `--port` and `--context` options, and `run -- visualize ...` is rejected so the server is not hidden behind the bounded native-query pass-through.

GrepAI lifecycle commands run in workspace mode rather than inside a memory root. `install` installs the pinned platform-specific release binary into `providers/_bin/grepai`, ensures provider-owned layout under `providers/grepai/`, starts or verifies the PostgreSQL/pgvector Docker backend when settings enable GrepAI, syncs provider-owned mirror roots under `providers/grepai/index-roots/`, and writes the GrepAI workspace config under `providers/grepai/home/.grepai/workspace.yaml`. The backend helpers pull/run the configured pgvector image, mount durable database data from `provider-data/grepai/postgres/data`, loop until both `pg_isready` and a target-database `SELECT 1` succeed, create or verify the `vector` extension, and record backend state plus image lock metadata. `status` checks `workspace status`, `watch --status`, backend data mount health, target database reachability, pgvector availability, recorded managed PID health, `.grepai/` containment in configured source memory roots, and process namespace diagnostics before reporting `ok`. `start`, `stop`, and `refresh` require a durable host process namespace unless they are dry-runs. `run` executes bounded native GrepAI commands such as `search` through the managed workspace environment, while rejecting watcher control so continuous processes stay on explicit lifecycle actions. `install` and `start` treat stale root `.grepai/` artifacts as disposable GrepAI cache/tooling state: after direct-child path validation, they remove those artifacts, resync provider-owned mirrors, and write workspace config instead of hard-failing setup. `start` adopts an already-running matching watcher before launching a new one, launches GrepAI through the runtime-owned binary with native `watch --background --workspace <workspace> --log-dir <runtimeRoot>/logs`, captures timeout results without treating first indexing as watcher death, probes watcher status after launch, parses any started PID from GrepAI output, and stores managed watcher state; `refresh` stops and restarts that watcher.

The aggregate `watchers` command now preserves per-provider outcomes when one provider succeeds and another fails. It catches provider-specific lifecycle errors, reports `partial` when applicable, and returns `recoveryActions` so setup callers can distinguish a partial recovery path from a generic failed workflow.

### Conventions

- Lifecycle commands infer the coordinator root from the installed script path by default; use `--coordination-root` only to intentionally point the script at a different coordinator root.
- CGC operations derive roots, backend settings, graph names, and runtime reconciliation from `<coordination_root>/system/settings.json` by default; use `--from-settings` only for debug runs against an alternate settings file.
- GrepAI operations derive explicit memory roots, workspace name, runtime root, mirror-root policy, embedder settings, and PostgreSQL backend settings from `contextProviders.providers.grepai-memory`; managed mode uses `providers/_bin/grepai` and does not fall back to a global command.
- Prefer `watchers start`, `watchers status`, and `watchers shutdown-all` for normal operator workflows across all enabled providers.
- Use one CGC provider instance per code repo, keyed by stable `--repo-id`; `start-all`, `shutdown-all`, `install-all`, and `refresh-all` operate across every configured root.
- Use `cgc run` when an agent or operator wants the native provider answer; `--json` remains ignored for successful native command rendering, and `run --lifecycle-json -- ...` is the opt-in compact API JSON with `outputLines` plus minimal execution metadata.
- Use `grepai run -- search ...` when an agent or operator wants a native GrepAI semantic result through the provider-owned workspace environment.
- Use `--json` for machine-readable lifecycle state in task/evaluation workflows.
- Use `--dry-run` to inspect command shapes without starting provider processes or rewriting provider state.
- Use `cgc visualize --port <port>` for the long-running visualizer server; do not launch it through `cgc run`.
- Treat `processNamespace.durableForDaemons` as the lifecycle-level answer for whether watcher/server commands may be started from the current execution context; bounded `cgc run` queries are not daemon actions and must not be blocked by that guard.
- Treat the recorded lifecycle PID as the authority for managed watcher status, using the platform PID probe rather than provider-native background-daemon status alone.

### Invariants And Boundaries

Provider lifecycle commands may create or mutate disposable provider runtime state under `ar-coordination/providers/`, but they should not write authoritative memory into indexed code repositories or indexed memory roots. CGC start/refresh should fail or be treated as unhealthy when source artifact probes find provider-created files in the code repo. GrepAI `.grepai/` state inside indexed memory roots is disposable provider cache, not durable onboarding; install/start may remove it after direct-child validation, and status treats remaining artifacts as unhealthy. Runtime reconciliation may delete stale provider-owned scaffolding, deprecated GrepAI root artifacts, and legacy embedded CGC artifacts, but must preserve durable backend data under `provider-data/` unless an explicit destructive database action is requested. Daemon/server actions must run from a durable host process namespace; bounded retrieval/query commands remain usable from sandboxed harnesses.

### Todos

- Add explicit lifecycle-state reporting for missing, installed, configured, indexed, watching, stale, refreshing, and faulted.
- Add a provider-level integration smoke test for GrepAI workspace config once the provider binary and local Docker backend can be exercised without network setup.

## Docs References

No external documentation is cited here. The script is a repository-local operational wrapper over configured provider CLIs.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The script imports shared provider layout, GrepAI PostgreSQL constants, disposable root artifact removal, CGC patch checks/apply helpers including the visualizer repo-query and route patches, cleanup, workspace-config, and state helpers from the installed runtime skill tree. | L38-L93 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| Subprocess helpers force UTF-8 child process behavior, generic JSON rendering reconfigures stdio to UTF-8 in CLI mode, and timeout-aware command capture can return structured timeout results instead of raising. | L96-L219; L2942-L2943 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| `default_coordination_root`, shared parser defaults, CGC normalization, and main dispatch make the installed script's parent directory the default coordinator root while preserving `--coordination-root` as an override. | L106-L109; L2589-L2616; L2618-L2631; L2710-L2746 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| Process namespace helpers detect non-Windows `--die-with-parent` PID namespaces, expose `processNamespace.durableForDaemons`, and raise explicit errors for daemon/server management from ephemeral harnesses. | L112-L153; L1238-L1239; L2360-L2362; L2574-L2580 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| Managed process health checks use `OpenProcess` / `GetExitCodeProcess` on Windows and `os.kill(pid, 0)` elsewhere, avoiding `tasklist` output as a lifecycle dependency. | L240-L263 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| `cgc run` bypasses the generic lifecycle renderer and prints the captured command stdout/stderr directly by default, including when `--json` is present; `run --lifecycle-json -- ...` renders a compact API payload with `outputLines` and small execution metadata, and JSON output preserves UTF-8 characters instead of ASCII-escaping Rich table glyphs. | L377-L424; L2700-L2704; L2733-L2737 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| Provider enabled checks read `contextProviders.providers.<id>` from the coordinator settings, and CGC settings expansion reads configured roots, backend settings, and graph names from `contextProviders.providers.codegraphcontext-code`; shared helpers tolerate omitted `--from-settings` overrides and reject unresolved or missing code repository root paths. | L458-L524 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| `apply-settings` creates configured instances, writes state, and reports stale runtime artifacts removed during reconciliation. | L681-L746 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| FalkorDB Docker backend commands inspect, start, lock, and health-check the shared browser-capable backend container and report the configured backend/data roots; dry-run uses deterministic default ports instead of sandbox-hostile bind probes when settings say `auto`. | L749-L1002; L871-L878 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| CGC install, status, and patch flows install from pinned requirements, verify required patches including the visualizer repo-query and route patches, record patch state, and include process namespace diagnostics in status. | L1005-L1317; L1219-L1240 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| CGC start, stop, start-all, and shutdown-all supervise per-repo watchers and require a durable process namespace for non-dry-run daemon management. | L1404-L1585 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| CGC refresh and refresh-all hard refresh configured repo scopes, while `cgc run` selects a configured repo layout, rejects the visualizer server, strips the optional `--` separator, and executes bounded native CGC query arguments through the managed provider environment without the daemon namespace guard. | L1614-L1743 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| `cgc visualize` is a separate long-running lifecycle action that builds `cgc visualize --repo <repo> --port <port>`, supports `--context`, requires a durable process namespace for non-dry-run launches, and runs in the foreground without the bounded command timeout. | L1746-L1794; L2658-L2675; L2718-L2737 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| GrepAI settings-backed layout expansion uses configured workspace roots and runtime settings, while GrepAI watcher helpers parse running/already-running status, match managed state to the runtime layout, probe native watcher status, and prepare workspaces by removing disposable root artifacts before mirror sync and config write. | L1797-L1963 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| GrepAI backend helpers derive PostgreSQL Docker settings, DSNs, embedder settings, target-database readiness probes, pgvector extension creation/verification, and backend state. | L1966-L2120 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| GrepAI backend status/start inspect and run the Docker container, validate the data mount against `provider-data/grepai/postgres/data`, verify target database and pgvector availability, allocate or reuse loopback ports, write image locks/state, and report health. | L2123-L2357 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| GrepAI install downloads the pinned release asset into `providers/_bin/grepai`, verifies checksums/version, starts the managed backend when configured, removes disposable `.grepai/` root artifacts through workspace preparation, syncs provider-owned mirror roots, and writes provider-owned workspace config. | L2360-L2439 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| GrepAI start adopts an already-running matching watcher, captures timeout-shaped launcher results, probes watcher state after launch, parses native background watcher PIDs from stdout/stderr, and writes lifecycle state so status/stop can use the managed process even when GrepAI's native workspace status does not report it as running. | L1870-L1963; L2535-L2622 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| GrepAI status/start/stop/refresh use the runtime-owned binary, workspace name, provider-owned config/log/state/mirror roots, Docker backend status, recorded PID health, process namespace checks for daemon actions, and source-root `.grepai/` checks/remediation instead of treating GrepAI cache as durable memory. | L2442-L2674 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| `grepai run` strips the optional `--` separator, rejects native watcher control, checks readiness, then executes bounded native GrepAI commands through the provider-owned runtime environment and streams native output by default. | L2480-L2535 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |
| The aggregate `watchers` lifecycle command reads enabled GrepAI and CGC providers from settings, rejects start/stop/shutdown-all in ephemeral process namespaces, catches provider-specific failures, reports partial success, returns recovery actions, and exposes parser entrypoints for GrepAI backend actions and watcher actions. | L2692-L2819; L2867-L2916 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |

## Cross-Repo References

No sibling repository evidence is needed for the lifecycle script.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T23:55+02:00: Updated after adding `grepai run -- ...` for lifecycle-managed semantic queries.
- 2026-05-21T23:18+02:00: Updated after provider lifecycle began treating stale GrepAI root artifacts as disposable cleanup state, strengthened PostgreSQL/pgvector readiness checks, adopted already-running watchers, returned structured partial watcher results, and forced UTF-8 subprocess/stdio handling.
- 2026-05-21T17:16+02:00: Updated after daemon/server lifecycle actions began refusing ephemeral `--die-with-parent` process namespaces, status began reporting `processNamespace`, CGC dry-run backend start stopped probing loopback ports, and `cgc run` remained the bounded query path outside that daemon guard.
- 2026-05-21T15:42+02:00: Updated after provider lifecycle commands began inferring the coordinator root from the installed script path by default while keeping `--coordination-root` as an explicit override.
- 2026-05-21T15:35+02:00: Updated after explicit `run --lifecycle-json -- ...` output was compacted to `outputLines` plus minimal metadata and generic JSON rendering stopped ASCII-escaping UTF-8 glyphs.
- 2026-05-21T15:31+02:00: Updated after `cgc run --json` was changed to keep native provider output as the default and the old structured envelope moved behind `run --lifecycle-json -- ...`.
- 2026-05-21T15:24+02:00: Updated after human-mode `cgc run` began streaming native command stdout/stderr instead of rendering the captured subprocess envelope.
- 2026-05-21T13:22+02:00: Updated patch/status documentation after adding visualizer server and CLI route patches to keep `/` pointed at the explorer and unknown API routes JSON-shaped.
- 2026-05-21T13:04+02:00: Updated GrepAI watcher notes after start began parsing and recording the native background PID for managed status/stop.
- 2026-05-21T12:40+02:00: Updated after adding the CGC visualizer repo-query patch to status/patch verification.
- 2026-05-21T12:12+02:00: Updated after splitting the CGC visualizer into its own long-running `cgc visualize` lifecycle action and rejecting `run -- visualize`.
- 2026-05-21T12:35+02:00: Updated GrepAI lifecycle notes for provider-owned mirror roots and source-root `.grepai/` containment checks.
- 2026-05-21T12:20+02:00: Clarified that settings-backed CGC commands default to coordinator settings when `--from-settings` is omitted, matching the reinstall path.
- 2026-05-21T11:50+02:00: Updated for GrepAI workspace-mode lifecycle with runtime-owned release binary, Docker PostgreSQL/pgvector backend, provider-owned workspace config/log/state, and indexed-root `.grepai/` containment checks.
- 2026-05-21T03:05+02:00: Updated after adding `cgc run` as the lifecycle-managed pass-through for native CodeGraphContext relationship queries.
- 2026-05-21T02:33+02:00: Updated after adding the aggregate `watchers` lifecycle command for all enabled provider watchers.
- 2026-05-21T02:25+02:00: Updated GrepAI status notes after lifecycle status began returning unhealthy when the index is present but no native or managed watcher is running.
- 2026-05-21T02:20+02:00: Updated after Windows managed watcher status switched from `tasklist` output to direct PID checks through the Windows process API.
- 2026-05-21T02:10+02:00: Updated lifecycle notes for the `provider-data/` backend root and disposable `providers/` scaffold model.
- 2026-05-21T01:47+02:00: Clarified that settings-expanded CGC roots must resolve to existing code repository directories before runtime state is created.
- 2026-05-21T01:32+02:00: Updated after CGC moved to FalkorDB Docker only, added settings-expanded multi-root lifecycle commands, start-all/shutdown-all, managed patch verification, GrepAI installation, and stale provider runtime cleanup. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
- 2026-05-20T19:11+02:00: Created onboarding for the provider lifecycle CLI covering CGC and GrepAI status/start/stop/refresh/doctor flows. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
