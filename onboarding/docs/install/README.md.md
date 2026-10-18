# docs/install/README.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The install-guide index: how to copy the Agents Remember starter package for each agent harness and
what the normal first-run path is. Per-harness pages are linked from it; the package files are meant
to be copy-pasteable.

## Current source account

The normal path: copy the harness-native package files from the repository into the workspace; render
the copied package with `render-starter` (`.py`, `.sh` or `.ps1`), which infers the workspace root from
the copied harness folder, fills repository names and hook/context commands, validates that each
requested repository folder exists, and creates the one shared host settings file when absent;
register the MCP server (`uvx agents-remember-mcp@latest --config <absolute path to
agents-remember-settings.json>`); restart the harness once; invoke `c-13-install-and-onboard`, which
runs or verifies `runtime_install()` — provisioning the build-pinned Paseo host and its plugin on the
product's checked Node — and then handles memory, onboarding and providers.

The renderer creates one shared `~/.config/agents-remember/settings.json` (or
`$XDG_CONFIG_HOME/agents-remember/settings.json`) `paseoRuntime` block for all harnesses, with absolute
data/state paths and a fresh `127.0.0.1:8766` listen; it never overwrites an existing file. The guide
records the shipped host's limits: Linux x86_64 with `/proc` only, one exact host, a whole npm lock,
and Node 26.11.1 with its official archive digest. A missing shared block is reported as
`configured=false`; a block is added from the c-13 five-key form and `runtime_install` is retried.
Existing per-harness blocks are ignored with a migration notice and are moved to the shared file
preserving explicit listen/home/prefix settings. The renderer also accepts `--coordination-root`,
`--host-port` and `--dashboard-port`, defaulting to workspace/ar-coordination, 8766 and 8765.

Settings: an old coordination settings file, alone or beside the user file, refuses rendering before
any harness file is changed; the refusal names both paths and the explicit whole-file upgrade command
(`agents-remember upgrade-user-settings --coordination-root <absolute root>`), and the renderer never
selects or migrates an old file. The dashboard start uses the served version from `server_info`; a
start uses the installed host and never installs or upgrades.

The guide also records initial skills and hooks/rules/instructions coming from the copied package
(they are not installed for first-run setup), the native-Windows long-path setting, and
`worktree_start` refusing a projected path the host cannot represent.

## Boundaries

Instructions for a person and an agent; not proof that a renderer or install ran, that a harness
restarted, or that a host was provisioned on any machine.
