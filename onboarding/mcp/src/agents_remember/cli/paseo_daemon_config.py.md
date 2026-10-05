# mcp/src/agents_remember/cli/paseo_daemon_config.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Writes private provider configuration and the daemon agent-tools setting.

## Code Commentary

Provider entries may contain environment secrets, so write_provider_entries writes the private config file rather than putting values on command lines. The preceding config and written digest support exact rollback; accept_provider_entries acknowledges confirmed native config. Recovery does not invent a second configuration store.

## Evidence

- Frozen implementation of write_provider_entries supporting the stated file behavior. [1]
- Frozen implementation of restore_previous_config supporting the stated file behavior. [2]
- Frozen implementation of agent_tools_setting supporting the stated file behavior. [3]
