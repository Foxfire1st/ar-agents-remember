# mcp/src/agents_remember/models/core.py

## Governing Overview

[overview](overview.md)

## Purpose

Declare boot/build identity, the running-server inventory row, role-launched server binding and retained server information.

## Code Commentary

ServingBuildPayload, RunningServerPayload and AgentBindingPayload forbid extra fields. Build identity is supplied
at boot, not fabricated at each query; agent binding carries recorded canonical selection
references and does not itself authorize work. ServerInfoResponse requires stdio transport,
configured roots and servingBuild, with optional toolServer/agentBinding.
Its allowedRepoIds, unusedProviderKeys, unusedSettingsKeys and runningServers lists default empty.
Old provider configuration keys are unused metadata, not live capabilities. tools/reservedTools
and allowedProviderIds are not current server-info inventory fields.
RunningServerPayload is one live server's recorded boot identity (pid, role, start time, config
path, optional loaded digest and package root) with its observed BuildCurrentnessPayload;
server_info and runtime_install report a list of them from the server registry. Read-only information
and DTO presence are distinct from actual runtime tool advertisement.

## Current model evidence

- Current source section contains excerpt `class ServerInfoResponse(ResponseModel):`; DTO/control ownership is not execution acceptance. [4]
- Current source section contains excerpt `class ServingBuildPayload(BaseModel):`; DTO/control ownership is not execution acceptance. [5]

- `server_info_payload` builds the server-info answer this module's DTO declares. [6]

## Response Shapes

`ServingBuildPayload` is the strict shared runtime identity: version and boot time plus optional
source digest, interpreter, package root, checkout commit, dashboard fingerprint, and proven-dirty
evidence. `ServerInfoResponse` reports server name, version, transport, config, coordination,
workspace and transcript roots, allowed repo ids, unused provider and settings keys, the optional
open-user-settings notice, that payload under `servingBuild`, and the running-server inventory under
`runningServers`.

### Role Runtime and Scope

AgentBindingPayload captures launch agent, role, request, report and optional canonical task references. ServerInfoResponse adds optional toolServer and agentBinding beside the server package name and servingBuild; unbound servers omit those launch-specific fields.

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

- `ServerInfoResponse` declares the strict server-info answer, including unused keys, serving build, running servers and the optional agent binding. [3]

## Server info keeps no harness skill root

`ServerInfoResponse` declares no `harnessSkillRoot`, and `server_info_payload` answers none: no skill folder is resolved for a harness.

- The strict server-info DTO without a harness skill root. [7]

- One running server's boot identity and observed build currentness. [8]
- Server info carries the running-server inventory, empty by default. [9]
