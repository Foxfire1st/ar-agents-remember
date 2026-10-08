# mcp/src/agents_remember/package_data/host-session-environment.json

## Governing Overview

[overview](../../../overview.md)

## Purpose

The product-owned exact-name list of harness session variables that a host start removes.

## Code Commentary

The file is a JSON object mapping each exact session-variable name to its rationale (an exact-name-to-reason map, not an array). `host_environment.py` reads the object's keys at import and joins `AR_HOSTED_SESSION_ID`, so product filtering works from the keys; the sandbox tooling merges the same mapping into its own additions, which is why its removal path expands `**SESSION_VARIABLES`.

## Evidence

- The packaged list read by the environment filter. [1]
