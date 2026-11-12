# mcp/src/agents_remember/providers/lifecycle/ - Provider Lifecycle Facade Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/providers/lifecycle/` |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`lifecycle/` supplies the shared Python facade, watcher aggregation, and provider-agnostic helpers for optional context-provider lifecycles. Provider-specific implementations live under `providers/cgc/lifecycle/` and `providers/grepai/lifecycle/`. The facade lazily resolves exports from those packages and the shared modules. It no longer exports a CLI module; `cli.py` and `__main__.py` are absent from this source checkout.

## Hot Path Summary

Start with `__init__.py` for lazy export resolution and `watchers.py` for enabled-provider stop and shutdown-all aggregation. `providers/lifecycle_service.py` calls the facade directly with settings-owned arguments. Shared responsibilities are split among `command_runner.py`, `compose_runtime.py`, `docker_runtime.py`, `host_ports.py`, `log_capture.py`, `process_status.py`, `provider_settings.py`, `runtime_environment.py`, and `state_files.py`.

CGC's package groups settings/layout, Compose rendering, FalkorDB backend, runner, installation/status, and process control functions. GrepAI's package groups settings/workspace, Compose rendering, PostgreSQL backend, Ollama embedder, runner, and high-level actions. These retained Python implementations do not establish an executable package entrypoint.

## How It Is Built

The facade searches its ordered module tuple on attribute access and caches a matching attribute in its globals. Watcher aggregation reads provider enablement from an explicit settings file, invokes enabled GrepAI and CGC handlers, and combines their results, partial-success indication, process-namespace information, and recovery actions. Every admitted watcher action is a stop.

Compose planning renders the symbolic `docker` command without requiring executable discovery. Real Compose execution resolves Docker through `docker_command` and then runs the command. Watcher Compose rendering emits a host `user:` block only when both `os.getuid` and `os.getgid` are callable.

`BackendStartReconciliation` is a frozen shared value containing network information and optional migration and forced-removal results. CGC and GrepAI backend-start functions construct it after migration and mismatched-container reconciliation. Their completed start responses carry its network information and reconciliation command results; dry-run responses carry planned Compose commands and migration information. This shared shape belongs here because both provider backends use it.

Docker helpers normalize container state, running state, start time, uptime, and health. Provider-specific modules turn those facts and their Compose command outcomes into lifecycle results; no shared projection aggregates provider readiness from them.

`log_capture.py` recursively reduces response detail. `_shrink_logs` empties captured output on successful nodes and keeps a bounded failure tail otherwise, retaining existing log keys. `_drop_verbose_plumbing` always removes the duplicate `json` mirror, removes command/Compose/migration detail on success, and retains failure detail with command-token redaction.

## Invariants And Boundaries

The shared facade is the entry used by the typed lifecycle service. Provider-specific lifecycle behavior belongs in the CGC and GrepAI packages; shared helpers cover subprocess execution, Compose, Docker inspection, ports, process namespaces, settings, rendering, environment construction, and JSON state files.

Settings readers require an explicit settings path. `require_lifecycle_settings_path` rejects `None` rather than selecting `<coordination_root>/system/settings.json`. Service callers supply that path through their normalized configuration. The retained error text names `--from-settings`; it does not establish an available CLI.

`run_command` accepts no environment override and obtains its environment from `runtime_environment.subprocess_env(None)`. Do not restore the removed environment-override knob; extra variables belong in runtime_environment.py. That helper copies the inherited process environment and sets `PYTHONUTF8` and `PYTHONIOENCODING`. This is environment construction with UTF-8 settings, not credential or environment sanitization.

The retained GrepAI lifecycle is organized around its Docker backend, embedder, runner, and Compose actions. Its Docker status combines backend, embedder, and watcher results. The shared facade does not add a host-binary or host-Ollama execution route.

Watcher stop and shutdown-all require the durable-process-namespace check when they are not dry runs. Disabled providers are omitted from watcher results; combined success is computed from the included results.

## Source And Authority Bounds

This account describes retained source behavior. It supplies no test execution, native-host result, whole-build acceptance, landing acceptance, or memory acceptance. Lifecycle/status metadata and historical repair labels are outside its operative promises; no lifecycle authority establishing a current operational status was supplied for this review.

There is a retained caller inconsistency: `providers/setup_common.py` still describes package execution and calls `lifecycle.main`, although this package has no `__main__.py`, no `cli.py`, and no CLI module in its export tuple. That caller does not restore the deleted route or prove successful execution.

## Evidence

- Public lifecycle exports are collected by the package facade. [1]
- The former package-execution entrypoint is absent; the current facade export tuple contains no CLI module. [2]
- CGC lifecycle implementation is grouped under the CGC provider package. [3]
- GrepAI lifecycle implementation is grouped under the GrepAI provider package. [4]
- Watcher aggregation uses explicit settings, enabled-provider dispatch, combined results, and durable-namespace checks. [5]
- Typed lifecycle services dispatch directly through the facade with settings-owned arguments. [6]
- Compose plans use symbolic Docker; execution discovers Docker; host-user rendering requires callable UID/GID functions. [7]
- Frozen backend reconciliation is shared by CGC and GrepAI and carried into start results. [8]
- Docker summaries expose container facts; no shared projection aggregates provider readiness, and the retired provider summary reports configured-or-not with `state: skipped` and reads no current-state or readiness detail. [9]
- Recursive response reduction distinguishes successful nodes from failure detail. [10]
- Settings readers reject a missing explicit path. [11]
- Command execution has no environment override; its environment inherits process variables and sets UTF-8 controls. [12]
- Shared port, namespace, rendering, and JSON-state responsibilities remain in named helper modules. [13]
- Retained GrepAI Docker status combines backend, embedder, and watcher results. [14]
- A retained setup caller still requests package execution and lifecycle.main. [15]
