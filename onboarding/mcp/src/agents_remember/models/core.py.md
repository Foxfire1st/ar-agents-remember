# mcp/src/agents_remember/models/core.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Declare boot/build identity, role-launched server binding and retained server information.

## Code Commentary

ServingBuildPayload and AgentBindingPayload forbid extra fields. Build identity is supplied
at boot, not fabricated at each query; agent binding carries recorded canonical selection
references and does not itself authorize work. ServerInfoResponse requires stdio transport,
configured roots and servingBuild, with optional toolServer/agentBinding.
Its allowedRepoIds and unusedProviderKeys lists default empty. Old provider configuration
keys are unused metadata, not live capabilities. PingResponse is deleted; tools/reservedTools
and allowedProviderIds are not current server-info inventory fields. Read-only information
and DTO presence are distinct from actual runtime tool advertisement.

## Current model evidence

- Current source section contains excerpt `class ServerInfoResponse(ResponseModel):`; DTO/control ownership is not execution acceptance. [4]
- Current source section contains excerpt `class ServingBuildPayload(BaseModel):`; DTO/control ownership is not execution acceptance. [5]
- Current source section contains excerpt `def server_info_payload(`; DTO/control ownership is not execution acceptance. [6]

## Historical superseded account (non-operative)

Prior removed-tool/current-roster claims below are preserved provenance, not current
registration, runtime capability or execution evidence.



`core.py` defines response models for the core `ping` MCP tool and `server_info`
tools.

Defines boot-bound build and core server-info response shapes.

## Code Commentary

`ServingBuildPayload` is the strict shared runtime identity: version and boot time plus optional
source digest, interpreter, package root, checkout commit, dashboard fingerprint, and proven-dirty
evidence. `PingResponse` reports server identity, version, and transport. `ServerInfoResponse` adds
config, coordination, workspace, transcript, allowed repo/provider, public-tool, reserved-tool
metadata, and that payload under `servingBuild`.

### Role Runtime and Scope

AgentBindingPayload captures launch agent, role, request, report and optional canonical task references. ServerInfoResponse adds optional toolServer and agentBinding beside unchanged server package name and servingBuild; unbound servers omit those launch-specific fields.

## Invariants And Boundaries

- Transport is currently the literal `stdio`.
- `server_info` should report configured authority and public surface, not
  perform runtime mutation.
- `servingBuild` is required on `server_info`; candidate identity cannot collapse to the package
  version string.

## Evidence

### Repo-Internal References

- Core payload builders serialize these models. [1]

### Runtime Source References

- Frozen implementation of AgentBindingPayload supporting the stated file behavior. [2]
- Frozen implementation of ServerInfoResponse supporting the stated file behavior. [3]

## Server info keeps no harness skill root

`ServerInfoResponse` no longer declares `harnessSkillRoot`, and `server_info_payload` no longer answers it: no skill folder is resolved for a harness, so the field had no current value to report. Transport, roots, allowed repo ids and unused provider keys are unchanged.

- The strict server-info DTO without a harness skill root. [7]
