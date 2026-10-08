# mcp/src/agents_remember/cli/paseo_bridge.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Runs one bounded JavaScript bridge command and interprets its one JSON reply.

## Code Commentary

bridge_call sends prompt/payload as stdin data and stops a process at 60 seconds. _bridge_environment removes inherited PASEO/AR_PASEO values, then supplies configured URL, home server ID, pin and deadline. Missing settings/identity refuse before process start; unreadable replies, replacement-decoded output and bounded fatal lines remain named failures.

## Bounded bridge calls (MIK-R76)

`bridge_call` takes an optional `timeout_seconds` that defaults to the existing
`PASEO_BRIDGE_TIMEOUT_SECONDS` (60 s). The subprocess timeout and the reported failure text use it,
and the bridge environment gains `AR_PASEO_DEADLINE_MS`, set to the smaller of the script deadline
and the supplied timeout minus a 100 ms margin, so a caller with a shorter remaining budget bounds
the JavaScript side too. The archive service uses this to keep its per-target call inside the
closing archive budget.

## Evidence

- Frozen implementation of bridge_call supporting the stated file behavior. [1]
- Frozen implementation of _bridge_environment supporting the stated file behavior. [2]
- Frozen implementation of _configured_server_id supporting the stated file behavior. [3]
- Checks exact endpoint/server-id environment and removal of inherited PASEO/AR_PASEO values. [4]
- Checks absent settings or home server-id start no process. [5]
- Exercises different/missing connected server identity and named refusal with reconnect disabled. [6]

## 260928-MIK-L96 Node and remedy text

The bridge starts the product's Node by its full path instead of looking for `node` on `PATH`; a missing product Node is named as the install step's state. The remedy that used to say the Paseo bridge needs Node.js on PATH now names the install step, and the not-installed text names the install step while the not-configured text keeps its own meaning.

- The bridge launch that starts the product's Node by full path with the packaged script and names this build's install state. [7]

- The configured-runtime requirement the bridge enforces before any process starts. [8]
