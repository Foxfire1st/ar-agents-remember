# mcp/src/agents_remember/models/core.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`core.py` defines response models for the core `ping` MCP tool and `server_info`
tools.

## Code Commentary

`ServingBuildPayload` is the strict shared runtime identity: version and boot time plus optional
source digest, interpreter, package root, checkout commit, dashboard fingerprint, and proven-dirty
evidence. `PingResponse` reports server identity, version, and transport. `ServerInfoResponse` adds
config, coordination, workspace, transcript, allowed repo/provider, public-tool, reserved-tool
metadata, and that payload under `servingBuild`.

## Invariants And Boundaries

- Transport is currently the literal `stdio`.
- `server_info` should report configured authority and public surface, not
  perform runtime mutation.
- `servingBuild` is required on `server_info`; candidate identity cannot collapse to the package
  version string.

## Evidence

### Repo-Internal References

- Core payload builders serialize these models. [1]
