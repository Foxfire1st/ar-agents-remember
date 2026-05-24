# mcp/src/agents_remember/install/runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/install/runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T00:37+02:00                     |
| lastVerifiedCommitHash | `31846c1136f0fe75503a63fb557303a79fa022e8` |
| lastVerifiedCommitDate | 2026-05-24T23:07:31+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`install/runtime.py` is the package-local runtime installer service used by the
MCP `runtime_install` tool. It reconciles runtime assets into the configured
coordinator root and can run provider dependency installation through
package-local lifecycle functions.

## Code Commentary

### Logic

The service copies package runtime skills, provider defaults, and runtime
`AGENTS.md` templates from the source/package runtime tree into the configured
coordinator. Runtime sync removes stale coordinator `scripts/` remnants because
the old source-side installer and skill-install script are no longer valid
runtime entry points. Dependency-skipped syncs preserve provider dependency and
runner state under `_bin`, `_venvs`, and `providers/runners`, while explicit
provider dependency installs can reconcile those paths through package-local
lifecycle code. All installs preserve durable `providers/data` and
`providers/logs`.

`source_root_from_package()` locates the packaged runtime assets by walking
upward from the installed module until it finds the source/runtime asset tree.
`install_runtime_from_config()` is the MCP entrypoint: it derives the target root
from `McpRuntimeConfig`, generates provider lifecycle settings from MCP
settings, calls package-local provider lifecycle install functions when provider
deps are enabled, and writes a runner integrity manifest after non-dry-run
installs. The optional `source_root` parameter is an internal development/test
hook, not a public MCP path field.

The module is intentionally not a second runtime-install command surface. MCP
clients reach it through the `runtime_install` tool.

### Invariants And Boundaries

- MCP callers do not provide `coordinationRoot` or `sourceRoot`.
- The MCP package path is the runtime-install owner; source checkout installer
  scripts must not remain as a parallel route.
- MCP provider dependency install must use generated settings from
  `McpRuntimeConfig`.
- Full provider reinstall can replace binaries, venvs, and runner instances,
  but must preserve `providers/data` and `providers/logs`.
- This service must not execute coordinator-local `scripts/provider-setup.py`
  for the MCP path.
- Coordinator runtimes do not receive source scripts; provider, benchmark, and
  install helpers stay in MCP package-owned code.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The MCP controller exposes only typed install booleans. | [runtime_install.py](agents-remember-md/mcp/src/agents_remember/controllers/runtime_install.py) |
| Provider settings generation derives lifecycle settings from MCP authority. | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |
| Integrity manifests are written after non-dry-run installs. | [integrity.py](agents-remember-md/mcp/src/agents_remember/providers/integrity.py) |

## Update History

- 2026-05-24T00:37+02:00: Refreshed verification and documented that packaged asset discovery owns normal runtime source selection, with `source_root` reserved for internal development/test use.
- 2026-05-23T14:20+02:00: Updated after `runtime_install` stopped requiring or copying `runtime/scripts/install-skills.sh` and began removing stale coordinator `scripts/` remnants.
- 2026-05-23T05:32+02:00: Clarified the earlier intermediate state where runtime sync still installed only `scripts/install-skills.sh` into coordinators while MCP provider installs used package-local lifecycle code.
- 2026-05-23T04:43+02:00: Clarified that MCP install is exposed through the typed tool, not a package-local wrapper command.
- 2026-05-23T04:29+02:00: Created when runtime installation moved behind the MCP/package-local boundary.
