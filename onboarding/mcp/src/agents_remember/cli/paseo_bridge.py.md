# mcp/src/agents_remember/cli/paseo_bridge.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Runs one bounded JavaScript bridge command and interprets its one JSON reply.

## Code Commentary

bridge_call sends prompt/payload as stdin data and stops a process at 60 seconds. _bridge_environment removes inherited PASEO/AR_PASEO values, then supplies configured URL, home server ID, pin and deadline. Missing settings/identity refuse before process start; unreadable replies, replacement-decoded output and bounded fatal lines remain named failures.

## Evidence

- Frozen implementation of bridge_call supporting the stated file behavior. [1]
- Frozen implementation of _bridge_environment supporting the stated file behavior. [2]
- Frozen implementation of _configured_server_id supporting the stated file behavior. [3]
- Checks exact endpoint/server-id environment and removal of inherited PASEO/AR_PASEO values. [4]
- Checks absent settings or home server-id start no process. [5]
- Exercises different/missing connected server identity and named refusal with reconnect disabled. [6]
