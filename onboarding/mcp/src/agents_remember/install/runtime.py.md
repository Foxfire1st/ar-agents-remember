# mcp/src/agents_remember/install/runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/install/runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-04T22:15+02:00|
| lastVerifiedCommitHash | `0eba27a75a37ebc4ce1baeb9da9d7b7a879a8974` |
| lastVerifiedCommitDate | 2026-06-04T22:38:48+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`install/runtime.py` is the package-local runtime installer service used by the
`runtime_install` MCP tool. It reconciles runtime assets into the configured
coordinator root, delegates provider watcher rebind orchestration to
`install/provider_watchers.py`, and can run provider dependency installation
through package-local lifecycle functions.

## Code Commentary

### Logic

The service copies package runtime skills, provider defaults, and runtime
`AGENTS.md` templates from the source/package runtime tree into the configured
coordinator. Runtime sync removes stale coordinator `scripts/` remnants because
the old source-side installer and skill-install script are no longer valid
runtime entry points. Dependency-skipped syncs preserve live provider runner
state under `providers/runners`, while stale `providers/_bin` and
`providers/_venvs` content is pruned because host provider binaries and venvs
are not part of the managed runtime contract. Explicit provider dependency
installs reconcile supported provider paths through package-local lifecycle
code. When provider dependencies are installed, the service stops enabled
provider watchers before runner scaffolding can be pruned, refreshes managed
provider runtime files and dependencies, then starts and checks the watchers so
containers rebind to the current runner roots. If the first post-install status
is still degraded, it records one non-destructive restart/rebind attempt and
reports recovery guidance if readiness is still not restored. All installs
preserve durable `providers/data` and central logs under `logs/`.

`source_root_from_package()` locates the packaged runtime assets by walking
upward from the installed module until it finds the source/runtime asset tree.
`install_runtime_from_config()` is the MCP entrypoint: it derives the target root
from `McpRuntimeConfig`, generates provider lifecycle settings from MCP
settings, and calls package-local provider lifecycle install functions when
provider deps are enabled. It threads `no_cache` through to the provider
lifecycle install calls:
by default image builds skip any image whose tag already exists, and
`no_cache=true` forces a from-scratch rebuild. The optional `source_root`
parameter is an internal development/test hook, not a public MCP path field.

The module is intentionally not a second runtime-install command surface. MCP
clients reach it through the `runtime_install` tool.

### Invariants And Boundaries

- MCP callers do not provide `coordinationRoot` or `sourceRoot`.
- The MCP package path is the runtime-install owner; source checkout installer
  scripts must not remain as a parallel route.
- MCP provider dependency install must use generated settings from
  `McpRuntimeConfig`.
- Full provider reinstall can replace Docker runner instances and image build
  roots, but must stop/restart enabled watchers around that replacement and
  must preserve `providers/data` and central logs under `logs/`.
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The MCP controller exposes only typed install booleans. | [runtime_install.py](agents-remember-md/mcp/src/agents_remember/controllers/runtime_install.py) |
| Provider settings generation derives lifecycle settings from MCP authority. | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |
| `install_runtime` stores a provider watcher rebind report, stops watchers before provider refresh, starts/checks them afterward, and includes rebind/recovery details in the MCP payload. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| Provider watcher lifecycle orchestration and recovery-action construction live in the extracted install helper. | [provider_watchers.py](agents-remember-md/mcp/src/agents_remember/install/provider_watchers.py) |
| Runtime-install tests cover watcher stop/start ordering, dry-run reporting, degraded-status retry, unrecovered failure reporting, and dependency-install failure recovery. | [test_install_runtime.py](agents-remember-md/mcp/tests/test_install_runtime.py) |

## Update History

- 2026-06-04T22:15+02:00 — Documented provider watcher rebind orchestration for `install_provider_deps=true`, including the extracted helper, non-destructive retry, recovery reporting, and preserved provider data.
- 2026-05-31T12:30+02:00 — Dropped the provider runner integrity-manifest write from `install_runtime_from_config` and the `integrity` return field, and removed the stale integrity.py reference (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented the `no_cache` flag threaded through `install_runtime_from_config` into the provider lifecycle install calls — image builds skip existing tags by default, `no_cache=true` forces a from-scratch rebuild. Verified against `8927f03`.
- 2026-05-29T18:35+02:00: Extracted `_remove_with_retry` from `remove_path` to drop cyclomatic complexity below 11; behavior-preserving (commit `e3dab63`).
- 2026-05-28T12:32+02:00: Updated after runtime install moved operator logs from `providers/logs/` into the central `logs/` tree.
- 2026-05-26T12:51+02:00: Updated after runtime install stopped preserving provider venvs and CGC provider dependencies became Docker-owned.
- 2026-05-25T18:07+02:00: Updated after runtime install stopped preserving `providers/_bin`; Docker-owned GrepAI keeps binaries inside the runner image.
- 2026-05-24T00:37+02:00: Refreshed verification and documented that packaged asset discovery owns normal runtime source selection, with `source_root` reserved for internal development/test use.
- 2026-05-23T14:20+02:00: Updated after `runtime_install` stopped requiring or copying `runtime/scripts/install-skills.sh` and began removing stale coordinator `scripts/` remnants.
- 2026-05-23T05:32+02:00: Clarified the earlier intermediate state where runtime sync still installed only `scripts/install-skills.sh` into coordinators while MCP provider installs used package-local lifecycle code.
- 2026-05-23T04:43+02:00: Clarified that MCP install is exposed through the typed tool, not a package-local wrapper command.
- 2026-05-23T04:29+02:00: Created when runtime installation moved behind the MCP/package-local boundary.
