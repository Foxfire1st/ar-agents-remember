# mcp/src/agents_remember/kernel/primitives/host_environment.py

## Governing Overview

[overview](overview.md)

## Purpose

The session identity a host must never hand to the next agent it starts.

## Code Commentary

`SESSION_VARIABLES` is loaded from the packaged `host-session-environment.json` and joined with `AR_HOSTED_SESSION_ID`; `is_session_variable` also matches the `PASEO_` and `AR_SPAWN_` prefixes. `host_environment` filters those names while keeping logins, and `carried_session_variables` reports names only, excluding `PASEO_HOME` which Paseo sets itself.

## Evidence

- The exact-name filter over a base environment. [1]
- The name-only observation of carried session variables. [2]
