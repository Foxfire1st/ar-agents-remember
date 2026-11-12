# mcp/src/agents_remember/mcp/tools/core.py

## Governing Overview

[overview](overview.md)

## Current source contract evidence

- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance.

## Purpose

Build server information, scoped slim orientation and runtime-installation answers. There is no context-resolution adapter in this module.

## Code Commentary

`server_info_payload` receives the boot-resolved serving build, reports unusedProviderKeys and
optional launch agentBinding/toolServer, and does not publish tools/reservedTools or remeasure the
serving-build identity. It adds `buildCurrentness` — the loaded build compared with the Python files
now at its package root, inspected for a checkout build too (`inspect_checkout=True`) and omitted
when no reading exists — and `runningServers`, the live records of the running-server registry, each
with its own currentness. `context_packet_payload` resolves the reader's exact task context
before calling the rich application builder, then applies `slim_context_packet` with the optional
serving-build commit. Mounted answers carry roots, task, action lines and short build/pair values;
the log preserves that delivered slim answer. Rich V2 is rebuilt through the internal/CLI/dashboard
builder, not automatically stored by this adapter. No TaskRef/resolve-context route remains.
Runtime installation forwards its per-call request unchanged; the request experiment takes
precedence over the documented environment fallback. With `request.dry_run=true`, the
adapter passes `report_path=None`: the preview files no per-call report and exposes no
`reportPath`. Only an executed install files the full result before response compaction
and supplies that report's path. Compaction projects only declared RUNTIME_INSTALL_ANSWER_FIELDS, which include the install's
`runningServers` inventory and `dashboard` result;
for a list of messages it retains string entries among the first five original entries,
truncates each to the short-string bound plus an ellipsis when needed, and reports overflow
from original list length. The rebind digest retains attempted/ok and phase/action/ok for
mapping-shaped runs. For an executed install, full detail can be reopened in its filed
report. Retained response logs are separate custody, not a per-call report for a preview;
the compactor's overflow wording does not establish that an unfiled preview has a report.
The module holds no ping or skill-installation adapter and supplies no generic restart tool.

## Current evidence

- Current source excerpt `def server_info_payload(` identifies this section's adapter/control owner, not an executed success.

- Current source excerpt `class ServerInfoResponse(ResponseModel):` identifies this section's adapter/control owner, not an executed success.

- Current source excerpt `def runtime_install_payload(` identifies this section's adapter/control owner, not an executed success.

- Current source excerpt `# Rule 2: a list with more entries is cut; the answer keeps the count, the` identifies this section's adapter/control owner, not an executed success.

## Invariants And Boundaries

- Every builder returns through `base._tool_payload`.
- Imports `SERVER_NAME`/`SERVER_VERSION` via `..` and `McpRuntimeConfig` from
  `kernel.primitives.runtime_config`.
- The registered `runtime_install` defaults `dry_run=False` (act-by-default); `dry_run=true` previews.
- `runtime_install_payload` takes the `RuntimeInstallRequest` the registration built and does not
  interpret its flags; the builder stays transport-thin.
- `server_info_payload` requires an explicit `ServingBuildPayload`; package version alone cannot identify
  equal-version source or installed candidates.

### Role Runtime and Scope

server_info_payload adds toolServer and AgentBindingPayload only for readable bound identity; servingBuild remains the process/build owner fact. context_packet_payload derives optional call-local admitted config before invoking the existing context packet owner. No binding creates a second globally selected repository root.

## Runtime installation owner

Core tool adapters import runtime installation from `application.runtime.install`; payload
validation and forwarding stay transport-thin.

## Evidence



### Runtime Source References

- `server_info_payload` reports the server identity, roots, unused keys, serving build, build currentness, running servers and any agent binding. [1]

- Frozen implementation of context_packet_payload supporting the stated file behavior. [2]

## Server info names no harness skill root

`server_info_payload` reports no harness skill root: no skill folder is resolved or installed, so there is no root to name, and `ServerInfoResponse` declares no such field. It reports the roots, allowed repo ids and unused provider/settings keys.

- The server-info answer carries no harness skill root. [8]

- `server_info` reports the process's build currentness, inspecting a checkout build too. [9]
- `server_info` lists the running-server registry's live records. [10]
