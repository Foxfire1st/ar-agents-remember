# mcp/src/agents_remember/serving/paseo/paseo_daemon_config.py

## Governing Overview

[overview](../overview.md)

## Purpose

Writes private provider configuration, and names and reads the daemon agent-tools setting.

## Code Commentary

Provider entries may contain environment secrets, so write_provider_entries writes the private config file rather than putting values on command lines. The preceding config and written digest support exact rollback; accept_provider_entries acknowledges confirmed native config. Recovery does not invent a second configuration store.

`provider_recovery_plan` makes the whole-file-versus-provider-only recovery decision without changing any file; `restore_previous_config` applies it, and the install preview uses the same decision and the recovered document while reporting no provider value.

`host_provider_extra_args` reads a provider's configured `extraArgs` names from `config.json` and from the running daemon's map through the `DaemonConfigRead` port, which the composition root binds to the bridge's `daemon-config` call; this layer makes no cli import. A read that fails, or a caller without that port, raises `daemon_config_unverified` naming the provider instead of answering no argument. The read only reports names and decides no limit.

## Evidence

- The private provider write with its rollback files. [1]

- The recovery decision is observed without changing recovery files and shared by preview and recovery. [2]
- The running daemon's provider map is read through the port and an unread map refuses. [3]
