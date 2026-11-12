# mcp/src/agents_remember/serving/paseo/paseo_install.py

## Governing Overview

[overview](../overview.md)

## Purpose

The host part of `runtime_install`: it reads the host block of the MCP authority settings file at call time, runs the provision or a strictly read-only preview, and returns the host part of the install result.

## Code Commentary

`install_host` resolves `authority_settings_path(config.config_path)`, the file the tool server was started with, and returns `configured: false` with that path and the message naming the block when it holds none, naming a Bootstrap `role_start` as what establishes one. `preview_host` observes without a lock, download, npm install, setting write or daemon start and reports what would change, the Node it would install and whether a restart holds it back. A failure returns the typed error payload while the earlier install steps stand.

The preview's `changes` is the action list of `paseo_install_plan.planned_changes`, described by the same functions the real provision records its changes with; `changed`, `daemon.action` (`started`, `reloaded` or `untouched`) follow from that list. When a restart is held back the preview plans no change, names the restart under `deferred` with its reasons, and reads the installed CLI version from its package manifest instead of running it.

## Evidence

- The install host entry point and its configured/absent result. [1]

- The read-only preview that makes no changing call. [2]

- The install host entry point and the authority file it reads. [3]

- The preview's action list, daemon action and deferred restart come from the shared install plan. [4]
