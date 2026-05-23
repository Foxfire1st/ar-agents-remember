# mcp/src/agents_remember/install/runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/install/runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T05:32+02:00                     |
| lastVerifiedCommitHash | `7ab4b520b9178a31c4a5f5f8a5393b9b6ba82e0e` |
| lastVerifiedCommitDate | 2026-05-22T21:20:47+02:00                 |
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

The service copies package runtime skills, the runtime `install-skills.sh` script, provider defaults, and
runtime `AGENTS.md` templates from the source/package runtime tree into the
configured coordinator. Normal runtime syncs preserve provider dependency and runner
state under `_bin`, `_venvs`, and `providers/runners`, while explicit provider
dependency installs can reconcile those paths through package-local lifecycle code.
All installs preserve durable `providers/data` and `providers/logs`.
`install_runtime_from_config()` is the MCP
entrypoint: it derives the target root from `McpRuntimeConfig`, generates
provider lifecycle settings from MCP settings, calls package-local provider
lifecycle install functions when provider deps are enabled, and writes a runner
integrity manifest after non-dry-run installs.

The module is intentionally not a second runtime-install command surface. MCP
clients reach it through the `runtime_install` tool; old direct CLI install
behavior remains in the root `installer/install-runtime.py` path.

### Invariants And Boundaries

- MCP callers do not provide `coordinationRoot` or `sourceRoot`.
- The MCP package path must not carry a separate runtime-install wrapper.
- MCP provider dependency install must use generated settings from
  `McpRuntimeConfig`.
- Full provider reinstall can replace binaries, venvs, and runner instances,
  but must preserve `providers/data` and `providers/logs`.
- This service must not execute coordinator-local `scripts/provider-setup.py`
  for the MCP path.
- Coordinator runtimes receive only `scripts/install-skills.sh`; Python
  provider and benchmark helpers stay in source/package-owned code.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The MCP controller exposes only typed install booleans. | [runtime_install.py](agents-remember-md/mcp/src/agents_remember/controllers/runtime_install.py) |
| Provider settings generation derives lifecycle settings from MCP authority. | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |
| Integrity manifests are written after non-dry-run installs. | [integrity.py](agents-remember-md/mcp/src/agents_remember/providers/integrity.py) |

## Update History

- 2026-05-23T05:32+02:00: Clarified that runtime sync installs only `scripts/install-skills.sh` into coordinators while MCP provider installs use package-local lifecycle code.
- 2026-05-23T04:43+02:00: Clarified that MCP install is exposed through the typed tool, not a package-local wrapper command.
- 2026-05-23T04:29+02:00: Created when runtime installation moved behind the MCP/package-local boundary.
