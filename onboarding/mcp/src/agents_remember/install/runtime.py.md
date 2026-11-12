# mcp/src/agents_remember/install/runtime.py

## Current operative account — MIK-R112

The current source facts below are the operative account. Original paragraphs, evidence and citation identities remain in the explicitly historical section, corrected where the code does not support them; they grant no current call, restored route or fresh execution acceptance.

- Current install attempts only old-watcher stop and continues on failed stop.
- Current assets include docs and leftover/unused-provider reporting. Removed-store discovery and report formatting are imported from the shared `install/removed_stores.py` owner; this installer defines no second store/gate/lock inventory and performs no automatic deletion.
- Every accepted install removes the retired coordinator startup files `AGENTS.md`, `system/AGENTS.md` and `tasks/AGENTS.md`, selected experiment or not, and writes none of them.
- The `runtime_install` result carries `mcpSettings`: the one-time copy of the workspace's `.claude/mcp/agents-remember-settings.json` to the user's MCP settings file (`install/mcp_settings.py`), reported as `copied`, `would-copy`, `already-present`, `no-source`, `permission` or `refused`.
- The explicit upgrade copies the complete settings bytes and metadata to an exclusively created user file before removing the old file. R137 then closes file permissions to0444 and its folder to0555; permission bits are deliberately normalized, not preserved unchanged. Closure OSError leaves the completed move and a permissionsNote/protection report. Dry-run performs no transfer or closure. This read does not run an upgrade or edit the user file.

- Every accepted install removes the three retired coordinator startup files. [19]
- The install result carries the MCP settings copy outcome. [20]

- Whole-file exclusive transfer precedes old-file removal; permission closure and its OSError report follow it. [12]

- File0444/folder0555 closure is attempted, and protection reporting reads modes with exact commands. [13]

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/install/runtime.py:243-254`.
- Source comparison: `mcp/src/agents_remember/install/runtime.py:495-512`.
- Source comparison: `mcp/src/agents_remember/install/runtime.py:736-811`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[overview](../../../overview.md)

## Purpose

`install/runtime.py` is the package-local runtime installer service used by the
`runtime_install` MCP tool. It reconciles runtime assets into the configured
coordinator root and delegates provider watcher stop orchestration to
`install/provider_watchers.py`.

It also owns the **instruction cutover**: every accepted run removes the retired coordinator
startup files, and an explicitly selected run additionally probes the capsule path and records
the run. The selection vocabulary, the capability probe and the run record live in
`install/experiment.py`; this module decides *what an installation is* from that input.

## Code Commentary

### Experimental Cutover And The Two Entry Points

**One private path, two public entry points, deliberately.**

- `RuntimeInstallScope(source_root, coordination_root, dry_run, provider_deps, include_benchmarks,
  experiment)` is the frozen scope one install resolves. `experiment` is an optional
  `ExperimentSelection`; absent means the unmodified installation.
- `install_runtime(...)` keeps its five-argument signature for a run that selected nothing; it
  builds a scope without an experiment.
- `install_experimental_runtime(scope)` is the experimental entry point. It **refuses a scope that
  carries no experiment selection** instead of silently re-resolving the selection.
- Both funnel through one private `_install_runtime(scope)`, so the two cannot drift.
- `install_runtime_from_config(config, request)` is the MCP entry point: it resolves the request's
  `experiment` field before `AR_EXPERIMENT` from the ambient environment, and the run record names
  that fact as `selectionSource: environment` (a request-supplied selection records `request`).
  `resolve_experiment_install` also reads the ambient environment when a scope carries no selection.

**The refusal happens before the first write.** A selected run whose capability probe blocks raises
`ExperimentError` and creates no directory, replaces no file and removes nothing. A refused
experiment is never `legacy`: a runtime failure reports itself and preserves the selected mode rather
than quietly running the old startup chain.

**The cutover — `_capsule_cutover` and `RETIRED_STARTUP_TARGETS`.** Every accepted install, selected
or not, writes none of the three coordinator startup files (`AGENTS.md`, `system/AGENTS.md`,
`tasks/AGENTS.md`) and **removes** any copy an earlier install left, because a root holding both
instruction paths would carry exactly the duplicate startup corpus the cutover exists to prevent.
`_install_assets` syncs the provider tree and installs no coordinator `skills/` tree. In production
the capsule compiler resolves its corpus from the **packaged** tree (`application/skill_resources` →
`packaged_source_root()/runtime/skills`).

**No undo rows.** The experiment payload's `rollback` list is always empty; no run renders a
restore row, because no delivery mode restores the retired startup files.

### User settings upgrade and role-execution roots

`upgrade_user_settings` moves the entire old coordination settings file once to the user location: it refuses an existing destination, refuses a non-regular source, preserves metadata, and removes the old file only after the complete transfer succeeds, with dry-run and already-current/no-settings states. `_install_runtime` applies the location guard before any asset write, and the install ensures the workspace `.agents-remember/role-executions` directory with a Git ignore entry for per-execution report/scratch folders.

### Install Request And Tree-Sync Objects

Three frozen dataclasses carry what an install is asked to do:

- **`RuntimeTreeSync(source_root, destination_root, preserve=frozenset(), prune_ignore=frozenset(),
  copy_ignore=frozenset())`** — one packaged runtime tree mirrored into the coordination root.
  **The ownership rules travel with the pair of roots because they are what makes the mirror
  non-destructive**: `preserve` names destination paths a prune never removes (user-owned
  coordinator state), `prune_ignore` names paths pruned even when the packaged source still carries
  them, and `copy_ignore` names source paths the copy never writes.
  Signatures: `prune_tree(sync, summary, dry_run)` and `copy_tree(sync, summary, dry_run)`.
- **`ProviderDependencyInstall(settings, timeout, enabled=True, no_cache=False)`** — the
  provider-dependency step: whether it runs at all, the live provider settings it installs against,
  the per-provider budget, and whether caches may be reused. `install_runtime(source_root,
  coordination_root, dry_run, *, provider_deps, include_benchmarks=False)` takes it, and the
  watcher rebind is derived from the same object because it is the same step's stop/start cycle.
- **`RuntimeInstallRequest(dry_run=False, include_benchmarks=False, install_provider_deps=True,
  no_cache=False, provider_deps_timeout=None, source_root=None, experiment=None)`** — what one install
  is asked to do. `install_runtime_from_config(config, request)` takes it. `experiment` is the
  **per-run selection input** and the primary production input. `provider_deps_timeout` and
  `source_root` stay unset for MCP callers: the timeout then falls back to the config's provider
  setup cap and the source to the packaged runtime tree.

`dry_run=False` (act-by-default) is the default on both entry points.

### Logic

The service copies provider defaults and the shipped docs from the source/package runtime tree
into the configured coordinator and removes the retired coordinator `AGENTS.md` files. After the
user-owned directory ensures, this service
leaves the shared host/agentic settings authority to setup: the install step
never writes the single user settings file (`~/.config/agents-remember/settings.json`, under `XDG_CONFIG_HOME` when set). The c-13 install skill's Stage 2 interview edits the shared file
with the developer, and knob families the developer skips keep the built-in
absent-knob defaults. Runtime sync removes stale coordinator `scripts/` remnants because
the old source-side installer and skill-install script are not runtime entry points.
Dependency-skipped syncs preserve live provider runner
state under `providers/runners`, while stale `providers/_bin` and
`providers/_venvs` content is pruned because host provider binaries and venvs
are not part of the managed runtime contract. Before the provider tree is refreshed, the service
attempts to stop enabled provider watchers, records the result in the rebind report and continues
on a failed stop; enabled provider keys are reported as unused and drive no dependency install.
All installs preserve durable `providers/data` and central logs under `logs/`.

`install_runtime_from_config()` is the MCP entrypoint: it derives the target root
from `McpRuntimeConfig`, takes the packaged runtime assets from `packaged_source_root()`
(`install/assets.py`) unless the request names a `source_root`, and builds the provider step
from `lifecycle_settings_from_config()`, which emits an empty provider map; no provider
lifecycle install runs, and `no_cache` is carried on the step without reaching an install call.
The optional `source_root` parameter is an internal development/test hook, not a public MCP path field.

The module is intentionally not a second runtime-install command surface. MCP
clients reach it through the `runtime_install` tool, whose `experiment` parameter is
the run's own selection; `mcp/tools/core.py::runtime_install_payload` now takes the
run's `RuntimeInstallRequest` unchanged, so the knobs the tool exposes and the
fields the entry point reads cannot drift apart.

### Invariants And Boundaries

- MCP callers do not provide `coordinationRoot` or `sourceRoot`.
- The MCP package path is the runtime-install owner; source checkout installer
  scripts must not remain as a parallel route.
- **The selection is a run input, never a setting.** It is not read from a settings file and never
  written to one; the run record names which input supplied it. There is no persistent switch to
  leave on, and a deselected run is the unmodified installation.
- **`legacy` is unreachable for a selected run.** A selected run whose capsule path is unavailable
  is `refused` with the failure text — and refuses before the first write.
- **No delivery mode writes the coordinator startup files.** A third installer path, or a
  settings key that remembers the mode, is the silent/global switch the cutover forbids.
- **The coordination root carries no installed `skills/` tree.** The compiler reads
  `packaged_source_root()/runtime/skills`.
- Provider lifecycle settings come from `lifecycle_settings_from_config()`, which emits no
  provider block; no provider dependency install runs.
- Every install must preserve `providers/data` and central logs under `logs/`.
- `providers/_bin` is not preserved or recreated as a managed provider runtime
  path.
- `providers/_venvs` is not preserved or recreated as a managed provider
  runtime path.
- This service must not execute coordinator-local `scripts/provider-setup.py`
  for the MCP path.
- Coordinator runtimes do not receive source scripts; provider, benchmark, and
  install helpers stay in MCP package-owned code.
- `install_runtime_from_config`'s `dry_run` defaults to `False` (act-by-default),
  matching the `runtime_install` MCP tool; `dry_run=true` reports the reconcile
  plan without performing the reconcile.
- Provider watcher rebind reporting belongs in the install summary and response
  payload; the detailed lifecycle sequencing belongs in `install/provider_watchers.py`.
- **A symlinked `node_modules` is not covered by any ignore rule.** The root `.gitignore:8` entry is
  `node_modules/` **with a trailing slash**, which git matches against a **directory only**: a
  symlinked `node_modules` would be untracked-not-ignored and would stage as mode `120000`. What this
  module guarantees instead is asserted — the installed tree is a real directory (`is_dir()` and
  `not is_symlink()`) — and no `.gitignore` rule was added to cover the symlink case. Do not read
  that as a rule that exists.

## Evidence

### Repo-Internal References

- The MCP application entry point forwards one typed request to the installer. [1]

- `RuntimeInstallScope` carries an optional experiment selection, and both public entry points funnel through one private installer. [2]

- Every accepted install removes the retired coordinator startup files and writes none of them. [3]

- No skill tree is installed beside the runtime; the canonical corpus is reached from the packaged copy. [4]

- The selection is resolved and probed before any write; with no selection passed, the run's environment is read. [6]

- Provider settings generation derives lifecycle settings from MCP authority. [8]

- The install stores a provider watcher rebind report, attempts the old-watcher stop before the provider refresh and continues on a failed stop. [9]

- Provider watcher lifecycle orchestration and recovery-action construction live in the extracted install helper. [10]

## The host part

`install_runtime_from_config` returns the earlier service result only; the host part is composed by the application entry `run_runtime_install`, which adds `result["host"]` and the `ok` conjunction after this function returns, then the dashboard ensure (a plan on a dry run) as `result["dashboard"]` when a dashboard answers on its port, and the running-server inventory as `result["runningServers"]`. This function's result has no host, dashboard or server field.

- The application entry that composes the host step onto the lower service result. [11]

- The application entry adds the dashboard ensure and the running-server inventory to the install result. [21]

</details>

- Install consumes the one shared removed-store inventory without defining or deleting it. [14]

- The shared no-follow store/gate/lock inventory and reporting retain explicit user-owned removal. [15]

## Observed effects and no installed skill tree

`ensure_dir`, `copy_file`, `remove_path` and `ensure_gitignore_entry` each run inside `install.effects.observe_install_effect`, so the entries one call changed are reported whether the operation finished or raised, while an ordinary install's summary and behavior are unchanged. The install syncs no `skills` tree into the coordination root: canonical skills are served from the packaged copy by the tool server's own resource surface, and that folder is not created either. No install writes the coordinator, system or tasks instruction files; every accepted install removes them.

- The directory creation whose changed entries are observed. [16]
- The file copy whose changed entries are observed. [17]

- The install pass that writes the scaffold and no skill tree. [18]
