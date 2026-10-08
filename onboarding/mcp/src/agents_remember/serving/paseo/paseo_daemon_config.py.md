# mcp/src/agents_remember/serving/paseo/paseo_daemon_config.py

## Governing Overview

[overview](../overview.md)

## Purpose

Writes private provider configuration and the daemon agent-tools setting.

## Code Commentary

Provider entries may contain environment secrets, so write_provider_entries writes the private config file rather than putting values on command lines. The preceding config and written digest support exact rollback; accept_provider_entries acknowledges confirmed native config. Recovery does not invent a second configuration store.

L96: the module moved from `cli/paseo_daemon_config.py` into `serving/paseo/`; only its intra-package imports changed.

## Evidence

- The private provider write with its rollback files. [1]
